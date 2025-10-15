---
doc_id: "authoring.14_android.index"
source_path: "android/**"
source_sha: "HEAD"
last_sync_iso: "2025-10-15T22:21:56Z"
doc_class: "guide"
language: "pl"
title: "Android — Build, packaging i distribucja APK/AAB"
summary: "Kompletny przewodnik po artefaktach Android OTClient v8: AndroidManifest, Gradle, ABI (armeabi-v7a/arm64-v8a), CMake/NDK, assets i proces dystrybucji."
tags: ["otclient", "android", "build", "apk", "aab", "gradle", "ndk", "abi", "rag"]
---

# Android — Build, packaging i distribucja APK/AAB

**Cel rozdziału:** Udokumentować pełny pipeline Android dla OTClient v8: struktura projektu, manifest (permissions/activities), konfiguracja Gradle/CMake, wieloarchitekturowe ABI (ARM32/ARM64), zarządzanie assetami i proces dystrybucji do Google Play.

```{contents} Spis treści
:depth: 3
:local:
```

:::{admonition} TL;DR
:class: tip
Projekt Android OTClient v8 używa CMake + NDK do budowania natywnego kodu C++, generując APK/AAB dla ARM32/ARM64 z pełnym zestawem assetów i bibliotek SDL2.
:::

## Wprowadzenie domenowe

Port Android OTClient v8 to **aplikacja natywna** (C++/Lua) z cienką warstwą Java/Kotlin dla integracji z Android SDK. Architektura:

1. **Native layer** - C++ engine (src/**) kompilowany przez NDK
2. **Java/Kotlin layer** - `OTClientV8.java` (Activity, lifecycle, input handling)
3. **Assets** - data/ i modules/ pakowane do APK
4. **Libraries** - libSDL2.so (per ABI) dla grafiki/audio/input

### Komponenty projektu

```
android/
  otclientv8/            # Główny moduł aplikacji
    AndroidManifest.xml  # Manifest: permissions, activities
    build.xml            # Build config (legacy Ant)
    res/                 # Zasoby Android (layouts, strings, icons)
    src/                 # Java/Kotlin sources
  android_libs/          # Native libraries per ABI
    lib/                 # armeabi-v7a (ARM32)
    lib64/               # arm64-v8a (ARM64)
  otclientv8_lib/        # CMake project dla native code
  otclientv8.sln         # Visual Studio solution (opcjonalny)
  create_android_assets.ps1  # Skrypt pakowania assetów
```

## Architektura / Przepływ

### Diagram build pipeline

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
flowchart TD
    SRC[src/** C++/Lua sources]
    GRADLE[Gradle Build System]
    CMAKE[CMake + NDK]
    ASSETS[data/** + modules/**]
    LIBS[android_libs/*.so]
    
    SRC --> CMAKE
    CMAKE -->|per ABI| ARM32[lib/armeabi-v7a<br/>libotclient.so]
    CMAKE -->|per ABI| ARM64[lib64/arm64-v8a<br/>libotclient.so]
    
    ASSETS --> PACK[Asset packaging]
    PACK --> APK_ASSETS[APK assets/]
    
    ARM32 --> GRADLE
    ARM64 --> GRADLE
    LIBS --> GRADLE
    APK_ASSETS --> GRADLE
    
    GRADLE --> APK[otclient.apk<br/>otclient.aab]
    
    APK --> SIGN[Sign with keystore]
    SIGN --> DIST[Google Play<br/>or direct install]
```

### Diagram lifecycle aplikacji

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
sequenceDiagram
    participant USER as User
    participant OS as Android OS
    participant APP as OTClientV8 Activity
    participant SDL as libSDL2.so
    participant ENGINE as OTClient C++ Engine
    
    USER->>OS: Tap icon
    OS->>APP: onCreate()
    APP->>SDL: SDL_Init()
    SDL->>ENGINE: Init graphics/audio/input
    ENGINE-->>APP: Ready
    APP->>USER: Show main menu
    
    USER->>APP: Touch input
    APP->>SDL: SDL_Event
    SDL->>ENGINE: Process event
    ENGINE->>ENGINE: Update game state
    ENGINE->>SDL: Render frame
    SDL->>APP: Present
    
    USER->>OS: Back button
    OS->>APP: onPause()
    APP->>ENGINE: Pause game
    OS->>APP: onStop()
    APP->>ENGINE: Save state
    OS->>APP: onDestroy()
    APP->>ENGINE: Cleanup
```

### Diagram struktury APK

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd' } }}%%
graph TD
    APK[otclient.apk]
    
    APK --> META[META-INF/<br/>signatures]
    APK --> RES[res/<br/>Android resources]
    APK --> ASSETS[assets/<br/>game data]
    APK --> LIB[lib/<br/>native libraries]
    APK --> DEX[classes.dex<br/>Java bytecode]
    APK --> MANIFEST[AndroidManifest.xml]
    
    ASSETS --> DATA[data/**<br/>images, fonts, styles]
    ASSETS --> MODS[modules/**<br/>Lua scripts, OTUI]
    
    LIB --> ARM32[armeabi-v7a/<br/>libSDL2.so<br/>libotclient.so]
    LIB --> ARM64[arm64-v8a/<br/>libSDL2.so<br/>libhidapi.so<br/>libotclient.so]
```

## Datasets

### android_manifest.csv — AndroidManifest.xml

*Facet:* [`14_android.android_manifest`](#facet-14_android.android_manifest)

Szczegóły manifestu aplikacji.

| path | package | min_sdk | target_sdk | permissions | activities | services | receivers | features |
|---|---|---|---|---|---|---|---|---|
| android/otclientv8/AndroidManifest.xml | com.otclientv8 | 16 | 30 | WRITE_EXTERNAL_STORAGE, INTERNET, ACCESS_NETWORK_STATE, VIBRATE, WAKE_LOCK | com.otclientv8.OTClientV8 | - | - | touchscreen, wifi |

```{csv-table} android_manifest
:header-rows: 1
:file: ./datasets/android_manifest.csv
:widths: auto
```

**Permissions explained:**
- `WRITE_EXTERNAL_STORAGE` - zapis konfiguracji/logów
- `INTERNET` - połączenie z serwerem gry
- `ACCESS_NETWORK_STATE` - sprawdzanie dostępności sieci
- `VIBRATE` - haptyczne feedback
- `WAKE_LOCK` - zapobieganie uśpieniu podczas gry

### android_build.csv — Konfiguracja budowania

*Facet:* [`14_android.android_build`](#facet-14_android.android_build)

Parametry Gradle i CMake.

| module | gradle_path | abi | cmake_args | ndk_version | min_sdk | target_sdk | outputs | note |
|---|---|---|---|---|---|---|---|---|
| otclientv8 | android/otclientv8 | armeabi-v7a, arm64-v8a | -DCMAKE_BUILD_TYPE=Release | 21.3.6528147 | 16 | 30 | APK, AAB | główna aplikacja |
| otclientv8_lib | android/otclientv8_lib | armeabi-v7a, arm64-v8a | -DOTCLIENT_OPENGL_ES=ON | 21.3.6528147 | 16 | 30 | libotclient.so | native library |

```{csv-table} android_build
:header-rows: 1
:file: ./datasets/android_build.csv
:widths: auto
```

**CMake args:**
- `-DCMAKE_BUILD_TYPE=Release` - build zoptymalizowany
- `-DOTCLIENT_OPENGL_ES=ON` - użyj OpenGL ES zamiast desktop GL
- `-DANDROID_STL=c++_shared` - użyj shared STL (zamiast static)

### android_libs.csv — Biblioteki natywne

*Facet:* [`14_android.android_libs`](#facet-14_android.android_libs)

Lista bibliotek `.so` per ABI.

| abi | dll | soname | version | size_kb | required_by | note |
|---|---|---|---|---|---|---|
| armeabi-v7a | libSDL2.so | libSDL2-2.0.so.0 | 2.0.14 | 450 | otclient | SDL2 dla ARM32 |
| arm64-v8a | libSDL2.so | libSDL2-2.0.so.0 | 2.0.14 | 520 | otclient | SDL2 dla ARM64 |
| arm64-v8a | libhidapi.so | libhidapi.so | 0.10.1 | 25 | SDL2 | gamepad support |

```{csv-table} android_libs
:header-rows: 1
:file: ./datasets/android_libs.csv
:widths: auto
```

**Biblioteki:**
- `libSDL2.so` - Simple DirectMedia Layer (graphics, audio, input)
- `libhidapi.so` - HID API dla gamepadów (tylko ARM64)
- `libotclient.so` - OTClient engine (budowany z src/**)

### android_assets.csv — Assety pakowane do APK

*Facet:* [`14_android.android_assets`](#facet-14_android.android_assets)

| path | purpose | packed | abi_scope | size_mb | note |
|---|---|---|---|---|---|
| assets/data/** | zasoby gry (obrazy, fonty, style) | yes | all | 15 | pełny katalog data/ |
| assets/modules/** | moduły Lua + OTUI | yes | all | 3 | pełny katalog modules/ |
| assets/init.lua | główny skrypt inicjalizacji | yes | all | 0.01 | entry point |
| res/drawable/** | ikony aplikacji Android | yes | all | 0.5 | różne rozdzielczości |
| res/values/** | stringi i style Android | yes | all | 0.05 | lokalizacja UI |

```{csv-table} android_assets
:header-rows: 1
:file: ./datasets/android_assets.csv
:widths: auto
```

## Blueprints — Wzorce Android

### Blueprint 1: AndroidManifest.xml (kompletny)

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.otclientv8"
    android:versionCode="1"
    android:versionName="1.0">
    
    <!-- Minimalne wymagania -->
    <uses-sdk android:minSdkVersion="16" android:targetSdkVersion="30" />
    
    <!-- Permissions -->
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    
    <!-- Features -->
    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />
    <uses-feature android:name="android.hardware.wifi" android:required="false" />
    
    <application
        android:label="OTClient V8"
        android:icon="@drawable/ic_launcher"
        android:allowBackup="true"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:hardwareAccelerated="true">
        
        <!-- Main activity -->
        <activity
            android:name="com.otclientv8.OTClientV8"
            android:label="OTClient V8"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="landscape">
            
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### Blueprint 2: Gradle build config

**Plik:** `android/otclientv8/build.gradle`

```groovy
apply plugin: 'com.android.application'

android {
    compileSdkVersion 30
    buildToolsVersion "30.0.3"
    
    defaultConfig {
        applicationId "com.otclientv8"
        minSdkVersion 16
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
        
        // ABI splits
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
    }
    
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
            
            // Signing config (production)
            signingConfig signingConfigs.release
        }
        debug {
            applicationIdSuffix ".debug"
            debuggable true
        }
    }
    
    // CMake integration
    externalNativeBuild {
        cmake {
            path "CMakeLists.txt"
            version "3.18.1"
        }
    }
    
    // Asset packaging
    sourceSets {
        main {
            assets.srcDirs = ['../assets']
            jniLibs.srcDirs = ['../android_libs']
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.3.1'
}
```

### Blueprint 3: CMakeLists.txt dla native code

**Plik:** `android/otclientv8_lib/CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.10)
project(otclient)

# Android-specific flags
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -Wall")

# OpenGL ES instead of desktop GL
add_definitions(-DOTCLIENT_OPENGL_ES=1)

# Source files (add all src/** files)
file(GLOB_RECURSE SOURCES
    "${CMAKE_SOURCE_DIR}/../../src/**/*.cpp"
    "${CMAKE_SOURCE_DIR}/../../src/**/*.h"
)

