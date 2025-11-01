---
title: "src/framework/net/connection.h"
source_file: "src/framework/net/connection.h"
generated_at: "2025-11-01T08:45:15.311Z"
doc_type: "cpp_api"
---

# src/framework/net/connection.h

(connection)=
## `Connection`

**Signature:**
```cpp
public: Connection();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
static void poll();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
static void terminate();
```

---

(connect)=
## `connect`

**Signature:**
```cpp
void connect(const std::string& host, uint16 port, const std::function<void()>& connectCallback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `host` | - |
| `uint16` | `port` | - |
| `const std::function&lt;void()&gt;&` | `connectCallback` | - |

---

(close)=
## `close`

**Signature:**
```cpp
void close();
```

---

(write)=
## `write`

**Signature:**
```cpp
void write(uint8* buffer, size_t size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8*` | `buffer` | - |
| `size_t` | `size` | - |

---

(read)=
## `read`

**Signature:**
```cpp
void read(uint32 bytes, const RecvCallback& callback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `bytes` | - |
| `const RecvCallback&` | `callback` | - |

---

(read_until)=
## `read_until`

**Signature:**
```cpp
void read_until(const std::string& what, const RecvCallback& callback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |
| `const RecvCallback&` | `callback` | - |

---

(read_some)=
## `read_some`

**Signature:**
```cpp
void read_some(const RecvCallback& callback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const RecvCallback&` | `callback` | - |

---

(getip)=
## `getIp`

**Signature:**
```cpp
int getIp();
```

**Returns:**
- `int`

---

(internal_connect)=
## `internal_connect`

**Signature:**
```cpp
protected: void internal_connect(asio::ip::basic_resolver<asio::ip::tcp>::iterator endpointIterator);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `asio::ip::basic_resolver&lt;asio::ip::tcp&gt;::iterator` | `endpointIterator` | - |

---

(internal_write)=
## `internal_write`

**Signature:**
```cpp
void internal_write();
```

---

(onresolve)=
## `onResolve`

**Signature:**
```cpp
void onResolve(const boost::system::error_code& error, asio::ip::tcp::resolver::iterator endpointIterator);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |
| `asio::ip::tcp::resolver::iterator` | `endpointIterator` | - |

---

(onconnect)=
## `onConnect`

**Signature:**
```cpp
void onConnect(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(oncanwrite)=
## `onCanWrite`

**Signature:**
```cpp
void onCanWrite(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(onwrite)=
## `onWrite`

**Signature:**
```cpp
void onWrite(const boost::system::error_code& error, size_t writeSize, std::shared_ptr<asio::streambuf> outputStream);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |
| `size_t` | `writeSize` | - |
| `std::shared_ptr&lt;asio::streambuf&gt;` | `outputStream` | - |

---

(onrecv)=
## `onRecv`

**Signature:**
```cpp
void onRecv(const boost::system::error_code& error, size_t recvSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |
| `size_t` | `recvSize` | - |

---

(ontimeout)=
## `onTimeout`

**Signature:**
```cpp
void onTimeout(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(handleerror)=
## `handleError`

**Signature:**
```cpp
void handleError(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(seterrorcallback)=
## `setErrorCallback`

**Signature:**
```cpp
void setErrorCallback(const ErrorCallback& errorCallback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ErrorCallback&` | `errorCallback` | - |

---

(geterror)=
## `getError`

**Signature:**
```cpp
boost::system::error_code getError();
```

**Returns:**
- `boost::system::error_code`

---

(isconnecting)=
## `isConnecting`

**Signature:**
```cpp
bool isConnecting();
```

**Returns:**
- `bool`

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

(getelapsedtickssincelastread)=
## `getElapsedTicksSinceLastRead`

**Signature:**
```cpp
ticks_t getElapsedTicksSinceLastRead();
```

**Returns:**
- `ticks_t`

---

(asconnection)=
## `asConnection`

**Signature:**
```cpp
ConnectionPtr asConnection();
```

**Returns:**
- `ConnectionPtr`

---
