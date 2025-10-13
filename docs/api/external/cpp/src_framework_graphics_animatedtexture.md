# src/framework/graphics/animatedtexture.h

```cpp
public: AnimatedTexture(const Size& size, std::vector<ImagePtr> frames, std::vector<int> framesDelay, bool buildMipmaps = false, bool compress = false);
```
```cpp
void update();
```
```cpp
protected: virtual bool buildHardwareMipmaps();
```
```cpp
virtual void setSmooth(bool smooth);
```
```cpp
virtual void setRepeat(bool repeat);
```
```cpp
void replace(const ImagePtr& image);
```
```cpp
virtual bool isAnimatedTexture();
```