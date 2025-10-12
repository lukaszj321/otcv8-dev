# OTCv8 – Pełne API (auto)

Wygenerowano: 2025-10-12T21:03:00.017Z

> Ten plik jest generowany automatycznie z kodu. Nie edytuj ręcznie.

```{contents}
:depth: 2
:backlinks: entry
```

(lua-api)=
## 1. Lua

### 1.1. Zdarzenia `on*`
- `onAddItem(...)`
- `onAddonChange(...)`
- `onAddThing(...)`
- `onAddVip(...)`
- `onAmountChange(...)`
- `onAnimatedText(...)`
- `onAppearanceChange(...)`
- `onAttackingCreatureChange(...)`
- `onAuraSelect(...)`
- `onAutoWalkFail(...)`
- `onBaseMagicLevelChange(...)`
- `onBaseSkillChange(...)`
- `onBaseSpeedChange(...)`
- `onBattleButtonHoverChange(...)`
- `onBattleButtonMouseRelease(...)`
- `onBlessingsChange(...)`
- `onBuyWithBackpackChange(...)`
- `onCameraPositionChange(...)`
- `onCancelWalk(...)`
- `onChangeCategory(...)`
- `onChangeOfferType(...)`
- `onChangeSlotFilter(...)`
- `onChangeSortOrder(...)`
- `onChangeSortType(...)`
- `onChangeSubCategory(...)`
- `onChangeUseType(...)`
- `onChannelEvent(...)`
- `onChannelList(...)`
- `onCharacterList(...)`
- `onChildFocusChange(...)`
- `onChooseItemMouseRelease(...)`
- `onClick(...)`
- `onClickIgnoreButton(...)`
- `onClose(...)`
- `onCloseChannel(...)`
- `onCloseImbuementWindow(...)`
- `onCloseNpcTrade(...)`
- `onCoinBalance(...)`
- `onColorCheckChange(...)`
- `onColorModeChange(...)`
- `onCommandChange(...)`
- `onConfigChange(...)`
- `onConnect(...)`
- `onContainerChangeSize(...)`
- `onContainerClose(...)`
- `onContainerOpen(...)`
- `onContainerUpdateItem(...)`
- `onCreate(...)`
- `onCreatureAppear(...)`
- `onCreatureDisappear(...)`
- `onCreatureHealthPercentChange(...)`
- `onCreaturePositionChange(...)`
- `onDecrement(...)`
- `onDestroy(...)`
- `onDoubleClick(...)`
- `onDownload(...)`
- `onDownloadProgress(...)`
- `onDragEnter(...)`
- `onDragLeave(...)`
- `onDragMove(...)`
- `onDrop(...)`
- `onDropActionButton(...)`
- `onEmblemChange(...)`
- `onError(...)`
- `onExperienceChange(...)`
- `onExtendedJSONOpcode(...)`
- `onExtendedOpcode(...)`
- `onFilterSearch(...)`
- `onFlagMouseRelease(...)`
- `onFocusChange(...)`
- `onFreeCapacityChange(...)`
- `onGameCloseTrade(...)`
- `onGameConnectionError(...)`
- `onGameCounterTrade(...)`
- `onGameEditList(...)`
- `onGameEditText(...)`
- `onGameEnd(...)`
- `onGameLoginError(...)`
- `onGameLoginToken(...)`
- `onGameOwnTrade(...)`
- `onGameQuestLine(...)`
- `onGameQuestLog(...)`
- `onGameStart(...)`
- `onGameUpdateNeeded(...)`
- `onGeometryChange(...)`
- `onGet(...)`
- `onGetProgress(...)`
- `onGroupSpellCooldown(...)`
- `onHealthBarSelect(...)`
- `onHealthChange(...)`
- `onHeightChange(...)`
- `onHotkeyTextChange(...)`
- `onHover(...)`
- `onHoverChange(...)`
- `onHTTPResult(...)`
- `onIconChange(...)`
- `onIgnoreCapacityChange(...)`
- `onIgnoreEquippedChange(...)`
- `onImbuementWindow(...)`
- `onIncrement(...)`
- `onInventoryChange(...)`
- `onItemBoxChecked(...)`
- `onItemChange(...)`
- `onKeyDown(...)`
- `onKeypadTouchMove(...)`
- `onKeypadTouchPress(...)`
- `onKeypadTouchRelease(...)`
- `onKeyPress(...)`
- `onKeyUp(...)`
- `onLayoutUpdate(...)`
- `onLevelChange(...)`
- `onLoadCallback(...)`
- `onLocaleChanged(...)`
- `onLog(...)`
- `onLoginAdvice(...)`
- `onLoginError(...)`
- `onLoginWait(...)`
- `onLogout(...)`
- `onMagicLevelChange(...)`
- `onManaBarSelect(...)`
- `onManaChange(...)`
- `onMarketBrowse(...)`
- `onMarketDetail(...)`
- `onMarketEnter(...)`
- `onMarketLeave(...)`
- `onMarketMessage(...)`
- `onMessage(...)`
- `onMiniWindowClose(...)`
- `onMissle(...)`
- `onModalDialog(...)`
- `onMountButtonClick(...)`
- `onMountSelect(...)`
- `onMouseGrabberRelease(...)`
- `onMouseMove(...)`
- `onMousePress(...)`
- `onMouseRelease(...)`
- `onMouseWheel(...)`
- `onMovementChange(...)`
- `onOfflineTrainingChange(...)`
- `onOpcode(...)`
- `onOpen(...)`
- `onOpenChannel(...)`
- `onOpenNpcTrade(...)`
- `onOpenOwnPrivateChannel(...)`
- `onOpenPrivateChannel(...)`
- `onOpenPvpSituationsChange(...)`
- `onOptionChange(...)`
- `onOutfitChange(...)`
- `onOutfitSelect(...)`
- `onOverlayGeometryChange(...)`
- `onPiecePriceChange(...)`
- `onPlayerGoods(...)`
- `onPlayerHealthChange(...)`
- `onPlayerInventoryChange(...)`
- `onPlayerPositionChange(...)`
- `onPositionChange(...)`
- `onPost(...)`
- `onPostProgress(...)`
- `onPresetSelect(...)`
- `onPreyActive(...)`
- `onPreyFreeRolls(...)`
- `onPreyInactive(...)`
- `onPreyLocked(...)`
- `onPreyPrice(...)`
- `onPreySelection(...)`
- `onPreyTimeLeft(...)`
- `onProfileChange(...)`
- `onProtocolError(...)`
- `onProxyList(...)`
- `onQuantityValueChange(...)`
- `onRecv(...)`
- `onRegenerationChange(...)`
- `onRemoveItem(...)`
- `onRemoveThing(...)`
- `onResourceBalance(...)`
- `onRootGeometryUpdate(...)`
- `onRuleViolationCancel(...)`
- `onRuleViolationChannel(...)`
- `onRuleViolationLock(...)`
- `onRuleViolationRemove(...)`
- `onSave(...)`
- `onScrollHeightChange(...)`
- `onScrollWidthChange(...)`
- `onSearchTextChange(...)`
- `onSelectBuyOffer(...)`
- `onSelectHotkeyLabel(...)`
- `onSelectMyBuyOffer(...)`
- `onSelectMySellOffer(...)`
- `onSelectReason(...)`
- `onSelectSellOffer(...)`
- `onSendAutomaticallyChange(...)`
- `onServerChange(...)`
- `onSessionKey(...)`
- `onSetChaseMode(...)`
- `onSetFightMode(...)`
- `onSetPVPMode(...)`
- `onSetSafeFight(...)`
- `onSetSafeFight2(...)`
- `onSetup(...)`
- `onShaderSelect(...)`
- `onShieldChange(...)`
- `onShowAllItemsChange(...)`
- `onShowAuraChange(...)`
- `onShowBarsChange(...)`
- `onShowFloorChange(...)`
- `onShowMountChange(...)`
- `onShowOutfitChange(...)`
- `onShowShaderChange(...)`
- `onShowWingsChange(...)`
- `onSkillButtonClick(...)`
- `onSkillChange(...)`
- `onSkullChange(...)`
- `onSoulChange(...)`
- `onSpeedChange(...)`
- `onSpellCooldown(...)`
- `onSpellGroupCooldown(...)`
- `onStaminaChange(...)`
- `onStatesChange(...)`
- `onStaticText(...)`
- `onStoreCategories(...)`
- `onStoreError(...)`
- `onStoreInit(...)`
- `onStoreOffers(...)`
- `onStorePurchase(...)`
- `onStoreTransactionHistory(...)`
- `onStyleApply(...)`
- `onTabChange(...)`
- `onTabClick(...)`
- `onTabDragEnter(...)`
- `onTabDragLeave(...)`
- `onTabDragMove(...)`
- `onTabMousePress(...)`
- `onTabMouseRelease(...)`
- `onTalk(...)`
- `onTeleport(...)`
- `onTextAreaUpdate(...)`
- `onTextChange(...)`
- `onTextMessage(...)`
- `onTibia12HTTPResult(...)`
- `onTotalCapacityChange(...)`
- `onTotalPriceChange(...)`
- `onTouchRelease(...)`
- `onTrackOptionChange(...)`
- `onTradeClick(...)`
- `onTradeTypeChange(...)`
- `onTradeWith(...)`
- `onTurn(...)`
- `onTypeChange(...)`
- `onUnjustifiedPointsChange(...)`
- `onUpdateNeeded(...)`
- `onUse(...)`
- `onUseWith(...)`
- `onValueChange(...)`
- `onVipListLabelMousePress(...)`
- `onVipListMousePress(...)`
- `onVipStateChange(...)`
- `onVisibilityChange(...)`
- `onWalk(...)`
- `onWalkFinish(...)`
- `onWidgetHoverChange(...)`
- `onWidgetKeyDown(...)`
- `onWidgetKeyPress(...)`
- `onWidgetKeyUp(...)`
- `onWidgetStyleApply(...)`
- `onWingsSelect(...)`
- `onWsClose(...)`
- `onWsError(...)`
- `onWsMessage(...)`
- `onWsOpen(...)`
- `onZoomChange(...)`

