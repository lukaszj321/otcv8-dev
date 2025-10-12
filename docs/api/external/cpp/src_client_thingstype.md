# src/client/thingstype.h

```cpp
bool load(const std::string& file);
```
```cpp
void unload();
```
```cpp
bool parseThingType(const FileStreamPtr& fin, ThingType& thingType);
```
```cpp
uint32 getSignature() { return m_signature; } bool isLoaded() { return m_loaded; } uint16 getFirstItemId() { return 100; } uint16 getMaxItemid() { return m_things[Item].size() + 99; } bool isValidItemId(int id) { return id >= getFirstItemId() && id <= getMaxItemid();
```