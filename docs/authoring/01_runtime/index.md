---
title: 01_runtime - Runtime
---

# 01_runtime - Runtime

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`01_runtime.entities`](#facet-01_runtime.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `runtime_stats.csv`
*Facet:* [`01_runtime.runtime_stats`](#facet-01_runtime.runtime_stats)

```{csv-table} runtime_stats
:header-rows: 1
:file: ./datasets/runtime_stats.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`01_runtime.summary`](#facet-01_runtime.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`01_runtime.architecture`](#facet-01_runtime.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Runtime
        E0[Runtime Metrics]
        E1[Performance Stats]
        E2[Memory Usage]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `flow.mmd`
        *Facet:* [`01_runtime.flow`](#facet-01_runtime.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Runtime] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

#### `runtime_flow.mmd`
        *Facet:* [`01_runtime.runtime_flow`](#facet-01_runtime.runtime_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  RuntimeFlow[01_runtime:runtime_flow] --> Data[Datasets]
  Data --> Page[Index]

click RuntimeFlow "./index.html#facet-01_runtime.runtime_flow" "Open runtime_flow"
        ```

## Appendix / Facets
(facet-01_runtime.architecture)=
### Facet: `01_runtime.architecture`
(facet-01_runtime.entities)=
### Facet: `01_runtime.entities`
(facet-01_runtime.flow)=
### Facet: `01_runtime.flow`
(facet-01_runtime.runtime_flow)=
### Facet: `01_runtime.runtime_flow`
(facet-01_runtime.runtime_stats)=
### Facet: `01_runtime.runtime_stats`
(facet-01_runtime.summary)=
### Facet: `01_runtime.summary`
