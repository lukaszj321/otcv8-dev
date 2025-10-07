# Modul: `game_npctrade`


BUY = 1

SELL = 2

CURRENCY = 'gold'

CURRENCY_DECIMAL = false

WEIGHT_UNIT = 'oz'

LAST_INVENTORY = 10

npcWindow = nil

itemsPanel = nil

radioTabs = nil

radioItems = nil

searchText = nil

setupPanel = nil

quantity = nil

quantityScroll = nil

idLabel = nil

nameLabel = nil

priceLabel = nil

moneyLabel = nil

weightDesc = nil

weightLabel = nil

capacityDesc = nil

capacityLabel = nil

tradeButton = nil

buyTab = nil

sellTab = nil

initialized = false

showWeight = true

buyWithBackpack = nil

ignoreCapacity = nil

ignoreEquipped = nil

showAllItems = nil

sellAllButton = nil

sellAllWithDelayButton = nil

playerFreeCapacity = 0

playerMoney = 0

tradeItems = {}

playerItems = {}

selectedItem = nil

cancelNextRelease = nil

sellAllWithDelayEvent = nil

function init()

  npcWindow = g_ui.displayUI('npctrade')

  npcWindow:setVisible(false)

  itemsPanel = npcWindow:recursiveGetChildById('itemsPanel')

  searchText = npcWindow:recursiveGetChildById('searchText')

  setupPanel = npcWindow:recursiveGetChildById('setupPanel')

  quantityScroll = setupPanel:getChildById('quantityScroll')

  idLabel = setupPanel:getChildById('id')

  nameLabel = setupPanel:getChildById('name')

  priceLabel = setupPanel:getChildById('price')

  moneyLabel = setupPanel:getChildById('money')

  weightDesc = setupPanel:getChildById('weightDesc')

  weightLabel = setupPanel:getChildById('weight')

  capacityDesc = setupPanel:getChildById('capacityDesc')

  capacityLabel = setupPanel:getChildById('capacity')

  tradeButton = npcWindow:recursiveGetChildById('tradeButton')

  buyWithBackpack = npcWindow:recursiveGetChildById('buyWithBackpack')

  ignoreCapacity = npcWindow:recursiveGetChildById('ignoreCapacity')

  ignoreEquipped = npcWindow:recursiveGetChildById('ignoreEquipped')

  showAllItems = npcWindow:recursiveGetChildById('showAllItems')

  sellAllButton = npcWindow:recursiveGetChildById('sellAllButton')

  sellAllWithDelayButton = npcWindow:recursiveGetChildById('sellAllWithDelayButton')

  buyTab = npcWindow:getChildById('buyTab')

  sellTab = npcWindow:getChildById('sellTab')

  radioTabs = UIRadioGroup.create()

  radioTabs:addWidget(buyTab)

  radioTabs:addWidget(sellTab)

  radioTabs:selectWidget(buyTab)

  radioTabs.onSelectionChange = onTradeTypeChange

  cancelNextRelease = false

  if g_game.isOnline() then

    playerFreeCapacity = g_game.getLocalPlayer():getFreeCapacity()

  end

  connect(g_game, { onGameEnd = hide,

                    onOpenNpcTrade = onOpenNpcTrade,

                    onCloseNpcTrade = onCloseNpcTrade,

                    onPlayerGoods = onPlayerGoods } )

  connect(LocalPlayer, { onFreeCapacityChange = onFreeCapacityChange,

                         onInventoryChange = onInventoryChange } )

  initialized = true

end

function terminate()

  initialized = false

  npcWindow:destroy()

  removeEvent(sellAllWithDelayEvent)

  disconnect(g_game, {  onGameEnd = hide,

                        onOpenNpcTrade = onOpenNpcTrade,

                        onCloseNpcTrade = onCloseNpcTrade,

                        onPlayerGoods = onPlayerGoods } )

  disconnect(LocalPlayer, { onFreeCapacityChange = onFreeCapacityChange,

                            onInventoryChange = onInventoryChange } )

end

function show()

  if g_game.isOnline() then

    if #tradeItems[BUY] > 0 then

      radioTabs:selectWidget(buyTab)

    else

      radioTabs:selectWidget(sellTab)

    end

    npcWindow:show()

    npcWindow:raise()

    npcWindow:focus()

  end

