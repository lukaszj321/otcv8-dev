# Moduł: Moduł: `marketprotocol.lua`
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

-- private functions


#### Funkcje

- `send(msg)`
- `readMarketOffer(msg, action, var)`
- `parseMarketEnter(protocol, msg)`
- `parseMarketLeave(protocol, msg)`
- `parseMarketDetail(protocol, msg)`
- `parseMarketBrowse(protocol, msg)`
- `initProtocol()`
- `terminateProtocol()`
- `MarketProtocol.updateProtocol(_protocol)`
- `MarketProtocol.registerProtocol()`
- `MarketProtocol.unregisterProtocol()`
- `MarketProtocol.silent(mode)`
- `MarketProtocol.sendMarketLeave()`
- `MarketProtocol.sendMarketBrowse(browseId)`
- `MarketProtocol.sendMarketBrowseMyOffers()`
- `MarketProtocol.sendMarketBrowseMyHistory()`
- `MarketProtocol.sendMarketCreateOffer(type, spriteId, amount, price, anonymous)`
- `MarketProtocol.sendMarketCancelOffer(timestamp, counter)`
- `MarketProtocol.sendMarketAcceptOffer(timestamp, counter, amount)`
- `local send(msg)`
- `local readMarketOffer(msg, action, var)`
- `local parseMarketEnter(protocol, msg)`
- `local parseMarketLeave(protocol, msg)`
- `local parseMarketDetail(protocol, msg)`
- `local parseMarketBrowse(protocol, msg)`


#### Eventy / Hooki

- `connect`
- `onGameEnd`
- `onGameStart`
- `onMarketBrowse`
- `onMarketDetail`
- `onMarketEnter`
- `onMarketLeave`


#### Wywołania API

- `g_game`
