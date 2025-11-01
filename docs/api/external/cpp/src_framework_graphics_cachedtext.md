---
title: "src/framework/graphics/cachedtext.h"
source_file: "src/framework/graphics/cachedtext.h"
generated_at: "2025-11-01T04:06:42.745Z"
doc_type: "cpp_api"
---

# src/framework/graphics/cachedtext.h

(cachedtext)=
## `CachedText`

**Signature:**
```cpp
public: CachedText();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& rect, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |
| `const Color&` | `color` | - |

---

(wraptext)=
## `wrapText`

**Signature:**
```cpp
void wrapText(int maxWidth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxWidth` | - |

---

(setcoloredtext)=
## `setColoredText`

**Signature:**
```cpp
void setColoredText(const std::vector<std::string>& texts);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;std::string&gt;&` | `texts` | - |

---

(update)=
## `update`

**Signature:**
```cpp
private: void update();
```

---

(setfont)=
## `setFont`

**Signature:**
```cpp
void setFont(const BitmapFontPtr& font);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const BitmapFontPtr&` | `font` | - |

---

(settext)=
## `setText`

**Signature:**
```cpp
void setText(const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |

---

(setalign)=
## `setAlign`

**Signature:**
```cpp
void setAlign(Fw::AlignmentFlag align);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AlignmentFlag` | `align` | - |

---

(gettextsize)=
## `getTextSize`

**Signature:**
```cpp
Size getTextSize();
```

**Returns:**
- `Size`

---

(gettext)=
## `getText`

**Signature:**
```cpp
std::string getText();
```

**Returns:**
- `std::string`

---

(getfont)=
## `getFont`

**Signature:**
```cpp
BitmapFontPtr getFont();
```

**Returns:**
- `BitmapFontPtr`

---

(getalign)=
## `getAlign`

**Signature:**
```cpp
Fw::AlignmentFlag getAlign();
```

**Returns:**
- `Fw::AlignmentFlag`

---

(hastext)=
## `hasText`

**Signature:**
```cpp
bool hasText();
```

**Returns:**
- `bool`

---
