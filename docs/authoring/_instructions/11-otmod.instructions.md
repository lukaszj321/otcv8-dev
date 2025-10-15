
---
name: otmod
applyTo:
  - "modules/**/*"
read:
  - "modules/**"
  - "mods/**"
  - "src/**"
  - "data/**"
write:
  - "docs/authoring/12_otmod/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# OTMOD — Instructions

## Goal
Zmapuj pakiety/moduły (OTMOD): manifesty, zależności, eksporty, powiązane zasoby i UI.

## Output
- `docs/authoring/12_otmod/index.md`
- `docs/authoring/12_otmod/datasets/otmod_packages.csv|ndjson`
  - kolumny: `module,path,manifest,dependencies[],exports[],assets[],ui_roots[],entry_lua,notes`
- `diagrams/*.mmd` — zależności modułów (graph TD), ≤ 80 linii
- Crosslinks do `03_modules`, `11_data`, `04_ui`.

## Notes
- Szukaj plików manifestów i struktur katalogowych; agreguj eksporty Lua i odwołania do zasobów/OTUI.
