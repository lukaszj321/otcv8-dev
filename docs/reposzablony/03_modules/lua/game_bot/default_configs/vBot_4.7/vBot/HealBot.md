---
doc_id: "lua-spec-58d23146d2fd"
source_path: "game_bot/default_configs/vBot_4.7/vBot/HealBot.lua"
source_sha: "05ca843"
last_sync_iso: "2025-10-09T05:39:46Z"
doc_class: "spec"
language: "pl"
title: "Moduł Lua: HealBot.lua"
summary: "Dokumentacja modułu Lua dla game_bot/default_configs/vBot_4.7/vBot/HealBot.lua"
tags: ["lua", "module", "otclient"]
---

# game_bot/default_configs/vBot_4.7/vBot/HealBot.lua

## Overview

Moduł Lua zawierający funkcje i logikę dla HealBot.

## Globals/Exports

### `spellTable`

### `itemTable`

### `spellTable`

### `itemTable`

### `spellTable`

### `itemTable`

### `spellTable`

### `itemTable`

### `spellTable`

### `itemTable`

### `HealBot`

public functions

## Functions

### `ui.title.onClick(widget)`

**Parametry:**

- `widget`

### `ui.settings.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.onVisibilityChange(widget, visible)`

**Parametry:**

- `widget`
- `visible`

### `healWindow.settingsButton.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.profiles.Name.onTextChange(widget, text)`

**Parametry:**

- `widget`
- `text`

### `healWindow.settings.list.Visible.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.list.Cooldown.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.list.Interval.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.list.Conditions.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.list.Delay.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.settings.list.MessageDelay.onClick(widget)`

**Parametry:**

- `widget`

### `label.enabled.onClick(widget)`

**Parametry:**

- `widget`

### `label.remove.onClick(widget)`

**Parametry:**

- `widget`

### `label.enabled.onClick(widget)`

**Parametry:**

- `widget`

### `label.remove.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.spells.MoveUp.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.spells.MoveDown.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.items.MoveUp.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.items.MoveDown.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.spells.addSpell.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.healer.items.addItem.onClick(widget)`

**Parametry:**

- `widget`

### `healWindow.closeButton.onClick(widget)`

**Parametry:**

- `widget`

### `button.onClick()`

### `healWindow.settings.profiles.ResetSettings.onClick()`

### `HealBot.isOn()`

### `HealBot.isOff()`

### `HealBot.setOff()`

### `HealBot.setOn()`

### `HealBot.getActiveProfile()`

### `HealBot.setActiveProfile(n)`

**Parametry:**

- `n`

### `HealBot.show()`

## Events/Callbacks

### `figSave`

**Wywołanie:** `vBotConfigSave("heal")`

### `getRootWidget`

**Wywołanie:** `rootWidget = g_ui.getRootWidget()`

### `figSave`

**Wywołanie:** `vBotConfigSave("heal")`

### `umber`

**Wywołanie:** `local manaCost = tonumber(healWindow.healer.spells.manaCost:getText())`

### `umber`

**Wywołanie:** `local spellTrigger = tonumber(healWindow.healer.spells.spellValue:getText())`

### `umber`

**Wywołanie:** `local trigger = tonumber(healWindow.healer.items.itemValue:getText())`

### `figSave`

**Wywołanie:** `vBotConfigSave("heal")`

### `figSave`

**Wywołanie:** `vBotConfigSave("atk")`

### `figSave`

**Wywołanie:** `vBotConfigSave("atk")`

### `umber`

**Wywołanie:** `if not n or not tonumber(n) or n < 1 or n > 5 then`

### `PlayerHealthChange`

**Wywołanie:** `onPlayerHealthChange(function(healthPercent)`

### `ManaChange`

**Wywołanie:** `onManaChange(function(player, mana, maxMana, oldMana, oldMaxMana)`
