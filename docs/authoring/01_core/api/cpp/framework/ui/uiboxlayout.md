---
doc_id: "cpp-api-164e3abb42ae"
source_path: "framework/ui/uiboxlayout.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: uiboxlayout.h"
summary: "Dokumentacja API C++ dla framework/ui/uiboxlayout.h"
tags: ["cpp", "api", "otclient"]
---

# framework/ui/uiboxlayout.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu uiboxlayout.

## Classes/Structs

### Klasa: `UIBoxLayout`

| Member | Brief | Signature |
|--------|-------|-----------|
| `applyStyle` |  | `void applyStyle(const OTMLNodePtr& styleNode)` |
| `addWidget` |  | `void addWidget(const UIWidgetPtr& widget) { update(); }` |
| `removeWidget` |  | `void removeWidget(const UIWidgetPtr& widget) { update(); }` |
| `setSpacing` |  | `void setSpacing(int spacing) { m_spacing = spacing; update(); }` |
| `setFitChildren` |  | `void setFitChildren(bool fitParent) { m_fitChildren = fitParent; update(); }` |
| `isUIBoxLayout` |  | `bool isUIBoxLayout() { return true; }` |
| `m_fitChildren` |  | `stdext::boolean<false> m_fitChildren` |
| `m_spacing` |  | `int m_spacing` |

## Functions

### `applyStyle`

**Sygnatura:** `void applyStyle(const OTMLNodePtr& styleNode)`

### `addWidget`

**Sygnatura:** `void addWidget(const UIWidgetPtr& widget) { update(); }`

### `removeWidget`

**Sygnatura:** `void removeWidget(const UIWidgetPtr& widget) { update(); }`

### `setSpacing`

**Sygnatura:** `void setSpacing(int spacing) { m_spacing = spacing; update(); }`

### `setFitChildren`

**Sygnatura:** `void setFitChildren(bool fitParent) { m_fitChildren = fitParent; update(); }`

### `isUIBoxLayout`

**Sygnatura:** `bool isUIBoxLayout() { return true; }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    UIBoxLayout["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>UIBoxLayout</div><hr/>
            <b>Widget Management:</b><br/>
            + addWidget(widget)<br/>
            + removeWidget(widget)<br/>
            <b>Configuration:</b><br/>
            + setSpacing(spacing)<br/>
            + setFitChildren(fitParent)<br/>
            <b>Style:</b><br/>
            + applyStyle(styleNode)
        </div>
    "]:::ui;
    
    UILayout["UILayout<br/><i>base class</i>"]:::core
    
    UIBoxLayout --> |"extends"| UILayout
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
