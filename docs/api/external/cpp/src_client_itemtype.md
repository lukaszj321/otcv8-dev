# src/client/itemtype.h

```cpp
public: ItemType();
```
```cpp
void unserialize(const BinaryTreePtr& node);
```
```cpp
void setServerId(uint16 serverId);
```
```cpp
uint16 getServerId();
```
```cpp
void setClientId(uint16 clientId);
```
```cpp
uint16 getClientId();
```
```cpp
void setCategory(ItemCategory category);
```
```cpp
ItemCategory getCategory();
```
```cpp
void setName(const std::string& name);
```
```cpp
std::string getName();
```
```cpp
void setDesc(const std::string& desc);
```
```cpp
std::string getDesc();
```
```cpp
bool isNull();
```
```cpp
bool isWritable();
```