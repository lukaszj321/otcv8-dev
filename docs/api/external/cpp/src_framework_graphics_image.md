---
title: "src/framework/graphics/image.h"
source_file: "src/framework/graphics/image.h"
generated_at: "2025-11-01T08:19:49.444Z"
doc_type: "cpp_api"
---

# src/framework/graphics/image.h

(image)=
## `Image`

**Signature:**
```cpp
public: Image(const Size& size, int bpp = 4, uint8 *pixels = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Size&` | `size` |  | - |
| `int` | `bpp` | `4` | - |
| `uint8 *pixels` | - | `nullptr` | - |

---

(load)=
## `load`

**Signature:**
```cpp
static ImagePtr load(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `ImagePtr`

---

(loadpng)=
## `loadPNG`

**Signature:**
```cpp
static ImagePtr loadPNG(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `ImagePtr`

---

(loadpng-1)=
## `loadPNG`

**Signature:**
```cpp
static ImagePtr loadPNG(const void* data, uint32_t size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const void*` | `data` | - |
| `uint32_t` | `size` | - |

**Returns:**
- `ImagePtr`

---

(savepng)=
## `savePNG`

**Signature:**
```cpp
void savePNG(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(blit)=
## `blit`

**Signature:**
```cpp
void blit(const Point& dest, const ImagePtr& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `const ImagePtr&` | `other` | - |

---

(paste)=
## `paste`

**Signature:**
```cpp
void paste(const ImagePtr& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `other` | - |

---

(upscale)=
## `upscale`

**Signature:**
```cpp
ImagePtr upscale();
```

**Returns:**
- `ImagePtr`

---

(nextmipmap)=
## `nextMipmap`

**Signature:**
```cpp
bool nextMipmap();
```

**Returns:**
- `bool`

---

(fromqrcode)=
## `fromQRCode`

**Signature:**
```cpp
static ImagePtr fromQRCode(const std::string& code, int border);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `code` | - |
| `int` | `border` | - |

**Returns:**
- `ImagePtr`

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

(setpixel)=
## `setPixel`

**Signature:**
```cpp
void setPixel(int x, int y, uint8 *pixel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |
| `uint8 *pixel` | - | - |

---

(setpixel-1)=
## `setPixel`

**Signature:**
```cpp
void setPixel(int x, int y, uint32_t argb);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |
| `uint32_t` | `argb` | - |

---

(setpixel-2)=
## `setPixel`

**Signature:**
```cpp
void setPixel(int x, int y, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |
| `const Color&` | `color` | - |

---

(getpixels)=
## `getPixels`

**Signature:**
```cpp
std::vector<uint8>& getPixels();
```

**Returns:**
- `std::vector&lt;uint8&gt;&`

---

(getpixeldata)=
## `getPixelData`

**Signature:**
```cpp
uint8* getPixelData();
```

**Returns:**
- `uint8*`

---

(getpixelcount)=
## `getPixelCount`

**Signature:**
```cpp
int getPixelCount();
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

(getbpp)=
## `getBpp`

**Signature:**
```cpp
int getBpp();
```

**Returns:**
- `int`

---

(getpixel)=
## `getPixel`

**Signature:**
```cpp
uint8* getPixel(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

**Returns:**
- `uint8*`

---
