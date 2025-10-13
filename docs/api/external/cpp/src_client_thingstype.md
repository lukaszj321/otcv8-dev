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
uint32 getSignature();
```
```cpp
bool isLoaded();
```
```cpp
uint16 getFirstItemId();
```
```cpp
uint16 getMaxItemid();
```
```cpp
bool isValidItemId(int id);
```