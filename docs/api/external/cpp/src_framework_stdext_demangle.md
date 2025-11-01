---
title: "src/framework/stdext/demangle.h"
source_file: "src/framework/stdext/demangle.h"
generated_at: "2025-11-01T08:19:49.465Z"
doc_type: "cpp_api"
---

# src/framework/stdext/demangle.h

(demangle_name)=
## `demangle_name`

Demangle names for GNU g++ compiler

**Signature:**
```cpp
const char* demangle_name(const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |

**Returns:**
- `const char*`

---

(demangle_class)=
## `demangle_class`

Returns the name of a class

**Signature:**
```cpp
std::string demangle_class();
```

**Returns:**
- `std::string`

---

(demangle_type)=
## `demangle_type`

Returns the name of a type

**Signature:**
```cpp
std::string demangle_type();
```

**Returns:**
- `std::string`

---
