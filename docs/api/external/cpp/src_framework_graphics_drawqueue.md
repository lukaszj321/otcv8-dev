# src/framework/graphics/drawqueue.h

```cpp
virtual void draw() {} virtual void draw(const Point& pos) {} virtual bool cache() { return false; } TexturePtr m_texture; Color m_color; }; struct DrawQueueItemTexturedRect : public DrawQueueItem { DrawQueueItemTexturedRect() : DrawQueueItem(nullptr) {} DrawQueueItemTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src, const Color& color) : DrawQueueItem(texture, color), m_dest(dest), m_src(src) {}; virtual ~DrawQueueItemTexturedRect() = default; virtual void draw();
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
void draw() override; void draw(const Point& pos) override; bool cache() override { return false; } std::string m_shader; }; struct DrawQueueItemFilledRect : public DrawQueueItem { DrawQueueItemFilledRect(const Rect& rect, const Color& color) : DrawQueueItem(nullptr, color), m_dest(rect) {}; bool cache();
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
virtual void start(DrawQueue*) = 0; virtual void end(DrawQueue*) = 0; size_t m_start; size_t m_end; }; struct DrawQueueConditionClip : public DrawQueueCondition { DrawQueueConditionClip(size_t start, size_t end, const Rect& rect) : DrawQueueCondition(start, end), m_rect(rect) {} void start(DrawQueue* queue) override; void end(DrawQueue* queue) override; Rect m_rect; Rect m_prevClip; }; struct DrawQueueConditionRotation : public DrawQueueCondition { DrawQueueConditionRotation(size_t start, size_t end, const Point& center, float angle) : DrawQueueCondition(start, end), m_center(center), m_angle(angle) {} void start(DrawQueue* queue) override; void end(DrawQueue* queue) override; Point m_center; float m_angle; }; struct DrawQueueConditionMark : public DrawQueueCondition { DrawQueueConditionMark(size_t start, size_t end, const Color& color) : DrawQueueCondition(start, end), m_color(color) {} void start(DrawQueue* queue) override; void end(DrawQueue* queue) override; Color m_color; }; class DrawQueue { public: DrawQueue() = default; DrawQueue(const DrawQueue&) = delete; DrawQueue& operator= (const DrawQueue&) = delete; ~DrawQueue() { for (auto& item : m_queue) delete item; m_queue.clear();
```
```cpp
void draw(DrawType drawType = DRAW_ALL);
```
```cpp
void add(DrawQueueItem* item) { if (!item) return; m_queue.push_back(item);
```
```cpp
DrawQueueItemTexturedRect* addTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src, const Color& color = Color::white) { DrawQueueItemTexturedRect* item(new DrawQueueItemTexturedRect(dest, texture, src, color));
```
```cpp
void addTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const Color& color = Color::white) { m_queue.push_back(new DrawQueueItemTextureCoords(coords, texture, color));
```
```cpp
void addColoredTextureCoords(CoordsBuffer& coords, const TexturePtr& texture, const std::vector<std::pair<int, Color>>& colors) { m_queue.push_back(new DrawQueueItemColoredTextureCoords(coords, texture, colors));
```
```cpp
void addFilledRect(const Rect& dest, const Color& color = Color::white) { m_queue.push_back(new DrawQueueItemFilledRect(dest, color));
```
```cpp
void addFillCoords(CoordsBuffer& coords, const Color& color = Color::white) { m_queue.push_back(new DrawQueueItemFillCoords(coords, color));
```
```cpp
void addClearRect(const Rect& dest, const Color& color = Color::white) { m_queue.push_back(new DrawQueueItemClearRect(dest, color));
```
```cpp
void addText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft, const Color& color = Color::white, bool shadow = false);
```
```cpp
void addColoredText(BitmapFontPtr font, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```
```cpp
void addFilledTriangle(const Point& a, const Point& b, const Point& c, const Color& color = Color::white) { if (a == b || a == c || b == c) return; CoordsBuffer coordsBuffer; coordsBuffer.addTriangle(a, b, c);
```
```cpp
void addBoundingRect(const Rect& dest, int innerLineWidth, const Color& color = Color::white) { if (dest.isEmpty() || innerLineWidth == 0) return; CoordsBuffer coordsBuffer; coordsBuffer.addBoudingRect(dest, innerLineWidth);
```
```cpp
void addLine(const std::vector<Point>& points, int width, const Color& color = Color::white) { if (points.empty() || width < 0) return; m_queue.push_back(new DrawQueueItemLine(points, width, color));
```
```cpp
void setFrameBuffer(const Rect& dest, const Size& size, const Rect& src);
```
```cpp
bool hasFrameBuffer() { return m_useFrameBuffer; } Rect getFrameBufferDest() { return m_frameBufferDest; } Size getFrameBufferSize() { return m_frameBufferSize; } Rect getFrameBufferSrc() { return m_frameBufferSrc; } size_t size() { return m_queue.size();
```
```cpp
void setOpacity(size_t start, float opacity) { for (size_t i = start; i < m_queue.size();
```
```cpp
void setClip(size_t start, const Rect& clip) { if (start == m_queue.size()) return; m_conditions.push_back(new DrawQueueConditionClip(start, m_queue.size(), clip));
```
```cpp
void setRotation(size_t start, const Point& center, float angle) { if (start == m_queue.size() || angle == 0) return; m_conditions.push_back(new DrawQueueConditionRotation(start, m_queue.size(), center, angle));
```
```cpp
void setMark(size_t start, const Color& color) { if (start == m_queue.size()) return; m_conditions.push_back(new DrawQueueConditionMark(start, m_queue.size(), color));
```
```cpp
void markMapPosition() { mapPosition = m_queue.size();
```
```cpp
void correctOutfit(const Rect& dest, int fromPos, bool oldScaling);
```