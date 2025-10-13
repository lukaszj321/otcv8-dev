# src/framework/core/configmanager.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
ConfigPtr getSettings();
```
```cpp
ConfigPtr get(const std::string& file);
```
```cpp
ConfigPtr create(const std::string& file);
```
```cpp
ConfigPtr loadSettings(const std::string file);
```
```cpp
ConfigPtr load(const std::string& file);
```
```cpp
bool unload(const std::string& file);
```
```cpp
void remove(const ConfigPtr config);
```