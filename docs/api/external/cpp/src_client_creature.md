# src/client/creature.h

```cpp
virtual void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```
```cpp
virtual void drawOutfit(const Rect& destRect, Otc::Direction direction = Otc::InvalidDirection, const Color& color = Color::white, bool animate = false, bool ui = false, bool oldScaling = false);
```
```cpp
void drawInformation(const Point& point, bool useGray, const Rect& parentRect, int drawFlags);
```
```cpp
bool isInsideOffset(Point offset);
```
```cpp
void setId(uint32 id) { m_id = id; } void setName(const std::string& name);
```
```cpp
void setManaPercent(int8 value) { m_manaPercent = value; } void setHealthPercent(uint8 healthPercent);
```
```cpp
void setDirection(Otc::Direction direction);
```
```cpp
void setOutfit(const Outfit& outfit);
```
```cpp
void setOutfitColor(const Color& color, int duration);
```
```cpp
void setLight(const Light& light) { m_light = light; } void setSpeed(uint16 speed);
```
```cpp
void setBaseSpeed(double baseSpeed);
```
```cpp
void setSkull(uint8 skull);
```
```cpp
void setShield(uint8 shield);
```
```cpp
void setEmblem(uint8 emblem);
```
```cpp
void setType(uint8 type);
```
```cpp
void setIcon(uint8 icon);
```
```cpp
void setSkullTexture(const std::string& filename);
```
```cpp
void setShieldTexture(const std::string& filename, bool blink);
```
```cpp
void setEmblemTexture(const std::string& filename);
```
```cpp
void setTypeTexture(const std::string& filename);
```
```cpp
void setIconTexture(const std::string& filename);
```
```cpp
void setPassable(bool passable) { m_passable = passable; } void setSpeedFormula(double speedA, double speedB, double speedC);
```
```cpp
void addTimedSquare(uint8 color);
```
```cpp
void removeTimedSquare() { m_showTimedSquare = false; } void showStaticSquare(const Color& color) { m_showStaticSquare = true; m_staticSquareColor = color; } void hideStaticSquare() { m_showStaticSquare = false; } void setInformationColor(const Color& color) { m_useCustomInformationColor = true; m_informationColor = color; } void resetInformationColor() { m_useCustomInformationColor = false; setHealthPercent(getHealthPercent());
```
```cpp
Point getInformationOffset() { return m_informationOffset; } void setInformationOffset(int x, int y) { m_informationOffset = Point(x, y);
```
```cpp
void setText(const std::string& text, const Color& color);
```
```cpp
std::string getText();
```
```cpp
void clearText() { setText("", Color::white);
```
```cpp
void setTitle(const std::string& title, const std::string& font, const Color& color);
```
```cpp
void clearTitle() { setTitle("", "", Color::white);
```
```cpp
std::string getTitle() { return m_titleCache.getText();
```
```cpp
uint32 getId() { return m_id; } std::string getName() { return m_name; } uint8 getHealthPercent() { return m_healthPercent; } int8 getManaPercent() { return m_manaPercent; } Otc::Direction getDirection() { return m_direction; } Otc::Direction getWalkDirection() { return m_walkDirection; } Outfit getOutfit() { return m_outfit; } Light getLight() { return m_light; } uint16 getSpeed() { return m_speed; } double getBaseSpeed() { return m_baseSpeed; } uint8 getSkull() { return m_skull; } uint8 getShield() { return m_shield; } uint8 getEmblem() { return m_emblem; } uint8 getType() { return m_type; } uint8 getIcon() { return m_icon; } bool isPassable() { return m_passable; } Point getDrawOffset();
```
```cpp
uint16 getStepDuration(bool ignoreDiagonal = false, Otc::Direction dir = Otc::InvalidDirection);
```
```cpp
Point getWalkOffset(bool inNextFrame = false) { return inNextFrame ? m_walkOffsetInNextFrame : m_walkOffset; } Position getLastStepFromPosition() { return m_lastStepFromPosition; } Position getLastStepToPosition() { return m_lastStepToPosition; } float getStepProgress() { return m_walkTimer.ticksElapsed() / getStepDuration();
```
```cpp
int getStepTicksLeft() { return getStepDuration() - m_walkTimer.ticksElapsed();
```
```cpp
ticks_t getWalkTicksElapsed() { return m_walkTimer.ticksElapsed();
```
```cpp
double getSpeedFormula(Otc::SpeedFormula formula) { return m_speedFormula[formula]; } bool hasSpeedFormula();
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
virtual int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```
```cpp
PointF getJumpOffset() { return m_jumpOffset; } bool isTimedSquareVisible() { return m_showTimedSquare; } Color getTimedSquareColor() { return m_timedSquareColor; } bool isStaticSquareVisible() { return m_showStaticSquare; } Color getStaticSquareColor() { return m_staticSquareColor; } void updateShield();
```
```cpp
int getWalkAnimationPhases();
```
```cpp
virtual void turn(Otc::Direction direction);
```
```cpp
void jump(int height, int duration);
```
```cpp
virtual void walk(const Position& oldPos, const Position& newPos);
```
```cpp
virtual void stopWalk();
```
```cpp
void allowAppearWalk(uint16_t stepSpeed) { m_allowAppearWalk = true; m_stepDuration = stepSpeed; } bool isWalking() { return m_walking; } bool isRemoved() { return m_removed; } bool isInvisible() { return m_outfit.getCategory() == ThingCategoryEffect && m_outfit.getAuxId() == 13; } bool isDead() { return m_healthPercent <= 0; } bool canBeSeen() { return !isInvisible() || isPlayer();
```
```cpp
bool isCreature() { return true; } bool canShoot(int distance);
```
```cpp
const ThingTypePtr& getThingType();
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
```cpp
virtual void onDeath();
```
```cpp
virtual bool isPreWalking() { return false; } virtual Position getPrewalkingPosition(bool beforePrewalk = false) { return m_position; } TilePtr getWalkingTileOrTile() { return m_walkingTile ? m_walkingTile : getTile();
```
```cpp
virtual bool isServerWalking() { return true; } void setElevation(uint8 elevation) { m_elevation = elevation; } uint8 getElevation() { return m_elevation; } // widgets void addTopWidget(const UIWidgetPtr& widget);
```
```cpp
void addBottomWidget(const UIWidgetPtr& widget);
```
```cpp
void addDirectionalWidget(const UIWidgetPtr& widget);
```
```cpp
void removeTopWidget(const UIWidgetPtr& widget);
```
```cpp
void removeBottomWidget(const UIWidgetPtr& widget);
```
```cpp
void removeDirectionalWidget(const UIWidgetPtr& widget);
```
```cpp
std::list<UIWidgetPtr> getTopWidgets();
```
```cpp
std::list<UIWidgetPtr> getBottomWidgets();
```
```cpp
std::list<UIWidgetPtr> getDirectionalWdigets();
```
```cpp
void clearWidgets();
```
```cpp
void clearTopWidgets();
```
```cpp
void clearBottomWidgets();
```
```cpp
void clearDirectionalWidgets();
```
```cpp
void drawTopWidgets(const Point& rect, const Otc::Direction direction);
```
```cpp
void drawBottomWidgets(const Point& rect, const Otc::Direction direction);
```
```cpp
uint8 getProgressBarPercent() { return m_progressBarPercent; } void setProgressBar(uint32 duration, bool ltr);
```
```cpp
void updateProgressBar(uint32 duration, bool ltr);
```
```cpp
protected:
    virtual void updateWalkAnimation(uint8 totalPixelsWalked);
```
```cpp
virtual void updateWalkOffset(uint8 totalPixelsWalked, bool inNextFrame = false);
```
```cpp
void updateWalkingTile();
```
```cpp
virtual void nextWalkUpdate();
```
```cpp
virtual void updateWalk();
```
```cpp
virtual void terminateWalk();
```
```cpp
void updateOutfitColor(Color color, Color finalColor, Color delta, int duration);
```
```cpp
void updateJump();
```