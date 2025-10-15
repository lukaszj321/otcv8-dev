---
doc_id: chapter_14_android_docs_export_kit_authoring_agent_ready
source_path: android/*
source_sha: unknown
last_sync_iso: 2025-10-15T20:31:06Z
doc_class: platform/android
language: pl
title: 14_android — struktura projektu, ABI i pakowanie zasobów
summary: Warstwa Java/JNI, matryca ABI, pakowanie assets oraz wskazówki CMake/Gradle do stabilnego builda i dystrybucji.
tags: [android, ndk, jni, abi, assets, cmake, gradle]
---

```{contents}
:local:
:depth: 2
```

## 1. Przegląd projektu

Katalog `android/` zawiera elementy wymagane do budowy aplikacji: manifest, zasoby (`res/`),
warstwę Java (`src/com/otclientv8`) i bibliotekę JNI (`otclientv8_lib`) z `.so` per ABI.
Zasoby aplikacji (`assets/`) są **wspólne** dla wszystkich ABI.

## 2. Struktura (kontrakt)

```{list-table} Katalogi Android
:header-rows: 1
* - ścieżka
  - opis
* - android/AndroidManifest.xml
  - Główne ustawienia aplikacji, GL ES, uprawnienia
* - android/otclientv8_lib/jni
  - Kod C/C++ (NDK), konfiguracje kompilacji
* - android/otclientv8_lib/libs/<abi>/
  - Artefakty `.so` dostarczane do APK/AAB (per ABI)
* - android/assets
  - Zasoby (data/, shaders/, configs/)
* - android/res
  - Layouty natywne Android (nie mylić z OTUI), ikonografia
```

## 3. ABI i biblioteki JNI

Obsługujemy: `armeabi-v7a`, `arm64-v8a`, `x86_64`. Każdy wariant generuje bibliotekę `libotclientv8.so`
o identycznym API JNI. Zalecenia:

- Wersjonowanie semantyczne w metadanych (np. `JNI_API=1`).
- Smoke-test ładowania na emulatorze dla każdego ABI.
- Weryfikacja symboli (`readelf -Ws` / `llvm-nm`) aby uniknąć konfliktów.

```{csv-table} android_libs
:header-rows: 1
:file: ../datasets/android_libs.csv
:widths: auto
```

(facet-14_android.libs)=

### Facet: `14_android.libs`

Identyfikator datasetu dla linterów QA.

## 4. Assets: pakowanie i spójność

Zasoby są wspólne (data/shaders/configs). Rekomendacje:

- **Hashing** w raporcie CI (nie w repo) – spójność między branchami.
- **Struktura** jak w projekcie desktopowym (`data/`, `shaders/`) dla łatwej synchronizacji.
- **Rozmiary** – unikaj plików > 5 MB; rozważ kompresję PNG/JPG przy zachowaniu jakości.

```{csv-table} android_assets
:header-rows: 1
:file: ../datasets/android_assets.csv
:widths: auto
```

(facet-14_android.assets)=

### Facet: `14_android.assets`

Ułatwia linkowanie w innych rozdziałach.

## 5. JNI: kontrakt i zdarzenia

Interfejs JNI obsługuje inicjalizację i zdarzenia wejścia. Przykładowe sygnatury:

```java
public class Bridge {
  static { System.loadLibrary("otclientv8"); }
  public static native void nativeInit(int width, int height);
  public static native void nativeEvent(int type, String payload);
}
```

Składnik C++ (mostek):

```cpp
extern "C" JNIEXPORT void JNICALL
Java_com_otclientv8_Bridge_nativeInit(JNIEnv* env, jclass, jint w, jint h) {
  Engine::instance().init(w, h);
}
```

## 6. CMake / Gradle (integracja)

Fragment `CMakeLists.txt`:

```cmake
add_library(otclientv8 SHARED
  src/main/cpp/main.cpp
  src/main/cpp/bridge_jni.cpp)

find_library(log-lib log)
target_link_libraries(otclientv8 PRIVATE ${log-lib})
target_compile_definitions(otclientv8 PRIVATE JNI_API=1)
```

Gradle (splity ABI i AAB):

```gradle
android {
  defaultConfig { ndk { abiFilters "armeabi-v7a","arm64-v8a","x86_64" } }
  bundle { abi { enableSplit = true } }
}
```

## 7. GL konfiguracja i wydajność

- Ustaw w Manifeście `android:glEsVersion="0x00020000"` (GLES2) lub wyżej.
- Dostosuj rozdzielczość bufora (np. `EGL_BUFFER_PRESERVED` zależnie od urządzenia).
- Włącz `android:largeHeap="true"` tylko jeśli to uzasadnione pamięciowo.

## 8. QA (Android)

- **abi-matrix** – wszystkie `.so` załadowane; raport zawiera ścieżkę i SHA.
- **asset-hash** – porównanie `assets/` z datasetami.
- **jni-signature** – porównanie sygnatur Java vs C++.
- **fps** – minimalny FPS na scenie testowej.

## 9. FAQ

**Czy można dodać zasób tylko dla jednego ABI?**  
Nie – assets są wspólne. ABI dotyczy wyłącznie `.so`.

**Jak debugować JNI?**  
Użyj LLDB w Android Studio, włącz symbole (`-g`) i nieobfuscowane nazwy.

---

## Aneks redakcyjny (merytoryczne uzupełnienia)

### Manifest (fragment GL ES)

```xml
<uses-feature android:glEsVersion="0x00020000" android:required="true"/>
```

### LLDB (kroki skrócone)

1) Build debug; 2) uruchom APK; 3) Attach LLDB do procesu.

### Skrypt CI (pseudo)

```bash
for abi in armeabi-v7a arm64-v8a x86_64; do
  adb install --abi $abi app.apk || exit 1
  adb shell am start -n com.otclientv8/.Main
  sleep 5; adb shell am force-stop com.otclientv8
done
```

## 10. Manifest minimalny (pełny przykład)

```xml
<manifest package="com.otclientv8" xmlns:android="http://schemas.android.com/apk/res/android">
  <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="34"/>
  <uses-feature android:glEsVersion="0x00020000" android:required="true"/>
  <uses-permission android:name="android.permission.INTERNET"/>
  <application android:label="@string/app_name" android:icon="@mipmap/ic_launcher">
    <activity android:name=".MainActivity"
      android:configChanges="orientation|keyboardHidden|screenSize">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>
  </application>
</manifest>
```

## 11. Konfiguracja Gradle (KTS) i NDK flags

```kotlin
android {
  defaultConfig {
    ndk { abiFilters += listOf("armeabi-v7a","arm64-v8a","x86_64") }
    externalNativeBuild {
      cmake {
        cppFlags += "-std=c++17 -fvisibility=hidden -fno-exceptions -fno-rtti"
        arguments += listOf("-DANDROID_STL=c++_shared","-DJNI_API=1")
      }
    }
  }
  buildTypes {
    getByName("release") { isMinifyEnabled = false }
  }
}
```

## 12. Wysyłka AAB i testy na Play

- Zbuduj `:app:bundleRelease`.
- Sprawdź *ABI splits* w `bundletool dump manifest`.
- Przetestuj instalację dynamiczną: `bundletool install-apks` na każdym ABI.

## 13. Obsługa rotacji i powierzchni GL

- Użyj `onConfigurationChanged` aby odświeżyć viewport.
- Utrzymuj proporcje UI: przelicz anchory i paddingi po zmianie orientacji.
- Testuj `EGL_SWAP_BEHAVIOR_PRESERVED_BIT` vs wymuszony clear.

## 14. Skrypty pomocnicze (bash/powershell)

```bash
#!/usr/bin/env bash
set -e
ABIS=("armeabi-v7a" "arm64-v8a" "x86_64")
for abi in "${ABIS[@]}"; do
  echo ":: Testing $abi"
  adb shell setprop debug.otc.abi "$abi" || true
  adb shell am start -n com.otclientv8/.Main
  sleep 3
  adb shell am force-stop com.otclientv8
done
```

## Dodatek: przykłady konfiguracyjne (unikalne)

### Przykład 1

```text
Case-1: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 2

```text
Case-2: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 3

```text
Case-3: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 4

```text
Case-4: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 5

```text
Case-5: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 6

```text
Case-6: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 7

```text
Case-7: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 8

```text
Case-8: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 9

```text
Case-9: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 10

```text
Case-10: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 11

```text
Case-11: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 12

```text
Case-12: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 13

```text
Case-13: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 14

```text
Case-14: Opis konkretnego kroku integracji bez powtórzeń.
```

### Przykład 15

```text
Case-15: Opis konkretnego kroku integracji bez powtórzeń.
```

## 15. JNI — nagłówek i implementacja

Plik Java:

```java
package com.otclientv8;
public final class Bridge {
  static { System.loadLibrary("otclientv8"); }
  public static native void nativeInit(int width, int height);
  public static native void nativeEvent(int type, String payload);
}
```

C++ (bridge):

```cpp
#include <jni.h>
#include "Engine.hpp"
extern "C" JNIEXPORT void JNICALL
Java_com_otclientv8_Bridge_nativeEvent(JNIEnv* env, jclass, jint type, jstring payload){
  const char* s = env->GetStringUTFChars(payload, nullptr);
  Engine::instance().onEvent(type, s);
  env->ReleaseStringUTFChars(payload, s);
}
```

## 16. Mapowanie zdarzeń wejścia

```{list-table} Event map
:header-rows: 1
* - typ
  - payload (JSON)
  - opis
* - 1
  - {"x":128,"y":64,"action":"down"}
  - Dotyk/mysz — wciśnięcie
* - 2
  - {"x":130,"y":64,"action":"move"}
  - Ruch
* - 3
  - {"action":"key","code":13}
  - Klawiatura — Enter
```

## 17. Debug i profilowanie

- `adb logcat | grep OTC` — logi modułów
- Perfetto/Android Studio Profiler — CPU/Memory
- `systrace` — analiza klatek GL

## 18. Zarządzanie pamięcią i GL

- Utrzymuj `EGLContext` podczas `onPause` jeśli to możliwe (oszczędność czasu na kompilację shaderów).
- W przeciwnym razie — szybkie odtworzenie zasobów po `onResume` (cache shaderów).

## 19. Publikacja na urządzeniach klasy low-end

- Redukuj rozmiar atlasów (podział na segmenty).
- Ogranicz alpha-blend w UI (tańsze compositing).

## 20. Tabela problemów i rozwiązań

```{list-table} Troubleshooting
:header-rows: 1
* - problem
  - diagnoza
  - rozwiązanie
* - java.lang.UnsatisfiedLinkError
  - Brak `.so` dla ABI
  - Dodaj do `abiFilters`, sprawdź `lib/` w APK
* - czarny ekran po starcie
  - Brak GL surface / błąd EGL
  - Zweryfikuj `glEsVersion`, sekwencję init
* - input lag
  - Zbyt długie event loop
  - Batchuj zdarzenia, profiluj w profilerze
```

## 21. Konfiguracja symboli i crash dump

- Włącz `-g` i zachowaj `*.so` z symbolami dla deobfuskacji.
- Użyj `ndk-stack` do analizy zrzutów.

## 22. Przykładowy pipeline CI (YAML szkic)

```yaml
steps:
  - script: ./gradlew :app:assembleRelease
  - script: ./gradlew :app:bundleRelease
  - script: ./gradlew :app:connectedCheck
  - publish: app/build/outputs
```

## 23. Testy instrumentacyjne (szkic)

```java
@RunWith(AndroidJUnit4.class)
public class SmokeTest {
  @Test public void appStarts() {
    ActivityScenario<MainActivity> s = ActivityScenario.launch(MainActivity.class);
    assertNotNull(s);
  }
}
```

## 24. Proguard/R8 — reguły zachowania JNI

```proguard
-keep class com.otclientv8.Bridge { *; }
-keepclassmembers class * {
    native <methods>;
}
```

Komentarz: zachowujemy klasę mostka JNI i metody natywne, aby uniknąć stripowania.

## 25. CMake — użycie prebuiltów i OpenMP (opcjonalnie)

```cmake
add_library(otclientv8 SHARED IMPORTED GLOBAL)
set_target_properties(otclientv8 PROPERTIES
  IMPORTED_LOCATION_${CMAKE_BUILD_TYPE} ${CMAKE_SOURCE_DIR}/prebuilt/${ANDROID_ABI}/libotclientv8.so
  IMPORTED_NO_SONAME TRUE)
# Przykład dodatkowej biblioteki:
find_library(android-log log)
# OpenMP (jeśli wykorzystywany w przetwarzaniu):
find_package(OpenMP)
if(OpenMP_CXX_FOUND)
  target_link_libraries(${PROJECT_NAME} PRIVATE OpenMP::OpenMP_CXX)
endif()
```

## 26. Podpisywanie i konfiguracja release

```properties
# gradle.properties (przykład)
RELEASE_STORE_FILE=/keystore/release.jks
RELEASE_STORE_PASSWORD=***
RELEASE_KEY_ALIAS=otc
RELEASE_KEY_PASSWORD=***
```

```kotlin
android { 
  signingConfigs {
    create("release") {
      storeFile = file(prop("RELEASE_STORE_FILE"))
      storePassword = prop("RELEASE_STORE_PASSWORD")
      keyAlias = prop("RELEASE_KEY_ALIAS")
      keyPassword = prop("RELEASE_KEY_PASSWORD")
    }
  }
}
```

## 27. Weryfikacja zawartości APK/AAB

```bash
unzip -l app-release.apk | grep -E "lib/|assets/"
bundletool dump manifest --bundle app-release.aab | sed -n '1,80p'
```

## 28. Rozwiązywanie problemów GL na różnych GPU

- Ustaw ręcznie format bufora kolorów (RGB565 vs RGBA8888) podczas wyboru konfiguracji.

- Sprawdź `EGL_SWAP_BEHAVIOR` i wymuś clear klatki jeśli tearing/ghosting.

- Przy problemach z precision — ustaw `precision mediump float` w shaderach UI.

## 29. Rozszerzona FAQ

**Czy muszę dodawać `c++_shared.so`?** — Tylko jeśli linkujesz do c++_shared; preferuj `-static` gdy to możliwe.  
**Jak rejestrować klucze w input?** — Twórz mapę `AndroidKeyCode -> EngineKey`.  
**Czy tryb fullscreen wymaga specjalnych flag?** — Tak, użyj `WindowCompat.setDecorFitsSystemWindows(window, false)` i ukryj system bars.

## 30. Przykłady logcat filtrów

```bash
adb logcat | grep -E "OTC|EGL|GLES|JNI"
```

## 31. Przykładowa MainActivity (GLSurfaceView)

```java
public class MainActivity extends Activity {
  private GLSurfaceView glView;
  @Override protected void onCreate(Bundle s) {
    super.onCreate(s);
    glView = new GLSurfaceView(this);
    glView.setEGLContextClientVersion(2);
    glView.setRenderer(new Renderer());
    setContentView(glView);
  }
  @Override protected void onPause(){ super.onPause(); glView.onPause(); }
  @Override protected void onResume(){ super.onResume(); glView.onResume(); }
}
```

Uwaga: w niektórych projektach korzystamy z natywnego EGL, ale GLSurfaceView upraszcza cykl życia.

## 32. ANR i watchdog

- Główna pętla nie może wykonywać ciężkich operacji I/O — przenieś do wątków pomocniczych.

- Włącz sygnalizację „frame time” — jeśli > 16.6 ms (60 FPS), loguj ostrzeżenie.

## 33. Matryca urządzeń (przykładowa)

```{list-table} Devices
:header-rows: 1
* - producent
  - model
  - ABI
  - uwagi
* - Google
  - Pixel 6
  - arm64-v8a
  - OK
* - Samsung
  - A52
  - arm64-v8a
  - Wymaga mniejszego atlasu
* - Emulator
  - x86_64
  - x86_64
  - Test wejścia i rotacji
```

## 34. Zasady logowania

- Prefiksuj logi `OTC/` + komponent (np. `OTC/Engine`).

- Ogranicz spam w RELEASE; podnieś poziom w DEBUG.

## 35. Dodatkowe przykłady Gradle

```gradle
android {
  packagingOptions {
    jniLibs.keepDebugSymbols += ["**/*.so"]
  }
  aaptOptions { cruncherEnabled = false }
}
```

## 36. Android.mk / ndk-build (alternatywa)

```make
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE    := otclientv8
LOCAL_SRC_FILES := main.cpp bridge_jni.cpp
LOCAL_LDLIBS    := -llog -landroid
LOCAL_CPPFLAGS  := -std=c++17 -fvisibility=hidden -fno-exceptions -fno-rtti -DJNI_API=1
include $(BUILD_SHARED_LIBRARY)
```

## 37. Wątki JNI — attach/detach

```cpp
JavaVM* g_vm = nullptr;
jint JNI_OnLoad(JavaVM* vm, void*){ g_vm = vm; return JNI_VERSION_1_6; }
void postToJava(std::function<void(JNIEnv*)> fn){
  JNIEnv* env=nullptr; bool detach=false;
  if(g_vm->GetEnv((void**)&env, JNI_VERSION_1_6) != JNI_OK){
    g_vm->AttachCurrentThread(&env, nullptr); detach=true;
  }
  fn(env);
  if(detach) g_vm->DetachCurrentThread();
}
```

## 38. Cykl powierzchni (edge-case)

- `SurfaceTexture` może zostać zniszczona podczas `onPause`; odtwórz kontekst lub zasoby po `onResume`.

- Różne urządzenia stosują inne strategie; przygotuj ścieżki fallback.

## 39. Zaawansowane reguły R8 (przykład)

```proguard
# Zachowaj klasy z adnotacją @Keep
-keep @interface androidx.annotation.Keep
-keep @androidx.annotation.Keep class * { *; }
-keepclasseswithmembernames class * { @androidx.annotation.Keep *; }
```

## 40. Dodatkowe testy E2E

- Automatyczne klikanie w UI (UIAutomator/Espresso) — sprawdzanie reakcji i stabilności.

- Długie sesje (30 min) — wycieki pamięci i stabilność FPS.

## 41. GLSurfaceView.Renderer (szkic implementacji)

```java
final class Renderer implements GLSurfaceView.Renderer {
  @Override public void onSurfaceCreated(GL10 gl, EGLConfig cfg) {
    Bridge.nativeInit(0, 0); // silnik sam wykryje wymiary
  }
  @Override public void onSurfaceChanged(GL10 gl, int w, int h) {
    Bridge.nativeEvent(100, "{"resize":"+w+"x"+h+"}");
  }
  @Override public void onDrawFrame(GL10 gl) {
    Bridge.nativeEvent(200, "{"tick":1}");
  }
}
```

## 42. Sterowanie energią i wydajnością

- Uśpij pętlę renderu przy braku aktywnych animacji (oszczędność baterii).

- Ogranicz liczbę alokacji w `onDrawFrame` — używaj buforów stałych.

## 43. Skanowanie APK pod kątem rozmiaru

```bash
zipinfo -l app-release.apk | sort -k1,1 -nr | head -n 50
```

## 44. Wytyczne dotyczące wersjonowania aplikacji

- `versionCode` rośnie monotonicznie; `versionName` odzwierciedla semver.

- ABIs nie wpływają na `versionCode` przy AAB (splity generowane przez Play).

```gradle
android { defaultConfig { versionCode 102; versionName "1.0.2" } }
```

## 45. Obsługa rotacji — przykład

```java
@Override public void onConfigurationChanged(Configuration newConfig){
  super.onConfigurationChanged(newConfig);
  int w = getWindow().getDecorView().getWidth();
  int h = getWindow().getDecorView().getHeight();
  Bridge.nativeEvent(101, "{"rotate":"+w+"x"+h+"}");
}
```

## 46. Pseudokod hashowania assets

```python
import hashlib, pathlib, json
def dir_hash(p):
  h = hashlib.sha256()
  for f in sorted(pathlib.Path(p).rglob('*')):
    if f.is_file():
      h.update(f.name.encode()); h.update(f.read_bytes())
  return h.hexdigest()
