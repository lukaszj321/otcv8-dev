# Moduł: ModuĹ‚: `json.lua`
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

--
-- json.lua

--
-- Copyright (c) 2019 rxi

--
-- Permission is hereby granted, free of charge, to any person obtaining a copy of

-- this software and associated documentation files (the "Software"), to deal in

-- the Software without restriction, including without limitation the rights to

-- use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies

-- of the Software, and to permit persons to whom the Software is furnished to do

-- so, subject to the following conditions:


#### Funkcje

- `make_indent(state)`
- `escape_char(c)`
- `encode_nil()`
- `encode_table(val, state)`
- `encode_string(val)`
- `encode_number(val)`
- `json.encode(val, indent)`
- `create_set(...)`
- `next_char(str, idx, set, negate)`
- `decode_error(str, idx, msg)`
- `codepoint_to_utf8(n)`
- `parse_unicode_escape(s)`
- `parse_string(str, i)`
- `parse_number(str, i)`
- `parse_literal(str, i)`
- `parse_array(str, i)`
- `parse_object(str, i)`
- `json.decode(str)`
- `local make_indent(state)`
- `local escape_char(c)`
- `local encode_nil()`
- `local encode_table(val, state)`
- `local encode_string(val)`
- `local encode_number(val)`
- `local create_set(...)`
- `local next_char(str, idx, set, negate)`
- `local decode_error(str, idx, msg)`
- `local codepoint_to_utf8(n)`
- `local parse_unicode_escape(s)`
- `local parse_string(str, i)`
- `local parse_number(str, i)`
- `local parse_literal(str, i)`
- `local parse_array(str, i)`
- `local parse_object(str, i)`
