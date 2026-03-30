#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC="$ROOT/openapi/openapi.yaml"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/openapi-python-client-config.XXXXXX.yaml")"

cleanup() {
  rm -f "$TMP_CONFIG"
}
trap cleanup EXIT

if [[ ! -f "$SPEC" ]]; then
  echo "error: missing spec at $SPEC" >&2
  exit 1
fi

if ! command -v openapi-python-client >/dev/null 2>&1; then
  echo "error: openapi-python-client not found in PATH" >&2
  echo "hint: enter the devshell first (direnv allow / cd into repo)" >&2
  exit 1
fi

cat > "$TMP_CONFIG" <<'YAML'
post_hooks: []
package_name_override: quipu_client
project_name_override: quipu-client
YAML

rm -rf "$ROOT/python/generated"
openapi-python-client generate \
  --path "$SPEC" \
  --meta none \
  --config "$TMP_CONFIG" \
  --output-path "$ROOT/python/generated" \
  --overwrite

rm -rf "$ROOT/python/quipu_client"
mv "$ROOT/python/generated" "$ROOT/python/quipu_client"

echo "Regenerated python/quipu_client from openapi/openapi.yaml"
