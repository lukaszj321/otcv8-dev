# ModuĹ‚: `hotkeys_manager.lua`

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
- `online()`
- `offline()`
- `show()`
- `hide()`
- `toggle()`
- `ok()`
- `cancel()`
- `load(forceDefaults)`
- `unload()`
- `reset()`
- `reload()`
- `save()`
- `onConfigChange()`
- `loadDefautComboKeys()`
- `setDefaultComboKeys(combo)`
- `onChooseItemMouseRelease(self, mousePosition, mouseButton)`
- `startChooseItem()`
- `clearObject()`
- `addHotkey()`
- `addKeyCombo(keyCombo, keySettings, focus)`
- `prepareKeyCombo(keyCombo, ticks)`
- `doKeyCombo(keyCombo, repeated)`
- `updateHotkeyLabel(hotkeyLabel)`
- `updateHotkeyForm(reset)`
- `removeHotkey()`
- `updateHotkeyAction()`
- `onHotkeyTextChange(value)`
- `onSendAutomaticallyChange(autoSend)`
- `onChangeUseType(useTypeWidget)`
- `onSelectHotkeyLabel(hotkeyLabel)`
- `hotkeyCapture(assignWindow, keyCode, keyboardModifiers)`
- `hotkeyCaptureOk(assignWindow, keyCombo)`


#### Eventy / Hooki

- `connect`
- `onChangeUseType`
- `onChildFocusChange`
- `onChooseItemMouseRelease`
- `onConfigChange`
- `onGameEnd`
- `onGameStart`
- `onHotkeyTextChange`
- `onKeyDown`
- `onMouseRelease`
- `onSelectHotkeyLabel`
- `onSelectionChange`
- `onSendAutomaticallyChange`
- `online`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_mouse`
- `g_ui`

---
