---
doc_id: "lua-spec-84d73959e9b0"
source_path: "game_bot/default_configs/cavebot_1.3/cavebot/editor.lua"
source_sha: "05ca843"
last_sync_iso: "2025-10-09T05:39:45Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: editor.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/cavebot_1.3/cavebot/editor.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/cavebot_1.3/cavebot/editor.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla editor.

## Functions

### `CaveBot.Editor.registerAction(action, text, params)`

also works as registerAction(action, params), then text == action params are options for text editor or function to be executed when clicked you have many examples how to use it bellow

**Parametry:**

- `action`
- `text`
- `params`

### `button.onClick()`

### `CaveBot.Editor.setup()`

### `value()`

### `value()`

### `value()`

### `ui.autoRecording.onClick()`

### `CaveBot.Editor.show()`

### `CaveBot.Editor.hide()`

### `CaveBot.Editor.edit(action, value, callback)`

**Parametry:**

- `action`
- `value`
- `callback`

## Events/Callbacks

### `DoubleClick`

**Wywołanie:** `action.onDoubleClick(action)`

### `PlayerPositionChange`

callbacks

**Wywołanie:** `onPlayerPositionChange(function(pos)`
