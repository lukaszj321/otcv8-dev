---
title: 09_logging - Logging
---

# 09_logging - Logging

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### emitters
*Facet:* [`09_logging.emitters`](#facet-09_logging.emitters)

```{csv-table} emitters
:header-rows: 1
:file: ./datasets/emitters.csv
:widths: auto
```

### entities
*Facet:* [`09_logging.entities`](#facet-09_logging.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### log_events
*Facet:* [`09_logging.log_events`](#facet-09_logging.log_events)

```{csv-table} log_events
:header-rows: 1
:file: ./datasets/log_events.csv
:widths: auto
```

### logging_categories
*Facet:* [`09_logging.logging_categories`](#facet-09_logging.logging_categories)

```{csv-table} logging_categories
:header-rows: 1
:file: ./datasets/logging_categories.csv
:widths: auto
```

### sinks
*Facet:* [`09_logging.sinks`](#facet-09_logging.sinks)

```{csv-table} sinks
:header-rows: 1
:file: ./datasets/sinks.csv
:widths: auto
```

### summary
*Facet:* [`09_logging.summary`](#facet-09_logging.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
        *Facet:* [`09_logging.architecture`](#facet-09_logging.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Logging
        E0[Log Entries]
        E1[Log Levels]
        E2[Log Sources]
        E0 --> E1
        E1 --> E2
    end
        ```

### flow
        *Facet:* [`09_logging.flow`](#facet-09_logging.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Logging] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

### logging_flow
        *Facet:* [`09_logging.logging_flow`](#facet-09_logging.logging_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  LoggingFlow[09_logging:logging_flow] --> Data[Datasets]
  Data --> Page[Index]

click LoggingFlow "./index.html#facet-09_logging.logging_flow" "Open logging_flow"
        ```



## Crosslinks

- **observes** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **observes** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-09_logging.architecture)=
### Facet: `09_logging.architecture`
Type: diagram

(facet-09_logging.emitters)=
### Facet: `09_logging.emitters`
Type: dataset

(facet-09_logging.entities)=
### Facet: `09_logging.entities`
Type: dataset

(facet-09_logging.flow)=
### Facet: `09_logging.flow`
Type: diagram

(facet-09_logging.log_events)=
### Facet: `09_logging.log_events`
Type: dataset

(facet-09_logging.logging_categories)=
### Facet: `09_logging.logging_categories`
Type: dataset

(facet-09_logging.logging_flow)=
### Facet: `09_logging.logging_flow`
Type: diagram

(facet-09_logging.sinks)=
### Facet: `09_logging.sinks`
Type: dataset

(facet-09_logging.summary)=
### Facet: `09_logging.summary`
Type: dataset

