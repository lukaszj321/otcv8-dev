---
title: "src/framework/util/qrcodegen.h"
source_file: "src/framework/util/qrcodegen.h"
generated_at: "2025-11-01T08:29:23.729Z"
doc_type: "cpp_api"
---

# src/framework/util/qrcodegen.h

(qrcodegen_encodetext)=
## `qrcodegen_encodeText`

of at least qrcodegen_BUFFER_LEN_FOR_VERSION(maxVersion).
- After the function returns, tempBuffer contains no useful data.
- If successful, the resulting QR Code may use numeric,
alphanumeric, or byte mode to encode the text.
- In the most optimistic case, a QR Code at version 40 with low ECC
can hold any UTF-8 string up to 2953 bytes, or any alphanumeric string
up to 4296 characters, or any digit string up to 7089 characters.
These numbers represent the hard upper limit of the QR Code standard.
- Please consult the QR Code specification for information on
data capacities per version, ECC level, and text encoding mode.

**Signature:**
```cpp
bool qrcodegen_encodeText(const char *text, uint8_t tempBuffer[], uint8_t qrcode[], enum qrcodegen_Ecc ecl, int minVersion, int maxVersion, enum qrcodegen_Mask mask, bool boostEcl);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *text` | - | - |
| `uint8_t tempBuffer[]` | - | - |
| `uint8_t qrcode[]` | - | - |
| `enum qrcodegen_Ecc` | `ecl` | - |
| `int` | `minVersion` | - |
| `int` | `maxVersion` | - |
| `enum qrcodegen_Mask` | `mask` | - |
| `bool` | `boostEcl` | - |

**Returns:**
- `bool`

---

(qrcodegen_encodebinary)=
## `qrcodegen_encodeBinary`

- Requires 1 <= minVersion <= maxVersion <= 40.
- The arrays dataAndTemp and qrcode must each have a length
of at least qrcodegen_BUFFER_LEN_FOR_VERSION(maxVersion).
- After the function returns, the contents of dataAndTemp may have changed,
and does not represent useful data anymore.
- If successful, the resulting QR Code will use byte mode to encode the data.
- In the most optimistic case, a QR Code at version 40 with low ECC can hold any byte
sequence up to length 2953. This is the hard upper limit of the QR Code standard.
- Please consult the QR Code specification for information on
data capacities per version, ECC level, and text encoding mode.

**Signature:**
```cpp
bool qrcodegen_encodeBinary(uint8_t dataAndTemp[], size_t dataLen, uint8_t qrcode[], enum qrcodegen_Ecc ecl, int minVersion, int maxVersion, enum qrcodegen_Mask mask, bool boostEcl);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8_t dataAndTemp[]` | - | - |
| `size_t` | `dataLen` | - |
| `uint8_t qrcode[]` | - | - |
| `enum qrcodegen_Ecc` | `ecl` | - |
| `int` | `minVersion` | - |
| `int` | `maxVersion` | - |
| `enum qrcodegen_Mask` | `mask` | - |
| `bool` | `boostEcl` | - |

**Returns:**
- `bool`

---

(qrcodegen_encodesegments)=
## `qrcodegen_encodeSegments`

Renders a QR Code representing the given segments at the given error correction level.
The smallest possible QR Code version is automatically chosen for the output. Returns true if
QR Code creation succeeded, or false if the data is too long to fit in any version. The ECC level
of the result may be higher than the ecl argument if it can be done without increasing the version.
This function allows the user to create a custom sequence of segments that switches
between modes (such as alphanumeric and byte) to encode text in less space.
This is a low-level API; the high-level API is qrcodegen_encodeText() and qrcodegen_encodeBinary().
To save memory, the segments' data buffers can alias/overlap tempBuffer, and will
result in them being clobbered, but the QR Code output will still be correct.
But the qrcode array must not overlap tempBuffer or any segment's data buffer.

**Signature:**
```cpp
bool qrcodegen_encodeSegments(const struct qrcodegen_Segment segs[], size_t len, enum qrcodegen_Ecc ecl, uint8_t tempBuffer[], uint8_t qrcode[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const struct qrcodegen_Segment segs[]` | - | - |
| `size_t` | `len` | - |
| `enum qrcodegen_Ecc` | `ecl` | - |
| `uint8_t tempBuffer[]` | - | - |
| `uint8_t qrcode[]` | - | - |

**Returns:**
- `bool`

---

(qrcodegen_encodesegmentsadvanced)=
## `qrcodegen_encodeSegmentsAdvanced`

chosen for the output. Iff boostEcl is true, then the ECC level of the result
may be higher than the ecl argument if it can be done without increasing the
version. The mask is either between qrcodegen_Mask_0 to 7 to force that mask, or
qrcodegen_Mask_AUTO to automatically choose an appropriate mask (which may be slow).
This function allows the user to create a custom sequence of segments that switches
between modes (such as alphanumeric and byte) to encode text in less space.
This is a low-level API; the high-level API is qrcodegen_encodeText() and qrcodegen_encodeBinary().
To save memory, the segments' data buffers can alias/overlap tempBuffer, and will
result in them being clobbered, but the QR Code output will still be correct.
But the qrcode array must not overlap tempBuffer or any segment's data buffer.

