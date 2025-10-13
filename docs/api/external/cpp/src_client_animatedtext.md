# src/client/animatedtext.h

```cpp
public: AnimatedText();
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
void setFont(const std::string& fontName);
```
```cpp
bool merge(const AnimatedTextPtr& other);
```
```cpp
protected: virtual void onAppear();
```
```cpp
void setOffset(const Point& offset);
```
```cpp
Color getColor();
```
```cpp
const CachedText& getCachedText();
```
```cpp
Point getOffset();
```
```cpp
Timer getTimer();
```
```cpp
AnimatedTextPtr asAnimatedText();
```
```cpp
bool isAnimatedText();
```
```cpp
std::string getText();
```