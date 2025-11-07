---
doc_id: "cpp-api-010bd97ac7fb"
source_path: "framework/core/event.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: event.h"
summary: "Dokumentacja API C++ dla framework/core/event.h"
tags: ["cpp", "api", "otclient"]
---

# framework/core/event.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu event.

## Classes/Structs

### Klasa: `Event`

| Member | Brief | Signature |
|--------|-------|-----------|
| `execute` |  | `virtual void execute()` |
| `cancel` |  | `void cancel()` |
| `isCanceled` |  | `bool isCanceled() { return m_canceled; }` |
| `isExecuted` |  | `bool isExecuted() { return m_executed; }` |
| `isBotSafe` |  | `bool isBotSafe() { return m_botSafe; }` |
| `m_function` |  | `std::string m_function` |
| `m_callback` |  | `std::function<void()> m_callback` |
| `m_canceled` |  | `bool m_canceled` |
| `m_executed` |  | `bool m_executed` |
| `m_botSafe` |  | `bool m_botSafe` |

## Functions

### `cancel`

**Sygnatura:** `void cancel()`

### `isCanceled`

**Sygnatura:** `bool isCanceled() { return m_canceled; }`

### `isExecuted`

**Sygnatura:** `bool isExecuted() { return m_executed; }`

### `isBotSafe`

**Sygnatura:** `bool isBotSafe() { return m_botSafe; }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    Event["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>Event</div><hr/>
            <i>&lt;&lt;base class&gt;&gt;</i><br/>
            <b>Execution:</b><br/>
            + execute()*<br/>
            <b>Control:</b><br/>
            + cancel()<br/>
            <b>State:</b><br/>
            + isCanceled()<br/>
            + isExecuted()<br/>
            + isBotSafe()<br/>
            <b>Data:</b><br/>
            - m_function<br/>
            - m_callback<br/>
            - m_canceled<br/>
            - m_executed<br/>
            - m_botSafe
        </div>
    "]:::event;
    
    ScheduledEvent["ScheduledEvent<br/><i>extends Event</i>"]:::event
    
    Event --> |"base class"| ScheduledEvent
    
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    classDef event fill:#2a3a2f,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
