---
title: "src/framework/stdext/string.h"
source_file: "src/framework/stdext/string.h"
generated_at: "2025-11-01T00:11:49.064Z"
doc_type: "cpp_api"
---

# src/framework/stdext/string.h

(resolve_path)=
## `resolve_path`

Resolve a file path by combining sourcePath with filePath

**Signature:**
```cpp
std::string resolve_path(const std::string& filePath, std::string sourcePath);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filePath` | - |
| `std::string` | `sourcePath` | - |

**Returns:**
- `std::string`

---

(date_time_string)=
## `date_time_string`

Get current date and time in a std::string

**Signature:**
```cpp
std::string date_time_string();
```

**Returns:**
- `std::string`

---

(timestamp_to_date)=
## `timestamp_to_date`

**Signature:**
```cpp
std::string timestamp_to_date(time_t tnow);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `time_t` | `tnow` | - |

**Returns:**
- `std::string`

---

(dec_to_hex)=
## `dec_to_hex`

**Signature:**
```cpp
std::string dec_to_hex(uint32_t num);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `num` | - |

**Returns:**
- `std::string`

---

(dec_to_hex-1)=
## `dec_to_hex`

**Signature:**
```cpp
std::string dec_to_hex(uint64_t num);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64_t` | `num` | - |

**Returns:**
- `std::string`

---

(hex_to_dec)=
## `hex_to_dec`

**Signature:**
```cpp
uint64_t hex_to_dec(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

**Returns:**
- `uint64_t`

---

(tolower)=
## `tolower`

**Signature:**
```cpp
void tolower(std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `str` | - |

---

(toupper)=
## `toupper`

**Signature:**
```cpp
void toupper(std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `str` | - |

---

(trim)=
## `trim`

**Signature:**
```cpp
void trim(std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `str` | - |

---

(ucwords)=
## `ucwords`

**Signature:**
```cpp
void ucwords(std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `str` | - |

---

(upchar)=
## `upchar`

**Signature:**
```cpp
char upchar(char c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `c` | - |

**Returns:**
- `char`

---

(lochar)=
## `lochar`

**Signature:**
```cpp
char lochar(char c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `char` | `c` | - |

**Returns:**
- `char`

---

(ends_with)=
## `ends_with`

**Signature:**
```cpp
bool ends_with(const std::string& str, const std::string& test);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |
| `const std::string&` | `test` | - |

**Returns:**
- `bool`

---

(starts_with)=
## `starts_with`

**Signature:**
```cpp
bool starts_with(const std::string& str, const std::string& test);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |
| `const std::string&` | `test` | - |

**Returns:**
- `bool`

---

(replace_all)=
## `replace_all`

**Signature:**
```cpp
void replace_all(std::string& str, const std::string& search, const std::string& replacement);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string&` | `str` | - |
| `const std::string&` | `search` | - |
| `const std::string&` | `replacement` | - |

---

(is_valid_utf8)=
## `is_valid_utf8`

**Signature:**
```cpp
bool is_valid_utf8(const std::string& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `src` | - |

**Returns:**
- `bool`

---

(utf8_to_latin1)=
## `utf8_to_latin1`

**Signature:**
```cpp
std::string utf8_to_latin1(const std::string& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `src` | - |

**Returns:**
- `std::string`

---

(latin1_to_utf8)=
## `latin1_to_utf8`

**Signature:**
```cpp
std::string latin1_to_utf8(const std::string& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `src` | - |

**Returns:**
- `std::string`

---

(utf8_to_utf16)=
## `utf8_to_utf16`

**Signature:**
```cpp
std::wstring utf8_to_utf16(const std::string& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `src` | - |

**Returns:**
- `std::wstring`

---

(utf16_to_utf8)=
## `utf16_to_utf8`

**Signature:**
```cpp
std::string utf16_to_utf8(const std::wstring& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::wstring&` | `src` | - |

**Returns:**
- `std::string`

---

(utf16_to_latin1)=
## `utf16_to_latin1`

**Signature:**
```cpp
std::string utf16_to_latin1(const std::wstring& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::wstring&` | `src` | - |

**Returns:**
- `std::string`

---

(latin1_to_utf16)=
## `latin1_to_utf16`

**Signature:**
```cpp
std::wstring latin1_to_utf16(const std::string& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `src` | - |

**Returns:**
- `std::wstring`

---

(split)=
## `split`

**Signature:**
```cpp
std::vector<std::string> split(const std::string& str, const std::string& separators = " ");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `str` |  | - |
| `const std::string&` | `separators` | `" "` | - |

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(results)=
## `results`

**Signature:**
```cpp
std::vector<T> results(splitted.size());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `splitted.size()` | - | - |

**Returns:**
- `std::vector&lt;T&gt;`

---

(to_string)=
## `to_string`

**Signature:**
```cpp
std::string to_string(const T& t);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `t` | - |

**Returns:**
- `std::string`

---

(from_string)=
## `from_string`

**Signature:**
```cpp
template<typename T> T from_string(const std::string& str, T def = T());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `str` |  | - |
| `T` | `def` | `T()` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---

(split-1)=
## `split`

**Signature:**
```cpp
std::vector<T> split(const std::string& str, const std::string& separators = " ");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `str` |  | - |
| `const std::string&` | `separators` | `" "` | - |

**Returns:**
- `std::vector&lt;T&gt;`

---
