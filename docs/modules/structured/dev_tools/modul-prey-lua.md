# Moduł: Moduł: `prey.lua`
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
> Ten moduł pochodzi z: modules/modules_misc.md

### Zaimportowana treść (legacy)
#### Opis

-- sponsored by kivera-global.com

-- remade by Vithrax#5814


#### Funkcje

- `bonusDescription(bonusType, bonusValue, bonusGrade)`
- `timeleftTranslation(timeleft, forPreyTimeleft)`
- `init()`
- `onHover(widget)`
- `terminate()`
- `setUnsupportedSettings()`
- `check()`
- `toggleTracker()`
- `hide()`
- `show()`
- `toggle()`
- `onPreyFreeRolls(slot, timeleft)`
- `onPreyTimeLeft(slot, timeLeft)`
- `onPreyPrice(price)`
- `setTimeUntilFreeReroll(slot, timeUntilFreeReroll)`
- `onPreyLocked(slot, unlockState, timeUntilFreeReroll)`
- `onPreyInactive(slot, timeUntilFreeReroll)`
- `setBonusGradeStars(slot, grade)`
- `getBigIconPath(bonusType)`
- `getSmallIconPath(bonusType)`
- `getBonusDescription(bonusType)`
- `getTooltipBonusDescription(bonusType, bonusValue)`
- `capitalFormatStr(str)`
- `onItemBoxChecked(widget)`
- `onPreyActive(slot, currentHolderName, currentHolderOutfit, bonusType, bonusValue, bonusGrade, timeLeft, timeUntilFreeReroll, lockType)`
- `onPreySelection(slot, bonusType, bonusValue, bonusGrade, names, outfits, timeUntilFreeReroll)`
- `onResourceBalance(type, balance)`
- `showMessage(title, message)`


#### Eventy / Hooki

- `connect`
- `onClick`
- `onGameEnd`
- `onGameStart`
- `onHover`
- `onHoverChange`
- `onItemBoxChecked`
- `onPreyActive`
- `onPreyFreeRolls`
- `onPreyInactive`
- `onPreyLocked`
- `onPreyPrice`
- `onPreySelection`
- `onPreyTimeLeft`
- `onResourceBalance`
- `one`
- `only`


#### Wywołania API

- `g_game`
- `g_ui`

---
