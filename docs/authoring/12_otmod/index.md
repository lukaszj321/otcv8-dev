---
title: 12_otmod - Otmod
---

# 12_otmod - Otmod

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### lua_exports
*Facet:* [`12_otmod.lua_exports`](#facet-12_otmod.lua_exports)

```{csv-table} lua_exports
:header-rows: 1
:file: ./datasets/lua_exports.csv
:widths: auto
```

### module_deps
*Facet:* [`12_otmod.module_deps`](#facet-12_otmod.module_deps)

```{csv-table} module_deps
:header-rows: 1
:file: ./datasets/module_deps.csv
:widths: auto
```

### module_hooks
*Facet:* [`12_otmod.module_hooks`](#facet-12_otmod.module_hooks)

```{csv-table} module_hooks
:header-rows: 1
:file: ./datasets/module_hooks.csv
:widths: auto
```

### module_scripts
*Facet:* [`12_otmod.module_scripts`](#facet-12_otmod.module_scripts)

```{csv-table} module_scripts
:header-rows: 1
:file: ./datasets/module_scripts.csv
:widths: auto
```

### module_ui_links
*Facet:* [`12_otmod.module_ui_links`](#facet-12_otmod.module_ui_links)

```{csv-table} module_ui_links
:header-rows: 1
:file: ./datasets/module_ui_links.csv
:widths: auto
```

### modules_index
*Facet:* [`12_otmod.modules_index`](#facet-12_otmod.modules_index)

```{csv-table} modules_index
:header-rows: 1
:file: ./datasets/modules_index.csv
:widths: auto
```

### otmod_packages
*Facet:* [`12_otmod.otmod_packages`](#facet-12_otmod.otmod_packages)

```{csv-table} otmod_packages
:header-rows: 1
:file: ./datasets/otmod_packages.csv
:widths: auto
```

### summary
*Facet:* [`12_otmod.summary`](#facet-12_otmod.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### deps
*Facet:* [`12_otmod.deps`](#facet-12_otmod.deps)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Module A] --> B[Module B]
    A --> C[Module C]
    click A "./index.html#facet-12_otmod.modules_index" "Open modules index"
click Deps "./index.html#facet-12_otmod.deps" "Open deps"
```

### deps_graph
*Facet:* [`12_otmod.deps_graph`](#facet-12_otmod.deps_graph)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  game_interface --> game_skills
  game_interface --> game_inventory
  game_interface --> game_console
  game_skills --> game_stats
click DepsGraph "./index.html#facet-12_otmod.deps_graph" "Open deps_graph"
```

### lifecycle
*Facet:* [`12_otmod.lifecycle`](#facet-12_otmod.lifecycle)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
sequenceDiagram
  participant L as Loader
  participant M as Module(OTMOD)
  participant S as Scripts(Lua)
  L->>M: load()
  M->>S: scripts[] bootstrap
  M->>S: @onLoad -> init()
  S-->>M: ready()
  L->>M: unload()
  M->>S: @onUnload -> terminate()
    %% click Lifecycle "./index.html#facet-12_otmod.lifecycle" "Open lifecycle" %% REMOVED: click not supported in sequenceDiagram
```

### module_lifecycle
*Facet:* [`12_otmod.module_lifecycle`](#facet-12_otmod.module_lifecycle)

```mermaid
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant Client as OTClient Core
    participant Loader as Module Loader
    participant Sandbox as Sandbox Layer
    participant Module as User Module
    participant Game as Game Interface
    
    Note over Client,Game: Module Loading Phase
    Client->>Loader: Load modules
    Loader->>Loader: Parse manifests
    Loader->>Loader: Resolve dependencies
    
    Note over Loader: Phase 1: Core Modules
    Loader->>Module: Load core modules (sandboxed=false)
    Module-->>Loader: Initialized
    
    Note over Loader: Phase 2: Regular Modules
    Loader->>Sandbox: Create sandbox environment
    Sandbox->>Module: Load module (sandboxed=true)
    Module->>Module: init()
    Module-->>Sandbox: Initialized
    Sandbox-->>Loader: Success
    
    Note over Loader: Phase 3: Load-Later Modules
    Loader->>Game: Wait for game interface
    Game-->>Loader: Interface ready
    Loader->>Sandbox: Load load-later modules
    Sandbox->>Module: Load with dependencies ready
    Module->>Module: init()
    Module->>Game: Register extensions
    Module-->>Loader: Complete
    
    Note over Client,Game: Runtime Phase
    Game->>Module: Fire events
    Module->>Sandbox: Call approved APIs
    Sandbox->>Sandbox: Validate permissions
    Sandbox-->>Module: Result
    
    Note over Client,Game: Unload Phase
    Client->>Loader: Shutdown
    Loader->>Module: terminate()
    Module->>Module: Cleanup
    Module-->>Loader: Unloaded
    %% click ModuleLifecycle "./index.html#facet-12_otmod.module_lifecycle" "Open module_lifecycle" %% REMOVED: click not supported in sequenceDiagram
```

### modules_deps
*Facet:* [`12_otmod.modules_deps`](#facet-12_otmod.modules_deps)

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    MOD["Module<br/>(*.otmod)"] --> MANIFEST["Manifest<br/>dependencies<br/>load-later"]
    MOD --> LUA["Lua Scripts<br/>(*.lua)"]
    MOD --> OTUI["UI Files<br/>(*.otui)"]
    
    MANIFEST --> DEPS["Module Dependencies<br/>module_deps.csv"]
    LUA --> EXPORTS["Lua Exports<br/>lua_exports.csv"]
    LUA --> HOOKS["Hooks<br/>@onLoad/@onUnload"]
    OTUI --> UILINKS["UI Links<br/>module_ui_links.csv"]
    
    HOOKS --> LIFECYCLE["Module Lifecycle"]
    
    DEPS --> INDEX["Modules Index<br/>modules_index.csv"]
    EXPORTS --> INDEX
    UILINKS --> INDEX
    
    click INDEX "../12_otmod/index.html#facet-12_otmod.main" "Open OTMOD Index"
    click DEPS "../12_otmod/index.html#facet-12_otmod.module_deps" "Open Module Dependencies"
click ModulesDeps "./index.html#facet-12_otmod.modules_deps" "Open modules_deps"
```

### overview
*Facet:* [`12_otmod.overview`](#facet-12_otmod.overview)

```mermaid
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[OTMOD Packages] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-12_otmod.overview" "Open overview"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```



## Appendix / Facets

(facet-12_otmod.deps)=
### Facet: `12_otmod.deps`
Type: diagram

(facet-12_otmod.deps_graph)=
### Facet: `12_otmod.deps_graph`
Type: diagram

(facet-12_otmod.lifecycle)=
### Facet: `12_otmod.lifecycle`
Type: diagram

(facet-12_otmod.lua_exports)=
### Facet: `12_otmod.lua_exports`
Type: dataset

(facet-12_otmod.module_deps)=
### Facet: `12_otmod.module_deps`
Type: dataset

(facet-12_otmod.module_hooks)=
### Facet: `12_otmod.module_hooks`
Type: dataset

(facet-12_otmod.module_lifecycle)=
### Facet: `12_otmod.module_lifecycle`
Type: diagram

(facet-12_otmod.module_scripts)=
### Facet: `12_otmod.module_scripts`
Type: dataset

(facet-12_otmod.module_ui_links)=
### Facet: `12_otmod.module_ui_links`
Type: dataset

(facet-12_otmod.modules_deps)=
### Facet: `12_otmod.modules_deps`
Type: diagram

(facet-12_otmod.modules_index)=
### Facet: `12_otmod.modules_index`
Type: dataset

(facet-12_otmod.otmod_packages)=
### Facet: `12_otmod.otmod_packages`
Type: dataset

(facet-12_otmod.overview)=
### Facet: `12_otmod.overview`
Type: diagram

(facet-12_otmod.summary)=
### Facet: `12_otmod.summary`
Type: dataset

