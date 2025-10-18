---
title: 07_settings_crypto - Settings crypto
---

# 07_settings_crypto - Settings crypto

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### crypto_api
*Facet:* [`07_settings_crypto.crypto_api`](#facet-07_settings_crypto.crypto_api)

```{csv-table} crypto_api
:header-rows: 1
:file: ./datasets/crypto_api.csv
:widths: auto
```

### crypto_primitives
*Facet:* [`07_settings_crypto.crypto_primitives`](#facet-07_settings_crypto.crypto_primitives)

```{csv-table} crypto_primitives
:header-rows: 1
:file: ./datasets/crypto_primitives.csv
:widths: auto
```

### entities
*Facet:* [`07_settings_crypto.entities`](#facet-07_settings_crypto.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### key_management
*Facet:* [`07_settings_crypto.key_management`](#facet-07_settings_crypto.key_management)

```{csv-table} key_management
:header-rows: 1
:file: ./datasets/key_management.csv
:widths: auto
```

### secrets
*Facet:* [`07_settings_crypto.secrets`](#facet-07_settings_crypto.secrets)

```{csv-table} secrets
:header-rows: 1
:file: ./datasets/secrets.csv
:widths: auto
```

### settings
*Facet:* [`07_settings_crypto.settings`](#facet-07_settings_crypto.settings)

```{csv-table} settings
:header-rows: 1
:file: ./datasets/settings.csv
:widths: auto
```

### settings_migration
*Facet:* [`07_settings_crypto.settings_migration`](#facet-07_settings_crypto.settings_migration)

```{csv-table} settings_migration
:header-rows: 1
:file: ./datasets/settings_migration.csv
:widths: auto
```

### summary
*Facet:* [`07_settings_crypto.summary`](#facet-07_settings_crypto.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
*Facet:* [`07_settings_crypto.architecture`](#facet-07_settings_crypto.architecture)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Settings & Crypto
        E0[Settings]
        E1[Crypto Functions]
        E2[Config Options]
        E0 --> E1
        E1 --> E2
    end
click Architecture "./index.html#facet-07_settings_crypto.architecture" "Open architecture"
```

### config_flow
*Facet:* [`07_settings_crypto.config_flow`](#facet-07_settings_crypto.config_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[07_settings_crypto.config_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-07_settings_crypto.config_flow" "Open config_flow"
click ConfigFlow "./index.html#facet-07_settings_crypto.config_flow" "Open config_flow"
```

### crypto_flow
*Facet:* [`07_settings_crypto.crypto_flow`](#facet-07_settings_crypto.crypto_flow)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    Input[Sensitive Data] --> Choice{Security Need?}
    
    Choice -->|High| Hash[Hash Functions]
    Choice -->|Medium| Sym[Symmetric Encryption]
    Choice -->|Low| Obf[Obfuscation]
    
    Hash --> SHA256[SHA256/SHA512]
    Hash --> MD5[MD5 - Legacy Only]
    
    Sym --> MachineEnc[encrypt with UUID]
    Sym --> XOR[XOR Cipher]
    
    Obf --> Base64[Base64 Encoding]
    
    SHA256 --> Store1[Store Hash Only]
    MachineEnc --> Store2[Store Encrypted]
    Base64 --> Store3[Store Encoded]
    
    Store1 --> ConfigFile[config.otml]
    Store2 --> ConfigFile
    Store3 --> ConfigFile
    
    Retrieve[Retrieve Setting] --> Decrypt{Encrypted?}
    Decrypt -->|Yes| DecryptFunc[decrypt with UUID]
    Decrypt -->|No| Direct[Use Directly]
    
    DecryptFunc --> Use[Use Value]
    Direct --> Use
    
    click MachineEnc "./index.html#facet-07_settings_crypto.crypto_api" "Crypto API"
    click ConfigFile "./index.html#facet-07_settings_crypto.settings_migration" "Settings"
click CryptoFlow "./index.html#facet-07_settings_crypto.crypto_flow" "Open crypto_flow"
```

### crypto_overview
*Facet:* [`07_settings_crypto.crypto_overview`](#facet-07_settings_crypto.crypto_overview)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  CryptoOverview[07_settings_crypto:crypto_overview] --> Data[Datasets]
  Data --> Page[Index]

click CryptoOverview "./index.html#facet-07_settings_crypto.crypto_overview" "Open crypto_overview"
click CryptoOverview "./index.html#facet-07_settings_crypto.crypto_overview" "Open crypto_overview"
```

### flow
*Facet:* [`07_settings_crypto.flow`](#facet-07_settings_crypto.flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Settings & Crypto] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
click Flow "./index.html#facet-07_settings_crypto.flow" "Open flow"
```

### overview
*Facet:* [`07_settings_crypto.overview`](#facet-07_settings_crypto.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Settings & Crypto] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-07_settings_crypto.overview" "Open overview"
```

### settings_encryption_flow
*Facet:* [`07_settings_crypto.settings_encryption_flow`](#facet-07_settings_crypto.settings_encryption_flow)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
    participant User as User Action
    participant App as Application
    participant Config as Config Manager
    participant Crypt as g_crypt
    participant File as config.otml

    User->>App: Enable auto-login
    App->>App: Get current password
    
    App->>Crypt: getMachineUUID()
    Crypt-->>App: UUID
    
    App->>Crypt: encrypt(password)
    activate Crypt
    Crypt->>Crypt: Use UUID as key
    Crypt-->>App: Encrypted password
    deactivate Crypt
    
    App->>Config: setValue("saved-password", encrypted)
    Config->>File: Write to disk
    
    Note over File: Encrypted password stored
    
    User->>App: Restart client
    App->>Config: getValue("saved-password")
    Config->>File: Read from disk
    File-->>Config: Encrypted password
    Config-->>App: Encrypted password
    
    App->>Crypt: decrypt(encrypted)
    activate Crypt
    Crypt->>Crypt: Use UUID as key
    Crypt-->>App: Plaintext password
    deactivate Crypt
    
    App->>App: Auto-login with password
    %% click SettingsEncryptionFlow "./index.html#facet-07_settings_crypto.settings_encryption_flow" "Open settings_encryption_flow" %% REMOVED: click not supported in sequenceDiagram
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
```

## Crosslinks

- **affects** → `01_runtime.counters` (evidence: `docs/authoring/01_runtime/datasets/counters.csv`)
- **secures** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-07_settings_crypto.architecture)=
### Facet: `07_settings_crypto.architecture`
Type: diagram

(facet-07_settings_crypto.config_flow)=
### Facet: `07_settings_crypto.config_flow`
Type: diagram

(facet-07_settings_crypto.crypto_api)=
### Facet: `07_settings_crypto.crypto_api`
Type: dataset

(facet-07_settings_crypto.crypto_flow)=
### Facet: `07_settings_crypto.crypto_flow`
Type: diagram

(facet-07_settings_crypto.crypto_overview)=
### Facet: `07_settings_crypto.crypto_overview`
Type: diagram

(facet-07_settings_crypto.crypto_primitives)=
### Facet: `07_settings_crypto.crypto_primitives`
Type: dataset

(facet-07_settings_crypto.entities)=
### Facet: `07_settings_crypto.entities`
Type: dataset

(facet-07_settings_crypto.flow)=
### Facet: `07_settings_crypto.flow`
Type: diagram

(facet-07_settings_crypto.key_management)=
### Facet: `07_settings_crypto.key_management`
Type: dataset

(facet-07_settings_crypto.overview)=
### Facet: `07_settings_crypto.overview`
Type: diagram

(facet-07_settings_crypto.secrets)=
### Facet: `07_settings_crypto.secrets`
Type: dataset

(facet-07_settings_crypto.settings)=
### Facet: `07_settings_crypto.settings`
Type: dataset

(facet-07_settings_crypto.settings_encryption_flow)=
### Facet: `07_settings_crypto.settings_encryption_flow`
Type: diagram

(facet-07_settings_crypto.settings_migration)=
### Facet: `07_settings_crypto.settings_migration`
Type: dataset

(facet-07_settings_crypto.summary)=
### Facet: `07_settings_crypto.summary`
Type: dataset

