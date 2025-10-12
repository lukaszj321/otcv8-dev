# src/framework/graphics/texture.h

```cpp
public:
    Texture(const Size& size, bool depthTexture = false, bool smooth = false, bool upsideDown = false);
```
```cpp
virtual void replace(const ImagePtr& image);
```
```cpp
void resize(const Size& size);
```
```cpp
virtual void update();
```
```cpp
virtual void setUpsideDown(bool upsideDown);
```
```cpp
virtual void setSmooth(bool smooth);
```
```cpp
virtual void setRepeat(bool repeat);
```
```cpp
virtual bool buildHardwareMipmaps();
```
```cpp
void setTime(ticks_t time) { m_time = time; } void setCanCache(bool canCache) { m_canCache = canCache; } uint getId() { return m_id; } uint getUniqueId() { return m_uniqueId; } ticks_t getTime() { return m_time; } int getWidth() { return m_size.width();
```
```cpp
int getHeight() { return m_size.height();
```
```cpp
const Size& getSize() { return m_size; } const Matrix3& getTransformMatrix() { return m_transformMatrix; } bool isEmpty() { return false; } bool hasRepeat() { return m_repeat; } bool hasMipmaps() { return m_hasMipmaps; } bool canCache() { return m_canCache; } virtual bool isAnimatedTexture() { return false; } protected: void uploadPixels(const ImagePtr& image, bool buildMipmaps = false, bool compress = false);
```
```cpp
void setupSize(const Size& size);
```
```cpp
void setupWrap();
```
```cpp
void setupFilters();
```
```cpp
void setupTranformMatrix();
```
```cpp
void setupPixels(int level, const Size& size, uchar *pixels, int channels = 4, bool compress = false);
```