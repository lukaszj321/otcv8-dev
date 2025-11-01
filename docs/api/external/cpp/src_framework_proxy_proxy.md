---
title: "src/framework/proxy/proxy.h"
source_file: "src/framework/proxy/proxy.h"
generated_at: "2025-11-01T08:45:15.317Z"
doc_type: "cpp_api"
---

# src/framework/proxy/proxy.h

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(isactive)=
## `isActive`

**Signature:**
```cpp
bool isActive();
```

**Returns:**
- `bool`

---

(addproxy)=
## `addProxy`

**Signature:**
```cpp
void addProxy(const std::string& host, uint16_t port, int priority);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `host` | - |
| `uint16_t` | `port` | - |
| `int` | `priority` | - |

---

(removeproxy)=
## `removeProxy`

**Signature:**
```cpp
void removeProxy(const std::string& host, uint16_t port);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `host` | - |
| `uint16_t` | `port` | - |

---

(addsession)=
## `addSession`

**Signature:**
```cpp
uint32_t addSession(uint16_t port, std::function<void(ProxyPacketPtr)> recvCallback, std::function<void(boost::system::error_code)> disconnectCallback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16_t` | `port` | - |
| `std::function&lt;void(ProxyPacketPtr)&gt;` | `recvCallback` | - |
| `std::function&lt;void(boost::system::error_code)&gt;` | `disconnectCallback` | - |

**Returns:**
- `uint32_t`

---

(removesession)=
## `removeSession`

**Signature:**
```cpp
void removeSession(uint32_t sessionId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `sessionId` | - |

---

(send)=
## `send`

**Signature:**
```cpp
void send(uint32_t sessionId, ProxyPacketPtr packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `sessionId` | - |
| `ProxyPacketPtr` | `packet` | - |

---

(getping)=
## `getPing`

**Signature:**
```cpp
int getPing();
```

**Returns:**
- `int`

---

(setmaxactiveproxies)=
## `setMaxActiveProxies`

**Signature:**
```cpp
void setMaxActiveProxies(int value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `value` | - |

---
