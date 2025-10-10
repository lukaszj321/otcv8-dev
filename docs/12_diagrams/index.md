# Diagramy (Mermaid)

```{mermaid}
flowchart TD
  A[Start] --> B{Czy asset jest w cache?}
  B -- Tak --> C[Użyj z cache]
  B -- Nie --> D[Pobierz z dysku/HTTP]
  D --> E[Zapisz do cache]
  C --> F[Zwróć do runtime]
  E --> F
```
