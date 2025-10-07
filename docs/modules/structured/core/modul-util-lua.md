# Moduł: Moduł: `util.lua`
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

-- @docfuncs @{


#### Funkcje

- `print(...)`
- `pinfo(msg)`
- `perror(msg)`
- `pwarning(msg)`
- `pdebug(msg)`
- `fatal(msg)`
- `exit()`
- `quit()`
- `connect(object, arg1, arg2, arg3)`
- `disconnect(object, arg1, arg2)`
- `newclass(name)`
- `class.internalCreate()`
- `extends(base, name)`
- `derived.internalCreate()`
- `runinsandbox(func, ...)`
- `loadasmodule(name, file)`
- `module_loader(modname)`
- `import(table)`
- `export(what, key)`
- `unexport(key)`
- `getfsrcpath(depth)`
- `resolvepath(filePath, depth)`
- `toboolean(v)`
- `fromboolean(boolean)`
- `booleantonumber(boolean)`
- `numbertoboolean(number)`
- `protectedcall(func, ...)`
- `signalcall(param, ...)`
- `tr(s, ...)`
- `getOppositeAnchor(anchor)`
- `makesingleton(obj)`
- `comma_value(amount)`
- `local module_loader(modname)`


#### Eventy / Hooki

- `connect`

---
