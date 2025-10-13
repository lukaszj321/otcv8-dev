# Diagrams


## Diagrams

```{mermaid}
:caption: Actionbar

graph TD
    W0["cooldown (ActionButton)"]
    W1["image (LeftSliders)"]
    W2["nextPanel (RightSliders)"]
```

```{mermaid}
:caption: Alarms

graph TD
    W0["tick (AlarmCheckBox)"]
    W1["value (AlarmCheckBoxAndSpinBox)"]
    W2["text (AlarmCheckBoxAndTextEdit)"]
    W3["closeButton (AlarmsWindow)"]
```

```{mermaid}
:caption: Amountwindow

graph TD
    W0["buttonOk (AmountWindow)"]
```

```{mermaid}
:caption: Analyzer

graph TD
    W0["cooldown (BossCreaturePanel)"]
    W1["clear (SearchPanel)"]
    W2["drops (TrackerItem)"]
    W3["value (DualLabel)"]
    W4["healing (MemberWidget)"]
    W5["remove (AnalyzerPriceLabel)"]
    W6["AnalyzerListPanel (AnalyzerListPanel)"]
    W7["ListLabel (ListLabel)"]
    W8["List (AnalyzerItemsPanel)"]
    W9["count (AnalyzerLootItem)"]
    W10["AnalyzerGraph (AnalyzerGraph)"]
    W11["AnalyzerProgressBar (AnalyzerProgressBar)"]
    W12["AnalyzerButton (AnalyzerButton)"]
    W13["ResetSession (MainAnalyzerWindow)"]
    W14["HuntingAnalyzerWindow (HuntingAnalyzer)"]
    W15["LootAnalyzerWindow (LootAnalyzer)"]
    W16["SupplyAnalyzerWindow (SupplyAnalyzer)"]
    W17["ImpactAnalyzerWindow (ImpactAnalyzer)"]
    W18["XPAnalyzerWindow (XPAnalyzer)"]
    W19["PartyAnalyzerWindow (PartyAnalyzerWindow)"]
    W20["DropTracker (DropTracker)"]
    W21["CaveBotStats (CaveBotStats)"]
    W22["search (BossTracker)"]
    W23["closeButton (FeaturesWindow)"]
```

```{mermaid}
:caption: Architecture

graph LR
    subgraph UI (OTUI)
        E0[Widgets]
        E1[UI Components]
        E2[Layouts]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Attackbot

graph TD
    W0["remove (AttackEntry)"]
    W1["name (AttackBotBotPanel)"]
    W2["description (CategoryLabel)"]
    W3["description (SourceLabel)"]
    W4["description (RangeLabel)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["spellName (AttackBotPanel)"]
    W8["AntiRsRange (SettingsPanel)"]
    W9["settings (AttackBotWindow)"]
```

```{mermaid}
:caption: Basic

graph TD
    W0["BotButton (BotButton)"]
    W1["BotSwitch (BotSwitch)"]
    W2["SmallBotSwitch (SmallBotSwitch)"]
    W3["BotLabel (BotLabel)"]
    W4["BotItem (BotItem)"]
    W5["BotTextEdit (BotTextEdit)"]
    W6["BotSeparator (BotSeparator)"]
    W7["botPanelScroll (BotSmallScrollBar)"]
    W8["botPanelScroll (BotPanel)"]
    W9["CaveBotLabel (CaveBotLabel)"]
    W10["SlotComboBoxPopupMenu (SlotComboBoxPopupMenu)"]
    W11["SlotComboBoxPopupMenuButton (SlotComboBoxPopupMenuButton)"]
    W12["SlotComboBox (SlotComboBox)"]
```

```{mermaid}
:caption: Battle

graph TD
    W0["BattleIcon (BattleIcon)"]
    W1["BattlePlayers (BattlePlayers)"]
    W0 --> W1
    W2["BattleNPCs (BattleNPCs)"]
    W0 --> W2
    W3["BattleMonsters (BattleMonsters)"]
    W0 --> W3
    W4["BattleSkulls (BattleSkulls)"]
    W0 --> W4
    W5["battlePanel (BattleParty)"]
    W0 --> W5
```

```{mermaid}
:caption: Battlebutton

graph TD
    W0["BattleButton (BattleButton)"]
```

```{mermaid}
:caption: Bot

graph TD
    W0["BotTabBar (BotTabBar)"]
    W1["botPanel (BotTabBarPanel)"]
    W2["botPanel (BotTabBarButton)"]
```

```{mermaid}
:caption: Botserver

graph TD
    W0["Members (BotServerData)"]
    W1["Broadcast (FeaturePanel)"]
    W2["enabled (BotServerWindow)"]
```

```{mermaid}
:caption: Browse

graph TD
    W0["filterSearchAll (MarketItemBox)"]
```

```{mermaid}
:caption: Bugreport

graph TD
    W0["cancelButton (BugReportWindow)"]
```

```{mermaid}
:caption: Cavebot

graph TD
    W0["CaveBotAction (CaveBotAction)"]
    W1["showConfig (CaveBotPanel)"]
```

```{mermaid}
:caption: Channelswindow

graph TD
    W0["channelsScrollBar (ChannelListLabel)"]
```

```{mermaid}
:caption: Characterlist

graph TD
    W0["buttonCancel (CharacterWidget)"]
```

```{mermaid}
:caption: Combo

graph TD
    W0["AttackComboBoxPopupMenu (AttackComboBoxPopupMenu)"]
    W1["AttackComboBoxPopupMenuButton (AttackComboBoxPopupMenuButton)"]
    W2["AttackComboBox (AttackComboBox)"]
    W3["FollowComboBoxPopupMenu (FollowComboBoxPopupMenu)"]
    W4["FollowComboBoxPopupMenuButton (FollowComboBoxPopupMenuButton)"]
    W5["FollowComboBox (FollowComboBox)"]
    W6["onCastToggle (ComboTrigger)"]
    W7["commandsToggle (ComboActions)"]
    W8["Triggers (BotServer)"]
    W9["toolsButton (ComboWindow)"]
```

```{mermaid}
:caption: Communicationwindow

graph TD
    W0["IgnoreListLabel (IgnoreListLabel)"]
    W1["whiteListScrollBar (WhiteListLabel)"]
```

```{mermaid}
:caption: Conditions

graph TD
    W0["UturaComboBoxPopupMenu (UturaComboBoxPopupMenu)"]
    W1["UturaComboBoxPopupMenuButton (UturaComboBoxPopupMenuButton)"]
    W2["UturaComboBox (UturaComboBox)"]
    W3["ParalyseSpell (CureConditions)"]
    W4["StopHaste (HoldConditions)"]
    W5["closeButton (ConditionsWindow)"]
```

```{mermaid}
:caption: Config

graph TD
    W0["remove (BotConfig)"]
```

```{mermaid}
:caption: Container

graph TD
    W0["scroll (BotContainer)"]
```

```{mermaid}
:caption: Cooldown

graph TD
    W0["SpellGroupIcon (SpellGroupIcon)"]
    W1["SpellIcon (SpellIcon)"]
    W2["SpellProgressRect (SpellProgressRect)"]
    W3["cooldownPanel (GroupCooldownParticles)"]
```

```{mermaid}
:caption: Countwindow

graph TD
    W0["buttonOk (CountWindow)"]
```

```{mermaid}
:caption: Creature Editor

graph TD
    W0["scroll (TargetBotCreatureEditorScrollBar)"]
    W1["textEdit (TargetBotCreatureEditorTextEdit)"]
    W2["item (TargetBotCreatureEditorItem)"]
    W3["TargetBotCreatureEditorCheckBox (TargetBotCreatureEditorCheckBox)"]
    W4["cancel (TargetBotCreatureEditorWindow)"]
```

```{mermaid}
:caption: Currentoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["myBuyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Deathwindow

graph TD
    W0["buttonCancel (DeathWindow)"]
```

```{mermaid}
:caption: Depositer Config

graph TD
    W0["slot (StashItem)"]
    W1["CloseButton (DepositerPanel)"]
```

