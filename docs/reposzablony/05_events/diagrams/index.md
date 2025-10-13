# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Event Details
        E0[Event Patterns]
        E1[Event Chains]
        E2[Event Handlers]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Event Details] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