### 1.2. Kontekst `ctx.*`
_brak_

### 1.3. Moduły (eksporty `M.*`)
_brak_

### 1.4. Globalne funkcje (heur.)
- `abort()`
- `about_graphics()`
- `about_modules()`
- `about_version()`
- `abs()`
- `accept()`
- `action()`
- `add()`
- `alarm()`
- `api()`
- `append()`
- `assert()`
- `atan2()`
- `attack()`
- `back()`
- `band()`
- `bit()`
- `bonus()`
- `booleantonumber()`
- `button()`
- `buy()`
- `bxor()`
- `byte()`
- `callback()`
- `cancel()`
- `cast()`
- `cavebot()`
- `ceil()`
- `center()`
- `challenge()`
- `changed()`
- `char()`
- `check()`
- `chodzenie()`
- `clean()`
- `clear()`
- `clearbit()`
- `client()`
- `close()`
- `codepoint_to_utf8()`
- `collect()`
- `colortostring()`
- `comma_value()`
- `compare()`
- `concat()`
- `condition()`
- `config()`
- `connect()`
- `container()`
- `contains()`
- `copy()`
- `cos()`
- `countbrackets()`
- `create()`
- `create_set()`
- `date()`
- `debuff()`
- `decode()`
- `decode_error()`
- `decrement()`
- `decrypt()`
- `delay()`
- `destory()`
- `destroy()`
- `difftime()`
- `direction()`
- `directory()`
- `dirtostring()`
- `disable()`
- `disconnect()`
- `dismount()`
- `display()`
- `distance()`
- `dofile()`
- `dofiles()`
- `down()`
- `download()`
- `draw_debug_boxes()`
- `dump()`
- `edit()`
- `editor()`
- `elseif()`
- `empty()`
- `enable()`
- `encode()`
- `encode_nil()`
- `encode_number()`
- `encode_string()`
- `encode_table()`
- `encrypt()`
- `ends()`
- `enqueue()`
- `eof()`
- `equal()`
- `equals()`
- `error()`
- `escape_char()`
- `execute()`
- `exist()`
- `exists()`
- `exit()`
- `exp()`
- `explode()`
- `export()`
- `extends()`
- `extension()`
- `extract()`
- `fail()`
- `fatal()`
- `file()`
- `files()`
- `fill()`
- `find()`
- `findbyfield()`
- `findbykey()`
- `findkey()`
- `flash()`
- `float()`
- `floor()`
- `fmod()`
- `focus()`
- `follow()`
- `format()`
- `format_thousand()`
- `freecap()`
- `frexp()`
- `fromboolean()`
- `func()`
- `gcinfo()`
- `get()`
- `getfenv()`
- `getfsrcpath()`
- `getinfo()`
- `getmetatable()`
- `getn()`
- `getname()`
- `gmatch()`
- `gsub()`
- `haskey()`
- `helper()`
- `hide()`
- `hide_map()`
- `high()`
- `hotkey()`
- `hppercent()`
- `import()`
- `increment()`
- `info()`
- `information()`
- `init()`
- `insert()`
- `invalid()`
- `inventory()`
- `ipairs()`
- `iptostring()`
- `isinteger()`
- `issues()`
- `isu16()`
- `isu32()`
- `isu64()`
- `isu8()`
- `ldexp()`
- `left()`
- `len()`
- `level()`
- `line()`
- `lines()`
- `list()`
- `listen()`
- `load()`
- `loadasmodule()`
- `loadfile()`
- `loadstring()`
- `lock()`
- `log()`
- `login()`
- `logs()`
- `look()`
- `lose()`
- `lower()`
- `lvl()`
- `macro()`
- `macros()`
- `make_indent()`
- `makedecoder()`
- `makeencoder()`
- `makesingleton()`
- `mana()`
- `manapercent()`
- `match()`
- `matchcount()`
- `max()`
- `maximize()`
- `menu()`
- `merge()`
- `message()`
- `micros()`
- `millis()`
- `min()`
- `minimize()`
- `mod()`
- `module_loader()`
- `monitor()`
- `mount()`
- `move()`
- `music()`
- `name()`
- `new()`
- `newclass()`
- `next()`
- `next_char()`
- `nfiles()`
- `number()`
- `numbertoboolean()`
- `off()`
- `offline()`
- `opcode()`
- `open()`
- `order()`
- `pack()`
- `pairs()`
- `params()`
- `parse()`
- `parse_array()`
- `parse_literal()`
- `parse_number()`
- `parse_object()`
- `parse_string()`
- `parse_unicode_escape()`
- `pathfinder()`
- `pcall()`
- `pcolored()`
- `pdebug()`
- `permute()`
- `perror()`
- `pinfo()`
- `ping()`
- `place()`
- `play()`
- `pointtostring()`
- `popvalue()`
- `pos()`
- `position()`
- `post()`
- `postostring()`
- `posx()`
- `posy()`
- `posz()`
- `pow()`
- `preload()`
- `prev()`
- `process()`
- `proper()`
- `properly()`
- `protectedcall()`
- `pwarning()`
- `quit()`
- `raise()`
- `random()`
- `randomness()`
- `randomseed()`
- `range()`
- `rawget()`
- `read()`
- `recttostring()`
- `recursivecopy()`
- `recv()`
- `refresh()`
- `reload()`
- `remove()`
- `removevalue()`
- `rename()`
- `rep()`
- `report()`
- `require()`
- `reset()`
- `resize()`
- `resolvepath()`
- `restart()`
- `retries()`
- `reverse()`
- `rotate()`
- `rotation()`
- `round()`
- `rpairs()`
- `run()`
- `runinsandbox()`
- `sandboxed()`
- `save()`
- `say()`
- `scale()`
- `schedule()`
- `script()`
- `second()`
- `seconds()`
- `see()`
- `seek()`
- `select()`
- `selectivecopy()`
- `send()`
- `separatly()`
- `server()`
- `servidor()`
- `serwera()`
- `set()`
- `setbit()`
- `setfenv()`
- `setmetatable()`
- `setter()`
- `setup()`
- `shl()`
- `show()`
- `show_map()`
- `shr()`
- `signalcall()`
- `silent()`
- `sin()`
- `singlehotkey()`
- `size()`
- `sizetostring()`
- `slow()`
- `sort()`
- `split()`
- `splitlines()`
- `sqrt()`
- `stamina()`
- `starts()`
- `startup()`
- `stop()`
- `storage()`
- `sub()`
- `summons()`
- `table()`
- `talk()`
- `target()`
- `terminate()`
- `test()`
- `text()`
- `the()`
- `time()`
- `toboolean()`
- `tocolor()`
- `toggle()`
- `tonumber()`
- `topoint()`
- `torect()`
- `tosize()`
- `tostring()`
- `traceback()`
- `trim()`
- `turn()`
- `type()`
- `types()`
- `underscore()`
- `unexport()`
- `unload()`
- `unlock()`
- `unpack()`
- `update()`
- `upper()`
- `use()`
- `usewith()`
- `validate()`
- `value()`
- `values()`
- `voc()`
- `void()`
- `wait()`
- `walk()`
- `warn()`
- `warning()`
- `wrap()`
- `write()`

