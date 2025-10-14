
---
title: 09 — QA Checks (Authoring)
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
