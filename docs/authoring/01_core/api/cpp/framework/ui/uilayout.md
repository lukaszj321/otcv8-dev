---
doc_id: "cpp-api-e7d6bfcb7148"
source_path: "framework/ui/uilayout.h"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:28:07Z"
doc_class: "api"
language: "pl"
title: "API: uilayout.h"
summary: "Dokumentacja API C++ dla framework/ui/uilayout.h"
tags: ["cpp", "api", "otclient"]
---

# framework/ui/uilayout.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu uilayout.

## Classes/Structs

### Klasa: `UILayout`

| Member | Brief | Signature |
|--------|-------|-----------|
| `update` |  | `void update()` |
| `updateLater` |  | `void updateLater()` |
| `applyStyle` |  | `virtual void applyStyle(const OTMLNodePtr& styleNode) { }` |
| `addWidget` |  | `virtual void addWidget(const UIWidgetPtr& widget) { }` |
| `removeWidget` |  | `virtual void removeWidget(const UIWidgetPtr& widget) { }` |
| `disableUpdates` |  | `void disableUpdates() { m_updateDisabled++; }` |
| `enableUpdates` |  | `void enableUpdates() { m_updateDisabled = std::max<int>(m_updateDisabled-1,0); }` |
| `setParent` |  | `void setParent(UIWidgetPtr parentWidget) { m_parentWidget = parentWidget; }` |
| `getParentWidget` |  | `UIWidgetPtr getParentWidget() { return m_parentWidget; }` |
| `isUpdateDisabled` |  | `bool isUpdateDisabled() { return m_updateDisabled > 0; }` |
| `isUpdating` |  | `bool isUpdating() { return m_updating; }` |
| `isUIAnchorLayout` |  | `virtual bool isUIAnchorLayout() { return false; }` |
| `isUIBoxLayout` |  | `virtual bool isUIBoxLayout() { return false; }` |
| `isUIHorizontalLayout` |  | `virtual bool isUIHorizontalLayout() { return false; }` |
| `isUIVerticalLayout` |  | `virtual bool isUIVerticalLayout() { return false; }` |
| `isUIGridLayout` |  | `virtual bool isUIGridLayout() { return false; }` |
| `internalUpdate` |  | `virtual bool internalUpdate() { return false; }` |
| `m_updateDisabled` |  | `int m_updateDisabled` |
| `m_updating` |  | `stdext::boolean<false> m_updating` |
| `m_updateScheduled` |  | `stdext::boolean<false> m_updateScheduled` |
| `m_parentWidget` |  | `UIWidgetPtr m_parentWidget` |

## Functions

### `update`

**Sygnatura:** `void update()`

### `updateLater`

**Sygnatura:** `void updateLater()`

### `disableUpdates`

**Sygnatura:** `void disableUpdates() { m_updateDisabled++; }`

### `enableUpdates`

**Sygnatura:** `void enableUpdates() { m_updateDisabled = std::max<int>(m_updateDisabled-1,0); }`

### `setParent`

**Sygnatura:** `void setParent(UIWidgetPtr parentWidget) { m_parentWidget = parentWidget; }`

### `getParentWidget`

**Sygnatura:** `UIWidgetPtr getParentWidget() { return m_parentWidget; }`

### `isUpdateDisabled`

**Sygnatura:** `bool isUpdateDisabled() { return m_updateDisabled > 0; }`

### `isUpdating`

**Sygnatura:** `bool isUpdating() { return m_updating; }`

## Class Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    UILayout["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>UILayout</div><hr/>
            <i>&lt;&lt;abstract base&gt;&gt;</i><br/>
            <b>Update:</b><br/>
            + update()<br/>
            + updateLater()<br/>
            + disableUpdates()<br/>
            + enableUpdates()<br/>
            <b>Widget Management:</b><br/>
            + addWidget(widget)*<br/>
            + removeWidget(widget)*<br/>
            <b>Style:</b><br/>
            + applyStyle(styleNode)*<br/>
            <b>State:</b><br/>
            + isUpdateDisabled()<br/>
            + isUpdating()<br/>
            <b>Type Checks:</b><br/>
            + isUIAnchorLayout()<br/>
            + isUIBoxLayout()<br/>
            + isUIGridLayout()
        </div>
    "]:::core;
    
    UIAnchorLayout["UIAnchorLayout"]:::ui
    UIBoxLayout["UIBoxLayout"]:::ui
    UIGridLayout["UIGridLayout"]:::ui
    UIHorizontalLayout["UIHorizontalLayout"]:::ui
    UIVerticalLayout["UIVerticalLayout"]:::ui
    
    UILayout --> |"base class"| UIAnchorLayout
    UILayout --> |"base class"| UIBoxLayout
    UILayout --> |"base class"| UIGridLayout
    UIBoxLayout --> |"extends"| UIHorizontalLayout
    UIBoxLayout --> |"extends"| UIVerticalLayout
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->
