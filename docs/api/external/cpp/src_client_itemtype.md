# src/client/itemtype.h

```cpp
public:
    ItemType();
```
```cpp
void unserialize(const BinaryTreePtr& node);
```
```cpp
void setServerId(uint16 serverId) { m_attribs.set(ItemTypeAttrServerId, serverId);
```
```cpp
uint16 getServerId() { return m_attribs.get<uint16>(ItemTypeAttrServerId);
```
```cpp
void setClientId(uint16 clientId) { m_attribs.set(ItemTypeAttrClientId, clientId);
```
```cpp
uint16 getClientId() { return m_attribs.get<uint16>(ItemTypeAttrClientId);
```
```cpp
void setCategory(ItemCategory category) { m_category = category; } ItemCategory getCategory() { return m_category; } void setName(const std::string& name) { m_attribs.set(ItemTypeAttrName, name);
```
```cpp
std::string getName() { return m_attribs.get<std::string>(ItemTypeAttrName);
```
```cpp
void setDesc(const std::string& desc) { m_attribs.set(ItemTypeAttrDesc, desc);
```
```cpp
std::string getDesc() { return m_attribs.get<std::string>(ItemTypeAttrDesc);
```
```cpp
bool isNull() { return m_null; } bool isWritable() { return m_attribs.get<bool>(ItemTypeAttrWritable);
```