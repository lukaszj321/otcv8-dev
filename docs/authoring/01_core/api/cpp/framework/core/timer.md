---
doc_id: "cpp-api-5b416470c8d9"
source_path: "framework/core/timer.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: timer.h"
summary: "Dokumentacja API C++ dla framework/core/timer.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/timer.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu timer.

## Classes/Structs

### Klasa: `Timer`

| Member | Brief | Signature |
|--------|-------|-----------|
| `restart` |  | `void restart()` |
| `stop` |  | `void stop() { m_stopped = true; }` |
| `adjust` |  | `void adjust(ticks_t value) { m_startTicks += value; }` |
| `startTicks` |  | `ticks_t startTicks() { return m_startTicks; }` |
| `ticksElapsed` |  | `ticks_t ticksElapsed()` |
| `timeElapsed` |  | `float timeElapsed() { return ticksElapsed()/1000.0f; }` |
| `running` |  | `bool running() { return !m_stopped; }` |

## Functions

### `restart`

**Sygnatura:** `void restart()`

### `stop`

**Sygnatura:** `void stop() { m_stopped = true; }`

### `adjust`

**Sygnatura:** `void adjust(ticks_t value) { m_startTicks += value; }`

### `startTicks`

**Sygnatura:** `ticks_t startTicks() { return m_startTicks; }`

### `ticksElapsed`

**Sygnatura:** `ticks_t ticksElapsed()`

### `timeElapsed`

**Sygnatura:** `float timeElapsed() { return ticksElapsed()/1000.0f; }`

### `running`

**Sygnatura:** `bool running() { return !m_stopped; }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
    
    Timer["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Timer</div><hr/>
            <b>Control:</b><br/>
            + restart()<br/>
            + stop()<br/>
            + adjust(value)<br/>
            <b>Time Access:</b><br/>
            + startTicks()<br/>
            + ticksElapsed()<br/>
            + timeElapsed()<br/>
            <b>State:</b><br/>
            + running()
        </div>
    "]:::core;
    
    Clock["Clock"]:::core
    
    Timer --> |"uses"| Clock
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef data fill:#2b2f36,stroke:#7b9aa0,color:#ddd;
```
<!-- /mermaid-diagram -->
