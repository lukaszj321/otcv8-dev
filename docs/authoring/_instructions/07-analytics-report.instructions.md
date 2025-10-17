---
title: 07 — Analytics & Report (Authoring)
purpose: Produce per-chapter analytics CSV and short narrative.

outputs:
  - "docs/authoring/<chapter>/datasets/summary.csv"  # metrics per chapter
  - "docs/authoring/<chapter>/analysis.md"           # optional short narrative

summary:
  headers: ["metric","value","note"]
  metrics_examples:
    - { metric: "entities_total",  type: "<int>", note: "Count of primary entities in chapter" }
    - { metric: "datasets_count",  type: "<int>", note: "Number of CSV datasets" }
    - { metric: "diagrams_count",  type: "<int>", note: "Number of Mermaid diagrams" }
    - { metric: "crosslinks_out",  type: "<int>", note: "Outgoing xref edges" }
    - { metric: "crosslinks_in",   type: "<int>", note: "Incoming xref edges" }

analysis_md:
  template: |
    # Analysis
    This chapter contains **{entities_total} entities** across **{datasets_count} datasets** and **{diagrams_count} diagrams**.
    Crosslinks: out={crosslinks_out}, in={crosslinks_in}.

acceptance:
  - [ ] summary.csv present with required headers
  - [ ] Values are integers (0 allowed) and match filesystem scan
