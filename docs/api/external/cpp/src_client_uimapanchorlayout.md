# src/client/uimapanchorlayout.h

```cpp
int getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget);
```
```cpp
void addPositionAnchor(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge);
```
```cpp
void centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
void fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
public: UIPositionAnchor(Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge) : UIAnchor(anchoredEdge, std::string(), hookedEdge), m_hookedPosition(hookedPosition);
```
```cpp
UIWidgetPtr getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget);
```
```cpp
public: UIMapAnchorLayout(UIWidgetPtr parentWidget) : UIAnchorLayout(parentWidget);
```