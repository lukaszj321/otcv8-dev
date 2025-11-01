---
title: "src/framework/xml/tinystr.h"
source_file: "src/framework/xml/tinystr.h"
generated_at: "2025-11-01T08:45:15.332Z"
doc_type: "cpp_api"
---

# src/framework/xml/tinystr.h

(reserve)=
## `reserve`

**Signature:**
```cpp
void reserve(size_type cap);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_type` | `cap` | - |

---

(assign)=
## `assign`

**Signature:**
```cpp
TiXmlString& assign(const char* str, size_type len);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `str` | - |
| `size_type` | `len` | - |

**Returns:**
- `TiXmlString&`

---

(append)=
## `append`

**Signature:**
```cpp
TiXmlString& append(const char* str, size_type len);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `str` | - |
| `size_type` | `len` | - |

**Returns:**
- `TiXmlString&`

---

(c_str)=
## `c_str`

**Signature:**
```cpp
const char * c_str();
```

**Returns:**
- `const char *`

---

(data)=
## `data`

**Signature:**
```cpp
const char * data();
```

**Returns:**
- `const char *`

---

(length)=
## `length`

**Signature:**
```cpp
size_type length();
```

**Returns:**
- `size_type`

---

(size)=
## `size`

**Signature:**
```cpp
size_type size();
```

**Returns:**
- `size_type`

---

(empty)=
## `empty`

**Signature:**
```cpp
bool empty();
```

**Returns:**
- `bool`

---

(capacity)=
## `capacity`

**Signature:**
```cpp
size_type capacity();
```

**Returns:**
- `size_type`

---

(at)=
## `at`

**Signature:**
```cpp
const char& at(size_type index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_type` | `index` | - |

**Returns:**
- `const char&`

---

(find)=
## `find`

**Signature:**
```cpp
size_type find(char lookup);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `lookup` | - |

**Returns:**
- `size_type`

---

(find-1)=
## `find`

**Signature:**
```cpp
size_type find(char tofind, size_type offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `tofind` | - |
| `size_type` | `offset` | - |

**Returns:**
- `size_type`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(swap)=
## `swap`

**Signature:**
```cpp
void swap(TiXmlString& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlString&` | `other` | - |

---

(init)=
## `init`

**Signature:**
```cpp
private: void init(size_type sz);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_type` | `sz` | - |

---

(set_size)=
## `set_size`

**Signature:**
```cpp
void set_size(size_type sz);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_type` | `sz` | - |

---

(start)=
## `start`

**Signature:**
```cpp
char* start();
```

**Returns:**
- `char*`

---

(finish)=
## `finish`

**Signature:**
```cpp
char* finish();
```

**Returns:**
- `char*`

---

(init-1)=
## `init`

**Signature:**
```cpp
void init(size_type sz, size_type cap);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_type` | `sz` | - |
| `size_type` | `cap` | - |

---

(quit)=
## `quit`

**Signature:**
```cpp
void quit();
```

