# Moduł: Moduł: `entergame.lua`
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
> Ten moduł pochodzi z: modules/modules_core.md

### Zaimportowana treść (legacy)
#### Opis

-- private variables


#### Funkcje

- `onProtocolError(protocol, message, errorCode)`
- `onSessionKey(protocol, sessionKey)`
- `onCharacterList(protocol, characters, account, otui)`
- `onUpdateNeeded(protocol, signature)`
- `onProxyList(protocol, proxies)`
- `parseFeatures(features)`
- `validateThings(things)`
- `onTibia12HTTPResult(session, playdata)`
- `onHTTPResult(data, err)`
- `EnterGame.init()`
- `EnterGame.terminate()`
- `EnterGame.show()`
- `EnterGame.hide()`
- `EnterGame.openWindow()`
- `EnterGame.clearAccountFields()`
- `EnterGame.onServerChange()`
- `EnterGame.doLogin(account, password, token, host)`
- `EnterGame.doLoginHttp()`
- `EnterGame.onError(err)`
- `EnterGame.onLoginError(err)`
- `local onProtocolError(protocol, message, errorCode)`
- `local onSessionKey(protocol, sessionKey)`
- `local onCharacterList(protocol, characters, account, otui)`
- `local onUpdateNeeded(protocol, signature)`
- `local onProxyList(protocol, proxies)`
- `local parseFeatures(features)`
- `local validateThings(things)`
- `local onTibia12HTTPResult(session, playdata)`
- `local onHTTPResult(data, err)`


#### Eventy / Hooki

- `connect`
- `onCancel`
- `onCharacterList`
- `onError`
- `onHTTPResult`
- `onLoginError`
- `onOk`
- `onProtocolError`
- `onProxyList`
- `onServerChange`
- `onSessionKey`
- `onTibia12HTTPResult`
- `onUpdateNeeded`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_keyboard`
- `g_ui`

---
