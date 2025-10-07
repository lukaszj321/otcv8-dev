# Architektura (skrĂłt)

```mermaid
graph TD
  Client[OTCv8 Client] -->|Lua| vBot[vBot Modules]
  Client -->|OTUI| UI[UI System]
  Client --> CppCore[C++ Core]
  WS[WebSocket/IPC] --> Client

```

=== "Warstwy"

C++ Core â€“ silnik render/UI/IO

Lua â€“ logika moduĹ‚Ăłw (vBot)

OTUI â€“ deklaratywne layouty

=== "Kontrakty"

Eventy Lua âź· UI, IPC/WS, zasoby
