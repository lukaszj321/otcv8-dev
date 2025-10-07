# Moduł: Moduł: `inventory.lua`
**Rola:** *(krĂłtko â€“ 1â€“3 zdania co robi moduł i gdzie jest uĹĽywany).*

## Zakres
- â€¦

## Punkty wejścia
- **Lua:** â€¦
- **C++/IPC:** â€¦

## UI / OTUI
- Pliki OTUI: â€¦
- Kluczowe widĹĽety: â€¦

## Integracje i zaleĹĽności
- WspĂłłpracuje z: â€¦

## Scenariusze
1. â€¦
2. â€¦

## API (linki)
- [API Lua â†’ klient](../../api/lua/luafunctions_client.md)
- [Engine â†’ Spec UI](../../api/engine/otclient_v_8_specyfikacja_ui.md)

---

> **Uwagi migracyjne**
>
> Ten moduł pochodzi z: modules/modules_game_1.md

### Zaimportowana treść (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `toggleAdventurerStyle(hasBlessing)`
- `refresh()`
- `toggle()`
- `onMiniWindowClose()`
- `onInventoryChange(player, slot, item, oldItem)`
- `onBlessingsChange(player, blessings, oldBlessings)`
- `update()`
- `check()`
- `online()`
- `offline()`
- `onSetFightMode(self, selectedFightButton)`
- `onSetChaseMode(self, checked)`
- `onSetSafeFight(self, checked)`
- `onSetSafeFight2(self)`
- `onSetPVPMode(self, selectedPVPButton)`
- `onMountButtonClick(self, mousePos)`
- `onOutfitChange(localPlayer, outfit, oldOutfit)`
- `getPVPBoxByMode(mode)`
- `toggleIcon(bitChanged)`
- `loadIcon(bitChanged)`
- `onSoulChange(localPlayer, soul)`
- `onFreeCapacityChange(player, freeCapacity)`
- `onStatesChange(localPlayer, now, old)`


#### Eventy / Hooki

- `connect`
- `onAutoWalk`
- `onBlessingsChange`
- `onChaseModeChange`
- `onCheckChange`
- `onClick`
- `onFightModeChange`
- `onFreeCapacityChange`
- `onGameEnd`
- `onGameStart`
- `onInventoryChange`
- `onMiniWindowClose`
- `onMountButtonClick`
- `onOutfitChange`
- `onPVPModeChange`
- `onSafeFightChange`
- `onSelectionChange`
- `onSetChaseMode`
- `onSetFightMode`
- `onSetPVPMode`
- `onSetSafeFight`
- `onSetSafeFight2`
- `onSoulChange`
- `onStatesChange`
- `onWalk`
- `online`


#### Wywołania API

- `g_game`
- `g_keyboard`
- `g_ui`

---