```{mermaid}
:caption: Editor

graph TD
    W0["autoRecording (CaveBotEditorButton)"]
    W1["autoRecording (CaveBotEditorPanel)"]
```

```{mermaid}
:caption: Editvip

graph TD
    W0["buttonCancel (IconButton)"]
```

```{mermaid}
:caption: Equipper

graph TD
    W0["SlotBotItem (SlotBotItem)"]
    W1["remove (BossLabel)"]
    W2["ConditionBoxPopupMenu (ConditionBoxPopupMenu)"]
    W3["ConditionBoxPopupMenuButton (ConditionBoxPopupMenuButton)"]
    W4["ConditionBox (ConditionBox)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["text (CondidionLabel)"]
    W8["visible (Rule)"]
    W9["text (ConditionPanel)"]
    W10["down (ListPanel)"]
    W11["add (InputPanel)"]
    W12["default (EQPanel)"]
    W13["profileName (Profile)"]
    W14["add (BossList)"]
    W15["bossList (EquipWindow)"]
```

```{mermaid}
:caption: Extras

graph TD
    W0["scroll (ExtrasScrollBar)"]
    W1["textEdit (ExtrasTextEdit)"]
    W2["item (ExtrasItem)"]
    W3["ExtrasCheckBox (ExtrasCheckBox)"]
    W4["closeButton (ExtrasWindow)"]
```

```{mermaid}
:caption: Flagwindow

graph TD
    W0["FlagButton (FlagButton)"]
    W1["cancelButton (FlagWindow)"]
```

```{mermaid}
:caption: Flow

graph TD
    A[UI (OTUI)] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```

```{mermaid}
:caption: Gameinterface

graph TD
    W0["GameSidePanel (GameSidePanel)"]
    W1["GameMapPanel (GameMapPanel)"]
    W2["gameTopBar (GameAction)"]
```

```{mermaid}
:caption: Healbot

graph TD
    W0["SettingCheckBox (SettingCheckBox)"]
    W1["SpellSourceBoxPopupMenu (SpellSourceBoxPopupMenu)"]
    W2["SpellSourceBoxPopupMenuButton (SpellSourceBoxPopupMenuButton)"]
    W3["SpellSourceBox (SpellSourceBox)"]
    W4["SpellConditionBoxPopupMenu (SpellConditionBoxPopupMenu)"]
    W5["SpellConditionBoxPopupMenuButton (SpellConditionBoxPopupMenuButton)"]
    W6["SpellConditionBox (SpellConditionBox)"]
    W7["remove (SpellEntry)"]
    W8["remove (ItemEntry)"]
    W9["MoveDown (SpellHealing)"]
    W10["MoveDown (ItemHealing)"]
    W11["items (HealerPanel)"]
    W12["ResetSettings (HealBotSettingsPanel)"]
    W13["settingsButton (HealWindow)"]
```

```{mermaid}
:caption: Hotkeys Manager

graph TD
    W0["cancelButton (HotkeyListLabel)"]
    W1["cancelButton (HotkeyAssignWindow)"]
```

```{mermaid}
:caption: Icons

graph TD
    W0["text (BotIcon)"]
```

```{mermaid}
:caption: Imbuing

graph TD
    W0["Slot (Slot)"]
    W1["count (RequiredItem)"]
    W2["selectSlot (ItemInformation)"]
    W3["cost (EmptyImbue)"]
    W4["balance (ClearImbue)"]
```

```{mermaid}
:caption: Itemdetails

graph TD
    W0["DetailsTableRow (DetailsTableRow)"]
    W1["detailsTableScrollBar (DetailsTableColumn)"]
```

```{mermaid}
:caption: Itemoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["buyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Itemselector

graph TD
    W0["cancelButton (ItemSelectorWindow)"]
```

```{mermaid}
:caption: Itemstats

graph TD
    W0["StatsTableRow (StatsTableRow)"]
    W1["sellStatsTableScrollBar (StatsTableColumn)"]
```

```{mermaid}
:caption: Locales

graph TD
    W0["LocalesMainLabel (LocalesMainLabel)"]
    W1["localesPanel (LocalesButton)"]
```

```{mermaid}
:caption: Looting

graph TD
    W0["value (TargetBotLootingPanel)"]
```

```{mermaid}
:caption: Market

graph TD
    W0["resetButton (MarketWindow)"]
```

```{mermaid}
:caption: Marketbuttons

graph TD
    W0["MarketButtonBox (MarketButtonBox)"]
```

```{mermaid}
:caption: Marketcombobox

graph TD
    W0["MarketComboBoxPopupMenuButton (MarketComboBoxPopupMenuButton)"]
    W1["MarketComboBoxPopupMenuSeparator (MarketComboBoxPopupMenuSeparator)"]
    W2["MarketComboBoxPopupMenu (MarketComboBoxPopupMenu)"]
    W3["MarketComboBox (MarketComboBox)"]
```

```{mermaid}
:caption: Markettabs

graph TD
    W0["MarketTabBar (MarketTabBar)"]
    W1["MarketTabBarPanel (MarketTabBarPanel)"]
    W2["MarketTabBarButton (MarketTabBarButton)"]
    W3["MarketRightTabBar (MarketRightTabBar)"]
    W4["MarketRightTabBarPanel (MarketRightTabBarPanel)"]
    W5["MarketRightTabBarButton (MarketRightTabBarButton)"]
```

```{mermaid}
:caption: Modaldialog

graph TD
    W0["ChoiceListLabel (ChoiceListLabel)"]
    W1["choiceList (ChoiceList)"]
    W2["choiceScrollBar (ChoiceScrollBar)"]
    W3["ModalButton (ModalButton)"]
    W4["buttonsPanel (ModalDialog)"]
```

```{mermaid}
:caption: New Healer

graph TD
    W0["CategoryCheckBox (CategoryCheckBox)"]
    W1["scroll (HealScroll)"]
    W2["text (HealItem)"]
    W3["ToolTipLabel (ToolTipLabel)"]
    W4["remove (HealerPlayerEntry)"]
    W5["decrement (PriorityEntry)"]
    W3 --> W5
    W6["vocations (TargetSettings)"]
    W7["botserver (Groups)"]
    W8["sorcerers (Vocations)"]
    W9["list (Priority)"]
    W10["add (AddPlayer)"]
    W11["listScrollBar (PlayerList)"]
    W12["playerList (CustomList)"]
    W13["box (Conditions)"]
    W14["closeButton (FriendHealer)"]
```

```{mermaid}
:caption: Npctrade

graph TD
    W0["NPCOfferLabel (NPCOfferLabel)"]
    W1["tradeButton (NPCItemBox)"]
```

```{mermaid}
:caption: Object

graph TD
    W0["buttonOk (RoundCheckBox)"]
```

```{mermaid}
:caption: Options

graph TD
    W0["OptionCheckBox (OptionCheckBox)"]
    W1["OptionScrollbar (OptionScrollbar)"]
    W2["optionsTabContent (OptionPanel)"]
```

```{mermaid}
:caption: Outfitwindow

graph TD
    W0["FloorTile (FloorTile)"]
```

```{mermaid}
:caption: Panels

graph TD
    W0["text (DualScrollPanel)"]
    W1["scroll (SingleScrollItemPanel)"]
    W2["scroll2 (DualScrollItemPanel)"]
    W3["item5 (ItemsRow)"]
    W4["items (ItemsPanel)"]
    W5["title (ItemAndButtonPanel)"]
    W6["slot (ItemAndSlotPanel)"]
    W7["slot (TwoItemsAndSlotPanel)"]
    W8["right (DualLabelPanel)"]
    W9["right (LabelAndTextEditPanel)"]
    W10["left (SwitchAndButtonPanel)"]
```

```{mermaid}
:caption: Playerlist

graph TD
    W0["remove (PlayerLabel)"]
    W1["SettingCheckBox (SettingCheckBox)"]
    W2["AutoAdd (Settings)"]
    W3["add (tPanel)"]
    W4["closeButton (PlayerListWindow)"]
```

