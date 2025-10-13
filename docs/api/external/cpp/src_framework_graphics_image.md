# src/framework/graphics/image.h

```cpp
public: Image(const Size& size, int bpp = 4, uint8 *pixels = nullptr);
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
bool nextMipmap();
```
```cpp
static ImagePtr fromQRCode(const std::string& code, int border);
```
```cpp
void resize(const Size& size);
```
```cpp
void setPixel(int x, int y, uint8 *pixel);
```
```cpp
void setPixel(int x, int y, uint32_t argb);
```
```cpp
void setPixel(int x, int y, const Color& color);
```
```cpp
std::vector<uint8>& getPixels();
```
```cpp
uint8* getPixelData();
```
```cpp
int getPixelCount();
```
```cpp
const Size& getSize();
```
```cpp
int getWidth();
```
```cpp
int getHeight();
```
```cpp
int getBpp();
```
```cpp
uint8* getPixel(int x, int y);
```