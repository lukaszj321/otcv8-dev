---
doc_id: 10_game_runtime, source_path: docs/authoring/10_game_runtime, source_sha: 1e742b7, last_sync_iso: 2025-10-18T01:36:41.412529Z, doc_class: spec, language: pl, title: 10 - Game Runtime, summary: Game loop, input handling, map management, and dependencies with events/UI., tags: game,runtime,loop,input
---

# 10 - Game Runtime

Game loop, input handling, map management, and dependencies with events/UI.

## Przegląd

Ten rozdział dokumentuje 10 game runtime w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
blueprints/index
datasets/index
diagrams/index
```

## Game Loop Architecture

The OTClient v8 game loop is a sophisticated frame-based system that coordinates input processing, game state updates, and rendering across multiple threads.

### Frame Cycle

Each frame follows a strict sequence:

1. **Input Polling** - Process keyboard and mouse events from OS
2. **Event Dispatching** - Execute queued events and callbacks
3. **Game State Update** - Process protocol messages and update world state
4. **Animation Updates** - Advance creature and effect animations
5. **Map Culling** - Determine visible tiles based on viewport
6. **Tile Rendering** - Draw map tiles to framebuffer
7. **Creature Rendering** - Draw creatures with proper z-ordering
8. **Effect Rendering** - Draw visual effects and particles
9. **UI Rendering** - Draw interface widgets
10. **Buffer Swap** - Present frame to display
11. **Frame Limiting** - Throttle to target FPS

### Thread Coordination

The game loop coordinates across multiple threads:

- **Main Thread** - Owns the primary game loop
- **Dispatcher Thread** - Executes game events in parallel
- **Graphics Thread** - Processes graphics-specific events
- **Network Thread** - Handles protocol message reception

### Performance Targets

Target frame times for 60 FPS (16.67ms per frame):
- Input + Event Processing: <6ms
- Game State Update: <10ms
- Rendering Pipeline: <28ms total
  - Map/Creatures: <15ms
  - UI: <5ms
  - Other: <8ms

## Input Event Handling

Input events flow through multiple layers:

1. **OS Events** - Platform-specific input capture
2. **InputManager** - Cross-platform input abstraction
3. **Event Queue** - Buffered event storage
4. **Event Dispatch** - Route to appropriate handlers
5. **UI System** - Widget-level event handling
6. **Game Actions** - High-level game commands

Input is processed with priority levels to ensure responsive UI interactions.

## Map Rendering Pipeline

The map rendering system uses spatial culling and batched rendering:

1. **Viewport Calculation** - Determine visible tile range
2. **Tile Collection** - Gather tiles in view frustum
3. **Z-Order Sorting** - Sort by render layer
4. **Batch Rendering** - Group draws by texture/shader
5. **Creature Overlay** - Draw creatures on top
6. **Effect Layer** - Render visual effects
7. **Lighting** - Apply lighting and shadows (if enabled)

## Datasets

```{csv-table} Game Loop Phases
:header-rows: 1
:file: ./datasets/game_loop_phases.csv
```

```{csv-table} Rendering Pipeline Stages
:header-rows: 1
:file: ./datasets/rendering_pipeline.csv
```

```{csv-table} Input Event Types
:header-rows: 1
:file: ./datasets/input_events.csv
```

Legacy datasets:
- `entities.csv`
- `game_state.csv`
- `resources.csv`
- `ticks.csv`
- `summary.csv`

## Diagrams

```{mermaid}
:caption: Game Loop Cycle
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
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
```

```{mermaid}
:caption: Frame Sequence Diagram
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
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
```

```{contents}
:local:
:depth: 2
```

## Crosslinks

Internal references:
- [Runtime](../01_runtime/index.md) - EventDispatcher and thread pools
- [Events](../02_events/index.md) - Event emission and handling
- [UI](../04_ui/index.md) - Widget rendering and input
- [Core API](../01_core/index.md) - C++ game loop implementation
- [Network](../05_network/index.md) - Protocol message processing
- [Assets](../06_assets/index.md) - Texture and sprite loading

External source files:
- `src/framework/core/application.cpp` - Main loop implementation
- `src/client/game.cpp` - Game state update logic
- `src/client/map.cpp` - Map rendering and culling
- `src/framework/ui/uimanager.cpp` - UI rendering system


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.412529Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-10_game_runtime.main)=
### Facet: `10_game_runtime.main`

Main documentation facet for 10_game_runtime.

(facet-10_game_runtime.game_loop_phases)=
### Facet: `10_game_runtime.game_loop_phases`

Detailed breakdown of game loop phases from initialization through each frame cycle including component interactions, dependencies, and execution order.

(facet-10_game_runtime.rendering_pipeline)=
### Facet: `10_game_runtime.rendering_pipeline`

Complete rendering pipeline documentation covering map culling, tile rendering, creature rendering, effects, UI rendering, and performance optimization strategies.

(facet-10_game_runtime.input_events)=
### Facet: `10_game_runtime.input_events`

Input event handling documentation including event types, sources, dispatch threads, priorities, and integration with game state updates.
