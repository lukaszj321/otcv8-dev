---
doc_id: "lua-spec-b3d6888f6a22"
source_path: "game_bot/default_configs/vBot_4.7/vBot/quiver_manager.lua"
source_sha: "05ca843"
last_sync_iso: "2025-10-09T05:39:46Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: quiver_manager.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.7/vBot/quiver_manager.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.7/vBot/quiver_manager.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla quiver_manager.

## Functions

### `manageQuiver(isBowEquipped, quiverContainer)`

**Parametry:**

- `isBowEquipped`
- `quiverContainer`

## Events/Callbacks

### `ContainerOpen`

**Wywołanie:** `onContainerOpen(function(container, previousContainer)`

### `ContainerClose`

**Wywołanie:** `onContainerClose(function(container)`

### `AddItem`

**Wywołanie:** `onAddItem(function(container, slot, item, oldItem)`

### `RemoveItem`

**Wywołanie:** `onRemoveItem(function(container, slot, item)`

### `ContainerUpdateItem`

**Wywołanie:** `onContainerUpdateItem(function(container, slot, item, oldItem)`

### `tainers`

**Wywołanie:** `local containers = getContainers()`

### `tainerIsFull`

**Wywołanie:** `if container ~= quiverContainer and not containerIsFull(container) then`

### `tainerIsFull`

**Wywołanie:** `if not containerIsFull(quiverContainer) then`

### `tainer`

**Wywołanie:** `local quiverEquipped = getRight() and getRight():isContainer()`

### `tainerByItem`

**Wywołanie:** `local quiverContainer = getContainerByItem(getRight():getId())`
