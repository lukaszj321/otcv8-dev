# Diagrams


## Diagrams

:caption: Architecture

```{mermaid}
graph LR
    subgraph Core API
        E0[Classes]
        E1[Functions]
        E2[Namespaces]
        E0 --> E1
        E1 --> E2
    end
```

:caption: Flow

```{mermaid}
graph TD
    A[Core API] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
