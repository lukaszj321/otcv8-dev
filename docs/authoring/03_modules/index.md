---
title: 03_modules - Modules
---

# 03_modules - Modules

metadane modulow (.otmod), w tym nazwa, autor, flagi (reloadable, sandboxed), listy skryptow i hookow, oraz relacje do UI i runtime.

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

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Lua Modules
        E0[Modules]
        E1[Exported Functions]
        E2[Callbacks]
        E0 --> E1
        E1 --> E2
    end
        ```

### flow
        *Facet:* [`03_modules.flow`](#facet-03_modules.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Lua Modules] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

### modules_architecture
        *Facet:* [`03_modules.modules_architecture`](#facet-03_modules.modules_architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  ModuleArchitecture[03_modules:modules_architecture] --> Data[Datasets]
  Data --> Page[Index]

click ModuleArchitecture "./index.html#facet-03_modules.modules_architecture" "Open modules_architecture"
        ```

### modules_graph
        *Facet:* [`03_modules.modules_graph`](#facet-03_modules.modules_graph)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[03_modules.modules_graph] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-03_modules.modules_graph" "Open modules_graph"
        ```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
lua/index
```

## Crosslinks

- **renders** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)
- **handles** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

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

(facet-03_modules.lua_exports)=
### Facet: `03_modules.lua_exports`
Type: dataset

(facet-03_modules.modules_architecture)=
### Facet: `03_modules.modules_architecture`
Type: diagram

(facet-03_modules.modules_graph)=
### Facet: `03_modules.modules_graph`
Type: diagram

(facet-03_modules.modules_index)=
### Facet: `03_modules.modules_index`
Type: dataset

(facet-03_modules.summary)=
### Facet: `03_modules.summary`
Type: dataset

