# src/client/uiitem.h

```cpp
public:
    UIItem();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setItemId(int id);
```
```cpp
void setItemCount(int count);
```
```cpp
void setItemSubType(int subType);
```
```cpp
void setItemVisible(bool visible) { m_itemVisible = visible; } void setItem(const ItemPtr& item);
```
```cpp
void setVirtual(bool virt) { m_virtual = virt; } void clearItem() { setItemId(0);
```
```cpp
void setShowCount(bool value) { m_showCount = value; } void setItemShader(const std::string& str);
```
```cpp
int getItemId() { return m_item ? m_item->getId() : 0; } int getItemCount() { return m_item ? m_item->getCount() : 0; } int getItemSubType() { return m_item ? m_item->getSubType() : 0; } int getItemCountOrSubType() { return m_item ? m_item->getCountOrSubType() : 0; } ItemPtr getItem() { return m_item; } bool isVirtual() { return m_virtual; } bool isItemVisible() { return m_itemVisible; } protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
void cacheCountText();
```