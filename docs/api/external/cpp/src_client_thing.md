# src/client/thing.h

```cpp
public: Thing();
```
```cpp
void setPosition(const Position& position);
```
```cpp
int getStackPriority();
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
Color updatedMarkedColor();
```
```cpp
virtual const ThingTypePtr& getThingType();
```
```cpp
virtual void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```
```cpp
virtual void setId(uint32 id);
```
```cpp
virtual uint32 getId();
```
```cpp
Position getPosition();
```
```cpp
void setMarked(const std::string& color);
```
```cpp
virtual bool isItem();
```
```cpp
virtual bool isEffect();
```
```cpp
virtual bool isMissile();
```
```cpp
virtual bool isCreature();
```
```cpp
virtual bool isNpc();
```
```cpp
virtual bool isMonster();
```
```cpp
virtual bool isPlayer();
```
```cpp
virtual bool isLocalPlayer();
```
```cpp
virtual bool isAnimatedText();
```
```cpp
virtual bool isStaticText();
```
```cpp
Size getSize();
```
```cpp
int getWidth();
```
```cpp
int getHeight();
```
```cpp
virtual Point getDisplacement();
```
```cpp
virtual int getDisplacementX();
```
```cpp
virtual int getDisplacementY();
```
```cpp
virtual int getExactSize(int layer, int xPattern, int yPattern, int zPattern, int animationPhase);
```
```cpp
int getLayers();
```
```cpp
int getNumPatternX();
```
```cpp
int getNumPatternY();
```
```cpp
int getNumPatternZ();
```
```cpp
int getAnimationPhases();
```
```cpp
AnimatorPtr getAnimator();
```
```cpp
AnimatorPtr getIdleAnimator();
```
```cpp
int getGroundSpeed();
```
```cpp
int getMaxTextLength();
```
```cpp
Light getLight();
```
```cpp
int getMinimapColor();
```
```cpp
int getLensHelp();
```
```cpp
int getClothSlot();
```
```cpp
int getElevation();
```
```cpp
bool isGround();
```
```cpp
bool isGroundBorder();
```
```cpp
bool isOnBottom();
```
```cpp
bool isOnTop();
```
```cpp
bool isContainer();
```
```cpp
bool isStackable();
```
```cpp
bool isForceUse();
```
```cpp
bool isMultiUse();
```
```cpp
bool isWritable();
```
```cpp
bool isChargeable();
```
```cpp
bool isWritableOnce();
```
```cpp
bool isFluidContainer();
```
```cpp
bool isSplash();
```
```cpp
bool isNotWalkable();
```
```cpp
bool isNotMoveable();
```
```cpp
bool blockProjectile();
```
```cpp
bool isNotPathable();
```
```cpp
bool isPickupable();
```
```cpp
bool isHangable();
```
```cpp
bool isHookSouth();
```
```cpp
bool isHookEast();
```
```cpp
bool isRotateable();
```
```cpp
bool hasLight();
```
```cpp
bool isDontHide();
```
```cpp
bool isTranslucent();
```
```cpp
bool hasDisplacement();
```
```cpp
bool hasElevation();
```
```cpp
bool isLyingCorpse();
```
```cpp
bool isAnimateAlways();
```
```cpp
bool hasMiniMapColor();
```
```cpp
bool hasLensHelp();
```
```cpp
bool isFullGround();
```
```cpp
bool isIgnoreLook();
```
```cpp
bool isCloth();
```
```cpp
bool isMarketable();
```
```cpp
bool isUsable();
```
```cpp
bool isWrapable();
```
```cpp
bool isUnwrapable();
```
```cpp
bool isTopEffect();
```
```cpp
MarketData getMarketData();
```
```cpp
void hide();
```
```cpp
void show();
```
```cpp
void setHidden(bool value);
```
```cpp
bool isHidden();
```
```cpp
virtual void onPositionChange(const Position& newPos, const Position& oldPos);
```
```cpp
virtual void onAppear();
```
```cpp
virtual void onDisappear();
```