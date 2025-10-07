# Moduł: ModuĹ‚: `topmenu.lua`
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
> Ten moduĹ‚ pochodzi z: modules/modules_core.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Opis

-- private variables

-- private functions


#### Funkcje

- `addButton(id, description, icon, callback, panel, toggle, front, index)`
- `init()`
- `terminate()`
- `online()`
- `offline()`
- `updateFps()`
- `updatePing(ping)`
- `setPingVisible(enable)`
- `setFpsVisible(enable)`
- `addLeftButton(id, description, icon, callback, front, index)`
- `addLeftToggleButton(id, description, icon, callback, front, index)`
- `addRightButton(id, description, icon, callback, front, index)`
- `addRightToggleButton(id, description, icon, callback, front, index)`
- `addLeftGameButton(id, description, icon, callback, front, index)`
- `addLeftGameToggleButton(id, description, icon, callback, front, index)`
- `addRightGameButton(id, description, icon, callback, front, index)`
- `addRightGameToggleButton(id, description, icon, callback, front, index)`
- `showGameButtons()`
- `hideGameButtons()`
- `getButton(id)`
- `getTopMenu()`
- `toggle()`
- `hide()`
- `show()`
- `updateStatus()`
- `local addButton(id, description, icon, callback, panel, toggle, front, index)`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onClick`
- `onGameEnd`
- `onGameStart`
- `onMouseRelease`
- `onPingBack`
- `onTouchRelease`
- `online`
- `onlineLabel`
- `scheduleEvent`


#### Wywołania API

- `g_game`
- `g_keyboard`
- `g_ui`

---
