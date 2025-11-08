#!/usr/bin/env bash
# Bootstrap system dependencies for extraction on Ubuntu/Debian.
# Usage: sudo ./scripts/bootstrap-ubuntu.sh
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
  echo "Please run as root (sudo)."
  exit 1
fi

echo "Adding Node.js 18 repository..."
# Ensure basic tools are present before adding the repo
apt-get update
apt-get install -y --no-install-recommends curl ca-certificates || {
  echo "Failed to install curl/ca-certificates"
  exit 1
}

# Retry helper for network commands
try_cmd() {
  local n=0 max=3 delay=3 cmd
  cmd="$*"
  until [ $n -ge $max ]; do
    if eval "$cmd"; then
      return 0
    fi
    n=$((n+1))
    echo "Command failed, retry $n/$max after ${delay}s..."
    sleep $delay
  done
  return 1
}

try_cmd curl -fsSL https://deb.nodesource.com/setup_18.x | bash - || {
  echo "Failed to add NodeSource repo"
  exit 1
}

echo "Installing all system dependencies..."
export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  cmake \
  git \
  jq \
  python3 \
  python3-venv \
  python3-pip \
  nodejs \
  npm \
  clang \
  libclang-dev \
  llvm \
  pkg-config \
  ca-certificates \
  curl || {
    echo "apt-get install failed"
    exit 1
}

# Optional: cleanup apt cache
echo "Cleaning up apt cache..."
apt-get clean
rm -rf /var/lib/apt/lists/*

echo ""
echo "Bootstrap finished successfully!"
echo "Installed tool versions:"
command -v node >/dev/null 2>&1 && node --version || echo "node: not found"
command -v npm >/dev/null 2>&1 && npm --version || echo "npm: not found"
command -v python3 >/dev/null 2>&1 && python3 --version || echo "python3: not found"
command -v cmake >/dev/null 2>&1 && cmake --version | head -n1 || echo "cmake: not found"
command -v clang >/dev/null 2>&1 && clang --version | head -n1 || echo "clang: not found"

echo ""
echo "Recommended next steps for a developer:"
echo "  1. Create a Python virtual environment: python3 -m venv .venv-extract"
echo "  2. Activate it: source .venv-extract/bin/activate"
echo "  3. Install Python packages: pip install -r requirements.txt"
echo "  4. Make scripts executable: chmod +x scripts/*.sh"
echo "  5. Run a quick smoke test: ./scripts/run-extract-full.sh --no-venv --skip-libclang"