(otui)=
## 2. OTUI (layouty)

(otui-layoutsmobilestyles10-scrollbarsotui)=
### layouts/mobile/styles/10-scrollbars.otui
- `sliderButton` — **ScrollBarSlider**
- `valueLabel` — **ScrollBarValueLabel**
- `decrementButton` — **UIButton**
- `incrementButton` — **UIButton**
- `decrementButton` — **UIButton**
- `incrementButton` — **UIButton**

(otui-layoutsmobilestyles20-smallscrollbarotui)=
### layouts/mobile/styles/20-smallscrollbar.otui
- `decrementButton` — **UIButton**
- `incrementButton` — **UIButton**
- `sliderButton` — **UIButton**
- `valueLabel` — **Label**

(otui-layoutsmobilestyles30-miniwindowotui)=
### layouts/mobile/styles/30-miniwindow.otui
- `miniwindowTopBar` — **UIWidget**
- `closeButton` — **UIButton**
- `minimizeButton` — **UIButton**
- `lockButton` — **UIButton**
- `miniwindowScrollBar` — **VerticalScrollBar**
- `bottomResizeBorder` — **ResizeBorder**
- `contentsPanel` — **MiniWindowContents**

(otui-layoutsmobilestyles40-consoleotui)=
### layouts/mobile/styles/40-console.otui
- `consoleTab` — **ConsoleTabBarPanel**
- `consoleBuffer` — **ScrollablePanel**
- `consoleScrollBar` — **VerticalScrollBar**
- `toggleChat` — **CheckBox**
- `prevChannelButton` — **TabButton**
- `consoleTabBar` — **ConsoleTabBar**
- `nextChannelButton` — **TabButton**
- `closeChannelButton` — **TabButton**
- `clearChannelButton` — **TabButton**
- `channelsButton` — **TabButton**
- `ignoreButton` — **TabButton**
- `consoleContentPanel` — **Panel**
- `sayModeButton` — **TabButton**
- `consoleTextEdit` — **TextEdit**

