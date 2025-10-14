# Authoring Scripts

Scripts for generating and maintaining the authoring documentation pipeline.

## build_authoring_pages.py

**Purpose:** Generate index.md files for all authoring chapters (01-10) with complete structure.

**Features:**
- Discovers all chapters matching pattern `0[1-9]_*` or `1[0-2]_*`
- Generates chapter index.md with:
  - Datasets section (CSV tables with facet links)
  - Diagrams section (Mermaid with init and clickable nodes)
  - Podkatalogi section (toctree for subdirectories)
  - Crosslinks section (from source metadata)
  - Appendix/Facets section (facet anchors with types)
- Generates main authoring/index.md with grid cards and toctree
- Ensures subdirectory index.md files exist

**Usage:**
```bash
python3 scripts/build_authoring_pages.py
```

**Output:**
- `docs/authoring/*/index.md` - Chapter landing pages
- `docs/authoring/index.md` - Main authoring index
- `docs/authoring/*/subdirectory/index.md` - Subdirectory indexes (if needed)

## verify_authoring_completeness.py

**Purpose:** Verify that all chapters meet the authoring requirements.

**Checks:**
- Required sections present (Datasets, Diagrams, Appendix/Facets)
- CSV tables have facet links
- Mermaid diagrams have init blocks
- Clickable nodes in diagrams
- Facet anchors properly formatted
- Optional sections (Podkatalogi, Crosslinks) where applicable

**Usage:**
```bash
python3 scripts/verify_authoring_completeness.py
```

**Exit codes:**
- 0: All checks passed
- 1: One or more errors found

## Related Scripts

### generate_authoring_pipeline.py
Generates cross-reference data (xref.csv, xref.json) from source metadata.

### analytics_generator.py
Generates analytics reports (coverage, statistics, chapter breakdown).

## Workflow Integration

These scripts are designed to run in GitHub Actions without modifying workflows:

1. **build_authoring_pages.py** - Run before Sphinx build
2. **verify_authoring_completeness.py** - Run as validation step
3. Sphinx build with myst_nb and PyData theme

## Requirements

- Python 3.8+
- No external dependencies beyond standard library
- Source files in `docs/authoring/_sources/`
- Chapter directories in `docs/authoring/0*_*/`

## Configuration

Environment:
- **Sphinx:** 7.4.7
- **PyData Theme:** 0.16.1
- **MyST-NB:** 1.3.0+
- **Language:** PL (Polish)

## Maintenance

When adding new chapters:
1. Create source file in `docs/authoring/_sources/`
2. Create chapter directory `docs/authoring/NN_name/`
3. Add datasets/*.csv and diagrams/*.mmd
4. Run `build_authoring_pages.py`
5. Verify with `verify_authoring_completeness.py`
