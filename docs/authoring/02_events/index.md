---
title: Event system and signals — export kit
---

# Event system and signals — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

### emitters
*Facet:* [`02_events.emitters`](#facet-02_events.emitters)

```{csv-table} emitters
:header-rows: 1
:file: ./datasets/emitters.csv
:widths: auto
```

### events_matrix
*Facet:* [`02_events.events_matrix`](#facet-02_events.events_matrix)

```{csv-table} events_matrix
:header-rows: 1
:file: ./datasets/events_matrix.csv
:widths: auto
```

### handlers
*Facet:* [`02_events.handlers`](#facet-02_events.handlers)

```{csv-table} handlers
:header-rows: 1
:file: ./datasets/handlers.csv
:widths: auto
```

### summary
*Facet:* [`02_events.summary`](#facet-02_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams

### bus
*Facet:* [`02_events.bus`](#facet-02_events.bus)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[02_events.bus] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-02_events.bus" "Open bus"
```

### propagation
*Facet:* [`02_events.propagation`](#facet-02_events.propagation)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[02_events.propagation] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-02_events.propagation" "Open propagation"
```

## Cross-References

- **handled_by** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **emits** → `04_ui.signals` (evidence: `docs/authoring/04_ui/datasets/signals.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-02_events.bus)=
### Facet: `02_events.bus`
Type: diagram

(facet-02_events.emitters)=
### Facet: `02_events.emitters`
Type: dataset

(facet-02_events.events_matrix)=
### Facet: `02_events.events_matrix`
Type: dataset

(facet-02_events.handlers)=
### Facet: `02_events.handlers`
Type: dataset

(facet-02_events.propagation)=
### Facet: `02_events.propagation`
Type: diagram

(facet-02_events.summary)=
### Facet: `02_events.summary`
Type: dataset
