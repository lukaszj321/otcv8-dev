---
title: 06_assets - Assets
---

# 06_assets - Assets

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### assets_index
*Facet:* [`06_assets.assets_index`](#facet-06_assets.assets_index)

```{csv-table} assets_index
:header-rows: 1
:file: ./datasets/assets_index.csv
:widths: auto
```

### entities
*Facet:* [`06_assets.entities`](#facet-06_assets.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### pipelines
*Facet:* [`06_assets.pipelines`](#facet-06_assets.pipelines)

```{csv-table} pipelines
:header-rows: 1
:file: ./datasets/pipelines.csv
:widths: auto
```

### spritesheets
*Facet:* [`06_assets.spritesheets`](#facet-06_assets.spritesheets)

```{csv-table} spritesheets
:header-rows: 1
:file: ./datasets/spritesheets.csv
:widths: auto
```

### summary
*Facet:* [`06_assets.summary`](#facet-06_assets.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
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

### assets_pipeline
        *Facet:* [`06_assets.assets_pipeline`](#facet-06_assets.assets_pipeline)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  AEtPipeline[06_assets:assets_pipeline] --> Data[Datasets]
  Data --> Page[Index]

click AEtPipeline "./index.html#facet-06_assets.assets_pipeline" "Open assets_pipeline"
        ```

### flow
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

### pipeline_flow
        *Facet:* [`06_assets.pipeline_flow`](#facet-06_assets.pipeline_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[06_assets.pipeline_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-06_assets.pipeline_flow" "Open pipeline_flow"
        ```



## Crosslinks

- **provides** → `10_game_runtime.resources` (evidence: `docs/authoring/10_game_runtime/datasets/resources.csv`)
- **used_by** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)

## Appendix / Facets

(facet-06_assets.architecture)=
### Facet: `06_assets.architecture`
Type: diagram

(facet-06_assets.assets_index)=
### Facet: `06_assets.assets_index`
Type: dataset

(facet-06_assets.assets_pipeline)=
### Facet: `06_assets.assets_pipeline`
Type: diagram

(facet-06_assets.entities)=
### Facet: `06_assets.entities`
Type: dataset

(facet-06_assets.flow)=
### Facet: `06_assets.flow`
Type: diagram

(facet-06_assets.pipeline_flow)=
### Facet: `06_assets.pipeline_flow`
Type: diagram

(facet-06_assets.pipelines)=
### Facet: `06_assets.pipelines`
Type: dataset

(facet-06_assets.spritesheets)=
### Facet: `06_assets.spritesheets`
Type: dataset

(facet-06_assets.summary)=
### Facet: `06_assets.summary`
Type: dataset

