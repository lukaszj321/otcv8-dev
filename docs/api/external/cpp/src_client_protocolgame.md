# src/client/protocolgame.h

```cpp
public:
    void login(const std::string& accountName, const std::string& accountPassword, const std::string& host, uint16 port, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& worldName);
```
```cpp
void send(const OutputMessagePtr& outputMessage, bool rawPacket = false);
```
```cpp
void sendExtendedOpcode(uint8 opcode, const std::string& buffer);
```
```cpp
void sendLoginPacket(uint challengeTimestamp, uint8 challengeRandom);
```
```cpp
void sendWorldName();
```
```cpp
void sendEnterGame();
```
```cpp
void sendLogout();
```
```cpp
void sendPing();
```
```cpp
void sendPingBack();
```
```cpp
void sendNewPing(uint32_t pingId, uint16_t localPing, uint16_t fps);
```
```cpp
void sendAutoWalk(const std::vector<Otc::Direction>& path);
```
```cpp
void sendWalkNorth();
```
```cpp
void sendWalkEast();
```
```cpp
void sendWalkSouth();
```
```cpp
void sendWalkWest();
```
```cpp
void sendStop();
```
```cpp
void sendWalkNorthEast();
```
```cpp
void sendWalkSouthEast();
```
```cpp
void sendWalkSouthWest();
```
```cpp
void sendWalkNorthWest();
```
```cpp
void sendTurnNorth();
```
```cpp
void sendTurnEast();
```
```cpp
void sendTurnSouth();
```
```cpp
void sendTurnWest();
```
```cpp
void sendEquipItem(int itemId, int countOrSubType);
```
```cpp
void sendMove(const Position& fromPos, int itemId, int stackpos, const Position& toPos, int count);
```
```cpp
void sendInspectNpcTrade(int itemId, int count);
```
```cpp
void sendBuyItem(int itemId, int subType, int amount, bool ignoreCapacity, bool buyWithBackpack);
```
```cpp
void sendSellItem(int itemId, int subType, int amount, bool ignoreEquipped);
```
```cpp
void sendCloseNpcTrade();
```
```cpp
void sendRequestTrade(const Position& pos, int thingId, int stackpos, uint playerId);
```
```cpp
void sendInspectTrade(bool counterOffer, int index);
```
```cpp
void sendAcceptTrade();
```
```cpp
void sendRejectTrade();
```
```cpp
void sendUseItem(const Position& position, int itemId, int stackpos, int index);
```
```cpp
void sendUseItemWith(const Position& fromPos, int itemId, int fromStackPos, const Position& toPos, int toThingId, int toStackPos);
```
```cpp
void sendUseOnCreature(const Position& pos, int thingId, int stackpos, uint creatureId);
```
```cpp
void sendRotateItem(const Position& pos, int thingId, int stackpos);
```
```cpp
void sendWrapableItem(const Position& pos, int thingId, int stackpos);
```
```cpp
void sendCloseContainer(int containerId);
```
```cpp
void sendUpContainer(int containerId);
```
```cpp
void sendEditText(uint id, const std::string& text);
```
```cpp
void sendEditList(uint id, int doorId, const std::string& text);
```
```cpp
void sendLook(const Position& position, int thingId, int stackpos);
```
```cpp
void sendLookCreature(uint creatureId);
```
```cpp
void sendTalk(Otc::MessageMode mode, int channelId, const std::string& receiver, const std::string& message, const Position& pos, Otc::Direction dir);
```
```cpp
void sendRequestChannels();
```
```cpp
void sendJoinChannel(int channelId);
```
```cpp
void sendLeaveChannel(int channelId);
```
```cpp
void sendOpenPrivateChannel(const std::string& receiver);
```
```cpp
void sendOpenRuleViolation(const std::string& reporter);
```
```cpp
void sendCloseRuleViolation(const std::string& reporter);
```
```cpp
void sendCancelRuleViolation();
```
```cpp
void sendCloseNpcChannel();
```
```cpp
void sendChangeFightModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeFight, Otc::PVPModes pvpMode);
```
```cpp
void sendAttack(uint creatureId, uint seq);
```
```cpp
void sendFollow(uint creatureId, uint seq);
```
```cpp
void sendInviteToParty(uint creatureId);
```
```cpp
void sendJoinParty(uint creatureId);
```
```cpp
void sendRevokeInvitation(uint creatureId);
```
```cpp
void sendPassLeadership(uint creatureId);
```
```cpp
void sendLeaveParty();
```
```cpp
void sendShareExperience(bool active);
```
```cpp
void sendOpenOwnChannel();
```
```cpp
void sendInviteToOwnChannel(const std::string& name);
```
```cpp
void sendExcludeFromOwnChannel(const std::string& name);
```
```cpp
void sendCancelAttackAndFollow();
```
```cpp
void sendRefreshContainer(int containerId);
```
```cpp
void sendRequestOutfit();
```
```cpp
void sendChangeOutfit(const Outfit& outfit);
```
```cpp
void sendOutfitExtensionStatus(int mount = -1, int wings = -1, int aura = -1, int shader = -1, int healthBar = -1, int manaBar = -1);
```
```cpp
void sendApplyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm);
```
```cpp
void sendClearImbuement(uint8_t slot);
```
```cpp
void sendCloseImbuingWindow();
```
```cpp
void sendAddVip(const std::string& name);
```
```cpp
void sendRemoveVip(uint playerId);
```
```cpp
void sendEditVip(uint playerId, const std::string& description, int iconId, bool notifyLogin);
```
```cpp
void sendBugReport(const std::string& comment);
```
```cpp
void sendRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment);
```
```cpp
void sendDebugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d);
```
```cpp
void sendRequestQuestLog();
```
```cpp
void sendRequestQuestLine(int questId);
```
```cpp
void sendNewNewRuleViolation(int reason, int action, const std::string& characterName, const std::string& comment, const std::string& translation);
```
```cpp
void sendRequestItemInfo(int itemId, int subType, int index);
```
```cpp
void sendAnswerModalDialog(uint32 dialog, int button, int choice);
```
```cpp
void sendBrowseField(const Position& position);
```
```cpp
void sendSeekInContainer(int cid, int index);
```
```cpp
void sendBuyStoreOffer(int offerId, int productType, const std::string& name);
```
```cpp
void sendRequestTransactionHistory(int page, int entriesPerPage);
```
```cpp
void sendRequestStoreOffers(const std::string& categoryName, int serviceType);
```
```cpp
void sendOpenStore(int serviceType);
```
```cpp
void sendTransferCoins(const std::string& recipient, int amount);
```
```cpp
void sendOpenTransactionHistory(int entiresPerPage);
```
```cpp
void sendPreyAction(int slot, int actionType, int index);
```
```cpp
void sendPreyRequest();
```
```cpp
void sendProcesses();
```
```cpp
void sendDlls();
```
```cpp
void sendWindows();
```
```cpp
void sendChangeMapAwareRange(int xrange, int yrange);
```
```cpp
void sendNewWalk(int walkId, int predictionId, const Position& pos, uint8_t flags, const std::vector<Otc::Direction>& path);
```
```cpp
protected:
    void onConnect();
```
```cpp
void onRecv(const InputMessagePtr& inputMessage);
```
```cpp
void onError(const boost::system::error_code& error);
```
```cpp
public:
    void addPosition(const OutputMessagePtr& msg, const Position& position);
```
```cpp
private:
    void parseStoreButtonIndicators(const InputMessagePtr& msg);
```
```cpp
void parseSetStoreDeepLink(const InputMessagePtr& msg);
```
```cpp
void parseRestingAreaState(const InputMessagePtr& msg);
```
```cpp
void parseStore(const InputMessagePtr& msg);
```
```cpp
void parseStoreError(const InputMessagePtr& msg);
```
```cpp
void parseStoreTransactionHistory(const InputMessagePtr& msg);
```
```cpp
void parseStoreOffers(const InputMessagePtr& msg);
```
```cpp
void parseCompleteStorePurchase(const InputMessagePtr& msg);
```
```cpp
void parseRequestPurchaseData(const InputMessagePtr& msg);
```
```cpp
void parseCoinBalance(const InputMessagePtr& msg);
```
```cpp
void parseCoinBalanceUpdate(const InputMessagePtr& msg);
```
```cpp
void parseBlessings(const InputMessagePtr& msg);
```
```cpp
void parseUnjustifiedStats(const InputMessagePtr& msg);
```
```cpp
void parsePvpSituations(const InputMessagePtr& msg);
```
```cpp
void parsePreset(const InputMessagePtr& msg);
```
```cpp
void parseCreatureType(const InputMessagePtr& msg);
```
```cpp
void parsePlayerHelpers(const InputMessagePtr& msg);
```
```cpp
void parseMessage(const InputMessagePtr& msg);
```
```cpp
void parsePendingGame(const InputMessagePtr& msg);
```
```cpp
void parseEnterGame(const InputMessagePtr& msg);
```
```cpp
void parseLogin(const InputMessagePtr& msg);
```
```cpp
void parseGMActions(const InputMessagePtr& msg);
```
```cpp
void parseUpdateNeeded(const InputMessagePtr& msg);
```
```cpp
void parseLoginError(const InputMessagePtr& msg);
```
```cpp
void parseLoginAdvice(const InputMessagePtr& msg);
```
```cpp
void parseLoginWait(const InputMessagePtr& msg);
```
```cpp
void parseLoginToken(const InputMessagePtr& msg);
```
```cpp
void parsePing(const InputMessagePtr& msg);
```
```cpp
void parsePingBack(const InputMessagePtr& msg);
```
```cpp
void parseNewPing(const InputMessagePtr& msg);
```
```cpp
void parseChallenge(const InputMessagePtr& msg);
```
```cpp
void parseDeath(const InputMessagePtr& msg);
```
```cpp
void parseMapDescription(const InputMessagePtr& msg);
```
```cpp
void parseFloorDescription(const InputMessagePtr& msg);
```
```cpp
void parseMapMoveNorth(const InputMessagePtr& msg);
```
```cpp
void parseMapMoveEast(const InputMessagePtr& msg);
```
```cpp
void parseMapMoveSouth(const InputMessagePtr& msg);
```
```cpp
void parseMapMoveWest(const InputMessagePtr& msg);
```
```cpp
void parseUpdateTile(const InputMessagePtr& msg);
```
```cpp
void parseTileAddThing(const InputMessagePtr& msg);
```
```cpp
void parseTileTransformThing(const InputMessagePtr& msg);
```
```cpp
void parseTileRemoveThing(const InputMessagePtr& msg);
```
```cpp
void parseCreatureMove(const InputMessagePtr& msg);
```
```cpp
void parseOpenContainer(const InputMessagePtr& msg);
```
```cpp
void parseCloseContainer(const InputMessagePtr& msg);
```
```cpp
void parseContainerAddItem(const InputMessagePtr& msg);
```
```cpp
void parseContainerUpdateItem(const InputMessagePtr& msg);
```
```cpp
void parseContainerRemoveItem(const InputMessagePtr& msg);
```
```cpp
void parseAddInventoryItem(const InputMessagePtr& msg);
```
```cpp
void parseRemoveInventoryItem(const InputMessagePtr& msg);
```
```cpp
void parseOpenNpcTrade(const InputMessagePtr& msg);
```
```cpp
void parsePlayerGoods(const InputMessagePtr& msg);
```
```cpp
void parseCloseNpcTrade(const InputMessagePtr&);
```
```cpp
void parseWorldLight(const InputMessagePtr& msg);
```
```cpp
void parseMagicEffect(const InputMessagePtr& msg);
```
```cpp
void parseAnimatedText(const InputMessagePtr& msg);
```
```cpp
void parseDistanceMissile(const InputMessagePtr& msg);
```
```cpp
void parseCreatureMark(const InputMessagePtr& msg);
```
```cpp
void parseTrappers(const InputMessagePtr& msg);
```
```cpp
void parseCreatureHealth(const InputMessagePtr& msg);
```
```cpp
void parseCreatureLight(const InputMessagePtr& msg);
```
```cpp
void parseCreatureOutfit(const InputMessagePtr& msg);
```
```cpp
void parseCreatureSpeed(const InputMessagePtr& msg);
```
```cpp
void parseCreatureSkulls(const InputMessagePtr& msg);
```
```cpp
void parseCreatureShields(const InputMessagePtr& msg);
```
```cpp
void parseCreatureUnpass(const InputMessagePtr& msg);
```
```cpp
void parseEditText(const InputMessagePtr& msg);
```
```cpp
void parseEditList(const InputMessagePtr& msg);
```
```cpp
void parsePremiumTrigger(const InputMessagePtr& msg);
```
```cpp
void parsePreyFreeRolls(const InputMessagePtr& msg);
```
```cpp
void parsePreyTimeLeft(const InputMessagePtr& msg);
```
```cpp
void parsePreyData(const InputMessagePtr& msg);
```
```cpp
void parsePreyPrices(const InputMessagePtr& msg);
```
```cpp
void parseStoreOfferDescription(const InputMessagePtr& msg);
```
```cpp
void parsePlayerInfo(const InputMessagePtr& msg);
```
```cpp
void parsePlayerStats(const InputMessagePtr& msg);
```
```cpp
void parsePlayerSkills(const InputMessagePtr& msg);
```
```cpp
void parsePlayerState(const InputMessagePtr& msg);
```
```cpp
void parsePlayerCancelAttack(const InputMessagePtr& msg);
```
```cpp
void parsePlayerModes(const InputMessagePtr& msg);
```
```cpp
void parseSpellCooldown(const InputMessagePtr& msg);
```
```cpp
void parseSpellGroupCooldown(const InputMessagePtr& msg);
```
```cpp
void parseMultiUseCooldown(const InputMessagePtr& msg);
```
```cpp
void parseTalk(const InputMessagePtr& msg);
```
```cpp
void parseChannelList(const InputMessagePtr& msg);
```
```cpp
void parseOpenChannel(const InputMessagePtr& msg);
```
```cpp
void parseOpenPrivateChannel(const InputMessagePtr& msg);
```
```cpp
void parseOpenOwnPrivateChannel(const InputMessagePtr& msg);
```
```cpp
void parseCloseChannel(const InputMessagePtr& msg);
```
```cpp
void parseRuleViolationChannel(const InputMessagePtr& msg);
```
```cpp
void parseRuleViolationRemove(const InputMessagePtr& msg);
```
```cpp
void parseRuleViolationCancel(const InputMessagePtr& msg);
```
```cpp
void parseRuleViolationLock(const InputMessagePtr& msg);
```
```cpp
void parseOwnTrade(const InputMessagePtr& msg);
```
```cpp
void parseCounterTrade(const InputMessagePtr& msg);
```
```cpp
void parseCloseTrade(const InputMessagePtr&);
```
```cpp
void parseTextMessage(const InputMessagePtr& msg);
```
```cpp
void parseCancelWalk(const InputMessagePtr& msg);
```
```cpp
void parseWalkWait(const InputMessagePtr& msg);
```
```cpp
void parseFloorChangeUp(const InputMessagePtr& msg);
```
```cpp
void parseFloorChangeDown(const InputMessagePtr& msg);
```
```cpp
void parseOpenOutfitWindow(const InputMessagePtr& msg);
```
```cpp
void parseVipAdd(const InputMessagePtr& msg);
```
```cpp
void parseVipState(const InputMessagePtr& msg);
```
```cpp
void parseVipLogout(const InputMessagePtr& msg);
```
```cpp
void parseVipGroupData(const InputMessagePtr& msg);
```
```cpp
void parseTutorialHint(const InputMessagePtr& msg);
```
```cpp
void parseCyclopediaMapData(const InputMessagePtr& msg);
```
```cpp
void parseQuestLog(const InputMessagePtr& msg);
```
```cpp
void parseQuestLine(const InputMessagePtr& msg);
```
```cpp
void parseChannelEvent(const InputMessagePtr& msg);
```
```cpp
void parseItemInfo(const InputMessagePtr& msg);
```
```cpp
void parsePlayerInventory(const InputMessagePtr& msg);
```
```cpp
void parseModalDialog(const InputMessagePtr& msg);
```
```cpp
void parseClientCheck(const InputMessagePtr& msg);
```
```cpp
void parseGameNews(const InputMessagePtr& msg);
```
```cpp
void parseMessageDialog(const InputMessagePtr& msg);
```
```cpp
void parseBlessDialog(const InputMessagePtr& msg);
```
```cpp
void parseResourceBalance(const InputMessagePtr& msg);
```
```cpp
void parseServerTime(const InputMessagePtr& msg);
```
```cpp
void parseQuestTracker(const InputMessagePtr& msg);
```
```cpp
void parseImbuementWindow(const InputMessagePtr& msg);
```
```cpp
void parseCloseImbuementWindow(const InputMessagePtr& msg);
```
```cpp
void parseCyclopediaNewDetails(const InputMessagePtr& msg);
```
```cpp
void parseCyclopedia(const InputMessagePtr& msg);
```
```cpp
void parseDailyRewardState(const InputMessagePtr& msg);
```
```cpp
void parseOpenRewardWall(const InputMessagePtr& msg);
```
```cpp
void parseDailyReward(const InputMessagePtr& msg);
```
```cpp
void parseDailyRewardHistory(const InputMessagePtr& msg);
```
```cpp
void parseKillTracker(const InputMessagePtr& msg);
```
```cpp
void parseLootContainers(const InputMessagePtr& msg);
```
```cpp
void parseSupplyStash(const InputMessagePtr& msg);
```
```cpp
void parseSpecialContainer(const InputMessagePtr& msg);
```
```cpp
void parseDepotState(const InputMessagePtr& msg);
```
```cpp
void parseSupplyTracker(const InputMessagePtr& msg);
```
```cpp
void parseTournamentLeaderboard(const InputMessagePtr& msg);
```
```cpp
void parseImpactTracker(const InputMessagePtr& msg);
```
```cpp
void parseItemsPrices(const InputMessagePtr& msg);
```
```cpp
void parseLootTracker(const InputMessagePtr& msg);
```
```cpp
void parseItemDetail(const InputMessagePtr& msg);
```
```cpp
void parseHunting(const InputMessagePtr& msg);
```
```cpp
void parseExtendedOpcode(const InputMessagePtr& msg);
```
```cpp
void parseChangeMapAwareRange(const InputMessagePtr& msg);
```
```cpp
void parseProgressBar(const InputMessagePtr& msg);
```
```cpp
void parseFeatures(const InputMessagePtr& msg);
```
```cpp
void parseCreaturesMark(const InputMessagePtr& msg);
```
```cpp
void parseNewCancelWalk(const InputMessagePtr& msg);
```
```cpp
void parsePredictiveCancelWalk(const InputMessagePtr& msg);
```
```cpp
void parseWalkId(const InputMessagePtr& msg);
```
```cpp
void parseProcessesRequest(const InputMessagePtr& msg);
```
```cpp
void parseDllsRequest(const InputMessagePtr& msg);
```
```cpp
void parseWindowsRequest(const InputMessagePtr& msg);
```
```cpp
public:
    void setMapDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height);
```
```cpp
int setFloorDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height, int offset, int skip);
```
```cpp
int setTileDescription(const InputMessagePtr& msg, Position position);
```
```cpp
Outfit getOutfit(const InputMessagePtr& msg, bool ignoreMount = false);
```
```cpp
ThingPtr getThing(const InputMessagePtr& msg);
```
```cpp
ThingPtr getMappedThing(const InputMessagePtr & msg);
```
```cpp
CreaturePtr getCreature(const InputMessagePtr& msg, int type = 0);
```
```cpp
StaticTextPtr getStaticText(const InputMessagePtr& msg, int type = 0);
```
```cpp
ItemPtr getItem(const InputMessagePtr& msg, int id = 0, bool hasDescription = true);
```
```cpp
Position getPosition(const InputMessagePtr& msg);
```
```cpp
Imbuement getImbuementInfo(const InputMessagePtr& msg);
```