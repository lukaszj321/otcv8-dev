# src/framework/core/modulemanager.h

```cpp
public: void clear();
```
```cpp
void discoverModules();
```
```cpp
void autoLoadModules(int maxPriority);
```
```cpp
ModulePtr discoverModule(const std::string& moduleFile);
```
```cpp
void ensureModuleLoaded(const std::string& moduleName);
```
```cpp
void unloadModules();
```
```cpp
void reloadModules();
```
```cpp
ModulePtr getModule(const std::string& moduleName);
```
```cpp
protected: void updateModuleLoadOrder(ModulePtr module);
```
```cpp
std::deque<ModulePtr> getModules();
```