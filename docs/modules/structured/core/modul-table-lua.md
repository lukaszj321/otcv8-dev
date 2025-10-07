# Moduł: Moduł: `table.lua`
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

-- @docclass table


#### Funkcje

- `table.dump(t, depth)`
- `table.clear(t)`
- `table.copy(t)`
- `table.recursivecopy(t)`
- `table.selectivecopy(t, keys)`
- `table.merge(t, src)`
- `table.find(t, value, lowercase)`
- `table.findbykey(t, key, lowercase)`
- `table.contains(t, value, lowercase)`
- `table.findkey(t, key)`
- `table.haskey(t, key)`
- `table.removevalue(t, value)`
- `table.popvalue(value)`
- `table.compare(t, other)`
- `table.empty(t)`
- `table.permute(t, n, count)`
- `table.findbyfield(t, fieldname, fieldvalue)`
- `table.size(t)`
- `table.tostring(t)`
- `table.collect(t, func)`
- `table.equals(t, comp)`
- `table.equal(t1,t2,ignore_mt)`
- `table.isList(t)`
- `table.isStringList(t)`
- `table.isStringPairList(t)`
- `table.encodeStringPairList(t)`
- `table.decodeStringPairList(l)`
