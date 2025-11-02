#!/bin/bash
# Script to populate source_mirror directory for Sphinx documentation
# Reference commit: 84add321aea1031e8700b9a4db4b5025ef0b1396
# This script copies source files from src/ to the location expected by RST files

set -e  # Exit on error

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="${REPO_ROOT}/src"
MIRROR_DIR="${REPO_ROOT}/docs/copilot/sphinx/code/src/source_mirror/src"

echo "=== Populating source_mirror for Sphinx documentation ==="
echo "Source: ${SRC_DIR}"
echo "Target: ${MIRROR_DIR}"

# Check if source directory exists
if [ ! -d "${SRC_DIR}" ]; then
    echo "ERROR: Source directory not found: ${SRC_DIR}"
    exit 1
fi

# Create target directory if it doesn't exist
mkdir -p "${MIRROR_DIR}"

# Copy source files to mirror location
echo "Copying files..."
cp -r "${SRC_DIR}/"* "${MIRROR_DIR}/"

# Verify copy was successful
if [ $? -eq 0 ]; then
    echo "✓ Successfully copied source files to source_mirror"
    echo "✓ Files available at: ${MIRROR_DIR}"
    
    # Show some statistics
    FILE_COUNT=$(find "${MIRROR_DIR}" -type f | wc -l)
    echo "✓ Total files copied: ${FILE_COUNT}"
else
    echo "ERROR: Failed to copy source files"
    exit 1
fi

exit 0
