---
title: 03_modules - Modules
---

# 03_modules - Modules

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`03_modules.entities`](#facet-03_modules.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### hot_reload
*Facet:* [`03_modules.hot_reload`](#facet-03_modules.hot_reload)

```{csv-table} hot_reload
:header-rows: 1
:file: ./datasets/hot_reload.csv
:widths: auto
```

### lua_bindings_map
*Facet:* [`03_modules.lua_bindings_map`](#facet-03_modules.lua_bindings_map)

```{csv-table} lua_bindings_map
:header-rows: 1
:file: ./datasets/lua_bindings_map.csv
:widths: auto
```

### lua_exports
*Facet:* [`03_modules.lua_exports`](#facet-03_modules.lua_exports)

```{csv-table} lua_exports
:header-rows: 1
:file: ./datasets/lua_exports.csv
:widths: auto
```

### modules_index
*Facet:* [`03_modules.modules_index`](#facet-03_modules.modules_index)

```{csv-table} modules_index
:header-rows: 1
:file: ./datasets/modules_index.csv
:widths: auto
```

### summary
*Facet:* [`03_modules.summary`](#facet-03_modules.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`03_modules.architecture`](#facet-03_modules.architecture)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Lua Modules
        E0[Modules]
        E1[Exported Functions]
        E2[Callbacks]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-03_modules.architecture" "Open architecture"
```

### flow
*Facet:* [`03_modules.flow`](#facet-03_modules.flow)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Lua Modules] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-03_modules.flow" "Open flow"
```

### lua_cpp_binding_flow
*Facet:* [`03_modules.lua_cpp_binding_flow`](#facet-03_modules.lua_cpp_binding_flow)

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
sequenceDiagram
    participant Lua as Lua Code
    participant Bind as Lua Binding Layer
    participant CPP as C++ Class
    participant Core as Core API
    
    Note over Lua,Core: Example: g_sounds.play()
    
    Lua->>Bind: g_sounds.play("/sounds/alarm.ogg")
    Bind->>Bind: Lookup @bindsingleton g_sounds
    Bind->>CPP: SoundManager::play()
    CPP->>Core: OpenAL alSourcePlay()
    Core-->>CPP: Source handle
    CPP-->>Bind: SoundSourcePtr
    Bind-->>Lua: Return source object
    
    Note over Lua,Core: C++ to Lua Callback
    
    Core->>CPP: Log message event
    CPP->>Bind: Invoke OnLogCallback
    Bind->>Lua: Execute Lua callback
    Lua-->>Bind: Callback complete
    
    %% click Bind "../index.html#facet-03_modules.bindings" "Lua Bindings" %% REMOVED: click not supported in sequenceDiagram
    %% click LuaCppBindingFlow "./index.html#facet-03_modules.lua_cpp_binding_flow" "Open lua_cpp_binding_flow" %% REMOVED: click not supported in sequenceDiagram
```

### module_dependencies
*Facet:* [`03_modules.module_dependencies`](#facet-03_modules.module_dependencies)

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    subgraph "Core Libraries"
        CL[corelib]
        GL[gamelib]
    end
    
    subgraph "Client Modules"
        CO[client_options]
        CT[client_terminal]
        CM[client_mobile]
        CS[client_styles]
    end
    
    subgraph "Game Modules"
        GI[game_interface]
        GS[game_skills]
        GIN[game_inventory]
        GB[game_battle]
        GC[game_console]
        GBOT[game_bot]
    end
    
    CL --> CO
    CL --> CT
    CL --> GI
    GL --> GI
    GI --> GS
    GI --> GIN
    GI --> GB
    GI --> GC
    GI --> GBOT
    
    CO -.reload.-> CO
    GS -.reload.-> GS
    GIN -.reload.-> GIN
    GC -.reload.-> GC
    
    click GS "../index.html#facet-03_modules.lua_exports" "Lua Exports"
    click GBOT "../index.html#facet-03_modules.hot_reload" "Hot Reload"
click ModuleDependencies "./index.html#facet-03_modules.module_dependencies" "Open module_dependencies"
```

### modules_architecture
*Facet:* [`03_modules.modules_architecture`](#facet-03_modules.modules_architecture)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  ModuleArchitecture[03_modules:modules_architecture] --> Data[Datasets]
  Data --> Page[Index]

click ModuleArchitecture "./index.html#facet-03_modules.modules_architecture" "Open modules_architecture"
click ModulesArchitecture "./index.html#facet-03_modules.modules_architecture" "Open modules_architecture"
```

### modules_graph
*Facet:* [`03_modules.modules_graph`](#facet-03_modules.modules_graph)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[03_modules.modules_graph] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-03_modules.modules_graph" "Open modules_graph"
click ModulesGraph "./index.html#facet-03_modules.modules_graph" "Open modules_graph"
```

### overview
*Facet:* [`03_modules.overview`](#facet-03_modules.overview)

```mermaid
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Modules] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-03_modules.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
lua/index
```

## Crosslinks

- **uses** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)
- **handles** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **uses** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-03_modules.architecture)=
### Facet: `03_modules.architecture`
Type: diagram

(facet-03_modules.entities)=
### Facet: `03_modules.entities`
Type: dataset

(facet-03_modules.flow)=
### Facet: `03_modules.flow`
Type: diagram

(facet-03_modules.hot_reload)=
### Facet: `03_modules.hot_reload`
Type: dataset

(facet-03_modules.lua_bindings_map)=
### Facet: `03_modules.lua_bindings_map`
Type: dataset

(facet-03_modules.lua_cpp_binding_flow)=
### Facet: `03_modules.lua_cpp_binding_flow`
Type: diagram

(facet-03_modules.lua_exports)=
### Facet: `03_modules.lua_exports`
Type: dataset

(facet-03_modules.module_dependencies)=
### Facet: `03_modules.module_dependencies`
Type: diagram

(facet-03_modules.modules_architecture)=
### Facet: `03_modules.modules_architecture`
Type: diagram

(facet-03_modules.modules_graph)=
### Facet: `03_modules.modules_graph`
Type: diagram

(facet-03_modules.modules_index)=
### Facet: `03_modules.modules_index`
Type: dataset

(facet-03_modules.overview)=
### Facet: `03_modules.overview`
Type: diagram

(facet-03_modules.summary)=
### Facet: `03_modules.summary`
Type: dataset

