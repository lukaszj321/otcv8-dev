#!/usr/bin/env bash
set -euo pipefail

# Ścieżki
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT/src"
BUILD_DIR="$ROOT/.doxygen"
XML_DIR="$BUILD_DIR/xml"
OUT_MD="$ROOT/docs/api/external/otcv8-full-api.md"

mkdir -p "$BUILD_DIR" "$(dirname "$OUT_MD")"

# Minimalny Doxyfile generowany w locie
cat > "$BUILD_DIR/Doxyfile" <<'EOF'
PROJECT_NAME           = "otcv8 C++ API"
INPUT                  = src
FILE_PATTERNS          = *.h *.hpp *.hh *.hxx
RECURSIVE              = YES
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = NO
EXTRACT_STATIC         = YES
EXTRACT_LOCAL_METHODS  = YES
EXTRACT_LOCAL_CLASSES  = YES
JAVADOC_AUTOBRIEF      = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = NO
QUIET                  = YES
GENERATE_HTML          = NO
GENERATE_XML           = YES
XML_OUTPUT             = xml
# Jeżeli są makra osłaniające mobilne/silnikowe rzeczy, można tu je dodać:
# PREDEFINED            = OTCLIENT_MOBILE=1
EOF

echo "==> Doxygen (C++)"
( cd "$ROOT" && doxygen "$BUILD_DIR/Doxyfile" )

echo "==> XML -> Markdown"
python3 "$ROOT/scripts/doxy_to_md.py" "$XML_DIR" > "$OUT_MD"

echo "Wygenerowano: $OUT_MD"
