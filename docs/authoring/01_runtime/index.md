---
title: 01_runtime - Runtime
---

# 01_runtime - Runtime

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`01_runtime.entities`](#facet-01_runtime.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### lifecycle_stages
*Facet:* [`01_runtime.lifecycle_stages`](#facet-01_runtime.lifecycle_stages)

```{csv-table} lifecycle_stages
:header-rows: 1
:file: ./datasets/lifecycle_stages.csv
:widths: auto
```

### runtime_stats
*Facet:* [`01_runtime.runtime_stats`](#facet-01_runtime.runtime_stats)

```{csv-table} runtime_stats
:header-rows: 1
:file: ./datasets/runtime_stats.csv
:widths: auto
```

### scheduler_dispatcher
*Facet:* [`01_runtime.scheduler_dispatcher`](#facet-01_runtime.scheduler_dispatcher)

```{csv-table} scheduler_dispatcher
:header-rows: 1
:file: ./datasets/scheduler_dispatcher.csv
:widths: auto
```

### summary
*Facet:* [`01_runtime.summary`](#facet-01_runtime.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

### thread_pools
*Facet:* [`01_runtime.thread_pools`](#facet-01_runtime.thread_pools)

```{csv-table} thread_pools
:header-rows: 1
:file: ./datasets/thread_pools.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`01_runtime.architecture`](#facet-01_runtime.architecture)

```{mermaid}
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Runtime
        E0[Runtime Metrics]
        E1[Performance Stats]
        E2[Memory Usage]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-01_runtime.architecture" "Open architecture"
```

### dispatcher_architecture
*Facet:* [`01_runtime.dispatcher_architecture`](#facet-01_runtime.dispatcher_architecture)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    Client[Client Code] -->|addEvent| ED[EventDispatcher]
    Client -->|scheduleEvent| ED
    Client -->|cycleEvent| ED
    Client -->|async task| AD[AsyncDispatcher]
    
    ED -->|immediate| Queue[Event Queue]
    ED -->|delayed| Scheduled[Scheduled Priority Queue]
    
    Queue -->|poll| Executor[Event Executor]
    Scheduled -->|delay expired| Executor
    
    AD -->|dispatch| TaskQueue[Task Queue]
    TaskQueue -->|worker thread| AsyncExec[Async Executor]
    
    Executor -->|VALIDATE_DISPATCHER_THREAD| DT[Dispatcher Thread]
    
    GD[GraphicsDispatcher] -->|VALIDATE_GRAPHICS_THREAD| GT[Graphics Thread]
    
    click ED "./index.html#facet-01_runtime.scheduler_dispatcher" "Scheduler & Dispatcher"
    click AD "./index.html#facet-01_runtime.thread_pools" "Thread Pools"
click DispatcherArchitecture "./index.html#facet-01_runtime.dispatcher_architecture" "Open dispatcher_architecture"
```

### flow
*Facet:* [`01_runtime.flow`](#facet-01_runtime.flow)

```{mermaid}
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Runtime] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-01_runtime.flow" "Open flow"
```

### lifecycle_sequence
*Facet:* [`01_runtime.lifecycle_sequence`](#facet-01_runtime.lifecycle_sequence)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant App as Application
    participant AD as AsyncDispatcher
    participant ED as EventDispatcher
    participant GD as GraphicsDispatcher
    participant Worker as WorkerThread

    App->>AD: init()
    AD->>Worker: spawn_thread()
    activate Worker
    
    App->>ED: Start main loop
    loop Game Loop
        ED->>ED: poll()
        Note over ED: Process events
        ED->>ED: Execute scheduled events
        GD->>GD: poll()
        Note over GD: Render frame
    end
    
    App->>ED: shutdown()
    ED->>ED: Clear event queue
    App->>AD: stop()
    AD->>Worker: Signal terminate
    deactivate Worker
    App->>AD: terminate()
    %% click LifecycleSequence "./index.html#facet-01_runtime.lifecycle_sequence" "Open lifecycle_sequence" %% REMOVED: click not supported in sequenceDiagram
```

### overview
*Facet:* [`01_runtime.overview`](#facet-01_runtime.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Runtime System] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-01_runtime.overview" "Open overview"
```

### runtime_flow
*Facet:* [`01_runtime.runtime_flow`](#facet-01_runtime.runtime_flow)

```{mermaid}
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  RuntimeFlow[01_runtime:runtime_flow] --> Data[Datasets]
  Data --> Page[Index]

click RuntimeFlow "./index.html#facet-01_runtime.runtime_flow" "Open runtime_flow"
click RuntimeFlow "./index.html#facet-01_runtime.runtime_flow" "Open runtime_flow"
```



## Crosslinks

- **uses** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **uses** → `04_ui.ui_widgets` (evidence: `docs/authoring/04_ui/datasets/ui_widgets.csv`)
- **emits** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **emits** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-01_runtime.architecture)=
### Facet: `01_runtime.architecture`
Type: diagram

(facet-01_runtime.dispatcher_architecture)=
### Facet: `01_runtime.dispatcher_architecture`
Type: diagram

(facet-01_runtime.entities)=
### Facet: `01_runtime.entities`
Type: dataset

(facet-01_runtime.flow)=
### Facet: `01_runtime.flow`
Type: diagram

(facet-01_runtime.lifecycle_sequence)=
### Facet: `01_runtime.lifecycle_sequence`
Type: diagram

(facet-01_runtime.lifecycle_stages)=
### Facet: `01_runtime.lifecycle_stages`
Type: dataset

(facet-01_runtime.overview)=
### Facet: `01_runtime.overview`
Type: diagram

(facet-01_runtime.runtime_flow)=
### Facet: `01_runtime.runtime_flow`
Type: diagram

(facet-01_runtime.runtime_stats)=
### Facet: `01_runtime.runtime_stats`
Type: dataset

(facet-01_runtime.scheduler_dispatcher)=
### Facet: `01_runtime.scheduler_dispatcher`
Type: dataset

(facet-01_runtime.summary)=
### Facet: `01_runtime.summary`
Type: dataset

(facet-01_runtime.thread_pools)=
### Facet: `01_runtime.thread_pools`
Type: dataset

