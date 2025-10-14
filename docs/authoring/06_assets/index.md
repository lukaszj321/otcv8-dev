---
title: 06_assets - Assets
---

# 06_assets - Assets

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `assets_index.csv`
*Facet:* [`06_assets.assets_index`](#facet-06_assets.assets_index)

```{csv-table} assets_index
:header-rows: 1
:file: ./datasets/assets_index.csv
:widths: auto
```

:::

:::{grid-item}

#### `entities.csv`
*Facet:* [`06_assets.entities`](#facet-06_assets.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`06_assets.summary`](#facet-06_assets.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`06_assets.architecture`](#facet-06_assets.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Assets
        E0[Sprites]
        E1[Textures]
        E2[Asset References]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `assets_pipeline.mmd`
        *Facet:* [`06_assets.assets_pipeline`](#facet-06_assets.assets_pipeline)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  AEtPipeline[06_assets:assets_pipeline] --> Data[Datasets]
  Data --> Page[Index]

click AEtPipeline "./index.html#facet-06_assets.assets_pipeline" "Open assets_pipeline"
        ```

#### `flow.mmd`
        *Facet:* [`06_assets.flow`](#facet-06_assets.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

## Appendix / Facets
(facet-06_assets.architecture)=
### Facet: `06_assets.architecture`
(facet-06_assets.assets_index)=
### Facet: `06_assets.assets_index`
(facet-06_assets.assets_pipeline)=
### Facet: `06_assets.assets_pipeline`
(facet-06_assets.entities)=
### Facet: `06_assets.entities`
(facet-06_assets.flow)=
### Facet: `06_assets.flow`
(facet-06_assets.summary)=
### Facet: `06_assets.summary`
