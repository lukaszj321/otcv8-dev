# Architektura (skrot)

graph TD
  Client[OTCv8 Client] -->|Lua| vBot[vBot Modules]
  Client -->|OTUI| UI[UI System]
  Client --> CppCore[C++ Core]
  WS[WebSocket/IPC] --> Client

```

=== "Warstwy"

C++ Core - silnik render/UI/IO

Lua - logika moduAaasow (vBot)

OTUI - deklaratywne layouty

=== "Kontrakty"

Eventy Lua ALs UI, IPC/WS, zasoby
