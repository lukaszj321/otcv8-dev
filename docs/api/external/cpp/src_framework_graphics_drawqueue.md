# src/framework/graphics/drawqueue.h

```cpp
virtual void draw();
```
```cpp
virtual void draw(const Point& pos);
```
```cpp
virtual bool cache();
```
```cpp
void draw();
```
```cpp
void draw(const Point& pos);
```
```cpp
bool cache();
```
```cpp
void draw();
```
```cpp
bool cache();
```
```cpp
void draw();
```
```cpp
bool cache();
```
```cpp
void draw();
```
```cpp
void draw();
```
```cpp
void draw();
```
```cpp
virtual void start(DrawQueue*);
```
```cpp
virtual void end(DrawQueue*);
```
```cpp
void draw(DrawType drawType = DRAW_ALL);
```
```cpp
DrawQueueItemTexturedRect* item(new DrawQueueItemTexturedRect(dest, texture, src, color));
```
```cpp
void addText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft, const Color& color = Color::white, bool shadow = false);
```
```cpp
void addColoredText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```
```cpp
void setFrameBuffer(const Rect& dest, const Size& size, const Rect& src);
```
```cpp
void correctOutfit(const Rect& dest, int fromPos, bool oldScaling);
```
```cpp
virtual void draw();
```
```cpp
virtual void draw(const Point& pos);
```
```cpp
virtual bool cache();
```
```cpp
void add(DrawQueueItem* item);
```
```cpp
DrawQueueItemTexturedRect* addTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src, const Color& color = Color::white);
```
```cpp
void addTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const Color& color = Color::white);
```
```cpp
void addColoredTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const std::vector<std::pair<int, Color>>& colors);
```
```cpp
void addFilledRect(const Rect& dest, const Color& color = Color::white);
```
```cpp
void addFillCoords(CoordsBuffer& coords, const Color& color = Color::white);
```
```cpp
void addClearRect(const Rect& dest, const Color& color = Color::white);
```
```cpp
void addFilledTriangle(const Point& a, const Point& b, const Point& c, const Color& color = Color::white);
```
```cpp
void addBoundingRect(const Rect& dest, int innerLineWidth, const Color& color = Color::white);
```
```cpp
void addLine(const std::vector<Point>& points, int width, const Color& color = Color::white);
```
```cpp
bool hasFrameBuffer();
```
```cpp
Rect getFrameBufferDest();
```
```cpp
Size getFrameBufferSize();
```
```cpp
Rect getFrameBufferSrc();
```
```cpp
size_t size();
```
```cpp
void setOpacity(size_t start, float opacity);
```
```cpp
void setClip(size_t start, const Rect& clip);
```
```cpp
void setRotation(size_t start, const Point& center, float angle);
```
```cpp
void setMark(size_t start, const Color& color);
```
```cpp
void markMapPosition();
```
```cpp
void setShader(const std::string& shader);
```
```cpp
std::string getShader();
```