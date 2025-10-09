---
doc_id: "lua-spec-af430830b4ae"
source_path: "game_bot/default_configs/vBot_4.8/vBot/eat_food.lua"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:58Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: eat_food.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.8/vBot/eat_food.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.8/vBot/eat_food.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla eat_food.

## Events/Callbacks

### `Time`

**Wywołanie:** `if player:getRegenerationTime() <= 400 then`

### `tainer`

**Wywołanie:** `local foodContainer = UI.Container(function(widget, items)`

### `Time`

**Wywołanie:** `if player:getRegenerationTime() > 400 or not storage.foodItems[1] then return end`

### `tainers`

search for food in containers

**Wywołanie:** `for _, container in pairs(g_game.getContainers()) do`
