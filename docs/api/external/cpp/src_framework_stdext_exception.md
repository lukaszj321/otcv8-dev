---
title: "src/framework/stdext/exception.h"
source_file: "src/framework/stdext/exception.h"
generated_at: "2025-11-01T08:19:49.466Z"
doc_type: "cpp_api"
---

# src/framework/stdext/exception.h

(exception)=
## `exception`

**Signature:**
```cpp
public: exception();
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
- `const char*`

---

(throw_exception)=
## `throw_exception`

Throws a generic exception

**Signature:**
```cpp
inline void throw_exception(const std::string& what);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `what` | - |

---
