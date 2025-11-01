---
title: "src/framework/net/server.h"
source_file: "src/framework/net/server.h"
generated_at: "2025-11-01T08:45:15.313Z"
doc_type: "cpp_api"
---

# src/framework/net/server.h

(server)=
## `Server`

**Signature:**
```cpp
public: Server(int port);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `port` | - |

---

(create)=
## `create`

**Signature:**
```cpp
static ServerPtr create(int port);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `port` | - |

**Returns:**
- `ServerPtr`

---

(close)=
## `close`

**Signature:**
```cpp
void close();
```

---

(acceptnext)=
## `acceptNext`

**Signature:**
```cpp
void acceptNext();
```

---

(isopen)=
## `isOpen`

**Signature:**
```cpp
bool isOpen();
```

**Returns:**
- `bool`

---
