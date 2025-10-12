# src/client/uiprogressrect.h

```cpp
public:
    UIProgressRect();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setPercent(float percent);
```
```cpp
float getPercent() { return m_percent; } protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```