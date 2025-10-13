# src/framework/ui/uilayout.h

```cpp
void update();
```
```cpp
void updateLater();
```
```cpp
public: UILayout(UIWidgetPtr parentWidget) : m_parentWidget(parentWidget);
```
```cpp
virtual void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
virtual void addWidget(const UIWidgetPtr& widget);
```
```cpp
virtual void removeWidget(const UIWidgetPtr& widget);
```
```cpp
void disableUpdates();
```
```cpp
void enableUpdates();
```
```cpp
void setParent(UIWidgetPtr parentWidget);
```
```cpp
UIWidgetPtr getParentWidget();
```
```cpp
bool isUpdateDisabled();
```
```cpp
bool isUpdating();
```
```cpp
virtual bool isUIAnchorLayout();
```
```cpp
virtual bool isUIBoxLayout();
```
```cpp
virtual bool isUIHorizontalLayout();
```
```cpp
virtual bool isUIVerticalLayout();
```
```cpp
virtual bool isUIGridLayout();
```
```cpp
protected: virtual bool internalUpdate();
```