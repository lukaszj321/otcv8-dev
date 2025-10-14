---
title: 01_core - Core
---

# 01_core - Core

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
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
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  Architecture[01_core:architecture] --> Data[Datasets]
  Data --> Page[Index]

click Architecture "./index.html#facet-01_core.architecture" "Open architecture"
        ```

### flow
        *Facet:* [`01_core.flow`](#facet-01_core.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Core API] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
api/index
```

## Crosslinks

- **uses** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **renders** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)
- **emits** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-01_core.architecture)=
### Facet: `01_core.architecture`
Type: diagram

(facet-01_core.cpp_headers)=
### Facet: `01_core.cpp_headers`
Type: dataset

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

(facet-01_core.lua_bindings)=
### Facet: `01_core.lua_bindings`
Type: dataset

(facet-01_core.summary)=
### Facet: `01_core.summary`
Type: dataset

