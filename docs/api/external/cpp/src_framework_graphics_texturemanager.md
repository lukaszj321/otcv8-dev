---
title: "src/framework/graphics/texturemanager.h"
source_file: "src/framework/graphics/texturemanager.h"
generated_at: "2025-11-01T08:46:04.920Z"
doc_type: "cpp_api"
---

# src/framework/graphics/texturemanager.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(clearcache)=
## `clearCache`

**Signature:**
```cpp
void clearCache();
```

---

(reload)=
## `reload`

**Signature:**
```cpp
void reload();
```

---

(gettexture)=
## `getTexture`

**Signature:**
```cpp
TexturePtr getTexture(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `TexturePtr`

---

(loadtexture)=
## `loadTexture`

**Signature:**
```cpp
TexturePtr loadTexture(std::stringstream& file, const std::string& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::stringstream&` | `file` | - |
| `const std::string&` | `source` | - |

**Returns:**
- `TexturePtr`

---

(preload)=
## `preload`

**Signature:**
```cpp
void preload(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---
