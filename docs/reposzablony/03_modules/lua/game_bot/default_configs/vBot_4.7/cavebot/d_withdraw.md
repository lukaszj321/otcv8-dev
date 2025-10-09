---
doc_id: "lua-spec-ca0953526faf"
source_path: "game_bot/default_configs/vBot_4.7/cavebot/d_withdraw.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:57Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: d_withdraw.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.7/cavebot/d_withdraw.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.7/cavebot/d_withdraw.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla d_withdraw.

## Functions

### `CaveBot.Extensions.DWithdraw.setup()`

## Events/Callbacks

### `umber`

**Wywołanie:** `local indexDp = tonumber(data[1]:trim())`

### `umber`

**Wywołanie:** `local destId = tonumber(data[3]:trim())`

### `umber`

**Wywołanie:** `capLimit = tonumber(data[4]:trim())`

### `tainers`

**Wywołanie:** `for i, container in ipairs(getContainers()) do`

### `tainers`

containers

**Wywołanie:** `for i, container in ipairs(getContainers()) do`

### `tainerIsFull`

**Wywołanie:** `if containerIsFull(destContainer) then`

### `tainerIsFull`

**Wywołanie:** `if containerIsFull(destContainer) then`

### `tainers`

**Wywołanie:** `for i, container in pairs(g_game.getContainers()) do`
