# src/client/mapview.h

```cpp
public:
    MapView();
```
```cpp
void drawMapBackground(const Rect& rect, const TilePtr& crosshairTile = nullptr);
```
```cpp
void drawMapForeground(const Rect& rect);
```
```cpp
private:
    void drawFloor(short floor, const Position& cameraPosition, const TilePtr& crosshairTile = nullptr);
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
void requestVisibleTilesCacheUpdate() { m_mustUpdateVisibleTilesCache = true; } protected: void onTileUpdate(const Position& pos);
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
int getLockedFirstVisibleFloor() { return m_lockedFirstVisibleFloor; } void setMultifloor(bool enable) { m_multifloor = enable; requestVisibleTilesCacheUpdate();
```
```cpp
bool isMultifloor() { return m_multifloor; } // map dimension related void setVisibleDimension(const Size& visibleDimension);
```
```cpp
void optimizeForSize(const Size & visibleSize);
```
```cpp
Size getVisibleDimension() { return m_visibleDimension; } Point getVisibleCenterOffset() { return m_visibleCenterOffset; } int getCachedFirstVisibleFloor() { return m_cachedFirstVisibleFloor; } int getCachedLastVisibleFloor() { return m_cachedLastVisibleFloor; } // camera related void followCreature(const CreaturePtr& creature);
```
```cpp
CreaturePtr getFollowingCreature() { return m_followingCreature; } bool isFollowingCreature() { return m_followingCreature && m_follow; } void setCameraPosition(const Position& pos);
```
```cpp
Position getCameraPosition();
```
```cpp
void setMinimumAmbientLight(float intensity) { m_minimumAmbientLight = intensity; } float getMinimumAmbientLight() { return m_minimumAmbientLight; } // drawing related void setDrawFlags(Otc::DrawFlags drawFlags) { m_drawFlags = drawFlags; requestVisibleTilesCacheUpdate();
```
```cpp
Otc::DrawFlags getDrawFlags() { return m_drawFlags; } void setDrawTexts(bool enable) { m_drawTexts = enable; } bool isDrawingTexts() { return m_drawTexts; } void setDrawNames(bool enable) { m_drawNames = enable; } bool isDrawingNames() { return m_drawNames; } void setDrawHealthBars(bool enable) { m_drawHealthBars = enable; } bool isDrawingHealthBars() { return m_drawHealthBars; } void setDrawHealthBarsOnTop(bool enable) { m_drawHealthBarsOnTop = enable; } bool isDrawingHealthBarsOnTop() { return m_drawHealthBarsOnTop; } void setDrawLights(bool enable);
```
```cpp
bool isDrawingLights() { return m_drawLight; } void setDrawManaBar(bool enable) { m_drawManaBar = enable; } bool isDrawingManaBar() { return m_drawManaBar; } void setDrawPlayerBars(bool enable) { m_drawPlayerBars = enable; } void move(int x, int y);
```
```cpp
void setAnimated(bool animated) { m_animated = animated; requestVisibleTilesCacheUpdate();
```
```cpp
bool isAnimating() { return m_animated; } void setFloorFading(int value) { m_floorFading = value; } void setCrosshair(const std::string& file);
```
```cpp
Position getPosition(const Point& point, const Size& mapSize);
```
```cpp
Point getPositionOffset(const Point& point, const Size& mapSize);
```
```cpp
MapViewPtr asMapView() { return static_self_cast<MapView>();
```
```cpp
private:
    Rect calcFramebufferSource(const Size& destSize, bool inNextFrame = false);
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