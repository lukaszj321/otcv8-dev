---
title: "src/client/healthbars.h"
source_file: "src/client/healthbars.h"
generated_at: "2025-11-01T08:29:23.677Z"
doc_type: "cpp_api"
---

# src/client/healthbars.h

(settexture)=
## `setTexture`

**Signature:**
```cpp
void setTexture(const std::string& path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `path` | - |

---

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

(addhealthbackground)=
## `addHealthBackground`

**Signature:**
```cpp
void addHealthBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `path` | - |
| `int` | `offsetX` | - |
| `int` | `offsetY` | - |
| `int` | `barOffsetX` | - |
| `int` | `barOffsetY` | - |
| `int` | `height` | - |

---

(addmanabackground)=
## `addManaBackground`

**Signature:**
```cpp
void addManaBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `path` | - |
| `int` | `offsetX` | - |
| `int` | `offsetY` | - |
| `int` | `barOffsetX` | - |
| `int` | `barOffsetY` | - |
| `int` | `height` | - |

---

(gethealthbarpath)=
## `getHealthBarPath`

**Signature:**
```cpp
std::string getHealthBarPath(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `std::string`

---

(getmanabarpath)=
## `getManaBarPath`

**Signature:**
```cpp
std::string getManaBarPath(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `std::string`

---

(gethealthbaroffset)=
## `getHealthBarOffset`

**Signature:**
```cpp
Point getHealthBarOffset(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `Point`

---

(getmanabaroffset)=
## `getManaBarOffset`

**Signature:**
```cpp
Point getManaBarOffset(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `Point`

---

(gethealthbaroffsetbar)=
## `getHealthBarOffsetBar`

**Signature:**
```cpp
Point getHealthBarOffsetBar(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `Point`

---

(getmanabaroffsetbar)=
## `getManaBarOffsetBar`

**Signature:**
```cpp
Point getManaBarOffsetBar(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `Point`

---

(gethealthbarheight)=
## `getHealthBarHeight`

**Signature:**
```cpp
int getHealthBarHeight(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `int`

---

(getmanabarheight)=
## `getManaBarHeight`

**Signature:**
```cpp
int getManaBarHeight(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `int`

---

(setpath)=
## `setPath`

**Signature:**
```cpp
public: void setPath(const std::string& path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `path` | - |

---

(getpath)=
## `getPath`

**Signature:**
```cpp
std::string getPath();
```

**Returns:**
- `std::string`

---

(gettexture)=
## `getTexture`

**Signature:**
```cpp
TexturePtr getTexture();
```

**Returns:**
- `TexturePtr`

---

(setoffset)=
## `setOffset`

**Signature:**
```cpp
void setOffset(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(getoffset)=
## `getOffset`

**Signature:**
```cpp
Point getOffset();
```

**Returns:**
- `Point`

---

(setbaroffset)=
## `setBarOffset`

**Signature:**
```cpp
void setBarOffset(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(getbaroffset)=
## `getBarOffset`

**Signature:**
```cpp
Point getBarOffset();
```

**Returns:**
- `Point`

---

(setheight)=
## `setHeight`

**Signature:**
```cpp
void setHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(getheight)=
## `getHeight`

**Signature:**
```cpp
int getHeight();
```

**Returns:**
- `int`

---

(gethealthbar)=
## `getHealthBar`

**Signature:**
```cpp
HealthBarPtr getHealthBar(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `HealthBarPtr`

---

(getmanabar)=
## `getManaBar`

**Signature:**
```cpp
HealthBarPtr getManaBar(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `HealthBarPtr`

---
