---
title: "src/framework/util/color.h"
source_file: "src/framework/util/color.h"
generated_at: "2025-11-01T05:32:59.309Z"
doc_type: "cpp_api"
---

# src/framework/util/color.h

(tohex)=
## `toHex`

**Signature:**
```cpp
std::string toHex();
```

**Returns:**
- `std::string`

---

(getoutfitcolor)=
## `getOutfitColor`

**Signature:**
```cpp
static Color getOutfitColor(int color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `color` | - |

**Returns:**
- `Color`

---

(setfill)=
## `setfill`

**Signature:**
```cpp
out << dec << setfill(' ');
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `' '` | - | - |

**Returns:**
- `out &lt;&lt; dec &lt;&lt;`

---

(a)=
## `a`

**Signature:**
```cpp
uint8 a();
```

**Returns:**
- `uint8`

---

(b)=
## `b`

**Signature:**
```cpp
uint8 b();
```

**Returns:**
- `uint8`

---

(g)=
## `g`

**Signature:**
```cpp
uint8 g();
```

**Returns:**
- `uint8`

---

(r)=
## `r`

**Signature:**
```cpp
uint8 r();
```

**Returns:**
- `uint8`

---

(af)=
## `aF`

**Signature:**
```cpp
float aF();
```

**Returns:**
- `float`

---

(bf)=
## `bF`

**Signature:**
```cpp
float bF();
```

**Returns:**
- `float`

---

(gf)=
## `gF`

**Signature:**
```cpp
float gF();
```

**Returns:**
- `float`

---

(rf)=
## `rF`

**Signature:**
```cpp
float rF();
```

**Returns:**
- `float`

---

(setred)=
## `setRed`

**Signature:**
```cpp
void setRed(int r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `r` | - |

---

(setgreen)=
## `setGreen`

**Signature:**
```cpp
void setGreen(int g);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `g` | - |

---

(setblue)=
## `setBlue`

**Signature:**
```cpp
void setBlue(int b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `b` | - |

---

(setalpha)=
## `setAlpha`

**Signature:**
```cpp
void setAlpha(int a);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `a` | - |

---

(setred-1)=
## `setRed`

**Signature:**
```cpp
void setRed(float r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `r` | - |

---

(setgreen-1)=
## `setGreen`

**Signature:**
```cpp
void setGreen(float g);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `g` | - |

---

(setblue-1)=
## `setBlue`

**Signature:**
```cpp
void setBlue(float b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `b` | - |

---

(setalpha-1)=
## `setAlpha`

**Signature:**
```cpp
void setAlpha(float a);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `a` | - |

---

(setrgba)=
## `setRGBA`

**Signature:**
```cpp
void setRGBA(uint8 r, uint8 g, uint8 b, uint8 a = 0xFF);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `uint8` | `r` |  | - |
| `uint8` | `g` |  | - |
| `uint8` | `b` |  | - |
| `uint8` | `a` | `0xFF` | - |

---

(setrgba-1)=
## `setRGBA`

**Signature:**
```cpp
void setRGBA(uint32 rgba);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `rgba` | - |

---

(opacity)=
## `opacity`

**Signature:**
```cpp
Color opacity(float opacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `opacity` | - |

**Returns:**
- `Color`

---

(operator)=
## `operator*`

**Signature:**
```cpp
Color operator*(float v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `v` | - |

**Returns:**
- `Color`

---

(to8bit)=
## `to8bit`

**Signature:**
```cpp
static uint8 to8bit(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

**Returns:**
- `uint8`

---

(from8bit)=
## `from8bit`

**Signature:**
```cpp
static Color from8bit(int color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `color` | - |

**Returns:**
- `Color`

---

(operator-1)=
## `operator<<`

**Signature:**
```cpp
inline std::ostream& operator<<(std::ostream& out, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const Color&` | `color` | - |

**Returns:**
- `std::ostream&`

---

(operator-2)=
## `operator>>`

**Signature:**
```cpp
inline std::istream& operator>>(std::istream& in, Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `Color&` | `color` | - |

**Returns:**
- `std::istream&`

---
