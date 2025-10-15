---
name: qa-analytics
applyTo: "docs/authoring/**/*"
read:
  - "docs/authoring/**"
write:
  - "docs/authoring/qa/**"
  - "docs/authoring/analytics/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---
purpose: Validate structure, schemas, anchors, and Sphinx render.
checks:
  structure:
    - docs/authoring/<chapter>/datasets/*.csv exist
    - docs/authoring/<chapter>/diagrams/*.mmd exist (>=1 recommended)
    - docs/authoring/<chapter>/index.md exists
  csv_headers:
    - summary.csv: ["metric","value","note"]
    - entities.csv (if present): ["id","name","type","notes"]
  mermaid:
    - First line has %%{init: ...}%%
    - If CSV with same stem exists → ensure click anchor
  facets:
    - Anchor exists: (facet-<chapter>.<stem>) in index.md
    - Mermaid click points to ./index.html#facet-<chapter>.<stem>
  sphinx:
    - Build succeeds with PyData theme (no blocking warnings)
    - At least one {csv-table} and one {mermaid} per chapter
report:
  - Save QA report to docs/authoring/_data/qa_report.csv
  - headers: ["chapter","check","status","details"]
acceptance:
  - [ ] qa_report.csv exists; any FAILs clearly listed


# QA + Analytics — Instructions

## QA outputs
- `qa/frontmatter_issues.csv`
- `qa/link_lint.csv`
- `qa/chunking_report.csv`
- `qa/dataset_sanity.csv`
- `qa/diagram_lint.csv`
- `qa/idempotency.md`
- `qa/qa_summary.md`

## Analytics outputs
- `analytics/coverage.csv`
- `analytics/gaps.csv`
- `analytics/xref_stats.csv`
- `analytics/coverage_matrix.md`
- `analytics/overview.mmd`
- `analytics/run_summary.json`
- `analytics/errors.md`