(otui-layoutsmobilestyles40-inventoryotui)=
### layouts/mobile/styles/40-inventory.otui
- `slot1` — **HeadSlot**
- `slot4` — **BodySlot**
- `slot7` — **LegSlot**
- `slot8` — **FeetSlot**
- `slot2` — **NeckSlot**
- `slot6` — **LeftSlot**
- `slot9` — **FingerSlot**
- `slot3` — **BackSlot**
- `slot5` — **RightSlot**
- `slot10` — **AmmoSlot**
- `purseButton` — **PurseButton**
- `inventoryWindow` — **InventoryWindow**
- `inventoryPanel` — **Panel**
- `soulLabel` — **SoulCapLabel**
- `capLabel` — **SoulCapLabel**
- `conditionPanel` — **Panel**
- `fightOffensiveBox` — **FightOffensiveBox**
- `chaseModeBox` — **ChaseModeBox**
- `fightBalancedBox` — **FightBalancedBox**
- `safeFightBox` — **SafeFightBox**
- `fightDefensiveBox` — **FightDefensiveBox**
- `mountButton` — **MountButton**
- `buttonsPanel` — **Panel**
- `buttonPvp` — **UIButton**

(otui-layoutsretrostyles20-tabbarsotui)=
### layouts/retro/styles/20-tabbars.otui
- `buttonsPanel` — **TabBar**
- `buttonsPanel` — **TabBarVertical**
- `scrollBar` — **VerticalScrollBar**

