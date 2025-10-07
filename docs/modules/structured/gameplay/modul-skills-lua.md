# ModuĹ‚: `skills.lua`

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
> Ten moduĹ‚ pochodzi z: modules/modules_game_2.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Funkcje

- `init()`
- `terminate()`
- `expForLevel(level)`
- `expToAdvance(currentLevel, currentExp)`
- `resetSkillColor(id)`
- `toggleSkill(id, state)`
- `setSkillBase(id, value, baseValue)`
- `setSkillValue(id, value)`
- `setSkillColor(id, value)`
- `setSkillTooltip(id, value)`
- `setSkillPercent(id, percent, tooltip, color)`
- `checkAlert(id, value, maxValue, threshold, greaterThan)`
- `update()`
- `refresh()`
- `offline()`
- `toggle()`
- `checkExpSpeed()`
- `onMiniWindowClose()`
- `onSkillButtonClick(button)`
- `onExperienceChange(localPlayer, value)`
- `onLevelChange(localPlayer, value, percent)`
- `onHealthChange(localPlayer, health, maxHealth)`
- `onManaChange(localPlayer, mana, maxMana)`
- `onSoulChange(localPlayer, soul)`
- `onFreeCapacityChange(localPlayer, freeCapacity)`
- `onTotalCapacityChange(localPlayer, totalCapacity)`
- `onStaminaChange(localPlayer, stamina)`
- `onOfflineTrainingChange(localPlayer, offlineTrainingTime)`
- `onRegenerationChange(localPlayer, regenerationTime)`
- `onSpeedChange(localPlayer, speed)`
- `onBaseSpeedChange(localPlayer, baseSpeed)`
- `onMagicLevelChange(localPlayer, magiclevel, percent)`
- `onBaseMagicLevelChange(localPlayer, baseMagicLevel)`
- `onSkillChange(localPlayer, id, level, percent)`
- `onBaseSkillChange(localPlayer, id, baseLevel)`


#### Eventy / Hooki

- `connect`
- `onBaseMagicLevelChange`
- `onBaseSkillChange`
- `onBaseSpeedChange`
- `onExperienceChange`
- `onFreeCapacityChange`
- `onGameEnd`
- `onGameStart`
- `onHealthChange`
- `onLevelChange`
- `onMagicLevelChange`
- `onManaChange`
- `onMiniWindowClose`
- `onOfflineTrainingChange`
- `onRegenerationChange`
- `onSkillButtonClick`
- `onSkillChange`
- `onSoulChange`
- `onSpeedChange`
- `onStaminaChange`
- `onTotalCapacityChange`
- `only`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_ui`

---
