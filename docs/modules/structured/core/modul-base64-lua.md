# ModuĹ‚: `base64.lua`

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

-- v1.5.1 public domain Lua base64 encoder/decoder


#### Funkcje

- `base64.makeencoder( s62, s63, spad )`
- `base64.makedecoder( s62, s63, spad )`
- `base64.encode( str, encoder, usecaching )`
- `base64.decode( b64, decoder, usecaching )`
