# src/client/uiminimap.h

```cpp
public: UIMinimap();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
bool setZoom(int zoom);
```
```cpp
void setCameraPosition(const Position& pos);
```
```cpp
bool floorUp();
```
```cpp
bool floorDown();
```
```cpp
Point getTilePoint(const Position& pos);
```
```cpp
Rect getTileRect(const Position& pos);
```
```cpp
Position getTilePosition(const Point& mousePos);
```
```cpp
void anchorPosition(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge);
```
```cpp
void fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
void centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
protected: virtual void onZoomChange(int zoom, int oldZoom);
```
```cpp
virtual void onCameraPositionChange(const Position& position, const Position& oldPosition);
```
```cpp
virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
private: void update();
```
```cpp
bool zoomIn();
```
```cpp
bool zoomOut();
```
```cpp
void setMinZoom(int minZoom);
```
```cpp
void setMaxZoom(int maxZoom);
```
```cpp
Position getCameraPosition();
```
```cpp
int getMinZoom();
```
```cpp
int getMaxZoom();
```
```cpp
int getZoom();
```
```cpp
float getScale();
```