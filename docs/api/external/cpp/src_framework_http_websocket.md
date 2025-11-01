---
title: "src/framework/http/websocket.h"
source_file: "src/framework/http/websocket.h"
generated_at: "2025-11-01T08:45:15.307Z"
doc_type: "cpp_api"
---

# src/framework/http/websocket.h

(start)=
## `start`

**Signature:**
```cpp
void start();
```

---

(send)=
## `send`

**Signature:**
```cpp
void send(std::string data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `data` | - |

---

(close)=
## `close`

**Signature:**
```cpp
void close();
```

---

(on_resolve)=
## `on_resolve`

**Signature:**
```cpp
void on_resolve(const boost::system::error_code& ec, boost::asio::ip::tcp::resolver::iterator iterator);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `boost::asio::ip::tcp::resolver::iterator` | `iterator` | - |

---

(on_connect)=
## `on_connect`

**Signature:**
```cpp
void on_connect(const boost::system::error_code& ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |

---

(on_handshake)=
## `on_handshake`

**Signature:**
```cpp
void on_handshake(const boost::system::error_code& ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |

---

(on_send)=
## `on_send`

**Signature:**
```cpp
void on_send(const boost::system::error_code& ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |

---

(on_read)=
## `on_read`

**Signature:**
```cpp
void on_read(const boost::system::error_code& ec, size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |
| `size_t` | `bytes_transferred` | - |

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

(onerror)=
## `onError`

**Signature:**
```cpp
void onError(const std::string& error, const std::string& details = "");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `error` |  | - |
| `const std::string&` | `details` | `""` | - |

