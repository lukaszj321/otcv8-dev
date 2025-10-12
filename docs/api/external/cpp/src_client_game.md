# src/client/game.h

```cpp
public:
    Game();
```
```cpp
void init();
```
```cpp
void terminate();
```
```cpp
private:
    void resetGameStates();
```
```cpp
protected:
    void processConnectionError(const boost::system::error_code& error);
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
void cancelAttack() { attack(nullptr, true);
```
```cpp
void follow(CreaturePtr creature);
```
```cpp
void cancelFollow() { follow(nullptr);
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
Otc::ChaseModes getChaseMode() { return m_chaseMode; } Otc::FightModes getFightMode() { return m_fightMode; } bool isSafeFight() { return m_safeFight; } Otc::PVPModes getPVPMode() { return m_pvpMode; } // pvp related void setUnjustifiedPoints(UnjustifiedPoints unjustifiedPoints);
```
```cpp
UnjustifiedPoints getUnjustifiedPoints() { return m_unjustifiedPoints; }; void setOpenPvpSituations(int openPvpSitations);
```
```cpp
int getOpenPvpSituations() { return m_openPvpSituations; } // npc trade related void inspectNpcTrade(const ItemPtr& item);
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
void setPingDelay(int delay) { m_pingDelay = delay; } // otclient only void changeMapAwareRange(int xrange, int yrange);
```
```cpp
void resetFeatures() { m_features.reset();
```
```cpp
void enableFeature(Otc::GameFeature feature) { m_features.set(feature, true);
```
```cpp
void disableFeature(Otc::GameFeature feature) { m_features.set(feature, false);
```
```cpp
void setFeature(Otc::GameFeature feature, bool enabled) { m_features.set(feature, enabled);
```
```cpp
bool getFeature(Otc::GameFeature feature) { return m_features.test(feature);
```
```cpp
void setProtocolVersion(int version);
```
```cpp
int getProtocolVersion() { return m_protocolVersion; } void setCustomProtocolVersion(int version) { m_customProtocolVersion = version; } int getCustomProtocolVersion() { return m_customProtocolVersion != 0 ? m_customProtocolVersion : m_protocolVersion; } void setClientVersion(int version);
```
```cpp
int getClientVersion() { return m_clientVersion; } void setCustomOs(int os) { m_clientCustomOs = os; } int getOs();
```
```cpp
bool canPerformGameAction();
```
```cpp
bool checkBotProtection();
```
```cpp
bool isOnline() { return m_online; } bool isLogging() { return !m_online && m_protocolGame; } bool isDead() { return m_dead; } bool isAttacking() { return !!m_attackingCreature && !m_attackingCreature->isRemoved();
```
```cpp
bool isFollowing() { return !!m_followingCreature && !m_followingCreature->isRemoved();
```
```cpp
bool isConnectionOk() { return m_protocolGame && m_protocolGame->getElapsedTicksSinceLastRead() < 5000; } int getPing() { return m_ping; } ContainerPtr getContainer(int index) { if (m_containers.find(index) == m_containers.end()) { return nullptr; } return m_containers[index]; } std::map<int, ContainerPtr> getContainers() { return m_containers; } std::map<int, Vip> getVips() { return m_vips; } CreaturePtr getAttackingCreature() { return m_attackingCreature; } CreaturePtr getFollowingCreature() { return m_followingCreature; } void setServerBeat(int beat) { m_serverBeat = beat; } int getServerBeat() { return m_serverBeat; } void setCanReportBugs(bool enable) { m_canReportBugs = enable; } bool canReportBugs() { return m_canReportBugs; } void setExpertPvpMode(bool enable) { m_expertPvpMode = enable; } bool getExpertPvpMode() { return m_expertPvpMode; } LocalPlayerPtr getLocalPlayer() { return m_localPlayer; } ProtocolGamePtr getProtocolGame() { return m_protocolGame; } std::string getCharacterName() { return m_characterName; } std::string getWorldName() { return m_worldName; } std::vector<uint8> getGMActions() { return m_gmActions; } bool isGM() { return m_gmActions.size() > 0; } Otc::Direction getLastWalkDir() { return m_lastWalkDir; } std::string formatCreatureName(const std::string &name);
```
```cpp
int findEmptyContainerId();
```
```cpp
void setTibiaCoins(int coins, int transferableCoins) { m_coins = coins; m_transferableCoins = transferableCoins; } int getTibiaCoins() { return m_coins; } int getTransferableTibiaCoins() { return m_transferableCoins; } void setMaxPreWalkingSteps(uint value) { m_maxPreWalkingSteps = value; } uint getMaxPreWalkingSteps() { return m_maxPreWalkingSteps; } void showRealDirection(bool value) { m_showRealDirection = value; } bool shouldShowingRealDirection() { return m_showRealDirection; } uint getWalkId() { return m_walkId; } uint getWalkPreditionId() { return m_walkPrediction; } void ignoreServerDirection(bool value) { m_ignoreServerDirection = value; } bool isIgnoringServerDirection() { return m_ignoreServerDirection; } void enableTileThingLuaCallback(bool value) { m_tileThingsLuaCallback = value; } bool isTileThingLuaCallbackEnabled() { return m_tileThingsLuaCallback; } int getRecivedPacketsCount() { return m_protocolGame ? m_protocolGame->getRecivedPacketsCount() : 0; } int getRecivedPacketsSize() { return m_protocolGame ? m_protocolGame->getRecivedPacketsSize() : 0; } protected: void enableBotCall() { m_denyBotCall = false; } void disableBotCall() { m_denyBotCall = true; } private: void setAttackingCreature(const CreaturePtr& creature);
```
```cpp
void setFollowingCreature(const CreaturePtr& creature);
```