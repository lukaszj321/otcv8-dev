---
name: otmod
applyTo: "modules/**/*"
read:
  - "modules/**"
write:
  - "docs/authoring/12_otmod/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# OTMOD — Instructions

## Goal
Document module packaging: structure, manifest, dependencies, entrypoints, integration with UI/Lua.

## Output
- `docs/authoring/12_otmod/index.md`
- `docs/authoring/12_otmod/datasets/otmod.csv|ndjson`
- Crosslinks to `03_modules` and `04_ui`.
