---
title: "src/client/tile.h"
source_file: "src/client/tile.h"
generated_at: "2025-10-31T23:33:30.329Z"
doc_type: "cpp_api"
---

# src/client/tile.h

(calculatecorpsecorrection)=
## `calculateCorpseCorrection`

**Signature:**
```cpp
void calculateCorpseCorrection();
```

---

(drawground)=
## `drawGround`

**Signature:**
```cpp
void drawGround(const Point& dest, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `LightView* lightView =` | `nullptr` | - |

---

(drawbottom)=
## `drawBottom`

**Signature:**
```cpp
void drawBottom(const Point& dest, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `LightView* lightView =` | `nullptr` | - |

---

(drawcreatures)=
## `drawCreatures`

**Signature:**
```cpp
void drawCreatures(const Point& dest, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `LightView* lightView =` | `nullptr` | - |

---

(drawtop)=
## `drawTop`

**Signature:**
```cpp
void drawTop(const Point& dest, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `dest` | - |
| `LightView* lightView =` | `nullptr` | - |

---

(drawtexts)=
## `drawTexts`

**Signature:**
```cpp
void drawTexts(Point dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `dest` | - |

---

(drawwidget)=
## `drawWidget`

**Signature:**
```cpp
void drawWidget(Point dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `dest` | - |

---

(clean)=
## `clean`

**Signature:**
```cpp
public: void clean();
```

**Returns:**
- `public: void`

---

(addwalkingcreature)=
## `addWalkingCreature`

**Signature:**
```cpp
void addWalkingCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(removewalkingcreature)=
## `removeWalkingCreature`

**Signature:**
```cpp
void removeWalkingCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(addthing)=
## `addThing`

**Signature:**
```cpp
void addThing(const ThingPtr& thing, int stackPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |
| `int` | `stackPos` | - |

---

(removething)=
## `removeThing`

**Signature:**
```cpp
bool removeThing(ThingPtr thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ThingPtr` | `thing` | - |

**Returns:**
- `bool`

---

(getthing)=
## `getThing`

**Signature:**
```cpp
ThingPtr getThing(int stackPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `stackPos` | - |

**Returns:**
- `ThingPtr`

---

(geteffect)=
## `getEffect`

**Signature:**
```cpp
EffectPtr getEffect(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

**Returns:**
- `EffectPtr`

---

(hasthing)=
## `hasThing`

**Signature:**
```cpp
bool hasThing(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

**Returns:**
- `bool`

---

(getthingstackpos)=
## `getThingStackPos`

**Signature:**
```cpp
int getThingStackPos(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

**Returns:**
- `int`

---

(gettopthing)=
## `getTopThing`

**Signature:**
```cpp
ThingPtr getTopThing();
```

**Returns:**
- `ThingPtr`

---

(gettoplookthing)=
## `getTopLookThing`

**Signature:**
```cpp
ThingPtr getTopLookThing();
```

**Returns:**
- `ThingPtr`

---

(gettoplookthingex)=
## `getTopLookThingEx`

**Signature:**
```cpp
ThingPtr getTopLookThingEx(Point offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `offset` | - |

**Returns:**
- `ThingPtr`

---

(gettopusething)=
## `getTopUseThing`

**Signature:**
```cpp
ThingPtr getTopUseThing();
```

**Returns:**
- `ThingPtr`

---

(gettopcreature)=
## `getTopCreature`

**Signature:**
```cpp
CreaturePtr getTopCreature();
```

**Returns:**
- `CreaturePtr`

---

(gettopcreatureex)=
## `getTopCreatureEx`

**Signature:**
```cpp
CreaturePtr getTopCreatureEx(Point offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `offset` | - |

**Returns:**
- `CreaturePtr`

---

(gettopmovething)=
## `getTopMoveThing`

**Signature:**
```cpp
ThingPtr getTopMoveThing();
```

**Returns:**
- `ThingPtr`

---

(gettopmultiusething)=
## `getTopMultiUseThing`

**Signature:**
```cpp
ThingPtr getTopMultiUseThing();
```

**Returns:**
- `ThingPtr`

---

(gettopmultiusethingex)=
## `getTopMultiUseThingEx`

**Signature:**
```cpp
ThingPtr getTopMultiUseThingEx(Point offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Point` | `offset` | - |

**Returns:**
- `ThingPtr`

---

(getitems)=
## `getItems`

**Signature:**
```cpp
std::vector<ItemPtr> getItems();
```

**Returns:**
- `std::vector&lt;ItemPtr&gt;`

---

(getcreatures)=
## `getCreatures`

**Signature:**
```cpp
std::vector<CreaturePtr> getCreatures();
```

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getground)=
## `getGround`

**Signature:**
```cpp
ItemPtr getGround();
```

**Returns:**
- `ItemPtr`

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

(getminimapcolorbyte)=
## `getMinimapColorByte`

**Signature:**
```cpp
uint8 getMinimapColorByte();
```

**Returns:**
- `uint8`

---

(ispathable)=
## `isPathable`

**Signature:**
```cpp
bool isPathable();
```

**Returns:**
- `bool`

---

(iswalkable)=
## `isWalkable`

**Signature:**
```cpp
bool isWalkable(bool ignoreCreatures = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool ignoreCreatures =` | `false` | - |

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

(isfullyopaque)=
## `isFullyOpaque`

**Signature:**
```cpp
bool isFullyOpaque();
```

**Returns:**
- `bool`

---

(issingledimension)=
## `isSingleDimension`

**Signature:**
```cpp
bool isSingleDimension();
```

**Returns:**
- `bool`

---

(islookpossible)=
## `isLookPossible`

**Signature:**
```cpp
bool isLookPossible();
```

**Returns:**
- `bool`

---

(isblockingprojectile)=
## `isBlockingProjectile`

**Signature:**
```cpp
bool isBlockingProjectile();
```

**Returns:**
- `bool`

---

(isclickable)=
## `isClickable`

**Signature:**
```cpp
bool isClickable();
```

**Returns:**
- `bool`

---

(isempty)=
## `isEmpty`

**Signature:**
```cpp
bool isEmpty();
```

**Returns:**
- `bool`

---

(isdrawable)=
## `isDrawable`

**Signature:**
```cpp
bool isDrawable();
```

**Returns:**
- `bool`

---

(musthooksouth)=
## `mustHookSouth`

**Signature:**
```cpp
bool mustHookSouth();
```

**Returns:**
- `bool`

---

(musthookeast)=
## `mustHookEast`

**Signature:**
```cpp
bool mustHookEast();
```

**Returns:**
- `bool`

---

(hascreature)=
## `hasCreature`

**Signature:**
```cpp
bool hasCreature();
```

**Returns:**
- `bool`

---

(hasblockingcreature)=
## `hasBlockingCreature`

**Signature:**
```cpp
bool hasBlockingCreature();
```

**Returns:**
- `bool`

---

(limitsfloorsview)=
## `limitsFloorsView`

**Signature:**
```cpp
bool limitsFloorsView(bool isFreeView = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool isFreeView =` | `false` | - |

**Returns:**
- `bool`

---

(canerase)=
## `canErase`

**Signature:**
```cpp
bool canErase();
```

**Returns:**
- `bool`

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

(haselevation)=
## `hasElevation`

**Signature:**
```cpp
bool hasElevation(int elevation = 1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `elevation` | Default: `1` |

**Returns:**
- `bool`

---

(settext)=
## `setText`

**Signature:**
```cpp
void setText(const std::string& text, Color color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `text` | - |
| `Color` | `color` | - |

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

(settimer)=
## `setTimer`

**Signature:**
```cpp
void setTimer(int time, Color color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `time` | - |
| `Color` | `color` | - |

---

(gettimer)=
## `getTimer`

**Signature:**
```cpp
int getTimer();
```

**Returns:**
- `int`

---

(setfill)=
## `setFill`

**Signature:**
```cpp
void setFill(Color color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Color` | `color` | - |

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

(checktranslucentlight)=
## `checkTranslucentLight`

**Signature:**
```cpp
private: void checkTranslucentLight();
```

**Returns:**
- `private: void`

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
const Position& getPosition();
```

**Returns:**
- `const Position&`

---

(getdrawelevation)=
## `getDrawElevation`

**Signature:**
```cpp
int getDrawElevation();
```

**Returns:**
- `int`

---

(getwalkingcreatures)=
## `getWalkingCreatures`

**Signature:**
```cpp
std::vector<CreaturePtr> getWalkingCreatures();
```

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getthings)=
## `getThings`

**Signature:**
```cpp
std::vector<ThingPtr> getThings();
```

**Returns:**
- `std::vector&lt;ThingPtr&gt;`

---

(geteffects)=
## `getEffects`

**Signature:**
```cpp
std::vector<EffectPtr> getEffects();
```

**Returns:**
- `std::vector&lt;EffectPtr&gt;`

---

(isblocking)=
## `isBlocking`

**Signature:**
```cpp
bool isBlocking();
```

**Returns:**
- `bool`

---

(getthingcount)=
## `getThingCount`

**Signature:**
```cpp
int getThingCount();
```

**Returns:**
- `int`

---

(hastranslucentlight)=
## `hasTranslucentLight`

**Signature:**
```cpp
bool hasTranslucentLight();
```

**Returns:**
- `bool`

---

(overwriteminimapcolor)=
## `overwriteMinimapColor`

**Signature:**
```cpp
void overwriteMinimapColor(uint8 color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `color` | - |

---

(remflag)=
## `remFlag`

**Signature:**
```cpp
void remFlag(uint32 flag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `flag` | - |

---

(setflag)=
## `setFlag`

**Signature:**
```cpp
void setFlag(uint32 flag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `flag` | - |

---

(setflags)=
## `setFlags`

**Signature:**
```cpp
void setFlags(uint32 flags);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `flags` | - |

---

(hasflag)=
## `hasFlag`

**Signature:**
```cpp
bool hasFlag(uint32 flag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `flag` | - |

**Returns:**
- `bool`

---

(getflags)=
## `getFlags`

**Signature:**
```cpp
uint32 getFlags();
```

**Returns:**
- `uint32`

---

(sethouseid)=
## `setHouseId`

**Signature:**
```cpp
void setHouseId(uint32 hid);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `hid` | - |

---

(gethouseid)=
## `getHouseId`

**Signature:**
```cpp
uint32 getHouseId();
```

**Returns:**
- `uint32`

---

(ishousetile)=
## `isHouseTile`

**Signature:**
```cpp
bool isHouseTile();
```

**Returns:**
- `bool`

---

(select)=
## `select`

**Signature:**
```cpp
void select();
```

---

(unselect)=
## `unselect`

**Signature:**
```cpp
void unselect();
```

---

(isselected)=
## `isSelected`

**Signature:**
```cpp
bool isSelected();
```

**Returns:**
- `bool`

---

(astile)=
## `asTile`

**Signature:**
```cpp
TilePtr asTile();
```

**Returns:**
- `TilePtr`

---

(setspeed)=
## `setSpeed`

**Signature:**
```cpp
void setSpeed(uint16_t speed, uint8_t blocking);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16_t` | `speed` | - |
| `uint8_t` | `blocking` | - |

---

(resetfill)=
## `resetFill`

**Signature:**
```cpp
void resetFill();
```

---

(setwidget)=
## `setWidget`

**Signature:**
```cpp
void setWidget(UIWidgetPtr widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `widget` | - |

---

(getwidget)=
## `getWidget`

**Signature:**
```cpp
UIWidgetPtr getWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(removewidget)=
## `removeWidget`

**Signature:**
```cpp
void removeWidget();
```

---
