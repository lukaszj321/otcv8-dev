---
title: "src/framework/graphics/framebuffer.h"
source_file: "src/framework/graphics/framebuffer.h"
generated_at: "2025-10-31T23:33:30.340Z"
doc_type: "cpp_api"
---

# src/framework/graphics/framebuffer.h

(framebuffer)=
## `FrameBuffer`

**Signature:**
```cpp
public: FrameBuffer(bool withDepth = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool withDepth =` | `false` | - |

**Returns:**
- `public:`

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

(bind)=
## `bind`

**Signature:**
```cpp
void bind(const FrameBufferPtr& depthFramebuffer = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FrameBufferPtr& depthFramebuffer =` | `nullptr` | - |

---

(release)=
## `release`

**Signature:**
```cpp
void release();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& dest, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |

---

(setsmooth)=
## `setSmooth`

**Signature:**
```cpp
void setSmooth(bool enabled);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enabled` | - |

---

(getsize)=
## `getSize`

**Signature:**
```cpp
Size getSize();
```

**Returns:**
- `Size`

---

(readpixels)=
## `readPixels`

**Signature:**
```cpp
std::vector<uint32_t> readPixels();
```

**Returns:**
- `std::vector&lt;uint32_t&gt;`

---

(doscreenshot)=
## `doScreenshot`

**Signature:**
```cpp
void doScreenshot(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(internalcreate)=
## `internalCreate`

**Signature:**
```cpp
private: void internalCreate();
```

**Returns:**
- `private: void`

---

(internalbind)=
## `internalBind`

**Signature:**
```cpp
void internalBind();
```

---

(internalrelease)=
## `internalRelease`

**Signature:**
```cpp
void internalRelease();
```

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

(issmooth)=
## `isSmooth`

**Signature:**
```cpp
bool isSmooth();
```

**Returns:**
- `bool`

---

(getdepthrenderbuffer)=
## `getDepthRenderBuffer`

**Signature:**
```cpp
uint getDepthRenderBuffer();
```

**Returns:**
- `uint`

---

(hasdepth)=
## `hasDepth`

**Signature:**
```cpp
bool hasDepth();
```

**Returns:**
- `bool`

---
