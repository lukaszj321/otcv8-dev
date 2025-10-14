
---
title: 05 — Relations & Cross‑References
purpose: Build cross‑chapter references (UI ↔ Events ↔ Modules ↔ Core ↔ Network).
constraints:
  - Use only in‑repo sources
  - Output CSV + optional JSON map

outputs:
  - docs/authoring/_data/xref.csv
    header: ["from_chapter","from_facet","to_chapter","to_facet","type","evidence_path","note"]
  - docs/authoring/_data/xref.json
    schema: [ { "from": {"c":"<ch>","f":"<facet>"}, "to": {...}, "type": "uses|emits|handles|includes|calls", "evidence": "<path>" } ]

builder:
  - If `authoring/_tools/xref_builder.py` exists, use it; else, infer from datasets keys (widget names, event names, module exports)
  - Normalize facet IDs to "<chapter>.<stem>"
  - Types allowed: uses|emits|handles|includes|calls

acceptance:
  - [ ] xref.csv exists with >= N rows (best effort)
  - [ ] At least one crosslink UI↔Events and Modules↔Core