end

function hide()

  removeEvent(sellAllWithDelayEvent)

  npcWindow:hide()

  local layout = itemsPanel:getLayout()

  layout:disableUpdates()

  clearSelectedItem()

  searchText:clearText()

  setupPanel:disable()

  itemsPanel:destroyChildren()

  if radioItems then

    radioItems:destroy()

    radioItems = nil

  end

  layout:enableUpdates()

  layout:update()  

end

function onItemBoxChecked(widget)

  if widget:isChecked() then

    local item = widget.item

    selectedItem = item

    refreshItem(item)

    tradeButton:enable()

    if getCurrentTradeType() == SELL then

      quantityScroll:setValue(quantityScroll:getMaximum())

    end

  end

end

function onQuantityValueChange(quantity)

  if selectedItem then

    weightLabel:setText(string.format('%.2f', selectedItem.weight*quantity) .. ' ' .. WEIGHT_UNIT)

    priceLabel:setText(formatCurrency(getItemPrice(selectedItem)))

  end

end

function onTradeTypeChange(radioTabs, selected, deselected)

  tradeButton:setText(selected:getText())

  selected:setOn(true)

  deselected:setOn(false)

  local currentTradeType = getCurrentTradeType()

  buyWithBackpack:setVisible(currentTradeType == BUY)

  ignoreCapacity:setVisible(currentTradeType == BUY)

  ignoreEquipped:setVisible(currentTradeType == SELL)

  showAllItems:setVisible(currentTradeType == SELL)

  sellAllButton:setVisible(currentTradeType == SELL)

  sellAllWithDelayButton:setVisible(currentTradeType == SELL)

  refreshTradeItems()

  refreshPlayerGoods()

end

function onTradeClick()

  removeEvent(sellAllWithDelayEvent)

  if getCurrentTradeType() == BUY then

    g_game.buyItem(selectedItem.ptr, quantityScroll:getValue(), ignoreCapacity:isChecked(), buyWithBackpack:isChecked())

  else

    g_game.sellItem(selectedItem.ptr, quantityScroll:getValue(), ignoreEquipped:isChecked())

  end

end

function onSearchTextChange()

  refreshPlayerGoods()

end

function itemPopup(self, mousePosition, mouseButton)

  if cancelNextRelease then

    cancelNextRelease = false

    return false

  end

  if mouseButton == MouseRightButton then

    local menu = g_ui.createWidget('PopupMenu')

    menu:setGameMenu(true)

    menu:addOption(tr('Look'), function() return g_game.inspectNpcTrade(self:getItem()) end)

    menu:display(mousePosition)

    return true

  elseif ((g_mouse.isPressed(MouseLeftButton) and mouseButton == MouseRightButton)

    or (g_mouse.isPressed(MouseRightButton) and mouseButton == MouseLeftButton)) then

    cancelNextRelease = true

    g_game.inspectNpcTrade(self:getItem())

    return true

  end

  return false

end

function onBuyWithBackpackChange()

  if selectedItem then

    refreshItem(selectedItem)

  end

end

function onIgnoreCapacityChange()

  refreshPlayerGoods()

end

function onIgnoreEquippedChange()

  refreshPlayerGoods()

end

function onShowAllItemsChange()

  refreshPlayerGoods()

end

function setCurrency(currency, decimal)

  CURRENCY = currency

  CURRENCY_DECIMAL = decimal

end

function setShowWeight(state)

  showWeight = state

  weightDesc:setVisible(state)

  weightLabel:setVisible(state)

end

function setShowYourCapacity(state)

  capacityDesc:setVisible(state)

  capacityLabel:setVisible(state)

  ignoreCapacity:setVisible(state)

end

function clearSelectedItem()

  idLabel:clearText()

  nameLabel:clearText()

  weightLabel:clearText()

  priceLabel:clearText()

  tradeButton:disable()

  quantityScroll:setMinimum(0)

  quantityScroll:setMaximum(0)

  if selectedItem then

    radioItems:selectWidget(nil)

    selectedItem = nil

  end

end

function getCurrentTradeType()

  if tradeButton:getText() == tr('Buy') then

    return BUY

  else

    return SELL

  end

