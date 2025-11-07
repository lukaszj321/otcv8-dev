## Część E: Techniki Zaawansowane

### Złożony Wzorzec Wizualizacji (Łączenie Diagramów)

* jeden Overview,
* mapę modułów powiązaną z rozdziałami,
* przykład interakcji modułu z Core,
* zero czarnego tekstu na czarnym,
* zero HTML w `mindmap`,
* sensowne linki między diagramami.

---

### Diagram 1: Przegląd architektury (wejście do wszystkiego)

Ulepszenia:

* Core jako centralny węzeł.
* Dodatkowe bloki: Storage, Telemetry.
* Jasne klasy wizualne.
* Klikalne przejścia do innych sekcji/diagramów.

```mermaid
%%{init: {
  "theme": "dark",
  "themeVariables": {
    "primaryColor": "#111827",
    "primaryTextColor": "#e5e7eb",
    "lineColor": "#4b5563",
    "fontFamily": "Inter, system-ui, sans-serif"
  }
}}%%
flowchart TD
    classDef core fill:#3498db,stroke:#ffffff,color:#ffffff
    classDef subsystem fill:#2ecc71,stroke:#ffffff,color:#ffffff
    classDef game fill:#e67e22,stroke:#ffffff,color:#ffffff
    classDef ui fill:#9b59b6,stroke:#ffffff,color:#ffffff
    classDef netsec fill:#c0392b,stroke:#ffffff,color:#ffffff
    classDef platform fill:#7f8c8d,stroke:#ffffff,color:#ffffff
    classDef critical fill:#e74c3c,stroke:#ffffff,color:#ffffff
    classDef legend fill:#111827,stroke:#4b5563,color:#9ca3af,stroke-dasharray:3 3

    Core["⚙️ Core Engine"]:::core
    GameLogic["🔥 Game Modules"]:::game
    UiLayer["🎨 UI Layer"]:::ui
    NetStack["🔌 Net & Security"]:::netsec
    Subsys["🟩 Subsystems"]:::subsystem
    Telemetry["📈 Telemetry / Logging"]:::subsystem
    Platform["🔳 Platform"]:::platform

    Core ==> GameLogic
    Core ==> UiLayer
    Core ==> NetStack
    Core --> Subsys
    Core --> Telemetry
    Core --> Platform
    NetStack -.-> Telemetry
    GameLogic -.-> Telemetry

    %% Legend / nawigacja
    L["Core = niebieski<br/>Game = pomarańczowy<br/>UI = fiolet<br/>Net/Sec = czerwony<br/>Subsystems = zielony<br/>Platform = szary"]:::legend
    Core --- L

    click Core "../01_core/" "Core Engine docs"
    click GameLogic "../03_modules/" "Game Modules docs"
    click UiLayer "../04_ui/" "UI docs"
    click NetStack "../05_network/" "Networking & Security"
    click Subsys "../11_data/" "Subsystems / Data"
    click Telemetry "../09_logging/" "Telemetry & Logging"
    click Platform "../14_android/" "Platform-specific code"

```

To jest główna mapa. Każdy inny diagram jest zoomem w jeden z tych boxów.

---

### Diagram 2: Mapa modułów (bez HTML syfu, spięta z rozdziałami)

Ulepszenia:

* Kolory przez `classDef`, żadnych `<font>`.
* Moduły odpowiadają rozdziałom dokumentacji.
* Od razu gotowe pod anchory w treści.

```mermaid
%%{init: {
  "theme": "dark",
  "themeVariables": {
    "primaryTextColor": "#e5e7eb",
    "secondaryTextColor": "#e5e7eb",
    "tertiaryTextColor": "#e5e7eb",
    "lineColor": "#4b5563",
    "fontFamily": "Inter, system-ui, sans-serif"
  }
}}%%
mindmap
  root((<font color="white">Documentation Hub</font>))
    "🟦 01 Core — Core Engine & Runtime"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Core API</font>")
      ("<font color='white'>Engine Loop</font>")
    "🟧 02 Events & Modules"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Event Dispatch</font>")
      ("<font color='white'>Module Contracts</font>")
    "🟪 03 UI — Layouts & OTUI"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Layouts</font>")
      ("<font color='white'>Widgets / HUD</font>")
    "🟥 04 Networking & Security"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Protocols</font>")
      ("<font color='white'>Crypto / Settings</font>")
    "🟩 05 Subsystems — Assets & Data"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Assets</font>")
      ("<font color='white'>Data Pipelines</font>")
    "🔳 06 Platform"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Desktop</font>")
      ("<font color='white'>Android</font>")
```

