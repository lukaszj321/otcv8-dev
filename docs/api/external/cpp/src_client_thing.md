# src/client/thing.h

```cpp
public:
    Thing();
```
```cpp
virtual void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr) { } virtual void setId(uint32 id) { } void setPosition(const Position& position);
```
```cpp
virtual uint32 getId() { return 0; } Position getPosition() { return m_position; } int getStackPriority();
```
```cpp
virtual const TilePtr& getTile();
```
```cpp
ContainerPtr getParentContainer();
```
```cpp
int getStackPos();
```
```cpp
void setMarked(const std::string& color) { if (color.empty()) { m_marked = false; return; } m_marked = true; m_markedColor = Color(color);
```
```cpp
Color updatedMarkedColor();
```
```cpp
virtual bool isItem() { return false; } virtual bool isEffect() { return false; } virtual bool isMissile() { return false; } virtual bool isCreature() { return false; } virtual bool isNpc() { return false; } virtual bool isMonster() { return false; } virtual bool isPlayer() { return false; } virtual bool isLocalPlayer() { return false; } virtual bool isAnimatedText() { return false; } virtual bool isStaticText() { return false; } // type shortcuts virtual const ThingTypePtr& getThingType();
```
```cpp
Size getSize() { return rawGetThingType()->getSize();
```
```cpp
int getWidth() { return rawGetThingType()->getWidth();
```
```cpp
int getHeight() { return rawGetThingType()->getHeight();
```
```cpp
virtual Point getDisplacement() { return rawGetThingType()->getDisplacement();
```
```cpp
virtual int getDisplacementX() { return rawGetThingType()->getDisplacementX();
```
```cpp
virtual int getDisplacementY() { return rawGetThingType()->getDisplacementY();
```
```cpp
virtual int getExactSize(int layer, int xPattern, int yPattern, int zPattern, int animationPhase) { return rawGetThingType()->getExactSize(layer, xPattern, yPattern, zPattern, animationPhase);
```
```cpp
int getLayers() { return rawGetThingType()->getLayers();
```
```cpp
int getNumPatternX() { return rawGetThingType()->getNumPatternX();
```
```cpp
int getNumPatternY() { return rawGetThingType()->getNumPatternY();
```
```cpp
int getNumPatternZ() { return rawGetThingType()->getNumPatternZ();
```
```cpp
int getAnimationPhases() { return rawGetThingType()->getAnimationPhases();
```
```cpp
AnimatorPtr getAnimator() { return rawGetThingType()->getAnimator();
```
```cpp
AnimatorPtr getIdleAnimator() { return rawGetThingType()->getIdleAnimator();
```
```cpp
int getGroundSpeed() { return rawGetThingType()->getGroundSpeed();
```
```cpp
int getMaxTextLength() { return rawGetThingType()->getMaxTextLength();
```
```cpp
Light getLight() { return rawGetThingType()->getLight();
```
```cpp
int getMinimapColor() { return rawGetThingType()->getMinimapColor();
```
```cpp
int getLensHelp() { return rawGetThingType()->getLensHelp();
```
```cpp
int getClothSlot() { return rawGetThingType()->getClothSlot();
```
```cpp
int getElevation() { return rawGetThingType()->getElevation();
```
```cpp
bool isGround() { return rawGetThingType()->isGround();
```
```cpp
bool isGroundBorder() { return rawGetThingType()->isGroundBorder();
```
```cpp
bool isOnBottom() { return rawGetThingType()->isOnBottom();
```
```cpp
bool isOnTop() { return rawGetThingType()->isOnTop();
```
```cpp
bool isContainer() { return rawGetThingType()->isContainer();
```
```cpp
bool isStackable() { return rawGetThingType()->isStackable();
```
```cpp
bool isForceUse() { return rawGetThingType()->isForceUse();
```
```cpp
bool isMultiUse() { return rawGetThingType()->isMultiUse();
```
```cpp
bool isWritable() { return rawGetThingType()->isWritable();
```
```cpp
bool isChargeable() { return rawGetThingType()->isChargeable();
```
```cpp
bool isWritableOnce() { return rawGetThingType()->isWritableOnce();
```
```cpp
bool isFluidContainer() { return rawGetThingType()->isFluidContainer();
```
```cpp
bool isSplash() { return rawGetThingType()->isSplash();
```
```cpp
bool isNotWalkable() { return rawGetThingType()->isNotWalkable();
```
```cpp
bool isNotMoveable() { return rawGetThingType()->isNotMoveable();
```
```cpp
bool blockProjectile() { return rawGetThingType()->blockProjectile();
```
```cpp
bool isNotPathable() { return rawGetThingType()->isNotPathable();
```
```cpp
bool isPickupable() { return rawGetThingType()->isPickupable();
```
```cpp
bool isHangable() { return rawGetThingType()->isHangable();
```
```cpp
bool isHookSouth() { return rawGetThingType()->isHookSouth();
```
```cpp
bool isHookEast() { return rawGetThingType()->isHookEast();
```
```cpp
bool isRotateable() { return rawGetThingType()->isRotateable();
```
```cpp
bool hasLight() { return rawGetThingType()->hasLight();
```
```cpp
bool isDontHide() { return rawGetThingType()->isDontHide();
```
```cpp
bool isTranslucent() { return rawGetThingType()->isTranslucent();
```
```cpp
bool hasDisplacement() { return rawGetThingType()->hasDisplacement();
```
```cpp
bool hasElevation() { return rawGetThingType()->hasElevation();
```
```cpp
bool isLyingCorpse() { return rawGetThingType()->isLyingCorpse();
```
```cpp
bool isAnimateAlways() { return rawGetThingType()->isAnimateAlways();
```
```cpp
bool hasMiniMapColor() { return rawGetThingType()->hasMiniMapColor();
```
```cpp
bool hasLensHelp() { return rawGetThingType()->hasLensHelp();
```
```cpp
bool isFullGround() { return rawGetThingType()->isFullGround();
```
```cpp
bool isIgnoreLook() { return rawGetThingType()->isIgnoreLook();
```
```cpp
bool isCloth() { return rawGetThingType()->isCloth();
```
```cpp
bool isMarketable() { return rawGetThingType()->isMarketable();
```
```cpp
bool isUsable() { return rawGetThingType()->isUsable();
```
```cpp
bool isWrapable() { return rawGetThingType()->isWrapable();
```
```cpp
bool isUnwrapable() { return rawGetThingType()->isUnwrapable();
```
```cpp
bool isTopEffect() { return rawGetThingType()->isTopEffect();
```
```cpp
MarketData getMarketData() { return rawGetThingType()->getMarketData();
```