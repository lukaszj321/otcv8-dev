---
doc_id: "lua-spec-871b5e110b91"
source_path: "game_interface/widgets/uigamemap.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:58Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: uigamemap.lua"
summary: "Dokumentacja modułu Lua dla game_interface/widgets/uigamemap.lua"
tags: ["lua", "module", "otclient"]
---

# game_interface/widgets/uigamemap.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla uigamemap.

## Functions

### `UIGameMap.create()`

## Events/Callbacks

### `Destroy`

**Wywołanie:** `function UIGameMap:onDestroy()`

### `DragEnter`

**Wywołanie:** `function UIGameMap:onDragEnter(mousePos)`

### `DragLeave`

**Wywołanie:** `function UIGameMap:onDragLeave(droppedWidget, mousePos)`

### `Drop`

**Wywołanie:** `function UIGameMap:onDrop(widget, mousePos)`

### `MouseMove`

**Wywołanie:** `function UIGameMap:onMouseMove(mousePos, mouseMoved)`

### `DragMove`

**Wywołanie:** `function UIGameMap:onDragMove(mousePos, mouseMoved)`

### `MouseRelease`

**Wywołanie:** `self:onMouseRelease(self.mousePos, MouseRightButton)`

### `MousePress`

**Wywołanie:** `function UIGameMap:onMousePress()`

### `MouseRelease`

**Wywołanie:** `function UIGameMap:onMouseRelease(mousePosition, mouseButton)`

### `Offset`

**Wywołanie:** `local positionOffset = self:getPositionOffset(mousePosition)`

### `TouchRelease`

**Wywołanie:** `function UIGameMap:onTouchRelease(mousePosition, mouseButton)`

### `MouseRelease`

**Wywołanie:** `return self:onMouseRelease(mousePosition, mouseButton)`
