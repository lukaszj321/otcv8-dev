# Moduł: ModuĹ‚: `http.lua`
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
#### Funkcje

- `HTTP.get(url, callback)`
- `HTTP.getJSON(url, callback)`
- `HTTP.post(url, data, callback)`
- `HTTP.postJSON(url, data, callback)`
- `HTTP.download(url, file, callback, progressCallback)`
- `HTTP.downloadImage(url, callback)`
- `HTTP.webSocket(url, callbacks, timeout, jsonWebsocket)`
- `HTTP.webSocketJSON(url, callbacks, timeout)`
- `HTTP.cancel(operationId)`
- `HTTP.onGet(operationId, url, err, data)`
- `HTTP.onGetProgress(operationId, url, progress)`
- `HTTP.onPost(operationId, url, err, data)`
- `HTTP.onPostProgress(operationId, url, progress)`
- `HTTP.onDownload(operationId, url, err, path, checksum)`
- `HTTP.onDownloadProgress(operationId, url, progress, speed)`
- `HTTP.onWsOpen(operationId, message)`
- `HTTP.onWsMessage(operationId, message)`
- `HTTP.onWsClose(operationId, message)`
- `HTTP.onWsError(operationId, message)`


#### Eventy / Hooki

- `connect`
- `onClose`
- `onDownload`
- `onDownloadProgress`
- `onError`
- `onGet`
- `onGetProgress`
- `onMessage`
- `onOpen`
- `onPost`
- `onPostProgress`
- `onWsClose`
- `onWsError`
- `onWsMessage`
- `onWsOpen`
