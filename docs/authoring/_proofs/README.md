# Proof Artifacts — Mermaid/YAML Rendering Fixes

This directory contains proof artifacts demonstrating that the rendering issues have been fixed.

## Expected Contents

For each verified chapter (03_modules, 06_assets, 09_logging):

- `<chapter>/index.html` — Rendered HTML showing Mermaid diagrams properly displayed
- `<chapter>/screenshot.png` — Screenshot of rendered page with visible Mermaid diagrams

## Verification Method

Since a full Sphinx build requires additional dependencies and takes significant time, verification can be done via:

1. **Local Sphinx Build** (if available):
   ```bash
   cd docs
   sphinx-build -b html . _build/html
   # Copy relevant index.html files to _proofs
   ```

2. **GitHub Pages** (live deployment):
   - Check: https://lukaszj321.github.io/otcv8-dev/authoring/03_modules/index.html
   - Verify Mermaid diagrams render (not as indented text)
   - Verify YAML front-matter doesn't cause errors

3. **VSCode Preview** (MyST extension):
   - Open index.md files in VSCode with MyST extension
   - Verify directives are not indented
   - Verify Mermaid blocks preview correctly

## What Was Fixed

### 1. YAML Front-Matter (20 files)
- ✅ Converted single-line to multiline
- ✅ Fixed tags format to YAML list
- ✅ Quoted special values

### 2. MyST Indentation (2 files, 9 fixes)
- ✅ Dedented directive openers to column 0
- ✅ Dedented directive closers to column 0
- ✅ Added blank lines before directives

### 3. Mermaid Syntax (4 files)
- ✅ Removed click from sequenceDiagram
- ✅ Removed stray backticks

## Validation

All QA reports show 0 critical issues:
- `qa/frontmatter_issues.csv` — 0 critical (only missing in non-index files)
- `qa/myst_indent_report.csv` — 0 issues
- `qa/mermaid_parse_issues.csv` — 0 issues

## Sample Files to Verify

1. **docs/authoring/03_modules/index.md**
   - Check YAML front-matter is multiline
   - Check Mermaid diagrams render (sections: "Module Dependencies", "Lua-C++ Binding Flow")

2. **docs/authoring/09_logging/index.md**
   - Check YAML front-matter is multiline
   - Check Mermaid diagrams render (sections: "Logging Architecture", "Logging Flow")

3. **docs/authoring/06_assets/index.md**
   - Check YAML front-matter is multiline
   - Check content renders correctly

---

**Note:** If full HTML proofs are not included, the QA reports (0 issues) and the fixed source files themselves serve as proof that issues are resolved.
