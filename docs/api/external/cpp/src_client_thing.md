---
title: "src/client/thing.h"
source_file: "src/client/thing.h"
generated_at: "2025-11-01T06:09:06.170Z"
doc_type: "cpp_api"
---

# src/client/thing.h

(thing)=
## `Thing`

**Signature:**
```cpp
public: Thing();
```

---

(setposition)=
## `setPosition`

**Signature:**
```cpp
void setPosition(const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |

---

(getstackpriority)=
## `getStackPriority`

**Signature:**
```cpp
int getStackPriority();
```

**Returns:**
- `int`

---

(gettile)=
## `getTile`

**Signature:**
```cpp
virtual const TilePtr& getTile();
```

**Returns:**
- `const TilePtr&`

---

(getparentcontainer)=
## `getParentContainer`

**Signature:**
```cpp
ContainerPtr getParentContainer();
```

**Returns:**
- `ContainerPtr`

---

(getstackpos)=
## `getStackPos`

**Signature:**
```cpp
int getStackPos();
```

**Returns:**
- `int`

---

(updatedmarkedcolor)=
## `updatedMarkedColor`

**Signature:**
```cpp
Color updatedMarkedColor();
```

**Returns:**
- `Color`

---

(getthingtype)=
## `getThingType`

**Signature:**
```cpp
virtual const ThingTypePtr& getThingType();
```

**Returns:**
- `const ThingTypePtr&`

---

(draw)=
## `draw`

**Signature:**
```cpp
virtual void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `bool` | `animate` | `true` | - |
| `LightView*` | `lightView` | `nullptr` | - |

---

(setid)=
## `setId`

**Signature:**
```cpp
virtual void setId(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

---

(getid)=
## `getId`

**Signature:**
```cpp
virtual uint32 getId();
```

**Returns:**
- `uint32`

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
Position getPosition();
```

**Returns:**
- `Position`

---

(setmarked)=
## `setMarked`

**Signature:**
```cpp
void setMarked(const std::string& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `color` | - |

---

(isitem)=
## `isItem`

**Signature:**
```cpp
virtual bool isItem();
```

**Returns:**
- `bool`

---

(iseffect)=
## `isEffect`

**Signature:**
```cpp
virtual bool isEffect();
```

**Returns:**
- `bool`

---

(ismissile)=
## `isMissile`

**Signature:**
```cpp
virtual bool isMissile();
```

**Returns:**
- `bool`

---

(iscreature)=
## `isCreature`

**Signature:**
```cpp
virtual bool isCreature();
```

**Returns:**
- `bool`

---

(isnpc)=
## `isNpc`

**Signature:**
```cpp
virtual bool isNpc();
```

**Returns:**
- `bool`

---

(ismonster)=
## `isMonster`

**Signature:**
```cpp
virtual bool isMonster();
```

**Returns:**
- `bool`

---

(isplayer)=
## `isPlayer`

**Signature:**
```cpp
virtual bool isPlayer();
```

**Returns:**
- `bool`

---

(islocalplayer)=
## `isLocalPlayer`

**Signature:**
```cpp
virtual bool isLocalPlayer();
```

**Returns:**
- `bool`

---

(isanimatedtext)=
## `isAnimatedText`

**Signature:**
```cpp
virtual bool isAnimatedText();
```

**Returns:**
- `bool`

---

(isstatictext)=
## `isStaticText`

**Signature:**
```cpp
virtual bool isStaticText();
```

**Returns:**
- `bool`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
Size getSize();
```

**Returns:**
- `Size`

---

(getwidth)=
## `getWidth`

**Signature:**
```cpp
int getWidth();
```

**Returns:**
- `int`

---

(getheight)=
## `getHeight`

**Signature:**
```cpp
int getHeight();
```

**Returns:**
- `int`

---

(getdisplacement)=
## `getDisplacement`

**Signature:**
```cpp
virtual Point getDisplacement();
```

**Returns:**
- `Point`

---

(getdisplacementx)=
## `getDisplacementX`

**Signature:**
```cpp
virtual int getDisplacementX();
```

**Returns:**
- `int`

---

(getdisplacementy)=
## `getDisplacementY`

**Signature:**
```cpp
virtual int getDisplacementY();
```

**Returns:**
- `int`

---

(getexactsize)=
## `getExactSize`

