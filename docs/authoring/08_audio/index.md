---
title: Audio system — export kit
---

# Audio system — export kit

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

### audio_assets
*Facet:* [`08_audio.audio_assets`](#facet-08_audio.audio_assets)

```{csv-table} audio_assets
:header-rows: 1
:file: ./datasets/audio_assets.csv
:widths: auto
```

### channels
*Facet:* [`08_audio.channels`](#facet-08_audio.channels)

```{csv-table} channels
:header-rows: 1
:file: ./datasets/channels.csv
:widths: auto
```

### events
*Facet:* [`08_audio.events`](#facet-08_audio.events)

```{csv-table} events
:header-rows: 1
:file: ./datasets/events.csv
:widths: auto
```

### summary
*Facet:* [`08_audio.summary`](#facet-08_audio.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams

### routing
*Facet:* [`08_audio.routing`](#facet-08_audio.routing)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[08_audio.routing] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-08_audio.routing" "Open routing"
```

## Cross-References

- **syncs_with** → `10_game_runtime.tick` (evidence: `docs/authoring/10_game_runtime/datasets/ticks.csv`)
- **uses** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)

## Appendix / Facets

(facet-08_audio.audio_assets)=
### Facet: `08_audio.audio_assets`
Type: dataset

(facet-08_audio.channels)=
### Facet: `08_audio.channels`
Type: dataset

(facet-08_audio.events)=
### Facet: `08_audio.events`
Type: dataset

(facet-08_audio.routing)=
### Facet: `08_audio.routing`
Type: diagram

(facet-08_audio.summary)=
### Facet: `08_audio.summary`
Type: dataset
