# Client Overview (Game Logic, Entities, Map)

Poniżej znajduje się przegląd klas i metod z folderu `client/`, odpowiedzialnych za logikę gry, gracza, mapę, efekty, kreatury i inne systemy w grze.


## client/animatedtext.cpp

- `rect(p, textSize)`

## client/animatedtext.h

class AnimatedText
- `AnimatedText()`
- `drawText(const Point& dest, const Rect& visibleRect)`
- `setColor(int color)`
- `setText(const std::string& text)`
- `setOffset(const Point& offset)`
- `setFont(const std::string& fontName)`
- `getColor()`
- `getOffset()`
- `getTimer()`
- `merge(const AnimatedTextPtr& other)`
- `asAnimatedText()`
- `isAnimatedText()`
- `getText()`
- `onAppear()`

## client/animator.cpp

- `calculateSynchronous()`

## client/animator.h

class Animator
- `Animator()`
- `unserialize(int animationPhases, const FileStreamPtr& fin)`
- `serialize(const FileStreamPtr& fin)`
- `setPhase(int phase)`
- `getPhase()`
- `getPhaseAt(Timer& timer, int lastPhase = 0)`
- `getStartPhase()`
- `getAnimationPhases()`
- `isAsync()`
- `isComplete()`
- `getTotalDuration()`
- `resetAnimation()`
- `getPingPongPhase()`
- `getLoopPhase()`
- `getPhaseDuration(int phase)`
- `calculateSynchronous()`

## client/client.cpp

- `registerLuaFunctions()`

## client/client.h

class Client
- `init(std::vector<std::string>& args)`
- `terminate()`
- `registerLuaFunctions()`

## client/container.h

class Container
class Game
- `Container(int id, int capacity, const std::string& name, const ItemPtr& containerItem, bool hasParent, bool isUnlocked, bool hasPages, int containerSize, int firstIndex)`
- `getItem(int slot)`
- `getItems()`
- `getItemsCount()`
- `getSlotPosition(int slot)`
- `Position(0xffff, m_id | 0x40, slot)`
- `getId()`
- `getCapacity()`
- `getContainerItem()`
- `getName()`
- `hasParent()`
- `isClosed()`
- `isUnlocked()`
- `hasPages()`
- `getSize()`
- `getFirstIndex()`
- `findItemById(uint itemId, int subType)`
- `onOpen(const ContainerPtr& previousContainer)`
- `onClose()`
- `onAddItem(const ItemPtr& item, int slot)`
- `onAddItems(const std::vector<ItemPtr>& items)`
- `onUpdateItem(int slot, const ItemPtr& item)`
- `onRemoveItem(int slot, const ItemPtr& lastItem)`
- `updateItemsPositions()`

## client/creature.cpp

- `rect(getDrawOffset() - (m_walking ? m_walkOffset : Point(0,0)), Size(Otc::TILE_PIXELS - getDisplacementY(), Otc::TILE_PIXELS - getDisplacementX()))`
- `rect(getDrawOffset() - getDisplacement(), Size(g_sprites.spriteSize(), g_sprites.spriteSize()))`
- `setDirection(m_lastStepDirection)`
- `nextWalkUpdate()`
- `terminateWalk()`
- `getAnimationPhases()`
- `getAnimator()->getAnimationPhases() + (g_game.getFeature(Otc::GameIdleAnimations) ? 1 : 0)`
- `virtualTileRect((xi + 1) * g_sprites.spriteSize(), (yi + 1) * g_sprites.spriteSize(), g_sprites.spriteSize(), g_sprites.spriteSize())`
- `updateWalk()`
- `updateWalkAnimation(totalPixelsWalked)`
- `Point(8, 8) * g_sprites.getOffsetFactor()`
- `Point(0, 0)`
- `StaticText())`

## client/creature.h

class Creature
class Npc
class Monster
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `drawOutfit(const Rect& destRect, Otc::Direction direction = Otc::InvalidDirection, const Color& color = Color::white, bool animate = false, bool ui = false, bool oldScaling = false)`
- `drawInformation(const Point& point, bool useGray, const Rect& parentRect, int drawFlags)`
- `isInsideOffset(Point offset)`
- `setId(uint32 id)`
- `setName(const std::string& name)`
- `setManaPercent(int8 value)`
- `setHealthPercent(uint8 healthPercent)`
- `setDirection(Otc::Direction direction)`
- `setOutfit(const Outfit& outfit)`
- `setOutfitColor(const Color& color, int duration)`
- `setLight(const Light& light)`
- `setSpeed(uint16 speed)`
- `setBaseSpeed(double baseSpeed)`
- `setSkull(uint8 skull)`
- `setShield(uint8 shield)`
- `setEmblem(uint8 emblem)`
- `setType(uint8 type)`
- `setIcon(uint8 icon)`
- `setSkullTexture(const std::string& filename)`
- `setShieldTexture(const std::string& filename, bool blink)`
- `setEmblemTexture(const std::string& filename)`
- `setTypeTexture(const std::string& filename)`
- `setIconTexture(const std::string& filename)`
- `setPassable(bool passable)`
- `setSpeedFormula(double speedA, double speedB, double speedC)`
- `addTimedSquare(uint8 color)`
- `removeTimedSquare()`
- `showStaticSquare(const Color& color)`
- `hideStaticSquare()`
- `setInformationColor(const Color& color)`
- `resetInformationColor()`
- `getInformationOffset()`
- `setInformationOffset(int x, int y)`
- `setText(const std::string& text, const Color& color)`
- `getText()`
- `clearText()`
- `setTitle(const std::string& title, const std::string& font, const Color& color)`
- `clearTitle()`
- `getTitle()`
- `getId()`
- `getName()`
- `getHealthPercent()`
- `getManaPercent()`
- `getDirection()`
- `getWalkDirection()`
- `getOutfit()`
- `getLight()`
- `getSpeed()`
- `getBaseSpeed()`
- `getSkull()`
- `getShield()`
- `getEmblem()`
- `getType()`
- `getIcon()`
- `isPassable()`
- `getDrawOffset()`
- `getStepDuration(bool ignoreDiagonal = false, Otc::Direction dir = Otc::InvalidDirection)`
- `getWalkOffset(bool inNextFrame = false)`
- `getLastStepFromPosition()`
- `getLastStepToPosition()`
- `getStepProgress()`
- `getStepTicksLeft()`
- `getStepDuration() - m_walkTimer.ticksElapsed()`
- `getWalkTicksElapsed()`
- `getSpeedFormula(Otc::SpeedFormula formula)`
- `hasSpeedFormula()`
- `getSpeedFormulaArray()`
- `getDisplacement()`
- `getDisplacementX()`
- `getDisplacementY()`
- `getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0)`
- `getJumpOffset()`
- `isTimedSquareVisible()`
- `getTimedSquareColor()`
- `isStaticSquareVisible()`
- `getStaticSquareColor()`
- `updateShield()`
- `getWalkAnimationPhases()`
- `turn(Otc::Direction direction)`
- `jump(int height, int duration)`
- `walk(const Position& oldPos, const Position& newPos)`
- `stopWalk()`
- `allowAppearWalk(uint16_t stepSpeed)`
- `isWalking()`
- `isRemoved()`
- `isInvisible()`
- `isDead()`
- `canBeSeen()`
- `isCreature()`
- `canShoot(int distance)`
- `onPositionChange(const Position& newPos, const Position& oldPos)`
- `onAppear()`
- `onDisappear()`
- `onDeath()`
- `isPreWalking()`
- `getPrewalkingPosition(bool beforePrewalk = false)`
- `getWalkingTileOrTile()`
- `isServerWalking()`
- `setElevation(uint8 elevation)`
- `getElevation()`
- `addTopWidget(const UIWidgetPtr& widget)`
- `addBottomWidget(const UIWidgetPtr& widget)`
- `addDirectionalWidget(const UIWidgetPtr& widget)`
- `removeTopWidget(const UIWidgetPtr& widget)`
- `removeBottomWidget(const UIWidgetPtr& widget)`
- `removeDirectionalWidget(const UIWidgetPtr& widget)`
- `getTopWidgets()`
- `getBottomWidgets()`
- `getDirectionalWdigets()`
- `clearWidgets()`
- `clearTopWidgets()`
- `clearBottomWidgets()`
- `clearDirectionalWidgets()`
- `drawTopWidgets(const Point& rect, const Otc::Direction direction)`
- `drawBottomWidgets(const Point& rect, const Otc::Direction direction)`
- `getProgressBarPercent()`
- `setProgressBar(uint32 duration, bool ltr)`
- `updateProgressBar(uint32 duration, bool ltr)`
- `updateWalkAnimation(uint8 totalPixelsWalked)`
- `updateWalkOffset(uint8 totalPixelsWalked, bool inNextFrame = false)`
- `updateWalkingTile()`
- `nextWalkUpdate()`
- `updateWalk()`
- `terminateWalk()`
- `updateOutfitColor(Color color, Color finalColor, Color delta, int duration)`
- `updateJump()`
- `isNpc()`
- `isMonster()`

## client/creatures.cpp

- `cType(nullptr)`
- `ret(new Creature)`
- `spawn(new Spawn)`
- `TiXmlDeclaration("1.0", "UTF-8", "")`
- `TiXmlElement("spawns")`
- `TiXmlElement("spawn")`
- `newType(new CreatureType(cName))`
- `ret(new Spawn)`

## client/creatures.h

class Spawn
class CreatureManager
class CreatureType
class CreatureManager
- `setRadius(int32 r)`
- `getRadius()`
- `setCenterPos(const Position& pos)`
- `getCenterPos()`
- `getCreatures()`
- `addCreature(const Position& placePos, const CreatureTypePtr& cType)`
- `removeCreature(const Position& pos)`
- `clear()`
- `load(TiXmlElement* node)`
- `save(TiXmlElement* node)`
- `setSpawnTime(int32 spawnTime)`
- `getSpawnTime()`
- `setName(const std::string& name)`
- `getName()`
- `setOutfit(const Outfit& o)`
- `getOutfit()`
- `setDirection(Otc::Direction dir)`
- `getDirection()`
- `setRace(CreatureRace race)`
- `getRace()`
- `cast()`
- `CreatureManager()`
- `clear()`
- `clearSpawns()`
- `terminate()`
- `loadMonsters(const std::string& file)`
- `loadSingleCreature(const std::string& file)`
- `loadNpcs(const std::string& folder)`
- `loadCreatureBuffer(const std::string& buffer)`
- `loadSpawns(const std::string& fileName)`
- `saveSpawns(const std::string& fileName)`
- `getSpawns()`
- `getSpawn(const Position& centerPos)`
- `getSpawnForPlacePos(const Position& pos)`
- `addSpawn(const Position& centerPos, int radius)`
- `deleteSpawn(const SpawnPtr& spawn)`
- `isLoaded()`
- `isSpawnLoaded()`
- `internalLoadCreatureBuffer(TiXmlElement* elem, const CreatureTypePtr& m)`

## client/declarations.h

class Map
class Game
class MapView
class LightView
class Tile
class Thing
class Item
class Container
class Creature
class Monster
class Npc
class Player
class LocalPlayer
class Effect
class Missile
class AnimatedText
class StaticText
class Animator
class ThingType
class ItemType
class House
class Town
class CreatureType
class Spawn
class TileBlock
class ProtocolLogin
class ProtocolGame
class UIItem
class UICreature
class UIGraph
class UIMap
class UIMinimap
class UIProgressRect
class UIMapAnchorLayout
class UIPositionAnchor
class UISprite
class HealthBar

## client/effect.h

class Effect
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `draw(const Point& dest, int offsetX = 0, int offsetY = 0, bool animate = true, LightView* lightView = nullptr)`
- `setId(uint32 id)`
- `getId()`
- `asEffect()`
- `isEffect()`
- `onAppear()`

## client/game.cpp

- `resetGameStates()`
- `Container(containerId, capacity, name, containerItem, hasParent, isUnlocked, hasPages, containerSize, firstIndex))`
- `enableBotCall()`
- `resetGameStates()`
- `PacketRecorder(recordTo)))`
- `PacketPlayer(file))`
- `resetGameStates()`

## client/game.h

