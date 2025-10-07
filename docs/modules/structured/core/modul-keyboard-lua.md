# Moduł: Moduł: `keyboard.lua`
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
> Ten moduł pochodzi z: modules/modules_core.md

### Zaimportowana treść (legacy)
#### Opis

-- @docclass

-- private functions


#### Funkcje

- `translateKeyCombo(keyCombo)`
- `getKeyCode(key)`
- `retranslateKeyComboDesc(keyComboDesc)`
- `determineKeyComboDesc(keyCode, keyboardModifiers)`
- `onWidgetKeyDown(widget, keyCode, keyboardModifiers)`
- `onWidgetKeyUp(widget, keyCode, keyboardModifiers)`
- `onWidgetKeyPress(widget, keyCode, keyboardModifiers, autoRepeatTicks)`
- `connectKeyDownEvent(widget)`
- `connectKeyUpEvent(widget)`
- `connectKeyPressEvent(widget)`
- `g_keyboard.bindKeyDown(keyComboDesc, callback, widget, alone)`
- `g_keyboard.bindKeyUp(keyComboDesc, callback, widget, alone)`
- `g_keyboard.bindKeyPress(keyComboDesc, callback, widget)`
- `getUnbindArgs(arg1, arg2)`
- `g_keyboard.unbindKeyDown(keyComboDesc, arg1, arg2)`
- `g_keyboard.unbindKeyUp(keyComboDesc, arg1, arg2)`
- `g_keyboard.unbindKeyPress(keyComboDesc, arg1, arg2)`
- `g_keyboard.getModifiers()`
- `g_keyboard.isKeyPressed(key)`
- `g_keyboard.areKeysPressed(keyComboDesc)`
- `g_keyboard.isKeySetPressed(keys, all)`
- `g_keyboard.isInUse()`
- `g_keyboard.isCtrlPressed()`
- `g_keyboard.isAltPressed()`
- `g_keyboard.isShiftPressed()`
- `local getKeyCode(key)`
- `local onWidgetKeyDown(widget, keyCode, keyboardModifiers)`
- `local onWidgetKeyUp(widget, keyCode, keyboardModifiers)`
- `local onWidgetKeyPress(widget, keyCode, keyboardModifiers, autoRepeatTicks)`
- `local connectKeyDownEvent(widget)`
- `local connectKeyUpEvent(widget)`
- `local connectKeyPressEvent(widget)`
- `local getUnbindArgs(arg1, arg2)`


#### Eventy / Hooki

- `connect`
- `onKeyDown`
- `onKeyPress`
- `onKeyUp`
- `onWidgetKeyDown`
- `onWidgetKeyPress`
- `onWidgetKeyUp`


#### Wywołania API

- `g_keyboard`
- `g_window`
