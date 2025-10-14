---
title: 04_ui - Ui
---

# 04_ui - Ui

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`04_ui.entities`](#facet-04_ui.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`04_ui.summary`](#facet-04_ui.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::{grid-item}

#### `ui_widgets.csv`
*Facet:* [`04_ui.ui_widgets`](#facet-04_ui.ui_widgets)

```{csv-table} ui_widgets
:header-rows: 1
:file: ./datasets/ui_widgets.csv
:widths: auto
```

:::

:::

## Diagrams
#### `AttackBot.mmd`
        *Facet:* [`04_ui.AttackBot`](#facet-04_ui.AttackBot)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `BotServer.mmd`
        *Facet:* [`04_ui.BotServer`](#facet-04_ui.BotServer)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["Members (BotServerData)"]
    W1["Broadcast (FeaturePanel)"]
    W2["enabled (BotServerWindow)"]
        ```

#### `Conditions.mmd`
        *Facet:* [`04_ui.Conditions`](#facet-04_ui.Conditions)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["UturaComboBoxPopupMenu (UturaComboBoxPopupMenu)"]
    W1["UturaComboBoxPopupMenuButton (UturaComboBoxPopupMenuButton)"]
    W2["UturaComboBox (UturaComboBox)"]
    W3["ParalyseSpell (CureConditions)"]
    W4["StopHaste (HoldConditions)"]
    W5["closeButton (ConditionsWindow)"]
        ```

#### `HealBot.mmd`
        *Facet:* [`04_ui.HealBot`](#facet-04_ui.HealBot)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `actionbar.mmd`
        *Facet:* [`04_ui.actionbar`](#facet-04_ui.actionbar)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cooldown (ActionButton)"]
    W1["image (LeftSliders)"]
    W2["nextPanel (RightSliders)"]
        ```

#### `alarms.mmd`
        *Facet:* [`04_ui.alarms`](#facet-04_ui.alarms)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["tick (AlarmCheckBox)"]
    W1["value (AlarmCheckBoxAndSpinBox)"]
    W2["text (AlarmCheckBoxAndTextEdit)"]
    W3["closeButton (AlarmsWindow)"]
        ```

#### `amountwindow.mmd`
        *Facet:* [`04_ui.amountwindow`](#facet-04_ui.amountwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (AmountWindow)"]
        ```

#### `analyzer.mmd`
        *Facet:* [`04_ui.analyzer`](#facet-04_ui.analyzer)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `architecture.mmd`
        *Facet:* [`04_ui.architecture`](#facet-04_ui.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph UI (OTUI)
        E0[Widgets]
        E1[UI Components]
        E2[Layouts]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `basic.mmd`
        *Facet:* [`04_ui.basic`](#facet-04_ui.basic)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `battle.mmd`
        *Facet:* [`04_ui.battle`](#facet-04_ui.battle)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `battlebutton.mmd`
        *Facet:* [`04_ui.battlebutton`](#facet-04_ui.battlebutton)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["BattleButton (BattleButton)"]
        ```

#### `bot.mmd`
        *Facet:* [`04_ui.bot`](#facet-04_ui.bot)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["BotTabBar (BotTabBar)"]
    W1["botPanel (BotTabBarPanel)"]
    W2["botPanel (BotTabBarButton)"]
        ```

#### `browse.mmd`
        *Facet:* [`04_ui.browse`](#facet-04_ui.browse)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["filterSearchAll (MarketItemBox)"]
        ```

#### `bugreport.mmd`
        *Facet:* [`04_ui.bugreport`](#facet-04_ui.bugreport)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (BugReportWindow)"]
        ```

#### `cavebot.mmd`
        *Facet:* [`04_ui.cavebot`](#facet-04_ui.cavebot)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["CaveBotAction (CaveBotAction)"]
    W1["showConfig (CaveBotPanel)"]
        ```

#### `channelswindow.mmd`
        *Facet:* [`04_ui.channelswindow`](#facet-04_ui.channelswindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["channelsScrollBar (ChannelListLabel)"]
        ```

#### `characterlist.mmd`
        *Facet:* [`04_ui.characterlist`](#facet-04_ui.characterlist)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (CharacterWidget)"]
        ```

#### `combo.mmd`
        *Facet:* [`04_ui.combo`](#facet-04_ui.combo)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `communicationwindow.mmd`
        *Facet:* [`04_ui.communicationwindow`](#facet-04_ui.communicationwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["IgnoreListLabel (IgnoreListLabel)"]
    W1["whiteListScrollBar (WhiteListLabel)"]
        ```

#### `config.mmd`
        *Facet:* [`04_ui.config`](#facet-04_ui.config)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (BotConfig)"]
        ```

#### `container.mmd`
        *Facet:* [`04_ui.container`](#facet-04_ui.container)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (BotContainer)"]
        ```

#### `cooldown.mmd`
        *Facet:* [`04_ui.cooldown`](#facet-04_ui.cooldown)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SpellGroupIcon (SpellGroupIcon)"]
    W1["SpellIcon (SpellIcon)"]
    W2["SpellProgressRect (SpellProgressRect)"]
    W3["cooldownPanel (GroupCooldownParticles)"]
        ```

#### `countwindow.mmd`
        *Facet:* [`04_ui.countwindow`](#facet-04_ui.countwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (CountWindow)"]
        ```

#### `creature_editor.mmd`
        *Facet:* [`04_ui.creature_editor`](#facet-04_ui.creature_editor)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (TargetBotCreatureEditorScrollBar)"]
    W1["textEdit (TargetBotCreatureEditorTextEdit)"]
    W2["item (TargetBotCreatureEditorItem)"]
    W3["TargetBotCreatureEditorCheckBox (TargetBotCreatureEditorCheckBox)"]
    W4["cancel (TargetBotCreatureEditorWindow)"]
        ```

#### `currentoffers.mmd`
        *Facet:* [`04_ui.currentoffers`](#facet-04_ui.currentoffers)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["myBuyingTableScrollBar (OfferTableHeaderColumn)"]
        ```

#### `deathwindow.mmd`
        *Facet:* [`04_ui.deathwindow`](#facet-04_ui.deathwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (DeathWindow)"]
        ```

#### `depositer_config.mmd`
        *Facet:* [`04_ui.depositer_config`](#facet-04_ui.depositer_config)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["slot (StashItem)"]
    W1["CloseButton (DepositerPanel)"]
        ```

#### `editor.mmd`
        *Facet:* [`04_ui.editor`](#facet-04_ui.editor)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["autoRecording (CaveBotEditorButton)"]
    W1["autoRecording (CaveBotEditorPanel)"]
        ```

#### `editvip.mmd`
        *Facet:* [`04_ui.editvip`](#facet-04_ui.editvip)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (IconButton)"]
        ```

#### `equipper.mmd`
        *Facet:* [`04_ui.equipper`](#facet-04_ui.equipper)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `extras.mmd`
        *Facet:* [`04_ui.extras`](#facet-04_ui.extras)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (ExtrasScrollBar)"]
    W1["textEdit (ExtrasTextEdit)"]
    W2["item (ExtrasItem)"]
    W3["ExtrasCheckBox (ExtrasCheckBox)"]
    W4["closeButton (ExtrasWindow)"]
        ```

#### `flagwindow.mmd`
        *Facet:* [`04_ui.flagwindow`](#facet-04_ui.flagwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["FlagButton (FlagButton)"]
    W1["cancelButton (FlagWindow)"]
        ```

#### `flow.mmd`
        *Facet:* [`04_ui.flow`](#facet-04_ui.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `gameinterface.mmd`
        *Facet:* [`04_ui.gameinterface`](#facet-04_ui.gameinterface)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["GameSidePanel (GameSidePanel)"]
    W1["GameMapPanel (GameMapPanel)"]
    W2["gameTopBar (GameAction)"]
        ```

#### `hotkeys_manager.mmd`
        *Facet:* [`04_ui.hotkeys_manager`](#facet-04_ui.hotkeys_manager)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (HotkeyListLabel)"]
    W1["cancelButton (HotkeyAssignWindow)"]
        ```

#### `icons.mmd`
        *Facet:* [`04_ui.icons`](#facet-04_ui.icons)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["text (BotIcon)"]
        ```

#### `imbuing.mmd`
        *Facet:* [`04_ui.imbuing`](#facet-04_ui.imbuing)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["Slot (Slot)"]
    W1["count (RequiredItem)"]
    W2["selectSlot (ItemInformation)"]
    W3["cost (EmptyImbue)"]
    W4["balance (ClearImbue)"]
        ```

#### `itemdetails.mmd`
        *Facet:* [`04_ui.itemdetails`](#facet-04_ui.itemdetails)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["DetailsTableRow (DetailsTableRow)"]
    W1["detailsTableScrollBar (DetailsTableColumn)"]
        ```

#### `itemoffers.mmd`
        *Facet:* [`04_ui.itemoffers`](#facet-04_ui.itemoffers)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["OfferTableRow (OfferTableRow)"]
    W1["OfferTableColumn (OfferTableColumn)"]
    W2["OfferTableWarningColumn (OfferTableWarningColumn)"]
    W1 --> W2
    W3["OfferTableHeaderRow (OfferTableHeaderRow)"]
    W4["buyingTableScrollBar (OfferTableHeaderColumn)"]
        ```

#### `itemselector.mmd`
        *Facet:* [`04_ui.itemselector`](#facet-04_ui.itemselector)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (ItemSelectorWindow)"]
        ```

#### `itemstats.mmd`
        *Facet:* [`04_ui.itemstats`](#facet-04_ui.itemstats)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["StatsTableRow (StatsTableRow)"]
    W1["sellStatsTableScrollBar (StatsTableColumn)"]
        ```

#### `locales.mmd`
        *Facet:* [`04_ui.locales`](#facet-04_ui.locales)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["LocalesMainLabel (LocalesMainLabel)"]
    W1["localesPanel (LocalesButton)"]
        ```

#### `looting.mmd`
        *Facet:* [`04_ui.looting`](#facet-04_ui.looting)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["value (TargetBotLootingPanel)"]
        ```

#### `market.mmd`
        *Facet:* [`04_ui.market`](#facet-04_ui.market)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["resetButton (MarketWindow)"]
        ```

#### `marketbuttons.mmd`
        *Facet:* [`04_ui.marketbuttons`](#facet-04_ui.marketbuttons)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["MarketButtonBox (MarketButtonBox)"]
        ```

#### `marketcombobox.mmd`
        *Facet:* [`04_ui.marketcombobox`](#facet-04_ui.marketcombobox)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["MarketComboBoxPopupMenuButton (MarketComboBoxPopupMenuButton)"]
    W1["MarketComboBoxPopupMenuSeparator (MarketComboBoxPopupMenuSeparator)"]
    W2["MarketComboBoxPopupMenu (MarketComboBoxPopupMenu)"]
    W3["MarketComboBox (MarketComboBox)"]
        ```

#### `markettabs.mmd`
        *Facet:* [`04_ui.markettabs`](#facet-04_ui.markettabs)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["MarketTabBar (MarketTabBar)"]
    W1["MarketTabBarPanel (MarketTabBarPanel)"]
    W2["MarketTabBarButton (MarketTabBarButton)"]
    W3["MarketRightTabBar (MarketRightTabBar)"]
    W4["MarketRightTabBarPanel (MarketRightTabBarPanel)"]
    W5["MarketRightTabBarButton (MarketRightTabBarButton)"]
        ```

#### `modaldialog.mmd`
        *Facet:* [`04_ui.modaldialog`](#facet-04_ui.modaldialog)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["ChoiceListLabel (ChoiceListLabel)"]
    W1["choiceList (ChoiceList)"]
    W2["choiceScrollBar (ChoiceScrollBar)"]
    W3["ModalButton (ModalButton)"]
    W4["buttonsPanel (ModalDialog)"]
        ```

#### `new_healer.mmd`
        *Facet:* [`04_ui.new_healer`](#facet-04_ui.new_healer)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `npctrade.mmd`
        *Facet:* [`04_ui.npctrade`](#facet-04_ui.npctrade)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["NPCOfferLabel (NPCOfferLabel)"]
    W1["tradeButton (NPCItemBox)"]
        ```

#### `object.mmd`
        *Facet:* [`04_ui.object`](#facet-04_ui.object)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (RoundCheckBox)"]
        ```

#### `options.mmd`
        *Facet:* [`04_ui.options`](#facet-04_ui.options)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["OptionCheckBox (OptionCheckBox)"]
    W1["OptionScrollbar (OptionScrollbar)"]
    W2["optionsTabContent (OptionPanel)"]
        ```

#### `outfitwindow.mmd`
        *Facet:* [`04_ui.outfitwindow`](#facet-04_ui.outfitwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["FloorTile (FloorTile)"]
        ```

#### `panels.mmd`
        *Facet:* [`04_ui.panels`](#facet-04_ui.panels)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `playerlist.mmd`
        *Facet:* [`04_ui.playerlist`](#facet-04_ui.playerlist)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (PlayerLabel)"]
    W1["SettingCheckBox (SettingCheckBox)"]
    W2["AutoAdd (Settings)"]
    W3["add (tPanel)"]
    W4["closeButton (PlayerListWindow)"]
        ```

#### `prey.mmd`
        *Facet:* [`04_ui.prey`](#facet-04_ui.prey)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `pushmax.mmd`
        *Facet:* [`04_ui.pushmax`](#facet-04_ui.pushmax)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["closeButton (PushMaxWindow)"]
        ```

#### `questlogwindow.mmd`
        *Facet:* [`04_ui.questlogwindow`](#facet-04_ui.questlogwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["description (QuestTrackerLabel)"]
    W1["QuestLabel (QuestLabel)"]
    W2["questListScrollBar (QuestLog)"]
    W3["missionDescription (MissionLog)"]
    W4["trackerButton (QuestLogWindow)"]
    W5["list (QuestTracker)"]
        ```

#### `ruleviolation.mmd`
        *Facet:* [`04_ui.ruleviolation`](#facet-04_ui.ruleviolation)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["RVListLabel (RVListLabel)"]
    W1["RVLabel (RVLabel)"]
    W2["commentText (RVTextEdit)"]
        ```

#### `shop.mmd`
        *Facet:* [`04_ui.shop`](#facet-04_ui.shop)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
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

#### `sideactionbar.mmd`
        *Facet:* [`04_ui.sideactionbar`](#facet-04_ui.sideactionbar)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cooldown (SideActionButton)"]
    W1["image (TopSliders)"]
    W2["nextPanel (BottomSliders)"]
        ```

#### `siolist.mmd`
        *Facet:* [`04_ui.siolist`](#facet-04_ui.siolist)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["RP (VocationPanel)"]
    W1["closeButton (SioListWindow)"]
        ```

#### `skills.mmd`
        *Facet:* [`04_ui.skills`](#facet-04_ui.skills)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SkillFirstWidget (SkillFirstWidget)"]
    W1["SkillButton (SkillButton)"]
    W2["SmallSkillButton (SmallSkillButton)"]
    W1 --> W2
    W3["SkillNameLabel (SkillNameLabel)"]
    W4["value (SkillValueLabel)"]
    W5["skillId12 (SkillPercentPanel)"]
        ```

#### `spell.mmd`
        *Facet:* [`04_ui.spell`](#facet-04_ui.spell)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (SpellPreview)"]
        ```

#### `spelllist.mmd`
        *Facet:* [`04_ui.spelllist`](#facet-04_ui.spelllist)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SpellListLabel (SpellListLabel)"]
    W1["SpellInfoLabel (SpellInfoLabel)"]
    W2["SpellInfoValueLabel (SpellInfoValueLabel)"]
    W3["premiumBoxYes (FilterButton)"]
        ```

#### `stats.mmd`
        *Facet:* [`04_ui.stats`](#facet-04_ui.stats)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["DebugText (DebugText)"]
    W1["debugScroll (DebugLabel)"]
        ```

#### `supplies.mmd`
        *Facet:* [`04_ui.supplies`](#facet-04_ui.supplies)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (ProfileLabel)"]
    W1["SupplySpinBox (SupplySpinBox)"]
    W2["avg (ItemPanel)"]
    W3["decrement (SuppliesWindow)"]
        ```

#### `supply.mmd`
        *Facet:* [`04_ui.supply`](#facet-04_ui.supply)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["max (SupplyItem)"]
    W1["scroll (SupplyItemList)"]
        ```

#### `target.mmd`
        *Facet:* [`04_ui.target`](#facet-04_ui.target)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["TargetBotEntry (TargetBotEntry)"]
    W1["right (TargetBotDualLabel)"]
    W2["debug (TargetBotPanel)"]
        ```

#### `terminal.mmd`
        *Facet:* [`04_ui.terminal`](#facet-04_ui.terminal)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["TerminalLabel (TerminalLabel)"]
    W1["rightResizeBorder (TerminalSelectText)"]
        ```

#### `textedit.mmd`
        *Facet:* [`04_ui.textedit`](#facet-04_ui.textedit)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancel (TextEditButtons)"]
    W1["examples (TextEditWindow)"]
    W2["text (SinglelineTextEditWindow)"]
    W1 --> W2
    W3["textScroll (MultilineTextEditWindow)"]
    W1 --> W3
        ```

#### `textmessage.mmd`
        *Facet:* [`04_ui.textmessage`](#facet-04_ui.textmessage)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["statusLabel (TextMessageLabel)"]
        ```

#### `textwindow.mmd`
        *Facet:* [`04_ui.textwindow`](#facet-04_ui.textwindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (TextWindow)"]
        ```

#### `topbar.mmd`
        *Facet:* [`04_ui.topbar`](#facet-04_ui.topbar)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["box (StatsPanel)"]
    W1["skills (SkillPanel)"]
        ```

#### `tradewindow.mmd`
        *Facet:* [`04_ui.tradewindow`](#facet-04_ui.tradewindow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["rejectButton (TradeWindow)"]
        ```

#### `unjustifiedpoints.mmd`
        *Facet:* [`04_ui.unjustifiedpoints`](#facet-04_ui.unjustifiedpoints)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SkullProgressBar (SkullProgressBar)"]
    W1["monthSkullWidget (SkullWidget)"]
        ```

#### `viplist.mmd`
        *Facet:* [`04_ui.viplist`](#facet-04_ui.viplist)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["vipWindow (VipListLabel)"]
        ```

#### `widgets_hierarchy.mmd`
        *Facet:* [`04_ui.widgets_hierarchy`](#facet-04_ui.widgets_hierarchy)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  WidgetHierarchy[04_ui:widgets_hierarchy] --> Data[Datasets]
  Data --> Page[Index]

click WidgetHierarchy "./index.html#facet-04_ui.widgets_hierarchy" "Open widgets_hierarchy"
        ```

## Appendix / Facets
(facet-04_ui.AttackBot)=
### Facet: `04_ui.AttackBot`
(facet-04_ui.BotServer)=
### Facet: `04_ui.BotServer`
(facet-04_ui.Conditions)=
### Facet: `04_ui.Conditions`
(facet-04_ui.HealBot)=
### Facet: `04_ui.HealBot`
(facet-04_ui.actionbar)=
### Facet: `04_ui.actionbar`
(facet-04_ui.alarms)=
### Facet: `04_ui.alarms`
(facet-04_ui.amountwindow)=
### Facet: `04_ui.amountwindow`
(facet-04_ui.analyzer)=
### Facet: `04_ui.analyzer`
(facet-04_ui.architecture)=
### Facet: `04_ui.architecture`
(facet-04_ui.basic)=
### Facet: `04_ui.basic`
(facet-04_ui.battle)=
### Facet: `04_ui.battle`
(facet-04_ui.battlebutton)=
### Facet: `04_ui.battlebutton`
(facet-04_ui.bot)=
### Facet: `04_ui.bot`
(facet-04_ui.browse)=
### Facet: `04_ui.browse`
(facet-04_ui.bugreport)=
### Facet: `04_ui.bugreport`
(facet-04_ui.cavebot)=
### Facet: `04_ui.cavebot`
(facet-04_ui.channelswindow)=
### Facet: `04_ui.channelswindow`
(facet-04_ui.characterlist)=
### Facet: `04_ui.characterlist`
(facet-04_ui.combo)=
### Facet: `04_ui.combo`
(facet-04_ui.communicationwindow)=
### Facet: `04_ui.communicationwindow`
(facet-04_ui.config)=
### Facet: `04_ui.config`
(facet-04_ui.container)=
### Facet: `04_ui.container`
(facet-04_ui.cooldown)=
### Facet: `04_ui.cooldown`
(facet-04_ui.countwindow)=
### Facet: `04_ui.countwindow`
(facet-04_ui.creature_editor)=
### Facet: `04_ui.creature_editor`
(facet-04_ui.currentoffers)=
### Facet: `04_ui.currentoffers`
(facet-04_ui.deathwindow)=
### Facet: `04_ui.deathwindow`
(facet-04_ui.depositer_config)=
### Facet: `04_ui.depositer_config`
(facet-04_ui.editor)=
### Facet: `04_ui.editor`
(facet-04_ui.editvip)=
### Facet: `04_ui.editvip`
(facet-04_ui.entities)=
### Facet: `04_ui.entities`
(facet-04_ui.equipper)=
### Facet: `04_ui.equipper`
(facet-04_ui.extras)=
### Facet: `04_ui.extras`
(facet-04_ui.flagwindow)=
### Facet: `04_ui.flagwindow`
(facet-04_ui.flow)=
### Facet: `04_ui.flow`
(facet-04_ui.gameinterface)=
### Facet: `04_ui.gameinterface`
(facet-04_ui.hotkeys_manager)=
### Facet: `04_ui.hotkeys_manager`
(facet-04_ui.icons)=
### Facet: `04_ui.icons`
(facet-04_ui.imbuing)=
### Facet: `04_ui.imbuing`
(facet-04_ui.itemdetails)=
### Facet: `04_ui.itemdetails`
(facet-04_ui.itemoffers)=
### Facet: `04_ui.itemoffers`
(facet-04_ui.itemselector)=
### Facet: `04_ui.itemselector`
(facet-04_ui.itemstats)=
### Facet: `04_ui.itemstats`
(facet-04_ui.locales)=
### Facet: `04_ui.locales`
(facet-04_ui.looting)=
### Facet: `04_ui.looting`
(facet-04_ui.market)=
### Facet: `04_ui.market`
(facet-04_ui.marketbuttons)=
### Facet: `04_ui.marketbuttons`
(facet-04_ui.marketcombobox)=
### Facet: `04_ui.marketcombobox`
(facet-04_ui.markettabs)=
### Facet: `04_ui.markettabs`
(facet-04_ui.modaldialog)=
### Facet: `04_ui.modaldialog`
(facet-04_ui.new_healer)=
### Facet: `04_ui.new_healer`
(facet-04_ui.npctrade)=
### Facet: `04_ui.npctrade`
(facet-04_ui.object)=
### Facet: `04_ui.object`
(facet-04_ui.options)=
### Facet: `04_ui.options`
(facet-04_ui.outfitwindow)=
### Facet: `04_ui.outfitwindow`
(facet-04_ui.panels)=
### Facet: `04_ui.panels`
(facet-04_ui.playerlist)=
### Facet: `04_ui.playerlist`
(facet-04_ui.prey)=
### Facet: `04_ui.prey`
(facet-04_ui.pushmax)=
### Facet: `04_ui.pushmax`
(facet-04_ui.questlogwindow)=
### Facet: `04_ui.questlogwindow`
(facet-04_ui.ruleviolation)=
### Facet: `04_ui.ruleviolation`
(facet-04_ui.shop)=
### Facet: `04_ui.shop`
(facet-04_ui.sideactionbar)=
### Facet: `04_ui.sideactionbar`
(facet-04_ui.siolist)=
### Facet: `04_ui.siolist`
(facet-04_ui.skills)=
### Facet: `04_ui.skills`
(facet-04_ui.spell)=
### Facet: `04_ui.spell`
(facet-04_ui.spelllist)=
### Facet: `04_ui.spelllist`
(facet-04_ui.stats)=
### Facet: `04_ui.stats`
(facet-04_ui.summary)=
### Facet: `04_ui.summary`
(facet-04_ui.supplies)=
### Facet: `04_ui.supplies`
(facet-04_ui.supply)=
### Facet: `04_ui.supply`
(facet-04_ui.target)=
### Facet: `04_ui.target`
(facet-04_ui.terminal)=
### Facet: `04_ui.terminal`
(facet-04_ui.textedit)=
### Facet: `04_ui.textedit`
(facet-04_ui.textmessage)=
### Facet: `04_ui.textmessage`
(facet-04_ui.textwindow)=
### Facet: `04_ui.textwindow`
(facet-04_ui.topbar)=
### Facet: `04_ui.topbar`
(facet-04_ui.tradewindow)=
### Facet: `04_ui.tradewindow`
(facet-04_ui.ui_widgets)=
### Facet: `04_ui.ui_widgets`
(facet-04_ui.unjustifiedpoints)=
### Facet: `04_ui.unjustifiedpoints`
(facet-04_ui.viplist)=
### Facet: `04_ui.viplist`
(facet-04_ui.widgets_hierarchy)=
### Facet: `04_ui.widgets_hierarchy`
