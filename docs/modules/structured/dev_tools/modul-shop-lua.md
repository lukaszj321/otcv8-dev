# ModuĹ‚: `shop.lua`

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
#### Opis

-- private variables

-- for classic store


#### Funkcje

- `sendAction(action, data)`
- `init()`
- `terminate()`
- `check()`
- `hide()`
- `show()`
- `softHide()`
- `showTransfer()`
- `hideTransfer()`
- `toggle()`
- `createShop()`
- `createTransferWindow()`
- `onStoreInit(url, coins)`
- `onStoreCategories(categories)`
- `onStoreOffers(categoryName, offers)`
- `onStoreTransactionHistory(currentPage, hasNextPage, offers)`
- `onStorePurchase(message)`
- `onStoreError(errorType, message)`
- `onCoinBalance(coins, transferableCoins)`
- `transferCoins()`
- `onExtendedJSONOpcode(protocol, code, json_data)`
- `clearOffers()`
- `clearCategories()`
- `clearHistory()`
- `processCategories(data)`
- `processHistory(data)`
- `processMessage(data)`
- `processStatus(data)`
- `processAd(data)`
- `addCategory(data)`
- `showHistory(force)`
- `addOffer(category, data)`
- `changeCategory(widget, newCategory)`
- `buyOffer(widget)`
- `buyConfirmed()`
- `buyCanceled()`
- `local sendAction(action, data)`


#### Eventy / Hooki

- `connect`
- `onChildFocusChange`
- `onClick`
- `onCoinBalance`
- `onDestroy`
- `onDoubleClick`
- `onExtendedJSONOpcode`
- `onGameEnd`
- `onGameStart`
- `onMouseRelease`
- `onStoreCategories`
- `onStoreError`
- `onStoreInit`
- `onStoreOffers`
- `onStorePurchase`
- `onStoreTransactionHistory`
- `scheduleEvent`


#### Wywołania API

- `g_game`
- `g_ui`

---
