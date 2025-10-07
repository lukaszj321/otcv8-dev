# Architektura (skrďż˝t)

`$fenceInfo
graph TD
  Client[OTCv8 Client] -->|Lua| vBot[vBot Modules]
  Client -->|OTUI| UI[UI System]
  Client --> CppCore[C++ Core]
  WS[WebSocket/IPC] --> Client

```

=== "Warstwy"

C++ Core ďż˝ silnik render/UI/IO

Lua ďż˝ logika moduďż˝aâ€šďż˝w (vBot)

OTUI ďż˝ deklaratywne layouty

=== "Kontrakty"

Eventy Lua A?Lsďż˝ UI, IPC/WS, zasoby
