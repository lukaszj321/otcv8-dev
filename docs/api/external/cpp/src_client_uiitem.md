# src/client/uiitem.h

```cpp
public: UIItem();
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
void setItem(const ItemPtr& item);
```
```cpp
void setItemShader(const std::string& str);
```
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
void cacheCountText();
```
```cpp
void setItemVisible(bool visible);
```
```cpp
void setVirtual(bool virt);
```
```cpp
void clearItem();
```
```cpp
void setShowCount(bool value);
```
```cpp
int getItemId();
```
```cpp
int getItemCount();
```
```cpp
int getItemSubType();
```
```cpp
int getItemCountOrSubType();
```
```cpp
ItemPtr getItem();
```
```cpp
bool isVirtual();
```
```cpp
bool isItemVisible();
```