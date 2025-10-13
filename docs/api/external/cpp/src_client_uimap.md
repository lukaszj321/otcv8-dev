# src/client/uimap.h

```cpp
public: UIMap();
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
void setVisibleDimension(const Size& visibleDimension);
```
```cpp
void setKeepAspectRatio(bool enable);
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
protected: virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```
```cpp
private: void updateVisibleDimension();
```
```cpp
void updateMapSize();
```
```cpp
void followCreature(const CreaturePtr& creature);
```
```cpp
void setCameraPosition(const Position& pos);
```
```cpp
void setMaxZoomIn(int maxZoomIn);
```
```cpp
void setMaxZoomOut(int maxZoomOut);
```
```cpp
void setMultifloor(bool enable);
```
```cpp
void lockVisibleFloor(int floor);
```
```cpp
void unlockVisibleFloor();
```
```cpp
void setDrawFlags(Otc::DrawFlags drawFlags);
```
```cpp
void setDrawTexts(bool enable);
```
```cpp
void setDrawNames(bool enable);
```
```cpp
void setDrawHealthBars(bool enable);
```
```cpp
void setDrawHealthBarsOnTop(bool enable);
```
```cpp
void setDrawLights(bool enable);
```
```cpp
void setDrawManaBar(bool enable);
```
```cpp
void setDrawPlayerBars(bool enable);
```
```cpp
void setAnimated(bool enable);
```
```cpp
void setMinimumAmbientLight(float intensity);
```
```cpp
void setLimitVisibleRange(bool limitVisibleRange);
```
```cpp
void setFloorFading(int value);
```
```cpp
void setCrosshair(const std::string& type);
```
```cpp
bool isMultifloor();
```
```cpp
bool isDrawingTexts();
```
```cpp
bool isDrawingNames();
```
```cpp
bool isDrawingHealthBars();
```
```cpp
bool isDrawingHealthBarsOnTop();
```
```cpp
bool isDrawingLights();
```
```cpp
bool isDrawingManaBar();
```
```cpp
bool isAnimating();
```
```cpp
bool isKeepAspectRatioEnabled();
```
```cpp
bool isLimitVisibleRangeEnabled();
```
```cpp
Size getVisibleDimension();
```
```cpp
CreaturePtr getFollowingCreature();
```
```cpp
Otc::DrawFlags getDrawFlags();
```
```cpp
Position getCameraPosition();
```
```cpp
int getMaxZoomIn();
```
```cpp
int getMaxZoomOut();
```
```cpp
int getZoom();
```
```cpp
float getMinimumAmbientLight();
```
```cpp
void setShader(const std::string& shader);
```
```cpp
std::string getShader();
```