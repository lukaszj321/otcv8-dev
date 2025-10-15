---
name: otui
applyTo: "modules/**/*.otui"
read:
  - "modules/**"
write:
  - "docs/authoring/04_ui/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# OTUI — Instructions

## Goal
Parse OTUI widget definitions into:
- `docs/authoring/04_ui/otui/**.md` (id, class, parent, key props, simplified AST)
- `docs/authoring/04_ui/diagrams/*.mmd` (graph TD: hierarchy)
- `docs/authoring/04_ui/datasets/ui.csv|ndjson`

## Notes
- Limit diagrams ≤ 80 lines; split by subtree.
- Link to assets in `11_data` when images/fonts appear.
