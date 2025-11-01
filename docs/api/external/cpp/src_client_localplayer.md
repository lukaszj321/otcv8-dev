---
title: "src/client/localplayer.h"
source_file: "src/client/localplayer.h"
generated_at: "2025-11-01T08:29:23.679Z"
doc_type: "cpp_api"
---

# src/client/localplayer.h

(localplayer)=
## `LocalPlayer`

**Signature:**
```cpp
public: LocalPlayer();
```

---

(lockwalk)=
## `lockWalk`

**Signature:**
```cpp
void lockWalk(int millis = 200);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `millis` | `200` | - |

---

(stopautowalk)=
## `stopAutoWalk`

**Signature:**
```cpp
void stopAutoWalk();
```

---

(autowalk)=
## `autoWalk`

**Signature:**
```cpp
bool autoWalk(Position destination, bool retry = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Position` | `destination` |  | - |
| `bool` | `retry` | `false` | - |

**Returns:**
- `bool`

---

(canwalk)=
## `canWalk`

**Signature:**
```cpp
bool canWalk(Otc::Direction direction, bool ignoreLock = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Otc::Direction` | `direction` |  | - |
| `bool` | `ignoreLock` | `false` | - |

**Returns:**
- `bool`

---

(setstates)=
## `setStates`

**Signature:**
```cpp
void setStates(int states);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `states` | - |

---

(setskill)=
## `setSkill`

**Signature:**
```cpp
void setSkill(uint8_t skill, int level, int levelPercent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `skill` | - |
| `int` | `level` | - |
| `int` | `levelPercent` | - |

---

(setbaseskill)=
## `setBaseSkill`

**Signature:**
```cpp
void setBaseSkill(uint8_t skill, int baseLevel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `skill` | - |
| `int` | `baseLevel` | - |

---

(sethealth)=
## `setHealth`

**Signature:**
```cpp
void setHealth(double health, double maxHealth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `health` | - |
| `double` | `maxHealth` | - |

---

(setfreecapacity)=
## `setFreeCapacity`

**Signature:**
```cpp
void setFreeCapacity(double freeCapacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `freeCapacity` | - |

---

(settotalcapacity)=
## `setTotalCapacity`

**Signature:**
```cpp
void setTotalCapacity(double totalCapacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `totalCapacity` | - |

---

(setexperience)=
## `setExperience`

**Signature:**
```cpp
void setExperience(double experience);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `experience` | - |

---

(setlevel)=
## `setLevel`

**Signature:**
```cpp
void setLevel(double level, double levelPercent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `level` | - |
| `double` | `levelPercent` | - |

---

(setmana)=
## `setMana`

**Signature:**
```cpp
void setMana(double mana, double maxMana);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `mana` | - |
| `double` | `maxMana` | - |

---

(setmagiclevel)=
## `setMagicLevel`

**Signature:**
```cpp
void setMagicLevel(double magicLevel, double magicLevelPercent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `magicLevel` | - |
| `double` | `magicLevelPercent` | - |

---

(setbasemagiclevel)=
## `setBaseMagicLevel`

**Signature:**
```cpp
void setBaseMagicLevel(double baseMagicLevel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `baseMagicLevel` | - |

---

(setsoul)=
## `setSoul`

**Signature:**
```cpp
void setSoul(double soul);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `soul` | - |

---

(setstamina)=
## `setStamina`

**Signature:**
```cpp
void setStamina(double stamina);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `stamina` | - |

---

(setinventoryitem)=
## `setInventoryItem`

**Signature:**
```cpp
void setInventoryItem(Otc::InventorySlot inventory, const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::InventorySlot` | `inventory` | - |
| `const ItemPtr&` | `item` | - |

---

(setvocation)=
## `setVocation`

**Signature:**
```cpp
void setVocation(int vocation);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `vocation` | - |

---

(setpremium)=
## `setPremium`

**Signature:**
```cpp
void setPremium(bool premium);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `premium` | - |

---

(setregenerationtime)=
## `setRegenerationTime`

**Signature:**
```cpp
void setRegenerationTime(double regenerationTime);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `regenerationTime` | - |

---

(setofflinetrainingtime)=
## `setOfflineTrainingTime`

**Signature:**
```cpp
void setOfflineTrainingTime(double offlineTrainingTime);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `offlineTrainingTime` | - |

---

(setspells)=
## `setSpells`

**Signature:**
```cpp
void setSpells(const std::vector<int>& spells);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;int&gt;&` | `spells` | - |

---

(setblessings)=
## `setBlessings`

**Signature:**
```cpp
void setBlessings(int blessings);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `blessings` | - |

---

(hassight)=
## `hasSight`

**Signature:**
```cpp
bool hasSight(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `bool`

---

(prewalk)=
## `preWalk`

**Signature:**
```cpp
void preWalk(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(cancelwalk)=
## `cancelWalk`

**Signature:**
```cpp
void cancelWalk(Otc::Direction direction = Otc::InvalidDirection);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Otc::Direction` | `direction` | `Otc::InvalidDirection` | - |

---

(cancelnewwalk)=
## `cancelNewWalk`

**Signature:**
```cpp
void cancelNewWalk(Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `dir` | - |

---

(predictivecancelwalk)=
## `predictiveCancelWalk`

**Signature:**
```cpp
bool predictiveCancelWalk(const Position& pos, uint32_t predictionId, Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `uint32_t` | `predictionId` | - |
| `Otc::Direction` | `dir` | - |

**Returns:**
- `bool`

---

(retryautowalk)=
## `retryAutoWalk`

**Signature:**
```cpp
bool retryAutoWalk();
```

**Returns:**
- `bool`

---

(unlockwalk)=
## `unlockWalk`

**Signature:**
```cpp
void unlockWalk();
```

---

(iswalklocked)=
## `isWalkLocked`

**Signature:**
```cpp
bool isWalkLocked();
```

**Returns:**
- `bool`

---

(setknown)=
## `setKnown`

**Signature:**
```cpp
void setKnown(bool known);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `known` | - |

---

(setpendinggame)=
## `setPendingGame`

**Signature:**
```cpp
void setPendingGame(bool pending);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `pending` | - |

---

(getstates)=
## `getStates`

**Signature:**
```cpp
int getStates();
```

**Returns:**
- `int`

---

(getskilllevel)=
## `getSkillLevel`

**Signature:**
```cpp
int getSkillLevel(uint8_t skill);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `skill` | - |

**Returns:**
- `int`

---

(getskillbaselevel)=
## `getSkillBaseLevel`

**Signature:**
```cpp
int getSkillBaseLevel(uint8_t skill);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `skill` | - |

**Returns:**
- `int`

---

(getskilllevelpercent)=
## `getSkillLevelPercent`

**Signature:**
```cpp
int getSkillLevelPercent(uint8_t skill);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `skill` | - |

**Returns:**
- `int`

---

(getvocation)=
## `getVocation`

**Signature:**
```cpp
int getVocation();
```

**Returns:**
- `int`

---

(gethealth)=
## `getHealth`

**Signature:**
```cpp
double getHealth();
```

**Returns:**
- `double`

---

(getmaxhealth)=
## `getMaxHealth`

**Signature:**
```cpp
double getMaxHealth();
```

**Returns:**
- `double`

---

(getfreecapacity)=
## `getFreeCapacity`

**Signature:**
```cpp
double getFreeCapacity();
```

**Returns:**
- `double`

---

(gettotalcapacity)=
## `getTotalCapacity`

**Signature:**
```cpp
double getTotalCapacity();
```

**Returns:**
- `double`

---

(getexperience)=
## `getExperience`

**Signature:**
```cpp
double getExperience();
```

**Returns:**
- `double`

---

(getlevel)=
## `getLevel`

**Signature:**
```cpp
double getLevel();
```

**Returns:**
- `double`

---

(getlevelpercent)=
## `getLevelPercent`

**Signature:**
```cpp
double getLevelPercent();
```

**Returns:**
- `double`

---

(getmana)=
## `getMana`

**Signature:**
```cpp
double getMana();
```

**Returns:**
- `double`

---

(getmaxmana)=
## `getMaxMana`

**Signature:**
```cpp
double getMaxMana();
```

**Returns:**
- `double`

---

(getmagiclevel)=
## `getMagicLevel`

**Signature:**
```cpp
double getMagicLevel();
```

**Returns:**
- `double`

---

(getmagiclevelpercent)=
## `getMagicLevelPercent`

**Signature:**
```cpp
double getMagicLevelPercent();
```

**Returns:**
- `double`

---

(getbasemagiclevel)=
## `getBaseMagicLevel`

**Signature:**
```cpp
double getBaseMagicLevel();
```

**Returns:**
- `double`

---

(getsoul)=
## `getSoul`

**Signature:**
```cpp
double getSoul();
```

**Returns:**
- `double`

---

(getstamina)=
## `getStamina`

**Signature:**
```cpp
double getStamina();
```

**Returns:**
- `double`

---

(getregenerationtime)=
## `getRegenerationTime`

**Signature:**
```cpp
double getRegenerationTime();
```

**Returns:**
- `double`

---

(getofflinetrainingtime)=
## `getOfflineTrainingTime`

**Signature:**
```cpp
double getOfflineTrainingTime();
```

**Returns:**
- `double`

---

(getspells)=
## `getSpells`

**Signature:**
```cpp
std::vector<int> getSpells();
```

**Returns:**
- `std::vector&lt;int&gt;`

---

(getinventoryitem)=
## `getInventoryItem`

**Signature:**
```cpp
ItemPtr getInventoryItem(Otc::InventorySlot inventory);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::InventorySlot` | `inventory` | - |

**Returns:**
- `ItemPtr`

---

(getblessings)=
## `getBlessings`

**Signature:**
```cpp
int getBlessings();
```

**Returns:**
- `int`

---

(isknown)=
## `isKnown`

**Signature:**
```cpp
bool isKnown();
```

**Returns:**
- `bool`

---

(isautowalking)=
## `isAutoWalking`

**Signature:**
```cpp
bool isAutoWalking();
```

**Returns:**
- `bool`

---

(ispremium)=
## `isPremium`

**Signature:**
```cpp
bool isPremium();
```

**Returns:**
- `bool`

---

(ispendinggame)=
## `isPendingGame`

**Signature:**
```cpp
bool isPendingGame();
```

**Returns:**
- `bool`

---

(aslocalplayer)=
## `asLocalPlayer`

**Signature:**
```cpp
LocalPlayerPtr asLocalPlayer();
```

**Returns:**
- `LocalPlayerPtr`

---

(getwalkprediction)=
## `getWalkPrediction`

**Signature:**
```cpp
uint32_t getWalkPrediction(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `uint32_t`

---

(dumpwalkmatrix)=
## `dumpWalkMatrix`

**Signature:**
```cpp
std::string dumpWalkMatrix();
```

**Returns:**
- `std::string`

---

(startserverwalking)=
## `startServerWalking`

**Signature:**
```cpp
void startServerWalking();
```

---

(finishserverwalking)=
## `finishServerWalking`

**Signature:**
```cpp
void finishServerWalking();
```

---
