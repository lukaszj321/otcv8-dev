# Moduł: Moduł: `textedit.lua`
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

-- also works as show(text, callback)

-- callback = function(newText)


#### Funkcje

- `init()`
- `terminate()`
- `destroyWindow()`
- `show(text, options, callback)`
- `hide()`
- `edit(...)`
- `singlelineEditor(text, callback)`
- `multilineEditor(description, text, callback)`


#### Eventy / Hooki

- `connect`
- `onClick`
- `onDestroy`
- `onEnter`
- `onEscape`
- `onGameEnd`
- `onOptionChange`
- `onTextChange`


#### Wywołania API

- `g_ui`
- `g_window`

---
