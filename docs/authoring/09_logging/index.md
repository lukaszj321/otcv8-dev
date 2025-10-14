---
title: 09_logging - Logging
---

# 09_logging - Logging

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`09_logging.entities`](#facet-09_logging.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `log_events.csv`
*Facet:* [`09_logging.log_events`](#facet-09_logging.log_events)

```{csv-table} log_events
:header-rows: 1
:file: ./datasets/log_events.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`09_logging.summary`](#facet-09_logging.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
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

#### `flow.mmd`
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

#### `logging_flow.mmd`
        *Facet:* [`09_logging.logging_flow`](#facet-09_logging.logging_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  LoggingFlow[09_logging:logging_flow] --> Data[Datasets]
  Data --> Page[Index]

click LoggingFlow "./index.html#facet-09_logging.logging_flow" "Open logging_flow"
        ```

## Appendix / Facets
(facet-09_logging.architecture)=
### Facet: `09_logging.architecture`
(facet-09_logging.entities)=
### Facet: `09_logging.entities`
(facet-09_logging.flow)=
### Facet: `09_logging.flow`
(facet-09_logging.log_events)=
### Facet: `09_logging.log_events`
(facet-09_logging.logging_flow)=
### Facet: `09_logging.logging_flow`
(facet-09_logging.summary)=
### Facet: `09_logging.summary`
