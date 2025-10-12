# src/client/animatedtext.h

```cpp
public:
    AnimatedText();
```
```cpp
void drawText(const Point& dest, const Rect& visibleRect);
```
```cpp
void setColor(int color);
```
```cpp
void setText(const std::string& text);
```
```cpp
void setOffset(const Point& offset) { m_offset = offset; } void setFont(const std::string& fontName);
```
```cpp
Color getColor() { return m_color; } const CachedText& getCachedText() const { return m_cachedText; } Point getOffset() { return m_offset; } Timer getTimer() { return m_animationTimer; } bool merge(const AnimatedTextPtr& other);
```
```cpp
AnimatedTextPtr asAnimatedText() { return static_self_cast<AnimatedText>();
```
```cpp
bool isAnimatedText() { return true; } std::string getText() { return m_cachedText.getText();
```
```cpp
protected:
    virtual void onAppear();
```