```{mermaid}
:caption: Prey

graph TD
    W0["shopTempButton (LockedPreyPanel)"]
    W1["Star (Star)"]
    W2["NoStar (NoStar)"]
    W3["noBonusIcon (NoCreaturePanel)"]
    W4["lockPreyPrice (ActivePreyPanel)"]
    W5["timeLeft (CreatureAndBonus)"]
    W6["price (BonusReroll)"]
    W7["list (InactivePreyPanel)"]
    W8["choosePreyButton (ChoosePrey)"]
    W9["price (SelectPreyCreature)"]
    W10["price (RerollButton)"]
    W11["text (CardLabel)"]
    W12["text (GoldLabel)"]
    W13["creature (PreyCreatureBox)"]
    W14["openStore (SlotPanel)"]
    W15["time (PreyCreature)"]
    W16["slot3 (PreyTracker)"]
```

```{mermaid}
:caption: Pushmax

graph TD
    W0["closeButton (PushMaxWindow)"]
```

```{mermaid}
:caption: Questlogwindow

graph TD
    W0["description (QuestTrackerLabel)"]
    W1["QuestLabel (QuestLabel)"]
    W2["questListScrollBar (QuestLog)"]
    W3["missionDescription (MissionLog)"]
    W4["trackerButton (QuestLogWindow)"]
    W5["list (QuestTracker)"]
```

```{mermaid}
:caption: Ruleviolation

graph TD
    W0["RVListLabel (RVListLabel)"]
    W1["RVLabel (RVLabel)"]
    W2["commentText (RVTextEdit)"]
```

```{mermaid}
:caption: Shop

graph TD
    W0["name (ShopCategory)"]
    W1["item (ShopCategoryItem)"]
    W0 --> W1
    W2["creature (ShopCategoryCreature)"]
    W0 --> W2
    W3["image (ShopCategoryImage)"]
    W0 --> W3
    W4["buyButton (ShopOffer)"]
    W5["item (ShopOfferItem)"]
    W4 --> W5
    W6["creature (ShopOfferCreature)"]
    W4 --> W6
    W7["buttonCancel (ShopOfferImage)"]
    W4 --> W7
```

```{mermaid}
:caption: Sideactionbar

graph TD
    W0["cooldown (SideActionButton)"]
    W1["image (TopSliders)"]
    W2["nextPanel (BottomSliders)"]
```

```{mermaid}
:caption: Siolist

graph TD
    W0["RP (VocationPanel)"]
    W1["closeButton (SioListWindow)"]
```

```{mermaid}
:caption: Skills

graph TD
    W0["SkillFirstWidget (SkillFirstWidget)"]
    W1["SkillButton (SkillButton)"]
    W2["SmallSkillButton (SmallSkillButton)"]
    W1 --> W2
    W3["SkillNameLabel (SkillNameLabel)"]
    W4["value (SkillValueLabel)"]
    W5["skillId12 (SkillPercentPanel)"]
```

```{mermaid}
:caption: Spell

graph TD
    W0["buttonOk (SpellPreview)"]
```

```{mermaid}
:caption: Spelllist

graph TD
    W0["SpellListLabel (SpellListLabel)"]
    W1["SpellInfoLabel (SpellInfoLabel)"]
    W2["SpellInfoValueLabel (SpellInfoValueLabel)"]
    W3["premiumBoxYes (FilterButton)"]
```

```{mermaid}
:caption: Stats

graph TD
    W0["DebugText (DebugText)"]
    W1["debugScroll (DebugLabel)"]
```

```{mermaid}
:caption: Supplies

graph TD
    W0["remove (ProfileLabel)"]
    W1["SupplySpinBox (SupplySpinBox)"]
    W2["avg (ItemPanel)"]
    W3["decrement (SuppliesWindow)"]
```

```{mermaid}
:caption: Supply

graph TD
    W0["max (SupplyItem)"]
    W1["scroll (SupplyItemList)"]
```

```{mermaid}
:caption: Target

graph TD
    W0["TargetBotEntry (TargetBotEntry)"]
    W1["right (TargetBotDualLabel)"]
    W2["debug (TargetBotPanel)"]
```

```{mermaid}
:caption: Terminal

graph TD
    W0["TerminalLabel (TerminalLabel)"]
    W1["rightResizeBorder (TerminalSelectText)"]
```

```{mermaid}
:caption: Textedit

graph TD
    W0["cancel (TextEditButtons)"]
    W1["examples (TextEditWindow)"]
    W2["text (SinglelineTextEditWindow)"]
    W1 --> W2
    W3["textScroll (MultilineTextEditWindow)"]
    W1 --> W3
```

```{mermaid}
:caption: Textmessage

graph TD
    W0["statusLabel (TextMessageLabel)"]
```

```{mermaid}
:caption: Textwindow

graph TD
    W0["cancelButton (TextWindow)"]
```

```{mermaid}
:caption: Topbar

graph TD
    W0["box (StatsPanel)"]
    W1["skills (SkillPanel)"]
```

```{mermaid}
:caption: Tradewindow

graph TD
    W0["rejectButton (TradeWindow)"]
```

```{mermaid}
:caption: Unjustifiedpoints

graph TD
    W0["SkullProgressBar (SkullProgressBar)"]
    W1["monthSkullWidget (SkullWidget)"]
```

```{mermaid}
:caption: Viplist

graph TD
    W0["vipWindow (VipListLabel)"]
```


## Diagrams

```{mermaid}
:caption: Actionbar

graph TD
    W0["cooldown (ActionButton)"]
    W1["image (LeftSliders)"]
    W2["nextPanel (RightSliders)"]
```

```{mermaid}
:caption: Alarms

graph TD
    W0["tick (AlarmCheckBox)"]
    W1["value (AlarmCheckBoxAndSpinBox)"]
    W2["text (AlarmCheckBoxAndTextEdit)"]
    W3["closeButton (AlarmsWindow)"]
```

```{mermaid}
:caption: Amountwindow

graph TD
    W0["buttonOk (AmountWindow)"]
```

```{mermaid}
:caption: Analyzer

graph TD
    W0["cooldown (BossCreaturePanel)"]
    W1["clear (SearchPanel)"]
    W2["drops (TrackerItem)"]
    W3["value (DualLabel)"]
    W4["healing (MemberWidget)"]
    W5["remove (AnalyzerPriceLabel)"]
    W6["AnalyzerListPanel (AnalyzerListPanel)"]
    W7["ListLabel (ListLabel)"]
    W8["List (AnalyzerItemsPanel)"]
    W9["count (AnalyzerLootItem)"]
    W10["AnalyzerGraph (AnalyzerGraph)"]
    W11["AnalyzerProgressBar (AnalyzerProgressBar)"]
    W12["AnalyzerButton (AnalyzerButton)"]
    W13["ResetSession (MainAnalyzerWindow)"]
    W14["HuntingAnalyzerWindow (HuntingAnalyzer)"]
    W15["LootAnalyzerWindow (LootAnalyzer)"]
    W16["SupplyAnalyzerWindow (SupplyAnalyzer)"]
    W17["ImpactAnalyzerWindow (ImpactAnalyzer)"]
    W18["XPAnalyzerWindow (XPAnalyzer)"]
    W19["PartyAnalyzerWindow (PartyAnalyzerWindow)"]
    W20["DropTracker (DropTracker)"]
    W21["CaveBotStats (CaveBotStats)"]
    W22["search (BossTracker)"]
    W23["closeButton (FeaturesWindow)"]
```

```{mermaid}
:caption: Architecture

graph LR
    subgraph UI (OTUI)
        E0[Widgets]
        E1[UI Components]
        E2[Layouts]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Attackbot

graph TD
    W0["remove (AttackEntry)"]
    W1["name (AttackBotBotPanel)"]
    W2["description (CategoryLabel)"]
    W3["description (SourceLabel)"]
    W4["description (RangeLabel)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["spellName (AttackBotPanel)"]
    W8["AntiRsRange (SettingsPanel)"]
    W9["settings (AttackBotWindow)"]
```

