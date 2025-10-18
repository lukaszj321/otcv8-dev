---
title: 05_events - Events
---

# 05_events - Events

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`05_events.entities`](#facet-05_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### events_details
*Facet:* [`05_events.events_details`](#facet-05_events.events_details)

```{csv-table} events_details
:header-rows: 1
:file: ./datasets/events_details.csv
:widths: auto
```

### summary
*Facet:* [`05_events.summary`](#facet-05_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`05_events.architecture`](#facet-05_events.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Event Details
        E0[Event Patterns]
        E1[Event Chains]
        E2[Event Handlers]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-05_events.architecture" "Open architecture"
```

### events_overview
*Facet:* [`05_events.events_overview`](#facet-05_events.events_overview)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventOverview[05_events:events_overview] --> Data[Datasets]
  Data --> Page[Index]

click EventOverview "./index.html#facet-05_events.events_overview" "Open events_overview"
click EventsOverview "./index.html#facet-05_events.events_overview" "Open events_overview"
```

### flow
*Facet:* [`05_events.flow`](#facet-05_events.flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Event Details] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-05_events.flow" "Open flow"
```





## Appendix / Facets

(facet-05_events.architecture)=
### Facet: `05_events.architecture`
Type: diagram

(facet-05_events.entities)=
### Facet: `05_events.entities`
Type: dataset

(facet-05_events.events_details)=
### Facet: `05_events.events_details`
Type: dataset

(facet-05_events.events_overview)=
### Facet: `05_events.events_overview`
Type: diagram

(facet-05_events.flow)=
### Facet: `05_events.flow`
Type: diagram

(facet-05_events.summary)=
### Facet: `05_events.summary`
Type: dataset