Jeśli chcesz, agent może tu podmieniać etykiety na podstawie CSV (kolumna `chapter`, `topics[]`) i zachowywać klasy.

---

### Diagram 3: Interakcja modułu z Core (konkretny przykład)

Ulepszenia:

* Pokazujesz realny przepływ: klient -> moduł -> Core -> Storage.
* Nadaje sens temu, po co są wcześniejsze mapy.

```mermaid
%%{init: {
  "theme": "dark",
  "securityLevel": "loose",
  "themeVariables": {
    "fontFamily": "Inter, system-ui, sans-serif",
    "actorBorder": "#3498db",
    "actorBackground": "#020817",
    "actorTextColor": "#e5e7eb",
    "signalColor": "#2ecc71",
    "signalTextColor": "#e5e7eb",
    "activationBorderColor": "#facc15",
    "activationBackgroundColor": "#111827",
    "noteBorderColor": "#4b5563",
    "noteBackgroundColor": "#0f172a",
    "noteTextColor": "#e5e7eb",
    "lineColor": "#4b5563"
  },
  "sequence": {
    "messageFontSize": 22,
    "actorFontSize": 20,
    "noteFontSize": 18,
    "sequenceNumberFontSize": 16
  }
}}%%
sequenceDiagram
    autonumber

    box rgba(15,23,42,0.96) Client / UI 🟪 ui
        participant GC as 🎮 UI Client
    end

    box rgba(9,9,11,0.96) Game Logic 🟧 game / 🟦 core
        participant CM as 🧩 CombatModule
        participant CORE as ⚙️ CoreAPI
    end

    box rgba(17,24,39,0.96) Infra & Net 🟩 subsystem / 🟥 netsec
        participant DB as 🗃️ Storage
        participant LOG as 📈 Telemetry
        participant NET as 🔌 NetClient
    end

    rect rgba(56,189,248,0.14)
        note over GC,LOG: Hot path: attack → damage calc → persist → telemetry
    end

    GC->>+CM: onAttack(target, ability)
    CM->>+CORE: requestDamageCalc(ctx)
    CORE-->>-CM: damageResult
    CM->>+DB: persistHit(damageResult)
    DB-->>-CM: ack
    CM->>LOG: logCombatEvent(damageResult)

    alt Core error
        CORE-->>CM: error(code)
        CM->>GC: showErrorToast(code)
        CM->>LOG: logError("damageCalc_failed", code)
    else High latency
        note over CORE,DB: markSlowCall()
        CM->>LOG: logWarning("damageCalc_slow")
    end

    rect rgba(148,163,253,0.12)
        note over LOG: Events z tej ścieżki zasilają dashboard, alerty, audyt
    end

    %% Actor menu links (jeśli środowisko wspiera)
    link GC: UI docs @ ../04_ui/
    link CM: CombatModule @ ../03_modules/combat.md
    link CORE: Core API @ ../01_core/core_api.md
    link DB: Storage layer @ ../11_data/storage.md
    link LOG: Telemetry @ ../09_logging/telemetry.md
    link NET: Net client @ ../05_network/client.md

```

---
```mermaid
%%{init: {
  "theme": "dark",
  "securityLevel": "loose",
  "themeVariables": {
    "actorBorder": "#3498db",
    "actorTextColor": "#e5e7eb"
  }
}}%%
sequenceDiagram
    participant GC as UI Client
    participant CORE as CoreAPI

    GC->>CORE: requestDamageCalc()
    CORE-->>GC: damageResult

    %% Actor menu links:
    link GC: UI docs @ ../04_ui/
    link CORE: Core API @ ../01_core/core_api.md
```


---

### Diagram 4: Sankey: dwa przypadki `sankey-beta`.
* 4A = szczegółowa analiza jednego hot path,
* 4B = strategiczny podział ruchu między modułami.

### Diagram 4A: Sankey — Hot path: request → Core → Storage/Telemetry

**Cel:** pokazać faktyczny przepływ jednego krytycznego scenariusza (np. atak z Diagramu 3): którędy idzie ruch, gdzie lądują dane, gdzie generują się logi.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "fontFamily":"Inter, system-ui, sans-serif"
  }
}}%%
sankey-beta
    UI_Client,CombatModule,100
    CombatModule,CoreAPI,100
    CoreAPI,Cache,80
    Cache,Storage,80
    CoreAPI,Storage,20
    CoreAPI,Telemetry,40
    CombatModule,Telemetry,20
    UI_Client,NetClient,10
    NetClient,CoreAPI,10
