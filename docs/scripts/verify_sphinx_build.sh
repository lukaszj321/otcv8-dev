#!/bin/bash
# Verify Sphinx build completes without critical errors
# Usage: ./docs/scripts/verify_sphinx_build.sh

set -e

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="${DOCS_DIR}/../build/html"

echo "=== Sphinx Build Verification ==="
echo "Docs dir: $DOCS_DIR"
echo "Build dir: $BUILD_DIR"
echo ""

# Run Sphinx build and capture output
echo "Running Sphinx build..."
if python3 -m sphinx -b html "$DOCS_DIR" "$BUILD_DIR" 2>&1 | tee /tmp/sphinx_build.log; then
    BUILD_EXIT=$?
else
    BUILD_EXIT=$?
fi

echo ""
echo "=== Build Summary ==="

# Count errors and warnings
ERRORS=$(grep -c "ERROR" /tmp/sphinx_build.log || true)
CRITICALS=$(grep -c "CRITICAL" /tmp/sphinx_build.log || true)
WARNINGS=$(grep -c "WARNING" /tmp/sphinx_build.log || true)

echo "Critical errors: $CRITICALS"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

# Check for specific known issues
TAB_ERRORS=$(grep -c "not enough values to unpack\|ValueError.*tab" /tmp/sphinx_build.log || true)
if [ "$TAB_ERRORS" -gt 0 ]; then
    echo "⚠️  Found $TAB_ERRORS tab-related errors"
    grep "not enough values to unpack\|ValueError.*tab" /tmp/sphinx_build.log | head -5
fi

CSV_ERRORS=$(grep -c "Insufficient data supplied.*csv-table" /tmp/sphinx_build.log || true)
if [ "$CSV_ERRORS" -gt 0 ]; then
    echo "⚠️  Found $CSV_ERRORS csv-table errors (may be non-critical)"
fi

TRANSITION_ERRORS=$(grep -c "may not begin with a transition\|may not end with a transition" /tmp/sphinx_build.log || true)
if [ "$TRANSITION_ERRORS" -gt 0 ]; then
    echo "⚠️  Found $TRANSITION_ERRORS transition errors"
    grep "may not begin with a transition\|may not end with a transition" /tmp/sphinx_build.log | head -5
fi

echo ""

# Exit with error if there are critical issues
if [ "$CRITICALS" -gt 0 ]; then
    echo "❌ Build failed with CRITICAL errors"
    exit 1
elif [ "$BUILD_EXIT" -ne 0 ]; then
    echo "❌ Build failed with exit code $BUILD_EXIT"
    exit 1
else
    echo "✅ Build completed (warnings: $WARNINGS, errors: $ERRORS)"
    if [ "$ERRORS" -eq 0 ]; then
        exit 0
    else
        echo "ℹ️  Build succeeded but has $ERRORS non-critical errors"
        exit 0
    fi
fi
