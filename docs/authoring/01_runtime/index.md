---
doc_id: 01_runtime, source_path: docs/authoring/01_runtime, source_sha: 488402e, last_sync_iso: 2025-10-18T01:36:41.410718Z, doc_class: spec, language: pl, title: 01 - Runtime, summary: Runtime lifecycle, scheduler/dispatcher, threading, and event queues., tags: runtime,lifecycle,scheduler,threads
---

# 01 - Runtime

Runtime lifecycle, scheduler/dispatcher, threading, and event queues.

## Przegląd

Ten rozdział dokumentuje 01 runtime w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
datasets/index
diagrams/index
```

## Scheduler & Dispatcher

The runtime system uses multiple dispatchers for event processing:

- **EventDispatcher** (`g_dispatcher`) - Main event queue for game logic
- **GraphicsDispatcher** (`g_graphicsDispatcher`) - Separate queue for rendering
- **AsyncDispatcher** (`g_asyncDispatcher`) - Worker thread pool for background tasks

### Thread Model

OTClient v8 uses a multi-threaded architecture with dedicated threads:

- **Main Thread** - Application initialization and main loop
- **Dispatcher Thread** - Event processing and game logic execution
- **Graphics Thread** - Rendering operations with separate OpenGL context
- **Worker Threads** - Async task execution pool

Thread safety is enforced with validation macros: `VALIDATE_DISPATCHER_THREAD()` and `VALIDATE_GRAPHICS_THREAD()`.

### Event Scheduling

Events can be scheduled in multiple ways:

- **Immediate** - `addEvent()` adds to queue, executed in next poll
- **Delayed** - `scheduleEvent(delay)` executes after delay in milliseconds
- **Cyclic** - `cycleEvent(interval)` re-schedules automatically after each execution

## Datasets

```{csv-table} Scheduler & Dispatcher Methods
:header-rows: 1
:file: ./datasets/scheduler_dispatcher.csv
```

```{csv-table} Thread Pools
:header-rows: 1
:file: ./datasets/thread_pools.csv
```

```{csv-table} Lifecycle Stages
:header-rows: 1
:file: ./datasets/lifecycle_stages.csv
```

Legacy datasets:
- `entities.csv`
- `runtime_stats.csv`
- `summary.csv`

## Diagrams

```{mermaid}
:caption: Runtime Lifecycle Sequence
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
```

```{mermaid}
:caption: Dispatcher Architecture
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
```

```{contents}
:local:
:depth: 2
```

## Crosslinks

Internal references:
- [Core API](../01_core/index.md) - C++ bindings and symbols
- [Events](../02_events/index.md) - Event emission and handling
- [Game Runtime](../10_game_runtime/index.md) - Game loop integration
- [Modules (Lua)](../03_modules/index.md) - Lua event scheduling
- [Network](../05_network/index.md) - Protocol dispatching

External source files:
- `src/framework/core/eventdispatcher.h` - EventDispatcher class
- `src/framework/core/asyncdispatcher.h` - AsyncDispatcher class
- `src/framework/stdext/thread.h` - Thread utilities


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.410718Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-01_runtime.main)=
### Facet: `01_runtime.main`

Main documentation facet for 01_runtime.

(facet-01_runtime.scheduler_dispatcher)=
### Facet: `01_runtime.scheduler_dispatcher`

Scheduler and dispatcher methods including EventDispatcher, GraphicsDispatcher, and AsyncDispatcher APIs.

(facet-01_runtime.thread_pools)=
### Facet: `01_runtime.thread_pools`

Thread pool configuration and thread model documentation covering main, dispatcher, graphics, and worker threads.

(facet-01_runtime.lifecycle_stages)=
### Facet: `01_runtime.lifecycle_stages`

Runtime lifecycle stages from initialization through shutdown, including dependencies and execution order.
