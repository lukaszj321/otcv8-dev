---
title: 02_events - Events
---

# 02_events - Events

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`02_events.entities`](#facet-02_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `events_matrix.csv`
*Facet:* [`02_events.events_matrix`](#facet-02_events.events_matrix)

```{csv-table} events_matrix
:header-rows: 1
:file: ./datasets/events_matrix.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`02_events.summary`](#facet-02_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
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

#### `event_flow.mmd`
        *Facet:* [`02_events.event_flow`](#facet-02_events.event_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventFlow[02_events:event_flow] --> Data[Datasets]
  Data --> Page[Index]

click EventFlow "./index.html#facet-02_events.event_flow" "Open event_flow"
        ```

#### `flow.mmd`
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

## Appendix / Facets
(facet-02_events.architecture)=
### Facet: `02_events.architecture`
(facet-02_events.entities)=
### Facet: `02_events.entities`
(facet-02_events.event_flow)=
### Facet: `02_events.event_flow`
(facet-02_events.events_matrix)=
### Facet: `02_events.events_matrix`
(facet-02_events.flow)=
### Facet: `02_events.flow`
(facet-02_events.summary)=
### Facet: `02_events.summary`
