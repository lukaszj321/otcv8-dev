# src/framework/graphics/vertexarray.h

```cpp
public:
    VertexArray() {} ~VertexArray() { if (m_hardwareBuffer) delete m_hardwareBuffer; } VertexArray(VertexArray& c) : m_buffer(c.m_buffer) { m_hardwareBuffer = nullptr; } VertexArray& operator=(VertexArray& c) = delete; inline void addVertex(float x, float y) { m_buffer << x << y; } inline void addTriangle(const Point& a, const Point& b, const Point& c) { addVertex(a.x, a.y);
```
```cpp
inline void addRect(const Rect& rect) { float top = rect.top();
```
```cpp
inline void addRect(const RectF& rect) { float top = rect.top();
```
```cpp
inline void addQuad(const Rect& rect) { float top = rect.top();
```
```cpp
inline void addUpsideDownQuad(const Rect& rect) { float top = rect.top();
```
```cpp
void clear() { m_buffer.reset();
```
```cpp
int vertexCount() const { return m_buffer.size() / 2; } int size() const { return m_buffer.size();
```
```cpp
void cache() { if (m_buffer.size() < CACHE_MIN_VERTICES_COUNT) return; if (m_hardwareBuffer) return; m_hardwareBuffer = new HardwareBuffer(HardwareBuffer::VertexBuffer);
```