---
title: "src/client/uimap.h"
source_file: "src/client/uimap.h"
generated_at: "2025-11-01T05:32:59.270Z"
doc_type: "cpp_api"
---

# src/client/uimap.h

(uimap)=
## `UIMap`

**Signature:**
```cpp
public: UIMap();
```

---

(onmousemove)=
## `onMouseMove`

**Signature:**
```cpp
bool onMouseMove(const Point& mousePos, const Point& mouseMoved);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |
| `const Point&` | `mouseMoved` | - |

**Returns:**
- `bool`

---

(drawself)=
## `drawSelf`

**Signature:**
```cpp
void drawSelf(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(movepixels)=
## `movePixels`

**Signature:**
```cpp
void movePixels(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(setzoom)=
## `setZoom`

**Signature:**
```cpp
bool setZoom(int zoom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `zoom` | - |

**Returns:**
- `bool`

---

(zoomin)=
## `zoomIn`

**Signature:**
```cpp
bool zoomIn();
```

**Returns:**
- `bool`

---

(zoomout)=
## `zoomOut`

**Signature:**
```cpp
bool zoomOut();
```

**Returns:**
- `bool`

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

(setkeepaspectratio)=
## `setKeepAspectRatio`

**Signature:**
```cpp
void setKeepAspectRatio(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
Position getPosition(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `Position`

---

(getpositionoffset)=
## `getPositionOffset`

**Signature:**
```cpp
Point getPositionOffset(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `Point`

---

(gettile)=
## `getTile`

**Signature:**
```cpp
TilePtr getTile(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `TilePtr`

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
protected: virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const OTMLNodePtr&` | `styleNode` | - |

---

(ongeometrychange)=
## `onGeometryChange`

**Signature:**
```cpp
virtual void onGeometryChange(const Rect& oldRect, const Rect& newRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `oldRect` | - |
| `const Rect&` | `newRect` | - |

---

(updatevisibledimension)=
## `updateVisibleDimension`

**Signature:**
```cpp
private: void updateVisibleDimension();
```

---

(updatemapsize)=
## `updateMapSize`

**Signature:**
```cpp
void updateMapSize();
```

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

(setmaxzoomin)=
## `setMaxZoomIn`

**Signature:**
```cpp
void setMaxZoomIn(int maxZoomIn);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxZoomIn` | - |

---

(setmaxzoomout)=
## `setMaxZoomOut`

**Signature:**
```cpp
void setMaxZoomOut(int maxZoomOut);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxZoomOut` | - |

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

(lockvisiblefloor)=
## `lockVisibleFloor`

**Signature:**
```cpp
void lockVisibleFloor(int floor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `floor` | - |

---

(unlockvisiblefloor)=
## `unlockVisibleFloor`

**Signature:**
```cpp
void unlockVisibleFloor();
```

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
void setAnimated(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

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

(setlimitvisiblerange)=
## `setLimitVisibleRange`

**Signature:**
```cpp
void setLimitVisibleRange(bool limitVisibleRange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `limitVisibleRange` | - |

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

(setcrosshair)=
## `setCrosshair`

**Signature:**
```cpp
void setCrosshair(const std::string& type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `type` | - |

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

(isdrawingtexts)=
## `isDrawingTexts`

**Signature:**
```cpp
bool isDrawingTexts();
```

**Returns:**
- `bool`

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

(isdrawinghealthbars)=
## `isDrawingHealthBars`

**Signature:**
```cpp
bool isDrawingHealthBars();
```

**Returns:**
- `bool`

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

(isdrawingmanabar)=
## `isDrawingManaBar`

**Signature:**
```cpp
bool isDrawingManaBar();
```

**Returns:**
- `bool`

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

(iskeepaspectratioenabled)=
## `isKeepAspectRatioEnabled`

**Signature:**
```cpp
bool isKeepAspectRatioEnabled();
```

**Returns:**
- `bool`

---

(islimitvisiblerangeenabled)=
## `isLimitVisibleRangeEnabled`

**Signature:**
```cpp
bool isLimitVisibleRangeEnabled();
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

(getfollowingcreature)=
## `getFollowingCreature`

**Signature:**
```cpp
CreaturePtr getFollowingCreature();
```

**Returns:**
- `CreaturePtr`

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

(getcameraposition)=
## `getCameraPosition`

**Signature:**
```cpp
Position getCameraPosition();
```

**Returns:**
- `Position`

---

(getmaxzoomin)=
## `getMaxZoomIn`

**Signature:**
```cpp
int getMaxZoomIn();
```

**Returns:**
- `int`

---

(getmaxzoomout)=
## `getMaxZoomOut`

**Signature:**
```cpp
int getMaxZoomOut();
```

**Returns:**
- `int`

---

(getzoom)=
## `getZoom`

**Signature:**
```cpp
int getZoom();
```

**Returns:**
- `int`

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

(setshader)=
## `setShader`

**Signature:**
```cpp
void setShader(const std::string& shader);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `shader` | - |

---

(getshader)=
## `getShader`

**Signature:**
```cpp
std::string getShader();
```

**Returns:**
- `std::string`

---
