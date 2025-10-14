---
title: UI — OTUI widget hierarchy — export kit
---

# UI — OTUI widget hierarchy — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

### otui_files
*Facet:* [`04_ui.otui_files`](#facet-04_ui.otui_files)

```{csv-table} otui_files
:header-rows: 1
:file: ./datasets/otui_files.csv
:widths: auto
```

### signals
*Facet:* [`04_ui.signals`](#facet-04_ui.signals)

```{csv-table} signals
:header-rows: 1
:file: ./datasets/signals.csv
:widths: auto
```

### summary
*Facet:* [`04_ui.summary`](#facet-04_ui.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

### ui_widgets
*Facet:* [`04_ui.ui_widgets`](#facet-04_ui.ui_widgets)

```{csv-table} ui_widgets
:header-rows: 1
:file: ./datasets/ui_widgets.csv
:widths: auto
```

## Diagrams

### hierarchy
*Facet:* [`04_ui.hierarchy`](#facet-04_ui.hierarchy)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[04_ui.hierarchy] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-04_ui.hierarchy" "Open hierarchy"
```

### ui_flow
*Facet:* [`04_ui.ui_flow`](#facet-04_ui.ui_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[04_ui.ui_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-04_ui.ui_flow" "Open ui_flow"
```

## Cross-References

- **renders** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **emits** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **uses** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-04_ui.hierarchy)=
### Facet: `04_ui.hierarchy`
Type: diagram

(facet-04_ui.otui_files)=
### Facet: `04_ui.otui_files`
Type: dataset

(facet-04_ui.signals)=
### Facet: `04_ui.signals`
Type: dataset

(facet-04_ui.summary)=
### Facet: `04_ui.summary`
Type: dataset

(facet-04_ui.ui_flow)=
### Facet: `04_ui.ui_flow`
Type: diagram

(facet-04_ui.ui_widgets)=
### Facet: `04_ui.ui_widgets`
Type: dataset
