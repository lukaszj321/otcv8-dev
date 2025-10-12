# src/framework/graphics/textrender.h

```cpp
public:
    void init();
```
```cpp
void terminate();
```
```cpp
void poll();
```
```cpp
uint64_t addText(BitmapFontPtr font, const std::string& text, const Size& size, Fw::AlignmentFlag align = Fw::AlignTopLeft);
```
```cpp
void drawText(const Rect& rect, const std::string& text, BitmapFontPtr font, const Color& color = Color::white, Fw::AlignmentFlag align = Fw::AlignTopLeft, bool shadow = false);
```
```cpp
void drawText(const Point& pos, uint64_t hash, const Color& color, bool shadow = false);
```
```cpp
void drawColoredText(const Point& pos, uint64_t hash, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```