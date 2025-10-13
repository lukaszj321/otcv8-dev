# src/client/mapview.h

```cpp
public: MapView();
```
```cpp
void drawMapBackground(const Rect& rect, const TilePtr& crosshairTile = nullptr);
```
```cpp
void drawMapForeground(const Rect& rect);
```
```cpp
private: void drawFloor(short floor, const Position& cameraPosition, const TilePtr& crosshairTile = nullptr);
```
```cpp
void drawTileTexts(const Rect& rect, const Rect& srcRect);
```
```cpp
void drawTileWidget(const Rect& rect, const Rect& srcRect);
```
```cpp
void updateGeometry(const Size& visibleDimension, const Size& optimizedSize);
```
```cpp
void updateVisibleTilesCache();
```
```cpp
protected: void onTileUpdate(const Position& pos);
```
```cpp
void onMapCenterChange(const Position& pos);
```
```cpp
void lockFirstVisibleFloor(int firstVisibleFloor);
```
```cpp
void unlockFirstVisibleFloor();
```
```cpp
void setVisibleDimension(const Size& visibleDimension);
```
```cpp
void optimizeForSize(const Size & visibleSize);
```
```cpp
void followCreature(const CreaturePtr& creature);
```
```cpp
void setCameraPosition(const Position& pos);
```
```cpp
Position getCameraPosition();
```
```cpp
void setDrawLights(bool enable);
```
```cpp
void move(int x, int y);
```
```cpp
void setCrosshair(const std::string& file);
```
```cpp
Position getPosition(const Point& point, const Size& mapSize);
```
```cpp
Point getPositionOffset(const Point& point, const Size& mapSize);
```
```cpp
private: Rect calcFramebufferSource(const Size& destSize, bool inNextFrame = false);
```
```cpp
int calcFirstVisibleFloor(bool forFading = false);
```
```cpp
int calcLastVisibleFloor();
```
```cpp
Point transformPositionTo2D(const Position& position, const Position& relativePosition);
```
```cpp
void requestVisibleTilesCacheUpdate();
```
```cpp
int getLockedFirstVisibleFloor();
```
```cpp
void setMultifloor(bool enable);
```
```cpp
bool isMultifloor();
```
```cpp
Size getVisibleDimension();
```
```cpp
Point getVisibleCenterOffset();
```
```cpp
int getCachedFirstVisibleFloor();
```
```cpp
int getCachedLastVisibleFloor();
```
```cpp
CreaturePtr getFollowingCreature();
```
```cpp
bool isFollowingCreature();
```
```cpp
void setMinimumAmbientLight(float intensity);
```
```cpp
float getMinimumAmbientLight();
```
```cpp
void setDrawFlags(Otc::DrawFlags drawFlags);
```
```cpp
Otc::DrawFlags getDrawFlags();
```
```cpp
void setDrawTexts(bool enable);
```
```cpp
bool isDrawingTexts();
```
```cpp
void setDrawNames(bool enable);
```
```cpp
bool isDrawingNames();
```
```cpp
void setDrawHealthBars(bool enable);
```
```cpp
bool isDrawingHealthBars();
```
```cpp
void setDrawHealthBarsOnTop(bool enable);
```
```cpp
bool isDrawingHealthBarsOnTop();
```
```cpp
bool isDrawingLights();
```
```cpp
void setDrawManaBar(bool enable);
```
```cpp
bool isDrawingManaBar();
```
```cpp
void setDrawPlayerBars(bool enable);
```
```cpp
void setAnimated(bool animated);
```
```cpp
bool isAnimating();
```
```cpp
void setFloorFading(int value);
```
```cpp
MapViewPtr asMapView();
```