```{mermaid}
:caption: Basic

graph TD
    W0["BotButton (BotButton)"]
    W1["BotSwitch (BotSwitch)"]
    W2["SmallBotSwitch (SmallBotSwitch)"]
    W3["BotLabel (BotLabel)"]
    W4["BotItem (BotItem)"]
    W5["BotTextEdit (BotTextEdit)"]
    W6["BotSeparator (BotSeparator)"]
    W7["botPanelScroll (BotSmallScrollBar)"]
    W8["botPanelScroll (BotPanel)"]
    W9["CaveBotLabel (CaveBotLabel)"]
    W10["SlotComboBoxPopupMenu (SlotComboBoxPopupMenu)"]
    W11["SlotComboBoxPopupMenuButton (SlotComboBoxPopupMenuButton)"]
    W12["SlotComboBox (SlotComboBox)"]
```

```{mermaid}
:caption: Battle

graph TD
    W0["BattleIcon (BattleIcon)"]
    W1["BattlePlayers (BattlePlayers)"]
    W0 --> W1
    W2["BattleNPCs (BattleNPCs)"]
    W0 --> W2
    W3["BattleMonsters (BattleMonsters)"]
    W0 --> W3
    W4["BattleSkulls (BattleSkulls)"]
    W0 --> W4
    W5["battlePanel (BattleParty)"]
    W0 --> W5
```

```{mermaid}
:caption: Battlebutton

graph TD
    W0["BattleButton (BattleButton)"]
```

```{mermaid}
:caption: Bot

graph TD
    W0["BotTabBar (BotTabBar)"]
    W1["botPanel (BotTabBarPanel)"]
    W2["botPanel (BotTabBarButton)"]
```

```{mermaid}
:caption: Botserver

graph TD
    W0["Members (BotServerData)"]
    W1["Broadcast (FeaturePanel)"]
    W2["enabled (BotServerWindow)"]
```

```{mermaid}
:caption: Browse

graph TD
    W0["filterSearchAll (MarketItemBox)"]
```

```{mermaid}
:caption: Bugreport

graph TD
    W0["cancelButton (BugReportWindow)"]
```

```{mermaid}
:caption: Cavebot

graph TD
    W0["CaveBotAction (CaveBotAction)"]
    W1["showConfig (CaveBotPanel)"]
```

```{mermaid}
:caption: Channelswindow

graph TD
    W0["channelsScrollBar (ChannelListLabel)"]
```

```{mermaid}
:caption: Characterlist

graph TD
    W0["buttonCancel (CharacterWidget)"]
```

```{mermaid}
:caption: Combo

graph TD
    W0["AttackComboBoxPopupMenu (AttackComboBoxPopupMenu)"]
    W1["AttackComboBoxPopupMenuButton (AttackComboBoxPopupMenuButton)"]
    W2["AttackComboBox (AttackComboBox)"]
    W3["FollowComboBoxPopupMenu (FollowComboBoxPopupMenu)"]
    W4["FollowComboBoxPopupMenuButton (FollowComboBoxPopupMenuButton)"]
    W5["FollowComboBox (FollowComboBox)"]
    W6["onCastToggle (ComboTrigger)"]
    W7["commandsToggle (ComboActions)"]
    W8["Triggers (BotServer)"]
    W9["toolsButton (ComboWindow)"]
```

```{mermaid}
:caption: Communicationwindow

graph TD
    W0["IgnoreListLabel (IgnoreListLabel)"]
    W1["whiteListScrollBar (WhiteListLabel)"]
```

```{mermaid}
:caption: Conditions

graph TD
    W0["UturaComboBoxPopupMenu (UturaComboBoxPopupMenu)"]
    W1["UturaComboBoxPopupMenuButton (UturaComboBoxPopupMenuButton)"]
    W2["UturaComboBox (UturaComboBox)"]
    W3["ParalyseSpell (CureConditions)"]
    W4["StopHaste (HoldConditions)"]
    W5["closeButton (ConditionsWindow)"]
```

```{mermaid}
:caption: Config

graph TD
    W0["remove (BotConfig)"]
```

```{mermaid}
:caption: Container

graph TD
    W0["scroll (BotContainer)"]
```

```{mermaid}
:caption: Cooldown

graph TD
    W0["SpellGroupIcon (SpellGroupIcon)"]
    W1["SpellIcon (SpellIcon)"]
    W2["SpellProgressRect (SpellProgressRect)"]
    W3["cooldownPanel (GroupCooldownParticles)"]
```

```{mermaid}
:caption: Countwindow

graph TD
    W0["buttonOk (CountWindow)"]
```

```{mermaid}
:caption: Creature Editor

graph TD
    W0["scroll (TargetBotCreatureEditorScrollBar)"]
    W1["textEdit (TargetBotCreatureEditorTextEdit)"]
    W2["item (TargetBotCreatureEditorItem)"]
    W3["TargetBotCreatureEditorCheckBox (TargetBotCreatureEditorCheckBox)"]
    W4["cancel (TargetBotCreatureEditorWindow)"]
```

```{mermaid}
:caption: Currentoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["myBuyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Deathwindow

graph TD
    W0["buttonCancel (DeathWindow)"]
```

```{mermaid}
:caption: Depositer Config

graph TD
    W0["slot (StashItem)"]
    W1["CloseButton (DepositerPanel)"]
```

```{mermaid}
:caption: Editor

graph TD
    W0["autoRecording (CaveBotEditorButton)"]
    W1["autoRecording (CaveBotEditorPanel)"]
```

```{mermaid}
:caption: Editvip

graph TD
    W0["buttonCancel (IconButton)"]
```

```{mermaid}
:caption: Equipper

graph TD
    W0["SlotBotItem (SlotBotItem)"]
    W1["remove (BossLabel)"]
    W2["ConditionBoxPopupMenu (ConditionBoxPopupMenu)"]
    W3["ConditionBoxPopupMenuButton (ConditionBoxPopupMenuButton)"]
    W4["ConditionBox (ConditionBox)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["text (CondidionLabel)"]
    W8["visible (Rule)"]
    W9["text (ConditionPanel)"]
    W10["down (ListPanel)"]
    W11["add (InputPanel)"]
    W12["default (EQPanel)"]
    W13["profileName (Profile)"]
    W14["add (BossList)"]
    W15["bossList (EquipWindow)"]
```

```{mermaid}
:caption: Extras

graph TD
    W0["scroll (ExtrasScrollBar)"]
    W1["textEdit (ExtrasTextEdit)"]
    W2["item (ExtrasItem)"]
    W3["ExtrasCheckBox (ExtrasCheckBox)"]
    W4["closeButton (ExtrasWindow)"]
```

```{mermaid}
:caption: Flagwindow

graph TD
    W0["FlagButton (FlagButton)"]
    W1["cancelButton (FlagWindow)"]
```

```{mermaid}
:caption: Flow

graph TD
    A[UI (OTUI)] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```

```{mermaid}
:caption: Gameinterface

graph TD
    W0["GameSidePanel (GameSidePanel)"]
    W1["GameMapPanel (GameMapPanel)"]
    W2["gameTopBar (GameAction)"]
```

```{mermaid}
:caption: Healbot

graph TD
    W0["SettingCheckBox (SettingCheckBox)"]
    W1["SpellSourceBoxPopupMenu (SpellSourceBoxPopupMenu)"]
    W2["SpellSourceBoxPopupMenuButton (SpellSourceBoxPopupMenuButton)"]
    W3["SpellSourceBox (SpellSourceBox)"]
    W4["SpellConditionBoxPopupMenu (SpellConditionBoxPopupMenu)"]
    W5["SpellConditionBoxPopupMenuButton (SpellConditionBoxPopupMenuButton)"]
    W6["SpellConditionBox (SpellConditionBox)"]
    W7["remove (SpellEntry)"]
    W8["remove (ItemEntry)"]
    W9["MoveDown (SpellHealing)"]
    W10["MoveDown (ItemHealing)"]
    W11["items (HealerPanel)"]
    W12["ResetSettings (HealBotSettingsPanel)"]
    W13["settingsButton (HealWindow)"]
```

