# ModuĹ‚: `battle.lua`

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
- `toggle()`
- `onMiniWindowClose()`
- `getSortType()`
- `setSortType(state)`
- `getSortOrder()`
- `setSortOrder(state)`
- `isSortAsc()`
- `isSortDesc()`
- `isHidingFilters()`
- `setHidingFilters(state)`
- `hideFilterPanel()`
- `showFilterPanel()`
- `toggleFilterPanel()`
- `onChangeSortType(comboBox, option, value)`
- `onChangeSortOrder(comboBox, option, value)`
- `updateBattleList()`
- `checkCreatures()`
- `doCreatureFitFilters(creature)`
- `getDistanceBetween(p1, p2)`
- `sortCreatures(creatures)`
- `onBattleButtonMouseRelease(self, mousePosition, mouseButton)`
- `onBattleButtonHoverChange(battleButton, hovered)`
- `onPlayerPositionChange(creature, newPos, oldPos)`
- `updateSquare()`
- `local getDistanceBetween(p1, p2)`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onAppear`
- `onAttackingCreatureChange`
- `onBattleButtonHoverChange`
- `onBattleButtonMouseRelease`
- `onChangeSortOrder`
- `onChangeSortType`
- `onCreatureAppear`
- `onCreatureDisappear`
- `onDisappear`
- `onFollowed`
- `onFollowingCreatureChange`
- `onHoverChange`
- `onIdle`
- `onMiniWindowClose`
- `onMouseRelease`
- `onOptionChange`
- `onPlayerPositionChange`
- `onPositionChange`
- `onTargeted`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_map`
- `g_mouse`
- `g_ui`

---
