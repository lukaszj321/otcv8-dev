---
title: "src/client/game.h"
source_file: "src/client/game.h"
generated_at: "2025-11-01T08:45:15.276Z"
doc_type: "cpp_api"
---

# src/client/game.h

(game)=
## `Game`

**Signature:**
```cpp
public: Game();
```

---

(init)=
## `init`

**Signature:**
```cpp
void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(resetgamestates)=
## `resetGameStates`

**Signature:**
```cpp
private: void resetGameStates();
```

---

(processconnectionerror)=
## `processConnectionError`

**Signature:**
```cpp
protected: void processConnectionError(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(processdisconnect)=
## `processDisconnect`

**Signature:**
```cpp
void processDisconnect();
```

---

(processping)=
## `processPing`

**Signature:**
```cpp
void processPing();
```

---

(processpingback)=
## `processPingBack`

**Signature:**
```cpp
void processPingBack();
```

---

(processnewping)=
## `processNewPing`

**Signature:**
```cpp
void processNewPing(uint32_t pingId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `pingId` | - |

---

(processupdateneeded)=
## `processUpdateNeeded`

**Signature:**
```cpp
void processUpdateNeeded(const std::string& signature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `signature` | - |

---

(processloginerror)=
## `processLoginError`

**Signature:**
```cpp
void processLoginError(const std::string& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `error` | - |

---

(processloginadvice)=
## `processLoginAdvice`

**Signature:**
```cpp
void processLoginAdvice(const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |

---

(processloginwait)=
## `processLoginWait`

**Signature:**
```cpp
void processLoginWait(const std::string& message, int time);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |
| `int` | `time` | - |

---

(processlogintoken)=
## `processLoginToken`

**Signature:**
```cpp
void processLoginToken(bool unknown);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `unknown` | - |

---

(processlogin)=
## `processLogin`

**Signature:**
```cpp
void processLogin();
```

---

(processpendinggame)=
## `processPendingGame`

**Signature:**
```cpp
void processPendingGame();
```

---

(processentergame)=
## `processEnterGame`

**Signature:**
```cpp
void processEnterGame();
```

---

(processgamestart)=
## `processGameStart`

**Signature:**
```cpp
void processGameStart();
```

---

(processgameend)=
## `processGameEnd`

**Signature:**
```cpp
void processGameEnd();
```

---

(processdeath)=
## `processDeath`

**Signature:**
```cpp
void processDeath(int deathType, int penality);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `deathType` | - |
| `int` | `penality` | - |

---

(processgmactions)=
## `processGMActions`

**Signature:**
```cpp
void processGMActions(const std::vector<uint8>& actions);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;uint8&gt;&` | `actions` | - |

---

(processinventorychange)=
## `processInventoryChange`

**Signature:**
```cpp
void processInventoryChange(int slot, const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |
| `const ItemPtr&` | `item` | - |

---

(processattackcancel)=
## `processAttackCancel`

**Signature:**
```cpp
void processAttackCancel(uint seq);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `seq` | - |

---

(processwalkcancel)=
## `processWalkCancel`

**Signature:**
```cpp
void processWalkCancel(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(processnewwalkcancel)=
## `processNewWalkCancel`

**Signature:**
```cpp
void processNewWalkCancel(Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `dir` | - |

---

(processpredictivewalkcancel)=
## `processPredictiveWalkCancel`

**Signature:**
```cpp
void processPredictiveWalkCancel(const Position& pos, Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `Otc::Direction` | `dir` | - |

---

(processwalkid)=
## `processWalkId`

**Signature:**
```cpp
void processWalkId(uint32_t walkId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `walkId` | - |

---

(processplayerhelpers)=
## `processPlayerHelpers`

**Signature:**
```cpp
void processPlayerHelpers(int helpers);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `helpers` | - |

---

(processplayermodes)=
## `processPlayerModes`

**Signature:**
```cpp
void processPlayerModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeMode, Otc::PVPModes pvpMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::FightModes` | `fightMode` | - |
| `Otc::ChaseModes` | `chaseMode` | - |
| `bool` | `safeMode` | - |
| `Otc::PVPModes` | `pvpMode` | - |

---

(processtextmessage)=
## `processTextMessage`

**Signature:**
```cpp
void processTextMessage(Otc::MessageMode mode, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::MessageMode` | `mode` | - |
| `const std::string&` | `text` | - |

---

(processtalk)=
## `processTalk`

**Signature:**
```cpp
void processTalk(const std::string& name, int level, Otc::MessageMode mode, const std::string& text, int channelId, const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `int` | `level` | - |
| `Otc::MessageMode` | `mode` | - |
| `const std::string&` | `text` | - |
| `int` | `channelId` | - |
| `const Position&` | `pos` | - |

---

(processopencontainer)=
## `processOpenContainer`

**Signature:**
```cpp
void processOpenContainer(int containerId, const ItemPtr& containerItem, const std::string& name, int capacity, bool hasParent, const std::vector<ItemPtr>& items, bool isUnlocked, bool hasPages, int containerSize, int firstIndex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |
| `const ItemPtr&` | `containerItem` | - |
| `const std::string&` | `name` | - |
| `int` | `capacity` | - |
| `bool` | `hasParent` | - |
| `const std::vector&lt;ItemPtr&gt;&` | `items` | - |
| `bool` | `isUnlocked` | - |
| `bool` | `hasPages` | - |
| `int` | `containerSize` | - |
| `int` | `firstIndex` | - |

---

(processclosecontainer)=
## `processCloseContainer`

**Signature:**
```cpp
void processCloseContainer(int containerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |

---

(processcontaineradditem)=
## `processContainerAddItem`

**Signature:**
```cpp
void processContainerAddItem(int containerId, const ItemPtr& item, int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |
| `const ItemPtr&` | `item` | - |
| `int` | `slot` | - |

---

(processcontainerupdateitem)=
## `processContainerUpdateItem`

**Signature:**
```cpp
void processContainerUpdateItem(int containerId, int slot, const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |
| `int` | `slot` | - |
| `const ItemPtr&` | `item` | - |

---

(processcontainerremoveitem)=
## `processContainerRemoveItem`

**Signature:**
```cpp
void processContainerRemoveItem(int containerId, int slot, const ItemPtr& lastItem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |
| `int` | `slot` | - |
| `const ItemPtr&` | `lastItem` | - |

---

(processchannellist)=
## `processChannelList`

**Signature:**
```cpp
void processChannelList(const std::vector<std::tuple<int, std::string> >& channelList);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;std::tuple&lt;int, std::string&gt; &gt;&` | `channelList` | - |

---

(processopenchannel)=
## `processOpenChannel`

**Signature:**
```cpp
void processOpenChannel(int channelId, const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |
| `const std::string&` | `name` | - |

---

(processopenprivatechannel)=
## `processOpenPrivateChannel`

**Signature:**
```cpp
void processOpenPrivateChannel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(processopenownprivatechannel)=
## `processOpenOwnPrivateChannel`

**Signature:**
```cpp
void processOpenOwnPrivateChannel(int channelId, const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |
| `const std::string&` | `name` | - |

---

(processclosechannel)=
## `processCloseChannel`

**Signature:**
```cpp
void processCloseChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(processruleviolationchannel)=
## `processRuleViolationChannel`

**Signature:**
```cpp
void processRuleViolationChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(processruleviolationremove)=
## `processRuleViolationRemove`

**Signature:**
```cpp
void processRuleViolationRemove(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(processruleviolationcancel)=
## `processRuleViolationCancel`

**Signature:**
```cpp
void processRuleViolationCancel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(processruleviolationlock)=
## `processRuleViolationLock`

**Signature:**
```cpp
void processRuleViolationLock();
```

---

(processvipadd)=
## `processVipAdd`

**Signature:**
```cpp
void processVipAdd(uint id, const std::string& name, uint status, const std::string& description, int iconId, bool notifyLogin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `const std::string&` | `name` | - |
| `uint` | `status` | - |
| `const std::string&` | `description` | - |
| `int` | `iconId` | - |
| `bool` | `notifyLogin` | - |

---

(processvipstatechange)=
## `processVipStateChange`

**Signature:**
```cpp
void processVipStateChange(uint id, uint status);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `uint` | `status` | - |

---

(processtutorialhint)=
## `processTutorialHint`

**Signature:**
```cpp
void processTutorialHint(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

---

(processaddautomapflag)=
## `processAddAutomapFlag`

**Signature:**
```cpp
void processAddAutomapFlag(const Position& pos, int icon, const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `icon` | - |
| `const std::string&` | `message` | - |

---

(processremoveautomapflag)=
## `processRemoveAutomapFlag`

**Signature:**
```cpp
void processRemoveAutomapFlag(const Position& pos, int icon, const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `icon` | - |
| `const std::string&` | `message` | - |

---

(processopenoutfitwindow)=
## `processOpenOutfitWindow`

**Signature:**
```cpp
void processOpenOutfitWindow(const Outfit& currentOutfit, const std::vector<std::tuple<int, std::string, int>>& outfitList, const std::vector<std::tuple<int, std::string>>& mountList, const std::vector<std::tuple<int, std::string>>& wingList, const std::vector<std::tuple<int, std::string>>& auraList, const std::vector<std::tuple<int, std::string>>& shaderList, const std::vector<std::tuple<int, std::string>>& healthBarList, const std::vector<std::tuple<int, std::string>>& manaBarList);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `currentOutfit` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string, int&gt;&gt;&` | `outfitList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `mountList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `wingList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `auraList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `shaderList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `healthBarList` | - |
| `const std::vector&lt;std::tuple&lt;int, std::string&gt;&gt;&` | `manaBarList` | - |

---

(processopennpctrade)=
## `processOpenNpcTrade`

**Signature:**
```cpp
void processOpenNpcTrade(const std::vector<std::tuple<ItemPtr, std::string, int, int64_t, int64_t> >& items);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;std::tuple&lt;ItemPtr, std::string, int, int64_t, int64_t&gt; &gt;&` | `items` | - |

---

(processplayergoods)=
## `processPlayerGoods`

**Signature:**
```cpp
void processPlayerGoods(uint64_t money, const std::vector<std::tuple<ItemPtr, int> >& goods);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64_t` | `money` | - |
| `const std::vector&lt;std::tuple&lt;ItemPtr, int&gt; &gt;&` | `goods` | - |

---

(processclosenpctrade)=
## `processCloseNpcTrade`

**Signature:**
```cpp
void processCloseNpcTrade();
```

---

(processowntrade)=
## `processOwnTrade`

**Signature:**
```cpp
void processOwnTrade(const std::string& name, const std::vector<ItemPtr>& items);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `const std::vector&lt;ItemPtr&gt;&` | `items` | - |

---

(processcountertrade)=
## `processCounterTrade`

**Signature:**
```cpp
void processCounterTrade(const std::string& name, const std::vector<ItemPtr>& items);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |
| `const std::vector&lt;ItemPtr&gt;&` | `items` | - |

---

(processclosetrade)=
## `processCloseTrade`

**Signature:**
```cpp
void processCloseTrade();
```

---

(processedittext)=
## `processEditText`

**Signature:**
```cpp
void processEditText(uint id, int itemId, int maxLength, const std::string& text, const std::string& writer, const std::string& date);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `int` | `itemId` | - |
| `int` | `maxLength` | - |
| `const std::string&` | `text` | - |
| `const std::string&` | `writer` | - |
| `const std::string&` | `date` | - |

---

(processeditlist)=
## `processEditList`

**Signature:**
```cpp
void processEditList(uint id, int doorId, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `int` | `doorId` | - |
| `const std::string&` | `text` | - |

---

(processquestlog)=
## `processQuestLog`

**Signature:**
```cpp
void processQuestLog(const std::vector<std::tuple<int, std::string, bool> >& questList);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;std::tuple&lt;int, std::string, bool&gt; &gt;&` | `questList` | - |

---

(processquestline)=
## `processQuestLine`

**Signature:**
```cpp
void processQuestLine(int questId, const std::vector<std::tuple<std::string, std::string, int> >& questMissions);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `questId` | - |
| `const std::vector&lt;std::tuple&lt;std::string, std::string, int&gt; &gt;&` | `questMissions` | - |

---

(processmodaldialog)=
## `processModalDialog`

**Signature:**
```cpp
void processModalDialog(uint32 id, std::string title, std::string message, std::vector<std::tuple<int, std::string> > buttonList, int enterButton, int escapeButton, std::vector<std::tuple<int, std::string> > choiceList, bool priority);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |
| `std::string` | `title` | - |
| `std::string` | `message` | - |
| `std::vector&lt;std::tuple&lt;int, std::string&gt; &gt;` | `buttonList` | - |
| `int` | `enterButton` | - |
| `int` | `escapeButton` | - |
| `std::vector&lt;std::tuple&lt;int, std::string&gt; &gt;` | `choiceList` | - |
| `bool` | `priority` | - |

---

(loginworld)=
## `loginWorld`

**Signature:**
```cpp
void loginWorld(const std::string& account, const std::string& password, const std::string& worldName, const std::string& worldHost, int worldPort, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& recordTo = "");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `account` |  | - |
| `const std::string&` | `password` |  | - |
| `const std::string&` | `worldName` |  | - |
| `const std::string&` | `worldHost` |  | - |
| `int` | `worldPort` |  | - |
| `const std::string&` | `characterName` |  | - |
| `const std::string&` | `authenticatorToken` |  | - |
| `const std::string&` | `sessionKey` |  | - |
| `const std::string&` | `recordTo` | `""` | - |

---

(playrecord)=
## `playRecord`

**Signature:**
```cpp
void playRecord(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(cancellogin)=
## `cancelLogin`

**Signature:**
```cpp
void cancelLogin();
```

---

(forcelogout)=
## `forceLogout`

**Signature:**
```cpp
void forceLogout();
```

---

(safelogout)=
## `safeLogout`

**Signature:**
```cpp
void safeLogout();
```

---

(walk)=
## `walk`

**Signature:**
```cpp
void walk(Otc::Direction direction, bool withPreWalk);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |
| `bool` | `withPreWalk` | - |

---

(autowalk)=
## `autoWalk`

**Signature:**
```cpp
void autoWalk(const std::vector<Otc::Direction>& dirs, Position startPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;Otc::Direction&gt;&` | `dirs` | - |
| `Position` | `startPos` | - |

---

(turn)=
## `turn`

**Signature:**
```cpp
void turn(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(stop)=
## `stop`

**Signature:**
```cpp
void stop();
```

---

(look)=
## `look`

**Signature:**
```cpp
void look(const ThingPtr& thing, bool isBattleList = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const ThingPtr&` | `thing` |  | - |
| `bool` | `isBattleList` | `false` | - |

---

(move)=
## `move`

**Signature:**
```cpp
void move(const ThingPtr& thing, const Position& toPos, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |
| `const Position&` | `toPos` | - |
| `int` | `count` | - |

---

(moveraw)=
## `moveRaw`

**Signature:**
```cpp
void moveRaw(const Position& pos, int id, int stackpos, const Position& toPos, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `id` | - |
| `int` | `stackpos` | - |
| `const Position&` | `toPos` | - |
| `int` | `count` | - |

---

(movetoparentcontainer)=
## `moveToParentContainer`

**Signature:**
```cpp
void moveToParentContainer(const ThingPtr& thing, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |
| `int` | `count` | - |

---

(rotate)=
## `rotate`

**Signature:**
```cpp
void rotate(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

---

(wrap)=
## `wrap`

**Signature:**
```cpp
void wrap(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

---

(use)=
## `use`

**Signature:**
```cpp
void use(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

---

(usewith)=
## `useWith`

**Signature:**
```cpp
void useWith(const ItemPtr& fromThing, const ThingPtr& toThing, int subType = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const ItemPtr&` | `fromThing` |  | - |
| `const ThingPtr&` | `toThing` |  | - |
| `int` | `subType` | `0` | - |

---

(useinventoryitem)=
## `useInventoryItem`

**Signature:**
```cpp
void useInventoryItem(int itemId, int subType = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `itemId` |  | - |
| `int` | `subType` | `0` | - |

---

(useinventoryitemwith)=
## `useInventoryItemWith`

**Signature:**
```cpp
void useInventoryItemWith(int itemId, const ThingPtr& toThing, int subType = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `itemId` |  | - |
| `const ThingPtr&` | `toThing` |  | - |
| `int` | `subType` | `0` | - |

---

(finditemincontainers)=
## `findItemInContainers`

**Signature:**
```cpp
ItemPtr findItemInContainers(uint itemId, int subType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `itemId` | - |
| `int` | `subType` | - |

**Returns:**
- `ItemPtr`

---

(open)=
## `open`

**Signature:**
```cpp
int open(const ItemPtr& item, const ContainerPtr& previousContainer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `const ContainerPtr&` | `previousContainer` | - |

**Returns:**
- `int`

---

(openparent)=
## `openParent`

**Signature:**
```cpp
void openParent(const ContainerPtr& container);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ContainerPtr&` | `container` | - |

---

(close)=
## `close`

**Signature:**
```cpp
void close(const ContainerPtr& container);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ContainerPtr&` | `container` | - |

---

(refreshcontainer)=
## `refreshContainer`

**Signature:**
```cpp
void refreshContainer(const ContainerPtr& container);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ContainerPtr&` | `container` | - |

---

(attack)=
## `attack`

**Signature:**
```cpp
void attack(CreaturePtr creature, bool cancel = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CreaturePtr` | `creature` |  | - |
| `bool` | `cancel` | `false` | - |

---

(follow)=
## `follow`

**Signature:**
```cpp
void follow(CreaturePtr creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CreaturePtr` | `creature` | - |

---

(cancelattackandfollow)=
## `cancelAttackAndFollow`

**Signature:**
```cpp
void cancelAttackAndFollow();
```

---

(talk)=
## `talk`

**Signature:**
```cpp
void talk(const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `message` | - |

---

(talkchannel)=
## `talkChannel`

**Signature:**
```cpp
void talkChannel(Otc::MessageMode mode, int channelId, const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::MessageMode` | `mode` | - |
| `int` | `channelId` | - |
| `const std::string&` | `message` | - |

---

(talkprivate)=
## `talkPrivate`

**Signature:**
```cpp
void talkPrivate(Otc::MessageMode mode, const std::string& receiver, const std::string& message);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::MessageMode` | `mode` | - |
| `const std::string&` | `receiver` | - |
| `const std::string&` | `message` | - |

---

(openprivatechannel)=
## `openPrivateChannel`

**Signature:**
```cpp
void openPrivateChannel(const std::string& receiver);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `receiver` | - |

---

(requestchannels)=
## `requestChannels`

**Signature:**
```cpp
void requestChannels();
```

---

(joinchannel)=
## `joinChannel`

**Signature:**
```cpp
void joinChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(leavechannel)=
## `leaveChannel`

**Signature:**
```cpp
void leaveChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(closenpcchannel)=
## `closeNpcChannel`

**Signature:**
```cpp
void closeNpcChannel();
```

---

(openownchannel)=
## `openOwnChannel`

**Signature:**
```cpp
void openOwnChannel();
```

---

(invitetoownchannel)=
## `inviteToOwnChannel`

**Signature:**
```cpp
void inviteToOwnChannel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(excludefromownchannel)=
## `excludeFromOwnChannel`

**Signature:**
```cpp
void excludeFromOwnChannel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(partyinvite)=
## `partyInvite`

**Signature:**
```cpp
void partyInvite(int creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `creatureId` | - |

---

(partyjoin)=
## `partyJoin`

**Signature:**
```cpp
void partyJoin(int creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `creatureId` | - |

---

(partyrevokeinvitation)=
## `partyRevokeInvitation`

**Signature:**
```cpp
void partyRevokeInvitation(int creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `creatureId` | - |

---

(partypassleadership)=
## `partyPassLeadership`

**Signature:**
```cpp
void partyPassLeadership(int creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `creatureId` | - |

---

(partyleave)=
## `partyLeave`

**Signature:**
```cpp
void partyLeave();
```

---

(partyshareexperience)=
## `partyShareExperience`

**Signature:**
```cpp
void partyShareExperience(bool active);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `active` | - |

---

(requestoutfit)=
## `requestOutfit`

**Signature:**
```cpp
void requestOutfit();
```

---

(changeoutfit)=
## `changeOutfit`

**Signature:**
```cpp
void changeOutfit(const Outfit& outfit);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `outfit` | - |

---

(addvip)=
## `addVip`

**Signature:**
```cpp
void addVip(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(removevip)=
## `removeVip`

**Signature:**
```cpp
void removeVip(int playerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `playerId` | - |

---

(editvip)=
## `editVip`

**Signature:**
```cpp
void editVip(int playerId, const std::string& description, int iconId, bool notifyLogin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `playerId` | - |
| `const std::string&` | `description` | - |
| `int` | `iconId` | - |
| `bool` | `notifyLogin` | - |

---

(setchasemode)=
## `setChaseMode`

**Signature:**
```cpp
void setChaseMode(Otc::ChaseModes chaseMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::ChaseModes` | `chaseMode` | - |

---

(setfightmode)=
## `setFightMode`

**Signature:**
```cpp
void setFightMode(Otc::FightModes fightMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::FightModes` | `fightMode` | - |

---

(setsafefight)=
## `setSafeFight`

**Signature:**
```cpp
void setSafeFight(bool on);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `on` | - |

---

(setpvpmode)=
## `setPVPMode`

**Signature:**
```cpp
void setPVPMode(Otc::PVPModes pvpMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::PVPModes` | `pvpMode` | - |

---

(setunjustifiedpoints)=
## `setUnjustifiedPoints`

**Signature:**
```cpp
void setUnjustifiedPoints(UnjustifiedPoints unjustifiedPoints);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UnjustifiedPoints` | `unjustifiedPoints` | - |

---

(setopenpvpsituations)=
## `setOpenPvpSituations`

**Signature:**
```cpp
void setOpenPvpSituations(int openPvpSitations);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `openPvpSitations` | - |

---

(inspectnpctrade)=
## `inspectNpcTrade`

**Signature:**
```cpp
void inspectNpcTrade(const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |

---

(buyitem)=
## `buyItem`

**Signature:**
```cpp
void buyItem(const ItemPtr& item, int amount, bool ignoreCapacity, bool buyWithBackpack);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `int` | `amount` | - |
| `bool` | `ignoreCapacity` | - |
| `bool` | `buyWithBackpack` | - |

---

(sellitem)=
## `sellItem`

**Signature:**
```cpp
void sellItem(const ItemPtr& item, int amount, bool ignoreEquipped);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `int` | `amount` | - |
| `bool` | `ignoreEquipped` | - |

---

(closenpctrade)=
## `closeNpcTrade`

**Signature:**
```cpp
void closeNpcTrade();
```

---

(requesttrade)=
## `requestTrade`

**Signature:**
```cpp
void requestTrade(const ItemPtr& item, const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `const CreaturePtr&` | `creature` | - |

---

(inspecttrade)=
## `inspectTrade`

**Signature:**
```cpp
void inspectTrade(bool counterOffer, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `counterOffer` | - |
| `int` | `index` | - |

---

(accepttrade)=
## `acceptTrade`

**Signature:**
```cpp
void acceptTrade();
```

---

(rejecttrade)=
## `rejectTrade`

**Signature:**
```cpp
void rejectTrade();
```

---

(edittext)=
## `editText`

**Signature:**
```cpp
void editText(uint id, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `const std::string&` | `text` | - |

---

(editlist)=
## `editList`

**Signature:**
```cpp
void editList(uint id, int doorId, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `int` | `doorId` | - |
| `const std::string&` | `text` | - |

---

(openruleviolation)=
## `openRuleViolation`

**Signature:**
```cpp
void openRuleViolation(const std::string& reporter);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `reporter` | - |

---

(closeruleviolation)=
## `closeRuleViolation`

**Signature:**
```cpp
void closeRuleViolation(const std::string& reporter);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `reporter` | - |

---

(cancelruleviolation)=
## `cancelRuleViolation`

**Signature:**
```cpp
void cancelRuleViolation();
```

---

(reportbug)=
## `reportBug`

**Signature:**
```cpp
void reportBug(const std::string& comment);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `comment` | - |

---

(reportruleviolation)=
## `reportRuleViolation`

**Signature:**
```cpp
void reportRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `target` | - |
| `int` | `reason` | - |
| `int` | `action` | - |
| `const std::string&` | `comment` | - |
| `const std::string&` | `statement` | - |
| `int` | `statementId` | - |
| `bool` | `ipBanishment` | - |

---

(debugreport)=
## `debugReport`

**Signature:**
```cpp
void debugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `a` | - |
| `const std::string&` | `b` | - |
| `const std::string&` | `c` | - |
| `const std::string&` | `d` | - |

---

(requestquestlog)=
## `requestQuestLog`

**Signature:**
```cpp
void requestQuestLog();
```

---

(requestquestline)=
## `requestQuestLine`

**Signature:**
```cpp
void requestQuestLine(int questId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `questId` | - |

---

(equipitem)=
## `equipItem`

**Signature:**
```cpp
void equipItem(const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |

---

(equipitemid)=
## `equipItemId`

**Signature:**
```cpp
void equipItemId(int itemId, int subType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `subType` | - |

---

(mount)=
## `mount`

**Signature:**
```cpp
void mount(bool mount);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `mount` | - |

---

(setoutfitextensions)=
## `setOutfitExtensions`

**Signature:**
```cpp
void setOutfitExtensions(int mount, int wings, int aura, int shader, int healthBar, int manaBar);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `mount` | - |
| `int` | `wings` | - |
| `int` | `aura` | - |
| `int` | `shader` | - |
| `int` | `healthBar` | - |
| `int` | `manaBar` | - |

---

(requestiteminfo)=
## `requestItemInfo`

**Signature:**
```cpp
void requestItemInfo(const ItemPtr& item, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `int` | `index` | - |

---

(answermodaldialog)=
## `answerModalDialog`

**Signature:**
```cpp
void answerModalDialog(uint32 dialog, int button, int choice);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `dialog` | - |
| `int` | `button` | - |
| `int` | `choice` | - |

---

(browsefield)=
## `browseField`

**Signature:**
```cpp
void browseField(const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |

---

(seekincontainer)=
## `seekInContainer`

**Signature:**
```cpp
void seekInContainer(int cid, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `cid` | - |
| `int` | `index` | - |

---

(buystoreoffer)=
## `buyStoreOffer`

**Signature:**
```cpp
void buyStoreOffer(int offerId, int productType, const std::string& name = "");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `offerId` |  | - |
| `int` | `productType` |  | - |
| `const std::string&` | `name` | `""` | - |

---

(requesttransactionhistory)=
## `requestTransactionHistory`

**Signature:**
```cpp
void requestTransactionHistory(int page, int entriesPerPage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `page` | - |
| `int` | `entriesPerPage` | - |

---

(requeststoreoffers)=
## `requestStoreOffers`

**Signature:**
```cpp
void requestStoreOffers(const std::string& categoryName, int serviceType = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `categoryName` |  | - |
| `int` | `serviceType` | `0` | - |

---

(openstore)=
## `openStore`

**Signature:**
```cpp
void openStore(int serviceType = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `serviceType` | `0` | - |

---

(transfercoins)=
## `transferCoins`

**Signature:**
```cpp
void transferCoins(const std::string& recipient, int amount);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `recipient` | - |
| `int` | `amount` | - |

---

(opentransactionhistory)=
## `openTransactionHistory`

**Signature:**
```cpp
void openTransactionHistory(int entriesPerPage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `entriesPerPage` | - |

---

(preyaction)=
## `preyAction`

**Signature:**
```cpp
void preyAction(int slot, int actionType, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |
| `int` | `actionType` | - |
| `int` | `index` | - |

---

(preyrequest)=
## `preyRequest`

**Signature:**
```cpp
void preyRequest();
```

---

(applyimbuement)=
## `applyImbuement`

**Signature:**
```cpp
void applyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `slot` | - |
| `uint32_t` | `imbuementId` | - |
| `bool` | `protectionCharm` | - |

---

(clearimbuement)=
## `clearImbuement`

**Signature:**
```cpp
void clearImbuement(uint8_t slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `slot` | - |

---

(closeimbuingwindow)=
## `closeImbuingWindow`

**Signature:**
```cpp
void closeImbuingWindow();
```

---

(ping)=
## `ping`

**Signature:**
```cpp
void ping();
```

---

(newping)=
## `newPing`

**Signature:**
```cpp
void newPing();
```

---

(changemapawarerange)=
## `changeMapAwareRange`

**Signature:**
```cpp
void changeMapAwareRange(int xrange, int yrange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `xrange` | - |
| `int` | `yrange` | - |

---

(setprotocolversion)=
## `setProtocolVersion`

**Signature:**
```cpp
void setProtocolVersion(int version);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `version` | - |

---

(setclientversion)=
## `setClientVersion`

**Signature:**
```cpp
void setClientVersion(int version);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `version` | - |

---

(getos)=
## `getOs`

**Signature:**
```cpp
int getOs();
```

**Returns:**
- `int`

---

(canperformgameaction)=
## `canPerformGameAction`

**Signature:**
```cpp
bool canPerformGameAction();
```

**Returns:**
- `bool`

---

(checkbotprotection)=
## `checkBotProtection`

**Signature:**
```cpp
bool checkBotProtection();
```

**Returns:**
- `bool`

---

(formatcreaturename)=
## `formatCreatureName`

**Signature:**
```cpp
std::string formatCreatureName(const std::string &name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string &name` | - | - |

**Returns:**
- `std::string`

---

(findemptycontainerid)=
## `findEmptyContainerId`

**Signature:**
```cpp
int findEmptyContainerId();
```

**Returns:**
- `int`

---

(setattackingcreature)=
## `setAttackingCreature`

**Signature:**
```cpp
private: void setAttackingCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(setfollowingcreature)=
## `setFollowingCreature`

**Signature:**
```cpp
void setFollowingCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(cancelattack)=
## `cancelAttack`

**Signature:**
```cpp
void cancelAttack();
```

---

(cancelfollow)=
## `cancelFollow`

**Signature:**
```cpp
void cancelFollow();
```

---

(getchasemode)=
## `getChaseMode`

**Signature:**
```cpp
Otc::ChaseModes getChaseMode();
```

**Returns:**
- `Otc::ChaseModes`

---

(getfightmode)=
## `getFightMode`

**Signature:**
```cpp
Otc::FightModes getFightMode();
```

**Returns:**
- `Otc::FightModes`

---

(issafefight)=
## `isSafeFight`

**Signature:**
```cpp
bool isSafeFight();
```

**Returns:**
- `bool`

---

(getpvpmode)=
## `getPVPMode`

**Signature:**
```cpp
Otc::PVPModes getPVPMode();
```

**Returns:**
- `Otc::PVPModes`

---

(getunjustifiedpoints)=
## `getUnjustifiedPoints`

**Signature:**
```cpp
UnjustifiedPoints getUnjustifiedPoints();
```

**Returns:**
- `UnjustifiedPoints`

---

(getopenpvpsituations)=
## `getOpenPvpSituations`

**Signature:**
```cpp
int getOpenPvpSituations();
```

**Returns:**
- `int`

---

(setpingdelay)=
## `setPingDelay`

**Signature:**
```cpp
void setPingDelay(int delay);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `delay` | - |

---

(resetfeatures)=
## `resetFeatures`

**Signature:**
```cpp
void resetFeatures();
```

---

(enablefeature)=
## `enableFeature`

**Signature:**
```cpp
void enableFeature(Otc::GameFeature feature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::GameFeature` | `feature` | - |

---

(disablefeature)=
## `disableFeature`

**Signature:**
```cpp
void disableFeature(Otc::GameFeature feature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::GameFeature` | `feature` | - |

---

(setfeature)=
## `setFeature`

**Signature:**
```cpp
void setFeature(Otc::GameFeature feature, bool enabled);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::GameFeature` | `feature` | - |
| `bool` | `enabled` | - |

---

(getfeature)=
## `getFeature`

**Signature:**
```cpp
bool getFeature(Otc::GameFeature feature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::GameFeature` | `feature` | - |

**Returns:**
- `bool`

---

(getprotocolversion)=
## `getProtocolVersion`

**Signature:**
```cpp
int getProtocolVersion();
```

**Returns:**
- `int`

---

(setcustomprotocolversion)=
## `setCustomProtocolVersion`

**Signature:**
```cpp
void setCustomProtocolVersion(int version);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `version` | - |

---

(getcustomprotocolversion)=
## `getCustomProtocolVersion`

**Signature:**
```cpp
int getCustomProtocolVersion();
```

**Returns:**
- `int`

---

(getclientversion)=
## `getClientVersion`

**Signature:**
```cpp
int getClientVersion();
```

**Returns:**
- `int`

---

(setcustomos)=
## `setCustomOs`

**Signature:**
```cpp
void setCustomOs(int os);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `os` | - |

---

(isonline)=
## `isOnline`

**Signature:**
```cpp
bool isOnline();
```

**Returns:**
- `bool`

---

(islogging)=
## `isLogging`

**Signature:**
```cpp
bool isLogging();
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

(isattacking)=
## `isAttacking`

**Signature:**
```cpp
bool isAttacking();
```

**Returns:**
- `bool`

---

(isfollowing)=
## `isFollowing`

**Signature:**
```cpp
bool isFollowing();
```

**Returns:**
- `bool`

---

(isconnectionok)=
## `isConnectionOk`

**Signature:**
```cpp
bool isConnectionOk();
```

**Returns:**
- `bool`

---

(getping)=
## `getPing`

**Signature:**
```cpp
int getPing();
```

**Returns:**
- `int`

---

(getcontainer)=
## `getContainer`

**Signature:**
```cpp
ContainerPtr getContainer(int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |

**Returns:**
- `ContainerPtr`

---

(getattackingcreature)=
## `getAttackingCreature`

**Signature:**
```cpp
CreaturePtr getAttackingCreature();
```

**Returns:**
- `CreaturePtr`

---

(getfollowingcreature)=
## `getFollowingCreature`

**Signature:**
```cpp
CreaturePtr getFollowingCreature();
```

**Returns:**
- `CreaturePtr`

---

(setserverbeat)=
## `setServerBeat`

**Signature:**
```cpp
void setServerBeat(int beat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `beat` | - |

---

(getserverbeat)=
## `getServerBeat`

**Signature:**
```cpp
int getServerBeat();
```

**Returns:**
- `int`

---

(setcanreportbugs)=
## `setCanReportBugs`

**Signature:**
```cpp
void setCanReportBugs(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(canreportbugs)=
## `canReportBugs`

**Signature:**
```cpp
bool canReportBugs();
```

**Returns:**
- `bool`

---

(setexpertpvpmode)=
## `setExpertPvpMode`

**Signature:**
```cpp
void setExpertPvpMode(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(getexpertpvpmode)=
## `getExpertPvpMode`

**Signature:**
```cpp
bool getExpertPvpMode();
```

**Returns:**
- `bool`

---

(getlocalplayer)=
## `getLocalPlayer`

**Signature:**
```cpp
LocalPlayerPtr getLocalPlayer();
```

**Returns:**
- `LocalPlayerPtr`

---

(getprotocolgame)=
## `getProtocolGame`

**Signature:**
```cpp
ProtocolGamePtr getProtocolGame();
```

**Returns:**
- `ProtocolGamePtr`

---

(getcharactername)=
## `getCharacterName`

**Signature:**
```cpp
std::string getCharacterName();
```

**Returns:**
- `std::string`

---

(getworldname)=
## `getWorldName`

**Signature:**
```cpp
std::string getWorldName();
```

**Returns:**
- `std::string`

---

(getgmactions)=
## `getGMActions`

**Signature:**
```cpp
std::vector<uint8> getGMActions();
```

**Returns:**
- `std::vector&lt;uint8&gt;`

---

(isgm)=
## `isGM`

**Signature:**
```cpp
bool isGM();
```

**Returns:**
- `bool`

---

(getlastwalkdir)=
## `getLastWalkDir`

**Signature:**
```cpp
Otc::Direction getLastWalkDir();
```

**Returns:**
- `Otc::Direction`

---

(settibiacoins)=
## `setTibiaCoins`

**Signature:**
```cpp
void setTibiaCoins(int coins, int transferableCoins);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `coins` | - |
| `int` | `transferableCoins` | - |

---

(gettibiacoins)=
## `getTibiaCoins`

**Signature:**
```cpp
int getTibiaCoins();
```

**Returns:**
- `int`

---

(gettransferabletibiacoins)=
## `getTransferableTibiaCoins`

**Signature:**
```cpp
int getTransferableTibiaCoins();
```

**Returns:**
- `int`

---

(setmaxprewalkingsteps)=
## `setMaxPreWalkingSteps`

**Signature:**
```cpp
void setMaxPreWalkingSteps(uint value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `value` | - |

---

(getmaxprewalkingsteps)=
## `getMaxPreWalkingSteps`

**Signature:**
```cpp
uint getMaxPreWalkingSteps();
```

**Returns:**
- `uint`

---

(showrealdirection)=
## `showRealDirection`

**Signature:**
```cpp
void showRealDirection(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(shouldshowingrealdirection)=
## `shouldShowingRealDirection`

**Signature:**
```cpp
bool shouldShowingRealDirection();
```

**Returns:**
- `bool`

---

(getwalkid)=
## `getWalkId`

**Signature:**
```cpp
uint getWalkId();
```

**Returns:**
- `uint`

---

(getwalkpreditionid)=
## `getWalkPreditionId`

**Signature:**
```cpp
uint getWalkPreditionId();
```

**Returns:**
- `uint`

---

(ignoreserverdirection)=
## `ignoreServerDirection`

**Signature:**
```cpp
void ignoreServerDirection(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(isignoringserverdirection)=
## `isIgnoringServerDirection`

**Signature:**
```cpp
bool isIgnoringServerDirection();
```

**Returns:**
- `bool`

---

(enabletilethingluacallback)=
## `enableTileThingLuaCallback`

**Signature:**
```cpp
void enableTileThingLuaCallback(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(istilethingluacallbackenabled)=
## `isTileThingLuaCallbackEnabled`

**Signature:**
```cpp
bool isTileThingLuaCallbackEnabled();
```

**Returns:**
- `bool`

---

(getrecivedpacketscount)=
## `getRecivedPacketsCount`

**Signature:**
```cpp
int getRecivedPacketsCount();
```

**Returns:**
- `int`

---

(getrecivedpacketssize)=
## `getRecivedPacketsSize`

**Signature:**
```cpp
int getRecivedPacketsSize();
```

**Returns:**
- `int`

---

(enablebotcall)=
## `enableBotCall`

**Signature:**
```cpp
protected: void enableBotCall();
```

---

(disablebotcall)=
## `disableBotCall`

**Signature:**
```cpp
void disableBotCall();
```

