---
title: 08_audio - Audio
---

# 08_audio - Audio

snapshot(y) konfiguracji i stanu audio: masterVolume, per-channel volume, muted, lista grajacych zrodel (jesli API na to pozwala). Best-effort z runtime.

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

### entities
*Facet:* [`08_audio.entities`](#facet-08_audio.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
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
### architecture
        *Facet:* [`08_audio.architecture`](#facet-08_audio.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Audio
        E0[Sound Channels]
        E1[Audio Sources]
        E2[Audio Stats]
        E0 --> E1
        E1 --> E2
    end
        ```

### audio_pipeline
        *Facet:* [`08_audio.audio_pipeline`](#facet-08_audio.audio_pipeline)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  AudioPipeline[08_audio:audio_pipeline] --> Data[Datasets]
  Data --> Page[Index]

click AudioPipeline "./index.html#facet-08_audio.audio_pipeline" "Open audio_pipeline"
        ```

### flow
        *Facet:* [`08_audio.flow`](#facet-08_audio.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Audio] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

### routing
        *Facet:* [`08_audio.routing`](#facet-08_audio.routing)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[08_audio.routing] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-08_audio.routing" "Open routing"
        ```



## Crosslinks

- **syncs_with** → `10_game_runtime.tick` (evidence: `docs/authoring/10_game_runtime/datasets/ticks.csv`)
- **uses** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)

## Appendix / Facets

(facet-08_audio.architecture)=
### Facet: `08_audio.architecture`
Type: diagram

(facet-08_audio.audio_assets)=
### Facet: `08_audio.audio_assets`
Type: dataset

(facet-08_audio.audio_pipeline)=
### Facet: `08_audio.audio_pipeline`
Type: diagram

(facet-08_audio.channels)=
### Facet: `08_audio.channels`
Type: dataset

(facet-08_audio.entities)=
### Facet: `08_audio.entities`
Type: dataset

(facet-08_audio.events)=
### Facet: `08_audio.events`
Type: dataset

(facet-08_audio.flow)=
### Facet: `08_audio.flow`
Type: diagram

(facet-08_audio.routing)=
### Facet: `08_audio.routing`
Type: diagram

(facet-08_audio.summary)=
### Facet: `08_audio.summary`
Type: dataset

