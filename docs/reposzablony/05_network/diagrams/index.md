# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Network
        E0[Network Messages]
        E1[Protocol Handlers]
        E2[Network Stats]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Network] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
