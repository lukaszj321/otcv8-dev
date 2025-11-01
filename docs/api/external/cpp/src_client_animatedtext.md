---
title: "src/client/animatedtext.h"
source_file: "src/client/animatedtext.h"
generated_at: "2025-11-01T06:09:06.156Z"
doc_type: "cpp_api"
---

# src/client/animatedtext.h

(animatedtext)=
## `AnimatedText`

**Signature:**
```cpp
public: AnimatedText();
```

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Point& dest, const Rect& visibleRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `const Rect&` | `visibleRect` | - |

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(int color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `color` | - |

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

(setfont)=
## `setFont`

**Signature:**
```cpp
void setFont(const std::string& fontName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fontName` | - |

---

(merge)=
## `merge`

**Signature:**
```cpp
bool merge(const AnimatedTextPtr& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const AnimatedTextPtr&` | `other` | - |

**Returns:**
- `bool`

---

(onappear)=
## `onAppear`

**Signature:**
```cpp
protected: virtual void onAppear();
```

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

(getcolor)=
## `getColor`

**Signature:**
```cpp
Color getColor();
```

**Returns:**
- `Color`

---

(getcachedtext)=
## `getCachedText`

**Signature:**
```cpp
const CachedText& getCachedText();
```

**Returns:**
- `const CachedText&`

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

(gettimer)=
## `getTimer`

**Signature:**
```cpp
Timer getTimer();
```

**Returns:**
- `Timer`

---

(asanimatedtext)=
## `asAnimatedText`

**Signature:**
```cpp
AnimatedTextPtr asAnimatedText();
```

**Returns:**
- `AnimatedTextPtr`

---

(isanimatedtext)=
## `isAnimatedText`

**Signature:**
```cpp
bool isAnimatedText();
```

**Returns:**
- `bool`

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
