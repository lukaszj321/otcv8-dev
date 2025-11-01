---
title: "src/framework/graphics/shaderprogram.h"
source_file: "src/framework/graphics/shaderprogram.h"
generated_at: "2025-11-01T05:32:59.285Z"
doc_type: "cpp_api"
---

# src/framework/graphics/shaderprogram.h

(shaderprogram)=
## `ShaderProgram`

**Signature:**
```cpp
public: ShaderProgram(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(create)=
## `create`

**Signature:**
```cpp
static PainterShaderProgramPtr create(const std::string& name, const std::string& vertexShader, const std::string& fragmentShader, bool colorMatrix = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `name` |  | - |
| `const std::string&` | `vertexShader` |  | - |
| `const std::string&` | `fragmentShader` |  | - |
| `bool` | `colorMatrix` | `false` | - |

**Returns:**
- `PainterShaderProgramPtr`

---

(addshader)=
## `addShader`

**Signature:**
```cpp
bool addShader(const ShaderPtr& shader);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ShaderPtr&` | `shader` | - |

**Returns:**
- `bool`

---

(addshaderfromsourcecode)=
## `addShaderFromSourceCode`

**Signature:**
```cpp
bool addShaderFromSourceCode(Shader::ShaderType shaderType, const std::string& sourceCode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Shader::ShaderType` | `shaderType` | - |
| `const std::string&` | `sourceCode` | - |

**Returns:**
- `bool`

---

(addshaderfromsourcefile)=
## `addShaderFromSourceFile`

**Signature:**
```cpp
bool addShaderFromSourceFile(Shader::ShaderType shaderType, const std::string& sourceFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Shader::ShaderType` | `shaderType` | - |
| `const std::string&` | `sourceFile` | - |

**Returns:**
- `bool`

---

(removeshader)=
## `removeShader`

**Signature:**
```cpp
void removeShader(const ShaderPtr& shader);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ShaderPtr&` | `shader` | - |

---

(removeallshaders)=
## `removeAllShaders`

**Signature:**
```cpp
void removeAllShaders();
```

---

(link)=
## `link`

**Signature:**
```cpp
virtual bool link();
```

**Returns:**
- `bool`

---

(bind)=
## `bind`

**Signature:**
```cpp
bool bind();
```

**Returns:**
- `bool`

---

(release)=
## `release`

**Signature:**
```cpp
static void release();
```

---

(log)=
## `log`

**Signature:**
```cpp
std::string log();
```

**Returns:**
- `std::string`

---

(getattributelocation)=
## `getAttributeLocation`

**Signature:**
```cpp
int getAttributeLocation(const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |

**Returns:**
- `int`

---

(bindattributelocation)=
## `bindAttributeLocation`

**Signature:**
```cpp
void bindAttributeLocation(int location, const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const char*` | `name` | - |

---

(binduniformlocation)=
## `bindUniformLocation`

**Signature:**
```cpp
void bindUniformLocation(int location, const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const char*` | `name` | - |

---

(disableattributearray)=
## `disableAttributeArray`

**Signature:**
```cpp
static void disableAttributeArray(int location);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |

---

(enableattributearray)=
## `enableAttributeArray`

**Signature:**
```cpp
static void enableAttributeArray(int location);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |

---

(disableattributearray-1)=
## `disableAttributeArray`

**Signature:**
```cpp
void disableAttributeArray(const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |

---

(enableattributearray-1)=
## `enableAttributeArray`

**Signature:**
```cpp
void enableAttributeArray(const char* name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |

---

(setattributearray)=
## `setAttributeArray`

**Signature:**
```cpp
void setAttributeArray(int location, const float* values, int size, int stride = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `location` |  | - |
| `const float*` | `values` |  | - |
| `int` | `size` |  | - |
| `int` | `stride` | `0` | - |

---

(setattributevalue)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(int location, float value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `value` | - |

---

(setattributevalue-1)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(int location, float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `x` | - |
| `float` | `y` | - |

---

(setattributevalue-2)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(int location, float x, float y, float z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |

---

(setattributearray-1)=
## `setAttributeArray`

**Signature:**
```cpp
void setAttributeArray(const char* name, const float* values, int size, int stride = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const char*` | `name` |  | - |
| `const float*` | `values` |  | - |
| `int` | `size` |  | - |
| `int` | `stride` | `0` | - |

---

(setattributevalue-3)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(const char* name, float value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `value` | - |

---

(setattributevalue-4)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(const char* name, float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `x` | - |
| `float` | `y` | - |

---

(setattributevalue-5)=
## `setAttributeValue`

**Signature:**
```cpp
void setAttributeValue(const char* name, float x, float y, float z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |

---

(setuniformvalue)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const Color&` | `color` | - |

---

(setuniformvalue-1)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, int value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `int` | `value` | - |

---

(setuniformvalue-2)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, float value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `value` | - |

---

(setuniformvalue-3)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `x` | - |
| `float` | `y` | - |

---

(setuniformvalue-4)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, float x, float y, float z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |

---

(setuniformvalue-5)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, float x, float y, float z, float w);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |
| `float` | `w` | - |

---

(setuniformvalue-6)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, const Matrix2& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const Matrix2&` | `mat` | - |

---

(setuniformvalue-7)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, const Matrix3& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const Matrix3&` | `mat` | - |

---

(setuniformvalue-8)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, const Matrix4& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `const Matrix4&` | `mat` | - |

---

(setuniformvalue-9)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(int location, int count, const int* value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `int` | `count` | - |
| `const int*` | `value` | - |

---

(setuniformvalue-10)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `const Color&` | `color` | - |

---

(setuniformvalue-11)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, int value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `int` | `value` | - |

---

(setuniformvalue-12)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, float value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `value` | - |

---

(setuniformvalue-13)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `x` | - |
| `float` | `y` | - |

---

(setuniformvalue-14)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, float x, float y, float z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |

---

(setuniformvalue-15)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, float x, float y, float z, float w);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `z` | - |
| `float` | `w` | - |

---

(setuniformvalue-16)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, const Matrix2& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `const Matrix2&` | `mat` | - |

---

(setuniformvalue-17)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, const Matrix3& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `const Matrix3&` | `mat` | - |

---

(setuniformvalue-18)=
## `setUniformValue`

**Signature:**
```cpp
void setUniformValue(const char* name, const Matrix4& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char*` | `name` | - |
| `const Matrix4&` | `mat` | - |

---

(islinked)=
## `isLinked`

**Signature:**
```cpp
bool isLinked();
```

**Returns:**
- `bool`

---

(getprogramid)=
## `getProgramId`

**Signature:**
```cpp
uint getProgramId();
```

**Returns:**
- `uint`

---

(getshaders)=
## `getShaders`

**Signature:**
```cpp
ShaderList getShaders();
```

**Returns:**
- `ShaderList`

---

(getname)=
## `getName`

**Signature:**
```cpp
std::string getName();
```

**Returns:**
- `std::string`

---
