---
title: Logging system — export kit
---

# Logging system — export kit

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

## Cross-References

- **observes** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **observes** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-09_logging.emitters)=
### Facet: `09_logging.emitters`
Type: dataset

(facet-09_logging.flow)=
### Facet: `09_logging.flow`
Type: diagram

(facet-09_logging.logging_categories)=
### Facet: `09_logging.logging_categories`
Type: dataset

(facet-09_logging.sinks)=
### Facet: `09_logging.sinks`
Type: dataset

(facet-09_logging.summary)=
### Facet: `09_logging.summary`
Type: dataset
