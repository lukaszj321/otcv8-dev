---
name: diagrams
applyTo: "docs/authoring/**/*"
read:
  - "docs/authoring/**"
write:
  - "docs/authoring/**/diagrams/**"
constraints:
  - "UTF-8"
  - "LF"
  - "idempotent"
---

# Diagrams — Instructions

## Goal
Ensure Mermaid diagrams exist, are split ≤ 80 lines, and include neutral theme init.

## Mermaid init
Use at top of each diagram:
