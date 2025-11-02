---
title: 06_assets - Assets
---

# 06_assets - Assets

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### asset_loading_pipeline
*Facet:* [`06_assets.asset_loading_pipeline`](#facet-06_assets.asset_loading_pipeline)

```{csv-table} asset_loading_pipeline
:header-rows: 1
:file: ./datasets/asset_loading_pipeline.csv
:widths: auto
```

### assets_index
*Facet:* [`06_assets.assets_index`](#facet-06_assets.assets_index)

```{csv-table} assets_index
:header-rows: 1
:file: ./datasets/assets_index.csv
:widths: auto
```

### compression_strategies
*Facet:* [`06_assets.compression_strategies`](#facet-06_assets.compression_strategies)

```{csv-table} compression_strategies
:header-rows: 1
:file: ./datasets/compression_strategies.csv
:widths: auto
```

### entities
*Facet:* [`06_assets.entities`](#facet-06_assets.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### optimization_techniques
*Facet:* [`06_assets.optimization_techniques`](#facet-06_assets.optimization_techniques)

```{csv-table} optimization_techniques
:header-rows: 1
:file: ./datasets/optimization_techniques.csv
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
click Architecture "./index.html#facet-06_assets.architecture" "Open architecture"
```

### asset_pipeline
*Facet:* [`06_assets.asset_pipeline`](#facet-06_assets.asset_pipeline)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    Request[Asset Request] --> Cache{In Cache?}
    Cache -->|Yes| Return[Return Cached Texture]
    Cache -->|No| Load[Load from Disk]
    
    Load --> Decode[Decode Image]
    Decode --> Upload[Upload to GPU]
    Upload --> Store[Store in Cache]
    Store --> Return
    
    Return --> Bind[Bind Texture]
    Bind --> Draw[Render]
    
    Load -.->|Async| Worker[Worker Thread]
    Worker -.-> Decode
    
    Upload --> Atlas{Use Atlas?}
    Atlas -->|Yes| Pack[Pack into Atlas]
    Atlas -->|No| Individual[Individual Texture]
    
    Pack --> Store
    Individual --> Store
    
    click Cache "./index.html#facet-06_assets.asset_loading_pipeline" "Loading Pipeline"
    click Atlas "./index.html#facet-06_assets.optimization_techniques" "Optimizations"
click AssetPipeline "./index.html#facet-06_assets.asset_pipeline" "Open asset_pipeline"
```

### assets_pipeline
*Facet:* [`06_assets.assets_pipeline`](#facet-06_assets.assets_pipeline)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  AEtPipeline[06_assets:assets_pipeline] --> Data[Datasets]
  Data --> Page[Index]

click AEtPipeline "./index.html#facet-06_assets.assets_pipeline" "Open assets_pipeline"
click AssetsPipeline "./index.html#facet-06_assets.assets_pipeline" "Open assets_pipeline"
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
click Flow "./index.html#facet-06_assets.flow" "Open flow"
```

### overview
*Facet:* [`06_assets.overview`](#facet-06_assets.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Assets Pipeline] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-06_assets.overview" "Open overview"
```

### pipeline_flow
*Facet:* [`06_assets.pipeline_flow`](#facet-06_assets.pipeline_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[06_assets.pipeline_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-06_assets.pipeline_flow" "Open pipeline_flow"
click PipelineFlow "./index.html#facet-06_assets.pipeline_flow" "Open pipeline_flow"
```

### texture_loading_sequence
*Facet:* [`06_assets.texture_loading_sequence`](#facet-06_assets.texture_loading_sequence)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
sequenceDiagram
    participant App as Application
    participant TM as TextureManager
    participant FS as FileSystem
    participant Decoder as ImageDecoder
    participant GPU as OpenGL
    participant Cache as TextureCache

    App->>TM: getTexture(path)
    TM->>Cache: lookup(path)
    
    alt Cache Hit
        Cache-->>TM: Return cached texture
        TM-->>App: Texture handle
    else Cache Miss
        TM->>FS: readFile(path)
        FS-->>TM: File bytes
        
        TM->>Decoder: decode(bytes)
        Decoder-->>TM: RGBA pixels
        
        TM->>GPU: glGenTextures()
        GPU-->>TM: Texture ID
        
        TM->>GPU: glBindTexture(ID)
        TM->>GPU: glTexImage2D(pixels)
        
        TM->>Cache: store(path, ID)
        TM-->>App: Texture handle
    end
    
    App->>TM: bindTexture(handle)
    TM->>GPU: glBindTexture(handle)
    
    App->>App: Render with texture
    %% click TextureLoadingSequence "./index.html#facet-06_assets.texture_loading_sequence" "Open texture_loading_sequence" %% REMOVED: click not supported in sequenceDiagram
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```

## Crosslinks

- **provides** → `10_game_runtime.resources` (evidence: `docs/authoring/10_game_runtime/datasets/resources.csv`)
- **used_by** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)

## Appendix / Facets

(facet-06_assets.architecture)=
### Facet: `06_assets.architecture`
Type: diagram

(facet-06_assets.asset_loading_pipeline)=
### Facet: `06_assets.asset_loading_pipeline`
Type: dataset

(facet-06_assets.asset_pipeline)=
### Facet: `06_assets.asset_pipeline`
Type: diagram

(facet-06_assets.assets_index)=
### Facet: `06_assets.assets_index`
Type: dataset

(facet-06_assets.assets_pipeline)=
### Facet: `06_assets.assets_pipeline`
Type: diagram

(facet-06_assets.compression_strategies)=
### Facet: `06_assets.compression_strategies`
Type: dataset

(facet-06_assets.entities)=
### Facet: `06_assets.entities`
Type: dataset

(facet-06_assets.flow)=
### Facet: `06_assets.flow`
Type: diagram

(facet-06_assets.optimization_techniques)=
### Facet: `06_assets.optimization_techniques`
Type: dataset

(facet-06_assets.overview)=
### Facet: `06_assets.overview`
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

(facet-06_assets.texture_loading_sequence)=
### Facet: `06_assets.texture_loading_sequence`
Type: diagram

