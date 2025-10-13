# src/client/lightview.h

```cpp
return addLight(pos, light.color, light.intensity);
```
```cpp
void addLight(const Point& pos, uint8_t color, uint8_t intensity);
```
```cpp
void setFieldBrightness(const Point& pos, size_t start, uint8_t color);
```
```cpp
public: LightView(TexturePtr& lightTexture, const Size& mapSize, const Rect& dest, const Rect& src, uint8_t color, uint8_t intensity) : DrawQueueItem(nullptr), m_lightTexture(lightTexture), m_mapSize(mapSize), m_dest(dest), m_src(src);
```
```cpp
inline void addLight(const Point& pos, const Light& light);
```
```cpp
size_t size();
```