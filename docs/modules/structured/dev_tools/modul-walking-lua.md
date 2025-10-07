# ModuĹ‚: `walking.lua`

**Rola:** *(krĂłtko â€“ 1â€“3 zdania co robi moduĹ‚ i gdzie jest uĹĽywany).*

## Zakres
- â€¦

## Punkty wejĹ›cia
- **Lua:** â€¦
- **C++/IPC:** â€¦

## UI / OTUI
- Pliki OTUI: â€¦
- Kluczowe widĹĽety: â€¦

## Integracje i zaleĹĽnoĹ›ci
- WspĂłĹ‚pracuje z: â€¦

## Scenariusze
1. â€¦
2. â€¦

## API (linki)
- [API Lua â†’ klient](../../api/lua/luafunctions_client.md)
- [Engine â†’ Spec UI](../../api/engine/otclient_v_8_specyfikacja_ui.md)

---

> **Uwagi migracyjne**
>
> Ten moduĹ‚ pochodzi z: modules/modules_misc.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `bindKeys()`
- `unbindKeys()`
- `enableWSAD()`
- `disableWSAD()`
- `bindWalkKey(key, dir)`
- `unbindWalkKey(key)`
- `bindTurnKey(key, dir)`
- `unbindTurnKey(key)`
- `stopSmartWalk()`
- `changeWalkDir(dir, pop)`
- `smartWalk(dir, ticks)`
- `canChangeFloorDown(pos)`
- `canChangeFloorUp(pos)`
- `onPositionChange(player, newPos, oldPos)`
- `onWalk(player, newPos, oldPos)`
- `onTeleport(player, newPos, oldPos)`
- `onWalkFinish(player)`
- `onCancelWalk(player)`
- `walk(dir, ticks)`
- `turn(dir, repeated)`
- `checkTurn()`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onCancelWalk`
- `onFocusChange`
- `onPositionChange`
- `onTeleport`
- `onWalk`
- `onWalkFinish`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_map`

---
