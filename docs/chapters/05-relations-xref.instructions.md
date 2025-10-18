---
title: "05 — Relations & Cross-References"
purpose: "Build cross-chapter references (UI ↔ Events ↔ Modules ↔ Core ↔ Network)."
constraints:
  - "Use only in-repo sources"
  - "Output CSV + optional JSON map"

outputs:
  - file: "docs/authoring/_data/xref.csv"
    header: ["from_chapter","from_facet","to_chapter","to_facet","type","evidence_path","note"]
    rules:
      - 'type ∈ {"uses","emits","handles","includes","calls"}'
      - "evidence_path is relative (./...)"
      - "from_chapter,from_facet != to_chapter,to_facet"
  - file: "docs/authoring/_data/xref.json"
    schema:
      - from: { c: "<ch>", f: "<facet>" }
        to:   { c: "<ch>", f: "<facet>" }
        type: "uses|emits|handles|includes|calls"
        evidence: "<path>"
    rules:
      - "deduplicate identical {from,to,type}"
      - 'facet format: "<chapter>.<stem>"'

builder:
  tool: "authoring/_tools/xref_builder.py"
  fallback: "infer from datasets (widgets, events, module exports)"
  normalize_rule: 'facet = "<chapter>.<stem>"'
  types_allowed: ["uses","emits","handles","includes","calls"]

acceptance:
  - "[ ] docs/authoring/_data/xref.csv exists with >= N rows (best effort)"
  - "[ ] At least one crosslink UI↔Events and Modules↔Core"
---

# 05 — Relations & Cross-References

## Wyjścia
- CSV: `docs/authoring/_data/xref.csv`
- JSON (opcjonalnie): `docs/authoring/_data/xref.json`

### Schemat CSV
```csv
from_chapter,from_facet,to_chapter,to_facet,type,evidence_path,note
04_ui,04_ui.widgets_hierarchy,02_events,02_events.event_flow,uses,./04_ui/datasets/ui_widgets.csv,"example"
```

### Schemat JSON (przykład)
```json
[
  {
    "from": {"c":"04_ui","f":"04_ui.widgets_hierarchy"},
    "to":   {"c":"02_events","f":"02_events.event_flow"},
    "type": "uses",
    "evidence": "./04_ui/datasets/ui_widgets.csv"
  }
]
```

## Zasady
- `type`: tylko z listy `uses|emits|handles|includes|calls`.
- `facet` w formacie `<chapter>.<stem>`.
- Duplikaty `{from,to,type}` — usunąć.

## Akceptacja (DoD)
- [ ] CSV istnieje i ma ≥ N wierszy.  
- [ ] Min. jeden crosslink UI↔Events i Modules↔Core.  
