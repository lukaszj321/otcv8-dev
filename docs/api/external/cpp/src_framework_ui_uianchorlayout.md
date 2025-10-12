# src/framework/ui/uianchorlayout.h

```cpp
public:
    UIAnchor(Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge) : m_anchoredEdge(anchoredEdge), m_hookedEdge(hookedEdge), m_hookedWidgetId(hookedWidgetId) { } Fw::AnchorEdge getAnchoredEdge() const { return m_anchoredEdge; } Fw::AnchorEdge getHookedEdge() const { return m_hookedEdge; } virtual UIWidgetPtr getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget);
```
```cpp
virtual int getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget);
```
```cpp
public:
    UIAnchorGroup() : m_updated(true) { } void addAnchor(const UIAnchorPtr& anchor);
```
```cpp
const UIAnchorList& getAnchors() { return m_anchors; } bool isUpdated() { return m_updated; } void setUpdated(bool updated) { m_updated = updated; } private: UIAnchorList m_anchors; bool m_updated; }; // @bindclass class UIAnchorLayout : public UILayout { public: UIAnchorLayout(UIWidgetPtr parentWidget) : UILayout(parentWidget) { } void addAnchor(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge);
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
bool isUIAnchorLayout() { return true; } protected: virtual bool internalUpdate();
```
```cpp
virtual bool updateWidget(const UIWidgetPtr& widget, const UIAnchorGroupPtr& anchorGroup, UIWidgetPtr first = nullptr);
```