(otui-layoutsretrostyles20-topmenuotui)=
### layouts/retro/styles/20-topmenu.otui
- `topMenu` — **TopMenu**
- `discord` — **UIWidget**
- `discordLabel` — **Label**
- `rightButtonsPanel` — **TopMenuButtonsPanel**
- `rightGameButtonsPanel` — **TopMenuButtonsPanel**
- `onlineLabel` — **Label**
- `leftButtonsPanel` — **TopMenuButtonsPanel**
- `leftGameButtonsPanel` — **TopMenuButtonsPanel**

(otui-layoutsretrostyles30-miniwindowotui)=
### layouts/retro/styles/30-miniwindow.otui
- `miniwindowTopBar` — **UIWidget**
- `closeButton` — **UIButton**
- `minimizeButton` — **UIButton**
- `lockButton` — **UIButton**
- `miniwindowScrollBar` — **VerticalScrollBar**
- `bottomResizeBorder` — **ResizeBorder**
- `contentsPanel` — **MiniWindowContents**
- `minimizeButton` — **UIButton**
- `miniwindowTopBar` — **UIWidget**
- `closeButton` — **UIButton**
- `miniwindowScrollBar` — **VerticalScrollBar**
- `bottomResizeBorder` — **ResizeBorder**

(otui-layoutsretrostyles40-consoleotui)=
### layouts/retro/styles/40-console.otui
- `consoleTab` — **ConsoleTabBarPanel**
- `consoleBuffer` — **ScrollablePanel**
- `consoleScrollBar` — **VerticalScrollBar**
- `toggleChat` — **CheckBox**
- `prevChannelButton` — **TabButton**
- `consoleTabBar` — **ConsoleTabBar**
- `nextChannelButton` — **TabButton**
- `closeChannelButton` — **TabButton**
- `clearChannelButton` — **TabButton**
- `channelsButton` — **TabButton**
- `ignoreButton` — **TabButton**
- `consoleContentPanel` — **Panel**
- `sayModeButton` — **TabButton**
- `separator` — **HorizontalSeparator**
- `consoleTextEdit` — **TextEdit**

(otui-layoutsretrostyles40-gamebuttonsotui)=
### layouts/retro/styles/40-gamebuttons.otui
- `buttons` — **Panel**

(otui-layoutsretrostyles40-healthinfootui)=
### layouts/retro/styles/40-healthinfo.otui
- `experienceBar` — **ExperienceBar**
- `soulLabel` — **SoulLabel**
- `capLabel` — **CapLabel**
- `healthOverlay` — **HealthOverlay**
- `topHealthBar` — **HealthBar**
- `topManaBar` — **ManaBar**
- `healthCircle` — **UIProgressBar**
- `healthCircleFront` — **UIProgressBar**
- `manaCircle` — **UIProgressBar**
- `manaCircleFront` — **UIProgressBar**
- `healthBar` — **HealthBar**
- `manaBar` — **ManaBar**
- `conditionPanel` — **ExperienceBar**

(otui-layoutsretrostyles40-inventoryotui)=
### layouts/retro/styles/40-inventory.otui
- `slot1` — **HeadSlot**
- `slot4` — **BodySlot**
- `slot7` — **LegSlot**
- `slot8` — **FeetSlot**
- `slot2` — **NeckSlot**
- `slot6` — **LeftSlot**
- `slot9` — **FingerSlot**
- `slot3` — **BackSlot**
- `slot5` — **RightSlot**
- `slot10` — **AmmoSlot**
- `purseButton` — **PurseButton**
- `inventoryWindow` — **InventoryWindow**
- `minimizeButton` — **UIButton**
- `inventoryPanel` — **Panel**
- `soulLabel` — **SoulCapLabel**
- `capLabel` — **SoulCapLabel**
- `conditionPanel` — **Panel**
- `fightOffensiveBox` — **FightOffensiveBox**
- `chaseModeBox` — **ChaseModeBox**
- `fightBalancedBox` — **FightBalancedBox**
- `safeFightBox` — **SafeFightBox**
- `fightDefensiveBox` — **FightDefensiveBox**
- `mountButton` — **MountButton**
- `buttonsPanel` — **Panel**
- `buttonPvp` — **UIButton**

