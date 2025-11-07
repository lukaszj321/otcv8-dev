---
doc_id: "cpp-api-7857bf34d5aa"
source_path: "framework/ui/uiverticallayout.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: uiverticallayout.h"
summary: "Dokumentacja API C++ dla framework/ui/uiverticallayout.h"
tags: ["cpp", "api", "otclient"]
---

# framework/ui/uiverticallayout.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu uiverticallayout.

## Classes/Structs

### Klasa: `UIVerticalLayout`

| Member | Brief | Signature |
|--------|-------|-----------|
| `applyStyle` |  | `void applyStyle(const OTMLNodePtr& styleNode)` |
| `setAlignBottom` |  | `void setAlignBottom(bool aliginBottom) { m_alignBottom = aliginBottom; update(); }` |
| `isAlignBottom` |  | `bool isAlignBottom() { return m_alignBottom; }` |
| `isUIVerticalLayout` |  | `bool isUIVerticalLayout() { return true; }` |
| `internalUpdate` |  | `bool internalUpdate()` |
| `m_alignBottom` |  | `stdext::boolean<false> m_alignBottom` |

## Functions

### `applyStyle`

**Sygnatura:** `void applyStyle(const OTMLNodePtr& styleNode)`

### `setAlignBottom`

**Sygnatura:** `void setAlignBottom(bool aliginBottom) { m_alignBottom = aliginBottom; update(); }`

### `isAlignBottom`

**Sygnatura:** `bool isAlignBottom() { return m_alignBottom; }`

### `isUIVerticalLayout`

**Sygnatura:** `bool isUIVerticalLayout() { return true; }`

### `internalUpdate`

**Sygnatura:** `bool internalUpdate()`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    UIVerticalLayout["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>UIVerticalLayout</div><hr/>
            <b>Configuration:</b><br/>
            + setAlignBottom(alignBottom)<br/>
            + isAlignBottom()<br/>
            <b>Style:</b><br/>
            + applyStyle(styleNode)<br/>
            <b>Internal:</b><br/>
            + internalUpdate()
        </div>
    "]:::ui;
    
    UIBoxLayout["UIBoxLayout<br/><i>base class</i>"]:::core
    
    UIVerticalLayout --> |"extends"| UIBoxLayout
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
