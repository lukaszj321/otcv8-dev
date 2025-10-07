# Realtime (websocket)

sequenceDiagram
  participant UI as Dashboard (SPA)
  participant WS as WebSocket (wss)
  participant S as Server (Node)

  UI->>WS: handshake (JWT / token)
  WS->>S: connect
  S-->>UI: events: metrics, logs, char_info
  UI->>S: cmd: START/STOP, settings

```
## Zasady

- **WSS** + origin allowlist + rate-limit.
- Autoryzacja w handshake (JWT / session).
- Walidacja schematow wiadomoLci.
## PrzykL'ad (Node + socket io)

io.use(authMiddleware);
io.on("connection", (s) => {
  s.join(`user:${s.user.id}`);
  s.on("cmd", (payload) => {
    /* validate + run */
  });
});
```
