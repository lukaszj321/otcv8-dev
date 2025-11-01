---
title: "src/framework/otml/otmlparser.h"
source_file: "src/framework/otml/otmlparser.h"
generated_at: "2025-11-01T06:09:06.197Z"
doc_type: "cpp_api"
---

# src/framework/otml/otmlparser.h

(otmlparser)=
## `OTMLParser`

**Signature:**
```cpp
public: OTMLParser(OTMLDocumentPtr doc, std::istream& in);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `OTMLDocumentPtr` | `doc` | - |
| `std::istream&` | `in` | - |

---

(parse)=
## `parse`

Parse the entire document

**Signature:**
```cpp
void parse();
```

---

(getnextline)=
## `getNextLine`

Retrieve next line from the input stream

**Signature:**
```cpp
std::string getNextLine();
```

**Returns:**
- `std::string`

---

(getlinedepth)=
## `getLineDepth`

Counts depth of a line (every 2 spaces increments one depth)

**Signature:**
```cpp
int getLineDepth(const std::string& line, bool multilining = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `line` |  | - |
| `bool` | `multilining` | `false` | - |

**Returns:**
- `int`

---

(parseline)=
## `parseLine`

Parse each line of the input stream

**Signature:**
```cpp
void parseLine(std::string line);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `line` | - |

---

(parsenode)=
## `parseNode`

Parse nodes tag and value

**Signature:**
```cpp
void parseNode(const std::string& data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `data` | - |

---
