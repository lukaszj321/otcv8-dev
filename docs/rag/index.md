# RAG Hub — źródła wiedzy i kontekst

## Zakres (H2)
- **Źródła**: pliki z `docs/` + `data/` + wybrane foldery repo.
- **Aktualizacja**: strategia reindeksacji (po merge / po tagu).

### Struktura indeksu (H3)
- Klucze: ścieżka, tytuł H1, nagłówki H2/H3/H4, code blocks, metadane.

#### Przykład polityki (H4)
- `full-reindex`: co release.
- `partial-reindex`: zmienione pliki wg git diff.

## Integracja (placeholder)
- Export CSV/JSON z metadanymi nagłówków i linków kotwiczących.
- Runner do generowania _site map_ dla RAG.
