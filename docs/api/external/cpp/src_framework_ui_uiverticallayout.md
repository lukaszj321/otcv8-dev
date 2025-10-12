# src/framework/ui/uiverticallayout.h

```cpp
public:
    UIVerticalLayout(UIWidgetPtr parentWidget) : UIBoxLayout(parentWidget) { } void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
void setAlignBottom(bool aliginBottom) { m_alignBottom = aliginBottom; update();
```
```cpp
bool isAlignBottom() { return m_alignBottom; } bool isUIVerticalLayout() { return true; } protected: bool internalUpdate();
```