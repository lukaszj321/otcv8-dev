
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
