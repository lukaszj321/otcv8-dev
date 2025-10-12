# src/client/container.h

```cpp
protected:
    Container(int id, int capacity, const std::string& name, const ItemPtr& containerItem, bool hasParent, bool isUnlocked, bool hasPages, int containerSize, int firstIndex);
```
```cpp
public:
    ItemPtr getItem(int slot);
```
```cpp
std::deque<ItemPtr> getItems() { return m_items; } int getItemsCount() { return m_items.size();
```
```cpp
Position getSlotPosition(int slot) { return Position(0xffff, m_id | 0x40, slot);
```
```cpp
int getId() { return m_id; } int getCapacity() { return m_capacity; } ItemPtr getContainerItem() { return m_containerItem; } std::string getName() { return m_name; } bool hasParent() { return m_hasParent; } bool isClosed() { return m_closed; } bool isUnlocked() { return m_unlocked; } bool hasPages() { return m_hasPages; } int getSize() { return m_size; } int getFirstIndex() { return m_firstIndex; } ItemPtr findItemById(uint itemId, int subType);
```
```cpp
protected:
    void onOpen(const ContainerPtr& previousContainer);
```
```cpp
void onClose();
```
```cpp
void onAddItem(const ItemPtr& item, int slot);
```
```cpp
void onAddItems(const std::vector<ItemPtr>& items);
```
```cpp
void onUpdateItem(int slot, const ItemPtr& item);
```
```cpp
void onRemoveItem(int slot, const ItemPtr& lastItem);
```
```cpp
private:
    void updateItemsPositions();
```