---
doc_id: 06_assets
source_path: docs/authoring/06_assets
source_sha: f715219
last_sync_iso: "2025-10-18T01:36:41.411736Z"
doc_class: guide
language: pl
title: 06 - Assets Pipeline
---


# 06 - Assets Pipeline

Asset atlas, versioning, compression, and differences from data chapter.

## Przegląd

Ten rozdział dokumentuje 06 assets w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
blueprints/index
datasets/index
diagrams/index
```

## Assets vs Data Chapter Distinction

**This chapter (06_assets)** focuses on the **technical pipeline** for loading, processing, and optimizing assets (textures, sprites, sounds).

**Chapter 11_data** documents the **inventory and organization** of actual asset files in `data/**` and their usage in OTUI files.

### Key Differences

| Aspect | 06_assets (this chapter) | 11_data |
|--------|-------------------------|---------|
| Focus | Pipeline, loading, optimization | File inventory, usage tracking |
| Content | Technical implementation | Asset catalog, cross-references |
| Datasets | Loading stages, compression | Asset lists, UI usage links |
| Use Case | Developers optimizing performance | Developers finding/using assets |

## Asset Loading Pipeline

The asset pipeline processes files from disk to GPU in multiple stages:

1. **File I/O** - Read binary data from `data/` or `layouts/`
2. **Decoding** - Decompress PNG/JPG/OGG to raw format
3. **GPU Upload** - Transfer to video memory via OpenGL
4. **Caching** - Store texture handles to prevent reloading
5. **Atlas Packing** - Combine sprites into larger textures
6. **Binding** - Activate texture for rendering
7. **Drawing** - Use in actual render calls

### Performance Characteristics

- **Cache hit**: ~0.001ms (hash lookup)
- **Disk load + decode**: 5-50ms depending on size
- **GPU upload**: 1-10ms depending on size
- **Atlas benefit**: 50-90% reduction in draw calls

## Compression Strategies

Different asset types benefit from different compression approaches:

### Images
- **UI elements**: PNG (lossless, exact colors)
- **Backgrounds**: PNG or high-quality JPG
- **Sprites**: PNG in texture atlas

### Audio
- **Music**: OGG Vorbis (10-20x compression)
- **Sound effects**: WAV (uncompressed, low latency)

### Advanced Techniques
- **Spritesheet packing**: Combine multiple sprites
- **Mipmapping**: Generate LOD chain for distance rendering
- **POT sizing**: Use power-of-2 dimensions for compatibility

## Optimization Techniques

Key strategies for asset optimization:

### Texture Atlas Generation
Combine multiple small sprites into larger textures to reduce:
- OpenGL state changes
- Draw call overhead
- Texture binding costs

Example: 100 sprites in 10 atlases = ~90% fewer draw calls

### Lazy Loading
Load assets on-demand rather than at startup:
- Faster initial load time
- Lower memory footprint
- Eliminate loading stutters with async loading

### Memory Management
- **Reference counting**: Automatic cleanup when unused
- **Resource pools**: Reuse texture objects
- **Unloading**: Free textures when switching areas

## Datasets

```{csv-table} Asset Loading Pipeline
:header-rows: 1
:file: ./datasets/asset_loading_pipeline.csv
```

```{csv-table} Compression Strategies Comparison
:header-rows: 1
:file: ./datasets/compression_strategies.csv
```

```{csv-table} Optimization Techniques
:header-rows: 1
:file: ./datasets/optimization_techniques.csv
```

Legacy datasets:
- `assets_index.csv`
- `entities.csv`
- `pipelines.csv`
- `spritesheets.csv`
- `summary.csv`

## Diagrams

```{mermaid}
:caption: Asset Pipeline Flowchart
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
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
```

```{mermaid}
:caption: Texture Loading Sequence
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
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
```

```{contents}
:local:
:depth: 2
```

## Crosslinks

Internal references:
- [Data](../11_data/index.md) - Asset inventory and file organization
- [UI](../04_ui/index.md) - UI widget image properties
- [Layouts](../13_layouts/index.md) - Layout-specific asset overrides
- [Game Runtime](../10_game_runtime/index.md) - Rendering integration
- [Core API](../01_core/index.md) - C++ texture management classes
- [Runtime](../01_runtime/index.md) - Async loading with AsyncDispatcher

External source files:
- `src/framework/graphics/texturemanager.cpp` - Texture cache and loading
- `src/framework/graphics/texture.cpp` - Texture class implementation
- `src/client/spritemanager.cpp` - Sprite atlas management
- `src/framework/graphics/image.cpp` - Image decoding


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.411736Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-06_assets.main)=
### Facet: `06_assets.main`

Main documentation facet for 06_assets.

(facet-06_assets.asset_loading_pipeline)=
### Facet: `06_assets.asset_loading_pipeline`

Complete asset loading pipeline from disk I/O through GPU upload, including caching, atlas packing, and performance characteristics for each stage.

(facet-06_assets.compression_strategies)=
### Facet: `06_assets.compression_strategies`

Compression strategy comparison for different asset types (PNG, JPG, OGG, etc.) including compression ratios, quality trade-offs, and recommendations.

(facet-06_assets.optimization_techniques)=
### Facet: `06_assets.optimization_techniques`

Asset optimization techniques including texture atlasing, lazy loading, memory management, and performance impact analysis.