end

function getItemPrice(item, single)

  local amount = 1

  local single = single or false

  if not single then

    amount = quantityScroll:getValue()

  end

  if getCurrentTradeType() == BUY then

    if buyWithBackpack:isChecked() then

      if item.ptr:isStackable() then

          return item.price*amount + 20

      else

        return item.price*amount + math.ceil(amount/20)*20

      end

    end

  end

  return item.price*amount

end

function getSellQuantity(item)

  if not item or not playerItems[item:getId()] then return 0 end

  local removeAmount = 0

  if ignoreEquipped:isChecked() then

    local localPlayer = g_game.getLocalPlayer()

    for i=1,LAST_INVENTORY do

      local inventoryItem = localPlayer:getInventoryItem(i)

      if inventoryItem and inventoryItem:getId() == item:getId() then

        removeAmount = removeAmount + inventoryItem:getCount()

      end

    end

  end

  return playerItems[item:getId()] - removeAmount

end

function canTradeItem(item)

  if getCurrentTradeType() == BUY then

    return (ignoreCapacity:isChecked() or (not ignoreCapacity:isChecked() and playerFreeCapacity >= item.weight)) and playerMoney >= getItemPrice(item, true)

  else

    return getSellQuantity(item.ptr) > 0

  end

end

function refreshItem(item)

  idLabel:setText(item.ptr:getId())

  nameLabel:setText(item.name)

  weightLabel:setText(string.format('%.2f', item.weight) .. ' ' .. WEIGHT_UNIT)

  priceLabel:setText(formatCurrency(getItemPrice(item)))

  if getCurrentTradeType() == BUY then

    local capacityMaxCount = math.floor(playerFreeCapacity / item.weight)

    if ignoreCapacity:isChecked() then

      capacityMaxCount = 65535

    end

    local priceMaxCount = math.floor(playerMoney / getItemPrice(item, true))

    local finalCount = math.max(0, math.min(getMaxAmount(), math.min(priceMaxCount, capacityMaxCount)))

    quantityScroll:setMinimum(1)

    quantityScroll:setMaximum(finalCount)

  else

    quantityScroll:setMinimum(1)

    quantityScroll:setMaximum(math.max(0, math.min(getMaxAmount(), getSellQuantity(item.ptr))))

  end

  setupPanel:enable()

end

function refreshTradeItems()

  local layout = itemsPanel:getLayout()

  layout:disableUpdates()

  clearSelectedItem()

  searchText:clearText()

  setupPanel:disable()

  itemsPanel:destroyChildren()

  if radioItems then

    radioItems:destroy()

  end

  radioItems = UIRadioGroup.create()

  local currentTradeItems = tradeItems[getCurrentTradeType()]

  for key,item in pairs(currentTradeItems) do

    local itemBox = g_ui.createWidget('NPCItemBox', itemsPanel)

    itemBox.item = item

    local text = ''

    local name = item.name

    text = text .. name

    if showWeight then

      local weight = string.format('%.2f', item.weight) .. ' ' .. WEIGHT_UNIT

      text = text .. '\n' .. weight

    end

    local price = formatCurrency(item.price)

    text = text .. '\n' .. price

    itemBox:setText(text)

    local itemWidget = itemBox:getChildById('item')

    itemWidget:setItem(item.ptr)

    itemWidget.onMouseRelease = itemPopup

    radioItems:addWidget(itemBox)

  end

  layout:enableUpdates()

  layout:update()

end

function refreshPlayerGoods()

  if not initialized then return end

  checkSellAllTooltip()

  moneyLabel:setText(formatCurrency(playerMoney))

  capacityLabel:setText(string.format('%.2f', playerFreeCapacity) .. ' ' .. WEIGHT_UNIT)

  local currentTradeType = getCurrentTradeType()

  local searchFilter = searchText:getText():lower()

  local foundSelectedItem = false

  local items = itemsPanel:getChildCount()

  for i=1,items do

    local itemWidget = itemsPanel:getChildByIndex(i)

    local item = itemWidget.item

    local canTrade = canTradeItem(item)

    itemWidget:setOn(canTrade)

    itemWidget:setEnabled(canTrade)

    local searchCondition = (searchFilter == '') or (searchFilter ~= '' and string.find(item.name:lower(), searchFilter) ~= nil)

    local showAllItemsCondition = (currentTradeType == BUY) or (showAllItems:isChecked()) or (currentTradeType == SELL and not showAllItems:isChecked() and canTrade)

    itemWidget:setVisible(searchCondition and showAllItemsCondition)

    if selectedItem == item and itemWidget:isEnabled() and itemWidget:isVisible() then

      foundSelectedItem = true

    end

  end

  if not foundSelectedItem then

    clearSelectedItem()

  end

  if selectedItem then

    refreshItem(selectedItem)

  end

