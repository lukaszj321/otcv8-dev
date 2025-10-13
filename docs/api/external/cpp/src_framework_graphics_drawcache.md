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
void addRect(const Rect& dest, const Color& color);
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
bool hasSpace(int size);
```
```cpp
inline int getSize();
```
```cpp
private: inline void addRectRaw(float* dest, const Rect& rect);
```
```cpp
inline void addColorRaw(const Color& color, int count);
```