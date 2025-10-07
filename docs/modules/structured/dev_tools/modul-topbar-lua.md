# Moduł: ModuĹ‚: `topbar.lua`
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
- `setupTopBar()`
- `refresh(profileChange)`
- `refreshVisibleBars()`
- `setSkillsLayout()`
- `offline()`
- `toggleIcon(bitChanged)`
- `loadIcon(bitChanged)`
- `onHealthChange(localPlayer, health, maxHealth)`
- `onManaChange(localPlayer, mana, maxMana)`
- `onLevelChange(localPlayer, value, percent)`
- `onStatesChange(localPlayer, now, old)`
- `show()`
- `setupSkillPanel(id, parent, experience, defaultOff)`
- `menu(mouseButton)`
- `setupSkills()`
- `toggleSkillPanel(id)`
- `setSkillValue(id, value)`
- `setSkillPercent(id, percent, tooltip)`
- `setSkillBase(id, value, baseValue)`
- `onMagicLevelChange(localPlayer, magiclevel, percent)`
- `onBaseMagicLevelChange(localPlayer, baseMagicLevel)`
- `onSkillChange(localPlayer, id, level, percent)`
- `onBaseSkillChange(localPlayer, id, baseLevel)`
- `save()`
- `load()`


#### Eventy / Hooki

- `connect`
- `onBaseMagicLevelChange`
- `onBaseSkillChange`
- `onError`
- `onGameEnd`
- `onGameStart`
- `onGeometryChange`
- `onHealthChange`
- `onLevelChange`
- `onMagicLevelChange`
- `onManaChange`
- `onMouseRelease`
- `onSkillChange`
- `onStatesChange`


#### Wywołania API

- `g_game`
- `g_ui`

---
