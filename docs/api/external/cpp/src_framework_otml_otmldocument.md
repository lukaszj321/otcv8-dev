---
title: "src/framework/otml/otmldocument.h"
source_file: "src/framework/otml/otmldocument.h"
generated_at: "2025-11-01T08:29:23.713Z"
doc_type: "cpp_api"
---

# src/framework/otml/otmldocument.h

(create)=
## `create`

Create a new OTML document for filling it with nodes

**Signature:**
```cpp
static OTMLDocumentPtr create();
```

**Returns:**
- `OTMLDocumentPtr`

---

(parse)=
## `parse`

Parse OTML from a file

**Signature:**
```cpp
static OTMLDocumentPtr parse(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `OTMLDocumentPtr`

---

(parsestring)=
## `parseString`

Parse OTML from a string

**Signature:**
```cpp
static OTMLDocumentPtr parseString(const std::string& data, const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `data` | - |
| `const std::string&` | `source` | - |

**Returns:**
- `OTMLDocumentPtr`

---

(parse-1)=
## `parse`

Parse OTML from input stream
@param source is the file name that will be used to show errors messages

**Signature:**
```cpp
static OTMLDocumentPtr parse(std::istream& in, const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `const std::string&` | `source` | - |

**Returns:**
- `OTMLDocumentPtr`

---

(emit)=
## `emit`

Emits this document and all it's children to a std::string

**Signature:**
```cpp
std::string emit();
```

**Returns:**
- `std::string`

---

(save)=
## `save`

Save this document to a file

**Signature:**
```cpp
bool save(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(otmldocument)=
## `OTMLDocument`

**Signature:**
```cpp
private: OTMLDocument();
```

---