(otui-layoutsretrostyles40-minimapotui)=
### layouts/retro/styles/40-minimap.otui
- `floorUpWidget` — **MinimapFloorUpButton**
- `floorDownWidget` — **MinimapFloorDownButton**
- `zoomInWidget` — **MinimapZoomInButton**
- `zoomOutWidget` — **MinimapZoomOutButton**
- `resetWidget` — **MinimapResetButton**
- `position` — **Label**
- `description` — **TextEdit**
- `flag0` — **MinimapFlagCheckBox**
- `flag1` — **MinimapFlagCheckBox**
- `flag2` — **MinimapFlagCheckBox**
- `flag3` — **MinimapFlagCheckBox**
- `flag4` — **MinimapFlagCheckBox**
- `flag5` — **MinimapFlagCheckBox**
- `flag6` — **MinimapFlagCheckBox**
- `flag7` — **MinimapFlagCheckBox**
- `flag8` — **MinimapFlagCheckBox**
- `flag9` — **MinimapFlagCheckBox**
- `flag10` — **MinimapFlagCheckBox**
- `flag11` — **MinimapFlagCheckBox**
- `flag12` — **MinimapFlagCheckBox**
- `flag13` — **MinimapFlagCheckBox**
- `flag14` — **MinimapFlagCheckBox**
- `flag15` — **MinimapFlagCheckBox**
- `flag16` — **MinimapFlagCheckBox**
- `flag17` — **MinimapFlagCheckBox**
- `flag18` — **MinimapFlagCheckBox**
- `flag19` — **MinimapFlagCheckBox**
- `okButton` — **Button**
- `cancelButton` — **Button**
- `minimap` — **Minimap**

(otui-layoutsretrostyles40-outfitwindowotui)=
### layouts/retro/styles/40-outfitwindow.otui
- `creature` — **UICreature**
- `title` — **Label**
- `rename` — **Panel**
- `input` — **TextEdit**
- `save` — **Button**
- `outfit` — **UICreature**
- `bar` — **Panel**
- `name` — **Label**
- `preview` — **MiniPanel**
- `options` — **Panel**
- `showFloor` — **FlatPanel**
- `check` — **CheckBox**
- `showOutfit` — **FlatPanel**
- `check` — **CheckBox**
- `showMount` — **FlatPanel**
- `check` — **CheckBox**
- `showWings` — **FlatPanel**
- `check` — **CheckBox**
- `showAura` — **FlatPanel**
- `check` — **CheckBox**
- `showShader` — **FlatPanel**
- `check` — **CheckBox**
- `showBars` — **FlatPanel**
- `check` — **CheckBox**
- `panel` — **FlatPanel**
- `floor` — **Panel**
- `creature` — **UICreature**
- `bars` — **Panel**
- `name` — **Label**
- `healthBar` — **Panel**
- `image` — **Panel**
- `manaBar` — **Panel**
- `image` — **Panel**
- `movement` — **ChaseModeBox**
- `configure` — **MiniPanel**
- `addon1` — **FlatPanel**
- `check` — **CheckBox**
- `addon2` — **FlatPanel**
- `check` — **CheckBox**
- `mount` — **FlatPanel**
- `check` — **CheckBox**
- `appearance` — **MiniPanel**
- `settings` — **ScrollablePanel**
- `preset` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `outfit` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `mount` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `wings` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `aura` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `shader` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `healthBar` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `manaBar` — **Panel**
- `check` — **CheckBox**
- `name` — **FlatPanel**
- `scrollbar` — **VerticalScrollBar**
- `colorMode` — **Panel**
- `head` — **ButtonBox**
- `colorBoxPanel` — **Panel**
- `presetButtons` — **MiniPanel**
- `listSearch` — **MiniPanel**
- `search` — **TextEdit**
- `presetsList` — **ScrollablePanel**
- `presetsScroll` — **VerticalScrollBar**
- `selectionList` — **ScrollablePanel**
- `selectionScroll` — **VerticalScrollBar**
- `separator` — **HorizontalSeparator**

(ws)=
## 3. WebSocket / JSON

### 3.1. Typy wiadomości (wykryte)
- `array`
- `boolean`
- `commonjs`
- `git`
- `github`
- `integer`
- `MIT`
- `module`
- `object`
- `opencollective`
- `OpenCollective`
- `string`
- `time-permitting`
- `value`