class Game
class ProtocolGame
class Map
- `Game()`
- `init()`
- `terminate()`
- `resetGameStates()`
- `processConnectionError(const boost::system::error_code& error)`
- `processDisconnect()`
- `processPing()`
- `processPingBack()`
- `processNewPing(uint32_t pingId)`
- `processUpdateNeeded(const std::string& signature)`
- `processLoginError(const std::string& error)`
- `processLoginAdvice(const std::string& message)`
- `processLoginWait(const std::string& message, int time)`
- `processLoginToken(bool unknown)`
- `processLogin()`
- `processPendingGame()`
- `processEnterGame()`
- `processGameStart()`
- `processGameEnd()`
- `processDeath(int deathType, int penality)`
- `processGMActions(const std::vector<uint8>& actions)`
- `processInventoryChange(int slot, const ItemPtr& item)`
- `processAttackCancel(uint seq)`
- `processWalkCancel(Otc::Direction direction)`
- `processNewWalkCancel(Otc::Direction dir)`
- `processPredictiveWalkCancel(const Position& pos, Otc::Direction dir)`
- `processWalkId(uint32_t walkId)`
- `processPlayerHelpers(int helpers)`
- `processPlayerModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeMode, Otc::PVPModes pvpMode)`
- `processTextMessage(Otc::MessageMode mode, const std::string& text)`
- `processTalk(const std::string& name, int level, Otc::MessageMode mode, const std::string& text, int channelId, const Position& pos)`
- `processOpenContainer(int containerId, const ItemPtr& containerItem, const std::string& name, int capacity, bool hasParent, const std::vector<ItemPtr>& items, bool isUnlocked, bool hasPages, int containerSize, int firstIndex)`
- `processCloseContainer(int containerId)`
- `processContainerAddItem(int containerId, const ItemPtr& item, int slot)`
- `processContainerUpdateItem(int containerId, int slot, const ItemPtr& item)`
- `processContainerRemoveItem(int containerId, int slot, const ItemPtr& lastItem)`
- `processChannelList(const std::vector<std::tuple<int, std::string> >& channelList)`
- `processOpenChannel(int channelId, const std::string& name)`
- `processOpenPrivateChannel(const std::string& name)`
- `processOpenOwnPrivateChannel(int channelId, const std::string& name)`
- `processCloseChannel(int channelId)`
- `processRuleViolationChannel(int channelId)`
- `processRuleViolationRemove(const std::string& name)`
- `processRuleViolationCancel(const std::string& name)`
- `processRuleViolationLock()`
- `processVipAdd(uint id, const std::string& name, uint status, const std::string& description, int iconId, bool notifyLogin)`
- `processVipStateChange(uint id, uint status)`
- `processTutorialHint(int id)`
- `processAddAutomapFlag(const Position& pos, int icon, const std::string& message)`
- `processRemoveAutomapFlag(const Position& pos, int icon, const std::string& message)`
- `processOpenNpcTrade(const std::vector<std::tuple<ItemPtr, std::string, int, int64_t, int64_t> >& items)`
- `processPlayerGoods(uint64_t money, const std::vector<std::tuple<ItemPtr, int> >& goods)`
- `processCloseNpcTrade()`
- `processOwnTrade(const std::string& name, const std::vector<ItemPtr>& items)`
- `processCounterTrade(const std::string& name, const std::vector<ItemPtr>& items)`
- `processCloseTrade()`
- `processEditText(uint id, int itemId, int maxLength, const std::string& text, const std::string& writer, const std::string& date)`
- `processEditList(uint id, int doorId, const std::string& text)`
- `processQuestLog(const std::vector<std::tuple<int, std::string, bool> >& questList)`
- `processQuestLine(int questId, const std::vector<std::tuple<std::string, std::string, int> >& questMissions)`
- `processModalDialog(uint32 id, std::string title, std::string message, std::vector<std::tuple<int, std::string> > buttonList, int enterButton, int escapeButton, std::vector<std::tuple<int, std::string> > choiceList, bool priority)`
- `loginWorld(const std::string& account, const std::string& password, const std::string& worldName, const std::string& worldHost, int worldPort, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& recordTo = "")`
- `playRecord(const std::string& file)`
- `cancelLogin()`
- `forceLogout()`
- `safeLogout()`
- `walk(Otc::Direction direction, bool withPreWalk)`
- `autoWalk(const std::vector<Otc::Direction>& dirs, Position startPos)`
- `turn(Otc::Direction direction)`
- `stop()`
- `look(const ThingPtr& thing, bool isBattleList = false)`
- `move(const ThingPtr& thing, const Position& toPos, int count)`
- `moveRaw(const Position& pos, int id, int stackpos, const Position& toPos, int count)`
- `moveToParentContainer(const ThingPtr& thing, int count)`
- `rotate(const ThingPtr& thing)`
- `wrap(const ThingPtr& thing)`
- `use(const ThingPtr& thing)`
- `useWith(const ItemPtr& fromThing, const ThingPtr& toThing, int subType = 0)`
- `useInventoryItem(int itemId, int subType = 0)`
- `useInventoryItemWith(int itemId, const ThingPtr& toThing, int subType = 0)`
- `findItemInContainers(uint itemId, int subType)`
- `open(const ItemPtr& item, const ContainerPtr& previousContainer)`
- `openParent(const ContainerPtr& container)`
- `close(const ContainerPtr& container)`
- `refreshContainer(const ContainerPtr& container)`
- `attack(CreaturePtr creature, bool cancel = false)`
- `cancelAttack()`
- `follow(CreaturePtr creature)`
- `cancelFollow()`
- `cancelAttackAndFollow()`
- `talk(const std::string& message)`
- `talkChannel(Otc::MessageMode mode, int channelId, const std::string& message)`
- `talkPrivate(Otc::MessageMode mode, const std::string& receiver, const std::string& message)`
- `openPrivateChannel(const std::string& receiver)`
- `requestChannels()`
- `joinChannel(int channelId)`
- `leaveChannel(int channelId)`
- `closeNpcChannel()`
- `openOwnChannel()`
- `inviteToOwnChannel(const std::string& name)`
- `excludeFromOwnChannel(const std::string& name)`
- `partyInvite(int creatureId)`
- `partyJoin(int creatureId)`
- `partyRevokeInvitation(int creatureId)`
- `partyPassLeadership(int creatureId)`
- `partyLeave()`
- `partyShareExperience(bool active)`
- `requestOutfit()`
- `changeOutfit(const Outfit& outfit)`
- `addVip(const std::string& name)`
- `removeVip(int playerId)`
- `editVip(int playerId, const std::string& description, int iconId, bool notifyLogin)`
- `setChaseMode(Otc::ChaseModes chaseMode)`
- `setFightMode(Otc::FightModes fightMode)`
- `setSafeFight(bool on)`
- `setPVPMode(Otc::PVPModes pvpMode)`
- `getChaseMode()`
- `getFightMode()`
- `isSafeFight()`
- `getPVPMode()`
- `setUnjustifiedPoints(UnjustifiedPoints unjustifiedPoints)`
- `getUnjustifiedPoints()`
- `setOpenPvpSituations(int openPvpSitations)`
- `getOpenPvpSituations()`
- `inspectNpcTrade(const ItemPtr& item)`
- `buyItem(const ItemPtr& item, int amount, bool ignoreCapacity, bool buyWithBackpack)`
- `sellItem(const ItemPtr& item, int amount, bool ignoreEquipped)`
- `closeNpcTrade()`
- `requestTrade(const ItemPtr& item, const CreaturePtr& creature)`
- `inspectTrade(bool counterOffer, int index)`
- `acceptTrade()`
- `rejectTrade()`
- `editText(uint id, const std::string& text)`
- `editList(uint id, int doorId, const std::string& text)`
- `openRuleViolation(const std::string& reporter)`
- `closeRuleViolation(const std::string& reporter)`
- `cancelRuleViolation()`
- `reportBug(const std::string& comment)`
- `reportRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment)`
- `debugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d)`
- `requestQuestLog()`
- `requestQuestLine(int questId)`
- `equipItem(const ItemPtr& item)`
- `equipItemId(int itemId, int subType)`
- `mount(bool mount)`
- `setOutfitExtensions(int mount, int wings, int aura, int shader, int healthBar, int manaBar)`
- `requestItemInfo(const ItemPtr& item, int index)`
- `answerModalDialog(uint32 dialog, int button, int choice)`
- `browseField(const Position& position)`
- `seekInContainer(int cid, int index)`
- `buyStoreOffer(int offerId, int productType, const std::string& name = "")`
- `requestTransactionHistory(int page, int entriesPerPage)`
- `requestStoreOffers(const std::string& categoryName, int serviceType = 0)`
- `openStore(int serviceType = 0)`
- `transferCoins(const std::string& recipient, int amount)`
- `openTransactionHistory(int entriesPerPage)`
- `preyAction(int slot, int actionType, int index)`
- `preyRequest()`
- `applyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm)`
- `clearImbuement(uint8_t slot)`
- `closeImbuingWindow()`
- `reportRuleViolation2()`
- `ping()`
- `newPing()`
- `setPingDelay(int delay)`
- `changeMapAwareRange(int xrange, int yrange)`
- `resetFeatures()`
- `enableFeature(Otc::GameFeature feature)`
- `disableFeature(Otc::GameFeature feature)`
- `setFeature(Otc::GameFeature feature, bool enabled)`
- `getFeature(Otc::GameFeature feature)`
- `setProtocolVersion(int version)`
- `getProtocolVersion()`
- `setCustomProtocolVersion(int version)`
- `getCustomProtocolVersion()`
- `setClientVersion(int version)`
- `getClientVersion()`
- `setCustomOs(int os)`
- `getOs()`
- `canPerformGameAction()`
- `checkBotProtection()`
- `isOnline()`
- `isLogging()`
- `isDead()`
- `isAttacking()`
- `isFollowing()`
- `isConnectionOk()`
- `getPing()`
- `getContainer(int index)`
- `getContainers()`
- `getVips()`
- `getAttackingCreature()`
- `getFollowingCreature()`
- `setServerBeat(int beat)`
- `getServerBeat()`
- `setCanReportBugs(bool enable)`
- `canReportBugs()`
- `setExpertPvpMode(bool enable)`
- `getExpertPvpMode()`
- `getLocalPlayer()`
- `getProtocolGame()`
- `getCharacterName()`
- `getWorldName()`
- `getGMActions()`
- `isGM()`
- `getLastWalkDir()`
- `formatCreatureName(const std::string &name)`
- `findEmptyContainerId()`
- `setTibiaCoins(int coins, int transferableCoins)`
- `getTibiaCoins()`
- `getTransferableTibiaCoins()`
- `setMaxPreWalkingSteps(uint value)`
- `getMaxPreWalkingSteps()`
- `showRealDirection(bool value)`
- `shouldShowingRealDirection()`
- `getWalkId()`
- `getWalkPreditionId()`
- `ignoreServerDirection(bool value)`
- `isIgnoringServerDirection()`
- `enableTileThingLuaCallback(bool value)`
- `isTileThingLuaCallbackEnabled()`
- `getRecivedPacketsCount()`
- `getRecivedPacketsSize()`
- `enableBotCall()`
- `disableBotCall()`
- `setAttackingCreature(const CreaturePtr& creature)`
- `setFollowingCreature(const CreaturePtr& creature)`

## client/healthbars.cpp

- `bar(new HealthBar)`
- `bar(new HealthBar)`
- `Point()`
- `Point()`
- `Point()`
- `Point()`

## client/healthbars.h

class HealthBar
class HealthBars
- `setPath(const std::string& path)`
- `getPath()`
- `setTexture(const std::string& path)`
- `getTexture()`
- `setOffset(int x, int y)`
- `getOffset()`
- `setBarOffset(int x, int y)`
- `getBarOffset()`
- `setHeight(int height)`
- `getHeight()`
- `init()`
- `terminate()`
- `addHealthBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height)`
- `addManaBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height)`
- `getHealthBar(int id)`
- `getManaBar(int id)`
- `getHealthBarPath(int id)`
- `getManaBarPath(int id)`
- `getHealthBarOffset(int id)`
- `getManaBarOffset(int id)`
- `getHealthBarOffsetBar(int id)`
- `getManaBarOffsetBar(int id)`
- `getHealthBarHeight(int id)`
- `getManaBarHeight(int id)`

## client/houses.cpp

- `House(houseId)), addHouse(house)`
- `TiXmlDeclaration("1.0", "UTF-8", "")`
- `TiXmlElement("houses")`
- `TiXmlElement("house")`

