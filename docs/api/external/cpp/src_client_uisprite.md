# src/client/uisprite.h

```cpp
public: UISprite();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setSpriteId(uint32 id);
```
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
uint32 getSpriteId();
```
```cpp
void clearSprite();
```
```cpp
void setSpriteColor(Color color);
```
```cpp
bool isSpriteVisible();
```
```cpp
void setSpriteVisible(bool visible);
```
```cpp
bool hasSprite();
```