```{mermaid}
:caption: Hotkeys Manager

graph TD
    W0["cancelButton (HotkeyListLabel)"]
    W1["cancelButton (HotkeyAssignWindow)"]
```

```{mermaid}
:caption: Icons

graph TD
    W0["text (BotIcon)"]
```

```{mermaid}
:caption: Imbuing

graph TD
    W0["Slot (Slot)"]
    W1["count (RequiredItem)"]
    W2["selectSlot (ItemInformation)"]
    W3["cost (EmptyImbue)"]
    W4["balance (ClearImbue)"]
```

```{mermaid}
:caption: Itemdetails

graph TD
    W0["DetailsTableRow (DetailsTableRow)"]
    W1["detailsTableScrollBar (DetailsTableColumn)"]
```

```{mermaid}
:caption: Itemoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["buyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Itemselector

graph TD
    W0["cancelButton (ItemSelectorWindow)"]
```

```{mermaid}
:caption: Itemstats

graph TD
    W0["StatsTableRow (StatsTableRow)"]
    W1["sellStatsTableScrollBar (StatsTableColumn)"]
```

```{mermaid}
:caption: Locales

graph TD
    W0["LocalesMainLabel (LocalesMainLabel)"]
    W1["localesPanel (LocalesButton)"]
```

```{mermaid}
:caption: Looting

graph TD
    W0["value (TargetBotLootingPanel)"]
```

```{mermaid}
:caption: Market

graph TD
    W0["resetButton (MarketWindow)"]
```

```{mermaid}
:caption: Marketbuttons

graph TD
    W0["MarketButtonBox (MarketButtonBox)"]
```

```{mermaid}
:caption: Marketcombobox

graph TD
    W0["MarketComboBoxPopupMenuButton (MarketComboBoxPopupMenuButton)"]
    W1["MarketComboBoxPopupMenuSeparator (MarketComboBoxPopupMenuSeparator)"]
    W2["MarketComboBoxPopupMenu (MarketComboBoxPopupMenu)"]
    W3["MarketComboBox (MarketComboBox)"]
```

```{mermaid}
:caption: Markettabs

graph TD
    W0["MarketTabBar (MarketTabBar)"]
    W1["MarketTabBarPanel (MarketTabBarPanel)"]
    W2["MarketTabBarButton (MarketTabBarButton)"]
    W3["MarketRightTabBar (MarketRightTabBar)"]
    W4["MarketRightTabBarPanel (MarketRightTabBarPanel)"]
    W5["MarketRightTabBarButton (MarketRightTabBarButton)"]
```

```{mermaid}
:caption: Modaldialog

graph TD
    W0["ChoiceListLabel (ChoiceListLabel)"]
    W1["choiceList (ChoiceList)"]
    W2["choiceScrollBar (ChoiceScrollBar)"]
    W3["ModalButton (ModalButton)"]
    W4["buttonsPanel (ModalDialog)"]
```

```{mermaid}
:caption: New Healer

graph TD
    W0["CategoryCheckBox (CategoryCheckBox)"]
    W1["scroll (HealScroll)"]
    W2["text (HealItem)"]
    W3["ToolTipLabel (ToolTipLabel)"]
    W4["remove (HealerPlayerEntry)"]
    W5["decrement (PriorityEntry)"]
    W3 --> W5
    W6["vocations (TargetSettings)"]
    W7["botserver (Groups)"]
    W8["sorcerers (Vocations)"]
    W9["list (Priority)"]
    W10["add (AddPlayer)"]
    W11["listScrollBar (PlayerList)"]
    W12["playerList (CustomList)"]
    W13["box (Conditions)"]
    W14["closeButton (FriendHealer)"]
```

```{mermaid}
:caption: Npctrade

graph TD
    W0["NPCOfferLabel (NPCOfferLabel)"]
    W1["tradeButton (NPCItemBox)"]
```

```{mermaid}
:caption: Object

graph TD
    W0["buttonOk (RoundCheckBox)"]
```

```{mermaid}
:caption: Options

graph TD
    W0["OptionCheckBox (OptionCheckBox)"]
    W1["OptionScrollbar (OptionScrollbar)"]
    W2["optionsTabContent (OptionPanel)"]
```

```{mermaid}
:caption: Outfitwindow

graph TD
    W0["FloorTile (FloorTile)"]
```

```{mermaid}
:caption: Panels

graph TD
    W0["text (DualScrollPanel)"]
    W1["scroll (SingleScrollItemPanel)"]
    W2["scroll2 (DualScrollItemPanel)"]
    W3["item5 (ItemsRow)"]
    W4["items (ItemsPanel)"]
    W5["title (ItemAndButtonPanel)"]
    W6["slot (ItemAndSlotPanel)"]
    W7["slot (TwoItemsAndSlotPanel)"]
    W8["right (DualLabelPanel)"]
    W9["right (LabelAndTextEditPanel)"]
    W10["left (SwitchAndButtonPanel)"]
```

```{mermaid}
:caption: Playerlist

graph TD
    W0["remove (PlayerLabel)"]
    W1["SettingCheckBox (SettingCheckBox)"]
    W2["AutoAdd (Settings)"]
    W3["add (tPanel)"]
    W4["closeButton (PlayerListWindow)"]
```

```{mermaid}
:caption: Prey

graph TD
    W0["shopTempButton (LockedPreyPanel)"]
    W1["Star (Star)"]
    W2["NoStar (NoStar)"]
    W3["noBonusIcon (NoCreaturePanel)"]
    W4["lockPreyPrice (ActivePreyPanel)"]
    W5["timeLeft (CreatureAndBonus)"]
    W6["price (BonusReroll)"]
    W7["list (InactivePreyPanel)"]
    W8["choosePreyButton (ChoosePrey)"]
    W9["price (SelectPreyCreature)"]
    W10["price (RerollButton)"]
    W11["text (CardLabel)"]
    W12["text (GoldLabel)"]
    W13["creature (PreyCreatureBox)"]
    W14["openStore (SlotPanel)"]
    W15["time (PreyCreature)"]
    W16["slot3 (PreyTracker)"]
```

```{mermaid}
:caption: Pushmax

graph TD
    W0["closeButton (PushMaxWindow)"]
```

```{mermaid}
:caption: Questlogwindow

graph TD
    W0["description (QuestTrackerLabel)"]
    W1["QuestLabel (QuestLabel)"]
    W2["questListScrollBar (QuestLog)"]
    W3["missionDescription (MissionLog)"]
    W4["trackerButton (QuestLogWindow)"]
    W5["list (QuestTracker)"]
```

```{mermaid}
:caption: Ruleviolation

graph TD
    W0["RVListLabel (RVListLabel)"]
    W1["RVLabel (RVLabel)"]
    W2["commentText (RVTextEdit)"]
```

```{mermaid}
:caption: Shop

graph TD
    W0["name (ShopCategory)"]
    W1["item (ShopCategoryItem)"]
    W0 --> W1
    W2["creature (ShopCategoryCreature)"]
    W0 --> W2
    W3["image (ShopCategoryImage)"]
    W0 --> W3
    W4["buyButton (ShopOffer)"]
    W5["item (ShopOfferItem)"]
    W4 --> W5
    W6["creature (ShopOfferCreature)"]
    W4 --> W6
    W7["buttonCancel (ShopOfferImage)"]
    W4 --> W7
```

```{mermaid}
:caption: Sideactionbar

graph TD
    W0["cooldown (SideActionButton)"]
    W1["image (TopSliders)"]
    W2["nextPanel (BottomSliders)"]
```

```{mermaid}
:caption: Siolist

graph TD
    W0["RP (VocationPanel)"]
    W1["closeButton (SioListWindow)"]
```

```{mermaid}
:caption: Skills

graph TD
    W0["SkillFirstWidget (SkillFirstWidget)"]
    W1["SkillButton (SkillButton)"]
    W2["SmallSkillButton (SmallSkillButton)"]
    W1 --> W2
    W3["SkillNameLabel (SkillNameLabel)"]
    W4["value (SkillValueLabel)"]
    W5["skillId12 (SkillPercentPanel)"]
```