**Signature:**
```cpp
bool qrcodegen_encodeSegmentsAdvanced(const struct qrcodegen_Segment segs[], size_t len, enum qrcodegen_Ecc ecl, int minVersion, int maxVersion, enum qrcodegen_Mask mask, bool boostEcl, uint8_t tempBuffer[], uint8_t qrcode[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const struct qrcodegen_Segment segs[]` | - | - |
| `size_t` | `len` | - |
| `enum qrcodegen_Ecc` | `ecl` | - |
| `int` | `minVersion` | - |
| `int` | `maxVersion` | - |
| `enum qrcodegen_Mask` | `mask` | - |
| `bool` | `boostEcl` | - |
| `uint8_t tempBuffer[]` | - | - |
| `uint8_t qrcode[]` | - | - |

**Returns:**
- `bool`

---

(qrcodegen_isalphanumeric)=
## `qrcodegen_isAlphanumeric`

Tests whether the given string can be encoded as a segment in alphanumeric mode.
A string is encodable iff each character is in the following set: 0 to 9, A to Z
(uppercase only), space, dollar, percent, asterisk, plus, hyphen, period, slash, colon.

**Signature:**
```cpp
bool qrcodegen_isAlphanumeric(const char *text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *text` | - | - |

**Returns:**
- `bool`

---

(qrcodegen_isnumeric)=
## `qrcodegen_isNumeric`

Tests whether the given string can be encoded as a segment in numeric mode.
A string is encodable iff each character is in the range 0 to 9.

**Signature:**
```cpp
bool qrcodegen_isNumeric(const char *text);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *text` | - | - |

**Returns:**
- `bool`

---

(qrcodegen_calcsegmentbuffersize)=
## `qrcodegen_calcSegmentBufferSize`

Returns the number of bytes (uint8_t) needed for the data buffer of a segment
containing the given number of characters using the given mode. Notes:
- Returns SIZE_MAX on failure, i.e. numChars > INT16_MAX or
the number of needed bits exceeds INT16_MAX (i.e. 32767).
- Otherwise, all valid results are in the range [0, ceil(INT16_MAX / 8)], i.e. at most 4096.
- It is okay for the user to allocate more bytes for the buffer than needed.
- For byte mode, numChars measures the number of bytes, not Unicode code points.
- For ECI mode, numChars must be 0, and the worst-case number of bytes is returned.
An actual ECI segment can have shorter data. For non-ECI modes, the result is exact.

**Signature:**
```cpp
size_t qrcodegen_calcSegmentBufferSize(enum qrcodegen_Mode mode, size_t numChars);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `enum qrcodegen_Mode` | `mode` | - |
| `size_t` | `numChars` | - |

**Returns:**
- `size_t`

---

(qrcodegen_makebytes)=
## `qrcodegen_makeBytes`

Returns a segment representing the given binary data encoded in
byte mode. All input byte arrays are acceptable. Any text string
can be converted to UTF-8 bytes and encoded as a byte mode segment.

**Signature:**
```cpp
struct qrcodegen_Segment qrcodegen_makeBytes(const uint8_t data[], size_t len, uint8_t buf[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uint8_t data[]` | - | - |
| `size_t` | `len` | - |
| `uint8_t buf[]` | - | - |

**Returns:**
- `struct qrcodegen_Segment`

---

(qrcodegen_makenumeric)=
## `qrcodegen_makeNumeric`

Returns a segment representing the given string of decimal digits encoded in numeric mode.

**Signature:**
```cpp
struct qrcodegen_Segment qrcodegen_makeNumeric(const char *digits, uint8_t buf[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *digits` | - | - |
| `uint8_t buf[]` | - | - |

**Returns:**
- `struct qrcodegen_Segment`

---

(qrcodegen_makealphanumeric)=
## `qrcodegen_makeAlphanumeric`

Returns a segment representing the given text string encoded in alphanumeric mode.
The characters allowed are: 0 to 9, A to Z (uppercase only), space,
dollar, percent, asterisk, plus, hyphen, period, slash, colon.

**Signature:**
```cpp
struct qrcodegen_Segment qrcodegen_makeAlphanumeric(const char *text, uint8_t buf[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const char *text` | - | - |
| `uint8_t buf[]` | - | - |

**Returns:**
- `struct qrcodegen_Segment`

---

(qrcodegen_makeeci)=
## `qrcodegen_makeEci`

Returns a segment representing an Extended Channel Interpretation
(ECI) designator with the given assignment value.

**Signature:**
```cpp
struct qrcodegen_Segment qrcodegen_makeEci(long assignVal, uint8_t buf[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `long` | `assignVal` | - |
| `uint8_t buf[]` | - | - |

**Returns:**
- `struct qrcodegen_Segment`

---

(qrcodegen_getsize)=
## `qrcodegen_getSize`

Returns the side length of the given QR Code, assuming that encoding succeeded.
The result is in the range [21, 177]. Note that the length of the array buffer
is related to the side length - every 'uint8_t qrcode[]' must have length at least
qrcodegen_BUFFER_LEN_FOR_VERSION(version), which equals ceil(size^2 / 8 + 1).

**Signature:**
```cpp
int qrcodegen_getSize(const uint8_t qrcode[]);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uint8_t qrcode[]` | - | - |

**Returns:**
- `int`

---

(qrcodegen_getmodule)=
## `qrcodegen_getModule`

Returns the color of the module (pixel) at the given coordinates, which is false
for white or true for black. The top left corner has the coordinates (x=0, y=0).
If the given coordinates are out of bounds, then false (white) is returned.

**Signature:**
```cpp
bool qrcodegen_getModule(const uint8_t qrcode[], int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uint8_t qrcode[]` | - | - |
| `int` | `x` | - |
| `int` | `y` | - |

**Returns:**
- `bool`

---
