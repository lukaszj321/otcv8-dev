# ABI-Specific Build Configuration

## Overview

Android Application Binary Interface (ABI) defines how machine code interacts with the system. OTClient v8 supports multiple ABIs for broad device compatibility.

## Supported ABIs

| ABI | Architecture | Description | Priority |
|-----|-------------|-------------|----------|
| arm64-v8a | ARMv8 64-bit | Modern Android devices (2015+) | **High** |
| armeabi-v7a | ARMv7 32-bit | Older Android devices (pre-2015) | Medium |
| x86_64 | Intel/AMD 64-bit | Emulators, x86 tablets | Low |
| x86 | Intel/AMD 32-bit | Legacy emulators | Low |

## Gradle Configuration

### build.gradle (app level)

```gradle
android {
    defaultConfig {
        // ...
        ndk {
            // Specify ABIs to build
            abiFilters 'arm64-v8a', 'armeabi-v7a'
        }
    }
    
    // Per-ABI configuration
    splits {
        abi {
            enable true
            reset()
            include 'arm64-v8a', 'armeabi-v7a', 'x86_64', 'x86'
            universalApk false
        }
    }
    
    // CMake configuration
    externalNativeBuild {
        cmake {
            path "CMakeLists.txt"
            version "3.18.1"
        }
    }
    
    defaultConfig {
        externalNativeBuild {
            cmake {
                arguments "-DANDROID_STL=c++_shared",
                          "-DANDROID_PLATFORM=android-21"
                
                // ABI-specific flags
                abiFilters.each { abi ->
                    arguments "-DANDROID_ABI=${abi}"
                }
            }
        }
    }
}
```

## CMake Configuration

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.18.1)
project(otclient)

# ABI-specific configurations
if(ANDROID_ABI STREQUAL "arm64-v8a")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -march=armv8-a")
elseif(ANDROID_ABI STREQUAL "armeabi-v7a")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -march=armv7-a -mfpu=neon")
elseif(ANDROID_ABI STREQUAL "x86_64")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -msse4.2")
elseif(ANDROID_ABI STREQUAL "x86")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -msse3")
endif()

# Library paths per ABI
set(LIB_DIR "${CMAKE_SOURCE_DIR}/libs/${ANDROID_ABI}")

# Link libraries
target_link_libraries(otclient
    ${LIB_DIR}/libcrypto.so
    ${LIB_DIR}/libssl.so
    ${LIB_DIR}/libz.so
    log
    android
    EGL
    GLESv2
)
```

## Building Per ABI

### Command Line

```bash
# Build all ABIs
./gradlew assembleRelease

# Build specific ABI
./gradlew assembleRelease -Pandroid.injected.build.abi=arm64-v8a

# Build for ARM only
./gradlew assembleRelease -Pandroid.injected.build.abi=arm64-v8a,armeabi-v7a
```

### Split APKs

Generate separate APKs per ABI:

```gradle
android {
    splits {
        abi {
            enable true
            reset()
            include 'arm64-v8a', 'armeabi-v7a', 'x86_64'
            universalApk true  // Also generate universal APK
        }
    }
}
```

Output:
```
app/build/outputs/apk/release/
├── app-arm64-v8a-release.apk      (15 MB)
├── app-armeabi-v7a-release.apk    (14 MB)
├── app-x86_64-release.apk         (16 MB)
└── app-universal-release.apk      (45 MB)
```

## Library Management

### Pre-built Libraries

Structure:
```
app/
└── libs/
    ├── arm64-v8a/
    │   ├── libcrypto.so
    │   ├── libssl.so
    │   └── libz.so
    ├── armeabi-v7a/
    │   ├── libcrypto.so
    │   ├── libssl.so
    │   └── libz.so
    └── x86_64/
        ├── libcrypto.so
        ├── libssl.so
        └── libz.so
```

### Verification Script

```bash
#!/bin/bash
# verify_abi_libs.sh

ABIS=("arm64-v8a" "armeabi-v7a" "x86_64")
LIBS=("libcrypto.so" "libssl.so" "libz.so")

for abi in "${ABIS[@]}"; do
    echo "Checking $abi..."
    for lib in "${LIBS[@]}"; do
        path="libs/$abi/$lib"
        if [ -f "$path" ]; then
            echo "  [OK] $lib"
        else
            echo "  [MISSING] $lib"
        fi
    done
done
```

## Performance Optimization

### NEON (ARM)

```cmake
# Enable NEON for ARMv7
if(ANDROID_ABI STREQUAL "armeabi-v7a")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mfpu=neon")
    add_definitions(-DHAVE_NEON)
endif()
```

### Link-Time Optimization

```gradle
android {
    buildTypes {
        release {
            ndk {
                abiFilters.each { abi ->
                    arguments "-DCMAKE_CXX_FLAGS_RELEASE=-O3 -flto"
                }
            }
        }
    }
}
```

## Testing

### Emulator Testing

```bash
# Launch emulator with specific ABI
emulator -avd Pixel_4_API_30 -abi arm64-v8a

# Install and test
adb install app-arm64-v8a-release.apk
adb shell am start -n com.otclientv8/.MainActivity
```

### Device Testing

```bash
# Check device ABI
adb shell getprop ro.product.cpu.abi

# Install appropriate APK
adb install app-arm64-v8a-release.apk
```

## See Also

- [Android Build Pipeline](./diagrams/build_pipeline.mmd)
- [APK Signing Process](./apk_signing.md)
- [Asset Packaging](./diagrams/android_build.mmd)
