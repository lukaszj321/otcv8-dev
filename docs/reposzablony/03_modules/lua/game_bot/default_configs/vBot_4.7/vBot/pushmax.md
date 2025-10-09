---
doc_id: "lua-spec-5ea4020a1d9b"
source_path: "game_bot/default_configs/vBot_4.7/vBot/pushmax.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:57Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: pushmax.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.7/vBot/pushmax.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.7/vBot/pushmax.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla pushmax.

## Functions

### `ui.title.onClick(widget)`

**Parametry:**

- `widget`

### `ui.push.onClick(widget)`

**Parametry:**

- `widget`

### `pushWindow.closeButton.onClick(widget)`

**Parametry:**

- `widget`

### `pushWindow.delay.onValueChange(scroll, value)`

**Parametry:**

- `scroll`
- `value`

### `pushWindow.runeId.onItemChange(widget)`

**Parametry:**

- `widget`

### `pushWindow.mwallId.onItemChange(widget)`

**Parametry:**

- `widget`

### `pushWindow.hotkey.onTextChange(widget, text)`

**Parametry:**

- `widget`
- `text`

## Events/Callbacks

### `getRootWidget`

**Wywołanie:** `rootWidget = g_ui.getRootWidget()`

### `KeyDown`

**Wywołanie:** `onKeyDown(function(keys)`

### `KeyPress`

mark tile to throw anything from it

**Wywołanie:** `onKeyPress(function(keys)`

### `CreaturePositionChange`

**Wywołanie:** `onCreaturePositionChange(function(creature, newPos, oldPos)`

### `umber`

**Wywołanie:** `local pushDelay = tonumber(config.pushDelay)`

### `umber`

**Wywołanie:** `local rune = tonumber(config.pushMaxRuneId)`

### `event`

**Wywołanie:** `schedule(pushDelay+700, function()`