# Exclude platform-specific (Windows/Linux)
list(FILTER SOURCES EXCLUDE REGEX ".*/win32/.*")
list(FILTER SOURCES EXCLUDE REGEX ".*/linux/.*")

# Create shared library
add_library(otclient SHARED ${SOURCES})

# Link libraries
find_library(log-lib log)
find_library(android-lib android)
find_library(EGL-lib EGL)
find_library(GLESv2-lib GLESv2)

target_link_libraries(otclient
    ${log-lib}
    ${android-lib}
    ${EGL-lib}
    ${GLESv2-lib}
    SDL2
)

# Include directories
target_include_directories(otclient PRIVATE
    ${CMAKE_SOURCE_DIR}/../../src
    ${CMAKE_SOURCE_DIR}/../android_libs/include
)
```

### Blueprint 4: Asset packaging script

**Plik:** `android/create_android_assets.ps1` (PowerShell)

```powershell
# Package data/ and modules/ for Android APK

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$AssetsDir = Join-Path $PSScriptRoot "otclientv8ssets"

# Clean old assets
if (Test-Path $AssetsDir) {
    Remove-Item -Recurse -Force $AssetsDir
}
New-Item -ItemType Directory -Path $AssetsDir | Out-Null

# Copy data/
Write-Host "Copying data/..."
Copy-Item -Recurse (Join-Path $ProjectRoot "data") (Join-Path $AssetsDir "data")