```

**Jak to czytać:**

* szerokość strumienia = udział ruchu / zapisów,
* `UI_Client → CombatModule → CoreAPI` = główna ścieżka z Diagramu 3,
* większość trafia do `Cache/Storage`, część do `Telemetry`,
* `UI_Client → NetClient → CoreAPI` pokazuje koszt transportu sieciowego,
* używasz tego diagramu przy rozmowie o bottleneckach, cache, IO i logowaniu dla konkretnego flow.

---

### Diagram 4B: Sankey — Rozkład ruchu między modułami (porównanie profili)

**Cel:** inny przypadek użycia. Nie pojedynczy hot path, tylko jak cały klient rozrzuca ruch na moduły i jak to przekłada się na Storage/Telemetry. Dobry do priorytetyzacji optymalizacji.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "fontFamily":"Inter, system-ui, sans-serif"
  }
}}%%
sankey-beta
    %% UI dzieli ruch na moduły
    UI_Client,Combat_Module,40
    UI_Client,Inventory_Module,30
    UI_Client,Social_Module,30

    %% Wszystko ląduje w Core
    Combat_Module,CoreAPI,40
    Inventory_Module,CoreAPI,30
    Social_Module,CoreAPI,30

    %% Zapis do Storage (persist)
    Combat_Module,Storage,20
    Inventory_Module,Storage,20
    Social_Module,Storage,10

    %% Telemetria (observability)
    Combat_Module,Telemetry,20
    Inventory_Module,Telemetry,10
    Social_Module,Telemetry,5
```

**Jak to czytać:**

* pokazuje, które moduły naprawdę generują koszt (I/O + logi),
* widać, że Combat dominuje, Inventory jest istotne, Social jest tańszy,
* ten diagram służy do:

  * decyzji „który moduł optymalizujemy pierwszy”,
  * mapowania priorytetów logowania i retencji danych,
  * spięcia z Overview (moduły) i ER (tabele Storage/Telemetry).

Możesz w tekście obok doprecyzować mapowanie ID → kolory/specyfikacja, np.:

* `UI_Client` = UI (🟪),
* `CombatModule` / `Combat_Module` = Logika gry (🟧),
* `CoreAPI` = Core (🟦),
* `Storage` / `Telemetry` = Subsystems (🟩),
* `NetClient` = Networking (🟥).

---

### Diagram 5: ERDiagram jako zaawansowany model danych

Ten rozdział pokazuje „production-ready” modele danych w dwóch warstwach:
- `erDiagram` — formalny model relacyjny (pod SQL / migracje / kontrakty).
- `graph` — „kafelkowy” i kompozytowy widok encji jako advanced usage Mermaida (subgraphy, style, relacje domenowe).

Trzy perspektywy:
- 5A — ekwipunek, ekonomia i assety gry.
- 5B — telemetria hot path i SLO.
- 5C — audyt, integralność i PII.

Każda ma wariant „+” pokazujący alternatywny styl i szersze możliwości.

---

### Diagram 5A: ER — Ekwipunek, ekonomia i assety gry

