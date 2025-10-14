---
title: 01_core - Core
---

# 01_core - Core

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`01_core.entities`](#facet-01_core.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `headers.csv`
*Facet:* [`01_core.headers`](#facet-01_core.headers)

```{csv-table} headers
:header-rows: 1
:file: ./datasets/headers.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`01_core.summary`](#facet-01_core.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`01_core.architecture`](#facet-01_core.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  Architecture[01_core:architecture] --> Data[Datasets]
  Data --> Page[Index]

click Architecture "./index.html#facet-01_core.architecture" "Open architecture"
        ```

#### `flow.mmd`
        *Facet:* [`01_core.flow`](#facet-01_core.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

## Appendix / Facets
(facet-01_core.architecture)=
### Facet: `01_core.architecture`
(facet-01_core.entities)=
### Facet: `01_core.entities`
(facet-01_core.flow)=
### Facet: `01_core.flow`
(facet-01_core.headers)=
### Facet: `01_core.headers`
(facet-01_core.summary)=
### Facet: `01_core.summary`