# Copy modules/
Write-Host "Copying modules/..."
Copy-Item -Recurse (Join-Path $ProjectRoot "modules") (Join-Path $AssetsDir "modules")

# Copy init.lua
Write-Host "Copying init.lua..."
Copy-Item (Join-Path $ProjectRoot "init.lua") (Join-Path $AssetsDir "init.lua")

# Remove unnecessary files (reduce APK size)
Write-Host "Cleaning up..."
Get-ChildItem -Path $AssetsDir -Include *.psd,*.md,*.txt -Recurse | Remove-Item -Force

Write-Host "Assets packaged successfully: $AssetsDir"
```

### Blueprint 5: Java Activity (główna klasa)

**Plik:** `android/otclientv8/src/com/otclientv8/OTClientV8.java`

```java
package com.otclientv8;

import org.libsdl.app.SDLActivity;
import android.os.Bundle;
import android.util.Log;

public class OTClientV8 extends SDLActivity {
    private static final String TAG = "OTClientV8";
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "onCreate");
        super.onCreate(savedInstanceState);
        
        // Custom initialization
        initializeNative();
    }
    
    @Override
    protected void onPause() {
        Log.d(TAG, "onPause");
        super.onPause();
        saveGameState();
    }
    
    @Override
    protected void onResume() {
        Log.d(TAG, "onResume");
        super.onResume();
        restoreGameState();
    }
    
    @Override
    protected void onDestroy() {
        Log.d(TAG, "onDestroy");
        cleanupNative();
        super.onDestroy();
    }
    
    // Native methods (implemented in C++)
    private native void initializeNative();
    private native void saveGameState();
    private native void restoreGameState();
    private native void cleanupNative();
    
    // JNI library loading
    static {
        System.loadLibrary("SDL2");
        System.loadLibrary("otclient");
    }
}
```

## How-to / Playbook

### Procedura 1: Build APK z wiersza poleceń

**Krok 1:** Setup środowiska
```bash
# Zainstaluj Android SDK + NDK
# Ustaw zmienne środowiskowe
export ANDROID_HOME=/path/to/android-sdk
export ANDROID_NDK=/path/to/android-ndk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

**Krok 2:** Przygotuj assety
```bash
cd android
./create_android_assets.ps1  # lub .sh na Linux
```

**Krok 3:** Build native libraries
```bash
cd otclientv8_lib
mkdir build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake          -DANDROID_ABI=arm64-v8a          -DANDROID_PLATFORM=android-16          -DCMAKE_BUILD_TYPE=Release
make -j8
```

**Krok 4:** Build APK
```bash
cd ../otclientv8
./gradlew assembleRelease

# Output: otclientv8/build/outputs/apk/release/otclientv8-release-unsigned.apk
```

**Krok 5:** Sign APK
```bash
# Generuj keystore (raz)
keytool -genkey -v -keystore release.keystore -alias otclient -keyalg RSA -keysize 2048 -validity 10000

# Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1           -keystore release.keystore           otclientv8-release-unsigned.apk otclient

# Align (optimize)
zipalign -v 4 otclientv8-release-unsigned.apk otclientv8-release.apk
```

### Procedura 2: Build dla wielu ABI

**Krok 1:** Konfiguruj Gradle dla splits
```groovy
// build.gradle
android {
    splits {
        abi {
            enable true
            reset()
            include 'armeabi-v7a', 'arm64-v8a'
            universalApk false  // Oddzielne APK per ABI
        }
    }
}
```

**Krok 2:** Build
```bash
./gradlew assembleRelease

# Output:
# otclientv8-armeabi-v7a-release.apk
# otclientv8-arm64-v8a-release.apk
```

