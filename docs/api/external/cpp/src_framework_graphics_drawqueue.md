---
title: "src/framework/graphics/drawqueue.h"
source_file: "src/framework/graphics/drawqueue.h"
generated_at: "2025-11-01T04:06:42.747Z"
doc_type: "cpp_api"
---

# src/framework/graphics/drawqueue.h

(draw)=
## `draw`

**Signature:**
```cpp
virtual void draw();
```

---

(draw-1)=
## `draw`

**Signature:**
```cpp
virtual void draw(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(cache)=
## `cache`

**Signature:**
```cpp
virtual bool cache();
```

**Returns:**
- `bool`

---

(draw-2)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(draw-3)=
## `draw`

**Signature:**
```cpp
void draw(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(cache-1)=
## `cache`

**Signature:**
```cpp
bool cache();
```

**Returns:**
- `bool`

---

(draw-4)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(cache-2)=
## `cache`

**Signature:**
```cpp
bool cache();
```

**Returns:**
- `bool`

---

(draw-5)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(cache-3)=
## `cache`

**Signature:**
```cpp
bool cache();
```

**Returns:**
- `bool`

---

(draw-6)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(draw-7)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(draw-8)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(start)=
## `start`

**Signature:**
```cpp
virtual void start(DrawQueue*);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `DrawQueue*` | - | - |

---

(end)=
## `end`

**Signature:**
```cpp
virtual void end(DrawQueue*);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `DrawQueue*` | - | - |

---

(draw-9)=
## `draw`

**Signature:**
```cpp
void draw(DrawType drawType = DRAW_ALL);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `DrawType` | `drawType` | `DRAW_ALL` | - |

---

(item)=
## `item`

**Signature:**
```cpp
DrawQueueItemTexturedRect* item(new DrawQueueItemTexturedRect(dest, texture, src, color));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `new DrawQueueItemTexturedRect(dest` | - | - |
| `texture` | - | - |
| `src` | - | - |
| `color)` | - | - |

**Returns:**
- `DrawQueueItemTexturedRect*`

---

(addtext)=
## `addText`

**Signature:**
```cpp
void addText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft, const Color& color = Color::white, bool shadow = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `BitmapFontPtr` | `font` |  | - |
| `const std::string&` | `text` |  | - |
| `const Rect&` | `screenCoords` |  | - |
| `Fw::AlignmentFlag` | `align` | `Fw::AlignTopLeft` | - |
| `const Color&` | `color` | `Color::white` | - |
| `bool` | `shadow` | `false` | - |

---

(addcoloredtext)=
## `addColoredText`

**Signature:**
```cpp
void addColoredText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `BitmapFontPtr` | `font` |  | - |
| `const std::string&` | `text` |  | - |
| `const Rect&` | `screenCoords` |  | - |
| `Fw::AlignmentFlag` | `align` |  | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;&` | `colors` |  | - |
| `bool` | `shadow` | `false` | - |

---

(setframebuffer)=
## `setFrameBuffer`

**Signature:**
```cpp
void setFrameBuffer(const Rect& dest, const Size& size, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Size&` | `size` | - |
| `const Rect&` | `src` | - |

---

(correctoutfit)=
## `correctOutfit`

**Signature:**
```cpp
void correctOutfit(const Rect& dest, int fromPos, bool oldScaling);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `int` | `fromPos` | - |
| `bool` | `oldScaling` | - |

---

(draw-10)=
## `draw`

**Signature:**
```cpp
virtual void draw();
```

---

(draw-11)=
## `draw`

**Signature:**
```cpp
virtual void draw(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(cache-4)=
## `cache`

**Signature:**
```cpp
virtual bool cache();
```

**Returns:**
- `bool`

---

(add)=
## `add`

**Signature:**
```cpp
void add(DrawQueueItem* item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `DrawQueueItem*` | `item` | - |

---

(addtexturedrect)=
## `addTexturedRect`

**Signature:**
```cpp
DrawQueueItemTexturedRect* addTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `const TexturePtr&` | `texture` |  | - |
| `const Rect&` | `src` |  | - |
| `const Color&` | `color` | `Color::white` | - |

**Returns:**
- `DrawQueueItemTexturedRect*`

---

(addtexturecoords)=
## `addTextureCoords`

**Signature:**
```cpp
void addTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CoordsBuffer&` | `coords` |  | - |
| `const TexturePtr&` | `texture` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addcoloredtexturecoords)=
## `addColoredTextureCoords`

**Signature:**
```cpp
void addColoredTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const std::vector<std::pair<int, Color>>& colors);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CoordsBuffer&` | `coords` | - |
| `const TexturePtr&` | `texture` | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;&` | `colors` | - |

---

(addfilledrect)=
## `addFilledRect`

**Signature:**
```cpp
void addFilledRect(const Rect& dest, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addfillcoords)=
## `addFillCoords`

**Signature:**
```cpp
void addFillCoords(CoordsBuffer& coords, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CoordsBuffer&` | `coords` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addclearrect)=
## `addClearRect`

**Signature:**
```cpp
void addClearRect(const Rect& dest, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addfilledtriangle)=
## `addFilledTriangle`

**Signature:**
```cpp
void addFilledTriangle(const Point& a, const Point& b, const Point& c, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `a` |  | - |
| `const Point&` | `b` |  | - |
| `const Point&` | `c` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addboundingrect)=
## `addBoundingRect`

**Signature:**
```cpp
void addBoundingRect(const Rect& dest, int innerLineWidth, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `int` | `innerLineWidth` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(addline)=
## `addLine`

**Signature:**
```cpp
void addLine(const std::vector<Point>& points, int width, const Color& color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::vector&lt;Point&gt;&` | `points` |  | - |
| `int` | `width` |  | - |
| `const Color&` | `color` | `Color::white` | - |

---

(hasframebuffer)=
## `hasFrameBuffer`

**Signature:**
```cpp
bool hasFrameBuffer();
```

**Returns:**
- `bool`

---

(getframebufferdest)=
## `getFrameBufferDest`

**Signature:**
```cpp
Rect getFrameBufferDest();
```

**Returns:**
- `Rect`

---

(getframebuffersize)=
## `getFrameBufferSize`

**Signature:**
```cpp
Size getFrameBufferSize();
```

**Returns:**
- `Size`

---

(getframebuffersrc)=
## `getFrameBufferSrc`

**Signature:**
```cpp
Rect getFrameBufferSrc();
```

**Returns:**
- `Rect`

---

(size)=
## `size`

**Signature:**
```cpp
size_t size();
```

**Returns:**
- `size_t`

---

(setopacity)=
## `setOpacity`

**Signature:**
```cpp
void setOpacity(size_t start, float opacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `start` | - |
| `float` | `opacity` | - |

---

(setclip)=
## `setClip`

**Signature:**
```cpp
void setClip(size_t start, const Rect& clip);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `start` | - |
| `const Rect&` | `clip` | - |

---

(setrotation)=
## `setRotation`

**Signature:**
```cpp
void setRotation(size_t start, const Point& center, float angle);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `start` | - |
| `const Point&` | `center` | - |
| `float` | `angle` | - |

---

(setmark)=
## `setMark`

**Signature:**
```cpp
void setMark(size_t start, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `start` | - |
| `const Color&` | `color` | - |

---

(markmapposition)=
## `markMapPosition`

**Signature:**
```cpp
void markMapPosition();
```

---

(setshader)=
## `setShader`

**Signature:**
```cpp
void setShader(const std::string& shader);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `shader` | - |

---

(getshader)=
## `getShader`

**Signature:**
```cpp
std::string getShader();
```

**Returns:**
- `std::string`

---
