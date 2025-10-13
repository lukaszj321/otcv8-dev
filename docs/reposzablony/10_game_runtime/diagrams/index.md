# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Game Runtime
        E0[Game State]
        E1[Player Stats]
        E2[Runtime Events]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Game Runtime] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Game Runtime
        E0[Game State]
        E1[Player Stats]
        E2[Runtime Events]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Game Runtime] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