### 3.2. Schematy JSON ($id → plik)
- `https://raw.githubusercontent.com/DavidAnson/markdownlint/v0.38.0/schema/markdownlint-config-schema-strict.json` → `node_modules/markdownlint/schema/markdownlint-config-schema-strict.json`
- `https://raw.githubusercontent.com/DavidAnson/markdownlint/v0.38.0/schema/markdownlint-config-schema.json` → `node_modules/markdownlint/schema/markdownlint-config-schema.json`

(cpp-api)=
## 4. C++ (nagłówki)

```{toctree}
:maxdepth: 1

api/external/cpp/src_android_android_native_app_glue.md
api/external/cpp/src_client_animatedtext.md
api/external/cpp/src_client_animator.md
api/external/cpp/src_client_client.md
api/external/cpp/src_client_container.md
api/external/cpp/src_client_creature.md
api/external/cpp/src_client_creatures.md
api/external/cpp/src_client_effect.md
api/external/cpp/src_client_game.md
api/external/cpp/src_client_healthbars.md
api/external/cpp/src_client_houses.md
api/external/cpp/src_client_item.md
api/external/cpp/src_client_itemtype.md
api/external/cpp/src_client_lightview.md
api/external/cpp/src_client_localplayer.md
api/external/cpp/src_client_luavaluecasts_client.md
api/external/cpp/src_client_map.md
api/external/cpp/src_client_mapview.md
api/external/cpp/src_client_minimap.md
api/external/cpp/src_client_missile.md
api/external/cpp/src_client_outfit.md
api/external/cpp/src_client_player.md
api/external/cpp/src_client_position.md
api/external/cpp/src_client_protocolcodes.md
api/external/cpp/src_client_protocolgame.md
api/external/cpp/src_client_spritemanager.md
api/external/cpp/src_client_statictext.md
api/external/cpp/src_client_thing.md
api/external/cpp/src_client_thingstype.md
api/external/cpp/src_client_thingtype.md
api/external/cpp/src_client_thingtypemanager.md
api/external/cpp/src_client_tile.md
api/external/cpp/src_client_towns.md
api/external/cpp/src_client_uicreature.md
api/external/cpp/src_client_uigraph.md
api/external/cpp/src_client_uiitem.md
api/external/cpp/src_client_uimap.md
api/external/cpp/src_client_uimapanchorlayout.md
api/external/cpp/src_client_uiminimap.md
api/external/cpp/src_client_uiprogressrect.md
api/external/cpp/src_client_uisprite.md
api/external/cpp/src_client_walkmatrix.md
api/external/cpp/src_framework_core_adaptiverenderer.md
api/external/cpp/src_framework_core_application.md
api/external/cpp/src_framework_core_asyncdispatcher.md
api/external/cpp/src_framework_core_binarytree.md
api/external/cpp/src_framework_core_clock.md
api/external/cpp/src_framework_core_config.md
api/external/cpp/src_framework_core_configmanager.md
api/external/cpp/src_framework_core_consoleapplication.md
api/external/cpp/src_framework_core_event.md
api/external/cpp/src_framework_core_eventdispatcher.md
api/external/cpp/src_framework_core_filestream.md
api/external/cpp/src_framework_core_graphicalapplication.md
api/external/cpp/src_framework_core_inputevent.md
api/external/cpp/src_framework_core_logger.md
api/external/cpp/src_framework_core_module.md
api/external/cpp/src_framework_core_modulemanager.md
api/external/cpp/src_framework_core_resourcemanager.md
api/external/cpp/src_framework_core_scheduledevent.md
api/external/cpp/src_framework_core_timer.md
api/external/cpp/src_framework_global.md
api/external/cpp/src_framework_graphics_animatedtexture.md
api/external/cpp/src_framework_graphics_apngloader.md
api/external/cpp/src_framework_graphics_atlas.md
api/external/cpp/src_framework_graphics_bitmapfont.md
api/external/cpp/src_framework_graphics_cachedtext.md
api/external/cpp/src_framework_graphics_colorarray.md
api/external/cpp/src_framework_graphics_coordsbuffer.md
api/external/cpp/src_framework_graphics_deptharray.md
api/external/cpp/src_framework_graphics_drawcache.md
api/external/cpp/src_framework_graphics_drawqueue.md
api/external/cpp/src_framework_graphics_fontmanager.md
api/external/cpp/src_framework_graphics_framebuffer.md
api/external/cpp/src_framework_graphics_framebuffermanager.md
api/external/cpp/src_framework_graphics_graph.md
api/external/cpp/src_framework_graphics_graphics.md
api/external/cpp/src_framework_graphics_hardwarebuffer.md
api/external/cpp/src_framework_graphics_image.md
api/external/cpp/src_framework_graphics_painter.md
api/external/cpp/src_framework_graphics_paintershaderprogram.md
api/external/cpp/src_framework_graphics_shader.md
api/external/cpp/src_framework_graphics_shadermanager.md
api/external/cpp/src_framework_graphics_shaderprogram.md
api/external/cpp/src_framework_graphics_shaders_newshader.md
api/external/cpp/src_framework_graphics_shaders_outfits.md
api/external/cpp/src_framework_graphics_shaders_shadersources.md
api/external/cpp/src_framework_graphics_textrender.md
api/external/cpp/src_framework_graphics_texture.md
api/external/cpp/src_framework_graphics_texturemanager.md
api/external/cpp/src_framework_graphics_vertexarray.md
api/external/cpp/src_framework_http_http.md
api/external/cpp/src_framework_http_session.md
api/external/cpp/src_framework_http_websocket.md
api/external/cpp/src_framework_input_mouse.md
api/external/cpp/src_framework_luaengine_lbitlib.md
api/external/cpp/src_framework_luaengine_luabinder.md
api/external/cpp/src_framework_luaengine_luaexception.md
api/external/cpp/src_framework_luaengine_luainterface.md
api/external/cpp/src_framework_luaengine_luaobject.md
api/external/cpp/src_framework_luaengine_luavaluecasts.md
api/external/cpp/src_framework_net_connection.md
api/external/cpp/src_framework_net_inputmessage.md
api/external/cpp/src_framework_net_outputmessage.md
api/external/cpp/src_framework_net_packet_player.md
api/external/cpp/src_framework_net_packet_recorder.md
api/external/cpp/src_framework_net_protocol.md
api/external/cpp/src_framework_net_server.md
api/external/cpp/src_framework_otml_otmldocument.md
api/external/cpp/src_framework_otml_otmlemitter.md
api/external/cpp/src_framework_otml_otmlexception.md
api/external/cpp/src_framework_otml_otmlnode.md
api/external/cpp/src_framework_otml_otmlparser.md
api/external/cpp/src_framework_platform_androidwindow.md
api/external/cpp/src_framework_platform_crashhandler.md
api/external/cpp/src_framework_platform_platform.md
api/external/cpp/src_framework_platform_platformwindow.md
api/external/cpp/src_framework_platform_sdlwindow.md
api/external/cpp/src_framework_platform_win32window.md
api/external/cpp/src_framework_platform_x11window.md
api/external/cpp/src_framework_proxy_proxy.md
api/external/cpp/src_framework_proxy_proxy_client.md
api/external/cpp/src_framework_sound_combinedsoundsource.md
api/external/cpp/src_framework_sound_oggsoundfile.md
api/external/cpp/src_framework_sound_soundbuffer.md
api/external/cpp/src_framework_sound_soundchannel.md
api/external/cpp/src_framework_sound_soundfile.md
api/external/cpp/src_framework_sound_soundmanager.md
api/external/cpp/src_framework_sound_soundsource.md
api/external/cpp/src_framework_sound_streamsoundsource.md
api/external/cpp/src_framework_stdext_any.md
api/external/cpp/src_framework_stdext_cast.md
api/external/cpp/src_framework_stdext_demangle.md
api/external/cpp/src_framework_stdext_dynamic_storage.md
api/external/cpp/src_framework_stdext_exception.md
api/external/cpp/src_framework_stdext_fastrand.md
api/external/cpp/src_framework_stdext_format.md
api/external/cpp/src_framework_stdext_math.md
api/external/cpp/src_framework_stdext_net.md
api/external/cpp/src_framework_stdext_packed_any.md
api/external/cpp/src_framework_stdext_packed_storage.md
api/external/cpp/src_framework_stdext_shared_object.md
api/external/cpp/src_framework_stdext_string.md
api/external/cpp/src_framework_stdext_time.md
api/external/cpp/src_framework_stdext_uri.md
api/external/cpp/src_framework_ui_uianchorlayout.md
api/external/cpp/src_framework_ui_uiboxlayout.md
api/external/cpp/src_framework_ui_uigridlayout.md
api/external/cpp/src_framework_ui_uihorizontallayout.md
api/external/cpp/src_framework_ui_uilayout.md
api/external/cpp/src_framework_ui_uimanager.md
api/external/cpp/src_framework_ui_uitextedit.md
api/external/cpp/src_framework_ui_uitranslator.md
api/external/cpp/src_framework_ui_uiverticallayout.md
api/external/cpp/src_framework_ui_uiwidget.md
api/external/cpp/src_framework_util_color.md
api/external/cpp/src_framework_util_crypt.md
api/external/cpp/src_framework_util_databuffer.md
api/external/cpp/src_framework_util_extras.md
api/external/cpp/src_framework_util_framecounter.md
api/external/cpp/src_framework_util_pngunpacker.md
api/external/cpp/src_framework_util_point.md
api/external/cpp/src_framework_util_qrcodegen.md
api/external/cpp/src_framework_util_stats.md
api/external/cpp/src_framework_xml_tinystr.md
api/external/cpp/src_framework_xml_tinyxml.md
```

## 5. Uwaga
- Jeśli czegoś brakuje: doprecyzuj regexy w **tym skrypcie** (sekcje regexów).
- Dodaj JSON Schema do `schemas/ws/*.schema.json` — wygenerują się automatycznie jako strony w `docs/api/schemas`.
