
---
title: Data — Assets & Overrides (11)
doc_id: "authoring.11_data.index"
---

# Data — Assets & Overrides

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

::: {grid} 1 1 2 3
:gutter: 2

::: {grid-item}
#### `images.csv`
*Facet:* [`11_data.images`](#facet-11_data.images)

```{csv-table} images
:header-rows: 1
:file: ./datasets/images.csv
:widths: auto
```
:::

::: {grid-item}
#### `fonts.csv`
*Facet:* [`11_data.fonts`](#facet-11_data.fonts)

```{csv-table} fonts
:header-rows: 1
:file: ./datasets/fonts.csv
:widths: auto
```
:::

::: {grid-item}
#### `styles.csv`
*Facet:* [`11_data.styles`](#facet-11_data.styles)

```{csv-table} styles
:header-rows: 1
:file: ./datasets/styles.csv
:widths: auto
```
:::

::: {grid-item}
#### `locales.csv`
*Facet:* [`11_data.locales`](#facet-11_data.locales)

```{csv-table} locales
:header-rows: 1
:file: ./datasets/locales.csv
:widths: auto
```
:::

::: {grid-item}
#### `sounds.csv`
*Facet:* [`11_data.sounds`](#facet-11_data.sounds)

```{csv-table} sounds
:header-rows: 1
:file: ./datasets/sounds.csv
:widths: auto
```
:::

::: {grid-item}
#### `shaders.csv`
*Facet:* [`11_data.shaders`](#facet-11_data.shaders)

```{csv-table} shaders
:header-rows: 1
:file: ./datasets/shaders.csv
:widths: auto
```
:::

::: {grid-item}
#### `ui_asset_usage.csv`
*Facet:* [`11_data.ui_asset_usage`](#facet-11_data.ui_asset_usage)

```{csv-table} ui_asset_usage
:header-rows: 1
:file: ./datasets/ui_asset_usage.csv
:widths: auto
```
:::
:::

## Diagrams

#### `data_overview.mmd`
*Facet:* [`11_data.data_overview`](#facet-11_data.data_overview)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
  DATA[data/**] --> IMAGES
  DATA --> STYLES
  DATA --> FONTS
  DATA --> SOUNDS
  DATA --> SHADERS
  DATA --> LOCALES
  LAYOUTS[layouts/<name>/**] -->|override| DATA
```

#### `asset_to_ui.mmd`
*Facet:* [`11_data.asset_to_ui`](#facet-11_data.asset_to_ui)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph LR
  OTUI[/OTUI/] --> IMG[images.csv]
  OTUI --> FNT[fonts.csv]
  OTUI --> STY[styles.csv]
  IMG --> USE[ui_asset_usage.csv]
  FNT --> USE
  STY --> USE
  click IMG "./index.html#facet-11_data.images" "Open images"
  click FNT "./index.html#facet-11_data.fonts" "Open fonts"
  click USE "./index.html#facet-11_data.ui_asset_usage" "Open usage"
```

## Appendix / Facets

(facet-11_data.images)=
### Facet: `11_data.images`
Type: dataset

(facet-11_data.fonts)=
### Facet: `11_data.fonts`
Type: dataset

(facet-11_data.styles)=
### Facet: `11_data.styles`
Type: dataset

(facet-11_data.locales)=
### Facet: `11_data.locales`
Type: dataset

(facet-11_data.sounds)=
### Facet: `11_data.sounds`
Type: dataset

(facet-11_data.shaders)=
### Facet: `11_data.shaders`
Type: dataset

(facet-11_data.ui_asset_usage)=
### Facet: `11_data.ui_asset_usage`
Type: dataset

(facet-11_data.data_overview)=
### Facet: `11_data.data_overview`
Type: diagram

(facet-11_data.asset_to_ui)=
### Facet: `11_data.asset_to_ui`
Type: diagram
