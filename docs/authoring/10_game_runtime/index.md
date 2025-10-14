---
title: 10_game_runtime - Game runtime
---

# 10_game_runtime - Game runtime

obserwacje runtime gry w czasie (hp/mp, poziom, predkosc, pozycja, tryby walki, proste liczebnosci). Bez danych wrazliwych ani tresci czatu.

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`10_game_runtime.entities`](#facet-10_game_runtime.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### game_state
*Facet:* [`10_game_runtime.game_state`](#facet-10_game_runtime.game_state)

```{csv-table} game_state
:header-rows: 1
:file: ./datasets/game_state.csv
:widths: auto
```

### resources
*Facet:* [`10_game_runtime.resources`](#facet-10_game_runtime.resources)

```{csv-table} resources
:header-rows: 1
:file: ./datasets/resources.csv
:widths: auto
```

### summary
*Facet:* [`10_game_runtime.summary`](#facet-10_game_runtime.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

### ticks
*Facet:* [`10_game_runtime.ticks`](#facet-10_game_runtime.ticks)

```{csv-table} ticks
:header-rows: 1
:file: ./datasets/ticks.csv
:widths: auto
```

## Diagrams
### architecture
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

### flow
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

### loop
        *Facet:* [`10_game_runtime.loop`](#facet-10_game_runtime.loop)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[10_game_runtime.loop] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-10_game_runtime.loop" "Open loop"
        ```

### runtime_loop
        *Facet:* [`10_game_runtime.runtime_loop`](#facet-10_game_runtime.runtime_loop)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  RuntimeLoop[10_game_runtime:runtime_loop] --> Data[Datasets]
  Data --> Page[Index]

click RuntimeLoop "./index.html#facet-10_game_runtime.runtime_loop" "Open runtime_loop"
        ```



## Crosslinks

- **consumes** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)
- **driven_by** → `05_network.flows` (evidence: `docs/authoring/05_network/datasets/flows.csv`)
- **syncs** → `08_audio.events` (evidence: `docs/authoring/08_audio/datasets/events.csv`)

## Appendix / Facets

(facet-10_game_runtime.architecture)=
### Facet: `10_game_runtime.architecture`
Type: diagram

(facet-10_game_runtime.entities)=
### Facet: `10_game_runtime.entities`
Type: dataset

(facet-10_game_runtime.flow)=
### Facet: `10_game_runtime.flow`
Type: diagram

(facet-10_game_runtime.game_state)=
### Facet: `10_game_runtime.game_state`
Type: dataset

(facet-10_game_runtime.loop)=
### Facet: `10_game_runtime.loop`
Type: diagram

(facet-10_game_runtime.resources)=
### Facet: `10_game_runtime.resources`
Type: dataset

(facet-10_game_runtime.runtime_loop)=
### Facet: `10_game_runtime.runtime_loop`
Type: diagram

(facet-10_game_runtime.summary)=
### Facet: `10_game_runtime.summary`
Type: dataset

(facet-10_game_runtime.ticks)=
### Facet: `10_game_runtime.ticks`
Type: dataset