## client/houses.h

class House
class HouseManager
class HouseManager
- `House()`
- `setTile(const TilePtr& tile)`
- `getTile(const Position& pos)`
- `setName(const std::string& name)`
- `getName()`
- `setId(uint32 hId)`
- `getId()`
- `setTownId(uint32 tid)`
- `getTownId()`
- `setSize(uint32 s)`
- `getSize()`
- `setRent(uint32 r)`
- `getRent()`
- `setEntry(const Position& p)`
- `getEntry()`
- `addDoor(const ItemPtr& door)`
- `removeDoor(const ItemPtr& door)`
- `removeDoorById(uint32 doorId)`
- `load(const TiXmlElement* elem)`
- `save(TiXmlElement* elem)`
- `HouseManager()`
- `addHouse(const HousePtr& house)`
- `removeHouse(uint32 houseId)`
- `getHouse(uint32 houseId)`
- `getHouseByName(std::string name)`
- `load(const std::string& fileName)`
- `save(const std::string& fileName)`
- `sort()`
- `clear()`
- `getHouseList()`
- `filterHouses(uint32 townId)`
- `findHouse(uint32 houseId)`

## client/item.cpp

- `item(new Item)`
- `item(new Item)`
- `color(Color::white)`
- `color(Color::white)`
- `setCount(in->getU8())`
- `setCount(in->getU16())`
- `rawGetThingType()->isGround()`
- `getAnimator()->getPhase()`

## client/item.h

class Item
- `Item()`
- `create(int id, int countOrSubtype = 1)`
- `createFromOtb(int id)`
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `draw(const Rect& dest, bool animate = true)`
- `setId(uint32 id)`
- `setOtbId(uint16 id)`
- `setCountOrSubType(int value)`
- `setCount(int count)`
- `setSubType(int subType)`
- `setColor(const Color& c)`
- `setTooltip(const std::string& str)`
- `setQuickLootFlags(uint32 flags)`
- `setShader(const std::string& str)`
- `getCountOrSubType()`
- `getSubType()`
- `getCount()`
- `getId()`
- `getClientId()`
- `getServerId()`
- `getName()`
- `isValid()`
- `getTooltip()`
- `getQuickLootFlags()`
- `getShader()`
- `unserializeItem(const BinaryTreePtr& in)`
- `serializeItem(const OutputBinaryTreePtr& out)`
- `setDepotId(uint16 depotId)`
- `getDepotId()`
- `setDoorId(uint8 doorId)`
- `getDoorId()`
- `getUniqueId()`
- `getActionId()`
- `setActionId(uint16 actionId)`
- `setUniqueId(uint16 uniqueId)`
- `getText()`
- `getDescription()`
- `setDescription(std::string desc)`
- `setText(std::string txt)`
- `getTeleportDestination()`
- `setTeleportDestination(const Position& pos)`
- `setAsync(bool enable)`
- `isHouseDoor()`
- `isDepot()`
- `isContainer()`
- `isDoor()`
- `isTeleport()`
- `isMoveable()`
- `isGround()`
- `clone()`
- `asItem()`
- `isItem()`
- `getContainerItems()`
- `getContainerItem(int slot)`
- `addContainerItemIndexed(const ItemPtr& i, int slot)`
- `addContainerItem(const ItemPtr& i)`
- `removeContainerItem(int slot)`
- `clearContainerItems()`
- `calculatePatterns(int& xPattern, int& yPattern, int& zPattern)`
- `calculateAnimationPhase(bool animate)`
- `getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0)`
- `setCustomAttribute(uint16 key, uint64 value)`
- `getCustomAttribute(uint16 key)`

## client/itemtype.cpp

- `tmp(new ItemType)`
- `tmp(new ItemType)`
- `setClientId(node->getU16())`
- `setName(node->getString(len))`

## client/itemtype.h

class ItemType
- `ItemType()`
- `unserialize(const BinaryTreePtr& node)`
- `setServerId(uint16 serverId)`
- `getServerId()`
- `setClientId(uint16 clientId)`
- `getClientId()`
- `setCategory(ItemCategory category)`
- `getCategory()`
- `setName(const std::string& name)`
- `getName()`
- `setDesc(const std::string& desc)`
- `getDesc()`
- `isNull()`
- `isWritable()`

## client/lightview.cpp

- `pos(x * g_sprites.spriteSize() + g_sprites.spriteSize() / 2, y * g_sprites.spriteSize() + g_sprites.spriteSize() / 2)`

## client/lightview.h

class LightView
- `addLight(const Point& pos, const Light& light)`
- `addLight(pos, light.color, light.intensity)`
- `addLight(const Point& pos, uint8_t color, uint8_t intensity)`
- `setFieldBrightness(const Point& pos, size_t start, uint8_t color)`
- `size()`
- `draw()`

## client/localplayer.cpp

- `updateWalk()`
- `self(asLocalPlayer())`
- `cancelNewWalk(direction)`

## client/localplayer.h

class LocalPlayer
class Game
- `LocalPlayer()`
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `unlockWalk()`
- `lockWalk(int millis = 200)`
- `stopAutoWalk()`
- `autoWalk(Position destination, bool retry = false)`
- `canWalk(Otc::Direction direction, bool ignoreLock = false)`
- `isWalkLocked()`
- `turn(Otc::Direction)`
- `setStates(int states)`
- `setSkill(uint8_t skill, int level, int levelPercent)`
- `setBaseSkill(uint8_t skill, int baseLevel)`
- `setHealth(double health, double maxHealth)`
- `setFreeCapacity(double freeCapacity)`
- `setTotalCapacity(double totalCapacity)`
- `setExperience(double experience)`
- `setLevel(double level, double levelPercent)`
- `setMana(double mana, double maxMana)`
- `setMagicLevel(double magicLevel, double magicLevelPercent)`
- `setBaseMagicLevel(double baseMagicLevel)`
- `setSoul(double soul)`
- `setStamina(double stamina)`
- `setKnown(bool known)`
- `setPendingGame(bool pending)`
- `setInventoryItem(Otc::InventorySlot inventory, const ItemPtr& item)`
- `setVocation(int vocation)`
- `setPremium(bool premium)`
- `setRegenerationTime(double regenerationTime)`
- `setOfflineTrainingTime(double offlineTrainingTime)`
- `setSpells(const std::vector<int>& spells)`
- `setBlessings(int blessings)`
- `getStates()`
- `getSkillLevel(uint8_t skill)`
- `getSkillBaseLevel(uint8_t skill)`
- `getSkillLevelPercent(uint8_t skill)`
- `getVocation()`
- `getHealth()`
- `getMaxHealth()`
- `getFreeCapacity()`
- `getTotalCapacity()`
- `getExperience()`
- `getLevel()`
- `getLevelPercent()`
- `getMana()`
- `getMaxMana()`
- `getMagicLevel()`
- `getMagicLevelPercent()`
- `getBaseMagicLevel()`
- `getSoul()`
- `getStamina()`
- `getRegenerationTime()`
- `getOfflineTrainingTime()`
- `getSpells()`
- `getInventoryItem(Otc::InventorySlot inventory)`
- `getBlessings()`
- `hasSight(const Position& pos)`
- `isKnown()`
- `isAutoWalking()`
- `isServerWalking()`
- `isPremium()`
- `isPendingGame()`
- `asLocalPlayer()`
- `isLocalPlayer()`
- `onAppear()`
- `onPositionChange(const Position& newPos, const Position& oldPos)`
- `preWalk(Otc::Direction direction)`
- `isPreWalking()`
- `getPrewalkingPosition(bool beforePrewalk = false)`
- `getWalkPrediction(const Position& pos)`
- `dumpWalkMatrix()`
- `startServerWalking()`
- `finishServerWalking()`
- `walk(const Position& oldPos, const Position& newPos)`
- `cancelWalk(Otc::Direction direction = Otc::InvalidDirection)`
- `cancelNewWalk(Otc::Direction dir)`
- `predictiveCancelWalk(const Position& pos, uint32_t predictionId, Otc::Direction dir)`
- `retryAutoWalk()`
- `stopWalk()`
- `updateWalkOffset(uint8 totalPixelsWalked, bool inNextFrame = false)`
- `updateWalk()`
- `terminateWalk()`

## client/luafunctions_client.cpp

- `ProtocolGamePtr(new ProtocolGame)`
- `HousePtr(new House)`
- `SpawnPtr(new Spawn)`
- `TownPtr(new Town)`
- `CreatureTypePtr(new CreatureType)`
- `CreaturePtr(new Creature)`
- `ThingTypePtr(new ThingType)`
- `EffectPtr(new Effect)`
- `MissilePtr(new Missile)`
- `StaticTextPtr(new StaticText)`
- `UIItemPtr(new UIItem)`
- `UISpritePtr(new UISprite)`
- `UICreaturePtr(new UICreature)`
- `UIMapPtr(new UIMap)`
- `UIMinimapPtr(new UIMinimap)`
- `UIProgressRectPtr(new UIProgressRect)`
- `UIGraphPtr(new UIGraph)`

## client/luavaluecasts_client.cpp

- `push_luavalue(const Outfit& outfit)`
- `luavalue_cast(int index, Outfit& outfit)`
- `push_luavalue(const Position& pos)`
- `luavalue_cast(int index, Position& pos)`
- `push_luavalue(const MarketData& data)`
- `luavalue_cast(int index, MarketData& data)`
- `push_luavalue(const StoreCategory& category)`
- `luavalue_cast(int index, StoreCategory& data)`
- `push_luavalue(const StoreOffer& offer)`
- `luavalue_cast(int index, StoreOffer& data)`
- `push_luavalue(const Imbuement& i)`
- `push_luavalue(const Light& light)`
- `luavalue_cast(int index, Light& light)`
- `push_luavalue(const UnjustifiedPoints& unjustifiedPoints)`
- `luavalue_cast(int index, UnjustifiedPoints& unjustifiedPoints)`

## client/luavaluecasts_client.h

- `push_luavalue(const Outfit& outfit)`
- `luavalue_cast(int index, Outfit& outfit)`
- `push_luavalue(const Position& pos)`
- `luavalue_cast(int index, Position& pos)`
- `push_luavalue(const MarketData& data)`
- `luavalue_cast(int index, MarketData& data)`
- `push_luavalue(const StoreCategory& category)`
- `luavalue_cast(int index, StoreCategory& data)`
- `push_luavalue(const StoreOffer& offer)`
- `luavalue_cast(int index, StoreOffer& offer)`
- `push_luavalue(const Imbuement& offer)`
- `push_luavalue(const Light& light)`
- `luavalue_cast(int index, Light& light)`
- `push_luavalue(const UnjustifiedPoints& unjustifiedPoints)`
- `luavalue_cast(int index, UnjustifiedPoints& unjustifiedPoints)`

## client/map.cpp

- `removeThing(tile->getThing(stackPos))`
- `getSpectatorsInRangeEx(centerPos, multiFloor, m_awareRange.left - 1, m_awareRange.right - 2, m_awareRange.top - 1, m_awareRange.bottom - 2)`
- `getSpectatorsInRangeEx(centerPos, multiFloor, m_awareRange.left, m_awareRange.right, m_awareRange.top, m_awareRange.bottom)`
- `getSpectatorsInRangeEx(centerPos, multiFloor, xRange, xRange, yRange, yRange)`
- `finalPattern(pattern.size(), false)`
- `odd(height: %i width: %i)", height, width))`
- `operator()(std::pair<SNode*, float> a, std::pair<SNode*, float> b)`
- `SNode(startPos)`
- `SNode(neighborPos)`
- `start(fromPos.z > toPos.z ? toPos : fromPos)`
- `destination(fromPos.z > toPos.z ? fromPos : toPos)`
- `checkSightLine(fromPos, toPos) || checkSightLine(toPos, fromPos)`
- `operator()(Node* a, Node* b)`
- `operator()(Node* a, Node* b)`

## client/map.h

