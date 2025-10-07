# ModuĹ‚: `globals.lua`

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

-- @docvars @{

-- root widget

-- G is used as a global table to save variables in memory between reloads

-- @}

-- @docfuncs @{


#### Funkcje

- `scheduleEvent(callback, delay)`
- `addEvent(callback, front)`
- `cycleEvent(callback, interval)`
- `periodicalEvent(eventFunc, conditionFunc, delay, autoRepeatDelay)`
- `removeEvent(event)`


#### Eventy / Hooki

- `addEvent`
- `scheduleEvent`


#### Wywołania API

- `g_ui`
