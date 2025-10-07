# Moduł: ModuĹ‚: `healthinfo.lua`
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
> Ten moduĹ‚ pochodzi z: modules/modules_misc.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `toggle()`
- `toggleIcon(bitChanged)`
- `loadIcon(bitChanged)`
- `offline()`
- `onMiniWindowClose()`
- `onHealthChange(localPlayer, health, maxHealth)`
- `onManaChange(localPlayer, mana, maxMana)`
- `onLevelChange(localPlayer, value, percent)`
- `onSoulChange(localPlayer, soul)`
- `onFreeCapacityChange(player, freeCapacity)`
- `onStatesChange(localPlayer, now, old)`
- `hideLabels()`
- `hideExperience()`
- `setHealthTooltip(tooltip)`
- `setManaTooltip(tooltip)`
- `setExperienceTooltip(tooltip)`
- `onOverlayGeometryChange()`


#### Eventy / Hooki

- `connect`
- `onFreeCapacityChange`
- `onGameEnd`
- `onGeometryChange`
- `onHealthChange`
- `onLevelChange`
- `onManaChange`
- `onMiniWindowClose`
- `onOverlayGeometryChange`
- `onSoulChange`
- `onStatesChange`


#### Wywołania API

- `g_game`
- `g_ui`

---