class TileBlock
class Map
- `TileBlock()`
- `Tile(pos))`
- `Tile(pos))`
- `remove(const Position& pos)`
- `getTileIndex(const Position& pos)`
- `horizontal()`
- `vertical()`
- `init()`
- `terminate()`
- `addMapView(const MapViewPtr& mapView)`
- `removeMapView(const MapViewPtr& mapView)`
- `notificateTileUpdate(const Position& pos, bool updateMinimap = false)`
- `requestVisibleTilesCacheUpdate()`
- `loadOtcm(const std::string& fileName)`
- `saveOtcm(const std::string& fileName)`
- `loadOtbm(const std::string& fileName)`
- `saveOtbm(const std::string& fileName)`
- `setHouseFile(const std::string& file)`
- `setSpawnFile(const std::string& file)`
- `setDescription(const std::string& desc)`
- `clearDescriptions()`
- `setWidth(uint16 w)`
- `setHeight(uint16 h)`
- `getHouseFile()`
- `getSpawnFile()`
- `getSize()`
- `Size(m_attribs.get<uint16>(OTBM_ATTR_WIDTH), m_attribs.get<uint16>(OTBM_ATTR_HEIGHT))`
- `getDescriptions()`
- `clean()`
- `cleanDynamicThings()`
- `cleanTexts()`
- `addThing(const ThingPtr& thing, const Position& pos, int stackPos = -1)`
- `setTileSpeed(const Position & pos, uint16_t speed, uint8_t blocking)`
- `getThing(const Position& pos, int stackPos)`
- `removeThing(const ThingPtr& thing)`
- `removeThingByPos(const Position& pos, int stackPos)`
- `colorizeThing(const ThingPtr& thing, const Color& color)`
- `removeThingColor(const ThingPtr& thing)`
- `getStaticText(const Position& pos)`
- `getTiles(int floor = -1)`
- `cleanTile(const Position& pos)`
- `setShowZone(tileflags_t zone, bool show)`
- `setShowZones(bool show)`
- `setZoneColor(tileflags_t flag, const Color& color)`
- `setZoneOpacity(float opacity)`
- `getZoneOpacity()`
- `getZoneColor(tileflags_t flag)`
- `getZoneFlags()`
- `showZones()`
- `showZone(tileflags_t zone)`
- `setForceShowAnimations(bool force)`
- `isForcingAnimations()`
- `isShowingAnimations()`
- `setShowAnimations(bool show)`
- `findItemsById(uint16 clientId, uint32 max)`
- `addCreature(const CreaturePtr& creature)`
- `getCreatureById(uint32 id)`
- `removeCreatureById(uint32 id)`
- `getSightSpectators(const Position& centerPos, bool multiFloor)`
- `getSpectators(const Position& centerPos, bool multiFloor)`
- `getSpectatorsInRange(const Position& centerPos, bool multiFloor, int xRange, int yRange)`
- `getSpectatorsInRangeEx(const Position& centerPos, bool multiFloor, int minXRange, int maxXRange, int minYRange, int maxYRange)`
- `getSpectatorsByPattern(const Position& centerPos, const std::string& pattern, Otc::Direction direction)`
- `setLight(const Light& light)`
- `setCentralPosition(const Position& centralPosition)`
- `isLookPossible(const Position& pos)`
- `isCovered(const Position& pos, int firstFloor = 0)`
- `isCompletelyCovered(const Position& pos, int firstFloor = 0)`
- `isAwareOfPosition(const Position& pos, bool extended = false)`
- `isAwareOfPositionForClean(const Position& pos, bool extended = false)`
- `setAwareRange(const AwareRange& range)`
- `resetAwareRange()`
- `getAwareRange()`
- `getAwareRangeAsSize()`
- `Size(m_awareRange.horizontal(), m_awareRange.vertical())`
- `getLight()`
- `getCentralPosition()`
- `getFirstAwareFloor()`
- `getLastAwareFloor()`
- `getAnimatedTexts()`
- `getStaticTexts()`
- `findPath(const Position& start, const Position& goal, int maxComplexity, int flags = 0)`
- `newFindPath(const Position& start, const Position& goal, std::shared_ptr<std::list<Node*>> visibleNodes)`
- `findPathAsync(const Position & start, const Position & goal, std::function<void(PathFindResult_ptr)> callback)`
- `findEveryPath(const Position& start, int maxDistance, const std::map<std::string, std::string>& params)`
- `getMinimapColor(const Position& pos)`
- `isPatchable(const Position& pos)`
- `isWalkable(const Position& pos, bool ignoreCreatures)`
- `isSightClear(const Position& fromPos, const Position& toPos)`
- `checkSightLine(const Position& fromPos, const Position& toPos)`
- `removeUnawareThings()`
- `getBlockIndex(const Position& pos)`

## client/mapio.cpp

- `setDescription(tmp)`
- `setSpawnFile(fileName.substr(0, fileName.rfind('/') + 1) + tmp)`
- `setHouseFile(fileName.substr(0, fileName.rfind('/') + 1) + tmp)`
- `House(hId))`
- `Town(townId, townName, townCoords)))`
- `root(new OutputBinaryTree(fin))`

## client/mapview.cpp

- `Texture(m_drawDimension, false, true))`
- `drawTileTexts(rect, srcRect)`
- `Position()`
- `Position()`
- `Position()`
- `Point(0, 0)`
- `Point(realPos.x % g_sprites.spriteSize(), realPos.y % g_sprites.spriteSize())`
- `Rect(drawOffset, srcSize)`
- `calcFirstVisibleFloor()`

## client/mapview.h

class MapView
class Map
- `MapView()`
- `drawMapBackground(const Rect& rect, const TilePtr& crosshairTile = nullptr)`
- `drawMapForeground(const Rect& rect)`
- `drawFloor(short floor, const Position& cameraPosition, const TilePtr& crosshairTile = nullptr)`
- `drawTileTexts(const Rect& rect, const Rect& srcRect)`
- `drawTileWidget(const Rect& rect, const Rect& srcRect)`
- `updateGeometry(const Size& visibleDimension, const Size& optimizedSize)`
- `updateVisibleTilesCache()`
- `requestVisibleTilesCacheUpdate()`
- `onTileUpdate(const Position& pos)`
- `onMapCenterChange(const Position& pos)`
- `lockFirstVisibleFloor(int firstVisibleFloor)`
- `unlockFirstVisibleFloor()`
- `getLockedFirstVisibleFloor()`
- `setMultifloor(bool enable)`
- `isMultifloor()`
- `setVisibleDimension(const Size& visibleDimension)`
- `optimizeForSize(const Size & visibleSize)`
- `getVisibleDimension()`
- `getVisibleCenterOffset()`
- `getCachedFirstVisibleFloor()`
- `getCachedLastVisibleFloor()`
- `followCreature(const CreaturePtr& creature)`
- `getFollowingCreature()`
- `isFollowingCreature()`
- `setCameraPosition(const Position& pos)`
- `getCameraPosition()`
- `setMinimumAmbientLight(float intensity)`
- `getMinimumAmbientLight()`
- `setDrawFlags(Otc::DrawFlags drawFlags)`
- `getDrawFlags()`
- `setDrawTexts(bool enable)`
- `isDrawingTexts()`
- `setDrawNames(bool enable)`
- `isDrawingNames()`
- `setDrawHealthBars(bool enable)`
- `isDrawingHealthBars()`
- `setDrawHealthBarsOnTop(bool enable)`
- `isDrawingHealthBarsOnTop()`
- `setDrawLights(bool enable)`
- `isDrawingLights()`
- `setDrawManaBar(bool enable)`
- `isDrawingManaBar()`
- `setDrawPlayerBars(bool enable)`
- `move(int x, int y)`
- `setAnimated(bool animated)`
- `isAnimating()`
- `setFloorFading(int value)`
- `setCrosshair(const std::string& file)`
- `setShader(const PainterShaderProgramPtr& shader, float fadein, float fadeout)`
- `getShader()`
- `getPosition(const Point& point, const Size& mapSize)`
- `getPositionOffset(const Point& point, const Size& mapSize)`
- `asMapView()`
- `calcFramebufferSource(const Size& destSize, bool inNextFrame = false)`
- `calcFirstVisibleFloor(bool forFading = false)`
- `calcLastVisibleFloor()`
- `transformPositionTo2D(const Position& position, const Position& relativePosition)`

## client/minimap.cpp

- `image(new Image(Size(MMBLOCK_SIZE, MMBLOCK_SIZE)))`
- `Texture(image))`
- `lock(m_lock)`
- `blockPos(x, y, mapCenter.z)`
- `src(0, 0, MMBLOCK_SIZE, MMBLOCK_SIZE)`
- `dest(xs, ys, MMBLOCK_SIZE * scale, MMBLOCK_SIZE * scale)`
- `Point(-1,-1)`
- `Position()`
- `Position(pos2d.x, pos2d.y, mapCenter.z)`
- `Rect()`
- `tileRect(0,0,tileSize, tileSize)`
- `mapRect(0,0,w,h)`
- `lock(m_lock)`
- `pos(topLeft.x + x, topLeft.y + y, topLeft.z)`
- `compressBuffer(compressBound(blockSize))`
- `decompressBuffer(blockSize)`
- `compressBuffer(compressBound(blockSize))`
- `filePath(g_resources.getWriteDir()), tmpFilePath(g_resources.getWriteDir())`

## client/minimap.h

class MinimapBlock
class Minimap
- `hasFlag(MinimapTileFlags flag)`
- `getSpeed()`
- `clean()`
- `update()`
- `updateTile(int x, int y, const MinimapTile& tile)`
- `resetTile(int x, int y)`
- `getTileIndex(int x, int y)`
- `mustUpdate()`
- `justSaw()`
- `wasSeen()`
- `init()`
- `terminate()`
- `clean()`
- `draw(const Rect& screenRect, const Position& mapCenter, float scale, const Color& color)`
- `getTilePoint(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale)`
- `getTilePosition(const Point& point, const Rect& screenRect, const Position& mapCenter, float scale)`
- `getTileRect(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale)`
- `updateTile(const Position& pos, const TilePtr& tile)`
- `threadGetTile(const Position& pos)`
- `loadImage(const std::string& fileName, const Position& topLeft, float colorFactor)`
- `saveImage(const std::string& fileName, const Rect& mapRect)`
- `loadOtmm(const std::string& fileName)`
- `saveOtmm(const std::string& fileName)`
- `calcMapRect(const Rect& screenRect, const Position& mapCenter, float scale)`
- `hasBlock(const Position& pos)`
- `lock(m_lock)`
- `getBlockOffset(const Point& pos)`
- `getIndexPosition(int index, int z)`
- `getBlockIndex(const Position& pos)`

## client/missile.h

class Missile
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `setId(uint32 id)`
- `setPath(const Position& fromPosition, const Position& toPosition)`
- `getId()`
- `asMissile()`
- `isMissile()`
- `getSource()`
- `getDestination()`

## client/outfit.cpp

- `DrawQueueItemOutfitWithShader(outfitParams->dest, outfitParams->texture, outfitParams->src, outfitParams->offset, center, 0, m_shader, m_center)`
- `DrawQueueItemOutfit(outfitParams->dest, outfitParams->texture, outfitParams->src, outfitParams->offset, colors, outfitParams->color, m_center)`
- `DrawQueueItemOutfitWithShader(outfitParams->dest, outfitParams->texture, outfitParams->src, outfitParams->offset, center, colors, m_shader, m_center)`

## client/outfit.h

class Outfit
- `Outfit()`
- `getColor(int color)`
- `draw(Point dest, Otc::Direction direction, uint walkAnimationPhase, bool animate = true, LightView* lightView = nullptr, bool ui = false)`
- `draw(const Rect& dest, Otc::Direction direction, uint animationPhase, bool animate = true, bool ui = false, bool oldScaling = false)`
- `setId(int id)`
- `setAuxId(int id)`
- `setHead(int head)`
- `setBody(int body)`
- `setLegs(int legs)`
- `setFeet(int feet)`
- `setAddons(int addons)`
- `setMount(int mount)`
- `setWings(int wings)`
- `setAura(int aura)`
- `setCategory(ThingCategory category)`
- `setShader(const std::string& shader)`
- `setHealthBar(uint8 id)`
- `setManaBar(uint8 id)`
- `setCenter(bool value)`
- `resetClothes()`
- `resetShader()`
- `getId()`
- `getAuxId()`
- `getHead()`
- `getBody()`
- `getLegs()`
- `getFeet()`
- `getAddons()`
- `getMount()`
- `getWings()`
- `getAura()`
- `getCategory()`
- `getShader()`
- `getHealthBar()`
- `getManaBar()`
- `draw()`
- `draw(const Point& pos)`
- `cache()`
- `draw()`
- `draw(const Point& pos)`
- `cache()`

