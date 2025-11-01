---
title: 01_core - Core
---

# 01_core - Core

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### cpp_api_map
*Facet:* [`01_core.cpp_api_map`](#facet-01_core.cpp_api_map)

```{csv-table} cpp_api_map
:header-rows: 1
:file: ./datasets/cpp_api_map.csv
:widths: auto
```

### cpp_headers
*Facet:* [`01_core.cpp_headers`](#facet-01_core.cpp_headers)

```{csv-table} cpp_headers
:header-rows: 1
:file: ./datasets/cpp_headers.csv
:widths: auto
```

### cpp_symbols
*Facet:* [`01_core.cpp_symbols`](#facet-01_core.cpp_symbols)

```{csv-table} cpp_symbols
:header-rows: 1
:file: ./datasets/cpp_symbols.csv
:widths: auto
```

### entities
*Facet:* [`01_core.entities`](#facet-01_core.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### headers
*Facet:* [`01_core.headers`](#facet-01_core.headers)

```{csv-table} headers
:header-rows: 1
:file: ./datasets/headers.csv
:widths: auto
```

### lua_bindings
*Facet:* [`01_core.lua_bindings`](#facet-01_core.lua_bindings)

```{csv-table} lua_bindings
:header-rows: 1
:file: ./datasets/lua_bindings.csv
:widths: auto
```

### summary
*Facet:* [`01_core.summary`](#facet-01_core.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`01_core.architecture`](#facet-01_core.architecture)

```{mermaid}
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    Core[Core Framework] --> Graphics[Graphics System]
    Core --> UI[UI System]
    Core --> Net[Network Layer]
    Core --> Sound[Sound System]
    Graphics --> OpenGL[OpenGL/GLES]
    UI --> Widgets[Widget Tree]
    Net --> Protocol[Protocol Handler]
click Architecture "./index.html#facet-01_core.architecture" "Open architecture"
```

### cpp_singleton_hierarchy
*Facet:* [`01_core.cpp_singleton_hierarchy`](#facet-01_core.cpp_singleton_hierarchy)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    subgraph "Core Singletons"
        APP[g_app Application]
        LOG[g_logger Logger]
        CLK[g_clock Clock]
        DISP[g_dispatcher EventDispatcher]
        RES[g_resources ResourceManager]
        MOD[g_modules ModuleManager]
        CFG[g_configs ConfigManager]
    end
    
    subgraph "Graphics Singletons"
        GFX[g_graphics Graphics]
        FONT[g_fonts FontManager]
        SHDR[g_shaders ShaderManager]
        WIN[g_window PlatformWindow]
    end
    
    subgraph "Audio Singletons"
        SND[g_sounds SoundManager]
    end
    
    subgraph "UI Singletons"
        UI[g_ui UIManager]
    end
    
    subgraph "Game Singletons"
        GAME[g_game Game]
        MAP[g_map Map]
    end
    
    APP --> LOG
    APP --> CLK
    APP --> DISP
    APP --> RES
    APP --> MOD
    
    GFX --> FONT
    GFX --> SHDR
    GFX --> WIN
    
    GAME --> MAP
    
    click APP "../index.html#facet-01_core.singletons" "Core Singletons"
    click GAME "../index.html#facet-01_core.game_api" "Game API"
click CppSingletonHierarchy "./index.html#facet-01_core.cpp_singleton_hierarchy" "Open cpp_singleton_hierarchy"
```

### flow
*Facet:* [`01_core.flow`](#facet-01_core.flow)

```{mermaid}
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Core API] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-01_core.flow" "Open flow"
```

### lua_binding_sequence
*Facet:* [`01_core.lua_binding_sequence`](#facet-01_core.lua_binding_sequence)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant Lua as Lua Script
    participant Bind as Binding Layer
    participant Sing as C++ Singleton
    participant Impl as Implementation
    
    Note over Lua,Impl: Singleton Method Call
    
    Lua->>Bind: g_logger.info("message")
    Bind->>Bind: Resolve g_logger singleton
    Bind->>Sing: Logger::info()
    Sing->>Impl: log(LogInfo, message)
    Impl->>Impl: Write to file/console
    Impl-->>Sing: Complete
    Sing-->>Bind: void
    Bind-->>Lua: Return
    
    Note over Lua,Impl: Class Instance Method
    
    Lua->>Bind: channel:setGain(0.8)
    Bind->>Bind: Resolve SoundChannel instance
    Bind->>Sing: SoundChannel::setGain()
    Sing->>Impl: m_gain = 0.8
    Sing->>Impl: Update OpenAL source
    Impl-->>Sing: Complete
    Sing-->>Bind: void
    Bind-->>Lua: Return
    
    %% click Bind "../index.html#facet-01_core.bindings_flow" "Binding Flow" %% REMOVED: click not supported in sequenceDiagram
    %% click LuaBindingSequence "./index.html#facet-01_core.lua_binding_sequence" "Open lua_binding_sequence" %% REMOVED: click not supported in sequenceDiagram
```

### overview
*Facet:* [`01_core.overview`](#facet-01_core.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Core C++ API] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-01_core.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
api/index
blueprints/index
```



## Appendix / Facets

(facet-01_core.architecture)=
### Facet: `01_core.architecture`
Type: diagram

(facet-01_core.cpp_api_map)=
### Facet: `01_core.cpp_api_map`
Type: dataset

(facet-01_core.cpp_headers)=
### Facet: `01_core.cpp_headers`
Type: dataset

(facet-01_core.cpp_singleton_hierarchy)=
### Facet: `01_core.cpp_singleton_hierarchy`
Type: diagram

(facet-01_core.cpp_symbols)=
### Facet: `01_core.cpp_symbols`
Type: dataset

(facet-01_core.entities)=
### Facet: `01_core.entities`
Type: dataset

(facet-01_core.flow)=
### Facet: `01_core.flow`
Type: diagram

(facet-01_core.headers)=
### Facet: `01_core.headers`
Type: dataset

(facet-01_core.lua_binding_sequence)=
### Facet: `01_core.lua_binding_sequence`
Type: diagram

(facet-01_core.lua_bindings)=
### Facet: `01_core.lua_bindings`
Type: dataset

(facet-01_core.overview)=
### Facet: `01_core.overview`
Type: diagram

(facet-01_core.summary)=
### Facet: `01_core.summary`
Type: dataset

