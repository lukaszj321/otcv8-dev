# src/framework/graphics/coordsbuffer.h

```cpp
public:
    CoordsBuffer();
```
```cpp
void clear() { if (m_locked) unlock(true);
```
```cpp
void addTriangle(const Point& a, const Point& b, const Point& c) { if (m_locked) unlock();
```
```cpp
void addRect(const Rect& dest) { if (m_locked) unlock();
```
```cpp
void addRect(const Rect& dest, const Rect& src) { if (m_locked) unlock();
```
```cpp
void addRect(const RectF& dest, const RectF& src) { if (m_locked) unlock();
```
```cpp
void addQuad(const Rect& dest, const Rect& src) { if (m_locked) unlock();
```
```cpp
void addUpsideDownQuad(const Rect& dest, const Rect& src) { if (m_locked) unlock();
```
```cpp
void addBoudingRect(const Rect& dest, int innerLineWidth);
```
```cpp
void addRepeatedRects(const Rect& dest, const Rect& src);
```
```cpp
int getVertexCount() { return m_vertexArray->vertexCount();
```
```cpp
int getTextureCoordCount() { return m_textureCoordArray->vertexCount();
```
```cpp
HardwareBuffer* getVertexHardwareCache() { return m_vertexArray->getHardwareCache();
```
```cpp
HardwareBuffer* getTextureHardwareCache() { return m_textureCoordArray->getHardwareCache();
```
```cpp
void unlock(bool clear = false);
```
```cpp
void cache() { m_locked = true; m_vertexArray->cache();
```
```cpp
Rect getTextureRect();
```