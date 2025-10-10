# Diagramy (Mermaid)

Mermaid jest włączony przez rozszerzenie `sphinxcontrib-mermaid`.

```{mermaid}
flowchart TD
  A[Start] --> B{Zdarzenie?}
  B -- yes --> C[Dispatcher]
  C --> D[Handler: module/ui]
  D --> E[Render]
  B -- no --> F[Idle]
```
