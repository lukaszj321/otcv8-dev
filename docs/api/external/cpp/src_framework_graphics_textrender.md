---
title: "src/framework/graphics/textrender.h"
source_file: "src/framework/graphics/textrender.h"
generated_at: "2025-10-31T23:33:30.344Z"
doc_type: "cpp_api"
---

# src/framework/graphics/textrender.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

**Returns:**
- `public: void`

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(poll)=
## `poll`

**Signature:**
```cpp
void poll();
```

---

(addtext)=
## `addText`

**Signature:**
```cpp
uint64_t addText(BitmapFontPtr font, const std::string& text, const Size& size, Fw::AlignmentFlag align = Fw::AlignTopLeft);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `BitmapFontPtr` | `font` | - |
| `const std::string&` | `text` | - |
| `const Size&` | `size` | - |
| `Fw::AlignmentFlag align = Fw::` | `AlignTopLeft` | - |

**Returns:**
- `uint64_t`

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Rect& rect, const std::string& text, BitmapFontPtr font, const Color& color = Color::white, Fw::AlignmentFlag align = Fw::AlignTopLeft, bool shadow = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |
| `const std::string&` | `text` | - |
| `BitmapFontPtr` | `font` | - |
| `const Color& color = Color::` | `white` | - |
| `Fw::AlignmentFlag align = Fw::` | `AlignTopLeft` | - |
| `bool shadow =` | `false` | - |

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Point& pos, uint64_t hash, const Color& color, bool shadow = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `uint64_t` | `hash` | - |
| `const Color&` | `color` | - |
| `bool shadow =` | `false` | - |

---

(drawcoloredtext)=
## `drawColoredText`

**Signature:**
```cpp
void drawColoredText(const Point& pos, uint64_t hash, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `uint64_t` | `hash` | - |
| `const std::vector&lt;std::pair&lt;` | `int` | - |
| `Color&gt;&gt;&` | `colors` | - |
| `bool shadow =` | `false` | - |

---
