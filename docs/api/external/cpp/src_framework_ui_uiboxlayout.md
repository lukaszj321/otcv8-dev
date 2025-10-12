# src/framework/ui/uiboxlayout.h

```cpp
public:
    UIBoxLayout(UIWidgetPtr parentWidget);
```
```cpp
void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
void addWidget(const UIWidgetPtr& widget) { update();
```
```cpp
void removeWidget(const UIWidgetPtr& widget) { update();
```
```cpp
void setSpacing(int spacing) { m_spacing = spacing; update();
```
```cpp
void setFitChildren(bool fitParent) { m_fitChildren = fitParent; update();
```