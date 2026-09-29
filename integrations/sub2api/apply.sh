#!/usr/bin/env bash
set -euo pipefail
target=${1:?Usage: apply.sh /path/to/excel-codex-bridge}
here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
base=$(cat "$here/BASE_COMMIT")
if [ "$(git -C "$target" rev-parse HEAD)" != "$base" ]; then
  echo 'Expected the revision recorded in BASE_COMMIT' >&2
  exit 1
fi
git -C "$target" diff --quiet
git -C "$target" diff --cached --quiet
git -C "$target" apply --check "$here/excel-codex-bridge.patch"
git -C "$target" apply "$here/excel-codex-bridge.patch"
echo 'Applied Sub2API Excel account-pool integration'
