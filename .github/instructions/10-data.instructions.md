
---
name: data
applyTo:
  - "data/**/*"
read:
  - "data/**"
  - "modules/**"
  - "layouts/**"
  - "src/**"
write:
  - "docs/authoring/11_data/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Data — Instructions

## Goal
Zbuduj inwentarz zasobów z `data/**` (obrazy, fonty, dźwięki, style, configi) oraz ich powiązania z OTUI/layoutami.

## Output
- `docs/authoring/11_data/index.md` (intro + TOC)
- `docs/authoring/11_data/datasets/data_assets.csv|ndjson`
  - kolumny: `path,type,used_by_layouts[],used_by_otui[],used_by_modules[],tags[],notes`
- (opcjonalnie) `diagrams/*.mmd` — graf powiązań zasób ↔ UI/Layouts

## Notes
- Rozpoznaj typ po rozszerzeniu i/lub folderze; jeśli brak metadanych — heurystyki z referencji (grep po nazwach plików w `.otui`, `layouts/**`, `*.lua`).
