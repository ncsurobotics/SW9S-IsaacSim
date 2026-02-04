#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
ISAAC_ROOT="${ISAAC_ROOT:-/home/sidgupta4761/isaac/isaac-sim-standalone-5.0.0-linux-x86_64}"
PYTHON_SH="${ISAAC_ROOT}/python.sh"

if [[ ! -x "${PYTHON_SH}" ]]; then
  echo "python.sh not found or not executable: ${PYTHON_SH}" >&2
  echo "Set ISAAC_ROOT to your Isaac Sim root." >&2
  exit 1
fi

# Ensure OceanSim repo is importable
export PYTHONPATH="${REPO_ROOT}:${PYTHONPATH:-}"

# Pass all args through
exec "${PYTHON_SH}" -m standalone.zed_uw_example.main "$@"