**Signature:**
```cpp
virtual int getExactSize(int layer, int xPattern, int yPattern, int zPattern, int animationPhase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `layer` | - |
| `int` | `xPattern` | - |
| `int` | `yPattern` | - |
| `int` | `zPattern` | - |
| `int` | `animationPhase` | - |

**Returns:**
- `int`

---

(getlayers)=
## `getLayers`

**Signature:**
```cpp
int getLayers();
```

**Returns:**
- `int`

---

(getnumpatternx)=
## `getNumPatternX`

**Signature:**
```cpp
int getNumPatternX();
```

**Returns:**
- `int`

---

(getnumpatterny)=
## `getNumPatternY`

**Signature:**
```cpp
int getNumPatternY();
```

**Returns:**
- `int`

---

(getnumpatternz)=
## `getNumPatternZ`

**Signature:**
```cpp
int getNumPatternZ();
```

**Returns:**
- `int`

---

(getanimationphases)=
## `getAnimationPhases`

**Signature:**
```cpp
int getAnimationPhases();
```

**Returns:**
- `int`

---

(getanimator)=
## `getAnimator`

**Signature:**
```cpp
AnimatorPtr getAnimator();
```

**Returns:**
- `AnimatorPtr`

---

(getidleanimator)=
## `getIdleAnimator`

**Signature:**
```cpp
AnimatorPtr getIdleAnimator();
```

**Returns:**
- `AnimatorPtr`

---

(getgroundspeed)=
## `getGroundSpeed`

**Signature:**
```cpp
int getGroundSpeed();
```

**Returns:**
- `int`

---

(getmaxtextlength)=
## `getMaxTextLength`

**Signature:**
```cpp
int getMaxTextLength();
```

**Returns:**
- `int`

---

(getlight)=
## `getLight`

**Signature:**
```cpp
Light getLight();
```

**Returns:**
- `Light`

---

(getminimapcolor)=
## `getMinimapColor`

**Signature:**
```cpp
int getMinimapColor();
```

**Returns:**
- `int`

---

(getlenshelp)=
## `getLensHelp`

**Signature:**
```cpp
int getLensHelp();
```

**Returns:**
- `int`

---

(getclothslot)=
## `getClothSlot`

**Signature:**
```cpp
int getClothSlot();
```

**Returns:**
- `int`

---

(getelevation)=
## `getElevation`

**Signature:**
```cpp
int getElevation();
```

**Returns:**
- `int`

---

(isground)=
## `isGround`

**Signature:**
```cpp
bool isGround();
```

**Returns:**
- `bool`

---

(isgroundborder)=
## `isGroundBorder`

**Signature:**
```cpp
bool isGroundBorder();
```

**Returns:**
- `bool`

---

(isonbottom)=
## `isOnBottom`

**Signature:**
```cpp
bool isOnBottom();
```

**Returns:**
- `bool`

---

(isontop)=
## `isOnTop`

**Signature:**
```cpp
bool isOnTop();
```

**Returns:**
- `bool`

---

(iscontainer)=
## `isContainer`

**Signature:**
```cpp
bool isContainer();
```

**Returns:**
- `bool`

---

(isstackable)=
## `isStackable`

**Signature:**
```cpp
bool isStackable();
```

**Returns:**
- `bool`

---

(isforceuse)=
## `isForceUse`

**Signature:**
```cpp
bool isForceUse();
```

**Returns:**
- `bool`

---

(ismultiuse)=
## `isMultiUse`

**Signature:**
```cpp
bool isMultiUse();
```

**Returns:**
- `bool`

---

(iswritable)=
## `isWritable`

**Signature:**
```cpp
bool isWritable();
```

**Returns:**
- `bool`

---

(ischargeable)=
## `isChargeable`

**Signature:**
```cpp
bool isChargeable();
```

**Returns:**
- `bool`

---

(iswritableonce)=
## `isWritableOnce`

**Signature:**
```cpp
bool isWritableOnce();
```

**Returns:**
- `bool`

---

(isfluidcontainer)=
## `isFluidContainer`

**Signature:**
```cpp
bool isFluidContainer();
```

**Returns:**
- `bool`

---

(issplash)=
## `isSplash`

**Signature:**
```cpp
bool isSplash();
```

**Returns:**
- `bool`

---

(isnotwalkable)=
## `isNotWalkable`

**Signature:**
```cpp
bool isNotWalkable();
```

**Returns:**
- `bool`

---

(isnotmoveable)=
## `isNotMoveable`

**Signature:**
```cpp
bool isNotMoveable();
```

**Returns:**
- `bool`

---

(blockprojectile)=
## `blockProjectile`

**Signature:**
```cpp
bool blockProjectile();
```

**Returns:**
- `bool`

---

(isnotpathable)=
## `isNotPathable`

**Signature:**
```cpp
bool isNotPathable();
```

**Returns:**
- `bool`

---

(ispickupable)=
## `isPickupable`

**Signature:**
```cpp
bool isPickupable();
```

**Returns:**
- `bool`

---

(ishangable)=
## `isHangable`

**Signature:**
```cpp
bool isHangable();
```

**Returns:**
- `bool`

---

(ishooksouth)=
## `isHookSouth`

**Signature:**
```cpp
bool isHookSouth();
```

**Returns:**
- `bool`

---

(ishookeast)=
## `isHookEast`

**Signature:**
```cpp
bool isHookEast();
```

**Returns:**
- `bool`

---

(isrotateable)=
## `isRotateable`

**Signature:**
```cpp
bool isRotateable();
```

**Returns:**
- `bool`

---

(haslight)=
## `hasLight`

**Signature:**
```cpp
bool hasLight();
```

**Returns:**
- `bool`

---

(isdonthide)=
## `isDontHide`

**Signature:**
```cpp
bool isDontHide();
```

**Returns:**
- `bool`

---

(istranslucent)=
## `isTranslucent`

**Signature:**
```cpp
bool isTranslucent();
```

**Returns:**
- `bool`

---

(hasdisplacement)=
## `hasDisplacement`

**Signature:**
```cpp
bool hasDisplacement();
```

**Returns:**
- `bool`

---

(haselevation)=
## `hasElevation`

**Signature:**
```cpp
bool hasElevation();
```

**Returns:**
- `bool`

---

(islyingcorpse)=
## `isLyingCorpse`

**Signature:**
```cpp
bool isLyingCorpse();
```

**Returns:**
- `bool`

---

(isanimatealways)=
## `isAnimateAlways`

**Signature:**
```cpp
bool isAnimateAlways();
```

**Returns:**
- `bool`

---

(hasminimapcolor)=
## `hasMiniMapColor`

**Signature:**
```cpp
bool hasMiniMapColor();
```

**Returns:**
- `bool`

---

(haslenshelp)=
## `hasLensHelp`

**Signature:**
```cpp
bool hasLensHelp();
```

**Returns:**
- `bool`

---

(isfullground)=
## `isFullGround`

**Signature:**
```cpp
bool isFullGround();
```

**Returns:**
- `bool`

---

(isignorelook)=
## `isIgnoreLook`

**Signature:**
```cpp
bool isIgnoreLook();
```

**Returns:**
- `bool`

---

(iscloth)=
## `isCloth`

**Signature:**
```cpp
bool isCloth();
```

**Returns:**
- `bool`

---

(ismarketable)=
## `isMarketable`

**Signature:**
```cpp
bool isMarketable();
```

**Returns:**
- `bool`

---

(isusable)=
## `isUsable`

**Signature:**
```cpp
bool isUsable();
```

**Returns:**
- `bool`

---

(iswrapable)=
## `isWrapable`

**Signature:**
```cpp
bool isWrapable();
```

**Returns:**
- `bool`

---

(isunwrapable)=
## `isUnwrapable`

**Signature:**
```cpp
bool isUnwrapable();
```

**Returns:**
- `bool`

---

(istopeffect)=
## `isTopEffect`

**Signature:**
```cpp
bool isTopEffect();
```

**Returns:**
- `bool`

---

(getmarketdata)=
## `getMarketData`

**Signature:**
```cpp
MarketData getMarketData();
```

**Returns:**
- `MarketData`

---

(hide)=
## `hide`

**Signature:**
```cpp
void hide();
```

---

(show)=
## `show`

**Signature:**
```cpp
void show();
```

---

(sethidden)=
## `setHidden`

**Signature:**
```cpp
void setHidden(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(ishidden)=
## `isHidden`

**Signature:**
```cpp
bool isHidden();
```

**Returns:**
- `bool`

---

(onpositionchange)=
## `onPositionChange`

**Signature:**
```cpp
virtual void onPositionChange(const Position& newPos, const Position& oldPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `newPos` | - |
| `const Position&` | `oldPos` | - |

---

(onappear)=
## `onAppear`

**Signature:**
```cpp
virtual void onAppear();
```

---

(ondisappear)=
## `onDisappear`

**Signature:**
```cpp
virtual void onDisappear();
```

---
