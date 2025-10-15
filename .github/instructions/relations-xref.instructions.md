---
name: relations-xref
applyTo: "docs/authoring/**/*"
read:
  - "docs/authoring/**"
write:
  - "docs/authoring/relations/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Relations/XRef — Instructions

## Goal
Build cross-reference graph across chapters.

## Output
- `relations/relations.csv` (from_id,to_id,rel_type,src_path,line)
- `relations/matrix.md` (matrix element×target)
- Keep rel_types in: calls, handles, emits, owns, renders, uses.
