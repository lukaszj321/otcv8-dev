---
title: "src/framework/graphics/graphics.h"
source_file: "src/framework/graphics/graphics.h"
generated_at: "2025-11-01T06:09:06.185Z"
doc_type: "cpp_api"
---

# src/framework/graphics/graphics.h

(graphics)=
## `Graphics`

**Signature:**
```cpp
public: Graphics();
```

---

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(resize)=
## `resize`

**Signature:**
```cpp
void resize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(checkdepthsupport)=
## `checkDepthSupport`

**Signature:**
```cpp
void checkDepthSupport();
```

---

(checkforerror)=
## `checkForError`

**Signature:**
```cpp
void checkForError(const std::string& function, const std::string& file, int line);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `function` | - |
| `const std::string&` | `file` | - |
| `int` | `line` | - |

---

(checkdepthsupport-1)=
## `checkDepthSupport`

**Signature:**
```cpp
void checkDepthSupport();
```

---

(getmaxtexturesize)=
## `getMaxTextureSize`

**Signature:**
```cpp
int getMaxTextureSize();
```

**Returns:**
- `int`

---

(getviewportsize)=
## `getViewportSize`

**Signature:**
```cpp
const Size& getViewportSize();
```

**Returns:**
- `const Size&`

---

(getvendor)=
## `getVendor`

**Signature:**
```cpp
std::string getVendor();
```

**Returns:**
- `std::string`

---

(getrenderer)=
## `getRenderer`

**Signature:**
```cpp
std::string getRenderer();
```

**Returns:**
- `std::string`

---

(getversion)=
## `getVersion`

**Signature:**
```cpp
std::string getVersion();
```

**Returns:**
- `std::string`

---

(getextensions)=
## `getExtensions`

**Signature:**
```cpp
std::string getExtensions();
```

**Returns:**
- `std::string`

---

(ok)=
## `ok`

**Signature:**
```cpp
bool ok();
```

**Returns:**
- `bool`

---