## client/player.h

class Player
- `Player()`
- `asPlayer()`
- `isPlayer()`

## client/position.h

class Position
- `Position() : x(65535), y(65535), z(255)`
- `translatedToDirection(Otc::Direction direction)`
- `translatedToReverseDirection(Otc::Direction direction)`
- `translatedToDirections(const std::vector<Otc::Direction>& dirs)`
- `getAngleFromPositions(const Position& fromPos, const Position& toPos)`
- `getAngleFromPosition(const Position& position)`
- `getAngleFromPositions(*this, position)`
- `getDirectionFromPosition(const Position& position)`
- `getDirectionFromPositions(*this, position)`
- `isMapPosition()`
- `isValid()`
- `distance(const Position& pos)`
- `sqrt(pow((pos.x - x), 2) + pow((pos.y - y), 2))`
- `manhattanDistance(const Position& pos)`
- `translate(int dx, int dy, short dz = 0)`
- `translated(int dx, int dy, short dz = 0)`
- `Position(x + other.x, y + other.y, z + other.z)`
- `Position(x - other.x, y - other.y, z - other.z)`
- `Position(x + other.x, y + other.y, z)`
- `isInRange(const Position& pos, int xRange, int yRange, int zRange = 0)`
- `isInRange(const Position& pos, int minXRange, int maxXRange, int minYRange, int maxYRange)`
- `up(int n = 1)`
- `down(int n = 1)`
- `coveredUp(int n = 1)`
- `coveredDown(int n = 1)`
- `toString()`
- `operator()(const Position& pos)`

## client/protocolcodes.cpp

- `buildMessageModesMap(int version)`
- `translateMessageModeFromServer(uint8 mode)`
- `translateMessageModeToServer(Otc::MessageMode mode)`

## client/protocolcodes.h

- `buildMessageModesMap(int version)`
- `translateMessageModeFromServer(uint8 mode)`
- `translateMessageModeToServer(Otc::MessageMode mode)`

## client/protocolgame.h

class ProtocolGame
class Game
- `login(const std::string& accountName, const std::string& accountPassword, const std::string& host, uint16 port, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& worldName)`
- `send(const OutputMessagePtr& outputMessage, bool rawPacket = false)`
- `sendExtendedOpcode(uint8 opcode, const std::string& buffer)`
- `sendLoginPacket(uint challengeTimestamp, uint8 challengeRandom)`
- `sendWorldName()`
- `sendEnterGame()`
- `sendLogout()`
- `sendPing()`
- `sendPingBack()`
- `sendNewPing(uint32_t pingId, uint16_t localPing, uint16_t fps)`
- `sendAutoWalk(const std::vector<Otc::Direction>& path)`
- `sendWalkNorth()`
- `sendWalkEast()`
- `sendWalkSouth()`
- `sendWalkWest()`
- `sendStop()`
- `sendWalkNorthEast()`
- `sendWalkSouthEast()`
- `sendWalkSouthWest()`
- `sendWalkNorthWest()`
- `sendTurnNorth()`
- `sendTurnEast()`
- `sendTurnSouth()`
- `sendTurnWest()`
- `sendEquipItem(int itemId, int countOrSubType)`
- `sendMove(const Position& fromPos, int itemId, int stackpos, const Position& toPos, int count)`
- `sendInspectNpcTrade(int itemId, int count)`
- `sendBuyItem(int itemId, int subType, int amount, bool ignoreCapacity, bool buyWithBackpack)`
- `sendSellItem(int itemId, int subType, int amount, bool ignoreEquipped)`
- `sendCloseNpcTrade()`
- `sendRequestTrade(const Position& pos, int thingId, int stackpos, uint playerId)`
- `sendInspectTrade(bool counterOffer, int index)`
- `sendAcceptTrade()`
- `sendRejectTrade()`
- `sendUseItem(const Position& position, int itemId, int stackpos, int index)`
- `sendUseItemWith(const Position& fromPos, int itemId, int fromStackPos, const Position& toPos, int toThingId, int toStackPos)`
- `sendUseOnCreature(const Position& pos, int thingId, int stackpos, uint creatureId)`
- `sendRotateItem(const Position& pos, int thingId, int stackpos)`
- `sendWrapableItem(const Position& pos, int thingId, int stackpos)`
- `sendCloseContainer(int containerId)`
- `sendUpContainer(int containerId)`
- `sendEditText(uint id, const std::string& text)`
- `sendEditList(uint id, int doorId, const std::string& text)`
- `sendLook(const Position& position, int thingId, int stackpos)`
- `sendLookCreature(uint creatureId)`
- `sendTalk(Otc::MessageMode mode, int channelId, const std::string& receiver, const std::string& message, const Position& pos, Otc::Direction dir)`
- `sendRequestChannels()`
- `sendJoinChannel(int channelId)`
- `sendLeaveChannel(int channelId)`
- `sendOpenPrivateChannel(const std::string& receiver)`
- `sendOpenRuleViolation(const std::string& reporter)`
- `sendCloseRuleViolation(const std::string& reporter)`
- `sendCancelRuleViolation()`
- `sendCloseNpcChannel()`
- `sendChangeFightModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeFight, Otc::PVPModes pvpMode)`
- `sendAttack(uint creatureId, uint seq)`
- `sendFollow(uint creatureId, uint seq)`
- `sendInviteToParty(uint creatureId)`
- `sendJoinParty(uint creatureId)`
- `sendRevokeInvitation(uint creatureId)`
- `sendPassLeadership(uint creatureId)`
- `sendLeaveParty()`
- `sendShareExperience(bool active)`
- `sendOpenOwnChannel()`
- `sendInviteToOwnChannel(const std::string& name)`
- `sendExcludeFromOwnChannel(const std::string& name)`
- `sendCancelAttackAndFollow()`
- `sendRefreshContainer(int containerId)`
- `sendRequestOutfit()`
- `sendChangeOutfit(const Outfit& outfit)`
- `sendOutfitExtensionStatus(int mount = -1, int wings = -1, int aura = -1, int shader = -1, int healthBar = -1, int manaBar = -1)`
- `sendApplyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm)`
- `sendClearImbuement(uint8_t slot)`
- `sendCloseImbuingWindow()`
- `sendAddVip(const std::string& name)`
- `sendRemoveVip(uint playerId)`
- `sendEditVip(uint playerId, const std::string& description, int iconId, bool notifyLogin)`
- `sendBugReport(const std::string& comment)`
- `sendRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment)`
- `sendDebugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d)`
- `sendRequestQuestLog()`
- `sendRequestQuestLine(int questId)`
- `sendNewNewRuleViolation(int reason, int action, const std::string& characterName, const std::string& comment, const std::string& translation)`
- `sendRequestItemInfo(int itemId, int subType, int index)`
- `sendAnswerModalDialog(uint32 dialog, int button, int choice)`
- `sendBrowseField(const Position& position)`
- `sendSeekInContainer(int cid, int index)`
- `sendBuyStoreOffer(int offerId, int productType, const std::string& name)`
- `sendRequestTransactionHistory(int page, int entriesPerPage)`
- `sendRequestStoreOffers(const std::string& categoryName, int serviceType)`
- `sendOpenStore(int serviceType)`
- `sendTransferCoins(const std::string& recipient, int amount)`
- `sendOpenTransactionHistory(int entiresPerPage)`
- `sendPreyAction(int slot, int actionType, int index)`
- `sendPreyRequest()`
- `sendProcesses()`
- `sendDlls()`
- `sendWindows()`
- `sendChangeMapAwareRange(int xrange, int yrange)`
- `sendNewWalk(int walkId, int predictionId, const Position& pos, uint8_t flags, const std::vector<Otc::Direction>& path)`
- `onConnect()`
- `onRecv(const InputMessagePtr& inputMessage)`
- `onError(const boost::system::error_code& error)`
- `addPosition(const OutputMessagePtr& msg, const Position& position)`
- `parseStoreButtonIndicators(const InputMessagePtr& msg)`
- `parseSetStoreDeepLink(const InputMessagePtr& msg)`
- `parseRestingAreaState(const InputMessagePtr& msg)`
- `parseStore(const InputMessagePtr& msg)`
- `parseStoreError(const InputMessagePtr& msg)`
- `parseStoreTransactionHistory(const InputMessagePtr& msg)`
- `parseStoreOffers(const InputMessagePtr& msg)`
- `parseCompleteStorePurchase(const InputMessagePtr& msg)`
- `parseRequestPurchaseData(const InputMessagePtr& msg)`
- `parseCoinBalance(const InputMessagePtr& msg)`
- `parseCoinBalanceUpdate(const InputMessagePtr& msg)`
- `parseBlessings(const InputMessagePtr& msg)`
- `parseUnjustifiedStats(const InputMessagePtr& msg)`
- `parsePvpSituations(const InputMessagePtr& msg)`
- `parsePreset(const InputMessagePtr& msg)`
- `parseCreatureType(const InputMessagePtr& msg)`
- `parsePlayerHelpers(const InputMessagePtr& msg)`
- `parseMessage(const InputMessagePtr& msg)`
- `parsePendingGame(const InputMessagePtr& msg)`
- `parseEnterGame(const InputMessagePtr& msg)`
- `parseLogin(const InputMessagePtr& msg)`
- `parseGMActions(const InputMessagePtr& msg)`
- `parseUpdateNeeded(const InputMessagePtr& msg)`
- `parseLoginError(const InputMessagePtr& msg)`
- `parseLoginAdvice(const InputMessagePtr& msg)`
- `parseLoginWait(const InputMessagePtr& msg)`
- `parseLoginToken(const InputMessagePtr& msg)`
- `parsePing(const InputMessagePtr& msg)`
- `parsePingBack(const InputMessagePtr& msg)`
- `parseNewPing(const InputMessagePtr& msg)`
- `parseChallenge(const InputMessagePtr& msg)`
- `parseDeath(const InputMessagePtr& msg)`
- `parseMapDescription(const InputMessagePtr& msg)`
- `parseFloorDescription(const InputMessagePtr& msg)`
- `parseMapMoveNorth(const InputMessagePtr& msg)`
- `parseMapMoveEast(const InputMessagePtr& msg)`
- `parseMapMoveSouth(const InputMessagePtr& msg)`
- `parseMapMoveWest(const InputMessagePtr& msg)`
- `parseUpdateTile(const InputMessagePtr& msg)`
- `parseTileAddThing(const InputMessagePtr& msg)`
- `parseTileTransformThing(const InputMessagePtr& msg)`
- `parseTileRemoveThing(const InputMessagePtr& msg)`
- `parseCreatureMove(const InputMessagePtr& msg)`
- `parseOpenContainer(const InputMessagePtr& msg)`
- `parseCloseContainer(const InputMessagePtr& msg)`
- `parseContainerAddItem(const InputMessagePtr& msg)`
- `parseContainerUpdateItem(const InputMessagePtr& msg)`
- `parseContainerRemoveItem(const InputMessagePtr& msg)`
- `parseAddInventoryItem(const InputMessagePtr& msg)`
- `parseRemoveInventoryItem(const InputMessagePtr& msg)`
- `parseOpenNpcTrade(const InputMessagePtr& msg)`
- `parsePlayerGoods(const InputMessagePtr& msg)`
- `parseCloseNpcTrade(const InputMessagePtr&)`
- `parseWorldLight(const InputMessagePtr& msg)`
- `parseMagicEffect(const InputMessagePtr& msg)`
- `parseAnimatedText(const InputMessagePtr& msg)`
- `parseDistanceMissile(const InputMessagePtr& msg)`
- `parseCreatureMark(const InputMessagePtr& msg)`
- `parseTrappers(const InputMessagePtr& msg)`
- `parseCreatureHealth(const InputMessagePtr& msg)`
- `parseCreatureLight(const InputMessagePtr& msg)`
- `parseCreatureOutfit(const InputMessagePtr& msg)`
- `parseCreatureSpeed(const InputMessagePtr& msg)`
- `parseCreatureSkulls(const InputMessagePtr& msg)`
- `parseCreatureShields(const InputMessagePtr& msg)`
- `parseCreatureUnpass(const InputMessagePtr& msg)`
- `parseEditText(const InputMessagePtr& msg)`
- `parseEditList(const InputMessagePtr& msg)`
- `parsePremiumTrigger(const InputMessagePtr& msg)`
- `parsePreyFreeRolls(const InputMessagePtr& msg)`
- `parsePreyTimeLeft(const InputMessagePtr& msg)`
- `parsePreyData(const InputMessagePtr& msg)`
- `parsePreyPrices(const InputMessagePtr& msg)`
- `parseStoreOfferDescription(const InputMessagePtr& msg)`
- `parsePlayerInfo(const InputMessagePtr& msg)`
- `parsePlayerStats(const InputMessagePtr& msg)`
- `parsePlayerSkills(const InputMessagePtr& msg)`
- `parsePlayerState(const InputMessagePtr& msg)`
- `parsePlayerCancelAttack(const InputMessagePtr& msg)`
- `parsePlayerModes(const InputMessagePtr& msg)`
- `parseSpellCooldown(const InputMessagePtr& msg)`
- `parseSpellGroupCooldown(const InputMessagePtr& msg)`
- `parseMultiUseCooldown(const InputMessagePtr& msg)`
- `parseTalk(const InputMessagePtr& msg)`
- `parseChannelList(const InputMessagePtr& msg)`
- `parseOpenChannel(const InputMessagePtr& msg)`
- `parseOpenPrivateChannel(const InputMessagePtr& msg)`
- `parseOpenOwnPrivateChannel(const InputMessagePtr& msg)`
- `parseCloseChannel(const InputMessagePtr& msg)`
- `parseRuleViolationChannel(const InputMessagePtr& msg)`
- `parseRuleViolationRemove(const InputMessagePtr& msg)`
- `parseRuleViolationCancel(const InputMessagePtr& msg)`
- `parseRuleViolationLock(const InputMessagePtr& msg)`
- `parseOwnTrade(const InputMessagePtr& msg)`
- `parseCounterTrade(const InputMessagePtr& msg)`
- `parseCloseTrade(const InputMessagePtr&)`
- `parseTextMessage(const InputMessagePtr& msg)`
- `parseCancelWalk(const InputMessagePtr& msg)`
- `parseWalkWait(const InputMessagePtr& msg)`
- `parseFloorChangeUp(const InputMessagePtr& msg)`
- `parseFloorChangeDown(const InputMessagePtr& msg)`
- `parseOpenOutfitWindow(const InputMessagePtr& msg)`
- `parseVipAdd(const InputMessagePtr& msg)`
- `parseVipState(const InputMessagePtr& msg)`
- `parseVipLogout(const InputMessagePtr& msg)`
- `parseVipGroupData(const InputMessagePtr& msg)`
- `parseTutorialHint(const InputMessagePtr& msg)`
- `parseCyclopediaMapData(const InputMessagePtr& msg)`
- `parseQuestLog(const InputMessagePtr& msg)`
- `parseQuestLine(const InputMessagePtr& msg)`
- `parseChannelEvent(const InputMessagePtr& msg)`
- `parseItemInfo(const InputMessagePtr& msg)`
- `parsePlayerInventory(const InputMessagePtr& msg)`
- `parseModalDialog(const InputMessagePtr& msg)`
- `parseClientCheck(const InputMessagePtr& msg)`
- `parseGameNews(const InputMessagePtr& msg)`
- `parseMessageDialog(const InputMessagePtr& msg)`
- `parseBlessDialog(const InputMessagePtr& msg)`
- `parseResourceBalance(const InputMessagePtr& msg)`
- `parseServerTime(const InputMessagePtr& msg)`
- `parseQuestTracker(const InputMessagePtr& msg)`
- `parseImbuementWindow(const InputMessagePtr& msg)`
- `parseCloseImbuementWindow(const InputMessagePtr& msg)`
- `parseCyclopediaNewDetails(const InputMessagePtr& msg)`
- `parseCyclopedia(const InputMessagePtr& msg)`
- `parseDailyRewardState(const InputMessagePtr& msg)`
- `parseOpenRewardWall(const InputMessagePtr& msg)`
- `parseDailyReward(const InputMessagePtr& msg)`
- `parseDailyRewardHistory(const InputMessagePtr& msg)`
- `parseKillTracker(const InputMessagePtr& msg)`
- `parseLootContainers(const InputMessagePtr& msg)`
- `parseSupplyStash(const InputMessagePtr& msg)`
- `parseSpecialContainer(const InputMessagePtr& msg)`
- `parseDepotState(const InputMessagePtr& msg)`
- `parseSupplyTracker(const InputMessagePtr& msg)`
- `parseTournamentLeaderboard(const InputMessagePtr& msg)`
- `parseImpactTracker(const InputMessagePtr& msg)`
- `parseItemsPrices(const InputMessagePtr& msg)`
- `parseLootTracker(const InputMessagePtr& msg)`
- `parseItemDetail(const InputMessagePtr& msg)`
- `parseHunting(const InputMessagePtr& msg)`
- `parseExtendedOpcode(const InputMessagePtr& msg)`
- `parseChangeMapAwareRange(const InputMessagePtr& msg)`
- `parseProgressBar(const InputMessagePtr& msg)`
- `parseFeatures(const InputMessagePtr& msg)`
- `parseCreaturesMark(const InputMessagePtr& msg)`
- `parseNewCancelWalk(const InputMessagePtr& msg)`
- `parsePredictiveCancelWalk(const InputMessagePtr& msg)`
- `parseWalkId(const InputMessagePtr& msg)`
- `parseProcessesRequest(const InputMessagePtr& msg)`
- `parseDllsRequest(const InputMessagePtr& msg)`
- `parseWindowsRequest(const InputMessagePtr& msg)`
- `setMapDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height)`
- `setFloorDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height, int offset, int skip)`
- `setTileDescription(const InputMessagePtr& msg, Position position)`
- `getOutfit(const InputMessagePtr& msg, bool ignoreMount = false)`
- `getThing(const InputMessagePtr& msg)`
- `getMappedThing(const InputMessagePtr & msg)`
- `getCreature(const InputMessagePtr& msg, int type = 0)`
- `getStaticText(const InputMessagePtr& msg, int type = 0)`
- `getItem(const InputMessagePtr& msg, int id = 0, bool hasDescription = true)`
- `getPosition(const InputMessagePtr& msg)`
- `getImbuementInfo(const InputMessagePtr& msg)`
- `getRecivedPacketsCount()`
- `getRecivedPacketsSize()`

