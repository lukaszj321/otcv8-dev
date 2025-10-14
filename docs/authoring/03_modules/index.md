---
title: Lua modules — export kit
---

# Lua modules — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

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

### modules_graph
*Facet:* [`03_modules.modules_graph`](#facet-03_modules.modules_graph)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[03_modules.modules_graph] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-03_modules.modules_graph" "Open modules_graph"
```

## Cross-References

- **renders** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)
- **handles** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-03_modules.hot_reload)=
### Facet: `03_modules.hot_reload`
Type: dataset

(facet-03_modules.lua_exports)=
### Facet: `03_modules.lua_exports`
Type: dataset

(facet-03_modules.modules_graph)=
### Facet: `03_modules.modules_graph`
Type: diagram

(facet-03_modules.modules_index)=
### Facet: `03_modules.modules_index`
Type: dataset

(facet-03_modules.summary)=
### Facet: `03_modules.summary`
Type: dataset
