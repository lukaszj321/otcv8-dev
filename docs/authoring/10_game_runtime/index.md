---
title: Game runtime — export kit
---

# Game runtime — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

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

### loop
*Facet:* [`10_game_runtime.loop`](#facet-10_game_runtime.loop)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[10_game_runtime.loop] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-10_game_runtime.loop" "Open loop"
```

## Cross-References

- **consumes** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)
- **driven_by** → `05_network.flows` (evidence: `docs/authoring/05_network/datasets/flows.csv`)
- **syncs** → `08_audio.events` (evidence: `docs/authoring/08_audio/datasets/events.csv`)

## Appendix / Facets

(facet-10_game_runtime.game_state)=
### Facet: `10_game_runtime.game_state`
Type: dataset

(facet-10_game_runtime.loop)=
### Facet: `10_game_runtime.loop`
Type: diagram

(facet-10_game_runtime.resources)=
### Facet: `10_game_runtime.resources`
Type: dataset

(facet-10_game_runtime.summary)=
### Facet: `10_game_runtime.summary`
Type: dataset

(facet-10_game_runtime.ticks)=
### Facet: `10_game_runtime.ticks`
Type: dataset
