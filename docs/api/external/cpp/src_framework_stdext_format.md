---
title: "src/framework/stdext/format.h"
source_file: "src/framework/stdext/format.h"
generated_at: "2025-10-31T23:33:30.360Z"
doc_type: "cpp_api"
---

# src/framework/stdext/format.h

(_snprintf)=
## `_snprintf`

**Signature:**
```cpp
return _snprintf(s, maxlen, format, args...);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `s` | - |
| `` | `maxlen` | - |
| `` | `format` | - |
| `args...` | - | - |

**Returns:**
- `return`

---

(snprintf)=
## `snprintf`

**Signature:**
```cpp
return snprintf(s, maxlen, format, args...);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `s` | - |
| `` | `maxlen` | - |
| `` | `format` | - |
| `args...` | - | - |

**Returns:**
- `return`

---

(expand_snprintfstdtuple_sizedecltype)=
## `expand_snprintf<std::tuple_size<decltype`

**Signature:**
```cpp
return expand_snprintf<std::tuple_size<decltype(tuple)>::value>::call(s, maxlen, format, tuple);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `tuple)&gt;::value&gt;::call(` | `s` | - |
| `` | `maxlen` | - |
| `` | `format` | - |
| `` | `tuple` | - |

**Returns:**
- `return`

---

(strlen)=
## `strlen`

**Signature:**
```cpp
return strlen(s);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `s` | - |

**Returns:**
- `return`

---

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

(print_ostream)=
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
| `char *` | `s` | - |
| `size_t` | `maxlen` | - |
| `const char *` | `format` | - |
| `const Tuple&` | `tuple` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `static int`

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
| `char *` | `s` | - |
| `size_t` | `maxlen` | - |
| `const char *` | `format` | - |
| `const Tuple&` | `tuple` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `static int`

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
| `char *` | `s` | - |
| `size_t` | `maxlen` | - |
| `const char *` | `format` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `int`

---

(snprintf)=
## `snprintf`

**Signature:**
```cpp
inline int snprintf(char *s, size_t maxlen, const char *format);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char *` | `s` | - |
| `size_t` | `maxlen` | - |
| `const char *` | `format` | - |

**Returns:**
- `inline int`

---

(format)=
## `format`

**Signature:**
```cpp
inline std::string format();
```

**Returns:**
- `inline std::string`

---

(format)=
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
- `inline std::string`

---

(format)=
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