**Krok 3:** Generuj AAB (Android App Bundle)
```bash
./gradlew bundleRelease

# Output: otclientv8-release.aab
# Google Play automatycznie generuje APK per ABI
```

### Procedura 3: Debug na urządzeniu

**Krok 1:** Włącz USB debugging na urządzeniu
```
Settings → About phone → Tap "Build number" 7 times
Settings → Developer options → USB debugging ON
```

**Krok 2:** Podłącz urządzenie i sprawdź
```bash
adb devices
# List of devices attached
# ABC123456789    device
```

**Krok 3:** Install debug APK
```bash
./gradlew installDebug

# Lub ręcznie
adb install -r otclientv8-debug.apk
```

**Krok 4:** Monitor logs
```bash
# Filtruj logi OTClient
adb logcat | grep OTClientV8

# Lub pełne logi
adb logcat -s OTClientV8:D SDL:D *:E
```

**Krok 5:** Debug C++ z LLDB
```bash
# W Android Studio
Run → Debug 'otclientv8'
# Ustaw breakpointy w C++ code
```

### Procedura 4: Packaging do Google Play

**Krok 1:** Przygotuj store listing
```
- App name: OTClient V8
- Short description: Open-source MMORPG client for Tibia
- Full description: ...
- Screenshots: 1920x1080 (landscape)
- Feature graphic: 1024x500
- Icon: 512x512 PNG
```

**Krok 2:** Generuj signed AAB
```bash
./gradlew bundleRelease

# Sign AAB
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256           -keystore release.keystore           otclientv8-release.aab otclient
```

**Krok 3:** Upload do Google Play Console
```
1. Create new release (Production/Beta/Alpha)
2. Upload otclientv8-release.aab
3. Set version code and name
4. Add release notes
5. Review and rollout
```

**Krok 4:** Configure in-app updates (opcjonalnie)
```java
// In OTClientV8.java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(this);
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE) {
        // Request update
    }
});
```

### Procedura 5: Profiling i optymalizacja

**Krok 1:** Profile APK size
```bash
# Analyze APK content
./gradlew :otclientv8:analyzeReleaseApk

# Lub ręcznie
unzip -l otclientv8-release.apk | sort -k4 -rn | head -20
```

**Krok 2:** Profile runtime (CPU/Memory)
```bash
# W Android Studio
Run → Profile 'otclientv8'
# CPU Profiler, Memory Profiler, Network Profiler
```

**Krok 3:** Reduce APK size
```groovy
// build.gradle
android {
    buildTypes {
        release {
            // Enable ProGuard
            minifyEnabled true
            shrinkResources true
            
            // R8 (better than ProGuard)
            useProguard false
        }
    }
}
```

**Krok 4:** Optimize assets
```bash
# Compress PNG images
find assets -name "*.png" -exec optipng -o7 {} \;

# Remove unused assets
python scripts/find_unused_assets.py --remove
```

## Integracje / Pułapki

### Pułapka 1: ABI mismatch

**Problem:**
```
# APK zawiera libotclient.so tylko dla arm64-v8a
# Urządzenie: armeabi-v7a (ARM32)
# Crash at launch: java.lang.UnsatisfiedLinkError
```

**Remedium:**
```groovy
// Zawsze build dla obu ABI
android {
    defaultConfig {
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
    }
}
```

### Pułapka 2: Missing assets

**Problem:**
```
# Assets nie są pakowane do APK
# Logs: ERROR: cannot load data/images/ui/button.png
```

**Remedium:**
```groovy
// Sprawdź sourceSets w build.gradle
sourceSets {
    main {
        assets.srcDirs = ['assets']  // Prawidłowa ścieżka
    }
}

// Weryfikuj zawartość APK
unzip -l otclientv8-release.apk | grep "assets/data"
```

### Pułapka 3: Permissions not granted at runtime

**Problem:**
```
# Android 6.0+ wymaga runtime permissions
# WRITE_EXTERNAL_STORAGE declared, ale nie requested
# Crash przy zapisie pliku
```

**Remedium:**
```java
// W OTClientV8.java onCreate()
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    if (checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
        requestPermissions(new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 1);
    }
}
```

