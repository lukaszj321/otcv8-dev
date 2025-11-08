#!/usr/bin/env bash
# Generate compile_commands.json using CMake (CMake project root assumed)
# Usage: ./scripts/generate-compile-commands.sh [build-dir]
set -euo pipefail

BUILD_DIR=${1:-build}
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Repo root: $ROOT_DIR"

# Basic sanity checks
if [ ! -f "$ROOT_DIR/CMakeLists.txt" ]; then
  echo "WARNING: CMakeLists.txt not found in repo root ($ROOT_DIR)."
  echo "If your project root is elsewhere, run this script from the project root or pass correct paths."
fi

mkdir -p "$ROOT_DIR/$BUILD_DIR"
cd "$ROOT_DIR/$BUILD_DIR"

# Use cmake -S/-B to be explicit about source dir (more robust)
if ! cmake -S "$ROOT_DIR" -B . -DCMAKE_EXPORT_COMPILE_COMMANDS=ON; then
  echo "ERROR: CMake configuration failed"
  exit 1
fi

# If compile_commands.json is generated in the build directory, copy it to repo root
if [ -f compile_commands.json ]; then
  cp -f compile_commands.json "$ROOT_DIR/compile_commands.json"
  echo "compile_commands.json generated at $ROOT_DIR/compile_commands.json"
else
  echo "ERROR: compile_commands.json not found in $BUILD_DIR"
  echo "Troubleshooting:"
  echo "  - Ensure CMake configuration succeeded (see output above)."
  echo "  - Try running: cmake -S \"$ROOT_DIR\" -B \"$ROOT_DIR/$BUILD_DIR\" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
  echo "  - Make sure you are using CMake 3.5+ (required for CMAKE_EXPORT_COMPILE_COMMANDS)."
  exit 2
fi