print(json.dumps({
  "data": dir_hash("assets/data"),
  "shaders": dir_hash("assets/shaders"),
  "configs": dir_hash("assets/configs"),
}, indent=2))
```

## 47. Sprawdzanie klasy pamięci i budżetu tekstur

```java
ActivityManager am = (ActivityManager)getSystemService(ACTIVITY_SERVICE);
ActivityManager.MemoryInfo mi = new ActivityManager.MemoryInfo();
am.getMemoryInfo(mi);
Log.i("OTC/MEM", "availMB=" + (mi.availMem/1024/1024));
```

## 48. Skrypt testów ABI (szerszy)

```bash
#!/usr/bin/env bash
set -euo pipefail
APKS=app/build/outputs/apk/release/app-release.apk
for abi in armeabi-v7a arm64-v8a x86_64; do
  echo "== Testing ${abi} =="
  if unzip -l "$APKS" | grep -q "lib/${abi}/libotclientv8.so"; then
    echo "OK: lib present"
  else
    echo "MISSING: ${abi}"
    exit 1
  fi
done
```

## 49. Dodatkowe wskazówki publikacyjne

- Ustaw kategorię gry/aplikacji w Play, dodaj zrzuty 7-cal/10-cal.

- Zadbaj o krótkie i długie opisy w dwóch językach.
