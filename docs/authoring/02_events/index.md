---
title: 02_events - Events
---

# 02_events - Events

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### emitters
*Facet:* [`02_events.emitters`](#facet-02_events.emitters)

```{csv-table} emitters
:header-rows: 1
:file: ./datasets/emitters.csv
:widths: auto
```

### entities
*Facet:* [`02_events.entities`](#facet-02_events.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### event_catalog
*Facet:* [`02_events.event_catalog`](#facet-02_events.event_catalog)

```{csv-table} event_catalog
:header-rows: 1
:file: ./datasets/event_catalog.csv
:widths: auto
```

### event_tutorials
*Facet:* [`02_events.event_tutorials`](#facet-02_events.event_tutorials)

```{csv-table} event_tutorials
:header-rows: 1
:file: ./datasets/event_tutorials.csv
:widths: auto
```

### events_matrix
*Facet:* [`02_events.events_matrix`](#facet-02_events.events_matrix)

```{csv-table} events_matrix
:header-rows: 1
:file: ./datasets/events_matrix.csv
:widths: auto
```

### handlers
*Facet:* [`02_events.handlers`](#facet-02_events.handlers)

```{csv-table} handlers
:header-rows: 1
:file: ./datasets/handlers.csv
:widths: auto
```

### summary
*Facet:* [`02_events.summary`](#facet-02_events.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`02_events.architecture`](#facet-02_events.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Events
        E0[Event Types]
        E1[Signal Handlers]
        E2[Event Sequences]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-02_events.architecture" "Open architecture"
```

### bus
*Facet:* [`02_events.bus`](#facet-02_events.bus)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[02_events.bus] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-02_events.bus" "Open bus"
click Bus "./index.html#facet-02_events.bus" "Open bus"
```

### event_flow
*Facet:* [`02_events.event_flow`](#facet-02_events.event_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  EventFlow[02_events:event_flow] --> Data[Datasets]
  Data --> Page[Index]

click EventFlow "./index.html#facet-02_events.event_flow" "Open event_flow"
click EventFlow "./index.html#facet-02_events.event_flow" "Open event_flow"
```

### event_flow_map
*Facet:* [`02_events.event_flow_map`](#facet-02_events.event_flow_map)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
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
    
    click Lifecycle "./index.html#facet-02_events.event_catalog" "Event Catalog"
    click PlayerEvents "./index.html#facet-02_events.event_catalog" "Event Catalog"
click EventFlowMap "./index.html#facet-02_events.event_flow_map" "Open event_flow_map"
```

### flow
*Facet:* [`02_events.flow`](#facet-02_events.flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Events] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-02_events.flow" "Open flow"
```

### login_lifecycle
*Facet:* [`02_events.login_lifecycle`](#facet-02_events.login_lifecycle)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
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
    %% click LoginLifecycle "./index.html#facet-02_events.login_lifecycle" "Open login_lifecycle" %% REMOVED: click not supported in sequenceDiagram
```

### overview
*Facet:* [`02_events.overview`](#facet-02_events.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Events System] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-02_events.overview" "Open overview"
```

### propagation
*Facet:* [`02_events.propagation`](#facet-02_events.propagation)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[02_events.propagation] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-02_events.propagation" "Open propagation"
click Propagation "./index.html#facet-02_events.propagation" "Open propagation"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```

## Crosslinks

- **handles** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **emits** → `04_ui.signals_matrix` (evidence: `docs/authoring/04_ui/datasets/ui_signals.csv`)
- **uses** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-02_events.architecture)=
### Facet: `02_events.architecture`
Type: diagram

(facet-02_events.bus)=
### Facet: `02_events.bus`
Type: diagram

(facet-02_events.emitters)=
### Facet: `02_events.emitters`
Type: dataset

(facet-02_events.entities)=
### Facet: `02_events.entities`
Type: dataset

(facet-02_events.event_catalog)=
### Facet: `02_events.event_catalog`
Type: dataset

(facet-02_events.event_flow)=
### Facet: `02_events.event_flow`
Type: diagram

(facet-02_events.event_flow_map)=
### Facet: `02_events.event_flow_map`
Type: diagram

(facet-02_events.event_tutorials)=
### Facet: `02_events.event_tutorials`
Type: dataset

(facet-02_events.events_matrix)=
### Facet: `02_events.events_matrix`
Type: dataset

(facet-02_events.flow)=
### Facet: `02_events.flow`
Type: diagram

(facet-02_events.handlers)=
### Facet: `02_events.handlers`
Type: dataset

(facet-02_events.login_lifecycle)=
### Facet: `02_events.login_lifecycle`
Type: diagram

(facet-02_events.overview)=
### Facet: `02_events.overview`
Type: diagram

(facet-02_events.propagation)=
### Facet: `02_events.propagation`
Type: diagram

(facet-02_events.summary)=
### Facet: `02_events.summary`
Type: dataset

