---
title: 05_network - Network
---

# 05_network - Network

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`05_network.entities`](#facet-05_network.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `network_messages.csv`
*Facet:* [`05_network.network_messages`](#facet-05_network.network_messages)

```{csv-table} network_messages
:header-rows: 1
:file: ./datasets/network_messages.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`05_network.summary`](#facet-05_network.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`05_network.architecture`](#facet-05_network.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Network
        E0[Network Messages]
        E1[Protocol Handlers]
        E2[Network Stats]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `flow.mmd`
        *Facet:* [`05_network.flow`](#facet-05_network.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `network_sequence.mmd`
        *Facet:* [`05_network.network_sequence`](#facet-05_network.network_sequence)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  NetworkEquence[05_network:network_sequence] --> Data[Datasets]
  Data --> Page[Index]

click NetworkEquence "./index.html#facet-05_network.network_sequence" "Open network_sequence"
        ```

## Appendix / Facets
(facet-05_network.architecture)=
### Facet: `05_network.architecture`
(facet-05_network.entities)=
### Facet: `05_network.entities`
(facet-05_network.flow)=
### Facet: `05_network.flow`
(facet-05_network.network_messages)=
### Facet: `05_network.network_messages`
(facet-05_network.network_sequence)=
### Facet: `05_network.network_sequence`
(facet-05_network.summary)=
### Facet: `05_network.summary`
