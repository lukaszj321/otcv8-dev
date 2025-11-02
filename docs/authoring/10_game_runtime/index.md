---
title: 10_game_runtime - Game runtime
---

# 10_game_runtime - Game runtime

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

### game_loop_phases
*Facet:* [`10_game_runtime.game_loop_phases`](#facet-10_game_runtime.game_loop_phases)

```{csv-table} game_loop_phases
:header-rows: 1
:file: ./datasets/game_loop_phases.csv
:widths: auto
```

### game_state
*Facet:* [`10_game_runtime.game_state`](#facet-10_game_runtime.game_state)

```{csv-table} game_state
:header-rows: 1
:file: ./datasets/game_state.csv
:widths: auto
```

### input_events
*Facet:* [`10_game_runtime.input_events`](#facet-10_game_runtime.input_events)

```{csv-table} input_events
:header-rows: 1
:file: ./datasets/input_events.csv
:widths: auto
```

### rendering_pipeline
*Facet:* [`10_game_runtime.rendering_pipeline`](#facet-10_game_runtime.rendering_pipeline)

```{csv-table} rendering_pipeline
:header-rows: 1
:file: ./datasets/rendering_pipeline.csv
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
click Architecture "./index.html#facet-10_game_runtime.architecture" "Open architecture"
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
click Flow "./index.html#facet-10_game_runtime.flow" "Open flow"
```

### frame_sequence
*Facet:* [`10_game_runtime.frame_sequence`](#facet-10_game_runtime.frame_sequence)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
sequenceDiagram
    participant App as Application
    participant Input as InputManager
    participant Dispatcher as EventDispatcher
    participant Game as Game
    participant Map as Map
    participant UI as UIManager
    participant Graphics as Graphics

    Note over App: Frame Begin
    
    App->>Input: Poll OS events
    Input->>Dispatcher: Queue input events
    
    App->>Dispatcher: poll()
    activate Dispatcher
    Dispatcher->>Dispatcher: Execute queued events
    Dispatcher->>Game: Trigger game events
    deactivate Dispatcher
    
    App->>Game: update()
    activate Game
    Game->>Game: Process protocol messages
    Game->>Game: Update creatures
    Game->>Game: Update animations
    deactivate Game
    
    App->>Map: render()
    activate Map
    Map->>Map: Cull visible tiles
    Map->>Graphics: Draw tiles
    Map->>Graphics: Draw creatures
    Map->>Graphics: Draw effects
    deactivate Map
    
    App->>UI: render()
    activate UI
    UI->>Graphics: Draw widgets
    deactivate UI
    
    App->>Graphics: swapBuffers()
    Graphics-->>App: Frame displayed
    
    App->>App: Frame limiter
    Note over App: Frame End
    %% click FrameSequence "./index.html#facet-10_game_runtime.frame_sequence" "Open frame_sequence" %% REMOVED: click not supported in sequenceDiagram
```

### game_loop_cycle
*Facet:* [`10_game_runtime.game_loop_cycle`](#facet-10_game_runtime.game_loop_cycle)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    Start[Frame Start] --> PollInput[Poll Input Events]
    PollInput --> PollEvents[EventDispatcher Poll]
    PollEvents --> UpdateGame[Game State Update]
    
    UpdateGame --> ProcessProtocol[Process Protocol Messages]
    ProcessProtocol --> UpdateCreatures[Update Creatures]
    UpdateCreatures --> UpdateAnimations[Update Animations]
    UpdateAnimations --> UpdateEffects[Update Effects]
    
    UpdateEffects --> CullMap[Map Culling]
    CullMap --> RenderTiles[Render Map Tiles]
    RenderTiles --> RenderCreatures[Render Creatures]
    RenderCreatures --> RenderEffects[Render Effects]
    RenderEffects --> RenderUI[Render UI]
    
    RenderUI --> SwapBuffers[Swap Buffers]
    SwapBuffers --> FrameLimit[Frame Limiter]
    FrameLimit --> Start
    
    PollEvents -.->|Parallel| GraphicsPoll[Graphics Dispatcher Poll]
    GraphicsPoll -.-> RenderTiles
    
    click UpdateGame "./index.html#facet-10_game_runtime.game_loop_phases" "Game Loop Phases"
    click RenderTiles "./index.html#facet-10_game_runtime.rendering_pipeline" "Rendering Pipeline"
click GameLoopCycle "./index.html#facet-10_game_runtime.game_loop_cycle" "Open game_loop_cycle"
```

### loop
*Facet:* [`10_game_runtime.loop`](#facet-10_game_runtime.loop)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[10_game_runtime.loop] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-10_game_runtime.loop" "Open loop"
click Loop "./index.html#facet-10_game_runtime.loop" "Open loop"
```

### overview
*Facet:* [`10_game_runtime.overview`](#facet-10_game_runtime.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Game Runtime] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-10_game_runtime.overview" "Open overview"
```

### runtime_loop
*Facet:* [`10_game_runtime.runtime_loop`](#facet-10_game_runtime.runtime_loop)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  RuntimeLoop[10_game_runtime:runtime_loop] --> Data[Datasets]
  Data --> Page[Index]

click RuntimeLoop "./index.html#facet-10_game_runtime.runtime_loop" "Open runtime_loop"
click RuntimeLoop "./index.html#facet-10_game_runtime.runtime_loop" "Open runtime_loop"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
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

(facet-10_game_runtime.frame_sequence)=
### Facet: `10_game_runtime.frame_sequence`
Type: diagram

(facet-10_game_runtime.game_loop_cycle)=
### Facet: `10_game_runtime.game_loop_cycle`
Type: diagram

(facet-10_game_runtime.game_loop_phases)=
### Facet: `10_game_runtime.game_loop_phases`
Type: dataset

(facet-10_game_runtime.game_state)=
### Facet: `10_game_runtime.game_state`
Type: dataset

(facet-10_game_runtime.input_events)=
### Facet: `10_game_runtime.input_events`
Type: dataset

(facet-10_game_runtime.loop)=
### Facet: `10_game_runtime.loop`
Type: diagram

(facet-10_game_runtime.overview)=
### Facet: `10_game_runtime.overview`
Type: diagram

(facet-10_game_runtime.rendering_pipeline)=
### Facet: `10_game_runtime.rendering_pipeline`
Type: dataset

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

