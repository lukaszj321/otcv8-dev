# Moduł: Moduł: `npctrade.lua`
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
- `show()`
- `hide()`
- `onItemBoxChecked(widget)`
- `onQuantityValueChange(quantity)`
- `onTradeTypeChange(radioTabs, selected, deselected)`
- `onTradeClick()`
- `onSearchTextChange()`
- `itemPopup(self, mousePosition, mouseButton)`
- `onBuyWithBackpackChange()`
- `onIgnoreCapacityChange()`
- `onIgnoreEquippedChange()`
- `onShowAllItemsChange()`
- `setCurrency(currency, decimal)`
- `setShowWeight(state)`
- `setShowYourCapacity(state)`
- `clearSelectedItem()`
- `getCurrentTradeType()`
- `getItemPrice(item, single)`
- `getSellQuantity(item)`
- `canTradeItem(item)`
- `refreshItem(item)`
- `refreshTradeItems()`
- `refreshPlayerGoods()`
- `onOpenNpcTrade(items)`
- `closeNpcTrade()`
- `onCloseNpcTrade()`
- `onPlayerGoods(money, items)`
- `onFreeCapacityChange(localPlayer, freeCapacity, oldFreeCapacity)`
- `onInventoryChange(inventory, item, oldItem)`
- `getTradeItemData(id, type)`
- `checkSellAllTooltip()`
- `formatCurrency(amount)`
- `getMaxAmount()`
- `sellAll(delayed, exceptions)`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onBuyWithBackpackChange`
- `onCloseNpcTrade`
- `onFreeCapacityChange`
- `onGameEnd`
- `onIgnoreCapacityChange`
- `onIgnoreEquippedChange`
- `onInventoryChange`
- `onItemBoxChecked`
- `onMouseRelease`
- `onOpenNpcTrade`
- `onPlayerGoods`
- `onQuantityValueChange`
- `onSearchTextChange`
- `onSelectionChange`
- `onShowAllItemsChange`
- `onTradeClick`
- `onTradeTypeChange`
- `scheduleEvent`


#### Wywołania API

- `g_game`
- `g_mouse`
- `g_ui`

---
