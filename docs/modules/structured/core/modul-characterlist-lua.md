# Moduł: ModuĹ‚: `characterlist.lua`
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
> Ten moduĹ‚ pochodzi z: modules/modules_core.md

### Zaimportowana treĹ›Ä‡ (legacy)
#### Opis

-- private variables

-- private functions


#### Funkcje

- `tryLogin(charInfo, tries)`
- `updateWait(timeStart, timeEnd)`
- `resendWait()`
- `onLoginWait(message, time)`
- `onGameLoginError(message)`
- `onGameLoginToken(unknown)`
- `onGameConnectionError(message, code)`
- `onGameUpdateNeeded(signature)`
- `onGameEnd()`
- `onLogout()`
- `scheduleAutoReconnect()`
- `executeAutoReconnect()`
- `CharacterList.init()`
- `CharacterList.terminate()`
- `CharacterList.create(characters, account, otui)`
- `CharacterList.destroy()`
- `CharacterList.show()`
- `CharacterList.hide(showLogin)`
- `CharacterList.showAgain()`
- `CharacterList.isVisible()`
- `CharacterList.doLogin()`
- `CharacterList.destroyLoadBox()`
- `CharacterList.cancelWait()`
- `local tryLogin(charInfo, tries)`
- `local updateWait(timeStart, timeEnd)`
- `local resendWait()`
- `local onLoginWait(message, time)`


#### Eventy / Hooki

- `addEvent`
- `connect`
- `onCancel`
- `onChildFocusChange`
- `onClick`
- `onConnectionError`
- `onDoubleClick`
- `onGameConnectionError`
- `onGameEnd`
- `onGameLoginError`
- `onGameLoginToken`
- `onGameStart`
- `onGameUpdateNeeded`
- `onLoginError`
- `onLoginToken`
- `onLoginWait`
- `onLogout`
- `onOk`
- `onUpdateNeeded`
- `scheduleEvent`


#### Wywołania API

- `g_clock`
- `g_game`
- `g_ui`
