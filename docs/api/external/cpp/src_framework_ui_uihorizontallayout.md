# src/framework/ui/uihorizontallayout.h

```cpp
public:
    UIHorizontalLayout(UIWidgetPtr parentWidget) : UIBoxLayout(parentWidget) { } void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
void setAlignRight(bool aliginRight) { m_alignRight = aliginRight; update();
```
```cpp
bool isUIHorizontalLayout() { return true; } protected: bool internalUpdate();
```