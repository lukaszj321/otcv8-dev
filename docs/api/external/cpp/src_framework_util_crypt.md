# src/framework/util/crypt.h

```cpp
public:
    Crypt();
```
```cpp
std::string base64Encode(const std::string& decoded_string);
```
```cpp
std::string base64Decode(const std::string& encoded_string);
```
```cpp
std::string xorCrypt(const std::string& buffer, const std::string& key);
```
```cpp
std::string encrypt(const std::string& decrypted_string) { return _encrypt(decrypted_string, true);
```
```cpp
std::string decrypt(const std::string& encrypted_string) { return _decrypt(encrypted_string, true);
```
```cpp
std::string genUUID();
```
```cpp
bool setMachineUUID(std::string uuidstr);
```
```cpp
std::string getMachineUUID();
```
```cpp
std::string md5Encode(const std::string& decoded_string, bool upperCase);
```
```cpp
std::string sha1Encode(const std::string& decoded_string, bool upperCase);
```
```cpp
std::string sha256Encode(const std::string& decoded_string, bool upperCase);
```
```cpp
std::string sha512Encode(const std::string& decoded_string, bool upperCase);
```
```cpp
std::string crc32(const std::string& decoded_string, bool upperCase);
```
```cpp
void rsaGenerateKey(int bits, int e);
```
```cpp
void rsaSetPublicKey(const std::string& n, const std::string& e);
```
```cpp
void rsaSetPrivateKey(const std::string &p, const std::string &q, const std::string &d);
```
```cpp
bool rsaCheckKey();
```
```cpp
bool rsaEncrypt(unsigned char *msg, int size);
```
```cpp
bool rsaDecrypt(unsigned char *msg, int size);
```
```cpp
int rsaGetSize();
```
```cpp
void bencrypt(uint8_t * buffer, int len, uint64_t k);
```
```cpp
void bdecrypt(uint8_t * buffer, int len, uint64_t k);
```
```cpp
private:
    std::string _encrypt(const std::string& decrypted_string, bool useMachineUUID);
```
```cpp
std::string _decrypt(const std::string& encrypted_string, bool useMachineUUID);
```
```cpp
std::string getCryptKey(bool useMachineUUID);
```