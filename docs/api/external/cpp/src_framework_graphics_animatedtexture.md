---
title: "src/framework/graphics/animatedtexture.h"
source_file: "src/framework/graphics/animatedtexture.h"
generated_at: "2025-10-31T23:33:30.337Z"
doc_type: "cpp_api"
---

# src/framework/graphics/animatedtexture.h

(animatedtexture)=
## `AnimatedTexture`

**Signature:**
```cpp
public: AnimatedTexture(const Size& size, std::vector<ImagePtr> frames, std::vector<int> framesDelay, bool buildMipmaps = false, bool compress = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |
| `std::vector&lt;ImagePtr&gt;` | `frames` | - |
| `std::vector&lt;int&gt;` | `framesDelay` | - |
| `bool buildMipmaps =` | `false` | - |
| `bool compress =` | `false` | - |

**Returns:**
- `public:`

---

(update)=
## `update`

**Signature:**
```cpp
void update();
```

---

(buildhardwaremipmaps)=
## `buildHardwareMipmaps`

**Signature:**
```cpp
protected: virtual bool buildHardwareMipmaps();
```

**Returns:**
- `protected: virtual bool`

---

(setsmooth)=
## `setSmooth`

**Signature:**
```cpp
virtual void setSmooth(bool smooth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `smooth` | - |

**Returns:**
- `virtual void`

---

(setrepeat)=
## `setRepeat`

**Signature:**
```cpp
virtual void setRepeat(bool repeat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `repeat` | - |

**Returns:**
- `virtual void`

---

(replace)=
## `replace`

**Signature:**
```cpp
void replace(const ImagePtr& image);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `image` | - |

---

(isanimatedtexture)=
## `isAnimatedTexture`

**Signature:**
```cpp
virtual bool isAnimatedTexture();
```

**Returns:**
- `virtual bool`

---
