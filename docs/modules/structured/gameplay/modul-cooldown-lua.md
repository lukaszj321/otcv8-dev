# Moduł: Moduł: `cooldown.lua`
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
> Ten moduł pochodzi z: modules/modules_game_2.md

### Zaimportowana treść (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `loadIcon(iconId)`
- `onMiniWindowClose()`
- `toggle()`
- `online()`
- `refresh()`
- `removeCooldown(progressRect)`
- `turnOffCooldown(progressRect)`
- `initCooldown(progressRect, updateCallback, finishCallback)`
- `updateCooldown(progressRect, duration)`
- `isGroupCooldownIconActive(groupId)`
- `isCooldownIconActive(iconId)`
- `onSpellCooldown(iconId, duration)`
- `onSpellGroupCooldown(groupId, duration)`


#### Eventy / Hooki

- `connect`
- `onEffectEnd`
- `onGameStart`
- `onMiniWindowClose`
- `onSpellCooldown`
- `onSpellGroupCooldown`
- `online`
- `scheduleEvent`


#### Wywołania API

- `g_game`
- `g_ui`

---
