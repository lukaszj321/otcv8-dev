---
title: "src/framework/http/http.h"
source_file: "src/framework/http/http.h"
generated_at: "2025-11-01T08:46:04.920Z"
doc_type: "cpp_api"
---

# src/framework/http/http.h

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

(get)=
## `get`

**Signature:**
```cpp
int get(const std::string& url, int timeout = 5);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `url` |  | - |
| `int` | `timeout` | `5` | - |

**Returns:**
- `int`

---

(post)=
## `post`

**Signature:**
```cpp
int post(const std::string& url, const std::string& data, int timeout = 5, bool isJson = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `url` |  | - |
| `const std::string&` | `data` |  | - |
| `int` | `timeout` | `5` | - |
| `bool` | `isJson` | `false` | - |

**Returns:**
- `int`

---

(download)=
## `download`

**Signature:**
```cpp
int download(const std::string& url, std::string path, int timeout = 5);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `url` |  | - |
| `std::string` | `path` |  | - |
| `int` | `timeout` | `5` | - |

**Returns:**
- `int`

---

(ws)=
## `ws`

**Signature:**
```cpp
int ws(const std::string& url, int timeout = 5);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `url` |  | - |
| `int` | `timeout` | `5` | - |

**Returns:**
- `int`

---

(wssend)=
## `wsSend`

**Signature:**
```cpp
bool wsSend(int operationId, std::string message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `operationId` | - |
| `std::string` | `message` | - |

**Returns:**
- `bool`

---

(wsclose)=
## `wsClose`

**Signature:**
```cpp
bool wsClose(int operationId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `operationId` | - |

**Returns:**
- `bool`

---

(cancel)=
## `cancel`

**Signature:**
```cpp
bool cancel(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `bool`

---

(cleardownloads)=
## `clearDownloads`

**Signature:**
```cpp
void clearDownloads();
```

---

(getfile)=
## `getFile`

**Signature:**
```cpp
HttpResult_ptr getFile(std::string path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `path` | - |

**Returns:**
- `HttpResult_ptr`

---

(setuseragent)=
## `setUserAgent`

**Signature:**
```cpp
void setUserAgent(const std::string& userAgent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `userAgent` | - |

---
