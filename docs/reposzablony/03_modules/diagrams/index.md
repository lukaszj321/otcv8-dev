# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Lua Modules
        E0[Modules]
        E1[Exported Functions]
        E2[Callbacks]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Lua Modules] --> B[Data Collection]
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
    subgraph Lua Modules
        E0[Modules]
        E1[Exported Functions]
        E2[Callbacks]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Lua Modules] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
