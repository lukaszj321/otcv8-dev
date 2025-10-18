---
title: "07 — Analytics & Report (Authoring)"
purpose: "Produce per-chapter analytics CSV and short narrative."

outputs:
  - "docs/authoring/<chapter>/datasets/summary.csv"
  - "docs/authoring/<chapter>/analysis.md"

summary:
  headers: ["metric","value","note"]
  metrics_examples:
    - { metric: "entities_total",  type: "<int>", note: "Count of primary entities in chapter" }
    - { metric: "datasets_count",  type: "<int>", note: "Number of CSV datasets" }
    - { metric: "diagrams_count",  type: "<int>", note: "Number of Mermaid diagrams" }
    - { metric: "crosslinks_out",  type: "<int>", note: "Outgoing xref edges" }
    - { metric: "crosslinks_in",   type: "<int>", note: "Incoming xref edges" }

analysis_md:
  template: |
    # Analysis
    This chapter contains **{entities_total} entities** across **{datasets_count} datasets** and **{diagrams_count} diagrams**.
    Crosslinks: out={crosslinks_out}, in={crosslinks_in}.

acceptance:
  - "[ ] summary.csv present with required headers"
  - "[ ] Values are integers (0 allowed) and match filesystem scan"
---

## IPC

**Kanały IPC (Studio/Electron)**

- `studio:analytics.compute` — skanuje rozdział i generuje `datasets/summary.csv` + `analysis.md` wg szablonu.
- `studio:analytics.open` `{ file: 'summary'|'analysis' }` — otwiera wygenerowane artefakty.
- `studio:analytics.validate` — sprawdza typy wartości i spójność z filesystem scan.

## Sanity

- [ ] `summary.csv` istnieje i posiada nagłówki: `metric,value,note`.
- [ ] Wszystkie `value` to liczby całkowite (0 dozwolone) dopasowane do realnego skanu katalogu.
- [ ] `analysis.md` (opcjonalny) wypełniony na podstawie `summary.csv` i szablonu.

## Przykłady

**Przykład `summary.csv`**
```csv
metric,value,note
entities_total,42,"Łączna liczba bytów"
datasets_count,5,"CSV w rozdziale"
diagrams_count,3,"Mermaid w rozdziale"
crosslinks_out,7,"Zewnętrzne xrefy"
crosslinks_in,2,"Przychodzące xrefy"
```
