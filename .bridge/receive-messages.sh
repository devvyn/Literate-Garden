#!/usr/bin/env bash
# Bridge message receiver for Literate-Garden project
# Checks for messages relevant to this project

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LITERATE_GARDEN_ROOT="$(dirname "$SCRIPT_DIR")"
META_PROJECT_ROOT="${HOME}/devvyn-meta-project"

# Check if meta-project bridge is available
if [[ ! -d "$META_PROJECT_ROOT/bridge" ]]; then
    echo "❌ Meta-project bridge not found at: $META_PROJECT_ROOT"
    exit 1
fi

# Forward to meta-project bridge-receive.sh
cd "$META_PROJECT_ROOT"
exec ./scripts/bridge-receive.sh code