# src/client/container.h

```cpp
protected: Container(int id, int capacity, const std::string& name, const ItemPtr& containerItem, bool hasParent, bool isUnlocked, bool hasPages, int containerSize, int firstIndex);
```
```cpp
public: ItemPtr getItem(int slot);
```
```cpp
ItemPtr findItemById(uint itemId, int subType);
```
```cpp
protected: void onOpen(const ContainerPtr& previousContainer);
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
private: void updateItemsPositions();
```
```cpp
std::deque<ItemPtr> getItems();
```
```cpp
int getItemsCount();
```
```cpp
Position getSlotPosition(int slot);
```
```cpp
int getId();
```
```cpp
int getCapacity();
```
```cpp
ItemPtr getContainerItem();
```
```cpp
std::string getName();
```
```cpp
bool hasParent();
```
```cpp
bool isClosed();
```
```cpp
bool isUnlocked();
```
```cpp
bool hasPages();
```
```cpp
int getSize();
```
```cpp
int getFirstIndex();
```