### Pułapka 4: OpenGL ES incompatibility

**Problem:**
```
# Desktop OTClient uses OpenGL 2.1
# Android requires OpenGL ES 2.0/3.0
# Shader code incompatible
```

**Remedium:**
```cpp
// W shader code, użyj preprocessor directives
#ifdef OTCLIENT_OPENGL_ES
    precision mediump float;
    #define texture2D texture
#endif

// W CMakeLists.txt
add_definitions(-DOTCLIENT_OPENGL_ES=1)
```

### Pułapka 5: ProGuard removes needed code

**Problem:**
```
# ProGuard minification usuwa kod SDL/native methods
# Crash: NoSuchMethodError
```

**Remedium:**
```proguard
# proguard-rules.pro
# Keep SDL classes
-keep class org.libsdl.** { *; }

# Keep native methods
-keepclasseswithmembernames class * {
    native <methods>;
}

# Keep OTClient classes
-keep class com.otclientv8.** { *; }
```

## QA & Checklists

### Checklist: Build APK

- [ ] All ABIs built (armeabi-v7a, arm64-v8a)
- [ ] Assets packaged (data/, modules/, init.lua)
- [ ] Native libraries included (libSDL2.so, libotclient.so)
- [ ] AndroidManifest complete (permissions, activities)
- [ ] Signed with release keystore
- [ ] Zipaligned and optimized
- [ ] Tested on physical device (ARM32 and ARM64)
- [ ] No crashes in logs (adb logcat)

### Checklist: Google Play submission

- [ ] AAB generated and signed
- [ ] Version code incremented
- [ ] Release notes written (per language)
- [ ] Screenshots updated (1920x1080, landscape)
- [ ] Store listing complete (title, description, icon)
- [ ] Content rating filled
- [ ] Privacy policy URL provided
- [ ] Beta testing completed (no critical bugs)

### Checklist: Performance

- [ ] APK size < 50 MB (after splits)
- [ ] App startup < 3 seconds
- [ ] Frame rate stable 30+ FPS
- [ ] Memory usage < 200 MB
- [ ] No memory leaks (profiled)
- [ ] Battery consumption acceptable (< 5% per hour)

### Link-lint OK

```bash
python docs/authoring/_tools/link_lint.py --chapter 14_android
# Expected: 0 errors
```

### Diagram-lint OK

```bash
python docs/authoring/_tools/diagram_lint.py --chapter 14_android
# Expected: all diagrams have %%{init: ...}%% header
```

### Dataset-sanity OK

```bash
python docs/authoring/_tools/csv_schema_check.py --chapter 14_android
# Expected:
# - headers match schema
# - no empty rows
# - no NaN values
```

### Idempotency OK

```bash
python docs/authoring/_tools/android_scan.py --output /tmp/run1/
python docs/authoring/_tools/android_scan.py --output /tmp/run2/
diff -r /tmp/run1/ /tmp/run2/
# Expected: no differences
```

## See Also

### Crosslinks do innych rozdziałów

- **`01_core`** — C++ engine budowany przez NDK
- **`11_data`** — Assety pakowane do APK
- **`12_otmod`** — Moduły Lua w APK

### Narzędzia

- `docs/authoring/_tools/android_scan.py` - skaner struktury Android
- Android Studio - IDE i profiling
- adb - Android Debug Bridge

## Appendix / Facets

(facet-14_android.android_manifest)=
### Facet: `14_android.android_manifest`
Type: dataset
Schema: `path, package, min_sdk, target_sdk, permissions, activities, services, receivers, features`

(facet-14_android.android_build)=
### Facet: `14_android.android_build`
Type: dataset
Schema: `module, gradle_path, abi, cmake_args, ndk_version, min_sdk, target_sdk, outputs, note`

(facet-14_android.android_libs)=
### Facet: `14_android.android_libs`
Type: dataset
Schema: `abi, dll, soname, version, size_kb, required_by, note`

(facet-14_android.android_assets)=
### Facet: `14_android.android_assets`
Type: dataset
Schema: `path, purpose, packed, abi_scope, size_mb, note`

(facet-14_android.build_pipeline)=
### Facet: `14_android.build_pipeline`
Type: diagram
Format: mermaid (flowchart TD)
