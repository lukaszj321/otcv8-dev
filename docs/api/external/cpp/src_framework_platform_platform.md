# src/framework/platform/platform.h

```cpp
public: void processArgs(std::vector<std::string>& args);
```
```cpp
bool spawnProcess(std::string process, const std::vector<std::string>& args);
```
```cpp
int getProcessId();
```
```cpp
bool isProcessRunning(const std::string& name);
```
```cpp
bool killProcess(const std::string& name);
```
```cpp
std::string getTempPath();
```
```cpp
std::string getCurrentDir();
```
```cpp
bool copyFile(std::string from, std::string to);
```
```cpp
bool fileExists(std::string file);
```
```cpp
bool removeFile(std::string file);
```
```cpp
ticks_t getFileModificationTime(std::string file);
```
```cpp
bool openUrl(std::string url, bool now = false);
```
```cpp
bool openDir(std::string path, bool now = false);
```
```cpp
std::string getCPUName();
```
```cpp
double getTotalSystemMemory();
```
```cpp
double getMemoryUsage();
```
```cpp
std::string getOSName();
```
```cpp
std::string traceback(const std::string& where, int level = 1, int maxDepth = 32);
```
```cpp
std::vector<std::string> getMacAddresses();
```
```cpp
std::string getUserName();
```
```cpp
std::vector<std::string> getDlls();
```
```cpp
std::vector<std::string> getProcesses();
```
```cpp
std::vector<std::string> getWindows();
```