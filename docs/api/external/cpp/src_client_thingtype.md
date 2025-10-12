# src/client/thingtype.h

```cpp
public:
    ThingType();
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
uint16 getId() { return m_id; } ThingCategory getCategory() { return m_category; } bool isNull() { return m_null; } bool hasAttr(ThingAttr attr) { return m_attribs.has(attr);
```
```cpp
bool isLoaded() { return m_loaded; } ticks_t getLastUsage() { return m_lastUsage; } Size getSize() { return m_size; } int getWidth() { return m_size.width();
```
```cpp
int getHeight() { return m_size.height();
```
```cpp
int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```
```cpp
int getRealSize() { return m_realSize; } int getLayers() { return m_layers; } int getNumPatternX() { return m_numPatternX; } int getNumPatternY() { return m_numPatternY; } int getNumPatternZ() { return m_numPatternZ; } int getAnimationPhases() { return m_animationPhases; } AnimatorPtr getAnimator() { return m_animator; } AnimatorPtr getIdleAnimator() { return m_idleAnimator; } Point getDisplacement() { return m_displacement; } int getDisplacementX() { return getDisplacement().x; } int getDisplacementY() { return getDisplacement().y; } int getElevation() { return m_elevation; } const Point& getBones(int direction) { return m_bones[direction]; } int getGroundSpeed() { return m_attribs.get<uint16>(ThingAttrGround);
```
```cpp
int getMaxTextLength() { return m_attribs.has(ThingAttrWritableOnce) ? m_attribs.get<uint16>(ThingAttrWritableOnce) : m_attribs.get<uint16>(ThingAttrWritable);
```
```cpp
Light getLight() { return m_attribs.get<Light>(ThingAttrLight);
```
```cpp
int getMinimapColor() { return m_attribs.get<uint16>(ThingAttrMinimapColor);
```
```cpp
int getLensHelp() { return m_attribs.get<uint16>(ThingAttrLensHelp);
```
```cpp
int getClothSlot() { return m_attribs.get<uint16>(ThingAttrCloth);
```
```cpp
MarketData getMarketData() { return m_attribs.get<MarketData>(ThingAttrMarket);
```
```cpp
bool isGround() { return m_attribs.has(ThingAttrGround);
```
```cpp
bool isGroundBorder() { return m_attribs.has(ThingAttrGroundBorder);
```
```cpp
bool isOnBottom() { return m_attribs.has(ThingAttrOnBottom);
```
```cpp
bool isOnTop() { return m_attribs.has(ThingAttrOnTop);
```
```cpp
bool isContainer() { return m_attribs.has(ThingAttrContainer);
```
```cpp
bool isStackable() { return m_attribs.has(ThingAttrStackable);
```
```cpp
bool isForceUse() { return m_attribs.has(ThingAttrForceUse);
```
```cpp
bool isMultiUse() { return m_attribs.has(ThingAttrMultiUse);
```
```cpp
bool isWritable() { return m_attribs.has(ThingAttrWritable);
```
```cpp
bool isChargeable() { return m_attribs.has(ThingAttrChargeable);
```
```cpp
bool isWritableOnce() { return m_attribs.has(ThingAttrWritableOnce);
```
```cpp
bool isFluidContainer() { return m_attribs.has(ThingAttrFluidContainer);
```
```cpp
bool isSplash() { return m_attribs.has(ThingAttrSplash);
```
```cpp
bool isNotWalkable() { return m_attribs.has(ThingAttrNotWalkable);
```
```cpp
bool isNotMoveable() { return m_attribs.has(ThingAttrNotMoveable);
```
```cpp
bool blockProjectile() { return m_attribs.has(ThingAttrBlockProjectile);
```
```cpp
bool isNotPathable() { return m_attribs.has(ThingAttrNotPathable);
```
```cpp
bool isPickupable() { return m_attribs.has(ThingAttrPickupable);
```
```cpp
bool isHangable() { return m_attribs.has(ThingAttrHangable);
```
```cpp
bool isHookSouth() { return m_attribs.has(ThingAttrHookSouth);
```
```cpp
bool isHookEast() { return m_attribs.has(ThingAttrHookEast);
```
```cpp
bool isRotateable() { return m_attribs.has(ThingAttrRotateable);
```
```cpp
bool hasLight() { return m_attribs.has(ThingAttrLight);
```
```cpp
bool isDontHide() { return m_attribs.has(ThingAttrDontHide);
```
```cpp
bool isTranslucent() { return m_attribs.has(ThingAttrTranslucent);
```
```cpp
bool hasDisplacement() { return m_attribs.has(ThingAttrDisplacement);
```
```cpp
bool hasElevation() { return m_attribs.has(ThingAttrElevation);
```
```cpp
bool isLyingCorpse() { return m_attribs.has(ThingAttrLyingCorpse);
```
```cpp
bool isAnimateAlways() { return m_attribs.has(ThingAttrAnimateAlways);
```
```cpp
bool hasMiniMapColor() { return m_attribs.has(ThingAttrMinimapColor);
```
```cpp
bool hasLensHelp() { return m_attribs.has(ThingAttrLensHelp);
```
```cpp
bool isFullGround() { return m_attribs.has(ThingAttrFullGround);
```
```cpp
bool isIgnoreLook() { return m_attribs.has(ThingAttrLook);
```
```cpp
bool isCloth() { return m_attribs.has(ThingAttrCloth);
```
```cpp
bool isMarketable() { return m_attribs.has(ThingAttrMarket);
```
```cpp
bool isUsable() { return m_attribs.has(ThingAttrUsable);
```
```cpp
bool isWrapable() { return m_attribs.has(ThingAttrWrapable);
```
```cpp
bool isUnwrapable() { return m_attribs.has(ThingAttrUnwrapable);
```
```cpp
bool isTopEffect() { return m_attribs.has(ThingAttrTopEffect);
```
```cpp
bool hasBones() { return m_attribs.has(ThingAttrBones);
```
```cpp
std::vector<int> getSprites() { return m_spritesIndex; } // additional float getOpacity() { return m_opacity; } bool isNotPreWalkable() { return m_attribs.has(ThingAttrNotPreWalkable);
```
```cpp
void setPathable(bool var);
```
```cpp
private:
    const TexturePtr& getTexture(int animationPhase);
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