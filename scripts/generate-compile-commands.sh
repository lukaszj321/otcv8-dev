#!/usr/bin/env bash
# Generate compile_commands.json using CMake (CMake project root assumed)
# Usage: ./scripts/generate-compile-commands.sh [build-dir]
set -euo pipefail
BUILD_DIR=${1:-build}
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Repo root: $ROOT_DIR"
mkdir -p "$ROOT_DIR/$BUILD_DIR"
cd "$ROOT_DIR/$BUILD_DIR"
# Generate compile_commands.json (configure only)
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || { echo "ERROR: CMake configuration failed"; exit 1; }
# If compile_commands.json is in build, copy (or symlink) to repo root for helpers that expect it
if [ -f compile_commands.json ]; then
  cp -f compile_commands.json "$ROOT_DIR/compile_commands.json"
  echo "compile_commands.json generated at $ROOT_DIR/compile_commands.json"
else
  echo "ERROR: compile_commands.json not found in $BUILD_DIR"
  echo "Troubleshooting:"
  echo "  - Check that CMakeLists.txt exists in the project root."
  echo "  - Ensure that the CMake configuration step succeeded (see output above)."
  echo "  - Make sure you are using CMake 3.5+ (required for CMAKE_EXPORT_COMPILE_COMMANDS)."
  echo "Troubleshooting:"
  echo "  - Check that CMakeLists.txt exists in the project root."
  echo "  - Ensure that the CMake configuration step succeeded (see output above)."
  echo "  - Make sure you are using CMake 3.5+ (required for CMAKE_EXPORT_COMPILE_COMMANDS)."
  exit 2
fi
