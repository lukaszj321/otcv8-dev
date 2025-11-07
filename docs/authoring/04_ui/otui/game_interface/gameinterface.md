---
doc_id: "otui-ui-bdc6cf923a06"
source_path: "game_interface/gameinterface.otui"
source_sha: "3ead5ec"
last_sync_iso: "2025-10-09T10:29:14Z"
doc_class: "ui"
language: "pl"
title: "UI: gameinterface.otui"
summary: "Dokumentacja interfejsu OTUI dla game_interface/gameinterface.otui"
tags: ["otui", "ui", "widget"]
---

# game_interface/gameinterface.otui

## Overview

Plik OTUI definiujący interfejs użytkownika dla gameinterface.

## Widgets

| ID | Class | Parent | Key Properties |
|----|-------|--------|----------------|
| `GameSidePanel` | `GameSidePanel` | `UIMiniWindowContainer` | image-source=/images/ui/panel_side, image-border=4, padding=0 |
| `GameMapPanel` | `GameMapPanel` | `UIGameMap` | padding=0, image-source=/images/ui/panel_map, image-border=4 |
| `gameTopBar` | `GameAction` | `UIButton` | visible=false, size=48 48 |

## Widget Details

### `GameSidePanel`

- **Klasa:** `GameSidePanel`
- **Rodzic:** `UIMiniWindowContainer`
- **Właściwości:**
  - `image-source`: /images/ui/panel_side
  - `image-border`: 4
  - `padding`: 0
  - `padding-top`: 0
  - `width`: 200
  - `focusable`: false
  - `on`: true
  - `type`: verticalBox

### `GameMapPanel`

- **Klasa:** `GameMapPanel`
- **Rodzic:** `UIGameMap`
- **Właściwości:**
  - `padding`: 0
  - `image-source`: /images/ui/panel_map
  - `image-border`: 4

### `gameTopBar`

- **Klasa:** `GameAction`
- **Rodzic:** `UIButton`
- **Właściwości:**
  - `size`: 48 48
  - `phantom`: true
  - `id`: gameTopBar
  - `opacity`: 0.6
  - `background`: alpha
  - `focusable`: false
  - `width`: 0
  - `visible`: false
  - `type`: verticalBox
  - `fit-children`: true
  - `spacing`: -1
  - `margin-top`: 3
  - `height`: 0
  - `relative-margin`: bottom
  - `margin-bottom`: 150
  - `image-source`: /images/ui/panel_bottom2

## Hierarchy Diagram

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
graph TD
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
    
    UIMiniWindowContainer["UIMiniWindowContainer<br/><i>base class</i>"]:::core
    UIGameMap["UIGameMap<br/><i>base class</i>"]:::core
    UIButton["UIButton<br/><i>base class</i>"]:::core
    
    GameSidePanel["GameSidePanel<br/>image-source=/images/ui/panel_side<br/>image-border=4<br/>padding=0"]:::ui
    GameMapPanel["GameMapPanel<br/>image-source=/images/ui/panel_map<br/>image-border=4"]:::ui
    GameTopBar["gameTopBar<br/>GameAction<br/>size=48 48<br/>visible=false"]:::ui
    
    UIMiniWindowContainer --> |"extends"| GameSidePanel
    UIGameMap --> |"extends"| GameMapPanel
    UIButton --> |"extends"| GameTopBar
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    classDef core fill:#2b2f33,stroke:#9aa0a6,color:#ddd,stroke-width:1px;
```
<!-- /mermaid-diagram -->

## Diagram: Game Interface Layout

<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=3ead5ec; generated_at=2025-01-27T00:00:00Z -->
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6'}, 'securityLevel': 'loose'}}%%
flowchart LR
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
    
    subgraph "Game Interface Layout"
        direction TB
        TopBar["gameTopBar<br/>Top Action Bar<br/>visible=false"]:::ui
        MapPanel["GameMapPanel<br/>Main Game View<br/>image-border=4"]:::ui
        SidePanel["GameSidePanel<br/>Side Panel<br/>width=200<br/>padding=0"]:::ui
    end
    
    TopBar --> MapPanel
    MapPanel --> SidePanel
    
    classDef ui fill:#22303a,stroke:#6a8b92,color:#ddd,stroke-dasharray:4 2;
```
<!-- /mermaid-diagram -->
