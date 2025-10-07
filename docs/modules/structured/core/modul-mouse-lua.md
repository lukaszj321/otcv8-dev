# Moduł: Moduł: `mouse.lua`
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


#### Funkcje

- `g_mouse.bindAutoPress(widget, callback, delay, button)`
- `g_mouse.bindPressMove(widget, callback)`
- `g_mouse.bindPress(widget, callback, button)`


#### Eventy / Hooki

- `connect`
- `onMouseMove`
- `onMousePress`


#### Wywołania API

- `g_clock`
- `g_mouse`
- `g_window`
