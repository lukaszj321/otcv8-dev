---
title: 10_game_runtime - Game runtime
---

# 10_game_runtime - Game runtime

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`10_game_runtime.entities`](#facet-10_game_runtime.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `game_state.csv`
*Facet:* [`10_game_runtime.game_state`](#facet-10_game_runtime.game_state)

```{csv-table} game_state
:header-rows: 1
:file: ./datasets/game_state.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`10_game_runtime.summary`](#facet-10_game_runtime.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`10_game_runtime.architecture`](#facet-10_game_runtime.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Game Runtime
        E0[Game State]
        E1[Player Stats]
        E2[Runtime Events]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `flow.mmd`
        *Facet:* [`10_game_runtime.flow`](#facet-10_game_runtime.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Game Runtime] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

#### `runtime_loop.mmd`
        *Facet:* [`10_game_runtime.runtime_loop`](#facet-10_game_runtime.runtime_loop)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  RuntimeLoop[10_game_runtime:runtime_loop] --> Data[Datasets]
  Data --> Page[Index]

click RuntimeLoop "./index.html#facet-10_game_runtime.runtime_loop" "Open runtime_loop"
        ```

## Appendix / Facets
(facet-10_game_runtime.architecture)=
### Facet: `10_game_runtime.architecture`
(facet-10_game_runtime.entities)=
### Facet: `10_game_runtime.entities`
(facet-10_game_runtime.flow)=
### Facet: `10_game_runtime.flow`
(facet-10_game_runtime.game_state)=
### Facet: `10_game_runtime.game_state`
(facet-10_game_runtime.runtime_loop)=
### Facet: `10_game_runtime.runtime_loop`
(facet-10_game_runtime.summary)=
### Facet: `10_game_runtime.summary`