```{mermaid}
:caption: Spell

graph TD
    W0["buttonOk (SpellPreview)"]
```

```{mermaid}
:caption: Spelllist

graph TD
    W0["SpellListLabel (SpellListLabel)"]
    W1["SpellInfoLabel (SpellInfoLabel)"]
    W2["SpellInfoValueLabel (SpellInfoValueLabel)"]
    W3["premiumBoxYes (FilterButton)"]
```

```{mermaid}
:caption: Stats

graph TD
    W0["DebugText (DebugText)"]
    W1["debugScroll (DebugLabel)"]
```

```{mermaid}
:caption: Supplies

graph TD
    W0["remove (ProfileLabel)"]
    W1["SupplySpinBox (SupplySpinBox)"]
    W2["avg (ItemPanel)"]
    W3["decrement (SuppliesWindow)"]
```

```{mermaid}
:caption: Supply

graph TD
    W0["max (SupplyItem)"]
    W1["scroll (SupplyItemList)"]
```

```{mermaid}
:caption: Target

graph TD
    W0["TargetBotEntry (TargetBotEntry)"]
    W1["right (TargetBotDualLabel)"]
    W2["debug (TargetBotPanel)"]
```

```{mermaid}
:caption: Terminal

graph TD
    W0["TerminalLabel (TerminalLabel)"]
    W1["rightResizeBorder (TerminalSelectText)"]
```

```{mermaid}
:caption: Textedit

graph TD
    W0["cancel (TextEditButtons)"]
    W1["examples (TextEditWindow)"]
    W2["text (SinglelineTextEditWindow)"]
    W1 --> W2
    W3["textScroll (MultilineTextEditWindow)"]
    W1 --> W3
```

```{mermaid}
:caption: Textmessage

graph TD
    W0["statusLabel (TextMessageLabel)"]
```

```{mermaid}
:caption: Textwindow

graph TD
    W0["cancelButton (TextWindow)"]
```

```{mermaid}
:caption: Topbar

graph TD
    W0["box (StatsPanel)"]
    W1["skills (SkillPanel)"]
```

```{mermaid}
:caption: Tradewindow

graph TD
    W0["rejectButton (TradeWindow)"]
```

```{mermaid}
:caption: Unjustifiedpoints

graph TD
    W0["SkullProgressBar (SkullProgressBar)"]
    W1["monthSkullWidget (SkullWidget)"]
```

```{mermaid}
:caption: Viplist

graph TD
    W0["vipWindow (VipListLabel)"]
```


## Diagrams

```{mermaid}
:caption: Actionbar

graph TD
    W0["cooldown (ActionButton)"]
    W1["image (LeftSliders)"]
    W2["nextPanel (RightSliders)"]
```

```{mermaid}
:caption: Alarms

graph TD
    W0["tick (AlarmCheckBox)"]
    W1["value (AlarmCheckBoxAndSpinBox)"]
    W2["text (AlarmCheckBoxAndTextEdit)"]
    W3["closeButton (AlarmsWindow)"]
```

```{mermaid}
:caption: Amountwindow

graph TD
    W0["buttonOk (AmountWindow)"]
```

```{mermaid}
:caption: Analyzer

graph TD
    W0["cooldown (BossCreaturePanel)"]
    W1["clear (SearchPanel)"]
    W2["drops (TrackerItem)"]
    W3["value (DualLabel)"]
    W4["healing (MemberWidget)"]
    W5["remove (AnalyzerPriceLabel)"]
    W6["AnalyzerListPanel (AnalyzerListPanel)"]
    W7["ListLabel (ListLabel)"]
    W8["List (AnalyzerItemsPanel)"]
    W9["count (AnalyzerLootItem)"]
    W10["AnalyzerGraph (AnalyzerGraph)"]
    W11["AnalyzerProgressBar (AnalyzerProgressBar)"]
    W12["AnalyzerButton (AnalyzerButton)"]
    W13["ResetSession (MainAnalyzerWindow)"]
    W14["HuntingAnalyzerWindow (HuntingAnalyzer)"]
    W15["LootAnalyzerWindow (LootAnalyzer)"]
    W16["SupplyAnalyzerWindow (SupplyAnalyzer)"]
    W17["ImpactAnalyzerWindow (ImpactAnalyzer)"]
    W18["XPAnalyzerWindow (XPAnalyzer)"]
    W19["PartyAnalyzerWindow (PartyAnalyzerWindow)"]
    W20["DropTracker (DropTracker)"]
    W21["CaveBotStats (CaveBotStats)"]
    W22["search (BossTracker)"]
    W23["closeButton (FeaturesWindow)"]
```

```{mermaid}
:caption: Architecture

graph LR
    subgraph UI (OTUI)
        E0[Widgets]
        E1[UI Components]
        E2[Layouts]
        E0 --> E1
        E1 --> E2
    end
```

```{mermaid}
:caption: Attackbot

graph TD
    W0["remove (AttackEntry)"]
    W1["name (AttackBotBotPanel)"]
    W2["description (CategoryLabel)"]
    W3["description (SourceLabel)"]
    W4["description (RangeLabel)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["spellName (AttackBotPanel)"]
    W8["AntiRsRange (SettingsPanel)"]
    W9["settings (AttackBotWindow)"]
```

```{mermaid}
:caption: Basic

graph TD
    W0["BotButton (BotButton)"]
    W1["BotSwitch (BotSwitch)"]
    W2["SmallBotSwitch (SmallBotSwitch)"]
    W3["BotLabel (BotLabel)"]
    W4["BotItem (BotItem)"]
    W5["BotTextEdit (BotTextEdit)"]
    W6["BotSeparator (BotSeparator)"]
    W7["botPanelScroll (BotSmallScrollBar)"]
    W8["botPanelScroll (BotPanel)"]
    W9["CaveBotLabel (CaveBotLabel)"]
    W10["SlotComboBoxPopupMenu (SlotComboBoxPopupMenu)"]
    W11["SlotComboBoxPopupMenuButton (SlotComboBoxPopupMenuButton)"]
    W12["SlotComboBox (SlotComboBox)"]
```

```{mermaid}
:caption: Battle

graph TD
    W0["BattleIcon (BattleIcon)"]
    W1["BattlePlayers (BattlePlayers)"]
    W0 --> W1
    W2["BattleNPCs (BattleNPCs)"]
    W0 --> W2
    W3["BattleMonsters (BattleMonsters)"]
    W0 --> W3
    W4["BattleSkulls (BattleSkulls)"]
    W0 --> W4
    W5["battlePanel (BattleParty)"]
    W0 --> W5
```

```{mermaid}
:caption: Battlebutton

graph TD
    W0["BattleButton (BattleButton)"]
```

```{mermaid}
:caption: Bot

graph TD
    W0["BotTabBar (BotTabBar)"]
    W1["botPanel (BotTabBarPanel)"]
    W2["botPanel (BotTabBarButton)"]
```

```{mermaid}
:caption: Botserver

graph TD
    W0["Members (BotServerData)"]
    W1["Broadcast (FeaturePanel)"]
    W2["enabled (BotServerWindow)"]
```

```{mermaid}
:caption: Browse

graph TD
    W0["filterSearchAll (MarketItemBox)"]
```

```{mermaid}
:caption: Bugreport

graph TD
    W0["cancelButton (BugReportWindow)"]
```

```{mermaid}
:caption: Cavebot

graph TD
    W0["CaveBotAction (CaveBotAction)"]
    W1["showConfig (CaveBotPanel)"]
```

```{mermaid}
:caption: Channelswindow

graph TD
    W0["channelsScrollBar (ChannelListLabel)"]
```

```{mermaid}
:caption: Characterlist

graph TD
    W0["buttonCancel (CharacterWidget)"]
```

