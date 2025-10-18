---
doc_id: 07_settings_crypto
source_path: docs/authoring/07_settings_crypto
source_sha: fab0cef
last_sync_iso: "2025-10-18T01:36:41.411933Z"
doc_class: spec
language: pl
title: 07 - Settings & Crypto
---


# 07 - Settings & Crypto

Settings formats, profiles, keys, and cryptographic flows.

## Przegląd

Ten rozdział dokumentuje 07 settings crypto w OTClient v8. Zawiera szczegółowe informacje techniczne, przykłady kodu, diagramy architektury oraz powiązania z innymi komponentami systemu.

## Zawartość

```{toctree}
:maxdepth: 2
:titlesonly:
:hidden:

README
blueprints/index
datasets/index
diagrams/index
```

## Cryptography API

OTClient v8 provides comprehensive cryptographic functions through the `g_crypt` singleton, exposed to Lua for secure data handling.

### Hash Functions

Used for integrity checking and password storage (with salt):

- **MD5** - Legacy; collision vulnerable
- **SHA1** - Deprecated; better than MD5
- **SHA256** - Recommended for checksums and hashes
- **SHA512** - Most secure hash; use for sensitive data
- **CRC32** - Fast non-cryptographic checksum

Example:
```lua
local hash = g_crypt.sha256Encode("my data", false)
-- Returns SHA256 hash in lowercase hex
```

### Symmetric Encryption

For encrypting local data:

- **encrypt()/decrypt()** - Uses machine UUID as key; binds to device
- **xorCrypt()** - Simple XOR; obfuscation only (NOT secure)

Example:
```lua
local encrypted = g_crypt.encrypt("sensitive data")
-- Decrypts only on same machine
local decrypted = g_crypt.decrypt(encrypted)
```

### Asymmetric Encryption (RSA)

Public key cryptography for server-client authentication:

- **rsaGenerateKey()** - Generate key pair
- **rsaSetPublicKey()** - Set public key for encryption
- **rsaSetPrivateKey()** - Set private key for decryption
- **rsaEncrypt()/rsaDecrypt()** - Perform RSA operations

### Machine Identity

- **getMachineUUID()** - Hardware-based identifier
- **genUUID()** - Generate random UUID v4

## Settings Management

Settings are stored in `config.otml` using OTML (OpenTibia Markup Language) format.

### Config API

```lua
-- Load config
g_configs.load("config.otml")

-- Read settings
local value = g_configs.get("graphics-engine")
local fps = g_configs.getNumber("max-fps")

-- Write settings
g_configs.set("vsync", true)
g_configs.set("max-fps", 144)

-- Save to disk
g_configs.save()
```

### Encrypted Settings

Sensitive settings like passwords use machine-specific encryption:

```lua
-- Store encrypted
local password = "user_password"
local encrypted = g_crypt.encrypt(password)
g_configs.set("saved-password", encrypted)
g_configs.save()

-- Retrieve and decrypt
local encrypted = g_configs.get("saved-password")
local password = g_crypt.decrypt(encrypted)
```

## Key Management Patterns

Different use cases require different cryptographic approaches:

| Use Case | Method | Security Level |
|----------|--------|----------------|
| Password Storage | SHA256 hash + salt | High |
| Auto-login Token | encrypt() with UUID | Medium |
| Session Token | SHA256 + random | High |
| API Key Obfuscation | Base64 + XOR | Very Low |
| License Verification | RSA signature | Very High |
| Save File Integrity | SHA256 checksum | Medium |

### Best Practices

1. **Never store plaintext passwords** - Always hash
2. **Use machine UUID encryption** for local-only secrets
3. **Rotate keys** when compromised
4. **Use SHA256 or better** for new code
5. **Add salt to hashes** to prevent rainbow tables

## Settings Migration

When updating client versions, settings may need migration:

1. **Detect old format** - Check version key
2. **Transform values** - Convert as needed
3. **Re-encrypt secrets** - Use new encryption if changed
4. **Preserve user data** - Don't reset unnecessarily
5. **Save migrated config** - Update version marker

Example migration flow:
```lua
local configVersion = g_configs.getNumber("config-version") or 1
if configVersion < 2 then
  -- Migrate old settings
  local oldEngine = g_configs.get("engine")
  g_configs.set("graphics-engine", oldEngine)
  g_configs.remove("engine")
  g_configs.set("config-version", 2)
  g_configs.save()
end
```

## Datasets

```{csv-table} Crypto API Functions
:header-rows: 1
:file: ./datasets/crypto_api.csv
```

```{csv-table} Key Management Patterns
:header-rows: 1
:file: ./datasets/key_management.csv
```

```{csv-table} Settings Migration Guide
:header-rows: 1
:file: ./datasets/settings_migration.csv
```

Legacy datasets:
- `crypto_primitives.csv`
- `entities.csv`
- `secrets.csv`
- `settings.csv`
- `summary.csv`

## Diagrams

```{mermaid}
:caption: Cryptography Flow
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
```

```{mermaid}
:caption: Settings Encryption Sequence
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
```

```{contents}
:local:
:depth: 2
```

## Crosslinks

Internal references:
- [Core API](../01_core/index.md) - C++ crypto implementation
- [Modules](../03_modules/index.md) - Lua config usage patterns
- [Network](../05_network/index.md) - RSA for protocol encryption
- [Runtime](../01_runtime/index.md) - Config loading at startup
- [Data](../11_data/index.md) - Config file location

External source files:
- `src/framework/util/crypt.h` - Cryptography class
- `src/framework/util/crypt.cpp` - Crypto implementation
- `src/framework/core/config.h` - Config manager
- `src/framework/core/config.cpp` - Settings persistence


## QA Block

**Status:** ✅ Dataset generated  
**Coverage:** In progress  
**Last Updated:** 2025-10-18T01:36:41.411933Z

### Checklist

- [x] Frontmatter present
- [x] Datasets generated
- [ ] Diagrams added
- [ ] Crosslinks verified
- [ ] Content complete (≥18KB target)

## Appendix / Facets

(facet-07_settings_crypto.main)=
### Facet: `07_settings_crypto.main`

Main documentation facet for 07_settings_crypto.

(facet-07_settings_crypto.crypto_api)=
### Facet: `07_settings_crypto.crypto_api`

Complete crypto API reference including hash functions (MD5, SHA1, SHA256, SHA512), symmetric encryption (encrypt/decrypt, XOR), asymmetric encryption (RSA), and machine identity functions.

(facet-07_settings_crypto.key_management)=
### Facet: `07_settings_crypto.key_management`

Key management patterns and best practices for different use cases including password storage, session tokens, API keys, license verification, and auto-login tokens.

(facet-07_settings_crypto.settings_migration)=
### Facet: `07_settings_crypto.settings_migration`

Settings migration guide covering common settings, storage locations, encryption requirements, and migration strategies for client version updates.