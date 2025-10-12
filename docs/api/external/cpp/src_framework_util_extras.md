# src/framework/util/extras.h

```cpp
public:
    Extras() { DEFINE_OPTION(limitedPolling, "Limited polling");
```
```cpp
void set(const std::string& key, bool value) { auto it = m_options.find(key);
```
```cpp
bool get(const std::string& key) { auto it = m_options.find(key);
```
```cpp
std::string getDescription(const std::string& key) { auto it = m_options.find(key);
```
```cpp
std::vector<std::string> getAll() { std::vector<std::string> ret; for (auto& it : m_options) ret.push_back(it.first);
```