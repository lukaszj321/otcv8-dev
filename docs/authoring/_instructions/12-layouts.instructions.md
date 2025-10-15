
---
name: layouts
applyTo:
  - "layouts/**/*"
read:
  - "layouts/**"
  - "modules/**"
  - "data/**"
write:
  - "docs/authoring/13_layouts/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Layouts — Instructions

## Goal
Inwentarz layoutów (ekrany/sekcje) z `layouts/**` i ich referencji do obrazów/fontów/OTUI.

## Output
- `docs/authoring/13_layouts/index.md` (intro, TOC)
- `docs/authoring/13_layouts/datasets/layouts.csv|ndjson`
  - kolumny: `layout_id,path,type,section,uses_images[],uses_fonts[],uses_otui[],notes`
- `diagrams/*.mmd` — graf powiązań (graph TD), ≤ 80 linii
- Crosslinks do `04_ui` i `11_data`.
