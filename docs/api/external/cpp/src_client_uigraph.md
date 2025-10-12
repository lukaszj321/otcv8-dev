# src/client/uigraph.h

```cpp
public:
    UIGraph();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void clear();
```
```cpp
void addValue(int value, bool ignoreSmallValues = false);
```
```cpp
void setLineWidth(int width) { m_width = width; } void setCapacity(int capacity) { m_capacity = capacity; } void setTitle(const std::string& title) { m_title = title; } void setShowLabels(bool value) { m_showLabes = value; } protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```