# src/client/statictext.h

```cpp
public: StaticText();
```
```cpp
void drawText(const Point& dest, const Rect& parentRect);
```
```cpp
void setText(const std::string& text);
```
```cpp
void setFont(const std::string& fontName);
```
```cpp
bool addMessage(const std::string& name, Otc::MessageMode mode, const std::string& text);
```
```cpp
bool addColoredMessage(const std::string& name, Otc::MessageMode mode, const std::vector<std::string>& texts);
```
```cpp
private: void update();
```
```cpp
void scheduleUpdate();
```
```cpp
void compose();
```
```cpp
std::string getName();
```
```cpp
std::string getText();
```
```cpp
Otc::MessageMode getMessageMode();
```
```cpp
std::vector<std::string> getFirstMessage();
```
```cpp
bool isYell();
```
```cpp
StaticTextPtr asStaticText();
```
```cpp
bool isStaticText();
```
```cpp
void setColor(const Color& color);
```
```cpp
Color getColor();
```
```cpp
CachedText& getCachedText();
```
```cpp
bool hasText();
```