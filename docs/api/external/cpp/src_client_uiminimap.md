# src/client/uiminimap.h

```cpp
public:
    UIMinimap();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
bool zoomIn() { return setZoom(m_zoom+1);
```
```cpp
bool zoomOut() { return setZoom(m_zoom-1);
```
```cpp
bool setZoom(int zoom);
```
```cpp
void setMinZoom(int minZoom) { m_minZoom = minZoom; } void setMaxZoom(int maxZoom) { m_maxZoom = maxZoom; } void setCameraPosition(const Position& pos);
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
Position getCameraPosition() { return m_cameraPosition; } int getMinZoom() { return m_minZoom; } int getMaxZoom() { return m_maxZoom; } int getZoom() { return m_zoom; } float getScale() { return m_scale; } void anchorPosition(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge);
```
```cpp
void fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
void centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```
```cpp
protected:
    virtual void onZoomChange(int zoom, int oldZoom);
```
```cpp
virtual void onCameraPositionChange(const Position& position, const Position& oldPosition);
```
```cpp
virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
private:
    void update();
```