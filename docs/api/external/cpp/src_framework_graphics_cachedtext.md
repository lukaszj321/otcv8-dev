# src/framework/graphics/cachedtext.h

```cpp
public: CachedText();
```
```cpp
void draw(const Rect& rect, const Color& color);
```
```cpp
void wrapText(int maxWidth);
```
```cpp
void setColoredText(const std::vector<std::string>& texts);
```
```cpp
private: void update();
```
```cpp
void setFont(const BitmapFontPtr& font);
```
```cpp
void setText(const std::string& text);
```
```cpp
void setAlign(Fw::AlignmentFlag align);
```
```cpp
Size getTextSize();
```
```cpp
std::string getText();
```
```cpp
BitmapFontPtr getFont();
```
```cpp
Fw::AlignmentFlag getAlign();
```
```cpp
bool hasText();
```