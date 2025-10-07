# ModuĹ‚: `outfit.lua`

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
- `onMovementChange(checkBox, checked)`
- `onShowFloorChange(checkBox, checked)`
- `onShowMountChange(checkBox, checked)`
- `onShowOutfitChange(checkBox, checked)`
- `onShowAuraChange(checkBox, checked)`
- `onShowWingsChange(checkBox, checked)`
- `onShowShaderChange(checkBox, checked)`
- `onShowBarsChange(checkBox, checked)`
- `create(currentOutfit, outfitList, mountList, wingList, auraList, shaderList, healthBarList, manaBarList)`
- `destroy()`
- `configureAddons(addons)`
- `newPreset()`
- `deletePreset()`
- `savePreset()`
- `renamePreset()`
- `saveRename(presetId)`
- `onAppearanceChange(widget, selectedWidget)`
- `showPresets()`
- `showOutfits()`
- `showMounts()`
- `showAuras()`
- `showWings()`
- `showShaders()`
- `showHealthBars()`
- `showManaBars()`
- `onPresetSelect(list, focusedChild, unfocusedChild, reason)`
- `onOutfitSelect(list, focusedChild, unfocusedChild, reason)`
- `onMountSelect(list, focusedChild, unfocusedChild, reason)`
- `onAuraSelect(list, focusedChild, unfocusedChild, reason)`
- `onWingsSelect(list, focusedChild, unfocusedChild, reason)`
- `onShaderSelect(list, focusedChild, unfocusedChild, reason)`
- `onHealthBarSelect(list, focusedChild, unfocusedChild, reason)`
- `onManaBarSelect(list, focusedChild, unfocusedChild, reason)`
- `updateAppearanceText(widget, text)`
- `updateAppearanceTexts(outfit)`
- `deselectPreset()`
- `onAddonChange(widget, checked)`
- `onColorModeChange(widget, selectedWidget)`
- `onColorCheckChange(widget, selectedWidget)`
- `updatePreview()`
- `rotate(value)`
- `onFilterSearch()`
- `saveSettings()`
- `loadSettings()`
- `loadDefaultSettings()`
- `accept()`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onAddonChange`
- `onAppearanceChange`
- `onAuraSelect`
- `onCheckChange`
- `onChildFocusChange`
- `onClick`
- `onColorCheckChange`
- `onColorModeChange`
- `onFilterSearch`
- `onGameEnd`
- `onHealthBarSelect`
- `onKeyPress`
- `onManaBarSelect`
- `onMountSelect`
- `onMovementChange`
- `onOpenOutfitWindow`
- `onOutfitSelect`
- `onPresetSelect`
- `onSelectionChange`
- `onShaderSelect`
- `onShowAuraChange`
- `onShowBarsChange`
- `onShowFloorChange`
- `onShowMountChange`
- `onShowOutfitChange`
- `onShowShaderChange`
- `onShowWingsChange`
- `onWingsSelect`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_ui`

---
