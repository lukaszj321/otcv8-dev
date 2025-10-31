---
title: "src/framework/stdext/cast.h"
source_file: "src/framework/stdext/cast.h"
generated_at: "2025-10-31T23:33:30.358Z"
doc_type: "cpp_api"
---

# src/framework/stdext/cast.h

(cast)=
## `cast`

**Signature:**
```cpp
bool cast(const T& in, R& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `in` | - |
| `R&` | `out` | - |

**Returns:**
- `bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
bool cast(const T& in, std::string& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `in` | - |
| `std::string&` | `out` | - |

**Returns:**
- `bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, std::string& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `std::string&` | `out` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, bool& b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `bool&` | `b` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, char& c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `char&` | `c` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, long& l);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `long&` | `l` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, int& i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `int&` | `i` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, double& d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `double&` | `d` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const std::string& in, float& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `in` | - |
| `float&` | `f` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<> inline bool cast(const bool& in, std::string& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const bool&` | `in` | - |
| `std::string&` | `out` | - |

**Returns:**
- `template&lt;&gt; inline bool`

---

(update_what)=
## `update_what`

**Signature:**
```cpp
void update_what();
```

---

(what)=
## `what`

**Signature:**
```cpp
virtual const char* what() const throw();
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) const throw(` | - | - |

**Returns:**
- `virtual const char*`

---
