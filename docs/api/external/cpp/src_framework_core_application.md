# src/framework/core/application.h

```cpp
public: Application();
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
virtual void run();
```
```cpp
virtual void poll();
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
std::string getOs();
```
```cpp
protected: void registerLuaFunctions();
```
```cpp
void setName(const std::string& name);
```
```cpp
void setCompactName(const std::string& compactName);
```
```cpp
void setVersion(const std::string& version);
```
```cpp
bool isRunning();
```
```cpp
bool isStopping();
```
```cpp
bool isTerminated();
```
```cpp
const std::string& getName();
```
```cpp
const std::string& getCompactName();
```
```cpp
const std::string& getVersion();
```
```cpp
std::string getCharset();
```
```cpp
std::string getBuildCompiler();
```
```cpp
std::string getBuildDate();
```
```cpp
std::string getBuildRevision();
```
```cpp
std::string getBuildCommit();
```
```cpp
std::string getBuildType();
```
```cpp
std::string getBuildType();
```
```cpp
std::string getBuildArch();
```
```cpp
std::string getAuthor();
```
```cpp
std::string getStartupOptions();
```
```cpp
bool isMobile();
```