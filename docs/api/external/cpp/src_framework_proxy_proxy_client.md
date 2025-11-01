---
title: "src/framework/proxy/proxy_client.h"
source_file: "src/framework/proxy/proxy_client.h"
generated_at: "2025-11-01T08:19:49.462Z"
doc_type: "cpp_api"
---

# src/framework/proxy/proxy_client.h

(start)=
## `start`

**Signature:**
```cpp
void start();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(getdebuginfo)=
## `getDebugInfo`

**Signature:**
```cpp
std::string getDebugInfo();
```

**Returns:**
- `std::string`

---

(addsession)=
## `addSession`

**Signature:**
```cpp
void addSession(uint32_t id, int m_port);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `id` | - |
| `int` | `m_port` | - |

---

(removesession)=
## `removeSession`

**Signature:**
```cpp
void removeSession(uint32_t id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `id` | - |

---

(send)=
## `send`

**Signature:**
```cpp
void send(const ProxyPacketPtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ProxyPacketPtr&` | `packet` | - |

---

(check)=
## `check`

**Signature:**
```cpp
private: void check(const boost::system::error_code& ec = boost::system::error_code());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const boost::system::error_code&` | `ec` | `boost::system::error_code()` | - |

---

(connect)=
## `connect`

**Signature:**
```cpp
void connect();
```

---

(disconnect)=
## `disconnect`

**Signature:**
```cpp
void disconnect();
```

---

(ping)=
## `ping`

**Signature:**
```cpp
void ping();
```

---

(onping)=
## `onPing`

**Signature:**
```cpp
void onPing(uint32_t packetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `packetId` | - |

---

(readheader)=
## `readHeader`

**Signature:**
```cpp
void readHeader();
```

---

(onheader)=
## `onHeader`

**Signature:**
```cpp
void onHeader(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(onpacket)=
## `onPacket`

**Signature:**
```cpp
void onPacket(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(onsent)=
## `onSent`

**Signature:**
```cpp
void onSent(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(start-1)=
## `start`

**Signature:**
```cpp
void start(int maxConnections = 3);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `maxConnections` | `3` | - |

---

(terminate-1)=
## `terminate`

**Signature:**
```cpp
void terminate(boost::system::error_code ec = boost::asio::error::eof);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `boost::system::error_code` | `ec` | `boost::asio::error::eof` | - |

---

(onpacket-1)=
## `onPacket`

**Signature:**
```cpp
void onPacket(const ProxyPacketPtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ProxyPacketPtr&` | `packet` | - |

---

(onproxypacket)=
## `onProxyPacket`

**Signature:**
```cpp
void onProxyPacket(uint32_t packetId, uint32_t lastRecivedPacketId, const ProxyPacketPtr& packet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `packetId` | - |
| `uint32_t` | `lastRecivedPacketId` | - |
| `const ProxyPacketPtr&` | `packet` | - |

---

(check-1)=
## `check`

**Signature:**
```cpp
private: void check(const boost::system::error_code& ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |

---

(selectproxies)=
## `selectProxies`

**Signature:**
```cpp
void selectProxies();
```

---

(readtibia12header)=
## `readTibia12Header`

**Signature:**
```cpp
void readTibia12Header();
```

---

(readheader-1)=
## `readHeader`

**Signature:**
```cpp
void readHeader();
```

---

(onheader-1)=
## `onHeader`

**Signature:**
```cpp
void onHeader(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(onbody)=
## `onBody`

**Signature:**
```cpp
void onBody(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(onsent-1)=
## `onSent`

**Signature:**
```cpp
void onSent(const boost::system::error_code& ec, std::size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `std::size_t` | `bytes_transferred` | - |

---

(getping)=
## `getPing`

**Signature:**
```cpp
uint32_t getPing();
```

**Returns:**
- `uint32_t`

---

(getrealping)=
## `getRealPing`

**Signature:**
```cpp
uint32_t getRealPing();
```

**Returns:**
- `uint32_t`

---

(getpriority)=
## `getPriority`

**Signature:**
```cpp
uint32_t getPriority();
```

**Returns:**
- `uint32_t`

---

(isconnected)=
## `isConnected`

**Signature:**
```cpp
bool isConnected();
```

**Returns:**
- `bool`

---

(gethost)=
## `getHost`

**Signature:**
```cpp
std::string getHost();
```

**Returns:**
- `std::string`

---

(getport)=
## `getPort`

**Signature:**
```cpp
uint16_t getPort();
```

**Returns:**
- `uint16_t`

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

(getid)=
## `getId`

**Signature:**
```cpp
uint32_t getId();
```

**Returns:**
- `uint32_t`

---
