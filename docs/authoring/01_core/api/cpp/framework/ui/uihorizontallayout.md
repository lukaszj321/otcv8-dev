---
doc_id: "cpp-api-00e9938fae30"
source_path: "framework/ui/uihorizontallayout.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: uihorizontallayout.h"
summary: "Dokumentacja API C++ dla framework/ui/uihorizontallayout.h"
tags: ["cpp", "api", "otclient"]
---

# framework/ui/uihorizontallayout.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu uihorizontallayout.

## Classes/Structs

### Klasa: `UIHorizontalLayout`

| Member | Brief | Signature |
|--------|-------|-----------|
| `applyStyle` |  | `void applyStyle(const OTMLNodePtr& styleNode)` |
| `setAlignRight` |  | `void setAlignRight(bool aliginRight) { m_alignRight = aliginRight; update(); }` |
| `isUIHorizontalLayout` |  | `bool isUIHorizontalLayout() { return true; }` |
| `internalUpdate` |  | `bool internalUpdate()` |
| `m_alignChidren` |  | `Fw::AlignmentFlag m_alignChidren` |
| `m_alignRight` |  | `stdext::boolean<false> m_alignRight` |

## Functions

### `applyStyle`

**Sygnatura:** `void applyStyle(const OTMLNodePtr& styleNode)`

### `setAlignRight`

**Sygnatura:** `void setAlignRight(bool aliginRight) { m_alignRight = aliginRight; update(); }`

### `isUIHorizontalLayout`

**Sygnatura:** `bool isUIHorizontalLayout() { return true; }`

### `internalUpdate`

**Sygnatura:** `bool internalUpdate()`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    UIHorizontalLayout["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>UIHorizontalLayout</div><hr/>
            <b>Configuration:</b><br/>
            + setAlignRight(alignRight)<br/>
            <b>Style:</b><br/>
            + applyStyle(styleNode)<br/>
            <b>Internal:</b><br/>
            + internalUpdate()
        </div>
    "]:::ui;
    
    UIBoxLayout["UIBoxLayout<br/><i>base class</i>"]:::core
    
    UIHorizontalLayout --> |"extends"| UIBoxLayout
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
