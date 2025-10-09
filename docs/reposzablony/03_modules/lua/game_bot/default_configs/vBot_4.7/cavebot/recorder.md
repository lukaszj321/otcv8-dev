---
doc_id: "lua-spec-c13e52785cec"
source_path: "game_bot/default_configs/vBot_4.7/cavebot/recorder.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:57Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: recorder.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.7/cavebot/recorder.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.7/cavebot/recorder.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla recorder.

## Functions

### `setup()`

### `addPosition(pos)`

**Parametry:**

- `pos`

### `addStairs(pos)`

**Parametry:**

- `pos`

### `CaveBot.Recorder.isOn()`

### `CaveBot.Recorder.enable()`

### `CaveBot.Recorder.disable()`

## Events/Callbacks

### `PlayerPositionChange`

**Wywołanie:** `onPlayerPositionChange(function(newPos, oldPos)`

### `Use`

**Wywołanie:** `onUse(function(pos, itemId, stackPos, subType)`

### `UseWith`

**Wywołanie:** `onUseWith(function(pos, itemId, target, subType)`
