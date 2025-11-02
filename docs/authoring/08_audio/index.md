---
title: 08_audio - Audio
---

# 08_audio - Audio

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

### audio_config
*Facet:* [`08_audio.audio_config`](#facet-08_audio.audio_config)

```{csv-table} audio_config
:header-rows: 1
:file: ./datasets/audio_config.csv
:widths: auto
```

### audio_examples
*Facet:* [`08_audio.audio_examples`](#facet-08_audio.audio_examples)

```{csv-table} audio_examples
:header-rows: 1
:file: ./datasets/audio_examples.csv
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

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Audio
        E0[Sound Channels]
        E1[Audio Sources]
        E2[Audio Stats]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-08_audio.architecture" "Open architecture"
```

### audio_pipeline
*Facet:* [`08_audio.audio_pipeline`](#facet-08_audio.audio_pipeline)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  AudioPipeline[08_audio:audio_pipeline] --> Data[Datasets]
  Data --> Page[Index]

click AudioPipeline "./index.html#facet-08_audio.audio_pipeline" "Open audio_pipeline"
click AudioPipeline "./index.html#facet-08_audio.audio_pipeline" "Open audio_pipeline"
```

### audio_playback_flow
*Facet:* [`08_audio.audio_playback_flow`](#facet-08_audio.audio_playback_flow)

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
sequenceDiagram
    participant App as Application
    participant SM as SoundManager
    participant CH as SoundChannel
    participant SS as SoundSource
    participant AL as OpenAL
    
    App->>SM: init()
    SM->>AL: Create device & context
    
    App->>SM: getChannel(1)
    SM-->>App: SoundChannel (Music)
    
    App->>CH: play("/sounds/startup")
    CH->>SM: createSoundSource()
    SM->>SS: Create SoundSource
    SM->>AL: Load buffer
    SS->>AL: alSourcePlay()
    
    App->>CH: setGain(0.8)
    CH->>SS: Update gain
    SS->>AL: alSourcef(AL_GAIN)
    
    App->>SM: stopAll()
    SM->>SS: stop()
    SS->>AL: alSourceStop()
    
    %% click SM "../index.html#facet-08_audio.audio_flow" "Audio Flow" %% REMOVED: click not supported in sequenceDiagram
    %% click AudioPlaybackFlow "./index.html#facet-08_audio.audio_playback_flow" "Open audio_playback_flow" %% REMOVED: click not supported in sequenceDiagram
```

### channels_hierarchy
*Facet:* [`08_audio.channels_hierarchy`](#facet-08_audio.channels_hierarchy)

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    SoundManager[SoundManager g_sounds] --> Channel1[Channel 1 - Music]
    SoundManager --> Channel2[Channel 2 - Ambient]
    SoundManager --> Channel3[Channel 3 - Effect]
    SoundManager --> Channel4[Channel 4 - Bot]
    
    Channel1 -->|setGain| MusicVolume[Music Volume Control]
    Channel1 -->|setEnabled| MusicToggle[Music Enable/Disable]
    
    Channel4 -->|setGain| BotVolume[Bot Volume Control]
    Channel4 -->|play| BotSounds[Bot Alarm Sounds]
    
    SoundManager -->|setAudioEnabled| GlobalControl[Global Audio Control]
    SoundManager -->|stopAll| Cleanup[Stop All Sources]
    
    click Channel1 "../index.html#facet-08_audio.channels" "Audio Channels"
    click Channel4 "../index.html#facet-08_audio.channels" "Audio Channels"
click ChannelsHierarchy "./index.html#facet-08_audio.channels_hierarchy" "Open channels_hierarchy"
```

### flow
*Facet:* [`08_audio.flow`](#facet-08_audio.flow)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Audio] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-08_audio.flow" "Open flow"
```

### overview
*Facet:* [`08_audio.overview`](#facet-08_audio.overview)

```mermaid
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Audio System] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-08_audio.overview" "Open overview"
```

### routing
*Facet:* [`08_audio.routing`](#facet-08_audio.routing)

```mermaid
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[08_audio.routing] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-08_audio.routing" "Open routing"
click Routing "./index.html#facet-08_audio.routing" "Open routing"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
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

(facet-08_audio.audio_config)=
### Facet: `08_audio.audio_config`
Type: dataset

(facet-08_audio.audio_examples)=
### Facet: `08_audio.audio_examples`
Type: dataset

(facet-08_audio.audio_pipeline)=
### Facet: `08_audio.audio_pipeline`
Type: diagram

(facet-08_audio.audio_playback_flow)=
### Facet: `08_audio.audio_playback_flow`
Type: diagram

(facet-08_audio.channels)=
### Facet: `08_audio.channels`
Type: dataset

(facet-08_audio.channels_hierarchy)=
### Facet: `08_audio.channels_hierarchy`
Type: diagram

(facet-08_audio.entities)=
### Facet: `08_audio.entities`
Type: dataset

(facet-08_audio.events)=
### Facet: `08_audio.events`
Type: dataset

(facet-08_audio.flow)=
### Facet: `08_audio.flow`
Type: diagram

(facet-08_audio.overview)=
### Facet: `08_audio.overview`
Type: diagram

(facet-08_audio.routing)=
### Facet: `08_audio.routing`
Type: diagram

(facet-08_audio.summary)=
### Facet: `08_audio.summary`
Type: dataset

