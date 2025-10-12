# src/framework/core/application.h

```cpp
public:
    Application();
```
```cpp
virtual void init(std::vector<std::string>& args);
```
```cpp
virtual void deinit();
```
```cpp
virtual void terminate();
```
```cpp
virtual void run() = 0; virtual void poll();
```
```cpp
virtual void exit();
```
```cpp
virtual void quick_exit();
```
```cpp
virtual void close();
```
```cpp
void restart();
```
```cpp
void restartArgs(const std::vector<std::string>& args);
```
```cpp
void setName(const std::string& name) { m_appName = name; } void setCompactName(const std::string& compactName) { m_appCompactName = compactName; } void setVersion(const std::string& version) { m_appVersion = version; } bool isRunning() { return m_running; } bool isStopping() { return m_stopping; } bool isTerminated() { return m_terminated; } const std::string& getName() { return m_appName; } const std::string& getCompactName() { return m_appCompactName; } const std::string& getVersion() { return m_appVersion; } std::string getCharset() { return m_charset; } std::string getBuildCompiler() { return BUILD_COMPILER; } std::string getBuildDate() { return std::string(__DATE__);
```
```cpp
std::string getBuildRevision() { return std::to_string(BUILD_REVISION);
```
```cpp
std::string getBuildCommit() { return BUILD_COMMIT; } #ifdef FREE_VERSION std::string getBuildType() { return "FREE"; } #else std::string getBuildType() { return "FULL"; } #endif std::string getBuildArch() { return BUILD_ARCH; } std::string getAuthor() { return "otclient.net"; } std::string getOs();
```
```cpp
std::string getStartupOptions() { return m_startupOptions; } bool isMobile() { return m_mobile; } protected: void registerLuaFunctions();
```