## client/protocolgameparse.cpp

- `s(STATS_PACKETS, std::to_string((int)opcode))`
- `parseLogin(msg)`
- `parseGMActions(msg)`
- `parseUpdateNeeded(msg)`
- `parseLoginError(msg)`
- `parseLoginAdvice(msg)`
- `parseLoginWait(msg)`
- `parseLoginToken(msg)`
- `parsePing(msg)`
- `parseChallenge(msg)`
- `parseNewPing(msg)`
- `parseDeath(msg)`
- `parseMapDescription(msg)`
- `parseMapMoveNorth(msg)`
- `parseMapMoveEast(msg)`
- `parseMapMoveSouth(msg)`
- `parseMapMoveWest(msg)`
- `parseUpdateTile(msg)`
- `parseTileAddThing(msg)`
- `parseTileTransformThing(msg)`
- `parseTileRemoveThing(msg)`
- `parseCreatureMove(msg)`
- `parseOpenContainer(msg)`
- `parseCloseContainer(msg)`
- `parseContainerAddItem(msg)`
- `parseContainerUpdateItem(msg)`
- `parseContainerRemoveItem(msg)`
- `parseAddInventoryItem(msg)`
- `parseRemoveInventoryItem(msg)`
- `parseOpenNpcTrade(msg)`
- `parsePlayerGoods(msg)`
- `parseCloseNpcTrade(msg)`
- `parseOwnTrade(msg)`
- `parseCounterTrade(msg)`
- `parseCloseTrade(msg)`
- `parseWorldLight(msg)`
- `parseMagicEffect(msg)`
- `parseAnimatedText(msg)`
- `parseDistanceMissile(msg)`
- `parseCreatureMark(msg)`
- `parseTrappers(msg)`
- `parseCreatureHealth(msg)`
- `parseCreatureLight(msg)`
- `parseCreatureOutfit(msg)`
- `parseCreatureSpeed(msg)`
- `parseCreatureSkulls(msg)`
- `parseCreatureShields(msg)`
- `parseCreatureUnpass(msg)`
- `parseEditText(msg)`
- `parseEditList(msg)`
- `parsePremiumTrigger(msg)`
- `parsePlayerStats(msg)`
- `parsePlayerSkills(msg)`
- `parsePlayerState(msg)`
- `parsePlayerCancelAttack(msg)`
- `parsePlayerModes(msg)`
- `parseTalk(msg)`
- `parseChannelList(msg)`
- `parseOpenChannel(msg)`
- `parseOpenPrivateChannel(msg)`
- `parseRuleViolationChannel(msg)`
- `parseRuleViolationRemove(msg)`
- `parseRuleViolationCancel(msg)`
- `parseRuleViolationLock(msg)`
- `parseOpenOwnPrivateChannel(msg)`
- `parseCloseChannel(msg)`
- `parseTextMessage(msg)`
- `parseCancelWalk(msg)`
- `parseWalkWait(msg)`
- `parseFloorChangeUp(msg)`
- `parseFloorChangeDown(msg)`
- `parseOpenOutfitWindow(msg)`
- `parseVipAdd(msg)`
- `parseVipState(msg)`
- `parseVipLogout(msg)`
- `parseTutorialHint(msg)`
- `parseCyclopediaMapData(msg)`
- `parseQuestLog(msg)`
- `parseQuestLine(msg)`
- `parseSpellCooldown(msg)`
- `parseSpellGroupCooldown(msg)`
- `parseMultiUseCooldown(msg)`
- `parseChannelEvent(msg)`
- `parseItemInfo(msg)`
- `parsePlayerInventory(msg)`
- `parsePlayerInfo(msg)`
- `parseModalDialog(msg)`
- `parseLogin(msg)`
- `parseEnterGame(msg)`
- `parsePlayerHelpers(msg)`
- `parseCreaturesMark(msg)`
- `parseCreatureType(msg)`
- `parseBlessings(msg)`
- `parseUnjustifiedStats(msg)`
- `parsePvpSituations(msg)`
- `parsePreset(msg)`
- `parseCoinBalanceUpdate(msg)`
- `parseCoinBalance(msg)`
- `parseRequestPurchaseData(msg)`
- `parseCompleteStorePurchase(msg)`
- `parseStore(msg)`
- `parseStoreOffers(msg)`
- `parseStoreTransactionHistory(msg)`
- `parseStoreError(msg)`
- `parseStoreButtonIndicators(msg)`
- `parseSetStoreDeepLink(msg)`
- `parseRestingAreaState(msg)`
- `parseClientCheck(msg)`
- `parseGameNews(msg)`
- `parseBlessDialog(msg)`
- `parseMessageDialog(msg)`
- `parseResourceBalance(msg)`
- `parseServerTime(msg)`
- `parsePreyFreeRolls(msg)`
- `parsePreyTimeLeft(msg)`
- `parsePreyData(msg)`
- `parsePreyPrices(msg)`
- `parseStoreOfferDescription(msg)`
- `parseImpactTracker(msg)`
- `parseItemsPrices(msg)`
- `parseSupplyTracker(msg)`
- `parseLootTracker(msg)`
- `parseQuestTracker(msg)`
- `parseKillTracker(msg)`
- `parseImbuementWindow(msg)`
- `parseCloseImbuementWindow(msg)`
- `parseCyclopediaNewDetails(msg)`
- `parseCyclopedia(msg)`
- `parseDailyRewardState(msg)`
- `parseOpenRewardWall(msg)`
- `parseDailyReward(msg)`
- `parseDailyRewardHistory(msg)`
- `parseLootContainers(msg)`
- `parseSupplyStash(msg)`
- `parseSpecialContainer(msg)`
- `parseTournamentLeaderboard(msg)`
- `parseItemDetail(msg)`
- `parseHunting(msg)`
- `parseExtendedOpcode(msg)`
- `parseChangeMapAwareRange(msg)`
- `parseProgressBar(msg)`
- `parseFeatures(msg)`
- `parseFloorDescription(msg)`
- `parseProcessesRequest(msg)`
- `parseDllsRequest(msg)`
- `parseWindowsRequest(msg)`
- `packet("packet.log", std::ifstream::app)`
- `getOutfit(msg, true)`
- `getOutfit(msg, true)`
- `items(itemCount)`
- `items(count)`
- `items(count)`
- `Missile())`
- `Missile())`
- `Effect())`
- `Effect())`
- `Missile())`
- `item(new Item)`
- `callLuaField("onExtendedOpcode", opcode, buffer)`
- `tilePos(x + nx + offset, y + ny + offset, z)`
- `id(0)")`
- `Position(x, y, z)`

