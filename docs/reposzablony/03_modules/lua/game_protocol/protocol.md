---
doc_id: "lua-spec-8a02fa81ae38"
source_path: "game_protocol/protocol.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:58Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: protocol.lua"
summary: "Dokumentacja modułu Lua dla game_protocol/protocol.lua"
tags: ["lua", "module", "otclient"]
---

# game_protocol/protocol.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla protocol.

## Globals/Exports

### `registredOpcodes`

## Functions

### `init()`

### `terminate()`

### `registerProtocol()`

### `readAddItem(msg)`

**Parametry:**

- `msg`

### `unregisterProtocol()`

### `registerOpcode(code, func)`

**Parametry:**

- `code`
- `func`

### `readDailyReward(msg)`

**Parametry:**

- `msg`

## Events/Callbacks

### `g_game`

**Wywołanie:** `connect(g_game, { onEnterGame = registerProtocol,`

### `g_game`

**Wywołanie:** `disconnect(g_game, { onEnterGame = registerProtocol,`
