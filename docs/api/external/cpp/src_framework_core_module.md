# src/framework/core/module.h

```cpp
public: Module(const std::string& name);
```
```cpp
bool load();
```
```cpp
void unload();
```
```cpp
bool reload();
```
```cpp
bool isDependent();
```
```cpp
bool hasDependency(const std::string& name, bool recursive = false);
```
```cpp
int getSandbox(LuaInterface *lua);
```
```cpp
protected: void discover(const OTMLNodePtr& moduleNode);
```
```cpp
bool canUnload();
```
```cpp
bool canReload();
```
```cpp
bool isLoaded();
```
```cpp
bool isReloadable();
```
```cpp
bool isSandboxed();
```
```cpp
std::string getDescription();
```
```cpp
std::string getName();
```
```cpp
std::string getAuthor();
```
```cpp
std::string getWebsite();
```
```cpp
std::string getVersion();
```
```cpp
bool isAutoLoad();
```
```cpp
int getAutoLoadPriority();
```
```cpp
ModulePtr asModule();
```