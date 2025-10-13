# build_authoring.py

## Purpose

This script prepares the `docs/reposzablony/**` directory structure for Sphinx documentation by:

1. **Creating index.md files** where missing
2. **Adding toctree directives** with natural-sorted children
3. **Rendering CSV files inline** using `{csv-table}` directives
4. **Rendering Mermaid diagrams inline** by embedding `.mmd` file content
5. **Updating authoring/index.md** to link internally to reposzablony

## Usage

The script is automatically run in the CI workflow before Sphinx builds:

```bash
python scripts/build_authoring.py
```

You can also run it locally:

```bash
cd /path/to/otcv8-dev
python scripts/build_authoring.py
```

## What It Does

### 1. Recursive Directory Processing

The script walks through all directories in `docs/reposzablony/**` and:

- Skips directories starting with `.` or `_` (e.g., `_build`, `.git`)
- Processes each directory to ensure it has an `index.md` file

### 2. Index.md Generation

For each directory:

- If `index.md` exists, it's updated in-place
- If missing, a new `index.md` is created with a title derived from the directory name
- Existing content is preserved (the script only appends new sections)

### 3. Toctree Generation

Each `index.md` gets a `{toctree}` directive that includes:

- **Subdirectories**: Listed as `subdir/index`
- **Sibling .md files**: Listed without the `.md` extension (excluding `index.md` itself)
- **Natural sorting**: Handles prefixes like `01_`, `02_` correctly

Example:
```markdown
```{toctree}
:maxdepth: 2
:titlesonly:

01_core/index
02_events/index
readme
```
```

### 4. CSV Table Rendering

If a directory contains:
- A `datasets/` subdirectory with `.csv` files, OR
- IS a `datasets/` directory itself

The script adds inline CSV tables:

```markdown
## Datasets

```{csv-table} Summary
:file: datasets/summary.csv
:header-rows: 1
:widths: auto
```
```

### 5. Mermaid Diagram Rendering

If a directory contains:
- A `diagrams/` subdirectory with `.mmd` files, OR
- IS a `diagrams/` directory itself

The script embeds the Mermaid diagram content:

```markdown
## Diagrams

```{mermaid}
:caption: Flow Diagram

graph TD
    A[Start] --> B[End]
```
```

### 6. Stub Replacement

The script replaces stub text patterns like:

```markdown
Location: datasets/summary.csv
```

With actual inline MyST blocks (CSV tables or Mermaid diagrams).

## Output

The script prints:
- List of updated files
- Success message

Example output:
```
Processing /path/to/docs/reposzablony...
Updated: docs/reposzablony/01_core/index.md
Updated: docs/reposzablony/01_core/api/cpp/index.md
...
Updating authoring/index.md...
Updated: docs/authoring/index.md

✓ Build authoring completed successfully
```

## Integration

The script is integrated into the CI workflow at `.github/workflows/sphinx-pages.yml`:

```yaml
- name: Run pre-build script
  run: |
    python scripts/build_authoring.py

- name: Build Sphinx
  run: |
    sphinx-build -b html docs docs/_build/html
```

## Idempotency

The script is idempotent:
- Running it multiple times with no changes produces no file updates
- Only updates files when content actually changes
- Safe to run before every build

## Requirements

- Python 3.7+
- Standard library only (no external dependencies)
- Run from repository root directory

## File Structure

The script expects this structure:

```
docs/
├── authoring/
│   └── index.md           # Updated to link to ../reposzablony/
├── reposzablony/
│   ├── 01_core/
│   │   ├── index.md       # Generated/updated
│   │   ├── datasets/
│   │   │   ├── summary.csv
│   │   │   └── entities.csv
│   │   └── diagrams/
│   │       ├── flow.mmd
│   │       └── architecture.mmd
│   └── ...
└── ...
```

## Troubleshooting

### Script doesn't find CSV/Mermaid files

- Ensure files are in `datasets/*.csv` or `diagrams/*.mmd`
- Check that directories aren't hidden (starting with `.` or `_`)

### Toctree not generated

- Verify subdirectories contain at least one `.md` file or subdirectory
- Check that `index.md` exists or will be created

### Changes not reflected

- The script only updates files if content differs
- Check that the file wasn't manually modified after the script ran
- Run with fresh checkout to regenerate all files

## Maintenance

When adding new chapters to `docs/reposzablony/`:

1. Create the directory structure
2. Add CSV files to `datasets/` subdirectory
3. Add Mermaid diagrams to `diagrams/` subdirectory
4. Run the script to generate `index.md` files
5. Optionally customize the generated `index.md` content

The script will preserve your customizations while updating navigation and inline content.
