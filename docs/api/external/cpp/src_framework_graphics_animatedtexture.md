# src/framework/graphics/animatedtexture.h

```cpp
public:
    AnimatedTexture(const Size& size, std::vector<ImagePtr> frames, std::vector<int> framesDelay, bool buildMipmaps = false, bool compress = false);
```
```cpp
void replace(const ImagePtr& image) { } void update();
```
```cpp
virtual bool isAnimatedTexture() { return true; } protected: virtual bool buildHardwareMipmaps();
```
```cpp
virtual void setSmooth(bool smooth);
```
```cpp
virtual void setRepeat(bool repeat);
```