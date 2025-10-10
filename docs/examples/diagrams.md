# Diagramy (Mermaid)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
(diagram-overview)=
## Przegląd architektury

Ten dokument zawiera kluczowe diagramy ilustrujące architekturę i przepływy w OTClientV8.

(diagram-main-architecture)=
## Główna architektura systemu

```{mermaid}
flowchart TD
  A[Core Engine C++] --> B(Event System)
  A --> C(Module Loader)
  C --> D[UI Manager OTUI]
  C --> E[Network Protocol]
  E --> F[(Asset Manager)]
  B --> G{Settings/Crypto}
  G --> H[Audio System]
  H --> I[Logging Framework]
  I --> J[Game Runtime Loop]
  
  style A fill:#f9f,stroke:#333,stroke-width:4px
  style D fill:#bbf,stroke:#333,stroke-width:2px
  style E fill:#bfb,stroke:#333,stroke-width:2px
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
Poniżej przykład prostego schematu z użyciem **Mermaid**. Blok jest automatycznie renderowany podczas budowania dokumentacji.

```mermaid
flowchart TB
  A[Start] --> B{Decyzja?}
  B -- Tak --> C[Wykonaj akcję]
  B -- Nie --> D[Zakończ]
  C --> D
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
```

(diagram-module-lifecycle)=
## Cykl życia modułu

```{mermaid}
stateDiagram-v2
    [*] --> Unloaded
    Unloaded --> Loading: load()
    Loading --> Loaded: init()
    Loaded --> Running: onGameStart
    Running --> Loaded: onGameEnd
    Loaded --> Unloading: terminate()
    Unloading --> Unloaded: cleanup()
    Unloaded --> [*]
    
    Loading --> Error: Fail
    Error --> Unloaded: cleanup()
```

(diagram-event-flow)=
## Przepływ zdarzeń

```{mermaid}
sequenceDiagram
    participant Game as Game Engine
    participant EventSys as Event System
    participant Module1 as Module A
    participant Module2 as Module B
    participant UI as UI Layer
    
    Game->>EventSys: emit(onLogin)
    EventSys->>Module1: notify(onLogin)
    Module1->>Module1: processLogin()
    EventSys->>Module2: notify(onLogin)
    Module2->>UI: updateLoginStatus()
    UI-->>Game: render()
```

(diagram-network-stack)=
## Stos sieciowy

```{mermaid}
flowchart LR
    subgraph Client
        A[Application Layer] --> B[Protocol Handler]
        B --> C[Packet Queue]
        C --> D[Socket Layer]
    end
    
    subgraph Network
        D <--> E[TCP/IP]
    end
    
    subgraph Server
        E <--> F[Server Socket]
        F --> G[Protocol Parser]
        G --> H[Game Logic]
    end
    
    style Client fill:#e1f5ff
    style Network fill:#fff3e0
    style Server fill:#f3e5f5
```

(diagram-ui-hierarchy)=
## Hierarchia UI

```{mermaid}
graph TD
    Root[Root Widget] --> MainWindow[Main Window]
    Root --> TopMenu[Top Menu Bar]
    
    MainWindow --> GameInterface[Game Interface]
    MainWindow --> Console[Console Panel]
    
    GameInterface --> GameMap[Game Map Viewport]
    GameInterface --> Sidebar[Right Sidebar]
    
    Sidebar --> Inventory[Inventory]
    Sidebar --> Skills[Skills Panel]
    Sidebar --> VipList[VIP List]
    
    style Root fill:#ff9800
    style MainWindow fill:#4caf50
    style GameInterface fill:#2196f3
```

(diagram-asset-pipeline)=
## Pipeline assetów

```{mermaid}
flowchart TD
    A[Raw Assets] --> B{Asset Type?}
    B -->|Image| C[Texture Loader]
    B -->|Audio| D[Sound Loader]
    B -->|Font| E[Font Loader]
    B -->|Data| F[Data Parser]
    
    C --> G[Texture Cache]
    D --> H[Audio Buffer]
    E --> I[Font Cache]
    F --> J[Memory]
    
    G --> K[Renderer]
    H --> L[Audio Mixer]
    I --> K
    J --> M[Game Logic]
    
    style A fill:#ffeb3b
    style K fill:#4caf50
    style L fill:#2196f3
```

:::tip
Wszystkie diagramy są renderowane dynamicznie przez Mermaid i można je kopiować jako kod źródłowy.
:::

(see-also-diagrams)=
## Zobacz też

* [Architektura Core](../chapters/01_specyfikacja.md)
* [System zdarzeń](../chapters/02_events.md)
* [Moduły](../chapters/03_modules.md)
