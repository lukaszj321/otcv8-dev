---
title: "src/framework/graphics/bitmapfont.h"
source_file: "src/framework/graphics/bitmapfont.h"
generated_at: "2025-11-01T04:06:42.745Z"
doc_type: "cpp_api"
---

# src/framework/graphics/bitmapfont.h

(load)=
## `load`

Load font from otml node

**Signature:**
```cpp
void load(const OTMLNodePtr& fontNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `fontNode` | - |

---

(drawtext)=
## `drawText`

Simple text render starting at startPos

**Signature:**
```cpp
void drawText(const std::string& text, const Point& startPos, const Color& color = Color::white, bool shadow = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `text` |  | - |
| `const Point&` | `startPos` |  | - |
| `const Color&` | `color` | `Color::white` | - |
| `bool` | `shadow` | `false` | - |

---

(drawtext-1)=
## `drawText`

Advanced text render delimited by a screen region and alignment

**Signature:**
```cpp
void drawText(const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft, const Color& color = Color::white, bool shadow = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `text` |  | - |
| `const Rect&` | `screenCoords` |  | - |
| `Fw::AlignmentFlag` | `align` | `Fw::AlignTopLeft` | - |
| `const Color&` | `color` | `Color::white` | - |
| `bool` | `shadow` | `false` | - |

---

(drawcoloredtext)=
## `drawColoredText`

**Signature:**
```cpp
void drawColoredText(const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `text` |  | - |
| `const Rect&` | `screenCoords` |  | - |
| `Fw::AlignmentFlag` | `align` |  | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;&` | `colors` |  | - |
| `bool` | `shadow` | `false` | - |

---

(calculatedrawtextcoords)=
## `calculateDrawTextCoords`

**Signature:**
```cpp
void calculateDrawTextCoords(CoordsBuffer& coordsBuffer, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CoordsBuffer&` | `coordsBuffer` |  | - |
| `const std::string&` | `text` |  | - |
| `const Rect&` | `screenCoords` |  | - |
| `Fw::AlignmentFlag` | `align` | `Fw::AlignTopLeft` | - |

---

(calculateglyphspositions)=
## `calculateGlyphsPositions`

Calculate glyphs positions to use on render, also calculates textBoxSize if wanted

**Signature:**
```cpp
const std::vector<Point>& calculateGlyphsPositions(const std::string& text, Fw::AlignmentFlag align = Fw::AlignTopLeft, Size* textBoxSize = NULL);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `text` |  | - |
| `Fw::AlignmentFlag` | `align` | `Fw::AlignTopLeft` | - |
| `Size*` | `textBoxSize` | `NULL` | - |

**Returns:**
- `const std::vector&lt;Point&gt;&`

---

(calculatetextrectsize)=
## `calculateTextRectSize`

Simulate render and calculate text size

**Signature:**
```cpp
Size calculateTextRectSize(const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |

**Returns:**
- `Size`

---

(wraptext)=
## `wrapText`

**Signature:**
```cpp
std::string wrapText(const std::string& text, int maxWidth, std::vector<std::pair<int, Color>>* colors = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `text` |  | - |
| `int` | `maxWidth` |  | - |
| `std::vector&lt;std::pair&lt;int, Color&gt;&gt;*` | `colors` | `nullptr` | - |

**Returns:**
- `std::string`

---

(calculateglyphswidthsautomatically)=
## `calculateGlyphsWidthsAutomatically`

Calculates each font character by inspecting font bitmap

**Signature:**
```cpp
void calculateGlyphsWidthsAutomatically(const ImagePtr& image, const Size& glyphSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ImagePtr&` | `image` | - |
| `const Size&` | `glyphSize` | - |

---

(updatecolors)=
## `updateColors`

**Signature:**
```cpp
void updateColors(std::vector<std::pair<int, Color>>* colors, int pos, int newTextLen);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::vector&lt;std::pair&lt;int, Color&gt;&gt;*` | `colors` | - |
| `int` | `pos` | - |
| `int` | `newTextLen` | - |

---

(getid)=
## `getId`

**Signature:**
```cpp
int getId();
```

**Returns:**
- `int`

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

(getglyphheight)=
## `getGlyphHeight`

**Signature:**
```cpp
int getGlyphHeight();
```

**Returns:**
- `int`

---

(getglyphstexturecoords)=
## `getGlyphsTextureCoords`

**Signature:**
```cpp
const Rect* getGlyphsTextureCoords();
```

**Returns:**
- `const Rect*`

---

(getglyphssize)=
## `getGlyphsSize`

**Signature:**
```cpp
const Size* getGlyphsSize();
```

**Returns:**
- `const Size*`

---

(gettexture)=
## `getTexture`

**Signature:**
```cpp
const TexturePtr& getTexture();
```

**Returns:**
- `const TexturePtr&`

---

(getyoffset)=
## `getYOffset`

**Signature:**
```cpp
int getYOffset();
```

**Returns:**
- `int`

---

(getglyphspacing)=
## `getGlyphSpacing`

**Signature:**
```cpp
Size getGlyphSpacing();
```

**Returns:**
- `Size`

---
