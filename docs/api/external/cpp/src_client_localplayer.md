# src/client/localplayer.h

```cpp
public:
    LocalPlayer();
```
```cpp
void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr) override; void unlockWalk() { m_walkLockExpiration = 0; } void lockWalk(int millis = 200);
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
bool isWalkLocked() { return (m_walkLockExpiration != 0 && g_clock.millis() < m_walkLockExpiration);
```
```cpp
void turn(Otc::Direction) override; void setStates(int states);
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
void setKnown(bool known) { m_known = known; } void setPendingGame(bool pending) { m_pending = pending; } void setInventoryItem(Otc::InventorySlot inventory, const ItemPtr& item);
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
int getStates() { return m_states; } int getSkillLevel(uint8_t skill) { return skill < m_skillsLevel.size() ? m_skillsLevel[skill] : 0; } int getSkillBaseLevel(uint8_t skill) { return skill < m_skillsBaseLevel.size() ? m_skillsBaseLevel[skill] : 0; } int getSkillLevelPercent(uint8_t skill) { return skill < m_skillsLevelPercent.size() ? m_skillsLevelPercent[skill] : 0; } int getVocation() { return m_vocation; } double getHealth() { return m_health; } double getMaxHealth() { return m_maxHealth; } double getFreeCapacity() { return m_freeCapacity; } double getTotalCapacity() { return m_totalCapacity; } double getExperience() { return m_experience; } double getLevel() { return m_level; } double getLevelPercent() { return m_levelPercent; } double getMana() { return m_mana; } double getMaxMana() { return std::max<double>(m_mana, m_maxMana);
```
```cpp
double getMagicLevel() { return m_magicLevel; } double getMagicLevelPercent() { return m_magicLevelPercent; } double getBaseMagicLevel() { return m_baseMagicLevel; } double getSoul() { return m_soul; } double getStamina() { return m_stamina; } double getRegenerationTime() { return m_regenerationTime; } double getOfflineTrainingTime() { return m_offlineTrainingTime; } std::vector<int> getSpells() { return m_spells; } ItemPtr getInventoryItem(Otc::InventorySlot inventory) { return m_inventoryItems[inventory]; } int getBlessings() { return m_blessings; } bool hasSight(const Position& pos);
```
```cpp
bool isKnown() { return m_known; } bool isAutoWalking() { return m_autoWalkDestination.isValid();
```
```cpp
bool isServerWalking() override { return m_serverWalking; } bool isPremium() { return m_premium; } bool isPendingGame() { return m_pending; } LocalPlayerPtr asLocalPlayer() { return static_self_cast<LocalPlayer>();
```
```cpp
bool isLocalPlayer() override { return true; } void onAppear() override; void onPositionChange(const Position& newPos, const Position& oldPos) override; // pre walking void preWalk(Otc::Direction direction);
```
```cpp
bool isPreWalking() override { return !m_preWalking.empty();
```
```cpp
Position getPrewalkingPosition(bool beforePrewalk = false) override { if(m_preWalking.empty()) return m_position; else if (!beforePrewalk && m_preWalking.size() == 1) return m_position; auto ret = m_preWalking.rbegin();
```
```cpp
uint32_t getWalkPrediction(const Position& pos) { return m_walkMatrix.get(pos);
```
```cpp
std::string dumpWalkMatrix() { return m_walkMatrix.dump();
```
```cpp
void startServerWalking() { m_serverWalking = true; } void finishServerWalking() { m_serverWalking = false; } protected: void walk(const Position& oldPos, const Position& newPos) override; void cancelWalk(Otc::Direction direction = Otc::InvalidDirection);
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