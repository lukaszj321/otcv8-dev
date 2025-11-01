---
title: "src/framework/http/session.h"
source_file: "src/framework/http/session.h"
generated_at: "2025-11-01T08:46:04.920Z"
doc_type: "cpp_api"
---

# src/framework/http/session.h

(start)=
## `start`

**Signature:**
```cpp
void start();
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

(on_request_sent)=
## `on_request_sent`

**Signature:**
```cpp
void on_request_sent(const boost::system::error_code& ec);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `ec` | - |

---

(on_read_header)=
## `on_read_header`

**Signature:**
```cpp
void on_read_header(const boost::system::error_code & ec, size_t bytes_transferred);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code &` | `ec` | - |
| `size_t` | `bytes_transferred` | - |

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

(close)=
## `close`

**Signature:**
```cpp
void close();
```

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

---

(cancel)=
## `cancel`

**Signature:**
```cpp
void cancel();
```

---
