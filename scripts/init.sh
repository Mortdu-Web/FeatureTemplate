#!/usr/bin/env bash
# Usage : ./scripts/init.sh <slug> <port> "<Titre>"
# Ex.   : ./scripts/init.sh hub-app 25001 "Hub App"
set -euo pipefail
[ $# -eq 3 ] || { echo "Usage: $0 <slug> <port> \"<Titre>\""; exit 1; }
SLUG=$1; PORT=$2; TITLE=$3
[[ $SLUG =~ ^[a-z0-9-]+$ ]] || { echo "Slug invalide (a-z, 0-9, -)"; exit 1; }
[[ $PORT =~ ^[0-9]+$ ]]     || { echo "Port invalide"; exit 1; }

cd "$(dirname "$0")/.."
grep -rlE '__(SLUG|PORT|TITLE)__' . --exclude-dir=.git --exclude=init.sh | while read -r f; do
  sed -i -e "s/__SLUG__/$SLUG/g" -e "s/__PORT__/$PORT/g" -e "s|__TITLE__|$TITLE|g" "$f"
done
[ -f .env ] || cp .env.example .env
echo "OK : $SLUG initialisé (port $PORT). Adapte .env puis : make up"
