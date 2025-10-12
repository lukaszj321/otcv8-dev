# src/framework/core/logger.h

```cpp
void logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction);
```
```cpp
void debug(const std::string& what) { log(Fw::LogDebug, what);
```
```cpp
void info(const std::string& what) { log(Fw::LogInfo, what);
```
```cpp
void warning(const std::string& what) { log(Fw::LogWarning, what);
```
```cpp
void error(const std::string& what) { log(Fw::LogError, what);
```
```cpp
void fatal(const std::string& what) { log(Fw::LogFatal, what);
```
```cpp
void fireOldMessages();
```
```cpp
void setLogFile(const std::string& file);
```
```cpp
void setOnLog(const OnLogCallback& onLog) { m_onLog = onLog; } std::string getLastLog() { return m_lastLog; } void setTestingMode() { m_testingMode = true; } private: std::list<LogMessage> m_logMessages; OnLogCallback m_onLog; std::fstream m_outFile; std::recursive_mutex m_mutex; std::string m_lastLog; bool m_testingMode = false; }; extern Logger g_logger; #define trace() logFunc(Fw::LogDebug, "", __PRETTY_FUNCTION__) #define traceDebug(a) logFunc(Fw::LogDebug, a, __PRETTY_FUNCTION__) #define traceInfo(a) logFunc(Fw::LogInfo, a, __PRETTY_FUNCTION__) #define traceWarning(a) logFunc(Fw::LogWarning, a, __PRETTY_FUNCTION__) #define traceError(a) logFunc(Fw::LogError, a, __PRETTY_FUNCTION__) #define logTraceCounter() { \ static int __count = 0; \ static Timer __timer; \ __count++; \ if(__timer.ticksElapsed() >= 1000) { \ logTraceDebug(__count);
```