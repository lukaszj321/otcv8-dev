# Diagrams


## Diagrams

```{mermaid}
:caption: Architecture

graph LR
    subgraph Audio
        E0[Sound Channels]
        E1[Audio Sources]
        E2[Audio Stats]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Audio] --> B[Data Collection]
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
    subgraph Audio
        E0[Sound Channels]
        E1[Audio Sources]
        E2[Audio Stats]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Flow

graph TD
    A[Audio] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```
