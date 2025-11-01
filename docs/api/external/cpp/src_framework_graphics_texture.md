---
title: "src/framework/graphics/texture.h"
source_file: "src/framework/graphics/texture.h"
generated_at: "2025-11-01T08:19:49.448Z"
doc_type: "cpp_api"
---

# src/framework/graphics/texture.h

(texture)=
## `Texture`

**Signature:**
```cpp
public: Texture(const Size& size, bool depthTexture = false, bool smooth = false, bool upsideDown = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Size&` | `size` |  | - |
| `bool` | `depthTexture` | `false` | - |
| `bool` | `smooth` | `false` | - |
| `bool` | `upsideDown` | `false` | - |

---

(replace)=
## `replace`

**Signature:**
```cpp
virtual void replace(const ImagePtr& image);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `image` | - |

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

(update)=
## `update`

**Signature:**
```cpp
virtual void update();
```

---

(setupsidedown)=
## `setUpsideDown`

**Signature:**
```cpp
virtual void setUpsideDown(bool upsideDown);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `upsideDown` | - |

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

---

(buildhardwaremipmaps)=
## `buildHardwareMipmaps`

**Signature:**
```cpp
virtual bool buildHardwareMipmaps();
```

**Returns:**
- `bool`

---

(uploadpixels)=
## `uploadPixels`

**Signature:**
```cpp
protected: void uploadPixels(const ImagePtr& image, bool buildMipmaps = false, bool compress = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const ImagePtr&` | `image` |  | - |
| `bool` | `buildMipmaps` | `false` | - |
| `bool` | `compress` | `false` | - |

---

(setupsize)=
## `setupSize`

**Signature:**
```cpp
void setupSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(setupwrap)=
## `setupWrap`

**Signature:**
```cpp
void setupWrap();
```

---

(setupfilters)=
## `setupFilters`

**Signature:**
```cpp
void setupFilters();
```

---

(setuptranformmatrix)=
## `setupTranformMatrix`

**Signature:**
```cpp
void setupTranformMatrix();
```

---

(setuppixels)=
## `setupPixels`

**Signature:**
```cpp
void setupPixels(int level, const Size& size, uchar *pixels, int channels = 4, bool compress = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `level` |  | - |
| `const Size&` | `size` |  | - |
| `uchar *pixels` | - |  | - |
| `int` | `channels` | `4` | - |
| `bool` | `compress` | `false` | - |

---

(settime)=
## `setTime`

**Signature:**
```cpp
void setTime(ticks_t time);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ticks_t` | `time` | - |

---

(setcancache)=
## `setCanCache`

**Signature:**
```cpp
void setCanCache(bool canCache);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `canCache` | - |

---

(getid)=
## `getId`

**Signature:**
```cpp
uint getId();
```

**Returns:**
- `uint`

---

(getuniqueid)=
## `getUniqueId`

**Signature:**
```cpp
uint getUniqueId();
```

**Returns:**
- `uint`

---

(gettime)=
## `getTime`

**Signature:**
```cpp
ticks_t getTime();
```

**Returns:**
- `ticks_t`

---

(getwidth)=
## `getWidth`

**Signature:**
```cpp
int getWidth();
```

**Returns:**
- `int`

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

(getsize)=
## `getSize`

**Signature:**
```cpp
const Size& getSize();
```

**Returns:**
- `const Size&`

---

(gettransformmatrix)=
## `getTransformMatrix`

**Signature:**
```cpp
const Matrix3& getTransformMatrix();
```

**Returns:**
- `const Matrix3&`

---

(isempty)=
## `isEmpty`

**Signature:**
```cpp
bool isEmpty();
```

**Returns:**
- `bool`

---

(hasrepeat)=
## `hasRepeat`

**Signature:**
```cpp
bool hasRepeat();
```

**Returns:**
- `bool`

---

(hasmipmaps)=
## `hasMipmaps`

**Signature:**
```cpp
bool hasMipmaps();
```

**Returns:**
- `bool`

---

(cancache)=
## `canCache`

**Signature:**
```cpp
bool canCache();
```

**Returns:**
- `bool`

---

(isanimatedtexture)=
## `isAnimatedTexture`

**Signature:**
```cpp
virtual bool isAnimatedTexture();
```

**Returns:**
- `bool`

---
