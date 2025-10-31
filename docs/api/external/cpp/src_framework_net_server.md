---
title: "src/framework/net/server.h"
source_file: "src/framework/net/server.h"
generated_at: "2025-10-31T23:33:30.351Z"
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

**Returns:**
- `public:`

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
- `static ServerPtr`

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