```{mermaid}
:caption: Combo

graph TD
    W0["AttackComboBoxPopupMenu (AttackComboBoxPopupMenu)"]
    W1["AttackComboBoxPopupMenuButton (AttackComboBoxPopupMenuButton)"]
    W2["AttackComboBox (AttackComboBox)"]
    W3["FollowComboBoxPopupMenu (FollowComboBoxPopupMenu)"]
    W4["FollowComboBoxPopupMenuButton (FollowComboBoxPopupMenuButton)"]
    W5["FollowComboBox (FollowComboBox)"]
    W6["onCastToggle (ComboTrigger)"]
    W7["commandsToggle (ComboActions)"]
    W8["Triggers (BotServer)"]
    W9["toolsButton (ComboWindow)"]
```

```{mermaid}
:caption: Communicationwindow

graph TD
    W0["IgnoreListLabel (IgnoreListLabel)"]
    W1["whiteListScrollBar (WhiteListLabel)"]
```

```{mermaid}
:caption: Conditions

graph TD
    W0["UturaComboBoxPopupMenu (UturaComboBoxPopupMenu)"]
    W1["UturaComboBoxPopupMenuButton (UturaComboBoxPopupMenuButton)"]
    W2["UturaComboBox (UturaComboBox)"]
    W3["ParalyseSpell (CureConditions)"]
    W4["StopHaste (HoldConditions)"]
    W5["closeButton (ConditionsWindow)"]
```

```{mermaid}
:caption: Config

graph TD
    W0["remove (BotConfig)"]
```

```{mermaid}
:caption: Container

graph TD
    W0["scroll (BotContainer)"]
```

```{mermaid}
:caption: Cooldown

graph TD
    W0["SpellGroupIcon (SpellGroupIcon)"]
    W1["SpellIcon (SpellIcon)"]
    W2["SpellProgressRect (SpellProgressRect)"]
    W3["cooldownPanel (GroupCooldownParticles)"]
```

```{mermaid}
:caption: Countwindow

graph TD
    W0["buttonOk (CountWindow)"]
```

```{mermaid}
:caption: Creature Editor

graph TD
    W0["scroll (TargetBotCreatureEditorScrollBar)"]
    W1["textEdit (TargetBotCreatureEditorTextEdit)"]
    W2["item (TargetBotCreatureEditorItem)"]
    W3["TargetBotCreatureEditorCheckBox (TargetBotCreatureEditorCheckBox)"]
    W4["cancel (TargetBotCreatureEditorWindow)"]
```

```{mermaid}
:caption: Currentoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["myBuyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Deathwindow

graph TD
    W0["buttonCancel (DeathWindow)"]
```

```{mermaid}
:caption: Depositer Config

graph TD
    W0["slot (StashItem)"]
    W1["CloseButton (DepositerPanel)"]
```

```{mermaid}
:caption: Editor

graph TD
    W0["autoRecording (CaveBotEditorButton)"]
    W1["autoRecording (CaveBotEditorPanel)"]
```

```{mermaid}
:caption: Editvip

graph TD
    W0["buttonCancel (IconButton)"]
```

```{mermaid}
:caption: Equipper

graph TD
    W0["SlotBotItem (SlotBotItem)"]
    W1["remove (BossLabel)"]
    W2["ConditionBoxPopupMenu (ConditionBoxPopupMenu)"]
    W3["ConditionBoxPopupMenuButton (ConditionBoxPopupMenuButton)"]
    W4["ConditionBox (ConditionBox)"]
    W5["PreButton (PreButton)"]
    W6["NexButton (NexButton)"]
    W7["text (CondidionLabel)"]
    W8["visible (Rule)"]
    W9["text (ConditionPanel)"]
    W10["down (ListPanel)"]
    W11["add (InputPanel)"]
    W12["default (EQPanel)"]
    W13["profileName (Profile)"]
    W14["add (BossList)"]
    W15["bossList (EquipWindow)"]
```

```{mermaid}
:caption: Extras

graph TD
    W0["scroll (ExtrasScrollBar)"]
    W1["textEdit (ExtrasTextEdit)"]
    W2["item (ExtrasItem)"]
    W3["ExtrasCheckBox (ExtrasCheckBox)"]
    W4["closeButton (ExtrasWindow)"]
```

```{mermaid}
:caption: Flagwindow

graph TD
    W0["FlagButton (FlagButton)"]
    W1["cancelButton (FlagWindow)"]
```

```{mermaid}
:caption: Flow

graph TD
    A[UI (OTUI)] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
```

```{mermaid}
:caption: Gameinterface

graph TD
    W0["GameSidePanel (GameSidePanel)"]
    W1["GameMapPanel (GameMapPanel)"]
    W2["gameTopBar (GameAction)"]
```

```{mermaid}
:caption: Healbot

graph TD
    W0["SettingCheckBox (SettingCheckBox)"]
    W1["SpellSourceBoxPopupMenu (SpellSourceBoxPopupMenu)"]
    W2["SpellSourceBoxPopupMenuButton (SpellSourceBoxPopupMenuButton)"]
    W3["SpellSourceBox (SpellSourceBox)"]
    W4["SpellConditionBoxPopupMenu (SpellConditionBoxPopupMenu)"]
    W5["SpellConditionBoxPopupMenuButton (SpellConditionBoxPopupMenuButton)"]
    W6["SpellConditionBox (SpellConditionBox)"]
    W7["remove (SpellEntry)"]
    W8["remove (ItemEntry)"]
    W9["MoveDown (SpellHealing)"]
    W10["MoveDown (ItemHealing)"]
    W11["items (HealerPanel)"]
    W12["ResetSettings (HealBotSettingsPanel)"]
    W13["settingsButton (HealWindow)"]
```

```{mermaid}
:caption: Hotkeys Manager

graph TD
    W0["cancelButton (HotkeyListLabel)"]
    W1["cancelButton (HotkeyAssignWindow)"]
```

```{mermaid}
:caption: Icons

graph TD
    W0["text (BotIcon)"]
```

```{mermaid}
:caption: Imbuing

graph TD
    W0["Slot (Slot)"]
    W1["count (RequiredItem)"]
    W2["selectSlot (ItemInformation)"]
    W3["cost (EmptyImbue)"]
    W4["balance (ClearImbue)"]
```

```{mermaid}
:caption: Itemdetails

graph TD
    W0["DetailsTableRow (DetailsTableRow)"]
    W1["detailsTableScrollBar (DetailsTableColumn)"]
```

```{mermaid}
:caption: Itemoffers

graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["buyingTableScrollBar (OfferTableHeaderColumn)"]
```

```{mermaid}
:caption: Itemselector

graph TD
    W0["cancelButton (ItemSelectorWindow)"]
```

```{mermaid}
:caption: Itemstats

graph TD
    W0["StatsTableRow (StatsTableRow)"]
    W1["sellStatsTableScrollBar (StatsTableColumn)"]
```

```{mermaid}
:caption: Locales

graph TD
    W0["LocalesMainLabel (LocalesMainLabel)"]
    W1["localesPanel (LocalesButton)"]
```

```{mermaid}
:caption: Looting

graph TD
    W0["value (TargetBotLootingPanel)"]
```

```{mermaid}
:caption: Market

graph TD
    W0["resetButton (MarketWindow)"]
```

```{mermaid}
:caption: Marketbuttons

graph TD
    W0["MarketButtonBox (MarketButtonBox)"]
```

```{mermaid}
:caption: Marketcombobox

graph TD
    W0["MarketComboBoxPopupMenuButton (MarketComboBoxPopupMenuButton)"]
    W1["MarketComboBoxPopupMenuSeparator (MarketComboBoxPopupMenuSeparator)"]
    W2["MarketComboBoxPopupMenu (MarketComboBoxPopupMenu)"]
    W3["MarketComboBox (MarketComboBox)"]
```

```{mermaid}
:caption: Markettabs

graph TD
    W0["MarketTabBar (MarketTabBar)"]
    W1["MarketTabBarPanel (MarketTabBarPanel)"]
    W2["MarketTabBarButton (MarketTabBarButton)"]
    W3["MarketRightTabBar (MarketRightTabBar)"]
    W4["MarketRightTabBarPanel (MarketRightTabBarPanel)"]
    W5["MarketRightTabBarButton (MarketRightTabBarButton)"]
```

