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
void setName(const std::string& name);
```
```cpp
void setHealthPercent(uint8 healthPercent);
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
void setSpeed(uint16 speed);
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
void setSpeedFormula(double speedA, double speedB, double speedC);
```
```cpp
void addTimedSquare(uint8 color);
```
```cpp
void setText(const std::string& text, const Color& color);
```
```cpp
std::string getText();
```
```cpp
void setTitle(const std::string& title, const std::string& font, const Color& color);
```
```cpp
Point getDrawOffset();
```
```cpp
uint16 getStepDuration(bool ignoreDiagonal = false, Otc::Direction dir = Otc::InvalidDirection);
```
```cpp
bool hasSpeedFormula();
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
void updateShield();
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
bool canShoot(int distance);
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
void addTopWidget(const UIWidgetPtr& widget);
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
void setProgressBar(uint32 duration, bool ltr);
```
```cpp
void updateProgressBar(uint32 duration, bool ltr);
```
```cpp
protected: virtual void updateWalkAnimation(uint8 totalPixelsWalked);
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
```cpp
void setId(uint32 id);
```
```cpp
void setManaPercent(int8 value);
```
```cpp
void setLight(const Light& light);
```
```cpp
void setPassable(bool passable);
```
```cpp
void removeTimedSquare();
```
```cpp
void showStaticSquare(const Color& color);
```
```cpp
void hideStaticSquare();
```
```cpp
void setInformationColor(const Color& color);
```
```cpp
void resetInformationColor();
```
```cpp
Point getInformationOffset();
```
```cpp
void setInformationOffset(int x, int y);
```
```cpp
void clearText();
```
```cpp
void clearTitle();
```
```cpp
std::string getTitle();
```
```cpp
uint32 getId();
```
```cpp
std::string getName();
```
```cpp
uint8 getHealthPercent();
```
```cpp
int8 getManaPercent();
```
```cpp
Otc::Direction getDirection();
```
```cpp
Otc::Direction getWalkDirection();
```
```cpp
Outfit getOutfit();
```
```cpp
Light getLight();
```
```cpp
uint16 getSpeed();
```
```cpp
double getBaseSpeed();
```
```cpp
uint8 getSkull();
```
```cpp
uint8 getShield();
```
```cpp
uint8 getEmblem();
```
```cpp
uint8 getType();
```
```cpp
uint8 getIcon();
```
```cpp
bool isPassable();
```
```cpp
Point getWalkOffset(bool inNextFrame = false);
```
```cpp
Position getLastStepFromPosition();
```
```cpp
Position getLastStepToPosition();
```
```cpp
float getStepProgress();
```
```cpp
int getStepTicksLeft();
```
```cpp
ticks_t getWalkTicksElapsed();
```
```cpp
double getSpeedFormula(Otc::SpeedFormula formula);
```
```cpp
PointF getJumpOffset();
```
```cpp
bool isTimedSquareVisible();
```
```cpp
Color getTimedSquareColor();
```
```cpp
bool isStaticSquareVisible();
```
```cpp
Color getStaticSquareColor();
```
```cpp
void allowAppearWalk(uint16_t stepSpeed);
```
```cpp
bool isWalking();
```
```cpp
bool isRemoved();
```
```cpp
bool isInvisible();
```
```cpp
bool isDead();
```
```cpp
bool canBeSeen();
```
```cpp
bool isCreature();
```
```cpp
virtual bool isPreWalking();
```
```cpp
virtual Position getPrewalkingPosition(bool beforePrewalk = false);
```
```cpp
TilePtr getWalkingTileOrTile();
```
```cpp
virtual bool isServerWalking();
```
```cpp
void setElevation(uint8 elevation);
```
```cpp
uint8 getElevation();
```
```cpp
uint8 getProgressBarPercent();
```
```cpp
public: bool isNpc();
```
```cpp
public: bool isMonster();
```