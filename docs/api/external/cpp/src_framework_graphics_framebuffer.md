# src/framework/graphics/framebuffer.h

```cpp
public:
    FrameBuffer(bool withDepth = false);
```
```cpp
void resize(const Size& size);
```
```cpp
void bind(const FrameBufferPtr& depthFramebuffer = nullptr);
```
```cpp
void release();
```
```cpp
void draw();
```
```cpp
void draw(const Rect& dest);
```
```cpp
void draw(const Rect& dest, const Rect& src);
```
```cpp
void setSmooth(bool enabled);
```
```cpp
TexturePtr getTexture() { return m_texture; } Size getSize();
```
```cpp
bool isSmooth() { return m_smooth; } #ifdef WITH_DEPTH_BUFFER uint getDepthRenderBuffer() { return m_depthRbo; } bool hasDepth() { return m_depth; } #endif std::vector<uint32_t> readPixels();
```
```cpp
void doScreenshot(std::string fileName);
```
```cpp
private:
    void internalCreate();
```
```cpp
void internalBind();
```
```cpp
void internalRelease();
```