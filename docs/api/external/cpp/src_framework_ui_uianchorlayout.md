# src/framework/ui/uianchorlayout.h

```cpp
virtual UIWidgetPtr getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget);
```
```cpp
virtual int getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget);
```
```cpp
void addAnchor(const UIAnchorPtr& anchor);
```
```cpp
void addAnchor(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge);
```
```cpp
void removeAnchors(const UIWidgetPtr& anchoredWidget);
```
```cpp
bool hasAnchors(const UIWidgetPtr& anchoredWidget);
```
```cpp
void centerIn(const UIWidgetPtr& anchoredWidget, const std::string& hookedWidgetId);
```
```cpp
void fill(const UIWidgetPtr& anchoredWidget, const std::string& hookedWidgetId);
```
```cpp
void addWidget(const UIWidgetPtr& widget);
```
```cpp
void removeWidget(const UIWidgetPtr& widget);
```
```cpp
protected: virtual bool internalUpdate();
```
```cpp
virtual bool updateWidget(const UIWidgetPtr& widget, const UIAnchorGroupPtr& anchorGroup, UIWidgetPtr first = nullptr);
```
```cpp
public: UIAnchor(Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge) : m_anchoredEdge(anchoredEdge), m_hookedEdge(hookedEdge), m_hookedWidgetId(hookedWidgetId);
```
```cpp
Fw::AnchorEdge getAnchoredEdge();
```
```cpp
Fw::AnchorEdge getHookedEdge();
```
```cpp
public: UIAnchorGroup() : m_updated(true);
```
```cpp
const UIAnchorList& getAnchors();
```
```cpp
bool isUpdated();
```
```cpp
void setUpdated(bool updated);
```
```cpp
public: UIAnchorLayout(UIWidgetPtr parentWidget) : UILayout(parentWidget);
```
```cpp
bool isUIAnchorLayout();
```