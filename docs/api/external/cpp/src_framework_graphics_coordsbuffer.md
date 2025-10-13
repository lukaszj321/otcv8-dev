# src/framework/graphics/coordsbuffer.h

```cpp
public: CoordsBuffer();
```
```cpp
void addBoudingRect(const Rect& dest, int innerLineWidth);
```
```cpp
void addRepeatedRects(const Rect& dest, const Rect& src);
```
```cpp
void unlock(bool clear = false);
```
```cpp
Rect getTextureRect();
```
```cpp
void clear();
```
```cpp
void addTriangle(const Point& a, const Point& b, const Point& c);
```
```cpp
void addRect(const Rect& dest);
```
```cpp
void addRect(const Rect& dest, const Rect& src);
```
```cpp
void addRect(const RectF& dest, const RectF& src);
```
```cpp
void addQuad(const Rect& dest, const Rect& src);
```
```cpp
void addUpsideDownQuad(const Rect& dest, const Rect& src);
```
```cpp
int getVertexCount();
```
```cpp
int getTextureCoordCount();
```
```cpp
HardwareBuffer* getVertexHardwareCache();
```
```cpp
HardwareBuffer* getTextureHardwareCache();
```
```cpp
void cache();
```