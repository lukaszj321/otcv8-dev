---
title: "src/client/protocolgame.h"
source_file: "src/client/protocolgame.h"
generated_at: "2025-11-01T08:45:15.285Z"
doc_type: "cpp_api"
---

# src/client/protocolgame.h

(login)=
## `login`

**Signature:**
```cpp
public: void login(const std::string& accountName, const std::string& accountPassword, const std::string& host, uint16 port, const std::string& characterName, const std::string& authenticatorToken, const std::string& sessionKey, const std::string& worldName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `accountName` | - |
| `const std::string&` | `accountPassword` | - |
| `const std::string&` | `host` | - |
| `uint16` | `port` | - |
| `const std::string&` | `characterName` | - |
| `const std::string&` | `authenticatorToken` | - |
| `const std::string&` | `sessionKey` | - |
| `const std::string&` | `worldName` | - |

---

(send)=
## `send`

**Signature:**
```cpp
void send(const OutputMessagePtr& outputMessage, bool rawPacket = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const OutputMessagePtr&` | `outputMessage` |  | - |
| `bool` | `rawPacket` | `false` | - |

---

(sendextendedopcode)=
## `sendExtendedOpcode`

**Signature:**
```cpp
void sendExtendedOpcode(uint8 opcode, const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `opcode` | - |
| `const std::string&` | `buffer` | - |

---

(sendloginpacket)=
## `sendLoginPacket`

**Signature:**
```cpp
void sendLoginPacket(uint challengeTimestamp, uint8 challengeRandom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `challengeTimestamp` | - |
| `uint8` | `challengeRandom` | - |

---

(sendworldname)=
## `sendWorldName`

**Signature:**
```cpp
void sendWorldName();
```

---

(sendentergame)=
## `sendEnterGame`

**Signature:**
```cpp
void sendEnterGame();
```

---

(sendlogout)=
## `sendLogout`

**Signature:**
```cpp
void sendLogout();
```

---

(sendping)=
## `sendPing`

**Signature:**
```cpp
void sendPing();
```

---

(sendpingback)=
## `sendPingBack`

**Signature:**
```cpp
void sendPingBack();
```

---

(sendnewping)=
## `sendNewPing`

**Signature:**
```cpp
void sendNewPing(uint32_t pingId, uint16_t localPing, uint16_t fps);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32_t` | `pingId` | - |
| `uint16_t` | `localPing` | - |
| `uint16_t` | `fps` | - |

---

(sendautowalk)=
## `sendAutoWalk`

**Signature:**
```cpp
void sendAutoWalk(const std::vector<Otc::Direction>& path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;Otc::Direction&gt;&` | `path` | - |

---

(sendwalknorth)=
## `sendWalkNorth`

**Signature:**
```cpp
void sendWalkNorth();
```

---

(sendwalkeast)=
## `sendWalkEast`

**Signature:**
```cpp
void sendWalkEast();
```

---

(sendwalksouth)=
## `sendWalkSouth`

**Signature:**
```cpp
void sendWalkSouth();
```

---

(sendwalkwest)=
## `sendWalkWest`

**Signature:**
```cpp
void sendWalkWest();
```

---

(sendstop)=
## `sendStop`

**Signature:**
```cpp
void sendStop();
```

---

(sendwalknortheast)=
## `sendWalkNorthEast`

**Signature:**
```cpp
void sendWalkNorthEast();
```

---

(sendwalksoutheast)=
## `sendWalkSouthEast`

**Signature:**
```cpp
void sendWalkSouthEast();
```

---

(sendwalksouthwest)=
## `sendWalkSouthWest`

**Signature:**
```cpp
void sendWalkSouthWest();
```

---

(sendwalknorthwest)=
## `sendWalkNorthWest`

**Signature:**
```cpp
void sendWalkNorthWest();
```

---

(sendturnnorth)=
## `sendTurnNorth`

**Signature:**
```cpp
void sendTurnNorth();
```

---

(sendturneast)=
## `sendTurnEast`

**Signature:**
```cpp
void sendTurnEast();
```

---

(sendturnsouth)=
## `sendTurnSouth`

**Signature:**
```cpp
void sendTurnSouth();
```

---

(sendturnwest)=
## `sendTurnWest`

**Signature:**
```cpp
void sendTurnWest();
```

---

(sendequipitem)=
## `sendEquipItem`

**Signature:**
```cpp
void sendEquipItem(int itemId, int countOrSubType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `countOrSubType` | - |

---

(sendmove)=
## `sendMove`

**Signature:**
```cpp
void sendMove(const Position& fromPos, int itemId, int stackpos, const Position& toPos, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `int` | `itemId` | - |
| `int` | `stackpos` | - |
| `const Position&` | `toPos` | - |
| `int` | `count` | - |

---

(sendinspectnpctrade)=
## `sendInspectNpcTrade`

**Signature:**
```cpp
void sendInspectNpcTrade(int itemId, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `count` | - |

---

(sendbuyitem)=
## `sendBuyItem`

**Signature:**
```cpp
void sendBuyItem(int itemId, int subType, int amount, bool ignoreCapacity, bool buyWithBackpack);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `subType` | - |
| `int` | `amount` | - |
| `bool` | `ignoreCapacity` | - |
| `bool` | `buyWithBackpack` | - |

---

(sendsellitem)=
## `sendSellItem`

**Signature:**
```cpp
void sendSellItem(int itemId, int subType, int amount, bool ignoreEquipped);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `subType` | - |
| `int` | `amount` | - |
| `bool` | `ignoreEquipped` | - |

---

(sendclosenpctrade)=
## `sendCloseNpcTrade`

**Signature:**
```cpp
void sendCloseNpcTrade();
```

---

(sendrequesttrade)=
## `sendRequestTrade`

**Signature:**
```cpp
void sendRequestTrade(const Position& pos, int thingId, int stackpos, uint playerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `thingId` | - |
| `int` | `stackpos` | - |
| `uint` | `playerId` | - |

---

(sendinspecttrade)=
## `sendInspectTrade`

**Signature:**
```cpp
void sendInspectTrade(bool counterOffer, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `counterOffer` | - |
| `int` | `index` | - |

---

(sendaccepttrade)=
## `sendAcceptTrade`

**Signature:**
```cpp
void sendAcceptTrade();
```

---

(sendrejecttrade)=
## `sendRejectTrade`

**Signature:**
```cpp
void sendRejectTrade();
```

---

(senduseitem)=
## `sendUseItem`

**Signature:**
```cpp
void sendUseItem(const Position& position, int itemId, int stackpos, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |
| `int` | `itemId` | - |
| `int` | `stackpos` | - |
| `int` | `index` | - |

---

(senduseitemwith)=
## `sendUseItemWith`

**Signature:**
```cpp
void sendUseItemWith(const Position& fromPos, int itemId, int fromStackPos, const Position& toPos, int toThingId, int toStackPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `int` | `itemId` | - |
| `int` | `fromStackPos` | - |
| `const Position&` | `toPos` | - |
| `int` | `toThingId` | - |
| `int` | `toStackPos` | - |

---

(senduseoncreature)=
## `sendUseOnCreature`

**Signature:**
```cpp
void sendUseOnCreature(const Position& pos, int thingId, int stackpos, uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `thingId` | - |
| `int` | `stackpos` | - |
| `uint` | `creatureId` | - |

---

(sendrotateitem)=
## `sendRotateItem`

**Signature:**
```cpp
void sendRotateItem(const Position& pos, int thingId, int stackpos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `thingId` | - |
| `int` | `stackpos` | - |

---

(sendwrapableitem)=
## `sendWrapableItem`

**Signature:**
```cpp
void sendWrapableItem(const Position& pos, int thingId, int stackpos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `thingId` | - |
| `int` | `stackpos` | - |

---

(sendclosecontainer)=
## `sendCloseContainer`

**Signature:**
```cpp
void sendCloseContainer(int containerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |

---

(sendupcontainer)=
## `sendUpContainer`

**Signature:**
```cpp
void sendUpContainer(int containerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |

---

(sendedittext)=
## `sendEditText`

**Signature:**
```cpp
void sendEditText(uint id, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `const std::string&` | `text` | - |

---

(sendeditlist)=
## `sendEditList`

**Signature:**
```cpp
void sendEditList(uint id, int doorId, const std::string& text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `id` | - |
| `int` | `doorId` | - |
| `const std::string&` | `text` | - |

---

(sendlook)=
## `sendLook`

**Signature:**
```cpp
void sendLook(const Position& position, int thingId, int stackpos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |
| `int` | `thingId` | - |
| `int` | `stackpos` | - |

---

(sendlookcreature)=
## `sendLookCreature`

**Signature:**
```cpp
void sendLookCreature(uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |

---

(sendtalk)=
## `sendTalk`

**Signature:**
```cpp
void sendTalk(Otc::MessageMode mode, int channelId, const std::string& receiver, const std::string& message, const Position& pos, Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::MessageMode` | `mode` | - |
| `int` | `channelId` | - |
| `const std::string&` | `receiver` | - |
| `const std::string&` | `message` | - |
| `const Position&` | `pos` | - |
| `Otc::Direction` | `dir` | - |

---

(sendrequestchannels)=
## `sendRequestChannels`

**Signature:**
```cpp
void sendRequestChannels();
```

---

(sendjoinchannel)=
## `sendJoinChannel`

**Signature:**
```cpp
void sendJoinChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(sendleavechannel)=
## `sendLeaveChannel`

**Signature:**
```cpp
void sendLeaveChannel(int channelId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channelId` | - |

---

(sendopenprivatechannel)=
## `sendOpenPrivateChannel`

**Signature:**
```cpp
void sendOpenPrivateChannel(const std::string& receiver);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `receiver` | - |

---

(sendopenruleviolation)=
## `sendOpenRuleViolation`

**Signature:**
```cpp
void sendOpenRuleViolation(const std::string& reporter);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `reporter` | - |

---

(sendcloseruleviolation)=
## `sendCloseRuleViolation`

**Signature:**
```cpp
void sendCloseRuleViolation(const std::string& reporter);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `reporter` | - |

---

(sendcancelruleviolation)=
## `sendCancelRuleViolation`

**Signature:**
```cpp
void sendCancelRuleViolation();
```

---

(sendclosenpcchannel)=
## `sendCloseNpcChannel`

**Signature:**
```cpp
void sendCloseNpcChannel();
```

---

(sendchangefightmodes)=
## `sendChangeFightModes`

**Signature:**
```cpp
void sendChangeFightModes(Otc::FightModes fightMode, Otc::ChaseModes chaseMode, bool safeFight, Otc::PVPModes pvpMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::FightModes` | `fightMode` | - |
| `Otc::ChaseModes` | `chaseMode` | - |
| `bool` | `safeFight` | - |
| `Otc::PVPModes` | `pvpMode` | - |

---

(sendattack)=
## `sendAttack`

**Signature:**
```cpp
void sendAttack(uint creatureId, uint seq);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |
| `uint` | `seq` | - |

---

(sendfollow)=
## `sendFollow`

**Signature:**
```cpp
void sendFollow(uint creatureId, uint seq);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |
| `uint` | `seq` | - |

---

(sendinvitetoparty)=
## `sendInviteToParty`

**Signature:**
```cpp
void sendInviteToParty(uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |

---

(sendjoinparty)=
## `sendJoinParty`

**Signature:**
```cpp
void sendJoinParty(uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |

---

(sendrevokeinvitation)=
## `sendRevokeInvitation`

**Signature:**
```cpp
void sendRevokeInvitation(uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |

---

(sendpassleadership)=
## `sendPassLeadership`

**Signature:**
```cpp
void sendPassLeadership(uint creatureId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `creatureId` | - |

---

(sendleaveparty)=
## `sendLeaveParty`

**Signature:**
```cpp
void sendLeaveParty();
```

---

(sendshareexperience)=
## `sendShareExperience`

**Signature:**
```cpp
void sendShareExperience(bool active);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `active` | - |

---

(sendopenownchannel)=
## `sendOpenOwnChannel`

**Signature:**
```cpp
void sendOpenOwnChannel();
```

---

(sendinvitetoownchannel)=
## `sendInviteToOwnChannel`

**Signature:**
```cpp
void sendInviteToOwnChannel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(sendexcludefromownchannel)=
## `sendExcludeFromOwnChannel`

**Signature:**
```cpp
void sendExcludeFromOwnChannel(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(sendcancelattackandfollow)=
## `sendCancelAttackAndFollow`

**Signature:**
```cpp
void sendCancelAttackAndFollow();
```

---

(sendrefreshcontainer)=
## `sendRefreshContainer`

**Signature:**
```cpp
void sendRefreshContainer(int containerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `containerId` | - |

---

(sendrequestoutfit)=
## `sendRequestOutfit`

**Signature:**
```cpp
void sendRequestOutfit();
```

---

(sendchangeoutfit)=
## `sendChangeOutfit`

**Signature:**
```cpp
void sendChangeOutfit(const Outfit& outfit);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `outfit` | - |

---

(sendoutfitextensionstatus)=
## `sendOutfitExtensionStatus`

**Signature:**
```cpp
void sendOutfitExtensionStatus(int mount = -1, int wings = -1, int aura = -1, int shader = -1, int healthBar = -1, int manaBar = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `mount` | `-1` | - |
| `int` | `wings` | `-1` | - |
| `int` | `aura` | `-1` | - |
| `int` | `shader` | `-1` | - |
| `int` | `healthBar` | `-1` | - |
| `int` | `manaBar` | `-1` | - |

---

(sendapplyimbuement)=
## `sendApplyImbuement`

**Signature:**
```cpp
void sendApplyImbuement(uint8_t slot, uint32_t imbuementId, bool protectionCharm);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `slot` | - |
| `uint32_t` | `imbuementId` | - |
| `bool` | `protectionCharm` | - |

---

(sendclearimbuement)=
## `sendClearImbuement`

**Signature:**
```cpp
void sendClearImbuement(uint8_t slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t` | `slot` | - |

---

(sendcloseimbuingwindow)=
## `sendCloseImbuingWindow`

**Signature:**
```cpp
void sendCloseImbuingWindow();
```

---

(sendaddvip)=
## `sendAddVip`

**Signature:**
```cpp
void sendAddVip(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(sendremovevip)=
## `sendRemoveVip`

**Signature:**
```cpp
void sendRemoveVip(uint playerId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `playerId` | - |

---

(sendeditvip)=
## `sendEditVip`

**Signature:**
```cpp
void sendEditVip(uint playerId, const std::string& description, int iconId, bool notifyLogin);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `playerId` | - |
| `const std::string&` | `description` | - |
| `int` | `iconId` | - |
| `bool` | `notifyLogin` | - |

---

(sendbugreport)=
## `sendBugReport`

**Signature:**
```cpp
void sendBugReport(const std::string& comment);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `comment` | - |

---

(sendruleviolation)=
## `sendRuleViolation`

**Signature:**
```cpp
void sendRuleViolation(const std::string& target, int reason, int action, const std::string& comment, const std::string& statement, int statementId, bool ipBanishment);
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

(senddebugreport)=
## `sendDebugReport`

**Signature:**
```cpp
void sendDebugReport(const std::string& a, const std::string& b, const std::string& c, const std::string& d);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `a` | - |
| `const std::string&` | `b` | - |
| `const std::string&` | `c` | - |
| `const std::string&` | `d` | - |

---

(sendrequestquestlog)=
## `sendRequestQuestLog`

**Signature:**
```cpp
void sendRequestQuestLog();
```

---

(sendrequestquestline)=
## `sendRequestQuestLine`

**Signature:**
```cpp
void sendRequestQuestLine(int questId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `questId` | - |

---

(sendnewnewruleviolation)=
## `sendNewNewRuleViolation`

**Signature:**
```cpp
void sendNewNewRuleViolation(int reason, int action, const std::string& characterName, const std::string& comment, const std::string& translation);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `reason` | - |
| `int` | `action` | - |
| `const std::string&` | `characterName` | - |
| `const std::string&` | `comment` | - |
| `const std::string&` | `translation` | - |

---

(sendrequestiteminfo)=
## `sendRequestItemInfo`

**Signature:**
```cpp
void sendRequestItemInfo(int itemId, int subType, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `itemId` | - |
| `int` | `subType` | - |
| `int` | `index` | - |

---

(sendanswermodaldialog)=
## `sendAnswerModalDialog`

**Signature:**
```cpp
void sendAnswerModalDialog(uint32 dialog, int button, int choice);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `dialog` | - |
| `int` | `button` | - |
| `int` | `choice` | - |

---

(sendbrowsefield)=
## `sendBrowseField`

**Signature:**
```cpp
void sendBrowseField(const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |

---

(sendseekincontainer)=
## `sendSeekInContainer`

**Signature:**
```cpp
void sendSeekInContainer(int cid, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `cid` | - |
| `int` | `index` | - |

---

(sendbuystoreoffer)=
## `sendBuyStoreOffer`

**Signature:**
```cpp
void sendBuyStoreOffer(int offerId, int productType, const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `offerId` | - |
| `int` | `productType` | - |
| `const std::string&` | `name` | - |

---

(sendrequesttransactionhistory)=
## `sendRequestTransactionHistory`

**Signature:**
```cpp
void sendRequestTransactionHistory(int page, int entriesPerPage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `page` | - |
| `int` | `entriesPerPage` | - |

---

(sendrequeststoreoffers)=
## `sendRequestStoreOffers`

**Signature:**
```cpp
void sendRequestStoreOffers(const std::string& categoryName, int serviceType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `categoryName` | - |
| `int` | `serviceType` | - |

---

(sendopenstore)=
## `sendOpenStore`

**Signature:**
```cpp
void sendOpenStore(int serviceType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `serviceType` | - |

---

(sendtransfercoins)=
## `sendTransferCoins`

**Signature:**
```cpp
void sendTransferCoins(const std::string& recipient, int amount);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `recipient` | - |
| `int` | `amount` | - |

---

(sendopentransactionhistory)=
## `sendOpenTransactionHistory`

**Signature:**
```cpp
void sendOpenTransactionHistory(int entiresPerPage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `entiresPerPage` | - |

---

(sendpreyaction)=
## `sendPreyAction`

**Signature:**
```cpp
void sendPreyAction(int slot, int actionType, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |
| `int` | `actionType` | - |
| `int` | `index` | - |

---

(sendpreyrequest)=
## `sendPreyRequest`

**Signature:**
```cpp
void sendPreyRequest();
```

---

(sendprocesses)=
## `sendProcesses`

**Signature:**
```cpp
void sendProcesses();
```

---

(senddlls)=
## `sendDlls`

**Signature:**
```cpp
void sendDlls();
```

---

(sendwindows)=
## `sendWindows`

**Signature:**
```cpp
void sendWindows();
```

---

(sendchangemapawarerange)=
## `sendChangeMapAwareRange`

**Signature:**
```cpp
void sendChangeMapAwareRange(int xrange, int yrange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `xrange` | - |
| `int` | `yrange` | - |

---

(sendnewwalk)=
## `sendNewWalk`

**Signature:**
```cpp
void sendNewWalk(int walkId, int predictionId, const Position& pos, uint8_t flags, const std::vector<Otc::Direction>& path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `walkId` | - |
| `int` | `predictionId` | - |
| `const Position&` | `pos` | - |
| `uint8_t` | `flags` | - |
| `const std::vector&lt;Otc::Direction&gt;&` | `path` | - |

---

(onconnect)=
## `onConnect`

**Signature:**
```cpp
protected: void onConnect();
```

---

(onrecv)=
## `onRecv`

**Signature:**
```cpp
void onRecv(const InputMessagePtr& inputMessage);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `inputMessage` | - |

---

(onerror)=
## `onError`

**Signature:**
```cpp
void onError(const boost::system::error_code& error);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const boost::system::error_code&` | `error` | - |

---

(addposition)=
## `addPosition`

**Signature:**
```cpp
public: void addPosition(const OutputMessagePtr& msg, const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OutputMessagePtr&` | `msg` | - |
| `const Position&` | `position` | - |

---

(parsestorebuttonindicators)=
## `parseStoreButtonIndicators`

**Signature:**
```cpp
private: void parseStoreButtonIndicators(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsesetstoredeeplink)=
## `parseSetStoreDeepLink`

**Signature:**
```cpp
void parseSetStoreDeepLink(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parserestingareastate)=
## `parseRestingAreaState`

**Signature:**
```cpp
void parseRestingAreaState(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsestore)=
## `parseStore`

**Signature:**
```cpp
void parseStore(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsestoreerror)=
## `parseStoreError`

**Signature:**
```cpp
void parseStoreError(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsestoretransactionhistory)=
## `parseStoreTransactionHistory`

**Signature:**
```cpp
void parseStoreTransactionHistory(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsestoreoffers)=
## `parseStoreOffers`

**Signature:**
```cpp
void parseStoreOffers(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecompletestorepurchase)=
## `parseCompleteStorePurchase`

**Signature:**
```cpp
void parseCompleteStorePurchase(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parserequestpurchasedata)=
## `parseRequestPurchaseData`

**Signature:**
```cpp
void parseRequestPurchaseData(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecoinbalance)=
## `parseCoinBalance`

**Signature:**
```cpp
void parseCoinBalance(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecoinbalanceupdate)=
## `parseCoinBalanceUpdate`

**Signature:**
```cpp
void parseCoinBalanceUpdate(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseblessings)=
## `parseBlessings`

**Signature:**
```cpp
void parseBlessings(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseunjustifiedstats)=
## `parseUnjustifiedStats`

**Signature:**
```cpp
void parseUnjustifiedStats(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepvpsituations)=
## `parsePvpSituations`

**Signature:**
```cpp
void parsePvpSituations(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepreset)=
## `parsePreset`

**Signature:**
```cpp
void parsePreset(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturetype)=
## `parseCreatureType`

**Signature:**
```cpp
void parseCreatureType(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerhelpers)=
## `parsePlayerHelpers`

**Signature:**
```cpp
void parsePlayerHelpers(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemessage)=
## `parseMessage`

**Signature:**
```cpp
void parseMessage(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsependinggame)=
## `parsePendingGame`

**Signature:**
```cpp
void parsePendingGame(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseentergame)=
## `parseEnterGame`

**Signature:**
```cpp
void parseEnterGame(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parselogin)=
## `parseLogin`

**Signature:**
```cpp
void parseLogin(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsegmactions)=
## `parseGMActions`

**Signature:**
```cpp
void parseGMActions(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseupdateneeded)=
## `parseUpdateNeeded`

**Signature:**
```cpp
void parseUpdateNeeded(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseloginerror)=
## `parseLoginError`

**Signature:**
```cpp
void parseLoginError(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseloginadvice)=
## `parseLoginAdvice`

**Signature:**
```cpp
void parseLoginAdvice(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseloginwait)=
## `parseLoginWait`

**Signature:**
```cpp
void parseLoginWait(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parselogintoken)=
## `parseLoginToken`

**Signature:**
```cpp
void parseLoginToken(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseping)=
## `parsePing`

**Signature:**
```cpp
void parsePing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepingback)=
## `parsePingBack`

**Signature:**
```cpp
void parsePingBack(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsenewping)=
## `parseNewPing`

**Signature:**
```cpp
void parseNewPing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsechallenge)=
## `parseChallenge`

**Signature:**
```cpp
void parseChallenge(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedeath)=
## `parseDeath`

**Signature:**
```cpp
void parseDeath(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemapdescription)=
## `parseMapDescription`

**Signature:**
```cpp
void parseMapDescription(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsefloordescription)=
## `parseFloorDescription`

**Signature:**
```cpp
void parseFloorDescription(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemapmovenorth)=
## `parseMapMoveNorth`

**Signature:**
```cpp
void parseMapMoveNorth(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemapmoveeast)=
## `parseMapMoveEast`

**Signature:**
```cpp
void parseMapMoveEast(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemapmovesouth)=
## `parseMapMoveSouth`

**Signature:**
```cpp
void parseMapMoveSouth(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemapmovewest)=
## `parseMapMoveWest`

**Signature:**
```cpp
void parseMapMoveWest(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseupdatetile)=
## `parseUpdateTile`

**Signature:**
```cpp
void parseUpdateTile(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetileaddthing)=
## `parseTileAddThing`

**Signature:**
```cpp
void parseTileAddThing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetiletransformthing)=
## `parseTileTransformThing`

**Signature:**
```cpp
void parseTileTransformThing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetileremovething)=
## `parseTileRemoveThing`

**Signature:**
```cpp
void parseTileRemoveThing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturemove)=
## `parseCreatureMove`

**Signature:**
```cpp
void parseCreatureMove(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopencontainer)=
## `parseOpenContainer`

**Signature:**
```cpp
void parseOpenContainer(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseclosecontainer)=
## `parseCloseContainer`

**Signature:**
```cpp
void parseCloseContainer(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecontaineradditem)=
## `parseContainerAddItem`

**Signature:**
```cpp
void parseContainerAddItem(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecontainerupdateitem)=
## `parseContainerUpdateItem`

**Signature:**
```cpp
void parseContainerUpdateItem(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecontainerremoveitem)=
## `parseContainerRemoveItem`

**Signature:**
```cpp
void parseContainerRemoveItem(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseaddinventoryitem)=
## `parseAddInventoryItem`

**Signature:**
```cpp
void parseAddInventoryItem(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseremoveinventoryitem)=
## `parseRemoveInventoryItem`

**Signature:**
```cpp
void parseRemoveInventoryItem(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopennpctrade)=
## `parseOpenNpcTrade`

**Signature:**
```cpp
void parseOpenNpcTrade(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayergoods)=
## `parsePlayerGoods`

**Signature:**
```cpp
void parsePlayerGoods(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseclosenpctrade)=
## `parseCloseNpcTrade`

**Signature:**
```cpp
void parseCloseNpcTrade(const InputMessagePtr&);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | - | - |

---

(parseworldlight)=
## `parseWorldLight`

**Signature:**
```cpp
void parseWorldLight(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemagiceffect)=
## `parseMagicEffect`

**Signature:**
```cpp
void parseMagicEffect(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseanimatedtext)=
## `parseAnimatedText`

**Signature:**
```cpp
void parseAnimatedText(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedistancemissile)=
## `parseDistanceMissile`

**Signature:**
```cpp
void parseDistanceMissile(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturemark)=
## `parseCreatureMark`

**Signature:**
```cpp
void parseCreatureMark(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetrappers)=
## `parseTrappers`

**Signature:**
```cpp
void parseTrappers(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturehealth)=
## `parseCreatureHealth`

**Signature:**
```cpp
void parseCreatureHealth(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturelight)=
## `parseCreatureLight`

**Signature:**
```cpp
void parseCreatureLight(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreatureoutfit)=
## `parseCreatureOutfit`

**Signature:**
```cpp
void parseCreatureOutfit(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturespeed)=
## `parseCreatureSpeed`

**Signature:**
```cpp
void parseCreatureSpeed(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreatureskulls)=
## `parseCreatureSkulls`

**Signature:**
```cpp
void parseCreatureSkulls(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreatureshields)=
## `parseCreatureShields`

**Signature:**
```cpp
void parseCreatureShields(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreatureunpass)=
## `parseCreatureUnpass`

**Signature:**
```cpp
void parseCreatureUnpass(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseedittext)=
## `parseEditText`

**Signature:**
```cpp
void parseEditText(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseeditlist)=
## `parseEditList`

**Signature:**
```cpp
void parseEditList(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepremiumtrigger)=
## `parsePremiumTrigger`

**Signature:**
```cpp
void parsePremiumTrigger(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepreyfreerolls)=
## `parsePreyFreeRolls`

**Signature:**
```cpp
void parsePreyFreeRolls(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepreytimeleft)=
## `parsePreyTimeLeft`

**Signature:**
```cpp
void parsePreyTimeLeft(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepreydata)=
## `parsePreyData`

**Signature:**
```cpp
void parsePreyData(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepreyprices)=
## `parsePreyPrices`

**Signature:**
```cpp
void parsePreyPrices(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsestoreofferdescription)=
## `parseStoreOfferDescription`

**Signature:**
```cpp
void parseStoreOfferDescription(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerinfo)=
## `parsePlayerInfo`

**Signature:**
```cpp
void parsePlayerInfo(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerstats)=
## `parsePlayerStats`

**Signature:**
```cpp
void parsePlayerStats(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerskills)=
## `parsePlayerSkills`

**Signature:**
```cpp
void parsePlayerSkills(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerstate)=
## `parsePlayerState`

**Signature:**
```cpp
void parsePlayerState(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayercancelattack)=
## `parsePlayerCancelAttack`

**Signature:**
```cpp
void parsePlayerCancelAttack(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayermodes)=
## `parsePlayerModes`

**Signature:**
```cpp
void parsePlayerModes(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsespellcooldown)=
## `parseSpellCooldown`

**Signature:**
```cpp
void parseSpellCooldown(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsespellgroupcooldown)=
## `parseSpellGroupCooldown`

**Signature:**
```cpp
void parseSpellGroupCooldown(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemultiusecooldown)=
## `parseMultiUseCooldown`

**Signature:**
```cpp
void parseMultiUseCooldown(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetalk)=
## `parseTalk`

**Signature:**
```cpp
void parseTalk(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsechannellist)=
## `parseChannelList`

**Signature:**
```cpp
void parseChannelList(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopenchannel)=
## `parseOpenChannel`

**Signature:**
```cpp
void parseOpenChannel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopenprivatechannel)=
## `parseOpenPrivateChannel`

**Signature:**
```cpp
void parseOpenPrivateChannel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopenownprivatechannel)=
## `parseOpenOwnPrivateChannel`

**Signature:**
```cpp
void parseOpenOwnPrivateChannel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseclosechannel)=
## `parseCloseChannel`

**Signature:**
```cpp
void parseCloseChannel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseruleviolationchannel)=
## `parseRuleViolationChannel`

**Signature:**
```cpp
void parseRuleViolationChannel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseruleviolationremove)=
## `parseRuleViolationRemove`

**Signature:**
```cpp
void parseRuleViolationRemove(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseruleviolationcancel)=
## `parseRuleViolationCancel`

**Signature:**
```cpp
void parseRuleViolationCancel(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseruleviolationlock)=
## `parseRuleViolationLock`

**Signature:**
```cpp
void parseRuleViolationLock(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseowntrade)=
## `parseOwnTrade`

**Signature:**
```cpp
void parseOwnTrade(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecountertrade)=
## `parseCounterTrade`

**Signature:**
```cpp
void parseCounterTrade(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseclosetrade)=
## `parseCloseTrade`

**Signature:**
```cpp
void parseCloseTrade(const InputMessagePtr&);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | - | - |

---

(parsetextmessage)=
## `parseTextMessage`

**Signature:**
```cpp
void parseTextMessage(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecancelwalk)=
## `parseCancelWalk`

**Signature:**
```cpp
void parseCancelWalk(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsewalkwait)=
## `parseWalkWait`

**Signature:**
```cpp
void parseWalkWait(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsefloorchangeup)=
## `parseFloorChangeUp`

**Signature:**
```cpp
void parseFloorChangeUp(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsefloorchangedown)=
## `parseFloorChangeDown`

**Signature:**
```cpp
void parseFloorChangeDown(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopenoutfitwindow)=
## `parseOpenOutfitWindow`

**Signature:**
```cpp
void parseOpenOutfitWindow(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsevipadd)=
## `parseVipAdd`

**Signature:**
```cpp
void parseVipAdd(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsevipstate)=
## `parseVipState`

**Signature:**
```cpp
void parseVipState(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseviplogout)=
## `parseVipLogout`

**Signature:**
```cpp
void parseVipLogout(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsevipgroupdata)=
## `parseVipGroupData`

**Signature:**
```cpp
void parseVipGroupData(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetutorialhint)=
## `parseTutorialHint`

**Signature:**
```cpp
void parseTutorialHint(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecyclopediamapdata)=
## `parseCyclopediaMapData`

**Signature:**
```cpp
void parseCyclopediaMapData(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsequestlog)=
## `parseQuestLog`

**Signature:**
```cpp
void parseQuestLog(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsequestline)=
## `parseQuestLine`

**Signature:**
```cpp
void parseQuestLine(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsechannelevent)=
## `parseChannelEvent`

**Signature:**
```cpp
void parseChannelEvent(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseiteminfo)=
## `parseItemInfo`

**Signature:**
```cpp
void parseItemInfo(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseplayerinventory)=
## `parsePlayerInventory`

**Signature:**
```cpp
void parsePlayerInventory(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemodaldialog)=
## `parseModalDialog`

**Signature:**
```cpp
void parseModalDialog(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseclientcheck)=
## `parseClientCheck`

**Signature:**
```cpp
void parseClientCheck(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsegamenews)=
## `parseGameNews`

**Signature:**
```cpp
void parseGameNews(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsemessagedialog)=
## `parseMessageDialog`

**Signature:**
```cpp
void parseMessageDialog(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseblessdialog)=
## `parseBlessDialog`

**Signature:**
```cpp
void parseBlessDialog(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseresourcebalance)=
## `parseResourceBalance`

**Signature:**
```cpp
void parseResourceBalance(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseservertime)=
## `parseServerTime`

**Signature:**
```cpp
void parseServerTime(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsequesttracker)=
## `parseQuestTracker`

**Signature:**
```cpp
void parseQuestTracker(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseimbuementwindow)=
## `parseImbuementWindow`

**Signature:**
```cpp
void parseImbuementWindow(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecloseimbuementwindow)=
## `parseCloseImbuementWindow`

**Signature:**
```cpp
void parseCloseImbuementWindow(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecyclopedianewdetails)=
## `parseCyclopediaNewDetails`

**Signature:**
```cpp
void parseCyclopediaNewDetails(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecyclopedia)=
## `parseCyclopedia`

**Signature:**
```cpp
void parseCyclopedia(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedailyrewardstate)=
## `parseDailyRewardState`

**Signature:**
```cpp
void parseDailyRewardState(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseopenrewardwall)=
## `parseOpenRewardWall`

**Signature:**
```cpp
void parseOpenRewardWall(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedailyreward)=
## `parseDailyReward`

**Signature:**
```cpp
void parseDailyReward(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedailyrewardhistory)=
## `parseDailyRewardHistory`

**Signature:**
```cpp
void parseDailyRewardHistory(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsekilltracker)=
## `parseKillTracker`

**Signature:**
```cpp
void parseKillTracker(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parselootcontainers)=
## `parseLootContainers`

**Signature:**
```cpp
void parseLootContainers(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsesupplystash)=
## `parseSupplyStash`

**Signature:**
```cpp
void parseSupplyStash(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsespecialcontainer)=
## `parseSpecialContainer`

**Signature:**
```cpp
void parseSpecialContainer(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedepotstate)=
## `parseDepotState`

**Signature:**
```cpp
void parseDepotState(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsesupplytracker)=
## `parseSupplyTracker`

**Signature:**
```cpp
void parseSupplyTracker(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsetournamentleaderboard)=
## `parseTournamentLeaderboard`

**Signature:**
```cpp
void parseTournamentLeaderboard(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseimpacttracker)=
## `parseImpactTracker`

**Signature:**
```cpp
void parseImpactTracker(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseitemsprices)=
## `parseItemsPrices`

**Signature:**
```cpp
void parseItemsPrices(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseloottracker)=
## `parseLootTracker`

**Signature:**
```cpp
void parseLootTracker(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseitemdetail)=
## `parseItemDetail`

**Signature:**
```cpp
void parseItemDetail(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsehunting)=
## `parseHunting`

**Signature:**
```cpp
void parseHunting(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseextendedopcode)=
## `parseExtendedOpcode`

**Signature:**
```cpp
void parseExtendedOpcode(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsechangemapawarerange)=
## `parseChangeMapAwareRange`

**Signature:**
```cpp
void parseChangeMapAwareRange(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseprogressbar)=
## `parseProgressBar`

**Signature:**
```cpp
void parseProgressBar(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsefeatures)=
## `parseFeatures`

**Signature:**
```cpp
void parseFeatures(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsecreaturesmark)=
## `parseCreaturesMark`

**Signature:**
```cpp
void parseCreaturesMark(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsenewcancelwalk)=
## `parseNewCancelWalk`

**Signature:**
```cpp
void parseNewCancelWalk(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsepredictivecancelwalk)=
## `parsePredictiveCancelWalk`

**Signature:**
```cpp
void parsePredictiveCancelWalk(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsewalkid)=
## `parseWalkId`

**Signature:**
```cpp
void parseWalkId(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parseprocessesrequest)=
## `parseProcessesRequest`

**Signature:**
```cpp
void parseProcessesRequest(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsedllsrequest)=
## `parseDllsRequest`

**Signature:**
```cpp
void parseDllsRequest(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(parsewindowsrequest)=
## `parseWindowsRequest`

**Signature:**
```cpp
void parseWindowsRequest(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

---

(setmapdescription)=
## `setMapDescription`

**Signature:**
```cpp
public: void setMapDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |
| `int` | `x` | - |
| `int` | `y` | - |
| `int` | `z` | - |
| `int` | `width` | - |
| `int` | `height` | - |

---

(setfloordescription)=
## `setFloorDescription`

**Signature:**
```cpp
int setFloorDescription(const InputMessagePtr& msg, int x, int y, int z, int width, int height, int offset, int skip);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |
| `int` | `x` | - |
| `int` | `y` | - |
| `int` | `z` | - |
| `int` | `width` | - |
| `int` | `height` | - |
| `int` | `offset` | - |
| `int` | `skip` | - |

**Returns:**
- `int`

---

(settiledescription)=
## `setTileDescription`

**Signature:**
```cpp
int setTileDescription(const InputMessagePtr& msg, Position position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |
| `Position` | `position` | - |

**Returns:**
- `int`

---

(getoutfit)=
## `getOutfit`

**Signature:**
```cpp
Outfit getOutfit(const InputMessagePtr& msg, bool ignoreMount = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const InputMessagePtr&` | `msg` |  | - |
| `bool` | `ignoreMount` | `false` | - |

**Returns:**
- `Outfit`

---

(getthing)=
## `getThing`

**Signature:**
```cpp
ThingPtr getThing(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

**Returns:**
- `ThingPtr`

---

(getmappedthing)=
## `getMappedThing`

**Signature:**
```cpp
ThingPtr getMappedThing(const InputMessagePtr & msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr &` | `msg` | - |

**Returns:**
- `ThingPtr`

---

(getcreature)=
## `getCreature`

**Signature:**
```cpp
CreaturePtr getCreature(const InputMessagePtr& msg, int type = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const InputMessagePtr&` | `msg` |  | - |
| `int` | `type` | `0` | - |

**Returns:**
- `CreaturePtr`

---

(getstatictext)=
## `getStaticText`

**Signature:**
```cpp
StaticTextPtr getStaticText(const InputMessagePtr& msg, int type = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const InputMessagePtr&` | `msg` |  | - |
| `int` | `type` | `0` | - |

**Returns:**
- `StaticTextPtr`

---

(getitem)=
## `getItem`

**Signature:**
```cpp
ItemPtr getItem(const InputMessagePtr& msg, int id = 0, bool hasDescription = true);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const InputMessagePtr&` | `msg` |  | - |
| `int` | `id` | `0` | - |
| `bool` | `hasDescription` | `true` | - |

**Returns:**
- `ItemPtr`

---

(getposition)=
## `getPosition`

**Signature:**
```cpp
Position getPosition(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

**Returns:**
- `Position`

---

(getimbuementinfo)=
## `getImbuementInfo`

**Signature:**
```cpp
Imbuement getImbuementInfo(const InputMessagePtr& msg);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputMessagePtr&` | `msg` | - |

**Returns:**
- `Imbuement`

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

