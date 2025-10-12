# src/client/uisprite.h

```cpp
public:
    UISprite();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setSpriteId(uint32 id);
```
```cpp
uint32 getSpriteId() { return m_spriteId; } void clearSprite() { setSpriteId(0);
```
```cpp
void setSpriteColor(Color color) { m_spriteColor = color; } bool isSpriteVisible() { return m_spriteVisible; } void setSpriteVisible(bool visible) { m_spriteVisible = visible; } bool hasSprite() { return m_sprite != nullptr; } protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```