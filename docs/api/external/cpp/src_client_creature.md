---
title: "src/client/creature.h"
source_file: "src/client/creature.h"
generated_at: "2025-11-01T04:06:42.716Z"
doc_type: "cpp_api"
---

# src/client/creature.h

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

(drawoutfit)=
## `drawOutfit`

**Signature:**
```cpp
virtual void drawOutfit(const Rect& destRect, Otc::Direction direction = Otc::InvalidDirection, const Color& color = Color::white, bool animate = false, bool ui = false, bool oldScaling = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `destRect` |  | - |
| `Otc::Direction` | `direction` | `Otc::InvalidDirection` | - |
| `const Color&` | `color` | `Color::white` | - |
| `bool` | `animate` | `false` | - |
| `bool` | `ui` | `false` | - |
| `bool` | `oldScaling` | `false` | - |

---

(drawinformation)=
## `drawInformation`

**Signature:**
```cpp
void drawInformation(const Point& point, bool useGray, const Rect& parentRect, int drawFlags);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |
| `bool` | `useGray` | - |
| `const Rect&` | `parentRect` | - |
| `int` | `drawFlags` | - |

---

(isinsideoffset)=
## `isInsideOffset`

**Signature:**
```cpp
bool isInsideOffset(Point offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `offset` | - |

**Returns:**
- `bool`

---

(setname)=
## `setName`

**Signature:**
```cpp
void setName(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(sethealthpercent)=
## `setHealthPercent`

**Signature:**
```cpp
void setHealthPercent(uint8 healthPercent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `healthPercent` | - |

---

(setdirection)=
## `setDirection`

**Signature:**
```cpp
void setDirection(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(setoutfit)=
## `setOutfit`

**Signature:**
```cpp
void setOutfit(const Outfit& outfit);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `outfit` | - |

---

(setoutfitcolor)=
## `setOutfitColor`

**Signature:**
```cpp
void setOutfitColor(const Color& color, int duration);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |
| `int` | `duration` | - |

---

(setspeed)=
## `setSpeed`

**Signature:**
```cpp
void setSpeed(uint16 speed);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `speed` | - |

---

(setbasespeed)=
## `setBaseSpeed`

**Signature:**
```cpp
void setBaseSpeed(double baseSpeed);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `baseSpeed` | - |

---

(setskull)=
## `setSkull`

**Signature:**
```cpp
void setSkull(uint8 skull);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `skull` | - |

---

(setshield)=
## `setShield`

**Signature:**
```cpp
void setShield(uint8 shield);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `shield` | - |

---

(setemblem)=
## `setEmblem`

**Signature:**
```cpp
void setEmblem(uint8 emblem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `emblem` | - |

---

(settype)=
## `setType`

**Signature:**
```cpp
void setType(uint8 type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `type` | - |

---

(seticon)=
## `setIcon`

**Signature:**
```cpp
void setIcon(uint8 icon);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `icon` | - |

---

(setskulltexture)=
## `setSkullTexture`

**Signature:**
```cpp
void setSkullTexture(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

---

(setshieldtexture)=
## `setShieldTexture`

**Signature:**
```cpp
void setShieldTexture(const std::string& filename, bool blink);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |
| `bool` | `blink` | - |

---

(setemblemtexture)=
## `setEmblemTexture`

**Signature:**
```cpp
void setEmblemTexture(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

---

(settypetexture)=
## `setTypeTexture`

**Signature:**
```cpp
void setTypeTexture(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

---

(seticontexture)=
## `setIconTexture`

**Signature:**
```cpp
void setIconTexture(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

---

(setspeedformula)=
## `setSpeedFormula`

**Signature:**
```cpp
void setSpeedFormula(double speedA, double speedB, double speedC);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `speedA` | - |
| `double` | `speedB` | - |
| `double` | `speedC` | - |

---

(addtimedsquare)=
## `addTimedSquare`

**Signature:**
```cpp
void addTimedSquare(uint8 color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `color` | - |

---

(settext)=
## `setText`

**Signature:**
```cpp
void setText(const std::string& text, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |
| `const Color&` | `color` | - |

---

(gettext)=
## `getText`

**Signature:**
```cpp
std::string getText();
```

**Returns:**
- `std::string`

---

(settitle)=
## `setTitle`

**Signature:**
```cpp
void setTitle(const std::string& title, const std::string& font, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `title` | - |
| `const std::string&` | `font` | - |
| `const Color&` | `color` | - |

---

(getdrawoffset)=
## `getDrawOffset`

**Signature:**
```cpp
Point getDrawOffset();
```

**Returns:**
- `Point`

---

(getstepduration)=
## `getStepDuration`

**Signature:**
```cpp
uint16 getStepDuration(bool ignoreDiagonal = false, Otc::Direction dir = Otc::InvalidDirection);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `ignoreDiagonal` | `false` | - |
| `Otc::Direction` | `dir` | `Otc::InvalidDirection` | - |

**Returns:**
- `uint16`

---

(hasspeedformula)=
## `hasSpeedFormula`

**Signature:**
```cpp
bool hasSpeedFormula();
```

**Returns:**
- `bool`

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
virtual int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
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

(updateshield)=
## `updateShield`

**Signature:**
```cpp
void updateShield();
```

---

(getwalkanimationphases)=
## `getWalkAnimationPhases`

**Signature:**
```cpp
int getWalkAnimationPhases();
```

**Returns:**
- `int`

---

(turn)=
## `turn`

**Signature:**
```cpp
virtual void turn(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(jump)=
## `jump`

**Signature:**
```cpp
void jump(int height, int duration);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |
| `int` | `duration` | - |

---

(walk)=
## `walk`

**Signature:**
```cpp
virtual void walk(const Position& oldPos, const Position& newPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `oldPos` | - |
| `const Position&` | `newPos` | - |

---

(stopwalk)=
## `stopWalk`

**Signature:**
```cpp
virtual void stopWalk();
```

---

(canshoot)=
## `canShoot`

**Signature:**
```cpp
bool canShoot(int distance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `distance` | - |

**Returns:**
- `bool`

---

(getthingtype)=
## `getThingType`

**Signature:**
```cpp
const ThingTypePtr& getThingType();
```

**Returns:**
- `const ThingTypePtr&`

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

(ondeath)=
## `onDeath`

**Signature:**
```cpp
virtual void onDeath();
```

---

(addtopwidget)=
## `addTopWidget`

**Signature:**
```cpp
void addTopWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(addbottomwidget)=
## `addBottomWidget`

**Signature:**
```cpp
void addBottomWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(adddirectionalwidget)=
## `addDirectionalWidget`

**Signature:**
```cpp
void addDirectionalWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(removetopwidget)=
## `removeTopWidget`

**Signature:**
```cpp
void removeTopWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(removebottomwidget)=
## `removeBottomWidget`

**Signature:**
```cpp
void removeBottomWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(removedirectionalwidget)=
## `removeDirectionalWidget`

**Signature:**
```cpp
void removeDirectionalWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(gettopwidgets)=
## `getTopWidgets`

**Signature:**
```cpp
std::list<UIWidgetPtr> getTopWidgets();
```

**Returns:**
- `std::list&lt;UIWidgetPtr&gt;`

---

(getbottomwidgets)=
## `getBottomWidgets`

**Signature:**
```cpp
std::list<UIWidgetPtr> getBottomWidgets();
```

**Returns:**
- `std::list&lt;UIWidgetPtr&gt;`

---

(getdirectionalwdigets)=
## `getDirectionalWdigets`

**Signature:**
```cpp
std::list<UIWidgetPtr> getDirectionalWdigets();
```

**Returns:**
- `std::list&lt;UIWidgetPtr&gt;`

---

(clearwidgets)=
## `clearWidgets`

**Signature:**
```cpp
void clearWidgets();
```

---

(cleartopwidgets)=
## `clearTopWidgets`

**Signature:**
```cpp
void clearTopWidgets();
```

---

(clearbottomwidgets)=
## `clearBottomWidgets`

**Signature:**
```cpp
void clearBottomWidgets();
```

---

(cleardirectionalwidgets)=
## `clearDirectionalWidgets`

**Signature:**
```cpp
void clearDirectionalWidgets();
```

---

(drawtopwidgets)=
## `drawTopWidgets`

**Signature:**
```cpp
void drawTopWidgets(const Point& rect, const Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `rect` | - |
| `const Otc::Direction` | `direction` | - |

---

(drawbottomwidgets)=
## `drawBottomWidgets`

**Signature:**
```cpp
void drawBottomWidgets(const Point& rect, const Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `rect` | - |
| `const Otc::Direction` | `direction` | - |

---

(setprogressbar)=
## `setProgressBar`

**Signature:**
```cpp
void setProgressBar(uint32 duration, bool ltr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `duration` | - |
| `bool` | `ltr` | - |

---

(updateprogressbar)=
## `updateProgressBar`

**Signature:**
```cpp
void updateProgressBar(uint32 duration, bool ltr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `duration` | - |
| `bool` | `ltr` | - |

---

(updatewalkanimation)=
## `updateWalkAnimation`

**Signature:**
```cpp
protected: virtual void updateWalkAnimation(uint8 totalPixelsWalked);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `totalPixelsWalked` | - |

---

(updatewalkoffset)=
## `updateWalkOffset`

**Signature:**
```cpp
virtual void updateWalkOffset(uint8 totalPixelsWalked, bool inNextFrame = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `uint8` | `totalPixelsWalked` |  | - |
| `bool` | `inNextFrame` | `false` | - |

---

(updatewalkingtile)=
## `updateWalkingTile`

**Signature:**
```cpp
void updateWalkingTile();
```

---

(nextwalkupdate)=
## `nextWalkUpdate`

**Signature:**
```cpp
virtual void nextWalkUpdate();
```

---

(updatewalk)=
## `updateWalk`

**Signature:**
```cpp
virtual void updateWalk();
```

---

(terminatewalk)=
## `terminateWalk`

**Signature:**
```cpp
virtual void terminateWalk();
```

---

(updateoutfitcolor)=
## `updateOutfitColor`

**Signature:**
```cpp
void updateOutfitColor(Color color, Color finalColor, Color delta, int duration);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Color` | `color` | - |
| `Color` | `finalColor` | - |
| `Color` | `delta` | - |
| `int` | `duration` | - |

---

(updatejump)=
## `updateJump`

**Signature:**
```cpp
void updateJump();
```

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

---

(setmanapercent)=
## `setManaPercent`

**Signature:**
```cpp
void setManaPercent(int8 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int8` | `value` | - |

---

(setlight)=
## `setLight`

**Signature:**
```cpp
void setLight(const Light& light);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Light&` | `light` | - |

---

(setpassable)=
## `setPassable`

**Signature:**
```cpp
void setPassable(bool passable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `passable` | - |

---

(removetimedsquare)=
## `removeTimedSquare`

**Signature:**
```cpp
void removeTimedSquare();
```

---

(showstaticsquare)=
## `showStaticSquare`

**Signature:**
```cpp
void showStaticSquare(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(hidestaticsquare)=
## `hideStaticSquare`

**Signature:**
```cpp
void hideStaticSquare();
```

---

(setinformationcolor)=
## `setInformationColor`

**Signature:**
```cpp
void setInformationColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(resetinformationcolor)=
## `resetInformationColor`

**Signature:**
```cpp
void resetInformationColor();
```

---

(getinformationoffset)=
## `getInformationOffset`

**Signature:**
```cpp
Point getInformationOffset();
```

**Returns:**
- `Point`

---

(setinformationoffset)=
## `setInformationOffset`

**Signature:**
```cpp
void setInformationOffset(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(cleartext)=
## `clearText`

**Signature:**
```cpp
void clearText();
```

---

(cleartitle)=
## `clearTitle`

**Signature:**
```cpp
void clearTitle();
```

---

(gettitle)=
## `getTitle`

**Signature:**
```cpp
std::string getTitle();
```

**Returns:**
- `std::string`

---

(getid)=
## `getId`

**Signature:**
```cpp
uint32 getId();
```

**Returns:**
- `uint32`

---

(getname)=
## `getName`

**Signature:**
```cpp
std::string getName();
```

**Returns:**
- `std::string`

---

(gethealthpercent)=
## `getHealthPercent`

**Signature:**
```cpp
uint8 getHealthPercent();
```

**Returns:**
- `uint8`

---

(getmanapercent)=
## `getManaPercent`

**Signature:**
```cpp
int8 getManaPercent();
```

**Returns:**
- `int8`

---

(getdirection)=
## `getDirection`

**Signature:**
```cpp
Otc::Direction getDirection();
```

**Returns:**
- `Otc::Direction`

---

(getwalkdirection)=
## `getWalkDirection`

**Signature:**
```cpp
Otc::Direction getWalkDirection();
```

**Returns:**
- `Otc::Direction`

---

(getoutfit)=
## `getOutfit`

**Signature:**
```cpp
Outfit getOutfit();
```

**Returns:**
- `Outfit`

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

(getspeed)=
## `getSpeed`

**Signature:**
```cpp
uint16 getSpeed();
```

**Returns:**
- `uint16`

---

(getbasespeed)=
## `getBaseSpeed`

**Signature:**
```cpp
double getBaseSpeed();
```

**Returns:**
- `double`

---

(getskull)=
## `getSkull`

**Signature:**
```cpp
uint8 getSkull();
```

**Returns:**
- `uint8`

---

(getshield)=
## `getShield`

**Signature:**
```cpp
uint8 getShield();
```

**Returns:**
- `uint8`

---

(getemblem)=
## `getEmblem`

**Signature:**
```cpp
uint8 getEmblem();
```

**Returns:**
- `uint8`

---

(gettype)=
## `getType`

**Signature:**
```cpp
uint8 getType();
```

**Returns:**
- `uint8`

---

(geticon)=
## `getIcon`

**Signature:**
```cpp
uint8 getIcon();
```

**Returns:**
- `uint8`

---

(ispassable)=
## `isPassable`

**Signature:**
```cpp
bool isPassable();
```

**Returns:**
- `bool`

---

(getwalkoffset)=
## `getWalkOffset`

**Signature:**
```cpp
Point getWalkOffset(bool inNextFrame = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `inNextFrame` | `false` | - |

**Returns:**
- `Point`

---

(getlaststepfromposition)=
## `getLastStepFromPosition`

**Signature:**
```cpp
Position getLastStepFromPosition();
```

**Returns:**
- `Position`

---

(getlaststeptoposition)=
## `getLastStepToPosition`

**Signature:**
```cpp
Position getLastStepToPosition();
```

**Returns:**
- `Position`

---

(getstepprogress)=
## `getStepProgress`

**Signature:**
```cpp
float getStepProgress();
```

**Returns:**
- `float`

---

(getstepticksleft)=
## `getStepTicksLeft`

**Signature:**
```cpp
int getStepTicksLeft();
```

**Returns:**
- `int`

---

(getwalktickselapsed)=
## `getWalkTicksElapsed`

**Signature:**
```cpp
ticks_t getWalkTicksElapsed();
```

**Returns:**
- `ticks_t`

---

(getspeedformula)=
## `getSpeedFormula`

**Signature:**
```cpp
double getSpeedFormula(Otc::SpeedFormula formula);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::SpeedFormula` | `formula` | - |

**Returns:**
- `double`

---

(getjumpoffset)=
## `getJumpOffset`

**Signature:**
```cpp
PointF getJumpOffset();
```

**Returns:**
- `PointF`

---

(istimedsquarevisible)=
## `isTimedSquareVisible`

**Signature:**
```cpp
bool isTimedSquareVisible();
```

**Returns:**
- `bool`

---

(gettimedsquarecolor)=
## `getTimedSquareColor`

**Signature:**
```cpp
Color getTimedSquareColor();
```

**Returns:**
- `Color`

---

(isstaticsquarevisible)=
## `isStaticSquareVisible`

**Signature:**
```cpp
bool isStaticSquareVisible();
```

**Returns:**
- `bool`

---

(getstaticsquarecolor)=
## `getStaticSquareColor`

**Signature:**
```cpp
Color getStaticSquareColor();
```

**Returns:**
- `Color`

---

(allowappearwalk)=
## `allowAppearWalk`

**Signature:**
```cpp
void allowAppearWalk(uint16_t stepSpeed);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16_t` | `stepSpeed` | - |

---

(iswalking)=
## `isWalking`

**Signature:**
```cpp
bool isWalking();
```

**Returns:**
- `bool`

---

(isremoved)=
## `isRemoved`

**Signature:**
```cpp
bool isRemoved();
```

**Returns:**
- `bool`

---

(isinvisible)=
## `isInvisible`

**Signature:**
```cpp
bool isInvisible();
```

**Returns:**
- `bool`

---

(isdead)=
## `isDead`

**Signature:**
```cpp
bool isDead();
```

**Returns:**
- `bool`

---

(canbeseen)=
## `canBeSeen`

**Signature:**
```cpp
bool canBeSeen();
```

**Returns:**
- `bool`

---

(iscreature)=
## `isCreature`

**Signature:**
```cpp
bool isCreature();
```

**Returns:**
- `bool`

---

(isprewalking)=
## `isPreWalking`

**Signature:**
```cpp
virtual bool isPreWalking();
```

**Returns:**
- `bool`

---

(getprewalkingposition)=
## `getPrewalkingPosition`

**Signature:**
```cpp
virtual Position getPrewalkingPosition(bool beforePrewalk = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `beforePrewalk` | `false` | - |

**Returns:**
- `Position`

---

(getwalkingtileortile)=
## `getWalkingTileOrTile`

**Signature:**
```cpp
TilePtr getWalkingTileOrTile();
```

**Returns:**
- `TilePtr`

---

(isserverwalking)=
## `isServerWalking`

**Signature:**
```cpp
virtual bool isServerWalking();
```

**Returns:**
- `bool`

---

(setelevation)=
## `setElevation`

**Signature:**
```cpp
void setElevation(uint8 elevation);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `elevation` | - |

---

(getelevation)=
## `getElevation`

**Signature:**
```cpp
uint8 getElevation();
```

**Returns:**
- `uint8`

---

(getprogressbarpercent)=
## `getProgressBarPercent`

**Signature:**
```cpp
uint8 getProgressBarPercent();
```

**Returns:**
- `uint8`

---

(isnpc)=
## `isNpc`

**Signature:**
```cpp
public: bool isNpc();
```

**Returns:**
- `bool`

---

(ismonster)=
## `isMonster`

**Signature:**
```cpp
public: bool isMonster();
```

**Returns:**
- `bool`

---
