# src/framework/core/module.h

```cpp
public:
    Module(const std::string& name);
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
bool canUnload() { return m_loaded && m_reloadable && !isDependent();
```
```cpp
bool canReload() { return m_reloadable && !isDependent();
```
```cpp
bool isLoaded() { return m_loaded; } bool isReloadable() { return m_reloadable; } bool isDependent();
```
```cpp
bool isSandboxed() { return m_sandboxed; } bool hasDependency(const std::string& name, bool recursive = false);
```
```cpp
int getSandbox(LuaInterface *lua);
```
```cpp
std::string getDescription() { return m_description; } std::string getName() { return m_name; } std::string getAuthor() { return m_author; } std::string getWebsite() { return m_website; } std::string getVersion() { return m_version; } bool isAutoLoad() { return m_autoLoad; } int getAutoLoadPriority() { return m_autoLoadPriority; } // @dontbind ModulePtr asModule() { return static_self_cast<Module>();
```
```cpp
protected:
    void discover(const OTMLNodePtr& moduleNode);
```