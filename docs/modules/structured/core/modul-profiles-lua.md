# Moduł: Moduł: `profiles.lua`
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

-- loads settings on character login

-- startup arguments has higher priority than settings


#### Funkcje

- `init()`
- `terminate()`
- `online()`
- `setProfileOption(index)`
- `getProfileFromSettings()`
- `getProfileFromStartupArgument()`
- `getSettingsFilePath(fileNameWithFormat)`
- `offline()`
- `onProfileChange(offline)`
- `collectiveReload()`
- `load()`
- `save()`


#### Eventy / Hooki

- `connect`
- `onError`
- `onGameEnd`
- `onGameStart`
- `onProfileChange`
- `online`
- `scheduleEvent`


#### Wywołania API

- `g_game`

---
