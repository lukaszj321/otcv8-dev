---
title: "src/client/statictext.h"
source_file: "src/client/statictext.h"
generated_at: "2025-11-01T08:45:15.287Z"
doc_type: "cpp_api"
---

# src/client/statictext.h

(statictext)=
## `StaticText`

**Signature:**
```cpp
public: StaticText();
```

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Point& dest, const Rect& parentRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `const Rect&` | `parentRect` | - |

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

(addmessage)=
## `addMessage`

**Signature:**
```cpp
bool addMessage(const std::string& name, Otc::MessageMode mode, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `Otc::MessageMode` | `mode` | - |
| `const std::string&` | `text` | - |

**Returns:**
- `bool`

---

(addcoloredmessage)=
## `addColoredMessage`

**Signature:**
```cpp
bool addColoredMessage(const std::string& name, Otc::MessageMode mode, const std::vector<std::string>& texts);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `Otc::MessageMode` | `mode` | - |
| `const std::vector&lt;std::string&gt;&` | `texts` | - |

**Returns:**
- `bool`

---

(update)=
## `update`

**Signature:**
```cpp
private: void update();
```

---

(scheduleupdate)=
## `scheduleUpdate`

**Signature:**
```cpp
void scheduleUpdate();
```

---

(compose)=
## `compose`

**Signature:**
```cpp
void compose();
```

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

(gettext)=
## `getText`

**Signature:**
```cpp
std::string getText();
```

**Returns:**
- `std::string`

---

(getmessagemode)=
## `getMessageMode`

**Signature:**
```cpp
Otc::MessageMode getMessageMode();
```

**Returns:**
- `Otc::MessageMode`

---

(getfirstmessage)=
## `getFirstMessage`

**Signature:**
```cpp
std::vector<std::string> getFirstMessage();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(isyell)=
## `isYell`

**Signature:**
```cpp
bool isYell();
```

**Returns:**
- `bool`

---

(asstatictext)=
## `asStaticText`

**Signature:**
```cpp
StaticTextPtr asStaticText();
```

**Returns:**
- `StaticTextPtr`

---

(isstatictext)=
## `isStaticText`

**Signature:**
```cpp
bool isStaticText();
```

**Returns:**
- `bool`

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

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
CachedText& getCachedText();
```

**Returns:**
- `CachedText&`

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
