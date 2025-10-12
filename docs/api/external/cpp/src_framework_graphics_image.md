# src/framework/graphics/image.h

```cpp
public:
    Image(const Size& size, int bpp = 4, uint8 *pixels = nullptr);
```
```cpp
static ImagePtr load(std::string file);
```
```cpp
static ImagePtr loadPNG(const std::string& file);
```
```cpp
static ImagePtr loadPNG(const void* data, uint32_t size);
```
```cpp
void savePNG(const std::string& fileName);
```
```cpp
void blit(const Point& dest, const ImagePtr& other);
```
```cpp
void paste(const ImagePtr& other);
```
```cpp
ImagePtr upscale();
```
```cpp
void resize(const Size& size) { m_size = size; m_pixels.resize(size.area() * m_bpp, 0);
```
```cpp
bool nextMipmap();
```
```cpp
void setPixel(int x, int y, uint8 *pixel) { memcpy(&m_pixels[(y * m_size.width() + x) * m_bpp], pixel, m_bpp);
```
```cpp
void setPixel(int x, int y, uint32_t argb) { setPixel(x, y, (uint8*)&argb);
```
```cpp
void setPixel(int x, int y, const Color& color) { m_pixels[(y * m_size.width() + x) * m_bpp] = color.r();
```
```cpp
std::vector<uint8>& getPixels() { return m_pixels; } uint8* getPixelData() { return &m_pixels[0]; } int getPixelCount() { return m_size.area();
```
```cpp
const Size& getSize() { return m_size; } int getWidth() { return m_size.width();
```
```cpp
int getHeight() { return m_size.height();
```
```cpp
int getBpp() { return m_bpp; } uint8* getPixel(int x, int y) { return &m_pixels[(y * m_size.width() + x) * m_bpp]; } static ImagePtr fromQRCode(const std::string& code, int border);
```