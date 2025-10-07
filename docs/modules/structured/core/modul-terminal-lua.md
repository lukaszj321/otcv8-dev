# Moduł: Moduł: `terminal.lua`
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

-- configs

-- private variables


#### Funkcje

- `navigateCommand(step)`
- `completeCommand()`
- `doCommand(textWidget)`
- `addNewline(textWidget)`
- `onCommandChange(textWidget, newText, oldText)`
- `onLog(level, message, time)`
- `init()`
- `terminate()`
- `hideButton()`
- `popWindow()`
- `toggle()`
- `show()`
- `hide()`
- `disable()`
- `flushLines()`
- `addLine(text, color)`
- `terminalPrint(value)`
- `executeCommand(command)`
- `clear()`
- `local navigateCommand(step)`
- `local completeCommand()`
- `local doCommand(textWidget)`
- `local addNewline(textWidget)`
- `local onCommandChange(textWidget, newText, oldText)`
- `local onLog(level, message, time)`


#### Eventy / Hooki

- `connect`
- `onCommandChange`
- `onDoubleClick`
- `onLog`
- `onMouseWheel`
- `onScrollChange`
- `onTextChange`
- `one`
- `scheduleEvent`


#### Wywołania API

- `g_game`
- `g_keyboard`
- `g_ui`
- `g_window`

---
