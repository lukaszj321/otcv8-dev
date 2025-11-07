---
doc_id: "cpp-api-2860aafc4f2c"
source_path: "framework/core/scheduledevent.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: scheduledevent.h"
summary: "Dokumentacja API C++ dla framework/core/scheduledevent.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/scheduledevent.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu scheduledevent.

## Classes/Structs

### Klasa: `ScheduledEvent`

| Member | Brief | Signature |
|--------|-------|-----------|
| `execute` |  | `void execute()` |
| `nextCycle` |  | `bool nextCycle()` |
| `ticks` |  | `int ticks() { return m_ticks; }` |
| `remainingTicks` |  | `int remainingTicks() { return m_ticks - g_clock.millis(); }` |
| `delay` |  | `int delay() { return m_delay; }` |
| `cyclesExecuted` |  | `int cyclesExecuted() { return m_cyclesExecuted; }` |
| `maxCycles` |  | `int maxCycles() { return m_maxCycles; }` |

### Struktura: `lessScheduledEvent`

## Functions

### `execute`

**Sygnatura:** `void execute()`

### `nextCycle`

**Sygnatura:** `bool nextCycle()`

### `ticks`

**Sygnatura:** `int ticks() { return m_ticks; }`

### `remainingTicks`

**Sygnatura:** `int remainingTicks() { return m_ticks - g_clock.millis(); }`

### `delay`

**Sygnatura:** `int delay() { return m_delay; }`

### `cyclesExecuted`

**Sygnatura:** `int cyclesExecuted() { return m_cyclesExecuted; }`

### `maxCycles`

**Sygnatura:** `int maxCycles() { return m_maxCycles; }`

### `operator`

**Sygnatura:** `bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b) {`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    ScheduledEvent["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>ScheduledEvent</div><hr/>
            <b>Execution:</b><br/>
            + execute()<br/>
            + nextCycle()<br/>
            <b>Time Access:</b><br/>
            + ticks()<br/>
            + remainingTicks()<br/>
            + delay()<br/>
            <b>Cycle Info:</b><br/>
            + cyclesExecuted()<br/>
            + maxCycles()
        </div>
    "]:::event;
    
    Event["Event<br/><i>base class</i>"]:::event
    EventDispatcher["EventDispatcher"]:::core
    
    ScheduledEvent --> |"extends"| Event
    EventDispatcher --> |"manages"| ScheduledEvent
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->

## Diagram: Scheduled Event Lifecycle (Advanced Sequence)

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
sequenceDiagram
    participant Dispatcher
    participant ScheduledEvent
    participant Clock
    participant Callback
    
    Note over Dispatcher,Callback: Event Scheduling
    Dispatcher->>ScheduledEvent: scheduleEventEx(callback, delay)
    ScheduledEvent->>Clock: Get current ticks
    Clock-->>ScheduledEvent: currentTicks
    ScheduledEvent->>ScheduledEvent: Calculate execution ticks
    
    Note over Dispatcher,Callback: Event Execution Loop
    loop Until maxCycles or cancelled
        Dispatcher->>Clock: Get current ticks
        Clock-->>Dispatcher: currentTicks
        alt Remaining ticks <= 0
            Dispatcher->>ScheduledEvent: execute()
            ScheduledEvent->>Callback: Execute callback
            Callback-->>ScheduledEvent: Return
            ScheduledEvent->>ScheduledEvent: nextCycle()
            alt Has more cycles
                ScheduledEvent->>ScheduledEvent: Schedule next cycle
                ScheduledEvent-->>Dispatcher: Continue
            else Max cycles reached
                ScheduledEvent-->>Dispatcher: Complete
            end
        else Not yet time
            ScheduledEvent-->>Dispatcher: Wait
        end
    end
    
    opt Event cancelled
        Dispatcher->>ScheduledEvent: cancel()
        ScheduledEvent->>ScheduledEvent: Mark as cancelled
    end
```
<!-- /mermaid-diagram -->
