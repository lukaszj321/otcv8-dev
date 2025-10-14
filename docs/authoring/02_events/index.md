---
title: 02_events - Events
---

# 02_events - Events

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

### entities
*Facet:* [`02_events.entities`](#facet-02_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
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
### architecture
        *Facet:* [`02_events.architecture`](#facet-02_events.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Events
        E0[Event Types]
        E1[Signal Handlers]
        E2[Event Sequences]
        E0 --> E1
        E1 --> E2
    end
        ```

### bus
        *Facet:* [`02_events.bus`](#facet-02_events.bus)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[02_events.bus] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-02_events.bus" "Open bus"
        ```

### event_flow
        *Facet:* [`02_events.event_flow`](#facet-02_events.event_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventFlow[02_events:event_flow] --> Data[Datasets]
  Data --> Page[Index]

click EventFlow "./index.html#facet-02_events.event_flow" "Open event_flow"
        ```

### flow
        *Facet:* [`02_events.flow`](#facet-02_events.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Events] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
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



## Crosslinks

- **handled_by** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **emits** → `04_ui.signals` (evidence: `docs/authoring/04_ui/datasets/signals.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-02_events.architecture)=
### Facet: `02_events.architecture`
Type: diagram

(facet-02_events.bus)=
### Facet: `02_events.bus`
Type: diagram

(facet-02_events.emitters)=
### Facet: `02_events.emitters`
Type: dataset

(facet-02_events.entities)=
### Facet: `02_events.entities`
Type: dataset

(facet-02_events.event_flow)=
### Facet: `02_events.event_flow`
Type: diagram

(facet-02_events.events_matrix)=
### Facet: `02_events.events_matrix`
Type: dataset

(facet-02_events.flow)=
### Facet: `02_events.flow`
Type: diagram

(facet-02_events.handlers)=
### Facet: `02_events.handlers`
Type: dataset

(facet-02_events.propagation)=
### Facet: `02_events.propagation`
Type: diagram

(facet-02_events.summary)=
### Facet: `02_events.summary`
Type: dataset

