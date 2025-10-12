# src/client/uimap.h

```cpp
public:
    UIMap();
```
```cpp
bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void movePixels(int x, int y);
```
```cpp
bool setZoom(int zoom);
```
```cpp
bool zoomIn();
```
```cpp
bool zoomOut();
```
```cpp
void followCreature(const CreaturePtr& creature) { m_mapView->followCreature(creature);
```
```cpp
void setCameraPosition(const Position& pos) { m_mapView->setCameraPosition(pos);
```
```cpp
void setMaxZoomIn(int maxZoomIn) { m_maxZoomIn = maxZoomIn; } void setMaxZoomOut(int maxZoomOut) { m_maxZoomOut = maxZoomOut; } void setMultifloor(bool enable) { m_mapView->setMultifloor(enable);
```
```cpp
void lockVisibleFloor(int floor) { m_mapView->lockFirstVisibleFloor(floor);
```
```cpp
void unlockVisibleFloor() { m_mapView->unlockFirstVisibleFloor();
```
```cpp
void setVisibleDimension(const Size& visibleDimension);
```
```cpp
void setDrawFlags(Otc::DrawFlags drawFlags) { m_mapView->setDrawFlags(drawFlags);
```
```cpp
void setDrawTexts(bool enable) { m_mapView->setDrawTexts(enable);
```
```cpp
void setDrawNames(bool enable) { m_mapView->setDrawNames(enable);
```
```cpp
void setDrawHealthBars(bool enable) { m_mapView->setDrawHealthBars(enable);
```
```cpp
void setDrawHealthBarsOnTop(bool enable) { m_mapView->setDrawHealthBarsOnTop(enable);
```
```cpp
void setDrawLights(bool enable) { m_mapView->setDrawLights(enable);
```
```cpp
void setDrawManaBar(bool enable) { m_mapView->setDrawManaBar(enable);
```
```cpp
void setDrawPlayerBars(bool enable) { m_mapView->setDrawPlayerBars(enable);
```
```cpp
void setAnimated(bool enable) { m_mapView->setAnimated(enable);
```
```cpp
void setKeepAspectRatio(bool enable);
```
```cpp
void setMinimumAmbientLight(float intensity) { m_mapView->setMinimumAmbientLight(intensity);
```
```cpp
void setLimitVisibleRange(bool limitVisibleRange) { m_limitVisibleRange = limitVisibleRange; updateVisibleDimension();
```
```cpp
void setFloorFading(int value) { m_mapView->setFloorFading(value);
```
```cpp
void setCrosshair(const std::string& type) { m_mapView->setCrosshair(type);
```
```cpp
bool isMultifloor() { return m_mapView->isMultifloor();
```
```cpp
bool isDrawingTexts() { return m_mapView->isDrawingTexts();
```
```cpp
bool isDrawingNames() { return m_mapView->isDrawingNames();
```
```cpp
bool isDrawingHealthBars() { return m_mapView->isDrawingHealthBars();
```
```cpp
bool isDrawingHealthBarsOnTop() { return m_mapView->isDrawingHealthBarsOnTop();
```
```cpp
bool isDrawingLights() { return m_mapView->isDrawingLights();
```
```cpp
bool isDrawingManaBar() { return m_mapView->isDrawingManaBar();
```
```cpp
bool isAnimating() { return m_mapView->isAnimating();
```
```cpp
bool isKeepAspectRatioEnabled() { return m_keepAspectRatio; } bool isLimitVisibleRangeEnabled() { return m_limitVisibleRange; } Size getVisibleDimension() { return m_mapView->getVisibleDimension();
```
```cpp
CreaturePtr getFollowingCreature() { return m_mapView->getFollowingCreature();
```
```cpp
Otc::DrawFlags getDrawFlags() { return m_mapView->getDrawFlags();
```
```cpp
Position getCameraPosition() { return m_mapView->getCameraPosition();
```
```cpp
Position getPosition(const Point& mousePos);
```
```cpp
Point getPositionOffset(const Point& mousePos);
```
```cpp
TilePtr getTile(const Point& mousePos);
```
```cpp
int getMaxZoomIn() { return m_maxZoomIn; } int getMaxZoomOut() { return m_maxZoomOut; } int getZoom() { return m_zoom; } float getMinimumAmbientLight() { return m_mapView->getMinimumAmbientLight();
```
```cpp
void setShader(const std::string& shader) { m_shader = shader; } std::string getShader() { return m_shader; } protected: virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```
```cpp
private:
    void updateVisibleDimension();
```
```cpp
void updateMapSize();
```