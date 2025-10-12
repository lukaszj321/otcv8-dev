# src/framework/ui/uilayout.h

```cpp
public:
    UILayout(UIWidgetPtr parentWidget) : m_parentWidget(parentWidget) { m_updateDisabled = 0; } void update();
```
```cpp
void updateLater();
```
```cpp
virtual void applyStyle(const OTMLNodePtr& styleNode) { } virtual void addWidget(const UIWidgetPtr& widget) { } virtual void removeWidget(const UIWidgetPtr& widget) { } void disableUpdates() { m_updateDisabled++; } void enableUpdates() { m_updateDisabled = std::max<int>(m_updateDisabled-1,0);
```