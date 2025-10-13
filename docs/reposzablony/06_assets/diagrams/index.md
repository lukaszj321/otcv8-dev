# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Assets
        E0[Sprites]
        E1[Textures]
        E2[Asset References]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Assets] --> B[Data Collection]
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
    subgraph Assets
        E0[Sprites]
        E1[Textures]
        E2[Asset References]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Assets] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
