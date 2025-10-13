# src/framework/core/logger.h

```cpp
public: void log(Fw::LogLevel level, const std::string& message);
```
```cpp
void logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction);
```
```cpp
void fireOldMessages();
```
```cpp
void setLogFile(const std::string& file);
```
```cpp
void debug(const std::string& what);
```
```cpp
void info(const std::string& what);
```
```cpp
void warning(const std::string& what);
```
```cpp
void error(const std::string& what);
```
```cpp
void fatal(const std::string& what);
```
```cpp
void setOnLog(const OnLogCallback& onLog);
```
```cpp
std::string getLastLog();
```
```cpp
void setTestingMode();
```