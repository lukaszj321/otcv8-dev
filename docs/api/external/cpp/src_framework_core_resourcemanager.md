# src/framework/core/resourcemanager.h

```cpp
void init(const char *argv0);
```
```cpp
void terminate();
```
```cpp
bool launchCorrect(const std::string& product, const std::string& app);
```
```cpp
bool setupWriteDir(const std::string& product, const std::string& app);
```
```cpp
bool setup();
```
```cpp
std::string getCompactName();
```
```cpp
bool loadDataFromSelf(bool unmountIfMounted = false);
```
```cpp
bool fileExists(const std::string& fileName);
```
```cpp
bool directoryExists(const std::string& directoryName);
```
```cpp
void readFileStream(const std::string& fileName, std::iostream& out);
```
```cpp
std::string readFileContents(const std::string& fileName, bool safe = false);
```
```cpp
std::string readFileContentsSafe(const std::string& fileName) { return readFileContents(fileName, true);
```
```cpp
bool isFileEncryptedOrCompressed(const std::string& fileName);
```
```cpp
bool writeFileBuffer(const std::string& fileName, const uchar* data, uint size);
```
```cpp
bool writeFileContents(const std::string& fileName, const std::string& data);
```
```cpp
bool writeFileStream(const std::string& fileName, std::iostream& in);
```
```cpp
FileStreamPtr openFile(const std::string& fileName, bool dontCache = false);
```
```cpp
FileStreamPtr appendFile(const std::string& fileName);
```
```cpp
FileStreamPtr createFile(const std::string& fileName);
```
```cpp
bool deleteFile(const std::string& fileName);
```
```cpp
bool makeDir(const std::string directory);
```
```cpp
std::list<std::string> listDirectoryFiles(const std::string & directoryPath = "", bool fullPath = false, bool raw = false);
```
```cpp
std::string resolvePath(std::string path);
```
```cpp
std::string getWorkDir() { return "/"; } #ifdef ANDROID std::string getWriteDir() { return "/"; } std::string getBinaryName() { return "otclientv8.apk"; } #else std::string getWriteDir() { return m_writeDir.string();
```
```cpp
std::string getBinaryName() { return m_binaryPath.filename().string();
```
```cpp
std::string guessFilePath(const std::string& filename, const std::string& type);
```
```cpp
bool isFileType(const std::string& filename, const std::string& type);
```
```cpp
bool isLoadedFromArchive() { return m_loadedFromArchive; } bool isLoadedFromMemory() { return m_loadedFromMemory; } std::string fileChecksum(const std::string& path);
```
```cpp
std::string selfChecksum();
```
```cpp
std::string readCrashLog(bool txt);
```
```cpp
void deleteCrashLog();
```
```cpp
void updateData(const std::set<std::string>& files, bool reMount);
```
```cpp
void updateExecutable(std::string fileName);
```
```cpp
std::string createArchive(const std::map<std::string, std::string>& files);
```
```cpp
void encrypt(const std::string& seed = "");
```
```cpp
bool encryptBuffer(std::string & buffer, uint32_t seed = 0);
```
```cpp
bool decryptBuffer(std::string & buffer);
```
```cpp
void installDlls(std::filesystem::path dest);
```
```cpp
void setLayout(std::string layout);
```
```cpp
std::string getLayout() { return m_layout; } private: bool mountMemoryData(const std::shared_ptr<std::vector<uint8_t>>& data);
```
```cpp
void unmountMemoryData();
```