```{mermaid}
:caption: Modaldialog

graph TD
    W0["ChoiceListLabel (ChoiceListLabel)"]
    W1["choiceList (ChoiceList)"]
    W2["choiceScrollBar (ChoiceScrollBar)"]
    W3["ModalButton (ModalButton)"]
    W4["buttonsPanel (ModalDialog)"]
```

```{mermaid}
:caption: New Healer

graph TD
    W0["CategoryCheckBox (CategoryCheckBox)"]
    W1["scroll (HealScroll)"]
    W2["text (HealItem)"]
    W3["ToolTipLabel (ToolTipLabel)"]
    W4["remove (HealerPlayerEntry)"]
    W5["decrement (PriorityEntry)"]
    W3 --> W5
    W6["vocations (TargetSettings)"]
    W7["botserver (Groups)"]
    W8["sorcerers (Vocations)"]
    W9["list (Priority)"]
    W10["add (AddPlayer)"]
    W11["listScrollBar (PlayerList)"]
    W12["playerList (CustomList)"]
    W13["box (Conditions)"]
    W14["closeButton (FriendHealer)"]
```

```{mermaid}
:caption: Npctrade

graph TD
    W0["NPCOfferLabel (NPCOfferLabel)"]
    W1["tradeButton (NPCItemBox)"]
```

```{mermaid}
:caption: Object

graph TD
    W0["buttonOk (RoundCheckBox)"]
```

```{mermaid}
:caption: Options

graph TD
    W0["OptionCheckBox (OptionCheckBox)"]
    W1["OptionScrollbar (OptionScrollbar)"]
    W2["optionsTabContent (OptionPanel)"]
```

```{mermaid}
:caption: Outfitwindow

graph TD
    W0["FloorTile (FloorTile)"]
```

```{mermaid}
:caption: Panels

graph TD
    W0["text (DualScrollPanel)"]
    W1["scroll (SingleScrollItemPanel)"]
    W2["scroll2 (DualScrollItemPanel)"]
    W3["item5 (ItemsRow)"]
    W4["items (ItemsPanel)"]
    W5["title (ItemAndButtonPanel)"]
    W6["slot (ItemAndSlotPanel)"]
    W7["slot (TwoItemsAndSlotPanel)"]
    W8["right (DualLabelPanel)"]
    W9["right (LabelAndTextEditPanel)"]
    W10["left (SwitchAndButtonPanel)"]
```

```{mermaid}
:caption: Playerlist

graph TD
    W0["remove (PlayerLabel)"]
    W1["SettingCheckBox (SettingCheckBox)"]
    W2["AutoAdd (Settings)"]
    W3["add (tPanel)"]
    W4["closeButton (PlayerListWindow)"]
```

```{mermaid}
:caption: Prey

graph TD
    W0["shopTempButton (LockedPreyPanel)"]
    W1["Star (Star)"]
    W2["NoStar (NoStar)"]
    W3["noBonusIcon (NoCreaturePanel)"]
    W4["lockPreyPrice (ActivePreyPanel)"]
    W5["timeLeft (CreatureAndBonus)"]
    W6["price (BonusReroll)"]
    W7["list (InactivePreyPanel)"]
    W8["choosePreyButton (ChoosePrey)"]
    W9["price (SelectPreyCreature)"]
    W10["price (RerollButton)"]
    W11["text (CardLabel)"]
    W12["text (GoldLabel)"]
    W13["creature (PreyCreatureBox)"]
    W14["openStore (SlotPanel)"]
    W15["time (PreyCreature)"]
    W16["slot3 (PreyTracker)"]
```

```{mermaid}
:caption: Pushmax

graph TD
    W0["closeButton (PushMaxWindow)"]
```

```{mermaid}
:caption: Questlogwindow

graph TD
    W0["description (QuestTrackerLabel)"]
    W1["QuestLabel (QuestLabel)"]
    W2["questListScrollBar (QuestLog)"]
    W3["missionDescription (MissionLog)"]
    W4["trackerButton (QuestLogWindow)"]
    W5["list (QuestTracker)"]
```

```{mermaid}
:caption: Ruleviolation

graph TD
    W0["RVListLabel (RVListLabel)"]
    W1["RVLabel (RVLabel)"]
    W2["commentText (RVTextEdit)"]
```

```{mermaid}
:caption: Shop

graph TD
    W0["name (ShopCategory)"]
    W1["item (ShopCategoryItem)"]
    W0 --> W1
    W2["creature (ShopCategoryCreature)"]
    W0 --> W2
    W3["image (ShopCategoryImage)"]
    W0 --> W3
    W4["buyButton (ShopOffer)"]
    W5["item (ShopOfferItem)"]
    W4 --> W5
    W6["creature (ShopOfferCreature)"]
    W4 --> W6
    W7["buttonCancel (ShopOfferImage)"]
    W4 --> W7
```

```{mermaid}
:caption: Sideactionbar

graph TD
    W0["cooldown (SideActionButton)"]
    W1["image (TopSliders)"]
    W2["nextPanel (BottomSliders)"]
```

```{mermaid}
:caption: Siolist

graph TD
    W0["RP (VocationPanel)"]
    W1["closeButton (SioListWindow)"]
```

```{mermaid}
:caption: Skills

graph TD
    W0["SkillFirstWidget (SkillFirstWidget)"]
    W1["SkillButton (SkillButton)"]
    W2["SmallSkillButton (SmallSkillButton)"]
    W1 --> W2
    W3["SkillNameLabel (SkillNameLabel)"]
    W4["value (SkillValueLabel)"]
    W5["skillId12 (SkillPercentPanel)"]
```

```{mermaid}
:caption: Spell

graph TD
    W0["buttonOk (SpellPreview)"]
```

```{mermaid}
:caption: Spelllist

graph TD
    W0["SpellListLabel (SpellListLabel)"]
    W1["SpellInfoLabel (SpellInfoLabel)"]
    W2["SpellInfoValueLabel (SpellInfoValueLabel)"]
    W3["premiumBoxYes (FilterButton)"]
```

```{mermaid}
:caption: Stats

graph TD
    W0["DebugText (DebugText)"]
    W1["debugScroll (DebugLabel)"]
```

```{mermaid}
:caption: Supplies

graph TD
    W0["remove (ProfileLabel)"]
    W1["SupplySpinBox (SupplySpinBox)"]
    W2["avg (ItemPanel)"]
    W3["decrement (SuppliesWindow)"]
```

```{mermaid}
:caption: Supply

graph TD
    W0["max (SupplyItem)"]
    W1["scroll (SupplyItemList)"]
```

```{mermaid}
:caption: Target

graph TD
    W0["TargetBotEntry (TargetBotEntry)"]
    W1["right (TargetBotDualLabel)"]
    W2["debug (TargetBotPanel)"]
```

```{mermaid}
:caption: Terminal

graph TD
    W0["TerminalLabel (TerminalLabel)"]
    W1["rightResizeBorder (TerminalSelectText)"]
```

```{mermaid}
:caption: Textedit

graph TD
    W0["cancel (TextEditButtons)"]
    W1["examples (TextEditWindow)"]
    W2["text (SinglelineTextEditWindow)"]
    W1 --> W2
    W3["textScroll (MultilineTextEditWindow)"]
    W1 --> W3
```

```{mermaid}
:caption: Textmessage

graph TD
    W0["statusLabel (TextMessageLabel)"]
```

```{mermaid}
:caption: Textwindow

graph TD
    W0["cancelButton (TextWindow)"]
```

```{mermaid}
:caption: Topbar

graph TD
    W0["box (StatsPanel)"]
    W1["skills (SkillPanel)"]
```

```{mermaid}
:caption: Tradewindow

graph TD
    W0["rejectButton (TradeWindow)"]
```

```{mermaid}
:caption: Unjustifiedpoints

graph TD
    W0["SkullProgressBar (SkullProgressBar)"]
    W1["monthSkullWidget (SkullWidget)"]
```

```{mermaid}
:caption: Viplist

graph TD
    W0["vipWindow (VipListLabel)"]
```