end

function onOpenNpcTrade(items)

  tradeItems[BUY] = {}

  tradeItems[SELL] = {}

  for key,item in pairs(items) do

    if item[4] > 0 then

      local newItem = {}

      newItem.ptr = item[1]

      newItem.name = item[2]

      newItem.weight = item[3] / 100

      newItem.price = item[4]

      table.insert(tradeItems[BUY], newItem)

    end

    if item[5] > 0 then

      local newItem = {}

      newItem.ptr = item[1]

      newItem.name = item[2]

      newItem.weight = item[3] / 100

      newItem.price = item[5]

      table.insert(tradeItems[SELL], newItem)

    end

  end

  refreshTradeItems()

  addEvent(show) -- player goods has not been parsed yet

end

function closeNpcTrade()

  g_game.closeNpcTrade()

  addEvent(hide)

end

function onCloseNpcTrade()

  addEvent(hide)

end

function onPlayerGoods(money, items)

  playerMoney = money

  playerItems = {}

  for key,item in pairs(items) do

    local id = item[1]:getId()

    if not playerItems[id] then

      playerItems[id] = item[2]

    else

      playerItems[id] = playerItems[id] + item[2]

    end

  end

  refreshPlayerGoods()

end

function onFreeCapacityChange(localPlayer, freeCapacity, oldFreeCapacity)

  playerFreeCapacity = freeCapacity

  if npcWindow:isVisible() then

    refreshPlayerGoods()

  end

end

function onInventoryChange(inventory, item, oldItem)

  refreshPlayerGoods()

end

function getTradeItemData(id, type)

  if table.empty(tradeItems[type]) then

    return false

  end

  if type then

    for key,item in pairs(tradeItems[type]) do

      if item.ptr and item.ptr:getId() == id then

        return item

      end

    end

  else

    for _,items in pairs(tradeItems) do

      for key,item in pairs(items) do

        if item.ptr and item.ptr:getId() == id then

          return item

        end

      end

    end

  end

  return false

end

function checkSellAllTooltip()

  sellAllButton:setEnabled(true)

  sellAllButton:removeTooltip()

  sellAllWithDelayButton:setEnabled(true)

  sellAllWithDelayButton:removeTooltip()

  local total = 0

  local info = ''

  local first = true

  for key, amount in pairs(playerItems) do

    local data = getTradeItemData(key, SELL)

    if data then

      amount = getSellQuantity(data.ptr)

      if amount > 0 then

        if data and amount > 0 then

          info = info..(not first and "\n" or "")..

                 amount.." "..

                 data.name.." ("..

                 data.price*amount.." gold)"

          total = total+(data.price*amount)

          if first then first = false end

        end

      end

    end

  end

  if info ~= '' then

    info = info.."\nTotal: "..total.." gold"

    sellAllButton:setTooltip(info)

    sellAllWithDelayButton:setTooltip(info)

  else

    sellAllButton:setEnabled(false)

    sellAllWithDelayButton:setEnabled(false)

  end

end

function formatCurrency(amount)

  if CURRENCY_DECIMAL then

    return string.format("%.02f", amount/100.0) .. ' ' .. CURRENCY

  else

    return amount .. ' ' .. CURRENCY

  end

end

function getMaxAmount()

  if getCurrentTradeType() == SELL and g_game.getFeature(GameDoubleShopSellAmount) then

    return 10000

  end

  return 100

end

