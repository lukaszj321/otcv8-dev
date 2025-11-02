---
title: 04_ui - Ui
---

# 04_ui - Ui

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### entities
*Facet:* [`04_ui.entities`](#facet-04_ui.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### needed_translations
*Facet:* [`04_ui.needed_translations`](#facet-04_ui.needed_translations)

```{csv-table} needed_translations
:header-rows: 1
:file: ./datasets/needed_translations.csv
:widths: auto
```

### otui_files
*Facet:* [`04_ui.otui_files`](#facet-04_ui.otui_files)

```{csv-table} otui_files
:header-rows: 1
:file: ./datasets/otui_files.csv
:widths: auto
```

### signals
*Facet:* [`04_ui.signals`](#facet-04_ui.signals)

```{csv-table} signals
:header-rows: 1
:file: ./datasets/signals.csv
:widths: auto
```

### summary
*Facet:* [`04_ui.summary`](#facet-04_ui.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

### ui_assets_map
*Facet:* [`04_ui.ui_assets_map`](#facet-04_ui.ui_assets_map)

```{csv-table} ui_assets_map
:header-rows: 1
:file: ./datasets/ui_assets_map.csv
:widths: auto
```

### ui_widgets
*Facet:* [`04_ui.ui_widgets`](#facet-04_ui.ui_widgets)

```{csv-table} ui_widgets
:header-rows: 1
:file: ./datasets/ui_widgets.csv
:widths: auto
```

## Diagrams
### AttackBot
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
click Attackbot "./index.html#facet-04_ui.AttackBot" "Open AttackBot"
```

### BotServer
*Facet:* [`04_ui.BotServer`](#facet-04_ui.BotServer)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["Members (BotServerData)"]
    W1["Broadcast (FeaturePanel)"]
    W2["enabled (BotServerWindow)"]
click Botserver "./index.html#facet-04_ui.BotServer" "Open BotServer"
```

### Conditions
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
click Conditions "./index.html#facet-04_ui.Conditions" "Open Conditions"
```

### HealBot
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
click Healbot "./index.html#facet-04_ui.HealBot" "Open HealBot"
```

### actionbar
*Facet:* [`04_ui.actionbar`](#facet-04_ui.actionbar)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cooldown (ActionButton)"]
    W1["image (LeftSliders)"]
    W2["nextPanel (RightSliders)"]
click Actionbar "./index.html#facet-04_ui.actionbar" "Open actionbar"
```

### alarms
*Facet:* [`04_ui.alarms`](#facet-04_ui.alarms)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["tick (AlarmCheckBox)"]
    W1["value (AlarmCheckBoxAndSpinBox)"]
    W2["text (AlarmCheckBoxAndTextEdit)"]
    W3["closeButton (AlarmsWindow)"]
click Alarms "./index.html#facet-04_ui.alarms" "Open alarms"
```

### amountwindow
*Facet:* [`04_ui.amountwindow`](#facet-04_ui.amountwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (AmountWindow)"]
click Amountwindow "./index.html#facet-04_ui.amountwindow" "Open amountwindow"
```

### analyzer
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
click Analyzer "./index.html#facet-04_ui.analyzer" "Open analyzer"
```

### architecture
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
click Architecture "./index.html#facet-04_ui.architecture" "Open architecture"
```

### basic
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
click Basic "./index.html#facet-04_ui.basic" "Open basic"
```

### battle
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
click Battle "./index.html#facet-04_ui.battle" "Open battle"
```

### battlebutton
*Facet:* [`04_ui.battlebutton`](#facet-04_ui.battlebutton)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["BattleButton (BattleButton)"]
click Battlebutton "./index.html#facet-04_ui.battlebutton" "Open battlebutton"
```

### bot
*Facet:* [`04_ui.bot`](#facet-04_ui.bot)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["BotTabBar (BotTabBar)"]
    W1["botPanel (BotTabBarPanel)"]
    W2["botPanel (BotTabBarButton)"]
click Bot "./index.html#facet-04_ui.bot" "Open bot"
```

### browse
*Facet:* [`04_ui.browse`](#facet-04_ui.browse)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["filterSearchAll (MarketItemBox)"]
click Browse "./index.html#facet-04_ui.browse" "Open browse"
```

### bugreport
*Facet:* [`04_ui.bugreport`](#facet-04_ui.bugreport)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (BugReportWindow)"]
click Bugreport "./index.html#facet-04_ui.bugreport" "Open bugreport"
```

### cavebot
*Facet:* [`04_ui.cavebot`](#facet-04_ui.cavebot)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["CaveBotAction (CaveBotAction)"]
    W1["showConfig (CaveBotPanel)"]
click Cavebot "./index.html#facet-04_ui.cavebot" "Open cavebot"
```

### channelswindow
*Facet:* [`04_ui.channelswindow`](#facet-04_ui.channelswindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["channelsScrollBar (ChannelListLabel)"]
click Channelswindow "./index.html#facet-04_ui.channelswindow" "Open channelswindow"
```

### characterlist
*Facet:* [`04_ui.characterlist`](#facet-04_ui.characterlist)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (CharacterWidget)"]
click Characterlist "./index.html#facet-04_ui.characterlist" "Open characterlist"
```

### combo
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
click Combo "./index.html#facet-04_ui.combo" "Open combo"
```

### communicationwindow
*Facet:* [`04_ui.communicationwindow`](#facet-04_ui.communicationwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["IgnoreListLabel (IgnoreListLabel)"]
    W1["whiteListScrollBar (WhiteListLabel)"]
click Communicationwindow "./index.html#facet-04_ui.communicationwindow" "Open communicationwindow"
```

### config
*Facet:* [`04_ui.config`](#facet-04_ui.config)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (BotConfig)"]
click Config "./index.html#facet-04_ui.config" "Open config"
```

### container
*Facet:* [`04_ui.container`](#facet-04_ui.container)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (BotContainer)"]
click Container "./index.html#facet-04_ui.container" "Open container"
```

### cooldown
*Facet:* [`04_ui.cooldown`](#facet-04_ui.cooldown)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SpellGroupIcon (SpellGroupIcon)"]
    W1["SpellIcon (SpellIcon)"]
    W2["SpellProgressRect (SpellProgressRect)"]
    W3["cooldownPanel (GroupCooldownParticles)"]
click Cooldown "./index.html#facet-04_ui.cooldown" "Open cooldown"
```

### countwindow
*Facet:* [`04_ui.countwindow`](#facet-04_ui.countwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (CountWindow)"]
click Countwindow "./index.html#facet-04_ui.countwindow" "Open countwindow"
```

### creature_editor
*Facet:* [`04_ui.creature_editor`](#facet-04_ui.creature_editor)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (TargetBotCreatureEditorScrollBar)"]
    W1["textEdit (TargetBotCreatureEditorTextEdit)"]
    W2["item (TargetBotCreatureEditorItem)"]
    W3["TargetBotCreatureEditorCheckBox (TargetBotCreatureEditorCheckBox)"]
    W4["cancel (TargetBotCreatureEditorWindow)"]
click CreatureEditor "./index.html#facet-04_ui.creature_editor" "Open creature_editor"
```

### currentoffers
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
click Currentoffers "./index.html#facet-04_ui.currentoffers" "Open currentoffers"
```

### deathwindow
*Facet:* [`04_ui.deathwindow`](#facet-04_ui.deathwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (DeathWindow)"]
click Deathwindow "./index.html#facet-04_ui.deathwindow" "Open deathwindow"
```

### depositer_config
*Facet:* [`04_ui.depositer_config`](#facet-04_ui.depositer_config)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["slot (StashItem)"]
    W1["CloseButton (DepositerPanel)"]
click DepositerConfig "./index.html#facet-04_ui.depositer_config" "Open depositer_config"
```

### editor
*Facet:* [`04_ui.editor`](#facet-04_ui.editor)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["autoRecording (CaveBotEditorButton)"]
    W1["autoRecording (CaveBotEditorPanel)"]
click Editor "./index.html#facet-04_ui.editor" "Open editor"
```

### editvip
*Facet:* [`04_ui.editvip`](#facet-04_ui.editvip)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonCancel (IconButton)"]
click Editvip "./index.html#facet-04_ui.editvip" "Open editvip"
```

### equipper
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
click Equipper "./index.html#facet-04_ui.equipper" "Open equipper"
```

### extras
*Facet:* [`04_ui.extras`](#facet-04_ui.extras)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["scroll (ExtrasScrollBar)"]
    W1["textEdit (ExtrasTextEdit)"]
    W2["item (ExtrasItem)"]
    W3["ExtrasCheckBox (ExtrasCheckBox)"]
    W4["closeButton (ExtrasWindow)"]
click Extras "./index.html#facet-04_ui.extras" "Open extras"
```

### flagwindow
*Facet:* [`04_ui.flagwindow`](#facet-04_ui.flagwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["FlagButton (FlagButton)"]
    W1["cancelButton (FlagWindow)"]
click Flagwindow "./index.html#facet-04_ui.flagwindow" "Open flagwindow"
```

### flow
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
click Flow "./index.html#facet-04_ui.flow" "Open flow"
```

### gameinterface
*Facet:* [`04_ui.gameinterface`](#facet-04_ui.gameinterface)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["GameSidePanel (GameSidePanel)"]
    W1["GameMapPanel (GameMapPanel)"]
    W2["gameTopBar (GameAction)"]
click Gameinterface "./index.html#facet-04_ui.gameinterface" "Open gameinterface"
```

### hierarchy
*Facet:* [`04_ui.hierarchy`](#facet-04_ui.hierarchy)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[04_ui.hierarchy] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-04_ui.hierarchy" "Open hierarchy"
click Hierarchy "./index.html#facet-04_ui.hierarchy" "Open hierarchy"
```

### hotkeys_manager
*Facet:* [`04_ui.hotkeys_manager`](#facet-04_ui.hotkeys_manager)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (HotkeyListLabel)"]
    W1["cancelButton (HotkeyAssignWindow)"]
click HotkeysManager "./index.html#facet-04_ui.hotkeys_manager" "Open hotkeys_manager"
```

### icons
*Facet:* [`04_ui.icons`](#facet-04_ui.icons)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["text (BotIcon)"]
click Icons "./index.html#facet-04_ui.icons" "Open icons"
```

### imbuing
*Facet:* [`04_ui.imbuing`](#facet-04_ui.imbuing)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["Slot (Slot)"]
    W1["count (RequiredItem)"]
    W2["selectSlot (ItemInformation)"]
    W3["cost (EmptyImbue)"]
    W4["balance (ClearImbue)"]
click Imbuing "./index.html#facet-04_ui.imbuing" "Open imbuing"
```

### itemdetails
*Facet:* [`04_ui.itemdetails`](#facet-04_ui.itemdetails)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["DetailsTableRow (DetailsTableRow)"]
    W1["detailsTableScrollBar (DetailsTableColumn)"]
click Itemdetails "./index.html#facet-04_ui.itemdetails" "Open itemdetails"
```

### itemoffers
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
click Itemoffers "./index.html#facet-04_ui.itemoffers" "Open itemoffers"
```

### itemselector
*Facet:* [`04_ui.itemselector`](#facet-04_ui.itemselector)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (ItemSelectorWindow)"]
click Itemselector "./index.html#facet-04_ui.itemselector" "Open itemselector"
```

### itemstats
*Facet:* [`04_ui.itemstats`](#facet-04_ui.itemstats)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["StatsTableRow (StatsTableRow)"]
    W1["sellStatsTableScrollBar (StatsTableColumn)"]
click Itemstats "./index.html#facet-04_ui.itemstats" "Open itemstats"
```

### locales
*Facet:* [`04_ui.locales`](#facet-04_ui.locales)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["LocalesMainLabel (LocalesMainLabel)"]
    W1["localesPanel (LocalesButton)"]
click Locales "./index.html#facet-04_ui.locales" "Open locales"
```

### looting
*Facet:* [`04_ui.looting`](#facet-04_ui.looting)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["value (TargetBotLootingPanel)"]
click Looting "./index.html#facet-04_ui.looting" "Open looting"
```

### market
*Facet:* [`04_ui.market`](#facet-04_ui.market)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["resetButton (MarketWindow)"]
click Market "./index.html#facet-04_ui.market" "Open market"
```

### marketbuttons
*Facet:* [`04_ui.marketbuttons`](#facet-04_ui.marketbuttons)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["MarketButtonBox (MarketButtonBox)"]
click Marketbuttons "./index.html#facet-04_ui.marketbuttons" "Open marketbuttons"
```

### marketcombobox
*Facet:* [`04_ui.marketcombobox`](#facet-04_ui.marketcombobox)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["MarketComboBoxPopupMenuButton (MarketComboBoxPopupMenuButton)"]
    W1["MarketComboBoxPopupMenuSeparator (MarketComboBoxPopupMenuSeparator)"]
    W2["MarketComboBoxPopupMenu (MarketComboBoxPopupMenu)"]
    W3["MarketComboBox (MarketComboBox)"]
click Marketcombobox "./index.html#facet-04_ui.marketcombobox" "Open marketcombobox"
```

### markettabs
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
click Markettabs "./index.html#facet-04_ui.markettabs" "Open markettabs"
```

### modaldialog
*Facet:* [`04_ui.modaldialog`](#facet-04_ui.modaldialog)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["ChoiceListLabel (ChoiceListLabel)"]
    W1["choiceList (ChoiceList)"]
    W2["choiceScrollBar (ChoiceScrollBar)"]
    W3["ModalButton (ModalButton)"]
    W4["buttonsPanel (ModalDialog)"]
click Modaldialog "./index.html#facet-04_ui.modaldialog" "Open modaldialog"
```

### new_healer
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
click NewHealer "./index.html#facet-04_ui.new_healer" "Open new_healer"
```

### npctrade
*Facet:* [`04_ui.npctrade`](#facet-04_ui.npctrade)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["NPCOfferLabel (NPCOfferLabel)"]
    W1["tradeButton (NPCItemBox)"]
click Npctrade "./index.html#facet-04_ui.npctrade" "Open npctrade"
```

### object
*Facet:* [`04_ui.object`](#facet-04_ui.object)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (RoundCheckBox)"]
click Object "./index.html#facet-04_ui.object" "Open object"
```

### options
*Facet:* [`04_ui.options`](#facet-04_ui.options)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["OptionCheckBox (OptionCheckBox)"]
    W1["OptionScrollbar (OptionScrollbar)"]
    W2["optionsTabContent (OptionPanel)"]
click Options "./index.html#facet-04_ui.options" "Open options"
```

### otui_assets_mapping
*Facet:* [`04_ui.otui_assets_mapping`](#facet-04_ui.otui_assets_mapping)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    OTUI[OTUI Widget] -->|references| Asset[Asset Path]
    
    subgraph "Image Assets"
        I1[/images/topbuttons/]
        I2[/images/ui/]
        I3[/images/game/]
    end
    
    subgraph "Font Assets"
        F1[verdana-11px-antialised]
        F2[verdana-11px-rounded]
        F3[terminus-14px-bold]
    end
    
    Asset -->|icon| I1
    Asset -->|background| I2
    Asset -->|texture| I3
    Asset -->|font| F1
    Asset -->|font| F2
    Asset -->|font| F3
    
    I1 -->|stored in| DataDir[data/images/topbuttons/]
    I2 -->|stored in| DataDir2[data/images/ui/]
    I3 -->|stored in| DataDir3[data/images/game/]
    
    F1 -->|defined in| FontsDir[data/fonts/]
    F2 -->|defined in| FontsDir
    F3 -->|defined in| FontsDir
    
    click Asset "../index.html#facet-04_ui.assets" "UI Assets"
    click OTUI "../index.html#facet-04_ui.otui_data" "OTUI-Data Mapping"
click OtuiAssetsMapping "./index.html#facet-04_ui.otui_assets_mapping" "Open otui_assets_mapping"
```

### outfitwindow
*Facet:* [`04_ui.outfitwindow`](#facet-04_ui.outfitwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["FloorTile (FloorTile)"]
click Outfitwindow "./index.html#facet-04_ui.outfitwindow" "Open outfitwindow"
```

### overview
*Facet:* [`04_ui.overview`](#facet-04_ui.overview)

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[UI/OTUI] --> B[Components]
    A --> C[Datasets]
    A --> D[Diagrams]
click Overview "./index.html#facet-04_ui.overview" "Open overview"
```

### panels
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
click Panels "./index.html#facet-04_ui.panels" "Open panels"
```

### playerlist
*Facet:* [`04_ui.playerlist`](#facet-04_ui.playerlist)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (PlayerLabel)"]
    W1["SettingCheckBox (SettingCheckBox)"]
    W2["AutoAdd (Settings)"]
    W3["add (tPanel)"]
    W4["closeButton (PlayerListWindow)"]
click Playerlist "./index.html#facet-04_ui.playerlist" "Open playerlist"
```

### prey
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
click Prey "./index.html#facet-04_ui.prey" "Open prey"
```

### pushmax
*Facet:* [`04_ui.pushmax`](#facet-04_ui.pushmax)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["closeButton (PushMaxWindow)"]
click Pushmax "./index.html#facet-04_ui.pushmax" "Open pushmax"
```

### questlogwindow
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
click Questlogwindow "./index.html#facet-04_ui.questlogwindow" "Open questlogwindow"
```

### ruleviolation
*Facet:* [`04_ui.ruleviolation`](#facet-04_ui.ruleviolation)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["RVListLabel (RVListLabel)"]
    W1["RVLabel (RVLabel)"]
    W2["commentText (RVTextEdit)"]
click Ruleviolation "./index.html#facet-04_ui.ruleviolation" "Open ruleviolation"
```

### shop
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
click Shop "./index.html#facet-04_ui.shop" "Open shop"
```

### sideactionbar
*Facet:* [`04_ui.sideactionbar`](#facet-04_ui.sideactionbar)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cooldown (SideActionButton)"]
    W1["image (TopSliders)"]
    W2["nextPanel (BottomSliders)"]
click Sideactionbar "./index.html#facet-04_ui.sideactionbar" "Open sideactionbar"
```

### signal_flow
*Facet:* [`04_ui.signal_flow`](#facet-04_ui.signal_flow)

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'},'securityLevel':'loose'}}%%
graph TD
    OTUI[OTUI File] -->|defines| Widget[UI Widget]
    Widget -->|emits| Signal[@onClick @onDoubleClick etc]
    Signal -->|connects to| LuaHandler[Lua Handler Function]
    
    subgraph "Signal Types"
        S1[@onClick]
        S2[@onDoubleClick]
        S3[@onHoverChange]
        S4[@onFocusChange]
        S5[@onTextChange]
    end
    
    Signal --> S1
    Signal --> S2
    Signal --> S3
    Signal --> S4
    Signal --> S5
    
    LuaHandler -->|calls| Module[Module Function]
    Module -->|updates| Widget
    
    subgraph "Common Handlers"
        H1[toggle]
        H2[show/hide]
        H3[setOption]
        H4[refresh]
    end
    
    Module --> H1
    Module --> H2
    Module --> H3
    Module --> H4
    
    click Signal "../index.html#facet-04_ui.signals" "UI Signals"
    click Widget "../index.html#facet-04_ui.widgets" "UI Widgets"
click SignalFlow "./index.html#facet-04_ui.signal_flow" "Open signal_flow"
```

### siolist
*Facet:* [`04_ui.siolist`](#facet-04_ui.siolist)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["RP (VocationPanel)"]
    W1["closeButton (SioListWindow)"]
click Siolist "./index.html#facet-04_ui.siolist" "Open siolist"
```

### skills
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
click Skills "./index.html#facet-04_ui.skills" "Open skills"
```

### spell
*Facet:* [`04_ui.spell`](#facet-04_ui.spell)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["buttonOk (SpellPreview)"]
click Spell "./index.html#facet-04_ui.spell" "Open spell"
```

### spelllist
*Facet:* [`04_ui.spelllist`](#facet-04_ui.spelllist)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SpellListLabel (SpellListLabel)"]
    W1["SpellInfoLabel (SpellInfoLabel)"]
    W2["SpellInfoValueLabel (SpellInfoValueLabel)"]
    W3["premiumBoxYes (FilterButton)"]
click Spelllist "./index.html#facet-04_ui.spelllist" "Open spelllist"
```

### stats
*Facet:* [`04_ui.stats`](#facet-04_ui.stats)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["DebugText (DebugText)"]
    W1["debugScroll (DebugLabel)"]
click Stats "./index.html#facet-04_ui.stats" "Open stats"
```

### supplies
*Facet:* [`04_ui.supplies`](#facet-04_ui.supplies)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["remove (ProfileLabel)"]
    W1["SupplySpinBox (SupplySpinBox)"]
    W2["avg (ItemPanel)"]
    W3["decrement (SuppliesWindow)"]
click Supplies "./index.html#facet-04_ui.supplies" "Open supplies"
```

### supply
*Facet:* [`04_ui.supply`](#facet-04_ui.supply)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["max (SupplyItem)"]
    W1["scroll (SupplyItemList)"]
click Supply "./index.html#facet-04_ui.supply" "Open supply"
```

### target
*Facet:* [`04_ui.target`](#facet-04_ui.target)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["TargetBotEntry (TargetBotEntry)"]
    W1["right (TargetBotDualLabel)"]
    W2["debug (TargetBotPanel)"]
click Target "./index.html#facet-04_ui.target" "Open target"
```

### terminal
*Facet:* [`04_ui.terminal`](#facet-04_ui.terminal)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["TerminalLabel (TerminalLabel)"]
    W1["rightResizeBorder (TerminalSelectText)"]
click Terminal "./index.html#facet-04_ui.terminal" "Open terminal"
```

### textedit
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
click Textedit "./index.html#facet-04_ui.textedit" "Open textedit"
```

### textmessage
*Facet:* [`04_ui.textmessage`](#facet-04_ui.textmessage)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["statusLabel (TextMessageLabel)"]
click Textmessage "./index.html#facet-04_ui.textmessage" "Open textmessage"
```

### textwindow
*Facet:* [`04_ui.textwindow`](#facet-04_ui.textwindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["cancelButton (TextWindow)"]
click Textwindow "./index.html#facet-04_ui.textwindow" "Open textwindow"
```

### topbar
*Facet:* [`04_ui.topbar`](#facet-04_ui.topbar)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["box (StatsPanel)"]
    W1["skills (SkillPanel)"]
click Topbar "./index.html#facet-04_ui.topbar" "Open topbar"
```

### tradewindow
*Facet:* [`04_ui.tradewindow`](#facet-04_ui.tradewindow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["rejectButton (TradeWindow)"]
click Tradewindow "./index.html#facet-04_ui.tradewindow" "Open tradewindow"
```

### ui_flow
*Facet:* [`04_ui.ui_flow`](#facet-04_ui.ui_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[04_ui.ui_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-04_ui.ui_flow" "Open ui_flow"
click UiFlow "./index.html#facet-04_ui.ui_flow" "Open ui_flow"
```

### unjustifiedpoints
*Facet:* [`04_ui.unjustifiedpoints`](#facet-04_ui.unjustifiedpoints)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["SkullProgressBar (SkullProgressBar)"]
    W1["monthSkullWidget (SkullWidget)"]
click Unjustifiedpoints "./index.html#facet-04_ui.unjustifiedpoints" "Open unjustifiedpoints"
```

### viplist
*Facet:* [`04_ui.viplist`](#facet-04_ui.viplist)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    W0["vipWindow (VipListLabel)"]
click Viplist "./index.html#facet-04_ui.viplist" "Open viplist"
```

### widgets_hierarchy
*Facet:* [`04_ui.widgets_hierarchy`](#facet-04_ui.widgets_hierarchy)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  WidgetHierarchy[04_ui:widgets_hierarchy] --> Data[Datasets]
  Data --> Page[Index]

click WidgetHierarchy "./index.html#facet-04_ui.widgets_hierarchy" "Open widgets_hierarchy"
click WidgetsHierarchy "./index.html#facet-04_ui.widgets_hierarchy" "Open widgets_hierarchy"
```

## Podkatalogi

```{toctree}
:maxdepth: 1
:titlesonly:
blueprints/index
otui/index
otui-templates/index
```

## Crosslinks

- **renders** → `03_modules.lua_exports` (evidence: `docs/authoring/03_modules/datasets/lua_exports.csv`)
- **emits** → `02_events.events_matrix` (evidence: `docs/authoring/02_events/datasets/events_matrix.csv`)
- **uses** → `06_assets.assets_index` (evidence: `docs/authoring/06_assets/datasets/assets_index.csv`)
- **logs** → `09_logging.logging_categories` (evidence: `docs/authoring/09_logging/datasets/logging_categories.csv`)

## Appendix / Facets

(facet-04_ui.AttackBot)=
### Facet: `04_ui.AttackBot`
Type: diagram

(facet-04_ui.BotServer)=
### Facet: `04_ui.BotServer`
Type: diagram

(facet-04_ui.Conditions)=
### Facet: `04_ui.Conditions`
Type: diagram

(facet-04_ui.HealBot)=
### Facet: `04_ui.HealBot`
Type: diagram

(facet-04_ui.actionbar)=
### Facet: `04_ui.actionbar`
Type: diagram

(facet-04_ui.alarms)=
### Facet: `04_ui.alarms`
Type: diagram

(facet-04_ui.amountwindow)=
### Facet: `04_ui.amountwindow`
Type: diagram

(facet-04_ui.analyzer)=
### Facet: `04_ui.analyzer`
Type: diagram

(facet-04_ui.architecture)=
### Facet: `04_ui.architecture`
Type: diagram

(facet-04_ui.basic)=
### Facet: `04_ui.basic`
Type: diagram

(facet-04_ui.battle)=
### Facet: `04_ui.battle`
Type: diagram

(facet-04_ui.battlebutton)=
### Facet: `04_ui.battlebutton`
Type: diagram

(facet-04_ui.bot)=
### Facet: `04_ui.bot`
Type: diagram

(facet-04_ui.browse)=
### Facet: `04_ui.browse`
Type: diagram

(facet-04_ui.bugreport)=
### Facet: `04_ui.bugreport`
Type: diagram

(facet-04_ui.cavebot)=
### Facet: `04_ui.cavebot`
Type: diagram

(facet-04_ui.channelswindow)=
### Facet: `04_ui.channelswindow`
Type: diagram

(facet-04_ui.characterlist)=
### Facet: `04_ui.characterlist`
Type: diagram

(facet-04_ui.combo)=
### Facet: `04_ui.combo`
Type: diagram

(facet-04_ui.communicationwindow)=
### Facet: `04_ui.communicationwindow`
Type: diagram

(facet-04_ui.config)=
### Facet: `04_ui.config`
Type: diagram

(facet-04_ui.container)=
### Facet: `04_ui.container`
Type: diagram

(facet-04_ui.cooldown)=
### Facet: `04_ui.cooldown`
Type: diagram

(facet-04_ui.countwindow)=
### Facet: `04_ui.countwindow`
Type: diagram

(facet-04_ui.creature_editor)=
### Facet: `04_ui.creature_editor`
Type: diagram

(facet-04_ui.currentoffers)=
### Facet: `04_ui.currentoffers`
Type: diagram

(facet-04_ui.deathwindow)=
### Facet: `04_ui.deathwindow`
Type: diagram

(facet-04_ui.depositer_config)=
### Facet: `04_ui.depositer_config`
Type: diagram

(facet-04_ui.editor)=
### Facet: `04_ui.editor`
Type: diagram

(facet-04_ui.editvip)=
### Facet: `04_ui.editvip`
Type: diagram

(facet-04_ui.entities)=
### Facet: `04_ui.entities`
Type: dataset

(facet-04_ui.equipper)=
### Facet: `04_ui.equipper`
Type: diagram

(facet-04_ui.extras)=
### Facet: `04_ui.extras`
Type: diagram

(facet-04_ui.flagwindow)=
### Facet: `04_ui.flagwindow`
Type: diagram

(facet-04_ui.flow)=
### Facet: `04_ui.flow`
Type: diagram

(facet-04_ui.gameinterface)=
### Facet: `04_ui.gameinterface`
Type: diagram

(facet-04_ui.hierarchy)=
### Facet: `04_ui.hierarchy`
Type: diagram

(facet-04_ui.hotkeys_manager)=
### Facet: `04_ui.hotkeys_manager`
Type: diagram

(facet-04_ui.icons)=
### Facet: `04_ui.icons`
Type: diagram

(facet-04_ui.imbuing)=
### Facet: `04_ui.imbuing`
Type: diagram

(facet-04_ui.itemdetails)=
### Facet: `04_ui.itemdetails`
Type: diagram

(facet-04_ui.itemoffers)=
### Facet: `04_ui.itemoffers`
Type: diagram

(facet-04_ui.itemselector)=
### Facet: `04_ui.itemselector`
Type: diagram

(facet-04_ui.itemstats)=
### Facet: `04_ui.itemstats`
Type: diagram

(facet-04_ui.locales)=
### Facet: `04_ui.locales`
Type: diagram

(facet-04_ui.looting)=
### Facet: `04_ui.looting`
Type: diagram

(facet-04_ui.market)=
### Facet: `04_ui.market`
Type: diagram

(facet-04_ui.marketbuttons)=
### Facet: `04_ui.marketbuttons`
Type: diagram

(facet-04_ui.marketcombobox)=
### Facet: `04_ui.marketcombobox`
Type: diagram

(facet-04_ui.markettabs)=
### Facet: `04_ui.markettabs`
Type: diagram

(facet-04_ui.modaldialog)=
### Facet: `04_ui.modaldialog`
Type: diagram

(facet-04_ui.needed_translations)=
### Facet: `04_ui.needed_translations`
Type: dataset

(facet-04_ui.new_healer)=
### Facet: `04_ui.new_healer`
Type: diagram

(facet-04_ui.npctrade)=
### Facet: `04_ui.npctrade`
Type: diagram

(facet-04_ui.object)=
### Facet: `04_ui.object`
Type: diagram

(facet-04_ui.options)=
### Facet: `04_ui.options`
Type: diagram

(facet-04_ui.otui_assets_mapping)=
### Facet: `04_ui.otui_assets_mapping`
Type: diagram

(facet-04_ui.otui_files)=
### Facet: `04_ui.otui_files`
Type: dataset

(facet-04_ui.outfitwindow)=
### Facet: `04_ui.outfitwindow`
Type: diagram

(facet-04_ui.overview)=
### Facet: `04_ui.overview`
Type: diagram

(facet-04_ui.panels)=
### Facet: `04_ui.panels`
Type: diagram

(facet-04_ui.playerlist)=
### Facet: `04_ui.playerlist`
Type: diagram

(facet-04_ui.prey)=
### Facet: `04_ui.prey`
Type: diagram

(facet-04_ui.pushmax)=
### Facet: `04_ui.pushmax`
Type: diagram

(facet-04_ui.questlogwindow)=
### Facet: `04_ui.questlogwindow`
Type: diagram

(facet-04_ui.ruleviolation)=
### Facet: `04_ui.ruleviolation`
Type: diagram

(facet-04_ui.shop)=
### Facet: `04_ui.shop`
Type: diagram

(facet-04_ui.sideactionbar)=
### Facet: `04_ui.sideactionbar`
Type: diagram

(facet-04_ui.signal_flow)=
### Facet: `04_ui.signal_flow`
Type: diagram

(facet-04_ui.signals)=
### Facet: `04_ui.signals`
Type: dataset

(facet-04_ui.siolist)=
### Facet: `04_ui.siolist`
Type: diagram

(facet-04_ui.skills)=
### Facet: `04_ui.skills`
Type: diagram

(facet-04_ui.spell)=
### Facet: `04_ui.spell`
Type: diagram

(facet-04_ui.spelllist)=
### Facet: `04_ui.spelllist`
Type: diagram

(facet-04_ui.stats)=
### Facet: `04_ui.stats`
Type: diagram

(facet-04_ui.summary)=
### Facet: `04_ui.summary`
Type: dataset

(facet-04_ui.supplies)=
### Facet: `04_ui.supplies`
Type: diagram

(facet-04_ui.supply)=
### Facet: `04_ui.supply`
Type: diagram

(facet-04_ui.target)=
### Facet: `04_ui.target`
Type: diagram

(facet-04_ui.terminal)=
### Facet: `04_ui.terminal`
Type: diagram

(facet-04_ui.textedit)=
### Facet: `04_ui.textedit`
Type: diagram

(facet-04_ui.textmessage)=
### Facet: `04_ui.textmessage`
Type: diagram

(facet-04_ui.textwindow)=
### Facet: `04_ui.textwindow`
Type: diagram

(facet-04_ui.topbar)=
### Facet: `04_ui.topbar`
Type: diagram

(facet-04_ui.tradewindow)=
### Facet: `04_ui.tradewindow`
Type: diagram

(facet-04_ui.ui_assets_map)=
### Facet: `04_ui.ui_assets_map`
Type: dataset

(facet-04_ui.ui_flow)=
### Facet: `04_ui.ui_flow`
Type: diagram

(facet-04_ui.ui_widgets)=
### Facet: `04_ui.ui_widgets`
Type: dataset

(facet-04_ui.unjustifiedpoints)=
### Facet: `04_ui.unjustifiedpoints`
Type: diagram

(facet-04_ui.viplist)=
### Facet: `04_ui.viplist`
Type: diagram

(facet-04_ui.widgets_hierarchy)=
### Facet: `04_ui.widgets_hierarchy`
Type: diagram

