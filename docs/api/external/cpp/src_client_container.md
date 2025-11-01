---
title: "src/client/container.h"
source_file: "src/client/container.h"
generated_at: "2025-11-01T08:45:15.275Z"
doc_type: "cpp_api"
---

# src/client/container.h

(container)=
## `Container`

**Signature:**
```cpp
protected: Container(int id, int capacity, const std::string& name, const ItemPtr& containerItem, bool hasParent, bool isUnlocked, bool hasPages, int containerSize, int firstIndex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |
| `int` | `capacity` | - |
| `const std::string&` | `name` | - |
| `const ItemPtr&` | `containerItem` | - |
| `bool` | `hasParent` | - |
| `bool` | `isUnlocked` | - |
| `bool` | `hasPages` | - |
| `int` | `containerSize` | - |
| `int` | `firstIndex` | - |

---

(getitem)=
## `getItem`

**Signature:**
```cpp
public: ItemPtr getItem(int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |

**Returns:**
- `ItemPtr`

---

(finditembyid)=
## `findItemById`

**Signature:**
```cpp
ItemPtr findItemById(uint itemId, int subType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `itemId` | - |
| `int` | `subType` | - |

**Returns:**
- `ItemPtr`

---

(onopen)=
## `onOpen`

**Signature:**
```cpp
protected: void onOpen(const ContainerPtr& previousContainer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ContainerPtr&` | `previousContainer` | - |

---

(onclose)=
## `onClose`

**Signature:**
```cpp
void onClose();
```

---

(onadditem)=
## `onAddItem`

**Signature:**
```cpp
void onAddItem(const ItemPtr& item, int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `item` | - |
| `int` | `slot` | - |

---

(onadditems)=
## `onAddItems`

**Signature:**
```cpp
void onAddItems(const std::vector<ItemPtr>& items);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;ItemPtr&gt;&` | `items` | - |

---

(onupdateitem)=
## `onUpdateItem`

**Signature:**
```cpp
void onUpdateItem(int slot, const ItemPtr& item);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |
| `const ItemPtr&` | `item` | - |

---

(onremoveitem)=
## `onRemoveItem`

**Signature:**
```cpp
void onRemoveItem(int slot, const ItemPtr& lastItem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |
| `const ItemPtr&` | `lastItem` | - |

---

(updateitemspositions)=
## `updateItemsPositions`

**Signature:**
```cpp
private: void updateItemsPositions();
```

---

(getitems)=
## `getItems`

**Signature:**
```cpp
std::deque<ItemPtr> getItems();
```

**Returns:**
- `std::deque&lt;ItemPtr&gt;`

---

(getitemscount)=
## `getItemsCount`

**Signature:**
```cpp
int getItemsCount();
```

**Returns:**
- `int`

---

(getslotposition)=
## `getSlotPosition`

**Signature:**
```cpp
Position getSlotPosition(int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |

**Returns:**
- `Position`

---

(getid)=
## `getId`

**Signature:**
```cpp
int getId();
```

**Returns:**
- `int`

---

(getcapacity)=
## `getCapacity`

**Signature:**
```cpp
int getCapacity();
```

**Returns:**
- `int`

---

(getcontaineritem)=
## `getContainerItem`

**Signature:**
```cpp
ItemPtr getContainerItem();
```

**Returns:**
- `ItemPtr`

---

(getname)=
## `getName`

**Signature:**
```cpp
std::string getName();
```

**Returns:**
- `std::string`

---

(hasparent)=
## `hasParent`

**Signature:**
```cpp
bool hasParent();
```

**Returns:**
- `bool`

---

(isclosed)=
## `isClosed`

**Signature:**
```cpp
bool isClosed();
```

**Returns:**
- `bool`

---

(isunlocked)=
## `isUnlocked`

**Signature:**
```cpp
bool isUnlocked();
```

**Returns:**
- `bool`

---

(haspages)=
## `hasPages`

**Signature:**
```cpp
bool hasPages();
```

**Returns:**
- `bool`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
int getSize();
```

**Returns:**
- `int`

---

(getfirstindex)=
## `getFirstIndex`

**Signature:**
```cpp
int getFirstIndex();
```

**Returns:**
- `int`

---
