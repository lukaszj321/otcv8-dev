# src/client/game.h

```cpp
public: Game();
```
```cpp
void init();
```
```cpp
void terminate();
```
```cpp
private: void resetGameStates();
```
```cpp
protected: void processConnectionError(const boost::system::error_code& error);
```
```cpp
void processDisconnect();
```
```cpp
void processPing();
```
```cpp
void processPingBack();
```
```cpp
void processNewPing(uint32_t pingId);
```
```cpp
void processUpdateNeeded(const std::string& signature);
```
```cpp
void processLoginError(const std::string& error);
```
```cpp
void processLoginAdvice(const std::string& message);
```
```cpp
void processLoginWait(const std::string& message, int time);
```
```cpp
void processLoginToken(bool unknown);
```
```cpp
void processLogin();
```
```cpp
void processPendingGame();
```
```cpp
void processEnterGame();
```
```cpp
void processGameStart();
```
```cpp
void processGameEnd();
```
```cpp
void processDeath(int deathType, int penality);
```
```cpp
void processGMActions(const std::vector<uint8>& actions);
```
```cpp
void processInventoryChange(int slot, const ItemPtr& item);
```
```cpp
void processAttackCancel(uint seq);
```
```cpp
void processWalkCancel(Otc::Direction direction);
```
```cpp
void processNewWalkCancel(Otc::Direction dir);
```
```cpp
void processPredictiveWalkCancel(const Position& pos, Otc::Direction dir);
```
```cpp
void processWalkId(uint32_t walkId);
```
```cpp
void processPlayerHelpers(int helpers);
```
```cpp
void processPlayerModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeMode, Otc::PVPModes pvpMode);
```
```cpp
void processTextMessage(Otc::MessageMode mode, const std::string& text);
```
```cpp
void processTalk(const std::string& name, int level, Otc::MessageMode mode, const std::string& text, int channelId, const Position& pos);
```
```cpp
void processOpenContainer(int containerId, const ItemPtr& containerItem, const std::string& name, int capacity, bool hasParent, const std::vector<ItemPtr>& items, bool isUnlocked, bool hasPages, int containerSize, int firstIndex);
```
```cpp
void processCloseContainer(int containerId);
```
```cpp
void processContainerAddItem(int containerId, const ItemPtr& item, int slot);
```
```cpp
void processContainerUpdateItem(int containerId, int slot, const ItemPtr& item);
```
```cpp
void processContainerRemoveItem(int containerId, int slot, const ItemPtr& lastItem);
```
```cpp
void processChannelList(const std::vector<std::tuple<int, std::string> >& channelList);
```
```cpp
void processOpenChannel(int channelId, const std::string& name);
```
```cpp
void processOpenPrivateChannel(const std::string& name);
```
```cpp
void processOpenOwnPrivateChannel(int channelId, const std::string& name);
```
```cpp
void processCloseChannel(int channelId);
```
```cpp
void processRuleViolationChannel(int channelId);
```
```cpp
void processRuleViolationRemove(const std::string& name);
```
```cpp
void processRuleViolationCancel(const std::string& name);
```
```cpp
void processRuleViolationLock();
```
```cpp
void processVipAdd(uint id, const std::string& name, uint status, const std::string& description, int iconId, bool notifyLogin);
```
```cpp
void processVipStateChange(uint id, uint status);
```
```cpp
void processTutorialHint(int id);
```
```cpp
void processAddAutomapFlag(const Position& pos, int icon, const std::string& message);
```
```cpp
void processRemoveAutomapFlag(const Position& pos, int icon, const std::string& message);
```
```cpp
void processOpenOutfitWindow(const Outfit& currentOutfit, const std::vector<std::tuple<int, std::string, int>>& outfitList, const std::vector<std::tuple<int, std::string>>& mountList, const std::vector<std::tuple<int, std::string>>& wingList, const std::vector<std::tuple<int, std::string>>& auraList, const std::vector<std::tuple<int, std::string>>& shaderList, const std::vector<std::tuple<int, std::string>>& healthBarList, const std::vector<std::tuple<int, std::string>>& manaBarList);
```
```cpp
void processOpenNpcTrade(const std::vector<std::tuple<ItemPtr, std::string, int, int64_t, int64_t> >& items);
```
```cpp
void processPlayerGoods(uint64_t money, const std::vector<std::tuple<ItemPtr, int> >& goods);
```
```cpp
void processCloseNpcTrade();
```
```cpp
void processOwnTrade(const std::string& name, const std::vector<ItemPtr>& items);
```
```cpp
void processCounterTrade(const std::string& name, const std::vector<ItemPtr>& items);
```
```cpp
void processCloseTrade();
```
```cpp
void processEditText(uint id, int itemId, int maxLength, const std::string& text, const std::string& writer, const std::string& date);
```
```cpp
void processEditList(uint id, int doorId, const std::string& text);
```
```cpp
void processQuestLog(const std::vector<std::tuple<int, std::string, bool> >& questList);
```
```cpp
void processQuestLine(int questId, const std::vector<std::tuple<std::string, std::string, int> >& questMissions);
```
```cpp
void processModalDialog(uint32 id, std::string title, std::string message, std::vector<std::tuple<int, std::string> > buttonList, int enterButton, int escapeButton, std::vector<std::tuple<int, std::string> > choiceList, bool priority);
```
```cpp
void loginWorld(const std::string& account, const std::string& password, const std::string& worldName, const std::string& worldHost, int worldPort, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& recordTo = "");
```
```cpp
void playRecord(const std::string& file);
```
```cpp
void cancelLogin();
```
```cpp
void forceLogout();
```
```cpp
void safeLogout();
```
```cpp
void walk(Otc::Direction direction, bool withPreWalk);
```
```cpp
void autoWalk(const std::vector<Otc::Direction>& dirs, Position startPos);
```
```cpp
void turn(Otc::Direction direction);
```
```cpp
void stop();
```
```cpp
void look(const ThingPtr& thing, bool isBattleList = false);
```
```cpp
void move(const ThingPtr& thing, const Position& toPos, int count);
```
```cpp
void moveRaw(const Position& pos, int id, int stackpos, const Position& toPos, int count);
```
```cpp
void moveToParentContainer(const ThingPtr& thing, int count);
```
```cpp
void rotate(const ThingPtr& thing);
```
```cpp
void wrap(const ThingPtr& thing);
```
```cpp
void use(const ThingPtr& thing);
```
```cpp
void useWith(const ItemPtr& fromThing, const ThingPtr& toThing, int subType = 0);
```
```cpp
void useInventoryItem(int itemId, int subType = 0);
```
```cpp
void useInventoryItemWith(int itemId, const ThingPtr& toThing, int subType = 0);
```
```cpp
ItemPtr findItemInContainers(uint itemId, int subType);
```
```cpp
int open(const ItemPtr& item, const ContainerPtr& previousContainer);
```
```cpp
void openParent(const ContainerPtr& container);
```
```cpp
void close(const ContainerPtr& container);
```
```cpp
void refreshContainer(const ContainerPtr& container);
```
```cpp
void attack(CreaturePtr creature, bool cancel = false);
```
```cpp
void follow(CreaturePtr creature);
```
```cpp
void cancelAttackAndFollow();
```
```cpp
void talk(const std::string& message);
```
```cpp
void talkChannel(Otc::MessageMode mode, int channelId, const std::string& message);
```
```cpp
void talkPrivate(Otc::MessageMode mode, const std::string& receiver, const std::string& message);
```
```cpp
void openPrivateChannel(const std::string& receiver);
```
```cpp
void requestChannels();
```
```cpp
void joinChannel(int channelId);
```
```cpp
void leaveChannel(int channelId);
```
```cpp
void closeNpcChannel();
```
```cpp
void openOwnChannel();
```
```cpp
void inviteToOwnChannel(const std::string& name);
```
```cpp
void excludeFromOwnChannel(const std::string& name);
```
```cpp
void partyInvite(int creatureId);
```
```cpp
void partyJoin(int creatureId);
```
```cpp
void partyRevokeInvitation(int creatureId);
```
```cpp
void partyPassLeadership(int creatureId);
```
```cpp
void partyLeave();
```
```cpp
void partyShareExperience(bool active);
```
```cpp
void requestOutfit();
```
```cpp
void changeOutfit(const Outfit& outfit);
```
```cpp
void addVip(const std::string& name);
```
```cpp
void removeVip(int playerId);
```
```cpp
void editVip(int playerId, const std::string& description, int iconId, bool notifyLogin);
```
```cpp
void setChaseMode(Otc::ChaseModes chaseMode);
```
```cpp
void setFightMode(Otc::FightModes fightMode);
```
```cpp
void setSafeFight(bool on);
```
```cpp
void setPVPMode(Otc::PVPModes pvpMode);
```
```cpp
void setUnjustifiedPoints(UnjustifiedPoints unjustifiedPoints);
```
```cpp
void setOpenPvpSituations(int openPvpSitations);
```
```cpp
void inspectNpcTrade(const ItemPtr& item);
```
```cpp
void buyItem(const ItemPtr& item, int amount, bool ignoreCapacity, bool buyWithBackpack);
```
```cpp
void sellItem(const ItemPtr& item, int amount, bool ignoreEquipped);
```
```cpp
void closeNpcTrade();
```
```cpp
void requestTrade(const ItemPtr& item, const CreaturePtr& creature);
```
```cpp
void inspectTrade(bool counterOffer, int index);
```
```cpp
void acceptTrade();
```
```cpp
void rejectTrade();
```
```cpp
void editText(uint id, const std::string& text);
```
```cpp
void editList(uint id, int doorId, const std::string& text);
```
```cpp
void openRuleViolation(const std::string& reporter);
```
```cpp
void closeRuleViolation(const std::string& reporter);
```
```cpp
void cancelRuleViolation();
```
```cpp
void reportBug(const std::string& comment);
```
```cpp
void reportRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment);
```
```cpp
void debugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d);
```
```cpp
void requestQuestLog();
```
```cpp
void requestQuestLine(int questId);
```
```cpp
void equipItem(const ItemPtr& item);
```
```cpp
void equipItemId(int itemId, int subType);
```
```cpp
void mount(bool mount);
```
```cpp
void setOutfitExtensions(int mount, int wings, int aura, int shader, int healthBar, int manaBar);
```
```cpp
void requestItemInfo(const ItemPtr& item, int index);
```
```cpp
void answerModalDialog(uint32 dialog, int button, int choice);
```
```cpp
void browseField(const Position& position);
```
```cpp
void seekInContainer(int cid, int index);
```
```cpp
void buyStoreOffer(int offerId, int productType, const std::string& name = "");
```
```cpp
void requestTransactionHistory(int page, int entriesPerPage);
```
```cpp
void requestStoreOffers(const std::string& categoryName, int serviceType = 0);
```
```cpp
void openStore(int serviceType = 0);
```
```cpp
void transferCoins(const std::string& recipient, int amount);
```
```cpp
void openTransactionHistory(int entriesPerPage);
```
```cpp
void preyAction(int slot, int actionType, int index);
```
```cpp
void preyRequest();
```
```cpp
void applyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm);
```
```cpp
void clearImbuement(uint8_t slot);
```
```cpp
void closeImbuingWindow();
```
```cpp
void ping();
```
```cpp
void newPing();
```
```cpp
void changeMapAwareRange(int xrange, int yrange);
```
```cpp
void setProtocolVersion(int version);
```
```cpp
void setClientVersion(int version);
```
```cpp
int getOs();
```
```cpp
bool canPerformGameAction();
```
```cpp
bool checkBotProtection();
```
```cpp
std::string formatCreatureName(const std::string &name);
```
```cpp
int findEmptyContainerId();
```
```cpp
private: void setAttackingCreature(const CreaturePtr& creature);
```
```cpp
void setFollowingCreature(const CreaturePtr& creature);
```
```cpp
void cancelAttack();
```
```cpp
void cancelFollow();
```
```cpp
Otc::ChaseModes getChaseMode();
```
```cpp
Otc::FightModes getFightMode();
```
```cpp
bool isSafeFight();
```
```cpp
Otc::PVPModes getPVPMode();
```
```cpp
UnjustifiedPoints getUnjustifiedPoints();
```
```cpp
int getOpenPvpSituations();
```
```cpp
void setPingDelay(int delay);
```
```cpp
void resetFeatures();
```
```cpp
void enableFeature(Otc::GameFeature feature);
```
```cpp
void disableFeature(Otc::GameFeature feature);
```
```cpp
void setFeature(Otc::GameFeature feature, bool enabled);
```
```cpp
bool getFeature(Otc::GameFeature feature);
```
```cpp
int getProtocolVersion();
```
```cpp
void setCustomProtocolVersion(int version);
```
```cpp
int getCustomProtocolVersion();
```
```cpp
int getClientVersion();
```
```cpp
void setCustomOs(int os);
```
```cpp
bool isOnline();
```
```cpp
bool isLogging();
```
```cpp
bool isDead();
```
```cpp
bool isAttacking();
```
```cpp
bool isFollowing();
```
```cpp
bool isConnectionOk();
```
```cpp
int getPing();
```
```cpp
ContainerPtr getContainer(int index);
```
```cpp
CreaturePtr getAttackingCreature();
```
```cpp
CreaturePtr getFollowingCreature();
```
```cpp
void setServerBeat(int beat);
```
```cpp
int getServerBeat();
```
```cpp
void setCanReportBugs(bool enable);
```
```cpp
bool canReportBugs();
```
```cpp
void setExpertPvpMode(bool enable);
```
```cpp
bool getExpertPvpMode();
```
```cpp
LocalPlayerPtr getLocalPlayer();
```
```cpp
ProtocolGamePtr getProtocolGame();
```
```cpp
std::string getCharacterName();
```
```cpp
std::string getWorldName();
```
```cpp
std::vector<uint8> getGMActions();
```
```cpp
bool isGM();
```
```cpp
Otc::Direction getLastWalkDir();
```
```cpp
void setTibiaCoins(int coins, int transferableCoins);
```
```cpp
int getTibiaCoins();
```
```cpp
int getTransferableTibiaCoins();
```
```cpp
void setMaxPreWalkingSteps(uint value);
```
```cpp
uint getMaxPreWalkingSteps();
```
```cpp
void showRealDirection(bool value);
```
```cpp
bool shouldShowingRealDirection();
```
```cpp
uint getWalkId();
```
```cpp
uint getWalkPreditionId();
```
```cpp
void ignoreServerDirection(bool value);
```
```cpp
bool isIgnoringServerDirection();
```
```cpp
void enableTileThingLuaCallback(bool value);
```
```cpp
bool isTileThingLuaCallbackEnabled();
```
```cpp
int getRecivedPacketsCount();
```
```cpp
int getRecivedPacketsSize();
```
```cpp
protected: void enableBotCall();
```
```cpp
void disableBotCall();
```