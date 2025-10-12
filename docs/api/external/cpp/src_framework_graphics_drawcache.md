# src/framework/graphics/drawcache.h

```cpp
void draw();
```
```cpp
void bind();
```
```cpp
void release();
```
```cpp
bool hasSpace(int size) { return size + m_size < MAX_SIZE; } inline int getSize() { return m_size; } void addRect(const Rect& dest, const Color& color);
```
```cpp
void addTexturedRect(const Rect& dest, const Rect& src, const Color& color);
```
```cpp
void addCoords(CoordsBuffer& coords, const Color& color);
```
```cpp
void addTexturedCoords(CoordsBuffer& coords, const Point& offset, const Color& color);
```
```cpp
private:
    inline void addRectRaw(float* dest, const Rect& rect) { dest[0] = dest[4] = dest[6] = rect.left();
```
```cpp
inline void addColorRaw(const Color& color, int count) { static float c[4]; c[0] = color.rF();
```