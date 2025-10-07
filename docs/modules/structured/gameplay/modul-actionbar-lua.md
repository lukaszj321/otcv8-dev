# ModuĹ‚: `actionbar.lua`

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
#### Opis

-- servers may have different id's, change if not working properly (only for protocols 910+)

-- ek


#### Funkcje

- `translateVocation(id)`
- `isSpell(text)`
- `init()`
- `terminate()`
- `createActionBars()`
- `offline()`
- `online()`
- `show()`
- `refresh()`
- `translateHotkeyDesc(text)`
- `destroyAssignWindows()`
- `changeLockState(widget)`
- `moveActionButtons(widget)`
- `onDropActionButton(self, mousePosition, mouseButton)`
- `setupActionBar(n)`
- `setupButton(widget)`
- `resetSlot(widget)`
- `assignItem(widget)`
- `assignText(widget)`
- `assignSpell(widget)`
- `filterByVocation(a, filter)`
- `assignHotkey(widget)`
- `setupAction(widget)`
- `onSpellCooldown(iconId, duration)`
- `onSpellGroupCooldown(groupId, duration)`
- `startCooldown(action, duration)`
- `updateCooldown(action)`
- `save()`
- `load()`
- `local translateVocation(id)`
- `local isSpell(text)`
- `local filterByVocation(a, filter)`


#### Eventy / Hooki

- `connect`
- `onCheckChange`
- `onChildFocusChange`
- `onClick`
- `onDragEnter`
- `onDropActionButton`
- `onEnter`
- `onEscape`
- `onGameEnd`
- `onGameStart`
- `onItemChange`
- `onKeyDown`
- `onMouseRelease`
- `onMouseWheel`
- `onSelectionChange`
- `onSpellCooldown`
- `onSpellGroupCooldown`
- `onTextChange`
- `one`
- `online`
- `only`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_mouse`
- `g_ui`

---
