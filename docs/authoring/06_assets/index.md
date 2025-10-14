---
title: Assets — export kit
---

# Assets — export kit

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

### pipeline_flow
*Facet:* [`06_assets.pipeline_flow`](#facet-06_assets.pipeline_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[06_assets.pipeline_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-06_assets.pipeline_flow" "Open pipeline_flow"
```

## Cross-References

- **provides** → `10_game_runtime.resources` (evidence: `docs/authoring/10_game_runtime/datasets/resources.csv`)
- **used_by** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)

## Appendix / Facets

(facet-06_assets.assets_index)=
### Facet: `06_assets.assets_index`
Type: dataset

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
