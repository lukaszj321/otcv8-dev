#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
OUT_DIR=".doxygen"
XML_DIR="$OUT_DIR/xml"

# 1) Zbierz istniejące wejścia (bez crasha gdy 'include/' nie ma)
INPUTS=()
[[ -d src ]] && INPUTS+=("src")
[[ -d include ]] && INPUTS+=("include")

if [ ${#INPUTS[@]} -eq 0 ]; then
  echo "::warning ::No input directories (expected src/ and/or include/). Skipping C++ API generation."
  exit 0
fi

# 2) Doxyfile (CI)
cat > Doxyfile.ci <<EOF
PROJECT_NAME           = OTCv8 CI
OUTPUT_DIRECTORY       = $OUT_DIR
GENERATE_XML           = YES
XML_OUTPUT             = xml
GENERATE_HTML          = NO
QUIET                  = YES
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_STATIC         = YES
RECURSIVE              = YES
JAVADOC_AUTOBRIEF      = YES
FILE_PATTERNS          = *.h *.hpp *.hh *.hxx *.c *.cc *.cpp
INPUT                  = ${INPUTS[*]}
WARN_IF_UNDOCUMENTED   = NO
WARNINGS               = YES
WARN_LOGFILE           = $OUT_DIR/doxygen-warnings.log
EOF

# 3) Uruchom doxygen
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"
echo "==> Doxygen (C++)"
doxygen Doxyfile.ci || { echo "::error ::Doxygen failed"; cat "$OUT_DIR/doxygen-warnings.log" || true; exit 2; }

# 4) Wymagany artefakt: .doxygen/xml/index.xml
if [[ ! -s "$XML_DIR/index.xml" ]]; then
  echo "::error ::Missing $XML_DIR/index.xml after Doxygen"
  echo "== Listing $XML_DIR =="
  ls -la "$XML_DIR" | head -n 200 || true
  echo "== Doxygen warnings =="
  sed -n '1,200p' "$OUT_DIR/doxygen-warnings.log" || true
  exit 2
fi

# 5) Opcjonalna konwersja XML -> Markdown (tylko jeśli masz konwerter)
echo "==> XML -> Markdown"
if [[ -f scripts/doxygen-xml2md.mjs ]]; then
  node scripts/doxygen-xml2md.mjs "$XML_DIR" "docs/api/external/cpp" \
    || echo "::warning ::xml->md converter failed, skipping"
else
  echo "::notice ::No scripts/doxygen-xml2md.mjs found; skipping conversion"
fi

echo "OK"
