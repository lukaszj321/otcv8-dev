# src/client/thingtype.h

```cpp
public: ThingType();
```
```cpp
void unserialize(uint16 clientId, ThingCategory category, const FileStreamPtr& fin);
```
```cpp
void unserializeOtml(const OTMLNodePtr& node);
```
```cpp
void unload();
```
```cpp
void serialize(const FileStreamPtr& fin);
```
```cpp
void exportImage(std::string fileName);
```
```cpp
void replaceSprites(std::map<uint32_t, ImagePtr>& replacements, std::string fileName);
```
```cpp
DrawQueueItem* draw(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white, LightView* lightView = nullptr);
```
```cpp
DrawQueueItem* draw(const Rect& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white);
```
```cpp
std::shared_ptr<DrawOutfitParams> drawOutfit(const Point& dest, int maskLayer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white, LightView* lightView = nullptr);
```
```cpp
Rect getDrawSize(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase);
```
```cpp
void drawWithShader(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white, LightView* lightView = nullptr);
```
```cpp
void drawWithShader(const Rect& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white);
```
```cpp
int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```
```cpp
void setPathable(bool var);
```
```cpp
private: const TexturePtr& getTexture(int animationPhase);
```
```cpp
Size getBestTextureDimension(int w, int h, int count);
```
```cpp
uint getSpriteIndex(int w, int h, int l, int x, int y, int z, int a);
```
```cpp
uint getTextureIndex(int l, int x, int y, int z);
```
```cpp
uint16 getId();
```
```cpp
ThingCategory getCategory();
```
```cpp
bool isNull();
```
```cpp
bool hasAttr(ThingAttr attr);
```
```cpp
bool isLoaded();
```
```cpp
ticks_t getLastUsage();
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
int getRealSize();
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
Point getDisplacement();
```
```cpp
int getDisplacementX();
```
```cpp
int getDisplacementY();
```
```cpp
int getElevation();
```
```cpp
const Point& getBones(int direction);
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
MarketData getMarketData();
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
bool hasBones();
```
```cpp
std::vector<int> getSprites();
```
```cpp
float getOpacity();
```
```cpp
bool isNotPreWalkable();
```