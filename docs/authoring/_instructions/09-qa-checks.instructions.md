---
title: "09 — QA Checks (Authoring)"
purpose: "Validate structure, schemas, anchors, and Sphinx render."

checks:
  structure:
    - "docs/authoring/<chapter>/datasets/*.csv exist (>=1)"
    - "docs/authoring/<chapter>/diagrams/*.mmd exist (>=1 recommended)"
    - "docs/authoring/<chapter>/index.md exists"
  csv_headers:
    - 'summary.csv: ["metric","value","note"]'
    - 'entities.csv (if present): ["id","name","type","notes"]'
  mermaid:
    - "First line STARTS with: %%{init: {...}}%% (UNQUOTED)"
    - "Use ASCII arrows only (->>, -->>); no Unicode arrows (→)"
    - "sequenceDiagram: NO `click` anchors (unsupported)"
    - "flowchart/graph: require `click` anchors if matching facet exists"
  facets:
    - "Anchor id exists in index.md: facet-<chapter>.<stem>"
    - "Flowchart clicks point to: ./index.html#facet-<chapter>.<stem>"
  sphinx:
    - "Build succeeds with PyData theme under `-W` (treat warnings as errors)"
    - "Each chapter has ≥1 `{csv-table}` and ≥1 `{mermaid}` block"

report:
  file: "docs/authoring/_data/qa_report.csv"
  headers: ["chapter","check","status","details"]

acceptance:
  - [ ] docs/authoring/_data/qa_report.csv exists
  - [ ] No FAIL status rows
  - [ ] sequence diagrams contain no `click` directives
  - [ ] flowcharts with facets have valid `click` targets
---

## IPC

**Kanały IPC (Studio/Electron)**

- `studio:qa.run` `{ suite }` — uruchamia zdefiniowany zestaw testów (linty, sanity, smoke).
- `studio:qa.open` `{ report }` — otwiera raport QA (CSV/MD/HTML) dla bieżącego rozdziału.
- `studio:qa.baseline` — zapisuje/porównuje baseline wyników (idempotency).

## Sanity

- [ ] Wszystkie testy krytyczne (linty, sanity) mają status PASS; FAIL wymaga `note` i ticketu.
- [ ] Raport QA zawiera sumy kontrolne (SHA256) kluczowych artefaktów (jeśli dotyczy).
- [ ] Idempotencja: ponowny bieg `studio:qa.run` nie zmienia wyników (poza timestampem).
