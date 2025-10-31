---
title: "src/framework/http/session.h"
source_file: "src/framework/http/session.h"
generated_at: "2025-10-31T23:33:30.345Z"
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

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `error` | - |
| `const std::string& details = ""` | - | - |

---

(httpsession)=
## `HttpSession`

**Signature:**
```cpp
public: HttpSession(boost::asio::io_service& service, const std::string& url, const std::string& agent, int timeout, bool isJson, HttpResult_ptr result, HttpResult_cb callback) : m_service(service), m_url(url), m_agent(agent), m_socket(service), m_resolver(service), m_callback(callback), m_result(result), m_timer(service), m_timeout(timeout), m_isJson(isJson);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `boost::asio::io_service&` | `service` | - |
| `const std::string&` | `url` | - |
| `const std::string&` | `agent` | - |
| `int` | `timeout` | - |
| `bool` | `isJson` | - |
| `HttpResult_ptr` | `result` | - |
| `HttpResult_cb callback) : m_service(service)` | - | - |
| `m_url(url)` | - | - |
| `m_agent(agent)` | - | - |
| `m_socket(service)` | - | - |
| `m_resolver(service)` | - | - |
| `m_callback(callback)` | - | - |
| `m_result(result)` | - | - |
| `m_timer(service)` | - | - |
| `m_timeout(timeout)` | - | - |
| `m_isJson(` | `isJson` | - |

**Returns:**
- `public:`

---

(cancel)=
## `cancel`

**Signature:**
```cpp
void cancel();
```

---
