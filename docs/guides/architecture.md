# Architektura (skrĂłt)

`$fenceInfo
graph TD
  Client[OTCv8 Client] -->|Lua| vBot[vBot Modules]
  Client -->|OTUI| UI[UI System]
  Client --> CppCore[C++ Core]
  WS[WebSocket/IPC] --> Client

```

=== "Warstwy"

C++ Core â€“ silnik render/UI/IO

Lua â€“ logika moduĂ„Ä…Ă˘â‚¬ĹˇĂłw (vBot)

OTUI â€“ deklaratywne layouty

=== "Kontrakty"

Eventy Lua Ä‚ËÄąĹźÂ· UI, IPC/WS, zasoby
