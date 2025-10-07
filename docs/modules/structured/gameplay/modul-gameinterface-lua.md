# Moduł: Moduł: `gameinterface.lua`
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
> Ten moduł pochodzi z: modules/modules_game_1.md

### Zaimportowana treść (legacy)
#### Funkcje

- `init()`
- `bindKeys()`
- `terminate()`
- `onGameStart()`
- `onGameEnd()`
- `show()`
- `hide()`
- `save()`
- `load()`
- `onLoginAdvice(message)`
- `forceExit()`
- `tryExit()`
- `tryLogout(prompt)`
- `updateStretchShrink()`
- `onMouseGrabberRelease(self, mousePosition, mouseButton)`
- `onUseWith(clickedWidget, mousePosition)`
- `onTradeWith(clickedWidget, mousePosition)`
- `startUseWith(thing, subType)`
- `startTradeWith(thing)`
- `isMenuHookCategoryEmpty(category)`
- `addMenuHook(category, name, callback, condition, shortcut)`
- `removeMenuHook(category, name)`
- `createThingMenu(menuPosition, lookThing, useThing, creatureThing)`
- `processMouseAction(menuPosition, mouseButton, autoWalkPos, lookThing, useThing, creatureThing, attackCreature, marking)`
- `moveStackableItem(item, toPos)`
- `getRootPanel()`
- `getMapPanel()`
- `getRightPanel()`
- `getLeftPanel()`
- `getContainerPanel()`
- `addRightPanel()`
- `addLeftPanel()`
- `removeRightPanel()`
- `removeLeftPanel()`
- `getBottomPanel()`
- `getBottomActionPanel()`
- `getLeftActionPanel()`
- `getRightActionPanel()`
- `getTopBar()`
- `refreshViewMode()`
- `limitZoom()`
- `updateSize()`
- `setupLeftActions()`
- `resetLeftActions()`
- `getLeftAction()`
- `isChatVisible()`
- `local addRightPanel()`
- `local addLeftPanel()`
- `local removeRightPanel()`
- `local removeLeftPanel()`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onClick`
- `onClose`
- `onEnter`
- `onEscape`
- `onExit`
- `onGameEnd`
- `onGameStart`
- `onGeometryChange`
- `onLeftPanelVisibilityChange`
- `onLoginAdvice`
- `onMapChangeAwareRange`
- `onMouseGrabberRelease`
- `onMouseRelease`
- `onRun`
- `onTouchRelease`
- `onTradeWith`
- `onUseWith`
- `onValueChange`
- `onVisibilityChange`
- `onVisibleDimensionChange`
- `online`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_map`
- `g_mouse`
- `g_ui`
- `g_window`

---
