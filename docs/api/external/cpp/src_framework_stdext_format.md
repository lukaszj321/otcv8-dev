---
title: "src/framework/stdext/format.h"
source_file: "src/framework/stdext/format.h"
generated_at: "2025-11-01T08:46:04.935Z"
doc_type: "cpp_api"
---

# src/framework/stdext/format.h

(buffer)=
## `buffer`

**Signature:**
```cpp
std::string buffer(n + 1, '\0');
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `n + 1` | - | - |
| `'\0'` | - | - |

**Returns:**
- `std::string`

---

(print_ostream)=
## `print_ostream`

**Signature:**
```cpp
void print_ostream(std::ostringstream& stream, const T& last);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostringstream&` | `stream` | - |
| `const T&` | `last` | - |

---

(print_ostream-1)=
## `print_ostream`

**Signature:**
```cpp
void print_ostream(std::ostringstream& stream, const T& first, const Args&... rest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostringstream&` | `stream` | - |
| `const T&` | `first` | - |
| `const Args&...` | `rest` | - |

---

(print)=
## `print`

**Signature:**
```cpp
void print(const T&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&...` | `args` | - |

---

(call)=
## `call`

**Signature:**
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char *s` | - | - |
| `size_t` | `maxlen` | - |
| `const char *format` | - | - |
| `const Tuple&` | `tuple` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(call-1)=
## `call`

**Signature:**
```cpp
static int call(char *s, size_t maxlen, const char *format, const Tuple& tuple, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char *s` | - | - |
| `size_t` | `maxlen` | - |
| `const char *format` | - | - |
| `const Tuple&` | `tuple` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(snprintf)=
## `snprintf`

**Signature:**
```cpp
int snprintf(char *s, size_t maxlen, const char *format, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char *s` | - | - |
| `size_t` | `maxlen` | - |
| `const char *format` | - | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(snprintf-1)=
## `snprintf`

**Signature:**
```cpp
inline int snprintf(char *s, size_t maxlen, const char *format);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char *s` | - | - |
| `size_t` | `maxlen` | - |
| `const char *format` | - | - |

**Returns:**
- `int`

---

(format)=
## `format`

**Signature:**
```cpp
inline std::string format();
```

**Returns:**
- `std::string`

---

(format-1)=
## `format`

**Signature:**
```cpp
inline std::string format(const std::string& format);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `format` | - |

**Returns:**
- `std::string`

---

(format-2)=
## `format`

**Signature:**
```cpp
std::string format(const std::string& format, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `format` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `std::string`

---