function sellAll(delayed, exceptions)

  -- backward support

  if type(delayed) == "table" then

    exceptions = delayed

    delayed = false

  end

  exceptions = exceptions or {}

  removeEvent(sellAllWithDelayEvent)

  local queue = {}

  for _,entry in ipairs(tradeItems[SELL]) do

    local id = entry.ptr:getId()

    if not table.find(exceptions, id) then

      local sellQuantity = getSellQuantity(entry.ptr)

      while sellQuantity > 0 do

        local maxAmount = math.min(sellQuantity, getMaxAmount())

        if delayed then

          g_game.sellItem(entry.ptr, maxAmount, ignoreEquipped:isChecked())

          sellAllWithDelayEvent = scheduleEvent(function() sellAll(true) end, 1100)

          return

        end

        table.insert(queue, {entry.ptr, maxAmount, ignoreEquipped:isChecked()})

        sellQuantity = sellQuantity - maxAmount

      end

    end

  end

  for _, entry in ipairs(queue) do

    g_game.sellItem(entry[1], entry[2], entry[3])

  end

end

```

---
# npctrade.otmod


Module

  name: game_npctrade

  description: NPC trade interface

  author: andrefaramir, baxnie

  website: https://github.com/edubart/otclient

  sandboxed: true

  scripts: [ npctrade ]

  @onLoad: init()

  @onUnload: terminate()

```

---
# npctrade.otui


NPCOfferLabel < Label

  anchors.left: prev.right

  anchors.top: prev.top

  margin-left: 5

  text-auto-resize: true

NPCItemBox < UICheckBox

  border-width: 1

  border-color: #000000

  color: #aaaaaa

  text-align: center

  text-offset: 0 30

  @onCheckChange: modules.game_npctrade.onItemBoxChecked(self)

  Item

    id: item

    phantom: true

    anchors.top: parent.top

    anchors.horizontalCenter: parent.horizontalCenter

    image-color: #ffffffff

    margin-top: 3

  $checked on:

    border-color: #ffffff

  $!checked:

    border-color: #000000

  $!on:

    image-color: #ffffff88

    color: #aaaaaa88

