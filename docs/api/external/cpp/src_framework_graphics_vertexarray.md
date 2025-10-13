# src/framework/graphics/vertexarray.h

```cpp
public: VertexArray();
```
```cpp
inline void addVertex(float x, float y);
```
```cpp
inline void addTriangle(const Point& a, const Point& b, const Point& c);
```
```cpp
inline void addRect(const Rect& rect);
```
```cpp
inline void addRect(const RectF& rect);
```
```cpp
inline void addQuad(const Rect& rect);
```
```cpp
inline void addUpsideDownQuad(const Rect& rect);
```
```cpp
void clear();
```
```cpp
int vertexCount();
```
```cpp
int size();
```
```cpp
void cache();
```
```cpp
bool isCached();
```
```cpp
HardwareBuffer* getHardwareCache();
```