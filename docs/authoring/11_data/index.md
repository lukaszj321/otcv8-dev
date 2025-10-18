---
title: 11_data - Data
---

# 11_data - Data

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### assets_catalog
*Facet:* [`11_data.assets_catalog`](#facet-11_data.assets_catalog)

```{csv-table} assets_catalog
:header-rows: 1
:file: ./datasets/assets_catalog.csv
:widths: auto
```

### assets_summary
*Facet:* [`11_data.assets_summary`](#facet-11_data.assets_summary)

```{csv-table} assets_summary
:header-rows: 1
:file: ./datasets/assets_summary.csv
:widths: auto
```

### data_assets
*Facet:* [`11_data.data_assets`](#facet-11_data.data_assets)

```{csv-table} data_assets
:header-rows: 1
:file: ./datasets/data_assets.csv
:widths: auto
```

### fonts
*Facet:* [`11_data.fonts`](#facet-11_data.fonts)

```{csv-table} fonts
:header-rows: 1
:file: ./datasets/fonts.csv
:widths: auto
```

### images
*Facet:* [`11_data.images`](#facet-11_data.images)

```{csv-table} images
:header-rows: 1
:file: ./datasets/images.csv
:widths: auto
```

### locales
*Facet:* [`11_data.locales`](#facet-11_data.locales)

```{csv-table} locales
:header-rows: 1
:file: ./datasets/locales.csv
:widths: auto
```

### shaders
*Facet:* [`11_data.shaders`](#facet-11_data.shaders)

```{csv-table} shaders
:header-rows: 1
:file: ./datasets/shaders.csv
:widths: auto
```

### sounds
*Facet:* [`11_data.sounds`](#facet-11_data.sounds)

```{csv-table} sounds
:header-rows: 1
:file: ./datasets/sounds.csv
:widths: auto
```

### styles
*Facet:* [`11_data.styles`](#facet-11_data.styles)

```{csv-table} styles
:header-rows: 1
:file: ./datasets/styles.csv
:widths: auto
```

### summary
*Facet:* [`11_data.summary`](#facet-11_data.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

### ui_asset_usage
*Facet:* [`11_data.ui_asset_usage`](#facet-11_data.ui_asset_usage)

```{csv-table} ui_asset_usage
:header-rows: 1
:file: ./datasets/ui_asset_usage.csv
:widths: auto
```

### ui_assets_links
*Facet:* [`11_data.ui_assets_links`](#facet-11_data.ui_assets_links)

```{csv-table} ui_assets_links
:header-rows: 1
:file: ./datasets/ui_assets_links.csv
:widths: auto
```

## Diagrams
### asset_linking
*Facet:* [`11_data.asset_linking`](#facet-11_data.asset_linking)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  I[OTUI property] -->|image-source/icon/font| ASSET[(Asset file)]
  ASSET --> INDEX[images.csv/fonts.csv/...]
  INDEX --> UI[Widgets Index]
click AssetLinking "./index.html#facet-11_data.asset_linking" "Open asset_linking"
```

### asset_to_ui
*Facet:* [`11_data.asset_to_ui`](#facet-11_data.asset_to_ui)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
flowchart LR
  OTUI[OTUI props]-->IMG(images.csv)
  OTUI-->FNT(fonts.csv)
  OTUI-->STY(styles.csv)
  IMG-->USE(ui_asset_usage.csv)
  FNT-->USE
  STY-->USE
click AssetToUi "./index.html#facet-11_data.asset_to_ui" "Open asset_to_ui"
```

### assets_links
*Facet:* [`11_data.assets_links`](#facet-11_data.assets_links)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    OTUI["OTUI Files<br/>(*.otui)"] --> PROPS["Properties:<br/>image-source<br/>icon<br/>font"]
    PROPS --> RESOLVE["Asset Resolver"]
    RESOLVE --> DATA["data/**<br/>(images/fonts/styles)"]
    RESOLVE --> LAYOUT["layouts/**<br/>(overrides)"]
    DATA --> INDEX["Asset Index<br/>data_assets.csv"]
    LAYOUT --> OVERRIDE["layout_overrides.csv"]
    INDEX --> USAGE["ui_asset_usage.csv"]
    OVERRIDE --> USAGE
    
    USAGE --> STATS["Statistics<br/>stats.json"]
    
    click INDEX "../11_data/index.html#facet-11_data.main" "Open Data Index"
    click USAGE "../11_data/index.html#facet-11_data.ui_asset_usage" "Open UI Asset Usage"
click AssetsLinks "./index.html#facet-11_data.assets_links" "Open assets_links"
```

### assets_topology
*Facet:* [`11_data.assets_topology`](#facet-11_data.assets_topology)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[OTUI widgets] --> B[Images/Textures]
    A --> C[Fonts]
    B --> D[Data/]
    click A "./index.html#facet-11_data.ui_assets_links" "See UI assets links"
click AssetsTopology "./index.html#facet-11_data.assets_topology" "Open assets_topology"
```

### data_flow
*Facet:* [`11_data.data_flow`](#facet-11_data.data_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
flowchart LR
  A[data/*] --> B[Indexer CSV]
  B --> C[Datasets]
  C --> D[UI Pages]
  B --> E[Crosslinks]
  D --> F[RAG]
click DataFlow "./index.html#facet-11_data.data_flow" "Open data_flow"
```

### data_overview
*Facet:* [`11_data.data_overview`](#facet-11_data.data_overview)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    Data[data/ Root] --> Images[images/]
    Data --> Fonts[fonts/]
    Data --> Sounds[sounds/]
    Data --> Styles[styles/]
    Data --> Locales[locales/]
    Data --> Shaders[shaders/]
    Images --> UI[UI Assets]
    Images --> Game[Game Assets]
    Fonts --> Bitmap[Bitmap Fonts]
    Fonts --> TTF[TTF Fonts]
click DataOverview "./index.html#facet-11_data.data_overview" "Open data_overview"
```

### overview
*Facet:* [`11_data.overview`](#facet-11_data.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Data Assets] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-11_data.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```



## Appendix / Facets

(facet-11_data.asset_linking)=
### Facet: `11_data.asset_linking`
Type: diagram

(facet-11_data.asset_to_ui)=
### Facet: `11_data.asset_to_ui`
Type: diagram

(facet-11_data.assets_catalog)=
### Facet: `11_data.assets_catalog`
Type: dataset

(facet-11_data.assets_links)=
### Facet: `11_data.assets_links`
Type: diagram

(facet-11_data.assets_summary)=
### Facet: `11_data.assets_summary`
Type: dataset

(facet-11_data.assets_topology)=
### Facet: `11_data.assets_topology`
Type: diagram

(facet-11_data.data_assets)=
### Facet: `11_data.data_assets`
Type: dataset

(facet-11_data.data_flow)=
### Facet: `11_data.data_flow`
Type: diagram

(facet-11_data.data_overview)=
### Facet: `11_data.data_overview`
Type: diagram

(facet-11_data.fonts)=
### Facet: `11_data.fonts`
Type: dataset

(facet-11_data.images)=
### Facet: `11_data.images`
Type: dataset

(facet-11_data.locales)=
### Facet: `11_data.locales`
Type: dataset

(facet-11_data.overview)=
### Facet: `11_data.overview`
Type: diagram

(facet-11_data.shaders)=
### Facet: `11_data.shaders`
Type: dataset

(facet-11_data.sounds)=
### Facet: `11_data.sounds`
Type: dataset

(facet-11_data.styles)=
### Facet: `11_data.styles`
Type: dataset

(facet-11_data.summary)=
### Facet: `11_data.summary`
Type: dataset

(facet-11_data.ui_asset_usage)=
### Facet: `11_data.ui_asset_usage`
Type: dataset

(facet-11_data.ui_assets_links)=
### Facet: `11_data.ui_assets_links`
Type: dataset

