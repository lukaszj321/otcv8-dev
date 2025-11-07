---
doc_id: "cpp-api-06e099fcbefb"
source_path: "framework/core/eventdispatcher.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: eventdispatcher.h"
summary: "Dokumentacja API C++ dla framework/core/eventdispatcher.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/eventdispatcher.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu eventdispatcher.

## Classes/Structs

### Klasa: `EventDispatcher`

| Member | Brief | Signature |
|--------|-------|-----------|
| `shutdown` |  | `void shutdown()` |
| `poll` |  | `void poll()` |
| `addEventEx` |  | `EventPtr addEventEx(const std::string& function, const std::function<void()>& callback, bool pushFront = false)` |
| `scheduleEventEx` |  | `ScheduledEventPtr scheduleEventEx(const std::string& function, const std::function<void()>& callback, int delay)` |
| `cycleEventEx` |  | `ScheduledEventPtr cycleEventEx(const std::string& function, const std::function<void()>& callback, int delay)` |
| `isBotSafe` |  | `bool isBotSafe() { return m_botSafe; }` |

## Functions

### `shutdown`

**Sygnatura:** `void shutdown()`

### `poll`

**Sygnatura:** `void poll()`

### `addEventEx`

**Sygnatura:** `EventPtr addEventEx(const std::string& function, const std::function<void()>& callback, bool pushFront = false)`

### `scheduleEventEx`

**Sygnatura:** `ScheduledEventPtr scheduleEventEx(const std::string& function, const std::function<void()>& callback, int delay)`

### `cycleEventEx`

**Sygnatura:** `ScheduledEventPtr cycleEventEx(const std::string& function, const std::function<void()>& callback, int delay)`

### `isBotSafe`

**Sygnatura:** `bool isBotSafe() { return m_botSafe; }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    EventDispatcher["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>EventDispatcher</div><hr/>
            <b>Event Management:</b><br/>
            + addEventEx(function, callback)<br/>
            + scheduleEventEx(function, callback, delay)<br/>
            + cycleEventEx(function, callback, delay)<br/>
            <b>Control:</b><br/>
            + poll()<br/>
            + shutdown()<br/>
            <b>State:</b><br/>
            + isBotSafe()
        </div>
    "]:::core;
    
    Event["Event"]:::event
    ScheduledEvent["ScheduledEvent"]:::event
    
    EventDispatcher --> |"creates"| Event
    EventDispatcher --> |"creates"| ScheduledEvent
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
