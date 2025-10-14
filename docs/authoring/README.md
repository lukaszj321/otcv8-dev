# Authoring Pipeline Documentation

## Overview

This directory contains the **Authoring-first** documentation pipeline for OTClient v8, with complete artifacts for chapters 01-10. All datasets, diagrams, and MyST pages are generated from source metadata.

## Directory Structure

```
docs/authoring/
├── _sources/           # Source markdown files with frontmatter metadata
│   └── chapter_*.md    # 10 chapter source files
├── _instructions/      # Domain-specific instructions for agents
│   ├── 01-cpp-api.instructions.md
│   ├── 02-ui-lua.instructions.md
│   └── ...
├── _data/              # Cross-reference and metadata
│   ├── xref.csv        # Cross-reference edges (27 total)
│   └── xref.json       # JSON format of xrefs
├── analytics/          # Pipeline statistics and reports
│   ├── summary.md      # Analytics summary
│   └── chapter_stats.csv
├── qa/                 # Quality assurance reports
│   ├── summary.md      # QA summary
│   └── *.csv          # Detailed issue reports
├── 01_core/           # Chapter directories (01-10)
│   ├── datasets/      # CSV datasets
│   ├── diagrams/      # Mermaid diagrams (.mmd)
│   └── index.md       # Chapter landing page (MyST)
├── 02_events/
├── ... (03-10)
└── index.md           # Main authoring index
```

## Chapters

| Chapter | Title | Datasets | Diagrams | XRefs |
|---------|-------|----------|----------|-------|
| 01_core | Core C++ API | 6 | 2 | 4 |
| 02_events | Event System | 4 | 2 | 3 |
| 03_modules | Lua Modules | 3 | 1 | 2 |
| 04_ui | UI Widgets | 4 | 2 | 2 |
| 05_network | Network Protocol | 4 | 1 | 2 |
| 06_assets | Assets Pipeline | 4 | 1 | 2 |
| 07_settings_crypto | Settings & Crypto | 4 | 1 | 2 |
| 08_audio | Audio System | 4 | 1 | 2 |
| 09_logging | Logging System | 4 | 1 | 2 |
| 10_game_runtime | Game Runtime | 4 | 1 | 2 |

**Total:** 40 datasets, 13 diagrams, 27 cross-references

## Pipeline Scripts

### 1. `scripts/generate_authoring_pipeline.py`

Main pipeline generator that processes all chapters from `_sources/` and generates:
- CSV datasets from frontmatter metadata
- Mermaid diagram stubs
- MyST chapter pages with embedded content
- Cross-reference data (CSV + JSON)
- Analytics reports

**Usage:**
```bash
python scripts/generate_authoring_pipeline.py
```

**Features:**
- ✅ UTF-8 encoding with LF line endings
- ✅ Automatic CSV header generation from frontmatter
- ✅ Mermaid init blocks for dark/light theme
- ✅ Facet anchors for cross-references
- ✅ Sample CSVs for files >2MB
- ✅ Analytics and coverage metrics

### 2. `scripts/qa_authoring_checker.py`

Quality assurance checker that validates:
- CSV headers match frontmatter specifications
- Mermaid diagrams have proper init blocks
- Facet anchors are present in index.md
- Index.md structure (sections, frontmatter)
- Cross-reference evidence files exist

**Usage:**
```bash
python scripts/qa_authoring_checker.py
```

**Output:** Reports in `docs/authoring/qa/`

### 3. `scripts/fix_mermaid_init.py`

Utility to add proper init blocks to existing Mermaid diagrams.

**Usage:**
```bash
python scripts/fix_mermaid_init.py
```

### 4. `scripts/build_authoring_pages.py`

Legacy script (kept for compatibility) that generates basic index pages.

## Frontmatter Schema

Each chapter source file in `_sources/` uses YAML frontmatter:

```yaml
---
chapter: "01_core"
slug: "01_core"
title: "Core C++ API"
status: "agent_ready"
artifacts:
  datasets:
    - id: "summary"
      file: "summary.csv"
      headers: ["metric", "value", "note"]
      facet: "01_core.summary"
  diagrams:
    - id: "architecture"
      file: "architecture.mmd"
      facet: "01_core.architecture"
xrefs:
  - to: "03_modules.lua_exports"
    type: "uses"
    evidence: "docs/authoring/03_modules/datasets/lua_exports.csv"
tags: ["cpp", "api", "core"]
---
```

## Facet System

**Facets** are stable identifiers for cross-referencing between chapters:

- Format: `<chapter>.<item>` (e.g., `01_core.summary`)
- Each dataset and diagram has a facet ID
- Facets are anchored in index.md: `(facet-01_core.summary)=`
- Used in xrefs to link related content

## MyST Syntax

Chapter pages use MyST (Markedly Structured Text) extensions:

### CSV Tables
```markdown
### summary
*Facet:* [`01_core.summary`](#facet-01_core.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```
```

### Mermaid Diagrams
```markdown
### architecture
*Facet:* [`01_core.architecture`](#facet-01_core.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
    A[Core] --> B[Framework]
```
```

### Grid Layouts
```markdown
:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Chapter Title
:link: chapter/index
:link-type: doc
:shadow: md
Description text.
:::

:::
```

## Cross-References

Cross-references track relationships between chapters:

```csv
from_chapter,from_facet,to_chapter,to_facet,type,evidence_path,note
01_core,01_core,03_modules,03_modules.lua_exports,uses,docs/authoring/03_modules/datasets/lua_exports.csv,
```

**Relationship Types:**
- `uses` - Chapter uses functionality from another
- `emits` - Emits events/signals
- `handles` / `handled_by` - Handles events
- `renders` - Renders UI components
- `logs` - Writes to logging system

## Analytics

The `analytics/` directory contains:

- **summary.md** - Overall pipeline statistics
- **chapter_stats.csv** - Per-chapter breakdown
- Coverage metrics (datasets, diagrams, xrefs)

View at: [analytics/summary.md](analytics/summary.md)

## QA Checks

The `qa/` directory contains validation reports:

- **summary.md** - QA status overview
- **csv_headers.csv** - Header validation issues
- **mermaid_init.csv** - Diagram init block issues
- **facet_anchors.csv** - Missing anchor issues
- **index_structure.csv** - Structure validation
- **xref_evidence.csv** - Missing evidence files

## Sphinx Configuration

The pipeline works with:
- **Sphinx:** 7.4.7
- **PyData Theme:** 0.16.1
- **MyST-NB:** (for MyST syntax)
- **sphinxcontrib.mermaid:** (for diagrams)
- **sphinx_design:** (for grids/cards)

See `docs/conf.py` for full configuration.

## Workflow Integration

The pipeline is designed to run in GitHub Actions without workflow changes:

```yaml
- name: Generate authoring artifacts
  run: python scripts/generate_authoring_pipeline.py

- name: Run QA checks
  run: python scripts/qa_authoring_checker.py

- name: Build Sphinx
  run: sphinx-build -b html docs docs/_build/html
```

## Best Practices

### 1. Updating Chapters

To update a chapter:
1. Edit source file in `_sources/chapter_*.md`
2. Update frontmatter metadata (datasets, diagrams, xrefs)
3. Run pipeline: `python scripts/generate_authoring_pipeline.py`
4. Run QA: `python scripts/qa_authoring_checker.py`

### 2. Adding New Datasets

```yaml
artifacts:
  datasets:
    - id: "new_dataset"
      file: "new_dataset.csv"
      headers: ["col1", "col2", "col3"]
      facet: "01_core.new_dataset"
```

Pipeline will create the CSV with headers automatically.

### 3. Adding New Diagrams

```yaml
artifacts:
  diagrams:
    - id: "new_diagram"
      file: "new_diagram.mmd"
      facet: "01_core.new_diagram"
```

Pipeline will create a Mermaid stub.

### 4. Large Datasets

For CSV files >2MB:
- Pipeline automatically creates `-sample.csv` versions
- Full file is linked, sample is embedded
- Keeps page load times reasonable

### 5. Facet Naming

- Use lowercase with underscores
- Format: `<chapter>.<descriptive_name>`
- Must be unique across all chapters
- Corresponds to file stem (without extension)

## Troubleshooting

### CSV Headers Don't Match

If QA reports header mismatches:
1. Check `_sources/chapter_*.md` frontmatter
2. Update `headers` list to match actual CSV
3. Or update CSV to match frontmatter

### Missing Facet Anchors

Anchors are auto-generated by the pipeline. If missing:
1. Re-run: `python scripts/generate_authoring_pipeline.py`
2. Check `index.md` for `(facet-...)=` lines

### Mermaid Diagrams Don't Render

1. Check for init block: `%%{init: { 'theme': 'neutral' }}%%`
2. Run: `python scripts/fix_mermaid_init.py`
3. Validate Mermaid syntax at https://mermaid.live

### Sphinx Build Errors

Common issues:
- Missing extensions: Install from `requirements-docs.txt`
- MyST syntax errors: Validate with QA checker
- Relative paths: Use `./datasets/` or `./diagrams/`

## Further Reading

- [MyST Syntax Guide](https://myst-parser.readthedocs.io/)
- [PyData Theme Docs](https://pydata-sphinx-theme.readthedocs.io/)
- [Mermaid Syntax](https://mermaid.js.org/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)

---

**Last Updated:** 2025-10-14  
**Pipeline Version:** 1.0  
**Status:** ✅ Production Ready