MainWindow

  id: npcWindow

  !text: tr('NPC Trade')

  size: 550 460

  @onEscape: modules.game_npctrade.closeNpcTrade()

  $mobile:

    size: 550 360

  TabButton

    id: buyTab

    !tooltip: tr("List of items that you're able to buy")

    !text: tr('Buy')

    checked: true

    on: true

    anchors.left: parent.left

    anchors.right: parent.horizontalCenter

    anchors.top: parent.top

    margin-top: 0

  TabButton

    id: sellTab

    !tooltip: tr("List of items that you're able to sell")

    !text: tr('Sell')

    anchors.left: parent.horizontalCenter

    anchors.right: parent.right

    anchors.top: parent.top

  FlatPanel

    height: 250

    anchors.left: parent.left

    anchors.right: parent.right

    anchors.top: prev.bottom

    margin-top: 5

    $mobile:

      height: 150

    VerticalScrollBar

      id: itemsPanelListScrollBar

      anchors.top: parent.top

      anchors.bottom: parent.bottom

      anchors.right: parent.right

      step: 24

      pixels-scroll: true

    ScrollablePanel

      id: itemsPanel

      height: 200

      anchors.left: parent.left

      anchors.right: prev.left

      anchors.top: parent.top

      anchors.bottom: parent.bottom

      vertical-scrollbar: itemsPanelListScrollBar

      margin-left: 5

      margin-right: 5

      layout:

        type: grid

        cell-size: 160 90

        flow: true

        auto-spacing: true

  FlatPanel

    id: setupPanel

    height: 105

    enabled: false

    anchors.left: parent.left

    anchors.right: parent.horizontalCenter

    anchors.top: prev.bottom

    margin-top: 5

    margin-right: 5

    image-color: #ffffff88

    Label

      !text: tr('Name') .. ':'

      anchors.left: parent.left

      anchors.top: parent.top

      margin-top: 5

      margin-left: 5

      width: 85

    NPCOfferLabel

      id: name

    Label

      !text: tr('Id') .. ':'

      anchors.left: parent.left

      anchors.top: parent.top

      margin-top: 5

      margin-left: 5

      margin-left: 195

      width: 15

    NPCOfferLabel

      id: id

    Label

      !text: tr('Price') .. ':'

      anchors.left: parent.left

      anchors.top: prev.bottom

      margin-top: 3

      margin-left: 5

      width: 85

    NPCOfferLabel

      id: price

    Label

      !text: tr('Your Money') .. ':'

      anchors.left: parent.left

      anchors.top: prev.bottom

      margin-top: 3

      margin-left: 5

      width: 85

    NPCOfferLabel

      id: money

    Label

      id: weightDesc

      !text: tr('Weight') .. ':'

      anchors.left: parent.left

      anchors.top: prev.bottom

      margin-top: 3

      margin-left: 5

      width: 85

    NPCOfferLabel

      id: weight

    Label

      id: capacityDesc

      !text: tr('Your Capacity') .. ':'

      anchors.left: parent.left

      anchors.top: prev.bottom

      margin-top: 3

      margin-left: 5

      width: 85

    NPCOfferLabel

      id: capacity

    HorizontalScrollBar

      id: quantityScroll

      anchors.left: parent.left

      anchors.right: parent.right

      anchors.top: prev.bottom

      margin-top: 3

      margin-left: 5

      margin-right: 5

      show-value: true

      minimum: 1

      maximum: 100

      step: 1

      @onValueChange: modules.game_npctrade.onQuantityValueChange(self:getValue())

  FlatPanel

    id: buyOptions

    height: 80

    anchors.top: prev.top

    anchors.left: parent.horizontalCenter

    anchors.right: parent.right

    margin-left: 5

    image-color: #ffffff88

    Label

      id: searchLabel

      !text: tr('Search') .. ':'

      anchors.left: parent.left

      anchors.top: parent.top

      text-auto-resize: true

      margin-top: 7

      margin-left: 5

    TextEdit

      id: searchText

      anchors.left: prev.right

      anchors.top: prev.top

      anchors.right: parent.right

      margin-top: -2

      margin-left: 5

      margin-right: 5

      @onTextChange: modules.game_npctrade.onSearchTextChange()

    CheckBox

      id: buyWithBackpack

      !text: tr('Buy with backpack')

      anchors.top: searchText.bottom

      anchors.left: parent.left

      anchors.right: parent.right

      margin-left: 5

      margin-top: 3

      @onCheckChange: modules.game_npctrade.onBuyWithBackpackChange()

    CheckBox

      id: ignoreCapacity

      !text: tr('Ignore capacity')

      anchors.top: prev.bottom

      anchors.left: parent.left

      anchors.right: parent.right

      margin-left: 5

      margin-top: 3

      @onCheckChange: modules.game_npctrade.onIgnoreCapacityChange()

    CheckBox

      id: ignoreEquipped

      !text: tr('Ignore equipped')

      anchors.top: searchText.bottom

      anchors.left: parent.left

      anchors.right: parent.right

      margin-left: 5

      margin-top: 3

      visible: false

      checked: true

      @onCheckChange: modules.game_npctrade.onIgnoreEquippedChange()

    CheckBox

      id: showAllItems

      !text: tr('Show all items')

      anchors.top: prev.bottom

      anchors.left: parent.left

      anchors.right: parent.right

      margin-left: 5

      margin-top: 3

      visible: false

      checked: true

      @onCheckChange: modules.game_npctrade.onShowAllItemsChange()

  Button

    id: sellAllWithDelayButton

    !text: tr('Sell all with delay')

    width: 128

    anchors.right: next.left

    anchors.bottom: parent.bottom

    margin-right: 10

    visible: false

    @onClick: modules.game_npctrade.sellAll(true)

  Button

    id: sellAllButton

    !text: tr('Sell all')

    width: 64

    anchors.right: next.left

    anchors.bottom: parent.bottom

    margin-right: 10

    visible: false

    @onClick: modules.game_npctrade.sellAll()

  Button

    id: tradeButton

    !text: tr('Buy')

    width: 64

    anchors.right: next.left

    anchors.bottom: parent.bottom

    margin-right: 10

    @onClick: modules.game_npctrade.onTradeClick()

  Button

    !text: tr('Close')

    width: 64

    anchors.right: parent.right

    anchors.bottom: parent.bottom

    @onClick: modules.game_npctrade.closeNpcTrade()

```

---
