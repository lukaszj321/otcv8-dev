---
doc_id: 02_events
source_path: docs/authoring/02_events
source_sha: 9609119
last_sync_iso: "2025-10-18T01:36:41.410923Z"
doc_class: api
language: pl
title: 02 - Events
---


# 02 - Events

C++ and Lua event emission, dispatch, signals, and emitter-handler mappings.

## Przegląd

Ten rozdział dokumentuje 02 events w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

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

## Event System Overview

The OTClient v8 event system provides a comprehensive signal/slot mechanism for connecting game events to handler functions. Events are emitted from C++ core components and can be handled in Lua modules.

### Event Categories

1. **Lifecycle Events** - Login, logout, game start/end
2. **Player Events** - Health, mana, stats, skills, inventory changes
3. **Creature Events** - Appearance, movement, outfit changes
4. **Protocol Events** - Network messages, extended opcodes
5. **Container Events** - Container open/close, item updates
6. **Combat Events** - Health changes, target changes
7. **Input Events** - Keyboard and mouse input

### Event Connection Pattern

Events are connected using the `connect()` function:

```lua
connect(source, {
  eventName = handlerFunction
})
```

Example:
```lua
connect(g_game, {
  onGameStart = function()
    print("Game started!")
  end,
  onGameEnd = function()
    print("Game ended!")
  end
})
```

### Custom Events

Modules can create custom signals for inter-module communication:

```lua
-- Create signal
myModule.onCustomEvent = {}

-- Emit signal
signalcall(myModule.onCustomEvent, param1, param2)

-- Connect to signal
connect(myModule, {onCustomEvent = myHandler})
```

## Datasets

```{csv-table} Event Emitters (Enhanced)
:header-rows: 1
:file: ./datasets/emitters.csv
```

```{csv-table} Event Catalog
:header-rows: 1
:file: ./datasets/event_catalog.csv
```

```{csv-table} Event Tutorials
:header-rows: 1
:file: ./datasets/event_tutorials.csv
```

Legacy datasets:
- `entities.csv`
- `events_matrix.csv`
- `handlers.csv`
- `summary.csv`

## Diagrams

```{mermaid}
:caption: Login and Lifecycle Event Sequence
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant Client as Client App
    participant Server as Game Server
    participant Protocol as ProtocolGame
    participant Game as g_game
    participant UI as UI Modules

    Client->>Server: Connect
    Server-->>Protocol: onRecvFirstMessage
    Protocol->>Game: Process handshake
    
    Client->>Server: Login credentials
    Server-->>Protocol: Login OK / Character list
    Protocol->>Game: onLogin
    Game->>UI: Emit onLogin
    
    Client->>Server: Enter game
    Server-->>Protocol: Enter world success
    Protocol->>Game: onGameStart
    Game->>UI: Emit onGameStart
    Note over UI: Initialize game modules
    
    loop Game Session
        Server-->>Protocol: Game updates
        Protocol->>Game: Various events
        Game->>UI: onHealthChange, onPositionChange, etc.
    end
    
    Client->>Server: Logout
    Server-->>Protocol: Logout OK
    Protocol->>Game: onGameEnd
    Game->>UI: Emit onGameEnd
    Note over UI: Cleanup game modules
```

```{mermaid}
:caption: Event Flow Architecture
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    Server[Game Server] -->|Protocol Messages| Protocol[ProtocolGame]
    
    Protocol -->|onLogin| Lifecycle[Lifecycle Events]
    Protocol -->|onGameStart| Lifecycle
    Protocol -->|onGameEnd| Lifecycle
    
    Protocol -->|Player Updates| PlayerEvents[Player Events]
    PlayerEvents -->|onHealthChange| HealthHandlers[Health Handlers]
    PlayerEvents -->|onManaChange| ManaHandlers[Mana Handlers]
    PlayerEvents -->|onStatsChange| StatsHandlers[Stats Handlers]
    PlayerEvents -->|onSkillChange| SkillHandlers[Skill Handlers]
    
    Protocol -->|Creature Updates| CreatureEvents[Creature Events]
    CreatureEvents -->|onAppear| BattleList[Battle List]
    CreatureEvents -->|onDisappear| BattleList
    CreatureEvents -->|onPositionChange| MapRenderer[Map Renderer]
    CreatureEvents -->|onOutfitChange| OutfitHandlers[Outfit Handlers]
    
    Protocol -->|Extended Opcodes| CustomEvents[Custom Events]
    CustomEvents -->|onExtendedOpcode| ExtHandlers[Extended Handlers]
    
    Protocol -->|Container Updates| ContainerEvents[Container Events]
    ContainerEvents -->|onOpen| ContainerUI[Container UI]
    ContainerEvents -->|onUpdateItem| ContainerUI
```

```{contents}
:local:
:depth: 2
```

## Crosslinks

Internal references:
- [Core API](../01_core/index.md) - C++ event emission infrastructure
- [Runtime](../01_runtime/index.md) - EventDispatcher and scheduling
- [Modules](../03_modules/index.md) - Lua event handlers
- [UI](../04_ui/index.md) - UI widget signals
- [Network](../05_network/index.md) - Protocol event emission
- [Game Runtime](../10_game_runtime/index.md) - Game loop event processing

External source files:
- `src/client/game.h` - g_game event definitions
- `src/client/protocolgame.cpp` - Protocol event emission
- `modules/game_interface/gameinterface.lua` - Main event handlers


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.410923Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-02_events.main)=
### Facet: `02_events.main`

Main documentation facet for 02_events.

(facet-02_events.event_catalog)=
### Facet: `02_events.event_catalog`

Comprehensive catalog of all event types including lifecycle, player, creature, protocol, container, combat, and input events with emitters, handlers, and payload schemas.

(facet-02_events.event_tutorials)=
### Facet: `02_events.event_tutorials`

Step-by-step tutorials for common event handling patterns from beginner to advanced including custom login events, health monitoring, auto loot tracking, and custom signal creation.