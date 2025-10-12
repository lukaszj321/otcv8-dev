# src/client/lightview.h

```cpp
public:
    LightView(TexturePtr& lightTexture, const Size& mapSize, const Rect& dest, const Rect& src, uint8_t color, uint8_t intensity) : DrawQueueItem(nullptr), m_lightTexture(lightTexture), m_mapSize(mapSize), m_dest(dest), m_src(src) { m_globalLight = Color::from8bit(color) * ((float)intensity / 255.f);
```
```cpp
inline void addLight(const Point& pos, const Light& light) { return addLight(pos, light.color, light.intensity);
```
```cpp
void addLight(const Point& pos, uint8_t color, uint8_t intensity);
```
```cpp
void setFieldBrightness(const Point& pos, size_t start, uint8_t color);
```
```cpp
size_t size() { return m_lights.size();
```