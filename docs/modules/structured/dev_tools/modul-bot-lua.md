# Moduł: Moduł: `bot.lua`
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
#### Funkcje

- `init()`
- `terminate()`
- `clear()`
- `refresh()`
- `save()`
- `onMiniWindowClose()`
- `toggle()`
- `online()`
- `offline()`
- `onError(message)`
- `edit()`
- `createDefaultConfigs()`
- `uploadConfig()`
- `downloadConfig()`
- `compressConfig(configName)`
- `decompressConfig(configName, archive)`
- `message(category, msg)`
- `check()`
- `initCallbacks()`
- `terminateCallbacks()`
- `safeBotCall(func)`
- `botKeyDown(widget, keyCode, keyboardModifiers)`
- `botKeyUp(widget, keyCode, keyboardModifiers)`
- `botKeyPress(widget, keyCode, keyboardModifiers, autoRepeatTicks)`
- `botOnTalk(name, level, mode, text, channelId, pos)`
- `botOnTextMessage(mode, text)`
- `botOnLoginAdvice(message)`
- `botAddThing(tile, thing)`
- `botRemoveThing(tile, thing)`
- `botCreatureAppear(creature)`
- `botCreatureDisappear(creature)`
- `botCreaturePositionChange(creature, newPos, oldPos)`
- `botCraetureHealthPercentChange(creature, healthPercent)`
- `botOnUse(pos, itemId, stackPos, subType)`
- `botOnUseWith(pos, itemId, target, subType)`
- `botContainerOpen(container, previousContainer)`
- `botContainerClose(container)`
- `botContainerUpdateItem(container, slot, item, oldItem)`
- `botOnMissle(missle)`
- `botOnAnimatedText(thing, text)`
- `botOnStaticText(thing, text)`
- `botChannelList(channels)`
- `botOpenChannel(channelId, name)`
- `botCloseChannel(channelId)`
- `botChannelEvent(channelId, name, event)`
- `botCreatureTurn(creature, direction)`
- `botCreatureWalk(creature, oldPos, newPos)`
- `botImbuementWindow(itemId, slots, activeSlots, imbuements, needItems)`
- `botModalDialog(id, title, message, buttons, enterButton, escapeButton, choices, priority)`
- `botGameEditText(id, itemId, maxLength, text, writer, time)`
- `botAttackingCreatureChange(creature, oldCreature)`
- `botManaChange(player, mana, maxMana, oldMana, oldMaxMana)`
- `botStatesChange(player, states, oldStates)`
- `botContainerAddItem(container, slot, item, oldItem)`
- `botContainerRemoveItem(container, slot, item)`
- `botSpellCooldown(iconId, duration)`
- `botGroupSpellCooldown(iconId, duration)`
- `botInventoryChange(player, slot, item, oldItem)`


#### Eventy / Hooki

- `connect`
- `onAddItem`
- `onAddThing`
- `onAnimatedText`
- `onAppear`
- `onAttackingCreatureChange`
- `onChannelEvent`
- `onChannelList`
- `onClick`
- `onClose`
- `onCloseChannel`
- `onContainerClose`
- `onContainerOpen`
- `onContainerUpdateItem`
- `onCreatureAppear`
- `onCreatureDisappear`
- `onCreatureHealthPercentChange`
- `onCreaturePositionChange`
- `onDisappear`
- `onError`
- `onGameEditText`
- `onGameEnd`
- `onGameStart`
- `onGroupSpellCooldown`
- `onHealthPercentChange`
- `onImbuementWindow`
- `onInventoryChange`
- `onKeyDown`
- `onKeyPress`
- `onKeyUp`
- `onLoginAdvice`
- `onManaChange`
- `onMiniWindowClose`
- `onMissle`
- `onModalDialog`
- `onOpen`
- `onOpenChannel`
- `onOptionChange`
- `onPositionChange`
- `onRemoveItem`
- `onRemoveThing`
- `onSpellCooldown`
- `onSpellGroupCooldown`
- `onStatesChange`
- `onStaticText`
- `onTalk`
- `onTextMessage`
- `onTurn`
- `onUpdateItem`
- `onUse`
- `onUseWith`
- `onWalk`
- `online`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_sounds`
- `g_ui`
