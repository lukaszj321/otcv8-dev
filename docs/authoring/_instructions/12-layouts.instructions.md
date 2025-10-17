---
name: "layouts"
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

outputs:
  - "docs/authoring/13_layouts/index.md"
  - "docs/authoring/13_layouts/datasets/layouts.csv"
  - "docs/authoring/13_layouts/datasets/layouts.ndjson"
  - "docs/authoring/13_layouts/diagrams/layouts_graph.mmd"
---

# Layouts — Instructions

## Goal
Inwentarz layoutów (ekrany/sekcje) z `layouts/**` i ich referencji do obrazów/fontów/OTUI.

## Datasets
- `layouts.csv` **lub** `.ndjson`
  - **CSV kolumny**:
    - `layout_id` (string)
    - `path` (string)
    - `type` (screen|section|partial|other)
    - `section` (string|null)
    - `uses_images` (JSON array)
    - `uses_fonts` (JSON array)
    - `uses_otui` (JSON array)
    - `notes` (string)

## Diagrams (opcjonalnie)
- `diagrams/layouts_graph.mmd` (flowchart)
- 1. linia wymagana:
```

%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%

```

## Crosslinks
- Dodaj xref do `04_ui` (OTUI) oraz `11_data` (assets).

## Index
- `index.md`: frontmatter, `{toctree}` hidden, `{contents} :local:`,
`{csv-table}` z `layouts.csv`, `{mermaid}` (jeśli jest diagram),
sekcja **Appendix / Facets** (jeśli używasz facetów).

## Notes
- Typ rozpoznawaj po ścieżce/nazwie; referencje wyciągaj grepem z `.otui`, `.lua` i plików layoutów.
- Listy w CSV serializuj jako **JSON arrays** (`[]`), ścieżki względne do repo.

## Acceptance
- [ ] `index.md` wygenerowany
- [ ] `layouts.csv` **lub** `.ndjson` (kolumny jak wyżej)
- [ ] (Jeśli diagram) Mermaid renderuje się (init w 1. linii, ASCII strzałki)
- [ ] Crosslinki do `04_ui` i `11_data` istnieją
