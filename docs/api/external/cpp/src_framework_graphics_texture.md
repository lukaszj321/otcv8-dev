# src/framework/graphics/texture.h

```cpp
public: Texture(const Size& size, bool depthTexture = false, bool smooth = false, bool upsideDown = false);
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
protected: void uploadPixels(const ImagePtr& image, bool buildMipmaps = false, bool compress = false);
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
```cpp
void setTime(ticks_t time);
```
```cpp
void setCanCache(bool canCache);
```
```cpp
uint getId();
```
```cpp
uint getUniqueId();
```
```cpp
ticks_t getTime();
```
```cpp
int getWidth();
```
```cpp
int getHeight();
```
```cpp
const Size& getSize();
```
```cpp
const Matrix3& getTransformMatrix();
```
```cpp
bool isEmpty();
```
```cpp
bool hasRepeat();
```
```cpp
bool hasMipmaps();
```
```cpp
bool canCache();
```
```cpp
virtual bool isAnimatedTexture();
```