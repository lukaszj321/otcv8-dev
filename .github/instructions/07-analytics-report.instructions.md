
---
title: 07 — Analytics & Report (Authoring)
purpose: Produce per‑chapter analytics CSV and short narrative.
outputs:
  - docs/authoring/<chapter>/datasets/summary.csv  # metrics per chapter
  - docs/authoring/<chapter>/analysis.md            # optional short narrative

summary.headers: ["metric","value","note"]
metrics.examples:
  - "entities_total", "<int>", "Count of primary entities in chapter"
  - "datasets_count", "<int>", "Number of CSV datasets"
  - "diagrams_count", "<int>", "Number of Mermaid diagrams"
  - "crosslinks_out", "<int>", "Outgoing xref edges"
  - "crosslinks_in", "<int>", "Incoming xref edges"

analysis.md.template: |
  # Analysis
  This chapter contains **{entities_total} entities** across **{datasets_count} datasets** and **{diagrams_count} diagrams**.
  Crosslinks: out={crosslinks_out}, in={crosslinks_in}.

acceptance:
  - [ ] summary.csv present with required headers
  - [ ] Any values are integers (0 allowed) and consistent with filesystem scan
