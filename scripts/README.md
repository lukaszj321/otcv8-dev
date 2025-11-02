# Scripts Directory

This directory contains utility scripts for maintaining the OTClient v8 documentation and codebase.

## fix_myst_tabs.py

A Python script that automatically fixes malformed MyST/sphinx-design tab directives across the repository.

### Purpose

The Sphinx documentation build can fail due to common formatting issues with MyST tab directives:
- Missing blank lines after `{tab}` headers
- Empty tab bodies that need placeholder content
- Improperly nested code fences inside tabs
- Inconsistent backtick usage (````{tabs}` vs ```{tabs}`)

This script automatically detects and fixes these issues.

### Usage

**Dry run (recommended first):**
```bash
python scripts/fix_myst_tabs.py --dry-run --verbose
```

**Apply fixes:**
```bash
python scripts/fix_myst_tabs.py
```

**Options:**
- `--dry-run`: Preview changes without modifying files
- `--verbose` or `-v`: Show detailed information about each fix
- `--help`: Show help message

### What It Fixes

1. **Missing blank lines**: Adds blank lines after `{tab}` directive headers
   ```markdown
   # Before
   ```{tab} Label
   Content here
   
   # After
   ```{tab} Label
   
   Content here
   ```

2. **Empty tabs**: Adds placeholder content to empty tab bodies
   ```markdown
   # Before
   ```{tab} Empty
   ```
   
   # After
   ```{tab} Empty
   
   TODO: add content
   ```

3. **Nested code blocks**: Converts raw code fences to MyST code-block directives when inside tabs
   ```markdown
   # Before
   ```{tab} Code
   ```python
   code here
   ```
   
   # After
   ```{tab} Code
   
   ```{code-block} python
   code here
   ```
   ```

4. **Backtick normalization**: Standardizes `{tabs}` to use three backticks
   ```markdown
   # Before
   ````{tabs}
   
   # After
   ```{tabs}
   ```

### Safety Features

- **Backups**: Creates `.bak` files before modifying originals
- **UTF-8 encoding**: Preserves proper text encoding
- **Idempotent**: Safe to run multiple times
- **Error handling**: Reports issues without crashing

### Integration with CI

The script is integrated into the GitHub Actions workflow (`.github/workflows/sphinx-pages.yml`) and runs automatically before building documentation. This ensures tab formatting issues are caught and fixed before the build.

## Local Documentation Build

To build the documentation locally and verify your changes:

### Prerequisites

```bash
# Install Python dependencies
pip install -r docs/requirements.txt
```

### Build Steps

1. **Run the tab fixer** (if you've made changes to markdown files):
   ```bash
   python scripts/fix_myst_tabs.py
   ```

2. **Generate authoring pages** (if needed):
   ```bash
   python scripts/build_authoring_pages.py
   ```

3. **Patch Mermaid diagrams** (if needed):
   ```bash
   python scripts/patch_diagrams_clicks.py
   ```

4. **Generate placeholder files**:
   ```bash
   python docs/scripts/generate_placeholders.py
   ```

5. **Build the documentation**:
   ```bash
   # Standard build
   sphinx-build -b html docs docs/_build/html
   
   # Build with warnings as errors (recommended)
   sphinx-build -E -W -b html docs docs/_build/html
   ```

6. **View the documentation**:
   ```bash
   # Serve locally
   python -m http.server 8000 --directory docs/_build/html
   
   # Open in browser: http://localhost:8000
   ```

### Troubleshooting

**Issue: Tab directive errors**
```
Solution: Run python scripts/fix_myst_tabs.py
```

**Issue: Missing dependencies**
```
Solution: pip install -r docs/requirements.txt
```

**Issue: Encoding errors**
```
Solution: Ensure files are UTF-8 encoded
```

**Issue: Mermaid diagram rendering fails**
```
Solution: Check that diagrams have proper %%{init} headers
```

## Other Scripts

- `build_authoring_pages.py` - Generates authoring documentation pages
- `patch_diagrams_clicks.py` - Adds facet links to Mermaid diagrams
- Various utility scripts for documentation enhancement and maintenance

For more information about each script, check the docstrings in the script files themselves.
