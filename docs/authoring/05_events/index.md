---
title: 05_events - Events
---

# 05_events - Events

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`05_events.entities`](#facet-05_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `events_details.csv`
*Facet:* [`05_events.events_details`](#facet-05_events.events_details)

```{csv-table} events_details
:header-rows: 1
:file: ./datasets/events_details.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`05_events.summary`](#facet-05_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
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
        ```

#### `events_overview.mmd`
        *Facet:* [`05_events.events_overview`](#facet-05_events.events_overview)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventOverview[05_events:events_overview] --> Data[Datasets]
  Data --> Page[Index]

click EventOverview "./index.html#facet-05_events.events_overview" "Open events_overview"
        ```

#### `flow.mmd`
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
        ```

## Appendix / Facets
(facet-05_events.architecture)=
### Facet: `05_events.architecture`
(facet-05_events.entities)=
### Facet: `05_events.entities`
(facet-05_events.events_details)=
### Facet: `05_events.events_details`
(facet-05_events.events_overview)=
### Facet: `05_events.events_overview`
(facet-05_events.flow)=
### Facet: `05_events.flow`
(facet-05_events.summary)=
### Facet: `05_events.summary`
