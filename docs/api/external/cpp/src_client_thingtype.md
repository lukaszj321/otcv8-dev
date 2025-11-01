---
title: "src/client/thingtype.h"
source_file: "src/client/thingtype.h"
generated_at: "2025-11-01T08:45:15.288Z"
doc_type: "cpp_api"
---

# src/client/thingtype.h

(thingtype)=
## `ThingType`

**Signature:**
```cpp
public: ThingType();
```

---

(unserialize)=
## `unserialize`

**Signature:**
```cpp
void unserialize(uint16 clientId, ThingCategory category, const FileStreamPtr& fin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `clientId` | - |
| `ThingCategory` | `category` | - |
| `const FileStreamPtr&` | `fin` | - |

---

(unserializeotml)=
## `unserializeOtml`

**Signature:**
```cpp
void unserializeOtml(const OTMLNodePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `node` | - |

---

(unload)=
## `unload`

**Signature:**
```cpp
void unload();
```

---

(serialize)=
## `serialize`

**Signature:**
```cpp
void serialize(const FileStreamPtr& fin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fin` | - |

---

(exportimage)=
## `exportImage`

**Signature:**
```cpp
void exportImage(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(replacesprites)=
## `replaceSprites`

**Signature:**
```cpp
void replaceSprites(std::map<uint32_t, ImagePtr>& replacements, std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::map&lt;uint32_t, ImagePtr&gt;&` | `replacements` | - |
| `std::string` | `fileName` | - |

---

(draw)=
## `draw`

**Signature:**
```cpp
DrawQueueItem* draw(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `int` | `layer` |  | - |
| `int` | `xPattern` |  | - |
| `int` | `yPattern` |  | - |
| `int` | `zPattern` |  | - |
| `int` | `animationPhase` |  | - |
| `Color` | `color` | `Color::white` | - |
| `LightView*` | `lightView` | `nullptr` | - |

**Returns:**
- `DrawQueueItem*`

---

(draw-1)=
## `draw`

**Signature:**
```cpp
DrawQueueItem* draw(const Rect& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `int` | `layer` |  | - |
| `int` | `xPattern` |  | - |
| `int` | `yPattern` |  | - |
| `int` | `zPattern` |  | - |
| `int` | `animationPhase` |  | - |
| `Color` | `color` | `Color::white` | - |

**Returns:**
- `DrawQueueItem*`

---

(drawoutfit)=
## `drawOutfit`

**Signature:**
```cpp
std::shared_ptr<DrawOutfitParams> drawOutfit(const Point& dest, int maskLayer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `int` | `maskLayer` |  | - |
| `int` | `xPattern` |  | - |
| `int` | `yPattern` |  | - |
| `int` | `zPattern` |  | - |
| `int` | `animationPhase` |  | - |
| `Color` | `color` | `Color::white` | - |
| `LightView*` | `lightView` | `nullptr` | - |

**Returns:**
- `std::shared_ptr&lt;DrawOutfitParams&gt;`

---

(getdrawsize)=
## `getDrawSize`

**Signature:**
```cpp
Rect getDrawSize(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `int` | `layer` | - |
| `int` | `xPattern` | - |
| `int` | `yPattern` | - |
| `int` | `zPattern` | - |
| `int` | `animationPhase` | - |

**Returns:**
- `Rect`

---

(drawwithshader)=
## `drawWithShader`

**Signature:**
```cpp
void drawWithShader(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `int` | `layer` |  | - |
| `int` | `xPattern` |  | - |
| `int` | `yPattern` |  | - |
| `int` | `zPattern` |  | - |
| `int` | `animationPhase` |  | - |
| `const std::string&` | `shader` |  | - |
| `Color` | `color` | `Color::white` | - |
| `LightView*` | `lightView` | `nullptr` | - |

---

(drawwithshader-1)=
## `drawWithShader`

**Signature:**
```cpp
void drawWithShader(const Rect& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `int` | `layer` |  | - |
| `int` | `xPattern` |  | - |
| `int` | `yPattern` |  | - |
| `int` | `zPattern` |  | - |
| `int` | `animationPhase` |  | - |
| `const std::string&` | `shader` |  | - |
| `Color` | `color` | `Color::white` | - |

---

(getexactsize)=
## `getExactSize`

**Signature:**
```cpp
int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `layer` | `0` | - |
| `int` | `xPattern` | `0` | - |
| `int` | `yPattern` | `0` | - |
| `int` | `zPattern` | `0` | - |
| `int` | `animationPhase` | `0` | - |

**Returns:**
- `int`

---

(setpathable)=
## `setPathable`

**Signature:**
```cpp
void setPathable(bool var);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `var` | - |

---

(gettexture)=
## `getTexture`

**Signature:**
```cpp
private: const TexturePtr& getTexture(int animationPhase);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `animationPhase` | - |

**Returns:**
- `const TexturePtr&`

---

(getbesttexturedimension)=
## `getBestTextureDimension`

**Signature:**
```cpp
Size getBestTextureDimension(int w, int h, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `w` | - |
| `int` | `h` | - |
| `int` | `count` | - |

**Returns:**
- `Size`

---

(getspriteindex)=
## `getSpriteIndex`

**Signature:**
```cpp
uint getSpriteIndex(int w, int h, int l, int x, int y, int z, int a);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `w` | - |
| `int` | `h` | - |
| `int` | `l` | - |
| `int` | `x` | - |
| `int` | `y` | - |
| `int` | `z` | - |
| `int` | `a` | - |

**Returns:**
- `uint`

---

(gettextureindex)=
## `getTextureIndex`

**Signature:**
```cpp
uint getTextureIndex(int l, int x, int y, int z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `l` | - |
| `int` | `x` | - |
| `int` | `y` | - |
| `int` | `z` | - |

**Returns:**
- `uint`

---

(getid)=
## `getId`

**Signature:**
```cpp
uint16 getId();
```

**Returns:**
- `uint16`

---

(getcategory)=
## `getCategory`

**Signature:**
```cpp
ThingCategory getCategory();
```

**Returns:**
- `ThingCategory`

---

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(hasattr)=
## `hasAttr`

**Signature:**
```cpp
bool hasAttr(ThingAttr attr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ThingAttr` | `attr` | - |

**Returns:**
- `bool`

---

(isloaded)=
## `isLoaded`

**Signature:**
```cpp
bool isLoaded();
```

**Returns:**
- `bool`

---

(getlastusage)=
## `getLastUsage`

**Signature:**
```cpp
ticks_t getLastUsage();
```

**Returns:**
- `ticks_t`

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

(getrealsize)=
## `getRealSize`

**Signature:**
```cpp
int getRealSize();
```

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

(getdisplacement)=
## `getDisplacement`

**Signature:**
```cpp
Point getDisplacement();
```

**Returns:**
- `Point`

---

(getdisplacementx)=
## `getDisplacementX`

**Signature:**
```cpp
int getDisplacementX();
```

**Returns:**
- `int`

---

(getdisplacementy)=
## `getDisplacementY`

**Signature:**
```cpp
int getDisplacementY();
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

(getbones)=
## `getBones`

**Signature:**
```cpp
const Point& getBones(int direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `direction` | - |

**Returns:**
- `const Point&`

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

(getmarketdata)=
## `getMarketData`

**Signature:**
```cpp
MarketData getMarketData();
```

**Returns:**
- `MarketData`

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

(hasbones)=
## `hasBones`

**Signature:**
```cpp
bool hasBones();
```

**Returns:**
- `bool`

---

(getsprites)=
## `getSprites`

**Signature:**
```cpp
std::vector<int> getSprites();
```

**Returns:**
- `std::vector&lt;int&gt;`

---

(getopacity)=
## `getOpacity`

**Signature:**
```cpp
float getOpacity();
```

**Returns:**
- `float`

---

(isnotprewalkable)=
## `isNotPreWalkable`

**Signature:**
```cpp
bool isNotPreWalkable();
```

**Returns:**
- `bool`

