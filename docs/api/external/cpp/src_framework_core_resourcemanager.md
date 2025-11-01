---
title: "src/framework/core/resourcemanager.h"
source_file: "src/framework/core/resourcemanager.h"
generated_at: "2025-11-01T06:09:06.180Z"
doc_type: "cpp_api"
---

# src/framework/core/resourcemanager.h

(init)=
## `init`

**Signature:**
```cpp
void init(const char *argv0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *argv0` | - | - |

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(launchcorrect)=
## `launchCorrect`

**Signature:**
```cpp
bool launchCorrect(const std::string& product, const std::string& app);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `product` | - |
| `const std::string&` | `app` | - |

**Returns:**
- `bool`

---

(setupwritedir)=
## `setupWriteDir`

**Signature:**
```cpp
bool setupWriteDir(const std::string& product, const std::string& app);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `product` | - |
| `const std::string&` | `app` | - |

**Returns:**
- `bool`

---

(setup)=
## `setup`

**Signature:**
```cpp
bool setup();
```

**Returns:**
- `bool`

---

(getcompactname)=
## `getCompactName`

**Signature:**
```cpp
std::string getCompactName();
```

**Returns:**
- `std::string`

---

(loaddatafromself)=
## `loadDataFromSelf`

**Signature:**
```cpp
bool loadDataFromSelf(bool unmountIfMounted = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `unmountIfMounted` | `false` | - |

**Returns:**
- `bool`

---

(fileexists)=
## `fileExists`

**Signature:**
```cpp
bool fileExists(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(directoryexists)=
## `directoryExists`

**Signature:**
```cpp
bool directoryExists(const std::string& directoryName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `directoryName` | - |

**Returns:**
- `bool`

---

(readfilestream)=
## `readFileStream`

**Signature:**
```cpp
void readFileStream(const std::string& fileName, std::iostream& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `std::iostream&` | `out` | - |

---

(readfilecontents)=
## `readFileContents`

**Signature:**
```cpp
std::string readFileContents(const std::string& fileName, bool safe = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `fileName` |  | - |
| `bool` | `safe` | `false` | - |

**Returns:**
- `std::string`

---

(isfileencryptedorcompressed)=
## `isFileEncryptedOrCompressed`

**Signature:**
```cpp
bool isFileEncryptedOrCompressed(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(writefilebuffer)=
## `writeFileBuffer`

**Signature:**
```cpp
bool writeFileBuffer(const std::string& fileName, const uchar* data, uint size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `const uchar*` | `data` | - |
| `uint` | `size` | - |

**Returns:**
- `bool`

---

(writefilecontents)=
## `writeFileContents`

**Signature:**
```cpp
bool writeFileContents(const std::string& fileName, const std::string& data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `const std::string&` | `data` | - |

**Returns:**
- `bool`

---

(writefilestream)=
## `writeFileStream`

**Signature:**
```cpp
bool writeFileStream(const std::string& fileName, std::iostream& in);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `std::iostream&` | `in` | - |

**Returns:**
- `bool`

---

(openfile)=
## `openFile`

**Signature:**
```cpp
FileStreamPtr openFile(const std::string& fileName, bool dontCache = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `fileName` |  | - |
| `bool` | `dontCache` | `false` | - |

**Returns:**
- `FileStreamPtr`

---

(appendfile)=
## `appendFile`

**Signature:**
```cpp
FileStreamPtr appendFile(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `FileStreamPtr`

---

(createfile)=
## `createFile`

**Signature:**
```cpp
FileStreamPtr createFile(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `FileStreamPtr`

---

(deletefile)=
## `deleteFile`

**Signature:**
```cpp
bool deleteFile(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(makedir)=
## `makeDir`

**Signature:**
```cpp
bool makeDir(const std::string directory);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string` | `directory` | - |

**Returns:**
- `bool`

---

(listdirectoryfiles)=
## `listDirectoryFiles`

**Signature:**
```cpp
std::list<std::string> listDirectoryFiles(const std::string & directoryPath = "", bool fullPath = false, bool raw = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string &` | `directoryPath` | `""` | - |
| `bool` | `fullPath` | `false` | - |
| `bool` | `raw` | `false` | - |

**Returns:**
- `std::list&lt;std::string&gt;`

---

(resolvepath)=
## `resolvePath`

**Signature:**
```cpp
std::string resolvePath(std::string path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `path` | - |

**Returns:**
- `std::string`

---

(guessfilepath)=
## `guessFilePath`

**Signature:**
```cpp
std::string guessFilePath(const std::string& filename, const std::string& type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |
| `const std::string&` | `type` | - |

**Returns:**
- `std::string`

---

(isfiletype)=
## `isFileType`

**Signature:**
```cpp
bool isFileType(const std::string& filename, const std::string& type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |
| `const std::string&` | `type` | - |

**Returns:**
- `bool`

---

(filechecksum)=
## `fileChecksum`

**Signature:**
```cpp
std::string fileChecksum(const std::string& path);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `path` | - |

**Returns:**
- `std::string`

---

(selfchecksum)=
## `selfChecksum`

**Signature:**
```cpp
std::string selfChecksum();
```

**Returns:**
- `std::string`

---

(readcrashlog)=
## `readCrashLog`

**Signature:**
```cpp
std::string readCrashLog(bool txt);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `txt` | - |

**Returns:**
- `std::string`

---

(deletecrashlog)=
## `deleteCrashLog`

**Signature:**
```cpp
void deleteCrashLog();
```

---

(updatedata)=
## `updateData`

**Signature:**
```cpp
void updateData(const std::set<std::string>& files, bool reMount);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::set&lt;std::string&gt;&` | `files` | - |
| `bool` | `reMount` | - |

---

(updateexecutable)=
## `updateExecutable`

**Signature:**
```cpp
void updateExecutable(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(createarchive)=
## `createArchive`

**Signature:**
```cpp
std::string createArchive(const std::map<std::string, std::string>& files);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::map&lt;std::string, std::string&gt;&` | `files` | - |

**Returns:**
- `std::string`

---

(encrypt)=
## `encrypt`

**Signature:**
```cpp
void encrypt(const std::string& seed = "");
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `seed` | `""` | - |

---

(encryptbuffer)=
## `encryptBuffer`

**Signature:**
```cpp
bool encryptBuffer(std::string & buffer, uint32_t seed = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `std::string &` | `buffer` |  | - |
| `uint32_t` | `seed` | `0` | - |

**Returns:**
- `bool`

---

(decryptbuffer)=
## `decryptBuffer`

**Signature:**
```cpp
bool decryptBuffer(std::string & buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string &` | `buffer` | - |

**Returns:**
- `bool`

---

(installdlls)=
## `installDlls`

**Signature:**
```cpp
void installDlls(std::filesystem::path dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::filesystem::path` | `dest` | - |

---

(setlayout)=
## `setLayout`

**Signature:**
```cpp
void setLayout(std::string layout);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `layout` | - |

---

(mountmemorydata)=
## `mountMemoryData`

**Signature:**
```cpp
private: bool mountMemoryData(const std::shared_ptr<std::vector<uint8_t>>& data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::shared_ptr&lt;std::vector&lt;uint8_t&gt;&gt;&` | `data` | - |

**Returns:**
- `bool`

---

(unmountmemorydata)=
## `unmountMemoryData`

**Signature:**
```cpp
void unmountMemoryData();
```

---

(readfilecontentssafe)=
## `readFileContentsSafe`

**Signature:**
```cpp
std::string readFileContentsSafe(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `std::string`

---

(getworkdir)=
## `getWorkDir`

**Signature:**
```cpp
std::string getWorkDir();
```

**Returns:**
- `std::string`

---

(getwritedir)=
## `getWriteDir`

**Signature:**
```cpp
std::string getWriteDir();
```

**Returns:**
- `std::string`

---

(getbinaryname)=
## `getBinaryName`

**Signature:**
```cpp
std::string getBinaryName();
```

**Returns:**
- `std::string`

---

(getwritedir-1)=
## `getWriteDir`

**Signature:**
```cpp
std::string getWriteDir();
```

**Returns:**
- `std::string`

---

(getbinaryname-1)=
## `getBinaryName`

**Signature:**
```cpp
std::string getBinaryName();
```

**Returns:**
- `std::string`

---

(isloadedfromarchive)=
## `isLoadedFromArchive`

**Signature:**
```cpp
bool isLoadedFromArchive();
```

**Returns:**
- `bool`

---

(isloadedfrommemory)=
## `isLoadedFromMemory`

**Signature:**
```cpp
bool isLoadedFromMemory();
```

**Returns:**
- `bool`

---

(getlayout)=
## `getLayout`

**Signature:**
```cpp
std::string getLayout();
```

**Returns:**
- `std::string`

---
