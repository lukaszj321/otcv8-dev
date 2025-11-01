---
title: "src/client/mapview.h"
source_file: "src/client/mapview.h"
generated_at: "2025-11-01T04:06:42.724Z"
doc_type: "cpp_api"
---

# src/client/mapview.h

(mapview)=
## `MapView`

**Signature:**
```cpp
public: MapView();
```

---

(drawmapbackground)=
## `drawMapBackground`

**Signature:**
```cpp
void drawMapBackground(const Rect& rect, const TilePtr& crosshairTile = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `rect` |  | - |
| `const TilePtr&` | `crosshairTile` | `nullptr` | - |

---

(drawmapforeground)=
## `drawMapForeground`

**Signature:**
```cpp
void drawMapForeground(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(drawfloor)=
## `drawFloor`

**Signature:**
```cpp
private: void drawFloor(short floor, const Position& cameraPosition, const TilePtr& crosshairTile = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `short` | `floor` |  | - |
| `const Position&` | `cameraPosition` |  | - |
| `const TilePtr&` | `crosshairTile` | `nullptr` | - |

---

(drawtiletexts)=
## `drawTileTexts`

**Signature:**
```cpp
void drawTileTexts(const Rect& rect, const Rect& srcRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |
| `const Rect&` | `srcRect` | - |

---

(drawtilewidget)=
## `drawTileWidget`

**Signature:**
```cpp
void drawTileWidget(const Rect& rect, const Rect& srcRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |
| `const Rect&` | `srcRect` | - |

---

(updategeometry)=
## `updateGeometry`

**Signature:**
```cpp
void updateGeometry(const Size& visibleDimension, const Size& optimizedSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `visibleDimension` | - |
| `const Size&` | `optimizedSize` | - |

---

(updatevisibletilescache)=
## `updateVisibleTilesCache`

**Signature:**
```cpp
void updateVisibleTilesCache();
```

---

(ontileupdate)=
## `onTileUpdate`

**Signature:**
```cpp
protected: void onTileUpdate(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(onmapcenterchange)=
## `onMapCenterChange`

**Signature:**
```cpp
void onMapCenterChange(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(lockfirstvisiblefloor)=
## `lockFirstVisibleFloor`

**Signature:**
```cpp
void lockFirstVisibleFloor(int firstVisibleFloor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `firstVisibleFloor` | - |

---

(unlockfirstvisiblefloor)=
## `unlockFirstVisibleFloor`

**Signature:**
```cpp
void unlockFirstVisibleFloor();
```

---

(setvisibledimension)=
## `setVisibleDimension`

**Signature:**
```cpp
void setVisibleDimension(const Size& visibleDimension);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `visibleDimension` | - |

---

(optimizeforsize)=
## `optimizeForSize`

**Signature:**
```cpp
void optimizeForSize(const Size & visibleSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size &` | `visibleSize` | - |

---

(followcreature)=
## `followCreature`

**Signature:**
```cpp
void followCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(setcameraposition)=
## `setCameraPosition`

**Signature:**
```cpp
void setCameraPosition(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(getcameraposition)=
## `getCameraPosition`

**Signature:**
```cpp
Position getCameraPosition();
```

**Returns:**
- `Position`

---

(setdrawlights)=
## `setDrawLights`

**Signature:**
```cpp
void setDrawLights(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(move)=
## `move`

**Signature:**
```cpp
void move(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(setcrosshair)=
## `setCrosshair`

**Signature:**
```cpp
void setCrosshair(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
Position getPosition(const Point& point, const Size& mapSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |
| `const Size&` | `mapSize` | - |

**Returns:**
- `Position`

---

(getpositionoffset)=
## `getPositionOffset`

**Signature:**
```cpp
Point getPositionOffset(const Point& point, const Size& mapSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |
| `const Size&` | `mapSize` | - |

**Returns:**
- `Point`

---

(calcframebuffersource)=
## `calcFramebufferSource`

**Signature:**
```cpp
private: Rect calcFramebufferSource(const Size& destSize, bool inNextFrame = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Size&` | `destSize` |  | - |
| `bool` | `inNextFrame` | `false` | - |

**Returns:**
- `Rect`

---

(calcfirstvisiblefloor)=
## `calcFirstVisibleFloor`

**Signature:**
```cpp
int calcFirstVisibleFloor(bool forFading = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `forFading` | `false` | - |

**Returns:**
- `int`

---

(calclastvisiblefloor)=
## `calcLastVisibleFloor`

**Signature:**
```cpp
int calcLastVisibleFloor();
```

**Returns:**
- `int`

---

(transformpositionto2d)=
## `transformPositionTo2D`

**Signature:**
```cpp
Point transformPositionTo2D(const Position& position, const Position& relativePosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |
| `const Position&` | `relativePosition` | - |

**Returns:**
- `Point`

---

(requestvisibletilescacheupdate)=
## `requestVisibleTilesCacheUpdate`

**Signature:**
```cpp
void requestVisibleTilesCacheUpdate();
```

---

(getlockedfirstvisiblefloor)=
## `getLockedFirstVisibleFloor`

**Signature:**
```cpp
int getLockedFirstVisibleFloor();
```

**Returns:**
- `int`

---

(setmultifloor)=
## `setMultifloor`

**Signature:**
```cpp
void setMultifloor(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(ismultifloor)=
## `isMultifloor`

**Signature:**
```cpp
bool isMultifloor();
```

**Returns:**
- `bool`

---

(getvisibledimension)=
## `getVisibleDimension`

**Signature:**
```cpp
Size getVisibleDimension();
```

**Returns:**
- `Size`

---

(getvisiblecenteroffset)=
## `getVisibleCenterOffset`

**Signature:**
```cpp
Point getVisibleCenterOffset();
```

**Returns:**
- `Point`

---

(getcachedfirstvisiblefloor)=
## `getCachedFirstVisibleFloor`

**Signature:**
```cpp
int getCachedFirstVisibleFloor();
```

**Returns:**
- `int`

---

(getcachedlastvisiblefloor)=
## `getCachedLastVisibleFloor`

**Signature:**
```cpp
int getCachedLastVisibleFloor();
```

**Returns:**
- `int`

---

(getfollowingcreature)=
## `getFollowingCreature`

**Signature:**
```cpp
CreaturePtr getFollowingCreature();
```

**Returns:**
- `CreaturePtr`

---

(isfollowingcreature)=
## `isFollowingCreature`

**Signature:**
```cpp
bool isFollowingCreature();
```

**Returns:**
- `bool`

---

(setminimumambientlight)=
## `setMinimumAmbientLight`

**Signature:**
```cpp
void setMinimumAmbientLight(float intensity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `intensity` | - |

---

(getminimumambientlight)=
## `getMinimumAmbientLight`

**Signature:**
```cpp
float getMinimumAmbientLight();
```

**Returns:**
- `float`

---

(setdrawflags)=
## `setDrawFlags`

**Signature:**
```cpp
void setDrawFlags(Otc::DrawFlags drawFlags);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::DrawFlags` | `drawFlags` | - |

---

(getdrawflags)=
## `getDrawFlags`

**Signature:**
```cpp
Otc::DrawFlags getDrawFlags();
```

**Returns:**
- `Otc::DrawFlags`

---

(setdrawtexts)=
## `setDrawTexts`

**Signature:**
```cpp
void setDrawTexts(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(isdrawingtexts)=
## `isDrawingTexts`

**Signature:**
```cpp
bool isDrawingTexts();
```

**Returns:**
- `bool`

---

(setdrawnames)=
## `setDrawNames`

**Signature:**
```cpp
void setDrawNames(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(isdrawingnames)=
## `isDrawingNames`

**Signature:**
```cpp
bool isDrawingNames();
```

**Returns:**
- `bool`

---

(setdrawhealthbars)=
## `setDrawHealthBars`

**Signature:**
```cpp
void setDrawHealthBars(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(isdrawinghealthbars)=
## `isDrawingHealthBars`

**Signature:**
```cpp
bool isDrawingHealthBars();
```

**Returns:**
- `bool`

---

(setdrawhealthbarsontop)=
## `setDrawHealthBarsOnTop`

**Signature:**
```cpp
void setDrawHealthBarsOnTop(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(isdrawinghealthbarsontop)=
## `isDrawingHealthBarsOnTop`

**Signature:**
```cpp
bool isDrawingHealthBarsOnTop();
```

**Returns:**
- `bool`

---

(isdrawinglights)=
## `isDrawingLights`

**Signature:**
```cpp
bool isDrawingLights();
```

**Returns:**
- `bool`

---

(setdrawmanabar)=
## `setDrawManaBar`

**Signature:**
```cpp
void setDrawManaBar(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(isdrawingmanabar)=
## `isDrawingManaBar`

**Signature:**
```cpp
bool isDrawingManaBar();
```

**Returns:**
- `bool`

---

(setdrawplayerbars)=
## `setDrawPlayerBars`

**Signature:**
```cpp
void setDrawPlayerBars(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setanimated)=
## `setAnimated`

**Signature:**
```cpp
void setAnimated(bool animated);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `animated` | - |

---

(isanimating)=
## `isAnimating`

**Signature:**
```cpp
bool isAnimating();
```

**Returns:**
- `bool`

---

(setfloorfading)=
## `setFloorFading`

**Signature:**
```cpp
void setFloorFading(int value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `value` | - |

---

(asmapview)=
## `asMapView`

**Signature:**
```cpp
MapViewPtr asMapView();
```

**Returns:**
- `MapViewPtr`

---
