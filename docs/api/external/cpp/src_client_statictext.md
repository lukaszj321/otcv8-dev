# src/client/statictext.h

```cpp
public:
    StaticText();
```
```cpp
void drawText(const Point& dest, const Rect& parentRect);
```
```cpp
std::string getName() { return m_name; } std::string getText() { return m_cachedText.getText();
```
```cpp
Otc::MessageMode getMessageMode() { return m_mode; } std::vector<std::string> getFirstMessage() { return m_messages[0].texts; } bool isYell() { return m_mode == Otc::MessageYell || m_mode == Otc::MessageMonsterYell || m_mode == Otc::MessageBarkLoud; } void setText(const std::string& text);
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
StaticTextPtr asStaticText() { return static_self_cast<StaticText>();
```
```cpp
bool isStaticText() { return true; } void setColor(const Color& color) { m_color = color; } Color getColor() { return m_color; } CachedText& getCachedText() { return m_cachedText; } bool hasText() { return m_cachedText.hasText();
```
```cpp
private:
    void update();
```
```cpp
void scheduleUpdate();
```
```cpp
void compose();
```