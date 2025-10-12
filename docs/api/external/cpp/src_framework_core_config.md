# src/framework/core/config.h

```cpp
public:
    Config();
```
```cpp
bool load(const std::string& file);
```
```cpp
bool unload();
```
```cpp
bool save();
```
```cpp
void clear();
```
```cpp
void setValue(const std::string& key, const std::string& value);
```
```cpp
void setList(const std::string& key, const std::vector<std::string>& list);
```
```cpp
std::string getValue(const std::string& key);
```
```cpp
std::vector<std::string> getList(const std::string& key);
```
```cpp
void setNode(const std::string& key, const OTMLNodePtr& node);
```
```cpp
void mergeNode(const std::string& key, const OTMLNodePtr& node);
```
```cpp
OTMLNodePtr getNode(const std::string& key);
```
```cpp
int getNodeSize(const std::string& key);
```
```cpp
bool exists(const std::string& key);
```
```cpp
void remove(const std::string& key);
```
```cpp
std::string getFileName();
```
```cpp
bool isLoaded();
```
```cpp
ConfigPtr asConfig() { return static_self_cast<Config>();
```