## client/protocolgamesend.cpp

- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `generateXteaKey()`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `addPosition(msg, pos)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`
- `msg(new OutputMessage)`

## client/spritemanager.cpp

- `loadCwmSpr(cwmFile)`
- `loadCasualSpr(sprFile)`
- `spriteData(m_spriteSize * m_spriteSize)`
- `buffer(pixelCount + 1024, 0)`
- `buffer(pixelCount + 1024, 0)`
- `getSpriteImageHd(id)`
- `getSpriteImageCasual(id)`
- `image(new Image(Size(m_spriteSize, m_spriteSize)))`
- `image(new Image(Size(m_spriteSize, m_spriteSize)))`

## client/spritemanager.h

class SpriteManager
- `SpriteManager()`
- `terminate()`
- `loadSpr(std::string file)`
- `unload()`
- `saveSpr(std::string fileName)`
- `saveSpr64(std::string fileName)`
- `encryptSprites(std::string fileName)`
- `dumpSprites(std::string dir)`
- `getSignature()`
- `getSpritesCount()`
- `getSpriteImage(int id)`
- `isLoaded()`
- `spriteSize()`
- `getOffsetFactor()`
- `isHdMod()`
- `loadCasualSpr(std::string file)`
- `loadCwmSpr(std::string file)`
- `getSpriteImageCasual(int id)`
- `getSpriteImageHd(int id)`

## client/statictext.cpp

- `addColoredMessage(name, mode, { text, "" })`

## client/statictext.h

class StaticText
- `StaticText()`
- `drawText(const Point& dest, const Rect& parentRect)`
- `getName()`
- `getText()`
- `getMessageMode()`
- `getFirstMessage()`
- `isYell()`
- `setText(const std::string& text)`
- `setFont(const std::string& fontName)`
- `addMessage(const std::string& name, Otc::MessageMode mode, const std::string& text)`
- `addColoredMessage(const std::string& name, Otc::MessageMode mode, const std::vector<std::string>& texts)`
- `asStaticText()`
- `isStaticText()`
- `setColor(const Color& color)`
- `getColor()`
- `hasText()`
- `update()`
- `scheduleUpdate()`
- `compose()`

## client/thing.h

class Thing
- `Thing()`
- `draw(const Point& dest, bool animate = true, LightView* lightView = nullptr)`
- `setId(uint32 id)`
- `setPosition(const Position& position)`
- `getId()`
- `getPosition()`
- `getStackPriority()`
- `getParentContainer()`
- `getStackPos()`
- `setMarked(const std::string& color)`
- `updatedMarkedColor()`
- `isItem()`
- `isEffect()`
- `isMissile()`
- `isCreature()`
- `isNpc()`
- `isMonster()`
- `isPlayer()`
- `isLocalPlayer()`
- `isAnimatedText()`
- `isStaticText()`
- `getSize()`
- `rawGetThingType()->getSize()`
- `getWidth()`
- `rawGetThingType()->getWidth()`
- `getHeight()`
- `rawGetThingType()->getHeight()`
- `getDisplacement()`
- `rawGetThingType()->getDisplacement()`
- `getDisplacementX()`
- `rawGetThingType()->getDisplacementX()`
- `getDisplacementY()`
- `rawGetThingType()->getDisplacementY()`
- `getExactSize(int layer, int xPattern, int yPattern, int zPattern, int animationPhase)`
- `rawGetThingType()->getExactSize(layer, xPattern, yPattern, zPattern, animationPhase)`
- `getLayers()`
- `rawGetThingType()->getLayers()`
- `getNumPatternX()`
- `rawGetThingType()->getNumPatternX()`
- `getNumPatternY()`
- `rawGetThingType()->getNumPatternY()`
- `getNumPatternZ()`
- `rawGetThingType()->getNumPatternZ()`
- `getAnimationPhases()`
- `rawGetThingType()->getAnimationPhases()`
- `getAnimator()`
- `rawGetThingType()->getAnimator()`
- `getIdleAnimator()`
- `rawGetThingType()->getIdleAnimator()`
- `getGroundSpeed()`
- `rawGetThingType()->getGroundSpeed()`
- `getMaxTextLength()`
- `rawGetThingType()->getMaxTextLength()`
- `getLight()`
- `rawGetThingType()->getLight()`
- `getMinimapColor()`
- `rawGetThingType()->getMinimapColor()`
- `getLensHelp()`
- `rawGetThingType()->getLensHelp()`
- `getClothSlot()`
- `rawGetThingType()->getClothSlot()`
- `getElevation()`
- `rawGetThingType()->getElevation()`
- `isGround()`
- `rawGetThingType()->isGround()`
- `isGroundBorder()`
- `rawGetThingType()->isGroundBorder()`
- `isOnBottom()`
- `rawGetThingType()->isOnBottom()`
- `isOnTop()`
- `rawGetThingType()->isOnTop()`
- `isContainer()`
- `rawGetThingType()->isContainer()`
- `isStackable()`
- `rawGetThingType()->isStackable()`
- `isForceUse()`
- `rawGetThingType()->isForceUse()`
- `isMultiUse()`
- `rawGetThingType()->isMultiUse()`
- `isWritable()`
- `rawGetThingType()->isWritable()`
- `isChargeable()`
- `rawGetThingType()->isChargeable()`
- `isWritableOnce()`
- `rawGetThingType()->isWritableOnce()`
- `isFluidContainer()`
- `rawGetThingType()->isFluidContainer()`
- `isSplash()`
- `rawGetThingType()->isSplash()`
- `isNotWalkable()`
- `rawGetThingType()->isNotWalkable()`
- `isNotMoveable()`
- `rawGetThingType()->isNotMoveable()`
- `blockProjectile()`
- `rawGetThingType()->blockProjectile()`
- `isNotPathable()`
- `rawGetThingType()->isNotPathable()`
- `isPickupable()`
- `rawGetThingType()->isPickupable()`
- `isHangable()`
- `rawGetThingType()->isHangable()`
- `isHookSouth()`
- `rawGetThingType()->isHookSouth()`
- `isHookEast()`
- `rawGetThingType()->isHookEast()`
- `isRotateable()`
- `rawGetThingType()->isRotateable()`
- `hasLight()`
- `rawGetThingType()->hasLight()`
- `isDontHide()`
- `rawGetThingType()->isDontHide()`
- `isTranslucent()`
- `rawGetThingType()->isTranslucent()`
- `hasDisplacement()`
- `rawGetThingType()->hasDisplacement()`
- `hasElevation()`
- `rawGetThingType()->hasElevation()`
- `isLyingCorpse()`
- `rawGetThingType()->isLyingCorpse()`
- `isAnimateAlways()`
- `rawGetThingType()->isAnimateAlways()`
- `hasMiniMapColor()`
- `rawGetThingType()->hasMiniMapColor()`
- `hasLensHelp()`
- `rawGetThingType()->hasLensHelp()`
- `isFullGround()`
- `rawGetThingType()->isFullGround()`
- `isIgnoreLook()`
- `rawGetThingType()->isIgnoreLook()`
- `isCloth()`
- `rawGetThingType()->isCloth()`
- `isMarketable()`
- `rawGetThingType()->isMarketable()`
- `isUsable()`
- `rawGetThingType()->isUsable()`
- `isWrapable()`
- `rawGetThingType()->isWrapable()`
- `isUnwrapable()`
- `rawGetThingType()->isUnwrapable()`
- `isTopEffect()`
- `rawGetThingType()->isTopEffect()`
- `getMarketData()`
- `rawGetThingType()->getMarketData()`
- `hide()`
- `show()`
- `setHidden(bool value)`
- `isHidden()`
- `onPositionChange(const Position& newPos, const Position& oldPos)`
- `onAppear()`
- `onDisappear()`

## client/thingstype.h

class ThingsType
- `load(const std::string& file)`
- `unload()`
- `parseThingType(const FileStreamPtr& fin, ThingType& thingType)`
- `getSignature()`
- `isLoaded()`
- `getFirstItemId()`
- `getMaxItemid()`
- `isValidItemId(int id)`

## client/thingtype.cpp

- `sprites(std::move(m_spritesIndex))`
- `image(new Image(Size(spriteSize * m_size.width() * m_layers * m_numPatternX, spriteSize * m_size.height() * m_animationPhases * m_numPatternY * m_numPatternZ)))`
- `newSprite(new Image(Size(orgSprite->getSize() * 2)))`
- `screenRect(dest + (textureOffset - m_displacement * g_sprites.getOffsetFactor() - (m_size.toPoint() - Point(1, 1)) * g_sprites.spriteSize()), textureRect.size())`
- `screenRect(dest + (textureOffset - m_displacement * g_sprites.getOffsetFactor() - (m_size.toPoint() - Point(1, 1)) * g_sprites.spriteSize()), textureRect.size())`
- `Rect(0, 0, 1, 1)`
- `Rect(0, 0, 1, 1)`
- `Rect(0, 0, 1, 1)`
- `Rect(0, 0, 1, 1)`
- `Rect(dest + textureOffset - m_displacement - (m_size.toPoint() - Point(1, 1)) * g_sprites.spriteSize(), textureRect.size())`
- `screenRect(dest + (textureOffset - m_displacement * g_sprites.getOffsetFactor() - (m_size.toPoint() - Point(1, 1)) * g_sprites.spriteSize()), textureRect.size())`
- `DrawQueueItemThingWithShader(screenRect, texture, textureRect, textureOffset, screenRect.center(), 0, shader)`
- `DrawQueueItemThingWithShader(screenRect, texture, textureRect, textureOffset, screenRect.center(), 0, shader)`
- `Image(textureSize * spriteSize))`
- `drawRect(framePos + Point(m_size.width(), m_size.height()) * spriteSize - Point(1,1), framePos)`
- `Texture(fullImage, true, false, true))`

## client/thingtype.h

class ThingType
- `ThingType()`
- `unserialize(uint16 clientId, ThingCategory category, const FileStreamPtr& fin)`
- `unserializeOtml(const OTMLNodePtr& node)`
- `unload()`
- `serialize(const FileStreamPtr& fin)`
- `exportImage(std::string fileName)`
- `replaceSprites(std::map<uint32_t, ImagePtr>& replacements, std::string fileName)`
- `drawOutfit(const Point& dest, int maskLayer, int xPattern, int yPattern, int zPattern, int animationPhase, Color color = Color::white, LightView* lightView = nullptr)`
- `getDrawSize(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase)`
- `drawWithShader(const Point& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white, LightView* lightView = nullptr)`
- `drawWithShader(const Rect& dest, int layer, int xPattern, int yPattern, int zPattern, int animationPhase, const std::string& shader, Color color = Color::white)`
- `getId()`
- `getCategory()`
- `isNull()`
- `hasAttr(ThingAttr attr)`
- `isLoaded()`
- `getLastUsage()`
- `getSize()`
- `getWidth()`
- `getHeight()`
- `getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0)`
- `getRealSize()`
- `getLayers()`
- `getNumPatternX()`
- `getNumPatternY()`
- `getNumPatternZ()`
- `getAnimationPhases()`
- `getAnimator()`
- `getIdleAnimator()`
- `getDisplacement()`
- `getDisplacementX()`
- `getDisplacementY()`
- `getElevation()`
- `getGroundSpeed()`
- `getMaxTextLength()`
- `getLight()`
- `getMinimapColor()`
- `getLensHelp()`
- `getClothSlot()`
- `getMarketData()`
- `isGround()`
- `isGroundBorder()`
- `isOnBottom()`
- `isOnTop()`
- `isContainer()`
- `isStackable()`
- `isForceUse()`
- `isMultiUse()`
- `isWritable()`
- `isChargeable()`
- `isWritableOnce()`
- `isFluidContainer()`
- `isSplash()`
- `isNotWalkable()`
- `isNotMoveable()`
- `blockProjectile()`
- `isNotPathable()`
- `isPickupable()`
- `isHangable()`
- `isHookSouth()`
- `isHookEast()`
- `isRotateable()`
- `hasLight()`
- `isDontHide()`
- `isTranslucent()`
- `hasDisplacement()`
- `hasElevation()`
- `isLyingCorpse()`
- `isAnimateAlways()`
- `hasMiniMapColor()`
- `hasLensHelp()`
- `isFullGround()`
- `isIgnoreLook()`
- `isCloth()`
- `isMarketable()`
- `isUsable()`
- `isWrapable()`
- `isUnwrapable()`
- `isTopEffect()`
- `hasBones()`
- `getSprites()`
- `getOpacity()`
- `isNotPreWalkable()`
- `setPathable(bool var)`
- `getBestTextureDimension(int w, int h, int count)`
- `getSpriteIndex(int w, int h, int l, int x, int y, int z, int a)`
- `getTextureIndex(int l, int x, int y, int z)`
- `draw()`
- `draw(const Point& pos)`
- `cache()`

