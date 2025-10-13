# src/client/localplayer.h

```cpp
public: LocalPlayer();
```
```cpp
void lockWalk(int millis = 200);
```
```cpp
void stopAutoWalk();
```
```cpp
bool autoWalk(Position destination, bool retry = false);
```
```cpp
bool canWalk(Otc::Direction direction, bool ignoreLock = false);
```
```cpp
void setStates(int states);
```
```cpp
void setSkill(uint8_t skill, int level, int levelPercent);
```
```cpp
void setBaseSkill(uint8_t skill, int baseLevel);
```
```cpp
void setHealth(double health, double maxHealth);
```
```cpp
void setFreeCapacity(double freeCapacity);
```
```cpp
void setTotalCapacity(double totalCapacity);
```
```cpp
void setExperience(double experience);
```
```cpp
void setLevel(double level, double levelPercent);
```
```cpp
void setMana(double mana, double maxMana);
```
```cpp
void setMagicLevel(double magicLevel, double magicLevelPercent);
```
```cpp
void setBaseMagicLevel(double baseMagicLevel);
```
```cpp
void setSoul(double soul);
```
```cpp
void setStamina(double stamina);
```
```cpp
void setInventoryItem(Otc::InventorySlot inventory, const ItemPtr& item);
```
```cpp
void setVocation(int vocation);
```
```cpp
void setPremium(bool premium);
```
```cpp
void setRegenerationTime(double regenerationTime);
```
```cpp
void setOfflineTrainingTime(double offlineTrainingTime);
```
```cpp
void setSpells(const std::vector<int>& spells);
```
```cpp
void setBlessings(int blessings);
```
```cpp
bool hasSight(const Position& pos);
```
```cpp
void preWalk(Otc::Direction direction);
```
```cpp
void cancelWalk(Otc::Direction direction = Otc::InvalidDirection);
```
```cpp
void cancelNewWalk(Otc::Direction dir);
```
```cpp
bool predictiveCancelWalk(const Position& pos, uint32_t predictionId, Otc::Direction dir);
```
```cpp
bool retryAutoWalk();
```
```cpp
void unlockWalk();
```
```cpp
bool isWalkLocked();
```
```cpp
void setKnown(bool known);
```
```cpp
void setPendingGame(bool pending);
```
```cpp
int getStates();
```
```cpp
int getSkillLevel(uint8_t skill);
```
```cpp
int getSkillBaseLevel(uint8_t skill);
```
```cpp
int getSkillLevelPercent(uint8_t skill);
```
```cpp
int getVocation();
```
```cpp
double getHealth();
```
```cpp
double getMaxHealth();
```
```cpp
double getFreeCapacity();
```
```cpp
double getTotalCapacity();
```
```cpp
double getExperience();
```
```cpp
double getLevel();
```
```cpp
double getLevelPercent();
```
```cpp
double getMana();
```
```cpp
double getMaxMana();
```
```cpp
double getMagicLevel();
```
```cpp
double getMagicLevelPercent();
```
```cpp
double getBaseMagicLevel();
```
```cpp
double getSoul();
```
```cpp
double getStamina();
```
```cpp
double getRegenerationTime();
```
```cpp
double getOfflineTrainingTime();
```
```cpp
std::vector<int> getSpells();
```
```cpp
ItemPtr getInventoryItem(Otc::InventorySlot inventory);
```
```cpp
int getBlessings();
```
```cpp
bool isKnown();
```
```cpp
bool isAutoWalking();
```
```cpp
bool isPremium();
```
```cpp
bool isPendingGame();
```
```cpp
LocalPlayerPtr asLocalPlayer();
```
```cpp
uint32_t getWalkPrediction(const Position& pos);
```
```cpp
std::string dumpWalkMatrix();
```
```cpp
void startServerWalking();
```
```cpp
void finishServerWalking();
```