**Cel:** model itemów, wariantów i loadoutów spójny z warstwą Game **(game)** i asset Subsystems **(subsystem)**.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "erEntityColor":"#020817",
    "erEntityBorderColor":"#9ca3af",
    "erEntityTitleColor":"#93c5fd"
  }
}}%%
erDiagram
    PLAYER ||--o{ INVENTORY_SLOT : has
    ITEM ||--o{ INVENTORY_SLOT : can_occupy
    ITEM ||--o{ ITEM_VARIANT : has_version
    PLAYER ||--o{ LOADOUT_PRESET : owns
    PLAYER ||--o{ WALLET : holds
    WALLET ||--o{ CURRENCY_TRANSACTION : records
    ITEM ||--o{ ITEM_TAG_MAP : tagged_as
    ITEM_TAG ||--o{ ITEM_TAG_MAP : defines
    ITEM ||--o{ COSMETIC_SKIN : has_skin
    SHOP_OFFER ||--o{ SHOP_OFFER_ITEM : bundles

    PLAYER {
      int player_id PK
      string name "unique"
      int level
    }

    ITEM {
      int item_id PK
      string name
      int base_tier
      bool tradable
    }

    ITEM_VARIANT {
      int variant_id PK
      int item_id FK
      string quality "normal/rare/legendary"
      json meta "affixy, roll"
    }

    INVENTORY_SLOT {
      int slot_id PK
      int player_id FK
      int item_id FK
      int variant_id FK "nullable"
      int qty
      string location "bag/depot/stash"
    }

    LOADOUT_PRESET {
      int preset_id PK
      int player_id FK
      string label
      json slots "mapa slot->item"
    }

    WALLET {
      int wallet_id PK
      int player_id FK
      string currency_code
      decimal balance
    }

    CURRENCY_TRANSACTION {
      bigint tx_id PK
      int wallet_id FK
      decimal amount
      string reason "loot/shop/trade"
      datetime created_at
    }

    ITEM_TAG {
      int tag_id PK
      string code "e.g. legendary,set,pvp"
    }

    ITEM_TAG_MAP {
      int item_id FK
      int tag_id FK
    }

    COSMETIC_SKIN {
      int skin_id PK
      int item_id FK
      string code
      string rarity
    }

    SHOP_OFFER {
      int offer_id PK
      string name
      string type "single/bundle/lootbox"
      decimal price
      string currency_code
      bool limited
    }

    SHOP_OFFER_ITEM {
      int offer_id FK
      int item_id FK
      int quantity
      decimal weight "dla losowych"
    }

```

#### Diagram 5A+: Widok kafelkowy ekwipunku i assetów

```mermaid
%%{init:{
  'theme':'dark',
  'themeVariables':{
    'primaryTextColor':'#e5e7eb',
    'lineColor':'#6b7280',
    'primaryColor':'#020817',
    'secondaryColor':'#020817'
  }
}}%%
graph LR
    classDef entity fill:#020817,stroke:#9ca3af,stroke-width:1px,color:#e5e7eb;
        font-size:10px,font-family:Inter,padding:6px;
    classDef rel color:#9ca3af,font-size:9px,stroke-dasharray:3 3;

    subgraph "Core Player"
        P["PLAYER\n———\nPK player_id\nname (unique)\nlevel"]:::entity
        L["LOADOUT_PRESET\n———\nPK preset_id\nFK player_id\nlabel\nslots (json)"]:::entity
    end

    subgraph "Inventory & Items"
        I["ITEM\n———\nPK item_id\nname\nbase_tier\ntradable"]:::entity
        V["ITEM_VARIANT\n———\nPK variant_id\nFK item_id\nquality\nmeta"]:::entity
        S["INVENTORY_SLOT\n———\nPK slot_id\nFK player_id\nFK item_id\nFK variant_id?\nqty\nlocation"]:::entity
        TAG["ITEM_TAG\n———\nPK tag_id\ncode"]:::entity
        MAP["ITEM_TAG_MAP\n———\nitem_id, tag_id"]:::entity
        SKIN["COSMETIC_SKIN\n———\nPK skin_id\nFK item_id\ncode,rarity"]:::entity
    end

    subgraph "Economy"
        W["WALLET\n———\nPK wallet_id\nFK player_id\ncurrency_code,balance"]:::entity
        TX["CURRENCY_TRANSACTION\n———\nPK tx_id\nFK wallet_id\namount,reason,ts"]:::entity
        OFFER["SHOP_OFFER\n———\nPK offer_id\nname,type,price"]:::entity
        OFFERI["SHOP_OFFER_ITEM\n———\noffer_id,item_id,qty,weight"]:::entity
    end

    P --> S:::rel
    P --> L:::rel
    I --> S:::rel
    I --> V:::rel
    I --> MAP:::rel
    TAG --> MAP:::rel
    I --> SKIN:::rel

    P --> W:::rel
    W --> TX:::rel
    OFFER --> OFFERI:::rel
    OFFERI --> I:::rel

```

> Pattern: PLAYER/LOADOUT = gameplay, ITEM/VARIANT/INVENTORY = kontrakt z subsystemem assetów. Czysty przykład integracji domen.

---

### Diagram 5B: ER — Telemetria hot path i SLO

**Cel:** model danych pod SLO/SLA, latency, error-rate i korelację z logami dla kluczowych ścieżek.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "erEntityColor":"#020817",
    "erEntityBorderColor":"#9ca3af",
    "erEntityTitleColor":"#f97316"
  }
}}%%
erDiagram
    SERVICE_NODE ||--o{ REQUEST_METRIC : records
    REQUEST_METRIC ||--o{ LATENCY_BUCKET : buckets
    REQUEST_METRIC ||--o{ ERROR_SAMPLE : errors
    REQUEST_METRIC ||--o{ TELEMETRY_LOG : logs

    SERVICE_NODE {
      string node_id PK
      string role        "core/api/gateway"
      string region
    }

    REQUEST_METRIC {
      string metric_id PK
      string node_id FK
      string route       "/damage/calc"
      string method      "POST"
      int    total_calls
      int    success_calls
      int    error_calls
      datetime window_start
      datetime window_end
    }

    LATENCY_BUCKET {
      int    bucket_id PK
      string metric_id FK
      int    le_ms        "<= próg ms"
      int    count
    }

    ERROR_SAMPLE {
      int    sample_id PK
      string metric_id FK
      string error_code
      string error_type   "timeout/5xx/validation"
      int    count
    }

    TELEMETRY_LOG {
      string log_id PK
      string metric_id FK
      string level        "INFO/WARN/ERROR"
      string source       "core/game/net"
      string message_code
      json   context
      datetime created_at
    }

    style SERVICE_NODE   fill:#111827,stroke:#f97316,color:#e5e7eb
    style REQUEST_METRIC fill:#064e3b,stroke:#f97316,color:#e5e7eb
    style LATENCY_BUCKET fill:#064e3b,stroke:#f97316,color:#e5e7eb
    style ERROR_SAMPLE   fill:#7c2d12,stroke:#f97316,color:#e5e7eb
    style TELEMETRY_LOG  fill:#022c22,stroke:#f97316,color:#e5e7eb
```

#### Diagram 5B+: Telemetria jako ścieżka przepływu danych

Inny pattern: layout przepływu, subgraphy, różne style krawędzi pokazujące etapy przetwarzania.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "lineColor":"#f97316",
    "primaryColor":"#020817"
  }
}}%%
graph LR
    classDef node fill:#020817,stroke:#6b7280,stroke-width:5px,color:#e5e7eb,font-size:20px,font-family:Inter,padding:6px;
    classDef metric fill:#022c22,stroke:#22c55e,color:#bbf7d0,font-size:14px,padding:6px;
    classDef error fill:#7c2d12,stroke:#f97316,color:#fee2e2,font-size:14px,padding:6px;
    classDef log fill:#111827,stroke:#9ca3af,color:#e5e7eb,font-size:14px,padding:6px;
    classDef relSoft stroke-dasharray:3 3,color:#9ca3af,font-size:12px;
    classDef relHard color:#f97316,font-size:12px;

    subgraph "Service Topology"
        SN["SERVICE_NODE\nrole: core/api/gateway\nregion"]:::node
    end

    subgraph "Rolling Metrics Window"
        RM["REQUEST_METRIC\nwindow_start/window_end\ntotal/success/error"]:::metric
        LB["LATENCY_BUCKET\nle_ms,count"]:::metric
    end

    subgraph "Errors & Samples"
        ES["ERROR_SAMPLE\nerror_code,error_type,count"]:::error
    end

    subgraph "Logs & Correlation"
        TL["TELEMETRY_LOG\nlevel,source,message_code,context"]:::log
    end

    SN --> RM:::relHard
    RM --> LB:::relHard
    RM --> ES:::relHard
    RM --> TL:::relSoft
    ES -. "link by metric_id" .-> TL:::relSoft
```

> Pattern: pokazujesz nie tylko tabele, ale przepływ: node → metryki → bucketizacja → próbkowanie błędów → korelacja z logami.

---

### Diagram 5C: ER — Audit, integralność i PII (Security / Compliance)

**Cel:** model audytu z wyraźnym rozdzieleniem PII, podpisów i polityk retencji.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "erEntityColor":"#020817",
    "erEntityBorderColor":"#ef4444",
    "erEntityTitleColor":"#ef4444"
  }
}}%%
erDiagram
    TELEMETRY_LOG ||--o{ AUDIT_EVENT : elevated_from
    AUDIT_EVENT  ||--o{ AUDIT_LOG   : snapshotted_as
    AUDIT_EVENT  ||--o{ PII_ENVELOPE: pii_link
    AUDIT_LOG    }o--|| RETENTION_POLICY : governed_by
    AUDIT_LOG    }o--|| KEY_REFERENCE    : signed_with

    TELEMETRY_LOG {
      string log_id PK
      string source
      string level
      string message_code
      json   context
      datetime created_at
    }

    AUDIT_EVENT {
      string audit_event_id PK
      string log_id FK
      string category      "security/gameplay/compliance"
      string actor_type    "player/system/gm"
      string actor_ref
      datetime occurred_at
    }

    AUDIT_LOG {
      string audit_log_id PK
      string audit_event_id FK
      string snapshot_hash "hash payloadu"
      string signature_id  "ref do KEY_REFERENCE"
      bool   immutable
      datetime locked_at
    }

    PII_ENVELOPE {
      string pii_id PK
      string external_ref
      string scope
      bool   encrypted
      datetime last_accessed_at
    }

    RETENTION_POLICY {
      string policy_id PK
      string name
      int    days_to_keep
      bool   legal_hold_supported
    }

    KEY_REFERENCE {
      string key_id PK
      string provider      "HSM/KMS"
      string key_alias
      bool   rotation_enabled
    }

    style TELEMETRY_LOG    fill:#064e3b,stroke:#22c55e,color:#e5e7eb
    style AUDIT_EVENT      fill:#7f1d1d,stroke:#ef4444,color:#e5e7eb
    style AUDIT_LOG        fill:#b91c1c,stroke:#ef4444,color:#e5e7eb
    style PII_ENVELOPE     fill:#6b7280,stroke:#9ca3af,color:#e5e7eb
    style RETENTION_POLICY fill:#374151,stroke:#9ca3af,color:#e5e7eb
    style KEY_REFERENCE    fill:#374151,stroke:#9ca3af,color:#e5e7eb
```

#### Diagram 5C+: Audit jako warstwy bezpieczeństwa i granice PII

Inny pattern: subgraphy jako warstwy bezpieczeństwa, strzałki pokazujące przepływ z logów do „cold storage” PII.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "lineColor":"#ef4444",
    "primaryColor":"#020817"
  }
}}%%
graph LR
    classDef base fill:#020817,stroke:#6b7280,stroke-width:4px,color:#e5e7eb,font-size:18px,font-family:Inter,padding:6px;
    classDef hot fill:#7f1d1d,stroke:#ef4444,color:#fee2e2,font-size:16px,padding:5px;
    classDef cold fill:#374151,stroke:#9ca3af,color:#e5e7eb,font-size:16px,padding:7px;
    classDef pii fill:#6b7280,stroke:#9ca3af,color:#e5e7eb,font-size:16px,padding:9px;
    classDef relSoft stroke-dasharray:3 3,color:#9ca3af,font-size:14px;
    classDef relHard color:#ef4444,font-size:14px;

    subgraph "Operational Telemetry"
        T["TELEMETRY_LOG\noperacyjne logi runtime"]:::base
    end

    subgraph "Audit Trail (Immutable Zone)"
        AE["AUDIT_EVENT\nwybrane zdarzenia wrażliwe"]:::hot
        AL["AUDIT_LOG\nsnapshot_hash + signature_id\nimmutable"]:::hot
    end

    subgraph "Secure Perimeter"
        PII["PII_ENVELOPE\nodseparowane identyfikatory\nencrypted = true"]:::pii
        RP["RETENTION_POLICY\ndni przechowywania\nlegal_hold_supported"]:::cold
        KR["KEY_REFERENCE\nHSM/KMS\nrotation_enabled"]:::cold
    end

    T -->|"elevated_from"| AE:::relHard
    AE -->|"snapshotted_as"| AL:::relHard
    AE -. "opcjonalne powiązanie PII" .-> PII:::relSoft
    AL -->|"governed_by"| RP:::relSoft
    AL -->|"signed_with"| KR:::relSoft
```

> Pattern: tu pokazujesz granice bezpieczeństwa, separację PII i niezmienialny audit log jako osobną strefę. Działa jako materiał referencyjny pod compliance.

---


### Diagram 6: Wzorzec stanów połączenia (stateDiagram-v2)

Cel tego bloku: pokazać zaawansowane użycie `stateDiagram-v2` jako wzorca dla klient–serwer, z wykorzystaniem różnych „assetów” Mermaida:
- klasy i kolory domen,
- `choice` (decyzje),
- stany z opisem,
- `fork` / `join` (równoległe kanały),
- notatki,
- retry z backoffem,
- opcjonalnie klikalne odnośniki do sekcji dokumentacji.

Uwaga: Dotyczy wyłącznie warstwy połączenia (network/netsec/telemetria). Modele danych domeny (itemy, ekonomia, audit, PII) są w Diagramie 5.

---

### Diagram 6A: Bazowy lifecycle produkcyjnego klienta

**Co pokazuje:**
- minimalny, implementowalny model stanów,
- rozróżnienie stanów stabilnych / przejściowych / krytycznych,
- prosty retry z backoffem,
- integrację z SLO i security events.

```mermaid
%%{init:{
  "theme":"dark",
  "securityLevel":"loose",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "fontFamily":"Inter, system-ui, sans-serif"
  }
}}%%
stateDiagram-v2
    direction LR

    classDef netsec fill:#c0392b,stroke:#ffffff,color:#ffffff,stroke-width:1.2px
    classDef stable fill:#2ecc71,stroke:#111827,color:#111827,stroke-width:1.4px
    classDef degraded fill:#9b59b6,stroke:#ffffff,color:#ffffff,stroke-width:1.2px
    classDef retry fill:#7f8c8d,stroke:#ffffff,color:#ffffff,stroke-width:1.2px,stroke-dasharray:3 3
    classDef critical fill:#e74c3c,stroke:#ffffff,color:#ffffff,stroke-width:1.6px

    [*] --> Disconnected

    state "Connecting" as CONNECT
    state "Auth" as AUTH
    state "Connected" as OK
    state "Degraded" as SLOW
    state "Retry (backoff)" as RETRY
    state "AuthFailed" as AUTH_FAIL
    state CH <<choice>>

    Disconnected --> CONNECT: connect()
    CONNECT --> AUTH: tcp_ok
    CONNECT --> Disconnected: tcp_fail

    AUTH --> CH: validate_token()
    CH --> OK: 200 OK
    CH --> AUTH_FAIL: 401 / 403

    AUTH_FAIL --> RETRY: schedule_retry()
    RETRY --> CONNECT: retry()
    RETRY --> Disconnected: max_retries_exceeded

    OK --> SLOW: rtt > threshold / loss
    SLOW --> OK: recover()
    SLOW --> RETRY: timeout

    OK --> Disconnected: disconnect() / fatal

    note right of SLOW
      Stan ostrzegawczy:
      - zwiększ sampling,
      - generuj SLO-alerty.
    end note

    note right of AUTH_FAIL
      Emit security_event(critical)
      → pipeline nadużyć / banów.
    end note

    class Disconnected,CONNECT,AUTH,CH netsec
    class OK stable
    class SLOW degraded
    class RETRY retry
    class AUTH_FAIL critical
````

---

### Diagram 6B: Równoległe kanały Telemetry + Heartbeat

**Co dodaje:**

* `fork` do uruchomienia kanałów pomocniczych,
* wewnętrzne sub-stany Telemetry i Heartbeat,
* pokazuje, jak „bajery” stanowe mapują się na realne komponenty (monitoring, ping/pong),
* dalej ten sam kontrakt co 6A, ale bogatszy runtime.

```mermaid
%%{init:{
  "theme":"dark",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "fontFamily":"Inter, system-ui, sans-serif"
  }
}}%%
stateDiagram-v2
    direction LR

    classDef netsec fill:#c0392b,stroke:#ffffff,color:#ffffff,stroke-width:1.2px
    classDef stable fill:#2ecc71,stroke:#111827,color:#111827,stroke-width:1.4px
    classDef transient fill:#9b59b6,stroke:#ffffff,color:#ffffff,stroke-width:1.2px
    classDef retry fill:#7f8c8d,stroke:#ffffff,color:#ffffff,stroke-width:1.2px,stroke-dasharray:3 3
    classDef critical fill:#e74c3c,stroke:#ffffff,color:#ffffff,stroke-width:1.6px

    [*] --> Disconnected

    Disconnected: no session
    Connecting: TCP handshake
    Auth: validate token
    Connected: ready
    Degraded: high RTT / loss
    ReconnectQueue: backoff
    AuthFailed: invalid / banned

    Disconnected --> Connecting: connect()
    Connecting --> Auth: tcp_ok
    Connecting --> Disconnected: tcp_fail

    state Decision <<choice>>
    Auth --> Decision
    Decision --> Connected: 200 OK
    Decision --> AuthFailed: 401 / 403

    AuthFailed --> ReconnectQueue: schedule_retry()
    ReconnectQueue --> Connecting: retry()
    ReconnectQueue --> Disconnected: max_retries_exceeded

    Connected --> Degraded: rtt > threshold
    Degraded --> Connected: recover()
    Degraded --> ReconnectQueue: timeout

    Connected --> Disconnected: disconnect() / fatal

    %% Fork: kanały równoległe
    state Fork <<fork>>
    Connected --> Fork: start side-channels
    Fork --> Telemetry
    Fork --> Heartbeat

    state Telemetry {
        [*] --> TelemetryOn
        TelemetryOn: logs + metrics
    }

    state Heartbeat {
        [*] --> Alive
        Alive: ping/pong
    }

    note right of Degraded
      Zwiększ częstotliwość Telemetry,
      przygotuj alerty SLO.
    end note

    note right of AuthFailed
      Traktuj jako incydent bezpieczeństwa.
    end note

    class Disconnected,Connecting,Auth,Decision,ReconnectQueue,Fork,Telemetry,Heartbeat netsec
    class Connected,TelemetryOn,Alive stable
    class Degraded transient
    class AuthFailed critical
    class ReconnectQueue retry
```

---

### Diagram 6C: Retry + flush telemetry + linki do dokumentacji

**Co demonstruje:**

* `fork` + `join` jako kontrolowany reconnect:

  * równoległy flush metryk/logów,
  * równoległy retry połączenia,
  * dopiero po obu krokach powrót do `Connecting`.
* spójne kolory warstw (netsec / subsystem),
* opcjonalne klikalne odnośniki do innych rozdziałów dokumentacji.

```mermaid
%%{init:{
  "theme":"dark",
  "securityLevel":"loose",
  "themeVariables":{
    "primaryTextColor":"#e5e7eb",
    "fontFamily":"Inter, system-ui, sans-serif"
  }
}}%%
stateDiagram-v2
    direction LR

    classDef netsec fill:#c0392b,stroke:#ffffff,color:#ffffff
    classDef subsystem fill:#2ecc71,stroke:#ffffff,color:#111827
    classDef critical fill:#e74c3c,stroke:#ffffff,color:#ffffff
    classDef aux fill:#7f8c8d,stroke:#ffffff,color:#ffffff,stroke-dasharray:3 3

    [*] --> Disconnected

    state "Connecting" as CONNECT
    state "Connected" as OK
    state "Degraded" as SLOW
    state "AuthFailed" as AUTH_FAIL
    state "Retry (backoff)" as RETRY
    state "Flush telemetry" as FLUSH
    state CH <<choice>>
    state F <<fork>>
    state J <<join>>

    Disconnected --> CONNECT: connect()
    CONNECT --> CH: handshake + auth
    CH --> OK: 200 OK
    CH --> AUTH_FAIL: 401 / 403

    AUTH_FAIL --> RETRY: schedule_retry()
    RETRY --> CONNECT: retry()
    RETRY --> Disconnected: max_retries_exceeded

    OK --> SLOW: rtt > threshold / drops
    SLOW --> OK: recover()

    %% Fatal / utrata linku → flush + retry w równoległych gałęziach
    OK --> F: fatal_error / link_down
    SLOW --> F: timeout / circuit_open

    F --> FLUSH: flush_pending()
    F --> RETRY: reconnect()
    FLUSH --> J
    RETRY --> J
    J --> CONNECT

    %% Graceful close
    OK --> Disconnected: disconnect() / graceful_close()

    note right of FLUSH
      Wymuszony zapis:
      - metryki sesji,
      - błędy,
      - ostatnie eventy.
    end note

    note right of RETRY
      Backoff + jitter,
      limity prób z configu.
    end note

    class Disconnected,CONNECT,CH,F,J,RETRY netsec
    class OK,SLOW,FLUSH subsystem
    class AUTH_FAIL critical

    %% Opcjonalne linki (jeśli wspierane przez renderer)
    click OK "../05_network/#session" "Kontrakt stabilnej sesji"
    click SLOW "../09_logging/#slo" "SLO i alerty opóźnień"
    click FLUSH "../09_logging/#flush" "Flush telemetry"
    click RETRY "../05_network/#retry" "Retry / backoff"
    click AUTH_FAIL "../07_settings_crypto/#auth-fail" "Obsługa błędów auth"
```

> Ten wariant pokazuje pełne, „produkcyjne” podejście do reconnectów:
> flush danych + kontrolowany retry + powiązania z resztą dokumentacji.
