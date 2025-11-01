---
title: "src/framework/graphics/shadermanager.h"
source_file: "src/framework/graphics/shadermanager.h"
generated_at: "2025-11-01T08:45:15.304Z"
doc_type: "cpp_api"
---

# src/framework/graphics/shadermanager.h

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

(createshader)=
## `createShader`

**Signature:**
```cpp
void createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `name` |  | - |
| `std::string` | `vertex` |  | - |
| `std::string` | `fragment` |  | - |
| `bool` | `colorMatrix` | `false` | - |

---

(addtexture)=
## `addTexture`

**Signature:**
```cpp
void addTexture(const std::string& name, const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `const std::string&` | `file` | - |

---

(getshader)=
## `getShader`

**Signature:**
```cpp
PainterShaderProgramPtr getShader(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

**Returns:**
- `PainterShaderProgramPtr`

---

(createoutfitshader)=
## `createOutfitShader`

**Signature:**
```cpp
void createOutfitShader(const std::string& name, std::string vertex, std::string fragment);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `std::string` | `vertex` | - |
| `std::string` | `fragment` | - |

