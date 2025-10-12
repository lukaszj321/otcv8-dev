# src/framework/util/pngunpacker.h

```cpp
public:
	FileMetadata(const FileStreamPtr& file);
```
```cpp
const std::string& getFileName() const { return fileName; } uint32_t getOffset() const { return offset; } uint32_t getFileSize() const { return fileSize; } private: std::string fileName; uint32_t offset = 0; uint32_t fileSize = 0; }; class PngUnpacker { public: static std::unordered_map<uint32_t, std::string> unpack(const FileStreamPtr& file);
```