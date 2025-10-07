# Moduł: ModuĹ‚: `viplist.lua`
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
> Ten moduĹ‚ pochodzi z: modules/modules_game_2.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `loadVipInfo()`
- `saveVipInfo()`
- `refresh()`
- `clear()`
- `toggle()`
- `onMiniWindowClose()`
- `createAddWindow()`
- `createEditWindow(widget)`
- `destroyAddWindow()`
- `addVip()`
- `removeVip(widgetOrName)`
- `hideOffline(state)`
- `isHiddingOffline()`
- `getSortedBy()`
- `sortBy(state)`
- `onAddVip(id, name, state, description, iconId, notify)`
- `onVipStateChange(id, state)`
- `onVipListMousePress(widget, mousePos, mouseButton)`
- `onVipListLabelMousePress(widget, mousePos, mouseButton)`


#### Eventy / Hooki

- `connect`
- `onAddVip`
- `onClick`
- `onDoubleClick`
- `onEnter`
- `onEscape`
- `onGameEnd`
- `onGameStart`
- `onMiniWindowClose`
- `onMousePress`
- `onVipListLabelMousePress`
- `onVipListMousePress`
- `onVipStateChange`


#### Wywołania API

- `g_game`
- `g_keyboard`
- `g_ui`
- `g_window`

---