## client/thingtypemanager.cpp

- `type(new ThingType)`
- `OTMLException(node, "not a valid thing category")`
- `OTMLException(node2, "thing not found")`
- `itemType(new ItemType)`
- `parseItemType(atoi(s.c_str()), element)`

## client/thingtypemanager.h

class ThingTypeManager
- `init()`
- `terminate()`
- `check()`
- `loadDat(std::string file)`
- `loadOtml(std::string file)`
- `loadOtb(const std::string& file)`
- `loadXml(const std::string& file)`
- `parseItemType(uint16 id, TiXmlElement *elem)`
- `saveDat(std::string fileName)`
- `dumpTextures(std::string dir)`
- `replaceTextures(std::string dir)`
- `addItemType(const ItemTypePtr& itemType)`
- `findItemTypesByName(std::string name)`
- `findItemTypesByString(std::string str)`
- `getMarketCategories()`
- `findThingTypeByAttr(ThingAttr attr, ThingCategory category)`
- `findItemTypeByCategory(ItemCategory category)`
- `getDatSignature()`
- `getOtbMajorVersion()`
- `getOtbMinorVersion()`
- `getContentRevision()`
- `isDatLoaded()`
- `isXmlLoaded()`
- `isOtbLoaded()`
- `isValidDatId(uint16 id, ThingCategory category)`
- `isValidOtbId(uint16 id)`

## client/tile.cpp

- `StaticText())`
- `300000(300s)!")`
- `StaticText())`

## client/tile.h

class Tile
- `calculateCorpseCorrection()`
- `drawGround(const Point& dest, LightView* lightView = nullptr)`
- `drawBottom(const Point& dest, LightView* lightView = nullptr)`
- `drawCreatures(const Point& dest, LightView* lightView = nullptr)`
- `drawTop(const Point& dest, LightView* lightView = nullptr)`
- `drawTexts(Point dest)`
- `drawWidget(Point dest)`
- `clean()`
- `addWalkingCreature(const CreaturePtr& creature)`
- `removeWalkingCreature(const CreaturePtr& creature)`
- `addThing(const ThingPtr& thing, int stackPos)`
- `removeThing(ThingPtr thing)`
- `getThing(int stackPos)`
- `getEffect(uint16 id)`
- `hasThing(const ThingPtr& thing)`
- `getThingStackPos(const ThingPtr& thing)`
- `getTopThing()`
- `getTopLookThing()`
- `getTopLookThingEx(Point offset)`
- `getTopUseThing()`
- `getTopCreature()`
- `getTopCreatureEx(Point offset)`
- `getTopMoveThing()`
- `getTopMultiUseThing()`
- `getTopMultiUseThingEx(Point offset)`
- `getDrawElevation()`
- `getItems()`
- `getCreatures()`
- `getWalkingCreatures()`
- `getThings()`
- `getEffects()`
- `getGround()`
- `getGroundSpeed()`
- `isBlocking()`
- `getMinimapColorByte()`
- `getThingCount()`
- `isPathable()`
- `isWalkable(bool ignoreCreatures = false)`
- `isFullGround()`
- `isFullyOpaque()`
- `isSingleDimension()`
- `isLookPossible()`
- `isBlockingProjectile()`
- `isClickable()`
- `isEmpty()`
- `isDrawable()`
- `hasTranslucentLight()`
- `mustHookSouth()`
- `mustHookEast()`
- `hasCreature()`
- `hasBlockingCreature()`
- `limitsFloorsView(bool isFreeView = false)`
- `canErase()`
- `getElevation()`
- `hasElevation(int elevation = 1)`
- `overwriteMinimapColor(uint8 color)`
- `remFlag(uint32 flag)`
- `setFlag(uint32 flag)`
- `setFlags(uint32 flags)`
- `hasFlag(uint32 flag)`
- `getFlags()`
- `setHouseId(uint32 hid)`
- `getHouseId()`
- `isHouseTile()`
- `select()`
- `unselect()`
- `isSelected()`
- `asTile()`
- `setSpeed(uint16_t speed, uint8_t blocking)`
- `setText(const std::string& text, Color color)`
- `getText()`
- `setTimer(int time, Color color)`
- `getTimer()`
- `setFill(Color color)`
- `resetFill()`
- `canShoot(int distance)`
- `setWidget(UIWidgetPtr widget)`
- `getWidget()`
- `removeWidget()`
- `checkTranslucentLight()`

## client/towns.h

class Town
class TownManager
- `Town()`
- `setId(uint32 tid)`
- `setName(const std::string& name)`
- `setPos(const Position& pos)`
- `getId()`
- `getName()`
- `getPos()`
- `TownManager()`
- `addTown(const TownPtr& town)`
- `removeTown(uint32 townId)`
- `sort()`
- `getTowns()`
- `clear()`
- `findTown(uint32 townId)`

## client/uicreature.h

class UICreature
- `drawSelf(Fw::DrawPane drawPane)`
- `setCreature(const CreaturePtr& creature)`
- `setFixedCreatureSize(bool fixed)`
- `setOutfit(const Outfit& outfit)`
- `getCreature()`
- `getOutfit()`
- `isFixedCreatureSize()`
- `setAutoRotating(bool value)`
- `setDirection(Otc::Direction direction)`
- `getDirection()`
- `setScale(float scale)`
- `getScale()`
- `setAnimate(bool value)`
- `isAnimating()`
- `setCenter(bool value)`
- `setOldScaling(bool value)`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`
- `onGeometryChange(const Rect& oldRect, const Rect& newRect)`

## client/uigraph.h

class UIGraph
- `UIGraph()`
- `drawSelf(Fw::DrawPane drawPane)`
- `clear()`
- `addValue(int value, bool ignoreSmallValues = false)`
- `setLineWidth(int width)`
- `setCapacity(int capacity)`
- `setTitle(const std::string& title)`
- `setShowLabels(bool value)`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`

## client/uiitem.h

class UIItem
- `UIItem()`
- `drawSelf(Fw::DrawPane drawPane)`
- `setItemId(int id)`
- `setItemCount(int count)`
- `setItemSubType(int subType)`
- `setItemVisible(bool visible)`
- `setItem(const ItemPtr& item)`
- `setVirtual(bool virt)`
- `clearItem()`
- `setShowCount(bool value)`
- `setItemShader(const std::string& str)`
- `getItemId()`
- `getItemCount()`
- `getItemSubType()`
- `getItemCountOrSubType()`
- `getItem()`
- `isVirtual()`
- `isItemVisible()`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`
- `cacheCountText()`

## client/uimap.cpp

- `Position()`
- `Point(0, 0)`

## client/uimap.h

class UIMap
- `UIMap()`
- `onMouseMove(const Point& mousePos, const Point& mouseMoved)`
- `drawSelf(Fw::DrawPane drawPane)`
- `movePixels(int x, int y)`
- `setZoom(int zoom)`
- `zoomIn()`
- `zoomOut()`
- `followCreature(const CreaturePtr& creature)`
- `setCameraPosition(const Position& pos)`
- `setMaxZoomIn(int maxZoomIn)`
- `setMaxZoomOut(int maxZoomOut)`
- `setMultifloor(bool enable)`
- `lockVisibleFloor(int floor)`
- `unlockVisibleFloor()`
- `setVisibleDimension(const Size& visibleDimension)`
- `setDrawFlags(Otc::DrawFlags drawFlags)`
- `setDrawTexts(bool enable)`
- `setDrawNames(bool enable)`
- `setDrawHealthBars(bool enable)`
- `setDrawHealthBarsOnTop(bool enable)`
- `setDrawLights(bool enable)`
- `setDrawManaBar(bool enable)`
- `setDrawPlayerBars(bool enable)`
- `setAnimated(bool enable)`
- `setKeepAspectRatio(bool enable)`
- `setMinimumAmbientLight(float intensity)`
- `setLimitVisibleRange(bool limitVisibleRange)`
- `setFloorFading(int value)`
- `setCrosshair(const std::string& type)`
- `isMultifloor()`
- `isDrawingTexts()`
- `isDrawingNames()`
- `isDrawingHealthBars()`
- `isDrawingHealthBarsOnTop()`
- `isDrawingLights()`
- `isDrawingManaBar()`
- `isAnimating()`
- `isKeepAspectRatioEnabled()`
- `isLimitVisibleRangeEnabled()`
- `getVisibleDimension()`
- `getFollowingCreature()`
- `getDrawFlags()`
- `getCameraPosition()`
- `getPosition(const Point& mousePos)`
- `getPositionOffset(const Point& mousePos)`
- `getTile(const Point& mousePos)`
- `getMaxZoomIn()`
- `getMaxZoomOut()`
- `getZoom()`
- `getMinimumAmbientLight()`
- `setShader(const std::string& shader)`
- `getShader()`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`
- `onGeometryChange(const Rect& oldRect, const Rect& newRect)`
- `updateVisibleDimension()`
- `updateMapSize()`

## client/uimapanchorlayout.cpp

- `VALIDATE(false)`
- `anchor(new UIPositionAnchor(anchoredEdge, hookedPosition, hookedEdge))`
- `update()`

## client/uimapanchorlayout.h

class UIPositionAnchor
class UIMapAnchorLayout
- `getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget)`
- `getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget)`
- `UIMapAnchorLayout(UIWidgetPtr parentWidget) : UIAnchorLayout(parentWidget)`
- `centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition)`
- `fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition)`

## client/uiminimap.cpp

- `UIMapAnchorLayout(static_self_cast<UIWidget>()))`

## client/uiminimap.h

class UIMinimap
- `UIMinimap()`
- `drawSelf(Fw::DrawPane drawPane)`
- `zoomIn()`
- `setZoom(m_zoom+1)`
- `zoomOut()`
- `setZoom(m_zoom-1)`
- `setZoom(int zoom)`
- `setMinZoom(int minZoom)`
- `setMaxZoom(int maxZoom)`
- `setCameraPosition(const Position& pos)`
- `floorUp()`
- `floorDown()`
- `getTilePoint(const Position& pos)`
- `getTileRect(const Position& pos)`
- `getTilePosition(const Point& mousePos)`
- `getCameraPosition()`
- `getMinZoom()`
- `getMaxZoom()`
- `getZoom()`
- `getScale()`
- `anchorPosition(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge)`
- `fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition)`
- `centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition)`
- `onZoomChange(int zoom, int oldZoom)`
- `onCameraPositionChange(const Position& position, const Position& oldPosition)`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`
- `update()`

## client/uiprogressrect.h

class UIProgressRect
- `UIProgressRect()`
- `drawSelf(Fw::DrawPane drawPane)`
- `setPercent(float percent)`
- `getPercent()`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`

## client/uisprite.cpp

- `Texture(image)`

## client/uisprite.h

class UISprite
- `UISprite()`
- `drawSelf(Fw::DrawPane drawPane)`
- `setSpriteId(uint32 id)`
- `getSpriteId()`
- `clearSprite()`
- `setSpriteColor(Color color)`
- `isSpriteVisible()`
- `setSpriteVisible(bool visible)`
- `hasSprite()`
- `onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode)`

## client/walkmatrix.h

class WalkMatrix
- `updatePosition(const Position& newPos)`
- `clear()`
- `inRange(const Position& pos2)`
- `update(const Position& pos2, int32_t value = 0)`
- `get(const Position& pos2)`
- `clear()`
- `reset(uint32_t value = 0)`
- `dump()`