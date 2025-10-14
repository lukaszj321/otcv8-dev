---
title: 03_modules - Modules
---

# 03_modules - Modules

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`03_modules.entities`](#facet-03_modules.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `lua_exports.csv`
*Facet:* [`03_modules.lua_exports`](#facet-03_modules.lua_exports)

```{csv-table} lua_exports
:header-rows: 1
:file: ./datasets/lua_exports.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`03_modules.summary`](#facet-03_modules.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
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

#### `flow.mmd`
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

#### `modules_architecture.mmd`
        *Facet:* [`03_modules.modules_architecture`](#facet-03_modules.modules_architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  ModuleArchitecture[03_modules:modules_architecture] --> Data[Datasets]
  Data --> Page[Index]

click ModuleArchitecture "./index.html#facet-03_modules.modules_architecture" "Open modules_architecture"
        ```

## Appendix / Facets
(facet-03_modules.architecture)=
### Facet: `03_modules.architecture`
(facet-03_modules.entities)=
### Facet: `03_modules.entities`
(facet-03_modules.flow)=
### Facet: `03_modules.flow`
(facet-03_modules.lua_exports)=
### Facet: `03_modules.lua_exports`
(facet-03_modules.modules_architecture)=
### Facet: `03_modules.modules_architecture`
(facet-03_modules.summary)=
### Facet: `03_modules.summary`
