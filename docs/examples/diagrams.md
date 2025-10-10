# Diagramy (Mermaid)

```{mermaid}
flowchart TD
  A[Core] --> B(Events)
  A --> C(Modules)
  C --> D[UI]
  C --> E[Network]
  E --> F[(Assets)]
  B --> G{Settings/Crypto}
  G --> H[Audio]
  H --> I[Logging]
  I --> J[Game Runtime]
```
