---
title: "src/client/protocolcodes.h"
source_file: "src/client/protocolcodes.h"
generated_at: "2025-11-01T00:11:49.023Z"
doc_type: "cpp_api"
---

# src/client/protocolcodes.h

(buildmessagemodesmap)=
## `buildMessageModesMap`

**Signature:**
```cpp
void buildMessageModesMap(int version);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `version` | - |

---

(translatemessagemodefromserver)=
## `translateMessageModeFromServer`

**Signature:**
```cpp
Otc::MessageMode translateMessageModeFromServer(uint8 mode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `mode` | - |

**Returns:**
- `Otc::MessageMode`

---

(translatemessagemodetoserver)=
## `translateMessageModeToServer`

**Signature:**
```cpp
uint8 translateMessageModeToServer(Otc::MessageMode mode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::MessageMode` | `mode` | - |

**Returns:**
- `uint8`

---
