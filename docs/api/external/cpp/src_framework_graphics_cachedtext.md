# src/framework/graphics/cachedtext.h

```cpp
public:
    CachedText();
```
```cpp
void draw(const Rect& rect, const Color& color);
```
```cpp
void wrapText(int maxWidth);
```
```cpp
void setFont(const BitmapFontPtr& font) { m_font = font; update();
```
```cpp
void setText(const std::string& text) { m_textColors.clear();
```
```cpp
void setColoredText(const std::vector<std::string>& texts);
```
```cpp
void setAlign(Fw::AlignmentFlag align) { m_align = align; update();
```
```cpp
Size getTextSize() { return m_textSize; } std::string getText() const { return m_text; } BitmapFontPtr getFont() const { return m_font; } Fw::AlignmentFlag getAlign() { return m_align; } bool hasText() { return !m_text.empty();
```
```cpp
private:
    void update();
```