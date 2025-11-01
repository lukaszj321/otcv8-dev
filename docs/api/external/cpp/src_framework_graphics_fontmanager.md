---
title: "src/framework/graphics/fontmanager.h"
source_file: "src/framework/graphics/fontmanager.h"
generated_at: "2025-11-01T08:45:15.301Z"
doc_type: "cpp_api"
---

# src/framework/graphics/fontmanager.h

(fontmanager)=
## `FontManager`

**Signature:**
```cpp
public: FontManager();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(clearfonts)=
## `clearFonts`

**Signature:**
```cpp
void clearFonts();
```

---

(importfont)=
## `importFont`

**Signature:**
```cpp
void importFont(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

---

(fontexists)=
## `fontExists`

**Signature:**
```cpp
bool fontExists(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

**Returns:**
- `bool`

---

(getfont)=
## `getFont`

**Signature:**
```cpp
BitmapFontPtr getFont(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

**Returns:**
- `BitmapFontPtr`

---

(getdefaultfont)=
## `getDefaultFont`

**Signature:**
```cpp
BitmapFontPtr getDefaultFont();
```

**Returns:**
- `BitmapFontPtr`

---

(setdefaultfont)=
## `setDefaultFont`

**Signature:**
```cpp
void setDefaultFont(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

---
