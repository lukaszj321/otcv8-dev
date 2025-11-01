---
title: "src/framework/graphics/paintershaderprogram.h"
source_file: "src/framework/graphics/paintershaderprogram.h"
generated_at: "2025-11-01T08:45:15.304Z"
doc_type: "cpp_api"
---

# src/framework/graphics/paintershaderprogram.h

(setupuniforms)=
## `setupUniforms`

**Signature:**
```cpp
virtual void setupUniforms();
```

---

(paintershaderprogram)=
## `PainterShaderProgram`

**Signature:**
```cpp
public: PainterShaderProgram(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(link)=
## `link`

**Signature:**
```cpp
bool link();
```

**Returns:**
- `bool`

---

(settransformmatrix)=
## `setTransformMatrix`

**Signature:**
```cpp
void setTransformMatrix(const Matrix3& transformMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `transformMatrix` | - |

---

(setprojectionmatrix)=
## `setProjectionMatrix`

**Signature:**
```cpp
void setProjectionMatrix(const Matrix3& projectionMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `projectionMatrix` | - |

---

(settexturematrix)=
## `setTextureMatrix`

**Signature:**
```cpp
void setTextureMatrix(const Matrix3& textureMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `textureMatrix` | - |

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setmatrixcolor)=
## `setMatrixColor`

**Signature:**
```cpp
void setMatrixColor(const Matrix4& colors);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix4&` | `colors` | - |

---

(setdepth)=
## `setDepth`

**Signature:**
```cpp
void setDepth(float depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `depth` | - |

---

(setresolution)=
## `setResolution`

**Signature:**
```cpp
void setResolution(const Size& resolution);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `resolution` | - |

---

(setoffset)=
## `setOffset`

**Signature:**
```cpp
void setOffset(const Point& offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `offset` | - |

---

(setcenter)=
## `setCenter`

**Signature:**
```cpp
void setCenter(const Point& center);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `center` | - |

---

(updatetime)=
## `updateTime`

**Signature:**
```cpp
void updateTime();
```

---

(addmultitexture)=
## `addMultiTexture`

**Signature:**
```cpp
void addMultiTexture(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(bindmultitextures)=
## `bindMultiTextures`

**Signature:**
```cpp
void bindMultiTextures();
```

---

(clearmultitextures)=
## `clearMultiTextures`

**Signature:**
```cpp
void clearMultiTextures();
```

---

(enablecolormatrix)=
## `enableColorMatrix`

**Signature:**
```cpp
void enableColorMatrix();
```

