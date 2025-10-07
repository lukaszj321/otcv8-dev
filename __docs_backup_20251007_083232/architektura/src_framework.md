# src framework
## PoniLLej znajduje sie kompletna dokumentacja techniczna dla repozytorium, src/framework
## Opis ogolny

Plik `const.h` peL'ni role centralnego repozytorium dla staL'ych, makr i typow wyliczeniowych (enum) uLLywanych w caL'ym frameworku. Definiuje on kluczowe wartoLci, takie jak kody klawiszy, poziomy logowania, flagi wyrownania, przyciski myszy, a takLLe staL'e matematyczne i makra kompilacji. Jest to fundamentalny plik nagL'owkowy, ktory zapewnia spojnoLc i czytelnoLc kodu poprzez zdefiniowanie nazwanych staL'ych zamiast "magicznych liczb".
## Definicje i Makra
## Makra matematyczne

-   `DEG_TO_RAD`: SL'uLLy do konwersji stopni na radiany.
# define DEG_TO_RAD (acos(-1)/180.0)
```
-   `RAD_TO_DEC`: SL'uLLy do konwersji radianow na stopnie.
# define RAD_TO_DEC (180.0/acos(-1))
```
## Makra budowania (Build Macros)

Makra te sa definiowane podczas kompilacji i dostarczaja informacji o wersji i Lrodowisku budowania.

-   `BUILD_COMMIT`: Przechowuje hash commita Git. DomyLlnie "dev".
# ifndef BUILD_COMMIT
# define BUILD_COMMIT "dev"
# endif
```
-   `BUILD_REVISION`: Przechowuje numer rewizji. DomyLlnie 0.
# ifndef BUILD_REVISION
# define BUILD_REVISION 0
# endif
```
-   `BUILD_TYPE`: OkreLla typ budowania (np. "release", "debug"). DomyLlnie "unknown".
# ifndef BUILD_TYPE
# define BUILD_TYPE "unknown"
# endif
```
-   `BUILD_ARCH`: OkreLla architekture procesora (x64, x86). Wykrywane automatycznie, jeLli nie jest zdefiniowane.
# ifndef BUILD_ARCH
# if defined(__amd64) || defined(_M_X64)
# define BUILD_ARCH "x64"
# elif defined(__i386) || defined(_M_IX86) || defined(_X86_)
# define BUILD_ARCH "x86"
# else
# define BUILD_ARCH "unknown"
# endif
# endif
```
## Namespace `Fw`

PrzestrzeL" nazw `Fw` (skrot od Framework) grupuje wszystkie staL'e i typy wyliczeniowe, aby uniknac konfliktow nazw w globalnej przestrzeni nazw.
## Zmienne globalne

-   `pi`: StaL'a matematyczna przechowujaca przybliLLona wartoLc liczby Pi.
    static const float pi = 3.14159265;
```
-   `MIN_ALPHA`: Minimalna wartoLc alfa (przezroczystoLci), poniLLej ktorej obiekty moga byc uznawane za w peL'ni przezroczyste.
    static const float MIN_ALPHA = 0.003f;
```
## Typy wyliczeniowe (Enums)
## `enum Key`

Definiuje kody klawiszy klawiatury. WartoLci liczbowe dla klawiszy drukowalnych odpowiadaja ich kodom ASCII.

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `KeyUnknown` | 0 | Nieznany klawisz |
| `KeyEscape` | 1 | Klawisz Escape |
| `KeyTab` | 2 | Klawisz Tab |
| `KeyBackspace` | 3 | Klawisz Backspace |
| `KeyEnter` | 5 | Klawisz Enter/Return |
| ... | ... | ... |
| `KeyNumpad9` | 150 | Klawisz 9 na klawiaturze numerycznej |
## `enum LogLevel`

Definiuje poziomy waLLnoLci dla komunikatow w systemie logowania.

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `LogDebug` | 0 | WiadomoLci debugowania |
| `LogInfo` | 1 | Informacje ogolne |
| `LogWarning` | 2 | OstrzeLLenia |
| `LogError` | 3 | BL'edy |
| `LogFatal` | 4 | BL'edy krytyczne, powodujace zamkniecie aplikacji |
## `enum AspectRatioMode`

OkreLla, w jaki sposob zachowac proporcje obrazu podczas skalowania.

| Nazwa | Opis |
| :--- | :--- |
| `IgnoreAspectRatio` | Ignoruje proporcje, rozciagajac obraz do peL'nego rozmiaru. |
| `KeepAspectRatio` | Zachowuje proporcje, dopasowujac obraz do mniejszego wymiaru. |
| `KeepAspectRatioByExpanding` | Zachowuje proporcje, wypeL'niajac caL'y obszar (moLLe przyciac obraz). |
## `enum AlignmentFlag`

Flagi bitowe uLLywane do okreLlania wyrownania tekstu lub widgetow w kontenerze. MoLLna je L'aczyc za pomoca operatora `|`.

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `AlignNone` | 0 | Brak wyrownania |
| `AlignLeft` | 1 | Wyrownanie do lewej |
| `AlignRight` | 2 | Wyrownanie do prawej |
| `AlignTop` | 4 | Wyrownanie do gory |
| `AlignBottom` | 8 | Wyrownanie do doL'u |
| `AlignHorizontalCenter` | 16 | WyLrodkowanie w poziomie |
| `AlignVerticalCenter` | 32 | WyLrodkowanie w pionie |
| `AlignCenter` | 48 | PeL'ne wyLrodkowanie (kombinacja `HorizontalCenter` i `VerticalCenter`) |
| ... | ... | Inne kombinacje |
## `enum AnchorEdge`

Definiuje krawedzie, do ktorych moLLna "zakotwiczyc" widget w layoucie typu `UIAnchorLayout`.

| Nazwa | Opis |
| :--- | :--- |
| `AnchorNone` | Brak zakotwiczenia |
| `AnchorTop` | Gorna krawedLs |
| `AnchorBottom` | Dolna krawedLs |
| ... | ... |
## `enum FocusReason`

OkreLla przyczyne, dla ktorej widget otrzymaL' fokus.

| Nazwa | Opis |
| :--- | :--- |
| `MouseFocusReason` | Fokus uzyskany przez klikniecie mysza. |
| `KeyboardFocusReason` | Fokus uzyskany przez nawigacje klawiatura (np. Tab). |
| `ActiveFocusReason` | Fokus ustawiony programowo. |
| `OtherFocusReason` | Inna przyczyna. |
## `enum AutoFocusPolicy`

Definiuje, jak widget-rodzic powinien automatycznie ustawiac fokus na swoich dzieciach.

| Nazwa | Opis |
| :--- | :--- |
| `AutoFocusNone` | Brak automatycznego fokusa. |
| `AutoFocusFirst` | Ustawia fokus na pierwszym dziecku, ktore moLLe go otrzymac. |
| `AutoFocusLast` | Ustawia fokus na ostatnim dziecku, ktore moLLe go otrzymac. |
## `enum InputEventType`

Definiuje typy zdarzeL" wejLciowych (klawiatura, mysz).

| Nazwa | Opis |
| :--- | :--- |
| `NoInputEvent` | Brak zdarzenia. |
| `KeyTextInputEvent` | Zdarzenie wprowadzenia tekstu. |
| `KeyDownInputEvent` | Zdarzenie wciLniecia klawisza. |
| `KeyPressInputEvent` | Zdarzenie przytrzymania klawisza (auto-powtarzanie). |
| ... | ... |
## `enum MouseButton`

Definiuje przyciski myszy oraz dotyk.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoButton` | Brak przycisku. |
| `MouseLeftButton` | Lewy przycisk myszy. |
| ... | ... |
## `enum MouseWheelDirection`

Definiuje kierunek przewijania koL'kiem myszy.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoWheel` | Brak przewijania. |
| `MouseWheelUp` | Przewijanie w gore. |
| `MouseWheelDown` | Przewijanie w doL'. |
## `enum KeyboardModifier`

Flagi bitowe dla klawiszy modyfikujacych (Ctrl, Alt, Shift).

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `KeyboardNoModifier` | 0 | Brak modyfikatora. |
| `KeyboardCtrlModifier` | 1 | WciLniety Ctrl. |
| `KeyboardAltModifier` | 2 | WciLniety Alt. |
| `KeyboardShiftModifier` | 4 | WciLniety Shift. |
## `enum WidgetState`

Flagi bitowe definiujace stan widgetu (np. aktywny, najechany, wciLniety). ULLywane do dynamicznego stylowania widgetow.

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `InvalidState` | -1 | NieprawidL'owy stan. |
| `DefaultState` | 0 | Stan domyLlny. |
| `ActiveState` | 1 | Widget jest aktywny. |
| `FocusState` | 2 | Widget ma fokus. |
| `HoverState` | 4 | Kursor myszy jest nad widgetem. |
| ... | ... | ... |
## `enum DrawPane`

OkreLla warstwe rysowania dla widgetow, co pozwala na kontrolowanie kolejnoLci renderowania.

| Nazwa | WartoLc | Opis |
| :--- | :--- | :--- |
| `ForegroundPane` | 1 | Warstwa pierwszoplanowa (interfejs uLLytkownika). |
| `MapBackgroundPane` | 2 | TL'o mapy gry. |
| `MapForegroundPane` | 3 | Pierwszy plan mapy gry (np. efekty nad postaciami). |
## ZaleLLnoLci i powiazania

-   `framework/stdext/compiler.h`: Plik ten dostarcza makr i definicji specyficznych dla kompilatora (np. `BUILD_COMPILER`).

---
# z"" CMakeLists.txt
## Opis ogolny

Plik `CMakeLists.txt` jest gL'ownym skryptem konfiguracyjnym dla systemu budowania CMake. Jego rola jest zdefiniowanie, jak projekt `otclient` ma byc kompilowany. OkreLla on flagi kompilatora, zaleLLnoLci od bibliotek zewnetrznych, liste plikow LsrodL'owych oraz opcje konfiguracyjne, ktore pozwalaja dostosowac proces budowania do roLLnych platform (Windows, Linux, Apple, WebAssembly) i potrzeb (np. wL'aczenie/wyL'aczenie obsL'ugi dLswieku, grafiki, sieci).
## Opcje budowania

Skrypt definiuje kilka opcji, ktore moLLna kontrolowac podczas generowania projektu.

| Opcja | DomyLlnie | Opis |
| :--- | :--- | :--- |
| `LUAJIT` | `ON` | ULLywa LuaJIT zamiast standardowej biblioteki Lua. |
| `CRASH_HANDLER` | `ON` (poza Apple) | WL'acza generowanie raportow po awarii aplikacji. |
| `USE_STATIC_LIBS`| `ON` (poza Apple) | Linkuje biblioteki statycznie zamiast dynamicznie (DLL). |
| `USE_LIBCPP` | `OFF` (dla Apple `ON`)| ULLywa `libc++` zamiast `stdc++`. |
| `USE_LTO` | `OFF` | WL'acza optymalizacje w czasie linkowania (Link Time Optimizations). |
| `OPENGLES` | `OFF` | ULLywa OpenGL ES zamiast standardowego OpenGL. Dostepne wersje "1.0", "2.0". |
| `WINDOWS_CONSOLE`| `OFF` | WL'acza okno konsoli w systemie Windows. |
## Flagi frameworka

Skrypt uLLywa flag preprocesora do warunkowej kompilacji moduL'ow:
-   `FRAMEWORK_SOUND`: WL'acza kompilacje moduL'u dLswieku.
-   `FRAMEWORK_GRAPHICS`: WL'acza kompilacje moduL'u grafiki.
-   `FRAMEWORK_NET`: WL'acza kompilacje moduL'u sieciowego.
-   `FRAMEWORK_XML`: WL'acza kompilacje moduL'u do parsowania XML (TinyXML).
-   `FRAMEWORK_THREAD_SAFE`: Dodaje definicje `THREAD_SAFE`, prawdopodobnie dla kodu wielowatkowego.
## Struktura projektu (pliki LsrodL'owe)

Plik definiuje liste wszystkich plikow LsrodL'owych (`.h`, `.cpp`, `.c`) skL'adajacych sie na framework. Sa one pogrupowane w logiczne moduL'y:

-   **GL'owne pliki**: `const.h`, `global.h`, `pch.h`, `luafunctions.cpp`
-   **`util`**: Narzedzia pomocnicze (kolory, kryptografia, obsL'uga PNG, struktury danych jak `Rect`, `Point`).
-   **`stdext`**: Rozszerzenia standardowej biblioteki C++ (obsL'uga stringow, czasu, rzutowania typow, watkow).
-   **`core`**: RdzeL" aplikacji (petla gL'owna, obsL'uga zdarzeL", logowanie, zarzadzanie moduL'ami i zasobami).
-   **`luaengine`**: Silnik Lua i mechanizmy bindowania C++ do Lua.
-   **`otml`**: Parser i emiter dla jezyka OTML (OTClient Markup Language).
-   **`platform`**: Kod specyficzny dla platformy (obsL'uga okien, obsL'uga awarii).
-   **`graphics` (warunkowo)**: Silnik graficzny (OpenGL, shadery, tekstury, fonty, UI).
-   **`sound` (warunkowo)**: Silnik dLswieku (OpenAL, obsL'uga OGG Vorbis).
-   **`net` (warunkowo)**: ObsL'uga sieci (poL'aczenia, protokoL'y, serwer, proxy).
-   **`xml` (warunkowo)**: Parser TinyXML.
## ZaleLLnoLci i powiazania

Skrypt wyszukuje i linkuje nastepujace biblioteki zewnetrzne:
-   **Boost** (`system`, `filesystem`): ULLywane do operacji na systemie plikow i innych podstawowych funkcjonalnoLci.
-   **ZLIB, BZip2, LibZip**: Do kompresji i dekompresji danych.
-   **LuaJIT** lub **Lua**: Silnik skryptowy.
-   **PhysFS**: Wirtualny system plikow, do obsL'ugi zasobow w archiwach.
-   **OpenSSL**: Do funkcji kryptograficznych (RSA, SHA, MD5).
-   **OpenGL/OpenGLES, EGL**: Do renderowania grafiki.
-   **GLEW**: Do zarzadzania rozszerzeniami OpenGL.
-   **OpenAL, Vorbis, Ogg**: Do obsL'ugi dLswieku.
## Konfiguracja dla WebAssembly (WASM)
Specjalny blok `if(WASM)` dostosowuje kompilacje dla platformy WebAssembly przy uLLyciu Emscripten. Ustawia specyficzne flagi (`-s USE_ZLIB=1`, etc.), linkuje prekompilowane biblioteki (`.a`) i doL'acza LsrodL'a Lua bezpoLrednio do projektu, zamiast linkowac je jako zewnetrzna biblioteke.
## Flagi kompilatora
Skrypt ustawia roLLne flagi kompilatora w zaleLLnoLci od typu budowania (`CMAKE_BUILD_TYPE`):
-   **Debug**: `-O0 -g` (niska optymalizacja, peL'ne informacje debugowania).
-   **Release**: `-O2` (wysoka optymalizacja, brak informacji debugowania).
-   **RelWithDebInfo**: `-O1 -g` (Lrednia optymalizacja z informacjami debugowania).
-   **Performance**: `-Ofast -march=native` (najwyLLsze optymalizacje, specyficzne dla architektury).

---
# z"" global.h
## Opis ogolny

Plik `global.h` jest jednym z kluczowych plikow nagL'owkowych w frameworku. Jego gL'ownym zadaniem jest wL'aczenie najwaLLniejszych, globalnie uLLywanych definicji i nagL'owkow w jednym miejscu. Dzieki temu inne pliki moga doL'aczyc tylko ten jeden plik, aby uzyskac dostep do podstawowych typow danych, staL'ych, makr i narzedzi.
## Definicje i Makra
## `VALIDATE(expression)`

Jest to makro asercji, ktore jest aktywne tylko w trybie debugowania (gdy `NDEBUG` nie jest zdefiniowane). JeLli wyraLLenie (expression) jest faL'szywe, makro wywoL'uje funkcje `fatalError`, ktora przerywa dziaL'anie programu i wyLwietla komunikat o bL'edzie zawierajacy nazwe pliku i numer linii. W trybie wydajnoLciowym (`NDEBUG` zdefiniowane) makro jest puste i nie generuje LLadnego kodu.

# if defined(NDEBUG)
# define VALIDATE(expression) ((void)0)
# else
extern void fatalError(const char* error, const char* file, int line);
# define VALIDATE(expression) { if(!(expression)) fatalError(#expression, __FILE__, __LINE__); };
# endif
```
-   **ULLycie**: SL'uLLy do sprawdzania warunkow, ktore musza byc zawsze prawdziwe w trakcie dziaL'ania programu, np. sprawdzania, czy wskaLsnik nie jest `nullptr`.
## ZaleLLnoLci i powiazania

Plik `global.h` wL'acza nastepujace nagL'owki, udostepniajac ich zawartoLc wszystkim plikom, ktore go doL'aczaja:

-   `framework/stdext/compiler.h`: Zawiera definicje specyficzne dla kompilatora.
-   `framework/pch.h`: Prekompilowany nagL'owek, ktory zawiera standardowe biblioteki C/C++ oraz biblioteki firm trzecich, takie jak Boost.
-   `framework/const.h`: Definiuje globalne staL'e, makra i typy wyliczeniowe (enumy).
-   `framework/stdext/stdext.h`: Zawiera rozszerzenia standardowej biblioteki C++, takie jak dodatkowe algorytmy.
-   `framework/util/point.h`, `color.h`, `rect.h`, `size.h`, `matrix.h`: Definiuja podstawowe struktury danych uLLywane w grafice i logice.
-   `framework/core/logger.h`: Udostepnia globalny obiekt `g_logger` do logowania komunikatow.

Dzieki temu `global.h` dziaL'a jako centralny punkt dostepu do najczeLciej uLLywanych elementow frameworka.

---
# z"" pch.h
## Opis ogolny

`pch.h` (Precompiled Header) to plik nagL'owkowy, ktorego celem jest przyspieszenie procesu kompilacji. Zawiera on dyrektywy `#include` dla nagL'owkow, ktore sa czesto uLLywane w caL'ym projekcie, ale rzadko sie zmieniaja. Kompilator moLLe wstepnie przetworzyc ten plik i zapisac jego stan, co pozwala na ponowne wykorzystanie go podczas kompilacji innych plikow LsrodL'owych, zamiast parsowac te same nagL'owki wielokrotnie.
## ZawartoLc pliku

Plik ten jest podzielony na kilka sekcji, grupujacych nagL'owki wedL'ug ich pochodzenia i przeznaczenia.
## Standardowe nagL'owki C

Zawiera podstawowe nagL'owki z biblioteki standardowej C, takie jak `cstdio`, `cstdlib`, `cstring`, `cmath`.

# include <cstdio>
# include <cstdlib>
# include <cstddef>
# include <cstring>
# include <cmath>
```
## Standardowe nagL'owki STL (C++)

WL'acza najwaLLniejsze i najczeLciej uLLywane kontenery, strumienie i algorytmy z biblioteki standardowej C++.

# include <iostream>
# include <sstream>
# include <string>
# include <vector>
# include <set>
# include <list>
# include <deque>
# include <map>
# include <algorithm>
# include <functional>
# include <array>
# include <unordered_map>
# include <unordered_set>
# include <tuple>
# include <iomanip>
# include <typeinfo>
```
## Nowoczesne nagL'owki C++ (C++11 i nowsze)

WL'acza nagL'owki zwiazane z wielowatkowoLcia, inteligentnymi wskaLsnikami, czasem i losowoLcia, wprowadzone w nowszych standardach C++. Plik `filesystem` jest doL'aczany warunkowo (poza Androidem).

# include <thread>
# include <memory>
# include <functional>
# include <condition_variable>
# include <mutex>
# include <future>
# include <chrono>
# include <random>
# ifndef ANDROID
# include <filesystem>
# endif
```
## Biblioteka Boost

WL'acza nagL'owki z biblioteki Boost, gL'ownie z moduL'ow **Asio** (do operacji sieciowych) i **Beast** (do obsL'ugi protokoL'ow HTTP i WebSocket).

-   `boost/system/config.hpp`, `error_code.hpp`: Podstawowe elementy systemu Boost.
-   `boost/asio.hpp`, `beast.hpp`: GL'owne nagL'owki dla Asio i Beast.
-   NagL'owki warunkowe dla SSL (`__EMSCRIPTEN__` wyL'acza je, poniewaLL obsL'uga SSL w przegladarce jest inna).
-   `boost/algorithm/hex.hpp`: Do operacji na systemie szesnastkowym.

# ifdef ANDROID
# define BOOST_UUID_RANDOM_PROVIDER_FORCE_POSIX
# endif
# include <boost/system/config.hpp>
// ... (inne nagL'owki boost)
```
## ZaleLLnoLci i powiazania

Plik `pch.h` jest plikiem "liLciem" w hierarchii zaleLLnoLci - sam nie zaleLLy od innych plikow projektu. JednakLLe, jest on doL'aczany przez `global.h`, co czyni go poLrednia zaleLLnoLcia dla niemal kaLLdego pliku w projekcie. Zapewnia on dostep do szerokiej gamy narzedzi z biblioteki standardowej C++ i Boost.

---
# z"" luafunctions.cpp
## Opis ogolny

Plik `luafunctions.cpp` implementuje metode `Application::registerLuaFunctions()`, ktora jest kluczowym elementem integracji silnika C++ z Lua. Funkcja ta jest odpowiedzialna za zarejestrowanie (zbindowanie) klas, funkcji i obiektow singletonowych z C++ w globalnym Lrodowisku Lua. Dzieki temu skrypty Lua moga wywoL'ywac funkcje C++, tworzyc obiekty C++ (np. widgety UI) i manipulowac nimi, co stanowi podstawe modularnoLci i rozszerzalnoLci klienta.
## `Application::registerLuaFunctions()`
## Opis semantyczny

Metoda ta jest wywoL'ywana jednorazowo podczas inicjalizacji aplikacji (`Application::init`). Przechodzi przez wszystkie gL'owne moduL'y frameworka (takie jak `Platform`, `Application`, `Crypt`, `ResourceManager`, `UIManager` itd.) i udostepnia ich publiczne API w Lrodowisku Lua. KaLLdy zarejestrowany element staje sie dostepny w Lua jako zmienna globalna (np. `g_app`, `g_crypt`) lub jako klasa (np. `UIWidget`).
## Zarejestrowane elementy

PoniLLej znajduje sie lista zarejestrowanych elementow pogrupowanych wedL'ug moduL'ow.
## Konwersje i narzedzia globalne

Rejestruje globalne funkcje pomocnicze w Lua do konwersji typow danych miedzy stringami a obiektami C++ oraz inne narzedzia.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `torect` | `stdext::from_string<Rect>` | Konwertuje string na obiekt `Rect`. |
| `topoint` | `stdext::from_string<Point>` | Konwertuje string na obiekt `Point`. |
| `ucwords` | `stdext::ucwords` | Zamienia pierwsza litere kaLLdego sL'owa na wielka. |
| `regexMatch` | `lambda` | Wyszukuje dopasowania wyraLLeL" regularnych w stringu. |
| ... | ... | ... |
## Platform (`g_platform`)

Udostepnia funkcje zwiazane z systemem operacyjnym. Niektore funkcje sa dostepne tylko gdy zdefiniowano `UNSAFE_LUA_FUNCTIONS`.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `spawnProcess` | `Platform::spawnProcess` | Uruchamia nowy proces (niebezpieczne). |
| `getProcessId` | `Platform::getProcessId` | Zwraca ID bieLLacego procesu. |
| `openUrl` | `Platform::openUrl` | Otwiera podany URL w domyLlnej przegladarce. |
| `getOSName` | `Platform::getOSName` | Zwraca nazwe systemu operacyjnego. |
| ... | ... | ... |
## Application (`g_app`)

Udostepnia API do zarzadzania gL'ownym obiektem aplikacji.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `setName` | `Application::setName` | Ustawia nazwe aplikacji. |
| `isRunning` | `Application::isRunning` | Sprawdza, czy aplikacja jest uruchomiona. |
| `exit` | `Application::exit` | Inicjuje proces zamykania aplikacji. |
| `getBuildCompiler`| `Application::getBuildCompiler`| Zwraca nazwe kompilatora uLLytego do budowy. |
| `isMobile` | `Application::isMobile` | Sprawdza, czy aplikacja dziaL'a w trybie mobilnym. |
| ... | ... | ... |
## Crypt (`g_crypt`)

Udostepnia funkcje kryptograficzne.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `genUUID` | `Crypt::genUUID` | Generuje unikalny identyfikator UUID. |
| `sha1Encode` | `Crypt::sha1Encode` | Koduje string za pomoca SHA1. |
| `rsaGenerateKey`| `Crypt::rsaGenerateKey` | Generuje klucze RSA. |
| ... | ... | ... |
## Clock (`g_clock`)

Udostepnia funkcje zwiazane z czasem i zegarem systemowym.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `micros` | `Clock::micros` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `millis` | `Clock::millis` | Zwraca czas w milisekundach. |
| `seconds` | `Clock::seconds` | Zwraca czas w sekundach. |
| ... | ... | ... |
## ConfigManager (`g_configs`)

API do zarzadzania plikami konfiguracyjnymi.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `getSettings` | `ConfigManager::getSettings` | Zwraca gL'owny obiekt konfiguracyjny. |
| `load` | `ConfigManager::load` | Laduje plik konfiguracyjny. |
| ... | ... | ... |
## Logger (`g_logger`)

API do logowania wiadomoLci.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `log` | `Logger::log` | Loguje wiadomoLc z podanym poziomem. |
| `debug` | `Logger::debug` | Loguje wiadomoLc na poziomie `LogDebug`. |
| ... | ... | ... |
## ResourceManager (`g_resources`)

Zarzadzanie plikami i zasobami.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `fileExists` | `ResourceManager::fileExists` | Sprawdza, czy plik istnieje. |
| `readFileContents`| `ResourceManager::readFileContentsSafe` | Odczytuje zawartoLc pliku. |
| `writeFileContents`|`ResourceManager::writeFileContents` | Zapisuje zawartoLc do pliku. |
| `createArchive` | `ResourceManager::createArchive` | Tworzy archiwum ZIP z podanych plikow. |
| ... | ... | ... |
## UI i Grafika (zaleLLne od `FW_GRAPHICS`)

Rejestruje klasy i funkcje zwiazane z interfejsem uLLytkownika, oknem, grafika i fontami. To najobszerniejsza sekcja.

-   **`g_app` (metody graficzne)**: `setMaxFps`, `getFps`, `doScreenshot`
-   **`g_window`**: Zarzadzanie oknem aplikacji (`move`, `resize`, `setTitle`, `setFullscreen`).
-   **`g_mouse`**: Zarzadzanie kursorami myszy.
-   **`g_graphics`**: Informacje o sterowniku graficznym.
-   **`g_textures`**: Zarzadzanie teksturami.
-   **`g_shaders`**: Tworzenie i zarzadzanie shaderami.
-   **`g_ui`**: GL'owny menedLLer UI (`loadUI`, `createWidget`).
-   **`g_fonts`**: Zarzadzanie fontami.
-   **`UIWidget`**: Rejestracja klasy bazowej dla wszystkich widgetow z ogromna liczba metod (np. `addChild`, `setRect`, `setText`, `setImageSource`).
-   **`UILayout` i pochodne**: Rejestracja klas layoutow (`UIBoxLayout`, `UIVerticalLayout`, `UIGridLayout`, `UIAnchorLayout`).
-   **`UITextEdit`**: Rejestracja widgetu do edycji tekstu.
## Siec (zaleLLne od `FW_NET`)

Rejestruje klasy do obsL'ugi sieci.

-   **`Server`**: Do tworzenia serwerow nasL'uchujacych.
-   **`Connection`**: Reprezentuje poL'aczenie TCP.
-   **`Protocol`**: Implementuje protokoL' komunikacyjny.
-   **`InputMessage` / `OutputMessage`**: Do odczytu i zapisu pakietow.
-   **`g_proxy`**: MenedLLer proxy.
-   **`g_http`**: Do zapytaL" HTTP/HTTPS i WebSocket.
## DLswiek (zaleLLne od `FW_SOUND`)

Rejestruje klasy i funkcje do obsL'ugi dLswieku.

-   **`g_sounds`**: MenedLLer dLswieku (`play`, `stopAll`).
-   **`SoundChannel`**: KanaL'y dLswiekowe.
-   **`SoundSource`**: LarodL'a dLswieku.
## ZaleLLnoLci i powiazania

Plik ten jest silnie powiazany z praktycznie kaLLdym moduL'em frameworka, poniewaLL jego zadaniem jest udostepnienie ich funkcjonalnoLci w Lua. WL'acza nagL'owki z:
-   `framework/core`
-   `framework/luaengine`
-   `framework/otml`
-   `framework/util`
-   `framework/graphics` (jeLli `FW_GRAPHICS` jest zdefiniowane)
-   `framework/sound` (jeLli `FW_SOUND` jest zdefiniowane)
-   `framework/net`
-   `framework/http`
-   `framework/proxy`
-   `framework/input`

Jest to centralny punkt L'aczacy warstwe C++ z warstwa skryptowa Lua.

---
# z"" resourcemanager.h
## Opis ogolny

Plik `resourcemanager.h` deklaruje klase `ResourceManager`, ktora jest singletonem (`g_resources`) odpowiedzialnym za zarzadzanie wszystkimi zasobami plikow w aplikacji. Abstrakcjonuje dostep do plikow, umoLLliwiajac ich odczyt zarowno z fizycznego systemu plikow, jak i z wirtualnych archiwow (np. `data.zip`) lub nawet z pamieci (dane wbudowane w plik wykonywalny). Jest to kluczowy element, ktory umoLLliwia L'atwe zarzadzanie zasobami gry, takimi jak grafiki, dLswieki, skrypty i pliki konfiguracyjne.
## Klasa `ResourceManager`
## Opis semantyczny

`ResourceManager` inicjalizuje wirtualny system plikow oparty na bibliotece **PhysFS**. OkreLla on katalogi robocze (`work dir`) i katalogi do zapisu (`write dir`), montuje archiwa z danymi i dostarcza ujednolicony interfejs do operacji na plikach. Klasa ta obsL'uguje rownieLL szyfrowanie i deszyfrowanie plikow w locie oraz mechanizmy aktualizacji klienta.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init(const char *argv0)` | Inicjalizuje PhysFS i ustawia LcieLLke do pliku binarnego aplikacji. |
| `terminate()` | Deinicjalizuje PhysFS. |
| `launchCorrect(...)` | Sprawdza, czy istnieje nowsza wersja pliku wykonywalnego w katalogu zapisu i ja uruchamia (tylko Windows). |
| `setupWriteDir(...)` | Konfiguruje i montuje katalog zapisu dla danych uLLytkownika. |
| `setup()` | Wyszukuje i montuje gL'owny katalog roboczy (np. z plikiem `init.lua` lub archiwum `data.zip`). |
| `loadDataFromSelf(...)` | Probuje zaL'adowac dane (archiwum) wbudowane w sam plik wykonywalny. |
| `fileExists(...)` | Sprawdza, czy plik istnieje w wirtualnym systemie plikow. |
| `directoryExists(...)` | Sprawdza, czy katalog istnieje. |
| `readFileContents(...)` | Odczytuje zawartoLc pliku jako string, opcjonalnie deszyfrujac go. |
| `writeFileContents(...)` | Zapisuje string do pliku w katalogu zapisu. |
| `openFile(...)` | Otwiera plik i zwraca wskaLsnik do `FileStream` do odczytu. |
| `createFile(...)` | Tworzy plik i zwraca wskaLsnik do `FileStream` do zapisu. |
| `deleteFile(...)` | Usuwa plik. |
| `makeDir(...)` | Tworzy katalog. |
| `listDirectoryFiles(...)` | Zwraca liste plikow w danym katalogu. |
| `resolvePath(...)` | TL'umaczy LcieLLke relatywna (np. wzgledem bieLLacego skryptu Lua) na LcieLLke absolutna w wirtualnym systemie plikow. |
| `getWorkDir()` | Zwraca gL'owny katalog roboczy (zawsze "/"). |
| `getWriteDir()` | Zwraca LcieLLke do katalogu zapisu. |
| `getBinaryName()` | Zwraca nazwe pliku wykonywalnego aplikacji. |
| `fileChecksum(...)` | Oblicza sume kontrolna CRC32 dla pliku. |
| `filesChecksums()` | Zwraca mape sum kontrolnych dla wszystkich plikow w zamontowanym archiwum. |
| `selfChecksum()` | Oblicza sume kontrolna CRC32 dla samego pliku wykonywalnego. |
| `updateData(...)` | Aktualizuje pliki w gL'ownym archiwum `data.zip`. |
| `updateExecutable(...)` | Zastepuje plik wykonywalny nowa wersja (np. po aktualizacji). |
| `createArchive(...)` | Tworzy archiwum ZIP w pamieci z podanej mapy plikow. |
| `decompressArchive(...)` | Dekompresuje archiwum ZIP (z pliku lub danych w pamieci) i zwraca mape plikow. |
| `encrypt(...)` | (Tylko z `WITH_ENCRYPTION`) Szyfruje pliki w katalogach `data`, `modules` itp. |
| `setLayout(...)` | Ustawia aktywny layout UI, co wpL'ywa na rozwiazywanie LcieLLek do zasobow. |
## Zmienne prywatne

-   `m_binaryPath`: LscieLLka do pliku wykonywalnego.
-   `m_writeDir`: LscieLLka do katalogu zapisu.
-   `m_loadedFromMemory`: Flaga wskazujaca, czy zasoby zostaL'y zaL'adowane z pamieci.
-   `m_loadedFromArchive`: Flaga wskazujaca, czy zasoby zostaL'y zaL'adowane z archiwum.
-   `m_memoryData`: WskaLsnik na dane archiwum w pamieci.
-   `m_customEncryption`: Klucz do niestandardowego szyfrowania.
-   `m_layout`: Nazwa aktywnego layoutu.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Definicje podstawowych typow w rdzeniu frameworka.
-   **PhysFS**: Biblioteka do obsL'ugi wirtualnego systemu plikow jest kluczowa zaleLLnoLcia.
-   **ZLIB, LibZip**: ULLywane do obsL'ugi archiwow ZIP.
-   `FileStream`: Klasa `ResourceManager` tworzy i zwraca obiekty `FileStream` do operacji na plikach.
-   `Application`: ULLywane do sprawdzania stanu aplikacji (np. czy jest zamykana).
-   `Logger`: Do logowania bL'edow i informacji.
-   `Crypt`: Do obliczania sum kontrolnych i (de)szyfrowania.
-   `Http`: ULLywane w kontekLcie pobierania plikow (`/downloads`).

---
# z"" adaptiverenderer.cpp
## Opis ogolny

Plik `adaptiverenderer.cpp` zawiera implementacje klasy `AdaptiveRenderer`, ktora jest odpowiedzialna za dynamiczne dostosowywanie jakoLci i wydajnoLci renderowania grafiki w zaleLLnoLci od aktualnej liczby klatek na sekunde (FPS). Celem tego mechanizmu jest utrzymanie pL'ynnoLci dziaL'ania aplikacji, zwL'aszcza na sL'abszych komputerach, poprzez redukcje liczby renderowanych obiektow lub obniLLenie czestotliwoLci aktualizacji, gdy FPS spada.
## Zmienne globalne
## `g_adaptiveRenderer`

Globalna instancja klasy `AdaptiveRenderer`, dostepna w caL'ym projekcie.

AdaptiveRenderer g_adaptiveRenderer;
```
## Klasa `AdaptiveRenderer`
## `void newFrame()`
## Opis semantyczny
Metoda wywoL'ywana na poczatku kaLLdej klatki renderowania. Rejestruje czas bieLLacej klatki i na podstawie liczby klatek z ostatnich 5 sekund decyduje, czy naleLLy zmienic poziom wydajnoLci (zwiekszyc lub zmniejszyc).
## DziaL'anie
1.  Dodaje bieLLacy czas (w milisekundach) do kolejki `m_frames`.
2.  Usuwa z kolejki klatki starsze niLL 5 sekund.
3.  JeLli poziom wydajnoLci jest narzucony (`m_forcedSpeed`), metoda koL"czy dziaL'anie.
4.  Co 5 sekund (`m_update + 5000 > now`):
    -   Pobiera maksymalny docelowy FPS z `g_app.getMaxFps()`.
    -   JeLli aktualna liczba klatek jest niLLsza niLL prog, zwieksza poziom `m_speed` (obniLLa jakoLc).
    -   JeLli aktualna liczba klatek jest wyLLsza niLL prog, zmniejsza poziom `m_speed` (zwieksza jakoLc).
    -   Poziom `m_speed` jest ograniczony do przedziaL'u `[1, RenderSpeeds - 1]`.
## `void refresh()`
## Opis semantyczny
Resetuje czas ostatniej aktualizacji poziomu wydajnoLci, co powoduje, LLe kolejna ocena FPS nastapi dopiero za 5 sekund.

void AdaptiveRenderer::refresh() {
    m_update = stdext::millis();
}
```
## Metody limitujace
## Opis semantyczny
Grupa metod zwracajacych limity dla roLLnych aspektow renderowania w zaleLLnoLci od aktualnego poziomu `m_speed`. Im wyLLszy `m_speed`, tym niLLsze limity i wieksze interwaL'y, co przekL'ada sie na mniejsze obciaLLenie procesora i karty graficznej.

-   **`effetsLimit()`**: Zwraca maksymalna liczbe efektow do renderowania.
-   **`creaturesLimit()`**: Zwraca maksymalna liczbe stworzeL".
-   **`itemsLimit()`**: Zwraca maksymalna liczbe przedmiotow.
-   **`mapRenderInterval()`**: Zwraca interwaL' (w milisekundach) ponownego renderowania mapy. `0` oznacza renderowanie w kaLLdej klatce.
-   **`textsLimit()`**: Zwraca maksymalna liczbe tekstow.
-   **`creaturesRenderInterval()`**: Zwraca interwaL' renderowania stworzeL" (obecnie nieuLLywane).
-   **`allowFading()`**: Zwraca `true`, jeLli dozwolone jest pL'ynne zanikanie/pojawianie sie obiektow (tylko na wyLLszych poziomach jakoLci).
-   **`foregroundUpdateInterval()`**: Zwraca interwaL' aktualizacji pierwszego planu.
## `std::string getDebugInfo()`
## Opis semantyczny
Zwraca sformatowany ciag znakow z informacjami debugowania, takimi jak aktualna liczba klatek, bieLLacy poziom `m_speed` i narzucony poziom `m_forcedSpeed`.
## ZaleLLnoLci i powiazania

-   `framework/core/graphicalapplication.h`: ULLywa `g_app.getMaxFps()` do okreLlenia docelowej liczby klatek.
-   `framework/stdext/format.h`: Do formatowania stringa w `getDebugInfo`.
-   `framework/util/extras.h`: Potencjalnie do flag debugowania.
-   `framework/core/logger.h`: Do logowania.

---
# z"" adaptiverenderer.h
## Opis ogolny

Plik `adaptiverenderer.h` jest plikiem nagL'owkowym dla klasy `AdaptiveRenderer`. Deklaruje on interfejs tej klasy, staL'e oraz globalna instancje `g_adaptiveRenderer`. UmoLLliwia to innym czeLciom systemu odpytywanie o aktualne limity i ustawienia wydajnoLci renderowania.
## Definicje i Makra
## `constexpr int RenderSpeeds`

Definiuje liczbe dostepnych poziomow wydajnoLci renderowania.

constexpr int RenderSpeeds = 5;
```
## Klasa `AdaptiveRenderer`
## Opis semantyczny
Klasa `AdaptiveRenderer` zarzadza dynamicznym skalowaniem jakoLci grafiki w celu utrzymania pL'ynnoLci dziaL'ania aplikacji. Implementuje mechanizm, ktory na podstawie bieLLacej liczby klatek na sekunde (FPS) dostosowuje roLLne parametry renderowania, takie jak limity renderowanych obiektow czy czestotliwoLc odLwieLLania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void newFrame()` | Rejestruje nowa klatke i aktualizuje poziom wydajnoLci, jeLli to konieczne. |
| `void refresh()` | Resetuje zegar aktualizacji, opoLsniajac nastepna ocene wydajnoLci. |
| `int effetsLimit()` | Zwraca limit dla renderowanych efektow. |
| `int creaturesLimit()` | Zwraca limit dla renderowanych stworzeL". |
| `int itemsLimit()` | Zwraca limit dla renderowanych przedmiotow. |
| `int textsLimit()` | Zwraca limit dla renderowanych tekstow. |
| `int mapRenderInterval()` | Zwraca interwaL' (opoLsnienie) ponownego renderowania mapy. |
| `int creaturesRenderInterval()` | Zwraca interwaL' renderowania stworzeL". |
| `bool allowFading()` | Sprawdza, czy dozwolone jest renderowanie efektow przejLcia (fading). |
| `int getLevel()` | Zwraca aktualny poziom wydajnoLci (`m_speed`). |
| `int foregroundUpdateInterval()` | Zwraca interwaL' aktualizacji pierwszego planu. |
| `std::string getDebugInfo()` | Zwraca informacje debugowania jako string. |
| `void setForcedLevel(int value)` | UmoLLliwia reczne ustawienie (narzucenie) poziomu wydajnoLci. |
## Zmienne prywatne

-   `m_forcedSpeed`: Narzucony poziom wydajnoLci (-1 oznacza automatyczny).
-   `m_speed`: Aktualny, automatycznie wyliczony poziom wydajnoLci (od 0 do `RenderSpeeds-1`).
-   `m_update`: Czas ostatniej aktualizacji poziomu wydajnoLci.
-   `m_frames`: Lista czasow ostatnich klatek, uLLywana do obliczania FPS.
## Zmienne globalne

-   `g_adaptiveRenderer`: Globalna instancja klasy `AdaptiveRenderer`.
## ZaleLLnoLci i powiazania

-   Plik wL'acza `<list>` do przechowywania czasow klatek.
-   Klasa jest uLLywana przez silnik renderujacy (np. w `client/mapview.cpp` - niezaL'aczony, ale moLLna sie domyLlac), aby dynamicznie ograniczac liczbe rysowanych obiektow.

---
# z"" application.cpp
## Opis ogolny

Plik `application.cpp` zawiera implementacje klasy `Application`, ktora jest bazowa klasa dla caL'ej aplikacji. Odpowiada za podstawowy cykl LLycia programu, w tym inicjalizacje, de-inicjalizacje, obsL'uge sygnaL'ow systemowych oraz zarzadzanie gL'ownymi komponentami frameworka, takimi jak menedLLer zasobow, menedLLer moduL'ow, silnik Lua i poL'aczenia sieciowe.
## Funkcje globalne
## `exitSignalHandler(int sig)`

Funkcja obsL'ugujaca sygnaL'y systemowe `SIGTERM` i `SIGINT` (np. zamkniecie terminala lub Ctrl+C). Po otrzymaniu sygnaL'u, dodaje do kolejki zdarzeL" wywoL'anie metody `Application::close()`, co pozwala na bezpieczne zamkniecie aplikacji.

void exitSignalHandler(int sig)
{
    static bool signaled = false;
    switch(sig) {
        case SIGTERM:
        case SIGINT:
            if(!signaled && !g_app.isStopping() && !g_app.isTerminated()) {
                signaled = true;
                g_dispatcher.addEvent(std::bind(&Application::close, &g_app));
}
            break;
}
}
```
## Klasa `Application`
## `Application::Application()`

Konstruktor, ktory ustawia domyLlne wartoLci dla nazwy aplikacji, wersji, kodowania znakow oraz flag stanu. Wykrywa rownieLL, czy aplikacja dziaL'a na platformie mobilnej (Android).
## `void Application::init(std::vector<std::string>& args)`
## Opis semantyczny
Metoda inicjalizujaca kluczowe komponenty aplikacji. Jest wywoL'ywana na samym poczatku dziaL'ania programu.
## DziaL'anie
1.  Rejestruje `exitSignalHandler` do obsL'ugi sygnaL'ow zamkniecia.
2.  Ustawia globalne locale.
3.  Przetwarza argumenty wiersza poleceL" za pomoca `g_platform`.
4.  Inicjalizuje `g_asyncDispatcher` do zadaL" asynchronicznych.
5.  Zapisuje opcje startowe i sprawdza, czy wL'aczono tryb mobilny (`-mobile`).
6.  Inicjalizuje menedLLera konfiguracji (`g_configs`).
7.  Inicjalizuje silnik Lua (`g_lua`) i rejestruje funkcje C++ (`registerLuaFunctions`).
8.  Inicjalizuje menedLLera proxy (`g_proxy`).
## `void Application::deinit()`
## Opis semantyczny
Metoda de-inicjalizujaca, wywoL'ywana przed zamknieciem aplikacji. Dba o poprawne zwolnienie zasobow w odwrotnej kolejnoLci do inicjalizacji.
## DziaL'anie
1.  WywoL'uje lua `g_app.onTerminate`.
2.  OdL'adowuje wszystkie moduL'y.
3.  Uruchamia garbage collector Lua, aby zwolnic referencje do obiektow.
4.  Przetwarza pozostaL'e zdarzenia z kolejki.
5.  WyL'acza `g_dispatcher`.
## `void Application::terminate()`
## Opis semantyczny
Finalny etap zamykania aplikacji. Zwalnia zasoby, ktore musza byc zwolnione jako ostatnie.
## DziaL'anie
1.  Zamyka wszystkie poL'aczenia sieciowe.
2.  Terminuje menedLLera konfiguracji.
3.  Terminuje menedLLera zasobow.
4.  Terminuje silnik Lua.
5.  Terminuje menedLLera proxy.
6.  Resetuje obsL'uge sygnaL'ow systemowych do domyLlnej.
## `void Application::poll()`
## Opis semantyczny
Przetwarza zdarzenia sieciowe i zdarzenia z gL'ownej kolejki (`g_dispatcher`). Jest to serce petli zdarzeL" aplikacji.
## `void Application::exit()`

Inicjuje proces zamykania aplikacji poprzez ustawienie flagi `m_stopping` i wywoL'anie lua `g_app.onExit`.
## `void Application::quick_exit()`

Natychmiastowo zamyka aplikacje z kodem 0, bez zwalniania zasobow.
## `void Application::close()`

Probuje zamknac aplikacje, wywoL'ujac lua `g_app.onClose`. JeLli skrypt zwroci `false` (lub nic), wywoL'ywana jest metoda `exit()`.
## `void Application::restart()` i `void Application::restartArgs(const std::vector<std::string>& args)`

Metody do restartowania aplikacji. Uruchamiaja nowa instancje procesu i natychmiast zamykaja bieLLaca. ULLywaja `boost::process` do stworzenia nowego procesu. Niedostepne na Androidzie i w wersji `FREE_VERSION`.
## `std::string Application::getOs()`

Zwraca nazwe bieLLacego systemu operacyjnego ("android", "windows", "mac", "linux").
## ZaleLLnoLci i powiazania

-   `framework/core/clock.h`: Do operacji na czasie.
-   `framework/core/resourcemanager.h`, `modulemanager.h`, `eventdispatcher.h`, `configmanager.h`: GL'owne moduL'y frameworka, ktorymi zarzadza.
-   `asyncdispatcher.h`: Do obsL'ugi zadaL" w tle.
-   `framework/luaengine/luainterface.h`: Do interakcji z Lua.
-   `framework/platform/platform.h`: Do operacji specyficznych dla platformy.
-   `framework/http/http.h`: Do obsL'ugi HTTP.
-   `framework/net/connection.h`: Do zarzadzania poL'aczeniami sieciowymi.
-   `framework/proxy/proxy.h`: Do zarzadzania proxy.
-   `boost/process.hpp`: Do restartowania aplikacji.

---
# z"" application.h
## Opis ogolny

Plik `application.h` jest plikiem nagL'owkowym dla klasy `Application`. Deklaruje on interfejs tej klasy, jej skL'adowe oraz zawiera dyrektywy doL'aczajace jedna z dwoch moLLliwych implementacji aplikacji: `GraphicalApplication` lub `ConsoleApplication`, w zaleLLnoLci od tego, czy zdefiniowano flage `FW_GRAPHICS`.
## Klasa `Application`
## Opis semantyczny
`Application` jest abstrakcyjna klasa bazowa, ktora definiuje podstawowy interfejs i cykl LLycia aplikacji. Zawiera metody do inicjalizacji, de-inicjalizacji, zamykania, restartowania oraz dostarcza informacji o samej aplikacji, takich jak nazwa, wersja czy system operacyjny.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `virtual void init(...)` | Inicjalizuje aplikacje. |
| `virtual void deinit()` | Zwalnia zasoby przed zamknieciem. |
| `virtual void terminate()` | Finalizuje zamykanie aplikacji. |
| `virtual void run() = 0` | Czysto wirtualna metoda, ktora musi byc zaimplementowana przez klasy pochodne. Zawiera gL'owna petle programu. |
| `virtual void poll()` | Przetwarza zdarzenia. |
| `virtual void exit()` | Rozpoczyna proces zamykania. |
| `virtual void quick_exit()` | Natychmiastowe zamkniecie programu. |
| `virtual void close()` | Probuje zamknac program (moLLe byc przerwane przez skrypt Lua). |
| `void restart()` | Restartuje aplikacje. |
| `void restartArgs(...)` | Restartuje aplikacje z nowymi argumentami. |
| `void setName(...)` | Ustawia nazwe aplikacji. |
| `void setCompactName(...)` | Ustawia skrocona nazwe aplikacji. |
| `void setVersion(...)` | Ustawia wersje aplikacji. |
| `bool isRunning()` | Zwraca `true`, jeLli aplikacja jest w gL'ownej petli. |
| `bool isStopping()` | Zwraca `true`, jeLli trwa proces zamykania. |
| `bool isTerminated()`| Zwraca `true`, jeLli aplikacja zostaL'a zakoL"czona. |
| `const std::string& getName()` | Zwraca nazwe aplikacji. |
| `std::string getBuildCompiler()` | Zwraca informacje o kompilatorze. |
| `std::string getBuildDate()` | Zwraca date kompilacji. |
| `std::string getBuildRevision()` | Zwraca numer rewizji. |
| `std::string getBuildCommit()` | Zwraca hash commita Git. |
| `std::string getBuildType()` | Zwraca typ budowania. |
| `std::string getBuildArch()` | Zwraca architekture. |
| `std::string getAuthor()` | Zwraca autora. |
| `std::string getOs()` | Zwraca nazwe systemu operacyjnego. |
| `std::string getStartupOptions()` | Zwraca opcje startowe. |
| `bool isMobile()` | Zwraca `true`, jeLli aplikacja dziaL'a w trybie mobilnym. |
## Metody chronione

-   `void registerLuaFunctions()`: Deklaracja metody odpowiedzialnej za bindowanie funkcji C++ do Lua.
## Zmienne chronione

-   `m_charset`: Kodowanie znakow.
-   `m_appName`, `m_appCompactName`, `m_appVersion`: Informacje o aplikacji.
-   `m_startupOptions`: Opcje startowe.
-   `m_running`, `m_stopping`, `m_terminated`, `m_mobile`: Flagi stanu aplikacji.
## DoL'aczanie implementacji

W zaleLLnoLci od flagi `FW_GRAPHICS`, doL'aczany jest jeden z dwoch plikow:
-   `graphicalapplication.h`: JeLli `FW_GRAPHICS` jest zdefiniowane, aplikacja bedzie miaL'a interfejs graficzny.
-   `consoleapplication.h`: W przeciwnym razie, bedzie to aplikacja konsolowa.

# ifdef FW_GRAPHICS
# include "graphicalapplication.h"
# else
# include "consoleapplication.h"
# endif
```
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje i nagL'owki uLLywane w caL'ym projekcie.
-   Klasa jest oznaczona adnotacja `@bindsingleton g_app`, co sugeruje, LLe jej instancja bedzie dostepna w Lua pod globalna nazwa `g_app`.

---
# z"" asyncdispatcher.h
## Opis ogolny

Plik `asyncdispatcher.h` deklaruje klase `AsyncDispatcher`, ktora zarzadza pula watkow roboczych do wykonywania zadaL" asynchronicznie. Jest to kluczowy komponent do odciaLLenia gL'ownego watku aplikacji (watku zdarzeL") z operacji, ktore moga zajac duLLo czasu, takich jak operacje wejLcia/wyjLcia na plikach, zapytania sieciowe czy intensywne obliczenia.
## Klasa `AsyncDispatcher`
## Opis semantyczny
`AsyncDispatcher` implementuje prosty model producent-konsument. Zadania (funkcje do wykonania) sa dodawane do kolejki, a watki robocze pobieraja je i wykonuja. Klasa uLLywa `std::thread`, `std::mutex` i `std::condition_variable` do synchronizacji.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje dyspozytor i tworzy pierwszy watek roboczy. |
| `void terminate()` | Zatrzymuje wszystkie watki i czyLci kolejke zadaL". |
| `void spawn_thread()` | Tworzy i uruchamia nowy watek roboczy. |
| `void stop()` | Zatrzymuje dziaL'anie wszystkich watkow roboczych. |
| `template<class F> schedule(const F& task)` | Planuje wykonanie zadania i zwraca `std::shared_future`, ktore pozwoli uzyskac wynik zadania w przyszL'oLci. ULLywa `std::promise` do przekazania wyniku. |
| `void dispatch(std::function<void()> f)` | Dodaje zadanie do kolejki bez oczekiwania na wynik (fire-and-forget). |
## PrzykL'ad uLLycia `schedule`
// Watek gL'owny
auto future = g_asyncDispatcher.schedule([]() -> int {
    // DL'ugotrwaL'a operacja
    std::this_thread::sleep_for(std::chrono::seconds(2));
    return 42;
});

// PoLsniej, w watku gL'ownym
int result = future.get(); // Czeka na zakoL"czenie zadania i pobiera wynik
```
## PrzykL'ad uLLycia `dispatch`
// Watek gL'owny
g_asyncDispatcher.dispatch([]() {
    // Operacja w tle, ktorej wynik nie jest bezpoLrednio potrzebny
    save_game_state();
});
```
## Metody chronione

-   `void exec_loop()`: GL'owna petla wykonywana przez kaLLdy watek roboczy. Czeka na zadania w kolejce i wykonuje je.
## Zmienne prywatne

-   `m_tasks`: Lista (kolejka) zadaL" do wykonania.
-   `m_threads`: Lista watkow roboczych.
-   `m_mutex`: Mutex do ochrony dostepu do `m_tasks`.
-   `m_condition`: Zmienna warunkowa do powiadamiania watkow o nowych zadaniach.
-   `m_running`: Flaga kontrolujaca, czy watki powinny kontynuowac prace.
## Zmienne globalne

-   `g_asyncDispatcher`: Globalna instancja klasy `AsyncDispatcher`.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Podstawowe deklaracje frameworka.
-   `framework/stdext/thread.h`: Zawiera nagL'owki `<thread>`, `<mutex>`, `<condition_variable>`.
-   Jest uLLywany przez inne moduL'y do wykonywania operacji w tle, np. `ResourceManager` do zapisu zrzutow ekranu, czy `Http` do zapytaL" sieciowych (chociaLL `Http` uLLywa wL'asnego `io_service` Boost.Asio, `AsyncDispatcher` moLLe byc uLLywany do przetwarzania wynikow).

---
# z"" binarytree.cpp
## Opis ogolny

Plik `binarytree.cpp` zawiera implementacje klas `BinaryTree` i `OutputBinaryTree`. Te klasy sL'uLLa do odczytu i zapisu danych w niestandardowym, hierarchicznym formacie binarnym, ktory przypomina drzewo. Format ten jest uLLywany w kliencie Tibii do przechowywania danych, np. plikow map (`.otbm`).
## Klasa `BinaryTree`
## `BinaryTree::BinaryTree(const FileStreamPtr& fin)`

Konstruktor, ktory przyjmuje wskaLsnik do strumienia pliku (`FileStream`) i zapamietuje pozycje startowa, od ktorej zaczyna sie wezeL' drzewa.
## `void BinaryTree::skipNodes()`

Metoda pomocnicza, ktora przeskakuje przez zagnieLLdLLone wezL'y w strumieniu danych, aby szybko przejLc do koL"ca bieLLacego wezL'a bez potrzeby jego peL'nego parsowania.
## `void BinaryTree::unserialize()`
## Opis semantyczny
To kluczowa metoda, ktora odczytuje "pL'askie" dane (wL'aLciwoLci) bieLLacego wezL'a ze strumienia pliku i zapisuje je do wewnetrznego bufora (`m_buffer`). Operacja ta jest wykonywana tylko raz (lazy loading), przy pierwszym dostepie do danych wezL'a. Deserializacja polega na odczytywaniu bajtow aLL do napotkania znacznika koL"ca wezL'a (`BINARYTREE_NODE_END`), z uwzglednieniem znakow specjalnych (`BINARYTREE_ESCAPE_CHAR`).
## `BinaryTreeVec BinaryTree::getChildren()`

Zwraca wektor wskaLsnikow do `BinaryTree`, reprezentujacych wszystkie bezpoLrednie dzieci bieLLacego wezL'a. Przeszukuje strumieL" w poszukiwaniu znacznikow poczatku wezL'a (`BINARYTREE_NODE_START`).
## Metody odczytu danych (`getU8`, `getU16`, `getString`, etc.)

Sa to metody do odczytywania konkretnych typow danych z wewnetrznego, zdeserializowanego bufora. KaLLde wywoL'anie przesuwa wskaLsnik odczytu (`m_pos`). JeLli bufor nie zostaL' jeszcze wypeL'niony, najpierw wywoL'ywana jest metoda `unserialize()`.
## Klasa `OutputBinaryTree`
## `OutputBinaryTree::OutputBinaryTree(const FileStreamPtr& fin)`

Konstruktor, ktory przyjmuje strumieL" pliku do zapisu i natychmiast rozpoczyna nowy wezeL', zapisujac znacznik `BINARYTREE_NODE_START`.
## Metody zapisu danych (`addU8`, `addU16`, `addString`, etc.)

Metody te sL'uLLa do zapisywania danych do strumienia. ULLywaja metody `write`, aby zapewnic poprawne "uciekanie" (escaping) znakow specjalnych (`0xFD`, `0xFE`, `0xFF`).
## `void OutputBinaryTree::startNode(uint8 node)`

Rozpoczyna nowy, zagnieLLdLLony wezeL' wewnatrz bieLLacego wezL'a.
## `void OutputBinaryTree::endNode()`

KoL"czy bieLLacy wezeL', zapisujac znacznik `BINARYTREE_NODE_END`.
## `void OutputBinaryTree::write(const uint8* data, size_t size)`

Prywatna metoda pomocnicza, ktora zapisuje surowe dane do strumienia, dodajac znak `BINARYTREE_ESCAPE_CHAR` przed kaLLdym bajtem, ktory jest znakiem specjalnym.
## ZaleLLnoLci i powiazania

-   `framework/core/binarytree.h`: Plik nagL'owkowy dla tych klas.
-   `framework/core/filestream.h`: ULLywa `FileStream` do operacji na plikach.
-   Format danych, ktory obsL'uguja te klasy, jest specyficzny dla klienta Tibii i jest uLLywany m.in. do parsowania plikow `.otbm` (mapy).

---
# z"" asyncdispatcher.cpp
## Opis ogolny

Plik `asyncdispatcher.cpp` zawiera implementacje klasy `AsyncDispatcher`, ktora zarzadza asynchronicznym wykonywaniem zadaL" w tle. Jest to realizacja mechanizmu puli watkow, ktory pozwala na odciaLLenie gL'ownego watku aplikacji.
## Zmienne globalne
## `g_asyncDispatcher`

Globalna instancja klasy `AsyncDispatcher`, zapewniajaca scentralizowany dostep do puli watkow z dowolnego miejsca w aplikacji.

AsyncDispatcher g_asyncDispatcher;
```
## Klasa `AsyncDispatcher`
## `void AsyncDispatcher::init()`
## Opis semantyczny
Inicjalizuje dyspozytor, wywoL'ujac `spawn_thread()` w celu utworzenia i uruchomienia pierwszego watku roboczego.
## `void AsyncDispatcher::terminate()`
## Opis semantyczny
Zamyka dyspozytor. Zatrzymuje wszystkie watki robocze i czyLci kolejke zadaL".
## `void AsyncDispatcher::spawn_thread()`
## Opis semantyczny
Tworzy nowy `std::thread`, ktory rozpoczyna wykonywanie petli `exec_loop()`. Watek jest dodawany do listy `m_threads`. Ustawia flage `m_running` na `true`.
## `void AsyncDispatcher::stop()`
## Opis semantyczny
Bezpiecznie zatrzymuje wszystkie watki robocze. Ustawia flage `m_running` na `false`, powiadamia wszystkie oczekujace watki za pomoca `m_condition.notify_all()`, a nastepnie czeka na ich zakoL"czenie za pomoca `thread.join()`.
## `void AsyncDispatcher::exec_loop()`
## Opis semantyczny
Jest to gL'owna funkcja petli dla kaLLdego watku roboczego.
## DziaL'anie
1.  Watek wchodzi w nieskoL"czona petle i blokuje mutex `m_mutex`.
2.  Czeka na zmiennej warunkowej `m_condition`, aLL w kolejce `m_tasks` pojawi sie zadanie lub flaga `m_running` zostanie ustawiona na `false`.
3.  Gdy zostanie obudzony i flaga `m_running` jest `true`, pobiera pierwsze zadanie z kolejki `m_tasks`.
4.  Odblokowuje mutex, aby inne watki mogL'y dodawac lub pobierac zadania.
5.  Wykonuje pobrane zadanie (`task()`).
6.  Ponownie blokuje mutex i wraca na poczatek petli.
7.  JeLli flaga `m_running` jest `false`, watek koL"czy dziaL'anie.
## ZaleLLnoLci i powiazania

-   `asyncdispatcher.h`: Plik nagL'owkowy dla tej klasy.
-   Klasa intensywnie korzysta z narzedzi wielowatkowoLci z biblioteki standardowej C++ (`<thread>`, `<mutex>`, `<condition_variable>`).
-   Jest uLLywana przez roLLne moduL'y, ktore potrzebuja wykonywac operacje w tle, np. `ResourceManager` do zapisu plikow, `Http` do przetwarzania pobranych danych.

---
# z"" clock.h
## Opis ogolny

Plik `clock.h` deklaruje klase `Clock`, ktora jest singletonem (`g_clock`) odpowiedzialnym za zarzadzanie czasem w aplikacji. Zapewnia buforowany, spojny czas dla jednej klatki oraz dostep do "rzeczywistego" czasu systemowego.
## Klasa `Clock`
## Opis semantyczny
Klasa `Clock` ma dwa gL'owne zadania:
1.  Dostarczac "buforowany" czas, ktory jest staL'y w obrebie jednej iteracji gL'ownej petli. Metoda `update()` jest wywoL'ywana raz na klatke, a metody `micros()`, `millis()`, `seconds()` zwracaja te sama, zapisana wartoLc czasu przez caL'a klatke. Zapewnia to spojnoLc obliczeL" zaleLLnych od czasu.
2.  Dostarczac "rzeczywisty" czas systemowy za pomoca metod `realMicros()` i `realMillis()`, ktore zawsze odczytuja aktualny czas systemowy.

Wszystkie skL'adowe przechowujace czas sa typu `std::atomic`, co zapewnia bezpieczeL"stwo watkowe przy odczycie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Clock()` | Konstruktor, inicjalizuje czas na 0. |
| `void update()` | Aktualizuje buforowany czas (`m_currentMicros`, `m_currentMillis`, `m_currentSeconds`) na podstawie aktualnego czasu systemowego. Powinna byc wywoL'ywana raz na klatke. |
| `ticks_t micros()` | Zwraca buforowany czas w mikrosekundach. |
| `ticks_t millis()` | Zwraca buforowany czas w milisekundach. |
| `float seconds()` | Zwraca buforowany czas w sekundach (jako `float`). |
| `ticks_t realMicros()` | Zwraca aktualny, "rzeczywisty" czas systemowy w mikrosekundach. |
| `ticks_t realMillis()` | Zwraca aktualny, "rzeczywisty" czas systemowy w milisekundach. |
## Zmienne prywatne

-   `m_currentMicros`: Atomowy licznik przechowujacy buforowany czas w mikrosekundach.
-   `m_currentMillis`: Atomowy licznik przechowujacy buforowany czas w milisekundach.
-   `m_currentSeconds`: Atomowa zmienna przechowujaca buforowany czas w sekundach.
## Zmienne globalne

-   `g_clock`: Globalna instancja klasy `Clock`.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Definicje podstawowych typow, w tym `ticks_t`.
-   `framework/stdext/time.h`: ULLywa funkcji `stdext::micros()` i `stdext::millis()` do pobierania czasu systemowego.
-   Klasa jest kluczowa dla caL'ego systemu, szczegolnie dla `EventDispatcher` (do planowania zdarzeL"), animacji i logiki gry. Metoda `update()` jest wywoL'ywana w gL'ownej petli aplikacji (w `GraphicalApplication::run()` i `ConsoleApplication::run()`).

---
# z"" binarytree.h
## Opis ogolny

Plik `binarytree.h` deklaruje interfejsy dla klas `BinaryTree` i `OutputBinaryTree`. Klasy te sL'uLLa do obsL'ugi niestandardowego, hierarchicznego formatu binarnego, uLLywanego do serializacji danych w strukturze drzewa. Format ten jest charakterystyczny dla plikow `.otbm` (OTClient Binary Map).
## Definicje i Makra
## Znaczniki binarne

Zdefiniowano trzy specjalne bajty, ktore kontroluja strukture drzewa w strumieniu binarnym:
-   `BINARYTREE_ESCAPE_CHAR` (0xFD): Znak "ucieczki", uLLywany do kodowania bajtow, ktore maja taka sama wartoLc jak inne znaki specjalne.
-   `BINARYTREE_NODE_START` (0xFE): Znacznik poczatku nowego wezL'a (dziecka).
-   `BINARYTREE_NODE_END` (0xFF): Znacznik koL"ca bieLLacego wezL'a.
## Klasa `BinaryTree`
## Opis semantyczny
Klasa `BinaryTree` reprezentuje pojedynczy wezeL' w drzewie danych i sL'uLLy do **odczytu** danych z tego wezL'a. DziaL'a na strumieniu `FileStream` i implementuje mechanizm leniwego odczytu (lazy loading) - dane wL'aLciwoLci wezL'a sa deserializowane do wewnetrznego bufora dopiero przy pierwszej probie dostepu do nich.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumieL" wejLciowy. |
| `seek(uint pos)` | Ustawia pozycje odczytu w zdeserializowanym buforze. |
| `skip(uint len)` | Przeskakuje o `len` bajtow w buforze. |
| `tell()` | Zwraca bieLLaca pozycje odczytu w buforze. |
| `size()` | Zwraca rozmiar zdeserializowanych danych wezL'a. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby caL'kowite bez znaku. |
| `getString(uint16 len = 0)` | Odczytuje ciag znakow (dL'ugoLc podana lub odczytana jako U16). |
| `getPoint()` | Odczytuje obiekt `Point`. |
| `getChildren()` | Zwraca wektor `BinaryTreePtr` zawierajacy wszystkie dzieci bieLLacego wezL'a. |
| `canRead()` | Sprawdza, czy moLLna jeszcze odczytywac dane z bufora. |
## Klasa `OutputBinaryTree`
## Opis semantyczny
Klasa `OutputBinaryTree` jest odpowiednikiem `BinaryTree` do **zapisu** danych w formacie drzewa binarnego. UmoLLliwia tworzenie wezL'ow i zapisywanie do nich wL'aLciwoLci, dbajac o poprawne formatowanie i "uciekanie" (escaping) znakow specjalnych.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OutputBinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumieL" wyjLciowy. |
| `addU8()`, `addU16()`, `addU32()` | Zapisuja liczby caL'kowite bez znaku. |
| `addString(const std::string& v)` | Zapisuje ciag znakow (z dL'ugoLcia). |
| `addPos(uint16 x, uint16 y, uint8 z)` | Zapisuje pozycje (x, y, z). |
| `addPoint(const Point& point)` | Zapisuje obiekt `Point`. |
| `startNode(uint8 node)` | Rozpoczyna nowy zagnieLLdLLony wezeL' z danym typem (atrybutem). |
| `endNode()` | KoL"czy bieLLacy wezeL'. |
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Definicje wskaLsnikow, np. `FileStreamPtr`.
-   `framework/util/databuffer.h`: Wewnetrzny bufor w `BinaryTree` jest typu `DataBuffer`.
-   Jest uLLywana przez moduL'y, ktore musza przetwarzac dane w formacie `.otbm`, np. edytor map lub sam klient do wczytywania mapy gry.

---
# z"" config.cpp
## Opis ogolny

Plik `config.cpp` zawiera implementacje klasy `Config`, ktora jest opakowaniem na dokument OTML (`OTMLDocument`). SL'uLLy do zarzadzania pojedynczym plikiem konfiguracyjnym, umoLLliwiajac L'atwy odczyt, zapis i modyfikacje wartoLci w formacie `key-value` oraz bardziej zL'oLLonych struktur zagnieLLdLLonych.
## Klasa `Config`
## `Config::Config()`

Konstruktor. Inicjalizuje pusty dokument OTML (`m_confsDoc`) i zeruje nazwe pliku (`m_fileName`).
## `bool Config::load(const std::string& file)`
## Opis semantyczny
Laduje i parsuje plik konfiguracyjny w formacie OTML.
## DziaL'anie
1.  Zapamietuje nazwe pliku w `m_fileName`.
2.  Sprawdza, czy plik istnieje za pomoca `g_resources.fileExists`.
3.  JeLli plik istnieje, parsuje go za pomoca `OTMLDocument::parse`.
4.  W przypadku sukcesu, zastepuje wewnetrzny dokument (`m_confsDoc`) nowo sparsowanym.
5.  W przypadku bL'edu parsowania, loguje bL'ad i zwraca `false`.
## `bool Config::unload()`

Zwalnia wewnetrzny dokument OTML i resetuje nazwe pliku. Zwraca `true`, jeLli obiekt byL' zaL'adowany.
## `bool Config::save()`

Zapisuje bieLLaca zawartoLc dokumentu OTML do pliku, ktorego nazwa jest przechowywana w `m_fileName`. ULLywa do tego metody `m_confsDoc->save()`.
## `void Config::clear()`

CzyLci wszystkie wezL'y z wewnetrznego dokumentu OTML.
## `void Config::setValue(const std::string& key, const std::string& value)`

Ustawia wartoLc dla danego klucza. JeLli wartoLc jest pusta, klucz jest usuwany. W przeciwnym razie tworzony jest nowy wezeL' OTML (`OTMLNode`) i dodawany do dokumentu. Istniejace wezL'y o tym samym kluczu sa nadpisywane.
## `void Config::setList(const std::string& key, const std::vector<std::string>& list)`

Zapisuje wektor stringow jako liste w dokumencie OTML. Tworzy wezeL' gL'owny o nazwie `key`, a nastepnie dodaje kaLLdy element wektora jako jego dziecko bez nazwy.
## `bool Config::exists(const std::string& key)`

Sprawdza, czy w dokumencie istnieje wezeL' o podanym kluczu.
## `std::string Config::getValue(const std::string& key)`

Zwraca wartoLc stringowa dla podanego klucza. JeLli klucz nie istnieje, zwraca pusty string.
## `std::vector<std::string> Config::getList(const std::string& key)`

Odczytuje liste stringow z wezL'a o podanym kluczu. Zwraca pusty wektor, jeLli klucz nie istnieje.
## `void Config::remove(const std::string& key)`

Usuwa wezeL' o podanym kluczu z dokumentu.
## `void Config::setNode(const std::string& key, const OTMLNodePtr& node)`

Zastepuje istniejacy wezeL' nowym wezL'em OTML. Najpierw usuwa stary wezeL', a nastepnie dodaje sklonowana wersje nowego.
## `void Config::mergeNode(const std::string& key, const OTMLNodePtr& node)`

Laczy podany wezeL' z istniejacym (lub tworzy nowy). DziaL'a podobnie do `setNode`, ale jest uLLywane do dodawania/aktualizowania danych bez usuwania caL'ego wezL'a.
## `OTMLNodePtr Config::getNode(const std::string& key)`

Zwraca wskaLsnik do wezL'a OTML o podanym kluczu.
## `int Config::getNodeSize(const std::string& key)`

Zwraca liczbe dzieci wezL'a o podanym kluczu. Zwraca 0, jeLli wezeL' nie istnieje.
## `bool Config::isLoaded()`

Zwraca `true`, jeLli obiekt `Config` jest powiazany z plikiem i ma zaL'adowana zawartoLc.
## ZaleLLnoLci i powiazania

-   `framework/core/config.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/core/resourcemanager.h`: ULLywany do sprawdzania istnienia plikow.
-   `framework/core/configmanager.h`: `ConfigManager` zarzadza instancjami klasy `Config`.
-   `framework/otml/otml.h`: Intensywnie korzysta z `OTMLDocument` i `OTMLNode` do przechowywania i manipulowania danymi konfiguracyjnymi.

---
# z"" configmanager.cpp
## Opis ogolny

Plik `configmanager.cpp` zawiera implementacje klasy `ConfigManager`, ktora jest singletonem (`g_configs`) sL'uLLacym do zarzadzania wieloma plikami konfiguracyjnymi (`Config`) w aplikacji. UmoLLliwia L'adowanie, tworzenie, pobieranie i zwalnianie konfiguracji na LLadanie.
## Zmienne globalne
## `g_configs`

Globalna instancja `ConfigManager`, zapewniajaca centralny punkt dostepu do wszystkich konfiguracji.

ConfigManager g_configs;
```
## Klasa `ConfigManager`
## `void ConfigManager::init()`
## Opis semantyczny
Inicjalizuje menedLLera. Tworzy gL'owny obiekt konfiguracyjny, zwany "settings" (`m_settings`), ktory jest przeznaczony do przechowywania ustawieL" samej aplikacji.
## `void ConfigManager::terminate()`
## Opis semantyczny
Zwalnia wszystkie zarzadzane obiekty `Config`. Zapewnia, LLe gL'owna konfiguracja (`m_settings`) jest zapisywana przed zamknieciem.
## DziaL'anie
1.  Zapisuje gL'owny plik ustawieL" (`m_settings->save()`).
2.  OdL'adowuje (`unload()`) gL'owny obiekt ustawieL".
3.  Iteruje po wszystkich pozostaL'ych zaL'adowanych konfiguracjach i je odL'adowuje.
4.  CzyLci liste `m_configs`.
## `ConfigPtr ConfigManager::getSettings()`

Zwraca wskaLsnik do gL'ownego obiektu konfiguracyjnego `m_settings`.
## `ConfigPtr ConfigManager::get(const std::string& file)`

Wyszukuje i zwraca wskaLsnik do juLL zaL'adowanego obiektu `Config` na podstawie nazwy pliku. JeLli konfiguracja nie jest zaL'adowana, zwraca `nullptr`.
## `ConfigPtr ConfigManager::loadSettings(const std::string file)`

Laduje gL'owny plik ustawieL" z podanej LcieLLki. Zastepuje domyLlny, pusty obiekt `m_settings`.
## `ConfigPtr ConfigManager::create(const std::string& file)`

Laduje plik konfiguracyjny, a jeLli on nie istnieje, tworzy go. Jest to przydatne do tworzenia domyLlnych plikow konfiguracyjnych przy pierwszym uruchomieniu.
## DziaL'anie
1.  Probuje zaL'adowac plik za pomoca `load(file)`.
2.  JeLli L'adowanie sie nie powiedzie (plik nie istnieje), tworzy nowy obiekt `Config`, L'aduje go (co tworzy pusty dokument), zapisuje go na dysku (tworzac plik) i dodaje do listy zarzadzanych konfiguracji.
## `ConfigPtr ConfigManager::load(const std::string& file)`

Laduje plik konfiguracyjny. JeLli plik byL' juLL zaL'adowany, zwraca istniejaca instancje. W przeciwnym razie tworzy nowy obiekt `Config`, probuje zaL'adowac plik z dysku i, jeLli sie powiedzie, dodaje go do listy zarzadzanych konfiguracji.
## `bool ConfigManager::unload(const std::string& file)`

Znajduje obiekt `Config` po nazwie pliku, odL'adowuje go (zwalniajac pamiec) i usuwa z listy zarzadzanych konfiguracji.
## `void ConfigManager::remove(const ConfigPtr config)`

Usuwa podany obiekt `Config` z listy `m_configs`.
## ZaleLLnoLci i powiazania

-   `framework/core/configmanager.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/core/config.h`: `ConfigManager` zarzadza obiektami typu `Config`.
-   `framework/core/logger.h`: ULLywany do logowania bL'edow, np. gdy nie moLLna zaL'adowac pliku.
-   Jest kluczowym komponentem rdzenia aplikacji, uLLywanym przez moduL'y do odczytu i zapisu swoich konfiguracji.

---
# z"" configmanager.h
## Opis ogolny

Plik `configmanager.h` deklaruje interfejs klasy `ConfigManager`, ktora peL'ni role centralnego menedLLera plikow konfiguracyjnych w formacie OTML. UmoLLliwia zarzadzanie cyklem LLycia wielu obiektow `Config`, w tym ich L'adowanie, tworzenie i zwalnianie.
## Klasa `ConfigManager`
## Opis semantyczny
`ConfigManager` to klasa singletonowa (`g_configs`), ktora przechowuje liste wszystkich aktywnych obiektow `Config`. WyroLLnia jeden specjalny obiekt konfiguracyjny, `m_settings`, przeznaczony na gL'owne ustawienia aplikacji. PozostaL'e konfiguracje sa zarzadzane w liLcie `m_configs` i identyfikowane po nazwie pliku.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedLLera, tworzac domyLlny obiekt `m_settings`. |
| `void terminate()` | Zwalnia wszystkie zaL'adowane konfiguracje, zapisujac wczeLniej `m_settings`. |
| `ConfigPtr getSettings()` | Zwraca wskaLsnik do gL'ownego obiektu ustawieL" aplikacji. |
| `ConfigPtr get(const std::string& file)` | Wyszukuje i zwraca wskaLsnik do zaL'adowanej konfiguracji o podanej nazwie pliku. |
| `ConfigPtr create(const std::string& file)` | Laduje konfiguracje z pliku lub tworzy nowy, pusty plik, jeLli nie istnieje. |
| `ConfigPtr loadSettings(const std::string file)` | Laduje gL'owny plik ustawieL" aplikacji z podanej LcieLLki. |
| `ConfigPtr load(const std::string& file)` | Laduje dodatkowy plik konfiguracyjny. |
| `bool unload(const std::string& file)` | Zwalnia i usuwa z menedLLera konfiguracje o podanej nazwie pliku. |
| `void remove(const ConfigPtr config)` | Usuwa podany obiekt `Config` z wewnetrznej listy. |
## Zmienne chronione

-   `m_settings`: WskaLsnik na gL'owny obiekt `Config` przechowujacy ustawienia aplikacji.
## Zmienne prywatne

-   `m_configs`: Lista wskaLsnikow na wszystkie dodatkowe zaL'adowane obiekty `Config`.
## Zmienne globalne

-   `g_configs`: Globalna instancja singletonu `ConfigManager`.
## ZaleLLnoLci i powiazania

-   `framework/core/config.h`: Deklaracja klasy `Config`, ktora zarzadza `ConfigManager`.
-   Jest oznaczona adnotacja `@bindsingleton g_configs`, co oznacza, LLe jej funkcjonalnoLc jest dostepna w skryptach Lua pod globalna nazwa `g_configs`.
-   WspoL'pracuje z `Application` (ktora wywoL'uje `init` i `terminate`) oraz z moduL'ami, ktore potrzebuja dostepu do swoich plikow konfiguracyjnych.

---
# z"" config.h
## Opis ogolny

Plik `config.h` deklaruje klase `Config`, ktora jest obiektowym interfejsem do odczytu, zapisu i manipulacji danymi w plikach konfiguracyjnych formatu OTML. Klasa ta dziedziczy po `LuaObject`, co oznacza, LLe jej instancje moga byc tworzone i uLLywane w skryptach Lua.
## Klasa `Config`
## Opis semantyczny
`Config` dziaL'a jako opakowanie (wrapper) na `OTMLDocument`. KaLLda instancja tej klasy reprezentuje jeden plik konfiguracyjny. UmoLLliwia operacje takie jak ustawianie wartoLci (`setValue`), list (`setList`), a takLLe bardziej zL'oLLonych struktur (`setNode`, `mergeNode`). Wszystkie dane sa przechowywane wewnetrznie jako drzewo wezL'ow OTML.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Config()` | Konstruktor domyLlny. |
| `bool load(const std::string& file)` | Laduje i parsuje konfiguracje z pliku OTML. |
| `bool unload()` | Zwalnia zaL'adowana konfiguracje. |
| `bool save()` | Zapisuje bieLLacy stan konfiguracji do pliku. |
| `void clear()` | Usuwa wszystkie dane z konfiguracji. |
| `void setValue(...)` | Ustawia wartoLc dla danego klucza. |
| `void setList(...)` | Ustawia liste wartoLci dla danego klucza. |
| `std::string getValue(...)` | Odczytuje wartoLc dla danego klucza. |
| `std::vector<std::string> getList(...)` | Odczytuje liste wartoLci dla danego klucza. |
| `void setNode(...)` | Zastepuje wezeL' o danym kluczu nowym wezL'em OTML. |
| `void mergeNode(...)` | Laczy (merge) podany wezeL' z istniejacym wezL'em o danym kluczu. |
| `OTMLNodePtr getNode(...)` | Zwraca wskaLsnik do wezL'a OTML o podanym kluczu. |
| `int getNodeSize(...)` | Zwraca liczbe dzieci wezL'a o danym kluczu. |
| `bool exists(const std::string& key)` | Sprawdza, czy klucz istnieje. |
| `void remove(const std::string& key)` | Usuwa klucz i jego wartoLc. |
| `std::string getFileName()` | Zwraca nazwe pliku powiazanego z ta konfiguracja. |
| `bool isLoaded()` | Zwraca `true`, jeLli konfiguracja zostaL'a zaL'adowana z pliku. |
| `ConfigPtr asConfig()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
## Zmienne prywatne

-   `m_fileName`: Nazwa pliku konfiguracyjnego.
-   `m_confsDoc`: WskaLsnik na `OTMLDocument`, ktory przechowuje dane konfiguracyjne.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Deklaracje typow, w tym `ConfigPtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`, aby byc dostepna w Lua.
-   `framework/otml/declarations.h`: ULLywa `OTMLDocumentPtr` i `OTMLNodePtr` do przechowywania danych.
-   Jest oznaczona jako `@bindclass`, co oznacza, LLe metody tej klasy sa dostepne do wywoL'ania z poziomu skryptow Lua na instancjach obiektow `Config`.
-   Instancje tej klasy sa tworzone i zarzadzane przez `ConfigManager`.

---
# z"" clock.cpp
## Opis ogolny

Plik `clock.cpp` zawiera implementacje metod klasy `Clock`. Odpowiada za dostarczanie mechanizmow pomiaru czasu, ktore sa kluczowe dla petli gL'ownej aplikacji, planowania zdarzeL" i animacji.
## Zmienne globalne
## `g_clock`

Globalna instancja klasy `Clock`, ktora jest uLLywana w caL'ym frameworku do uzyskiwania spojnych informacji o czasie.

Clock g_clock;
```
## Klasa `Clock`
## `Clock::Clock()`

Konstruktor klasy. Inicjalizuje wszystkie liczniki czasu na 0.
## `void Clock::update()`
## Opis semantyczny
Aktualizuje wewnetrzne, "buforowane" liczniki czasu. Ta metoda powinna byc wywoL'ywana raz na kaLLda iteracje gL'ownej petli aplikacji. Dzieki temu wszystkie operacje wewnatrz jednej klatki (np. logika gry, animacje, fizyka) bazuja na tej samej wartoLci czasu, co zapobiega niespojnoLciom.
## DziaL'anie
1.  Pobiera aktualny czas systemowy w mikrosekundach za pomoca `stdext::micros()`.
2.  Zapisuje te wartoLc do atomowej zmiennej `m_currentMicros`.
3.  Oblicza i zapisuje czas w milisekundach (`m_currentMillis`) i sekundach (`m_currentSeconds`).
## `ticks_t Clock::realMicros()`

Zwraca "na LLywo" aktualny czas systemowy w mikrosekundach. W przeciwieL"stwie do `micros()`, ta metoda nie korzysta z buforowanej wartoLci i przy kaLLdym wywoL'aniu odpytuje system operacyjny.
## `ticks_t Clock::realMillis()`

Zwraca "na LLywo" aktualny czas systemowy w milisekundach. Podobnie jak `realMicros()`, odczytuje aktualny czas.
## ZaleLLnoLci i powiazania

-   `framework/core/clock.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/stdext/time.h`: ULLywa funkcji `stdext::micros()` i `stdext::millis()`, ktore sa opakowaniem na `std::chrono` do pobierania czasu o wysokiej precyzji.
-   Jest uLLywana przez `EventDispatcher` do planowania zdarzeL", `GraphicalApplication` do synchronizacji petli renderowania oraz przez wiele innych komponentow do mierzenia czasu trwania operacji.

---
# z"" consoleapplication.h
## Opis ogolny

Plik `consoleapplication.h` deklaruje klase `ConsoleApplication`, ktora jest konkretna implementacja klasy `Application` dla aplikacji dziaL'ajacej w trybie konsolowym, bez interfejsu graficznego. Jest uLLywana, gdy flaga `FW_GRAPHICS` nie jest zdefiniowana podczas kompilacji.
## Klasa `ConsoleApplication`
## Opis semantyczny
`ConsoleApplication` dziedziczy po `Application` i implementuje jej czysto wirtualna metode `run()`. Ta implementacja zawiera prosta petle gL'owna, ktora przetwarza zdarzenia i usypia watek na krotki czas, aby uniknac 100% uLLycia procesora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void run()` | Implementuje gL'owna petle aplikacji konsolowej. |
## Zmienne globalne

-   `g_app`: Globalna instancja `ConsoleApplication`, ktora staje sie gL'ownym obiektem aplikacji, gdy kompilacja odbywa sie bez wsparcia dla grafiki.
## ZaleLLnoLci i powiazania

-   `framework/core/application.h`: Klasa bazowa, z ktorej dziedziczy `ConsoleApplication`.
-   Jest to jedna z dwoch moLLliwych implementacji aplikacji, wybierana w `application.h` za pomoca dyrektyw preprocesora.

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `core` jest plikiem nagL'owkowym sL'uLLacym do wczesnych deklaracji (forward declarations) klas i definicji typow wskaLsnikow (`typedef`) dla rdzennych komponentow frameworka. Jego celem jest rozwiazanie problemu zaleLLnoLci cyklicznych miedzy plikami nagL'owkowymi oraz zmniejszenie iloLci doL'aczanych nagL'owkow w plikach, ktore potrzebuja jedynie znac istnienie danego typu, a nie jego peL'na definicje.
## Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastepujacych klas, nie definiujac ich zawartoLci:

-   `ConfigManager`
-   `ModuleManager`
-   `ResourceManager`
-   `Module`
-   `Config`
-   `Event`
-   `ScheduledEvent`
-   `FileStream`
-   `BinaryTree`
-   `OutputBinaryTree`
## Definicje typow (Typedefs)

Na podstawie wczesnych deklaracji, plik definiuje typy inteligentnych wskaLsnikow (`shared_object_ptr`), ktore sa uLLywane w caL'ym frameworku. Upraszcza to skL'adnie i zapewnia spojnoLc.

-   `ModulePtr`: `stdext::shared_object_ptr<Module>`
-   `ConfigPtr`: `stdext::shared_object_ptr<Config>`
-   `EventPtr`: `stdext::shared_object_ptr<Event>`
-   `ScheduledEventPtr`: `stdext::shared_object_ptr<ScheduledEvent>`
-   `FileStreamPtr`: `stdext::shared_object_ptr<FileStream>`
-   `BinaryTreePtr`: `stdext::shared_object_ptr<BinaryTree>`
-   `OutputBinaryTreePtr`: `stdext::shared_object_ptr<OutputBinaryTree>`
-   `BinaryTreeVec`: `std::vector<BinaryTreePtr>`
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   Ten plik jest doL'aczany przez wiele innych plikow nagL'owkowych w module `core` i poza nim, aby umoLLliwic deklarowanie zmiennych i parametrow funkcji bez koniecznoLci doL'aczania peL'nych definicji klas.

---
# z"" event.cpp
## Opis ogolny

Plik `event.cpp` zawiera implementacje klasy `Event`, ktora jest podstawowym obiektem reprezentujacym jednorazowe, opoLsnione lub cykliczne zdarzenie w systemie.
## Klasa `Event`
## `Event::Event(const std::string& function, const std::function<void()>& callback, bool botSafe)`

Konstruktor, ktory inicjalizuje zdarzenie.

-   **Parametry**:
    -   `function`: Nazwa funkcji (lub opis), uLLywana do celow debugowania i statystyk.
    -   `callback`: Funkcja (lambda lub `std::function`), ktora zostanie wykonana.
    -   `botSafe`: Flaga okreLlajaca, czy zdarzenie moLLe byc wywoL'ane przez bota (uLLywane do filtrowania w niektorych kontekstach).
-   **DziaL'anie**: Inicjalizuje flagi `m_canceled` i `m_executed` na `false` oraz przechowuje podane parametry.
## `Event::~Event()`

Destruktor. W trybie debugowania, `VALIDATE(m_callback == nullptr)` sprawdza, czy `callback` zostaL' poprawnie zwolniony, aby zapobiec wyciekom pamieci lub wiszacym referencjom.
## `void Event::execute()`
## Opis semantyczny
Wykonuje `callback` powiazany ze zdarzeniem.
## DziaL'anie
1.  Sprawdza, czy zdarzenie nie zostaL'o anulowane (`!m_canceled`) i czy nie zostaL'o juLL wykonane (`!m_executed`).
2.  JeLli warunki sa speL'nione i `callback` istnieje, wywoL'uje go.
3.  Ustawia flage `m_executed` na `true`.
4.  Resetuje `m_callback` do `nullptr`, aby zwolnic wszelkie zasoby (np. obiekty przechwycone przez lambde).
## `void Event::cancel()`
## Opis semantyczny
Anuluje zdarzenie, zapobiegajac jego przyszL'emu wykonaniu.
## DziaL'anie
1.  Ustawia flage `m_canceled` na `true`.
2.  Resetuje `m_callback` do `nullptr`, aby natychmiast zwolnic zasoby.
## ZaleLLnoLci i powiazania

-   `framework/core/event.h`: Plik nagL'owkowy dla tej klasy.
-   Jest klasa bazowa dla `ScheduledEvent`.
-   Jest zarzadzana przez `EventDispatcher`, ktory przechowuje instancje `Event` w kolejce i wywoL'uje ich metode `execute()`.

---
# z"" event.h
## Opis ogolny

Plik `event.h` deklaruje klase `Event`, ktora jest podstawowa klasa do obsL'ugi zdarzeL" w systemie opartym na kolejce zdarzeL". Reprezentuje pojedyncze zadanie, ktore ma zostac wykonane w przyszL'oLci przez `EventDispatcher`.
## Klasa `Event`
## Opis semantyczny
`Event` to obiekt, ktory enkapsuluje funkcje zwrotna (`callback`) do wykonania. Dziedziczy po `LuaObject`, co pozwala na przekazywanie go do skryptow Lua. Posiada mechanizmy do wykonania, anulowania i sprawdzania jego stanu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Event(...)` | Konstruktor. |
| `virtual ~Event()` | Destruktor. |
| `virtual void execute()` | Wykonuje `callback`, jeLli zdarzenie nie jest anulowane. |
| `void cancel()` | Anuluje zdarzenie, zapobiegajac jego wykonaniu. |
| `bool isCanceled()` | Zwraca `true`, jeLli zdarzenie zostaL'o anulowane. |
| `bool isExecuted()` | Zwraca `true`, jeLli zdarzenie zostaL'o juLL wykonane. |
| `bool isBotSafe()` | Zwraca `true`, jeLli zdarzenie jest bezpieczne do wykonania w kontekLcie bota. |
| `const std::string& getFunction()` | Zwraca nazwe/opis funkcji powiazanej ze zdarzeniem. |
## Zmienne chronione

-   `m_function`: `std::string` przechowujaca nazwe funkcji dla celow debugowania.
-   `m_callback`: `std::function<void()>` zawierajaca kod do wykonania.
-   `m_canceled`: Flaga wskazujaca, czy zdarzenie zostaL'o anulowane.
-   `m_executed`: Flaga wskazujaza, czy zdarzenie zostaL'o wykonane.
-   `m_botSafe`: Flaga bezpieczeL"stwa.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/luaobject.h`: Jest klasa pochodna `LuaObject`.
-   Jest uLLywana przez `EventDispatcher` do tworzenia i zarzadzania kolejka zdarzeL".
-   Jest klasa bazowa dla `ScheduledEvent`.
-   Oznaczona jako `@bindclass`, co oznacza, LLe jest dostepna w Lua, a jej metody (`cancel`, `execute` itd.) moga byc wywoL'ywane ze skryptow.

---
# z"" eventdispatcher.cpp
## Opis ogolny

Plik `eventdispatcher.cpp` zawiera implementacje klasy `EventDispatcher`, ktora jest sercem systemu zdarzeL". Odpowiada za zarzadzanie kolejka zdarzeL" natychmiastowych oraz kolejka priorytetowa zdarzeL" zaplanowanych w czasie.
## Zmienne globalne

-   `g_dispatcher`: Globalna instancja `EventDispatcher` dla gL'ownego watku aplikacji (logika gry, siec).
-   `g_graphicsDispatcher`: Globalna instancja `EventDispatcher` dla watku graficznego.
-   `g_mainThreadId`, `g_graphicsThreadId`, `g_dispatcherThreadId`: Przechowuja identyfikatory watkow w celu weryfikacji, czy dana operacja jest wykonywana w odpowiednim watku.
## Klasa `EventDispatcher`
## `void EventDispatcher::shutdown()`
## Opis semantyczny
Zamyka dyspozytor, przetwarzajac wszystkie pozostaL'e zdarzenia i anulujac zaplanowane.
## DziaL'anie
1.  Przetwarza wszystkie zdarzenia z `m_eventList` za pomoca `poll()`.
2.  Iteruje po wszystkich zdarzeniach w `m_scheduledEventList`, anuluje je i usuwa z kolejki.
3.  Ustawia flage `m_disabled` na `true`, aby zapobiec dodawaniu nowych zdarzeL".
## `void EventDispatcher::poll()`
## Opis semantyczny
GL'owna metoda przetwarzajaca zdarzenia. WywoL'ywana regularnie w petli aplikacji.
## DziaL'anie
1.  **Przetwarzanie zdarzeL" zaplanowanych (`m_scheduledEventList`)**:
    -   Sprawdza kolejke priorytetowa i wykonuje wszystkie zdarzenia, dla ktorych minaL' czas (`remainingTicks() <= 0`).
    -   JeLli zdarzenie jest cykliczne (`nextCycle()` zwraca `true`), jest ponownie dodawane do kolejki z nowym czasem wykonania.
2.  **Przetwarzanie zdarzeL" natychmiastowych (`m_eventList`)**:
    -   Wchodzi w petle, ktora wykonuje wszystkie zdarzenia z `m_eventList`.
    -   Petla jest powtarzana, jeLli w trakcie wykonywania zdarzeL" zostaL'y dodane nowe (np. zdarzenie A dodaje zdarzenie B), aby zapewnic, LLe wszystkie zdarzenia zwiazane z bieLLaca klatka zostana wykonane przed jej zakoL"czeniem.
    -   Posiada zabezpieczenie przed nieskoL"czona petla (jeLli zdarzenia ciagle dodaja nowe zdarzenia).
3.  Zapisuje statystyki dotyczace liczby przetworzonych zdarzeL".
## `ScheduledEventPtr EventDispatcher::scheduleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe jednorazowe zdarzenie zaplanowane, ktore zostanie wykonane po upL'ywie `delay` milisekund.
## `ScheduledEventPtr EventDispatcher::cycleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe cykliczne zdarzenie zaplanowane, ktore bedzie wykonywane co `delay` milisekund.
## `EventPtr EventDispatcher::addEventEx(...)`

Dodaje nowe zdarzenie do kolejki zdarzeL" natychmiastowych. JeLli `pushFront` jest `true`, zdarzenie jest dodawane na poczatek kolejki, co gwarantuje jego wykonanie w bieLLacej iteracji petli `poll()`.
## ZaleLLnoLci i powiazania

-   `framework/core/eventdispatcher.h`: Plik nagL'owkowy.
-   `framework/core/clock.h`: ULLywa `g_clock` do sprawdzania czasu dla zdarzeL" zaplanowanych.
-   `framework/core/graphicalapplication.h`: ULLywa `g_app.isOnInputEvent()` do oznaczenia, czy zdarzenie zostaL'o wywoL'ane w trakcie obsL'ugi zdarzenia wejLciowego.
-   `framework/graphics/graph.h`: Zapisuje statystyki do `g_graphs`.
-   `framework/util/stats.h`: ULLywa `AutoStat` do profilowania.
-   `framework/core/timer.h`: ULLywany do zabezpieczenia przed nieskoL"czonymi petlami.
-   Jest kluczowym komponentem, uLLywanym przez niemal kaLLda czeLc aplikacji do planowania i wykonywania operacji w sposob asynchroniczny (wzgledem gL'ownej petli).

---
# z"" eventdispatcher.h
## Opis ogolny

Plik `eventdispatcher.h` deklaruje interfejs klasy `EventDispatcher` oraz powiazane z nia globalne instancje i makra. Definiuje on publiczne API do zarzadzania kolejka zdarzeL" w aplikacji.
## Definicje i Makra
## Makra pomocnicze do dodawania zdarzeL"

Upraszczaja one wywoL'ania metod `...Ex`, automatycznie dodajac nazwe bieLLacej funkcji (`__FUNCTION__`) jako opis zdarzenia dla celow debugowania.

-   `addEvent(...)`: Opakowanie na `addEventEx(__FUNCTION__, ...)`
-   `scheduleEvent(...)`: Opakowanie na `scheduleEventEx(__FUNCTION__, ...)`
-   `cycleEvent(...)`: Opakowanie na `cycleEventEx(__FUNCTION__, ...)`
## Makra do walidacji watkow

SL'uLLa do sprawdzania, czy dana funkcja jest wywoL'ywana w odpowiednim watku, co jest kluczowe dla bezpieczeL"stwa w Lrodowisku wielowatkowym.

-   `VALIDATE_GRAPHICS_THREAD()`: Sprawdza, czy bieLLacy watek to watek graficzny.
-   `VALIDATE_DISPATCHER_THREAD()`: Sprawdza, czy bieLLacy watek to watek dyspozytora (gL'owny watek logiki).
## Klasa `EventDispatcher`
## Opis semantyczny
`EventDispatcher` jest centralnym mechanizmem do zarzadzania i wykonywania zadaL" w sposob asynchroniczny, ale w ramach jednego, okreLlonego watku. Posiada dwie kolejki: jedna dla zdarzeL" natychmiastowych i druga (priorytetowa) dla zdarzeL" zaplanowanych w czasie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void shutdown()` | Zamyka dyspozytor, czyszczac i anulujac wszystkie zdarzenia. |
| `void poll()` | Przetwarza zdarzenia, ktore sa gotowe do wykonania. |
| `EventPtr addEventEx(...)` | Dodaje zdarzenie do wykonania w nastepnej iteracji petli `poll()`. |
| `ScheduledEventPtr scheduleEventEx(...)` | Planuje jednorazowe wykonanie zdarzenia po okreLlonym czasie. |
| `ScheduledEventPtr cycleEventEx(...)` | Planuje cykliczne wykonywanie zdarzenia co okreLlony czas. |
| `bool isBotSafe()` | Zwraca, czy aktualnie wykonywane zdarzenie jest oznaczone jako "bezpieczne dla bota". |
## Zmienne prywatne

-   `m_eventList`: Lista (`std::list`) zdarzeL" do natychmiastowego wykonania.
-   `m_pollEventsSize`: Rozmiar `m_eventList` na poczatku petli `poll()`, aby obsL'uLLyc zdarzenia dodane w trakcie.
-   `m_disabled`: Flaga blokujaca dodawanie nowych zdarzeL" po wywoL'aniu `shutdown()`.
-   `m_botSafe`: Flaga stanu dla aktualnie wykonywanego zdarzenia.
-   `m_mutex`: Mutex rekurencyjny do ochrony kolejek.
-   `m_scheduledEventList`: Kolejka priorytetowa (`std::priority_queue`) dla zdarzeL" zaplanowanych w czasie.
## Zmienne globalne

-   `g_dispatcher`: Globalny dyspozytor dla gL'ownego watku.
-   `g_graphicsDispatcher`: Globalny dyspozytor dla watku graficznego.
-   `g_mainThreadId`, `g_dispatcherThreadId`, `g_graphicsThreadId`: Identyfikatory watkow.
## ZaleLLnoLci i powiazania

-   `framework/core/clock.h`: Wymagany do obsL'ugi czasu.
-   `framework/core/scheduledevent.h`: Definicja `ScheduledEvent` i komparatora `lessScheduledEvent`.
-   `<queue>`: ULLywany do implementacji kolejki priorytetowej.

---
# z"" filestream.cpp
## Opis ogolny

Plik `filestream.cpp` zawiera implementacje klasy `FileStream`, ktora jest opakowaniem (wrapperem) na operacje plikowe, gL'ownie z wykorzystaniem biblioteki **PhysFS**. UmoLLliwia zarowno odczyt z plikow na dysku, jak i z danych w pamieci (np. z wbudowanego archiwum lub zdekompresowanych danych).
## Klasa `FileStream`
## Konstruktory

-   **`FileStream::FileStream(const std::string& name, PHYSFS_File *fileHandle, bool writeable)`**: Tworzy strumieL" na podstawie otwartego uchwytu pliku PhysFS.
-   **`FileStream::FileStream(const std::string& name, std::string&& buffer)`**: Tworzy strumieL" na podstawie bufora danych w pamieci (`std::string`). Probuje rownieLL zdekompresowac bufor, jeLli jest on w formacie GZIP.
## `bool FileStream::initFromGzip(const std::string& buffer)`

Prywatna metoda pomocnicza, ktora sprawdza, czy bufor danych jest skompresowany za pomoca GZIP (na podstawie "magicznych bajtow"). JeLli tak, dekompresuje go za pomoca biblioteki ZLIB i zapisuje wynik do wewnetrznego bufora `m_data`.
## `FileStream::~FileStream()` i `void FileStream::close()`

Destruktor i metoda `close()` zwalniaja zasoby. JeLli strumieL" byL' otwarty z pliku PhysFS, zamyka uchwyt `m_fileHandle`. CzyLci rownieLL wewnetrzne bufory danych (`m_data`, `m_strData`).
## `void FileStream::flush()`

W przypadku strumienia do zapisu, zapisuje zawartoLc bufora `m_data` na dysk za pomoca `PHYSFS_writeBytes`.
## `int FileStream::read(void* buffer, uint32 size, uint32 nmemb)`

Odczytuje dane ze strumienia. JeLli strumieL" jest oparty na pliku, uLLywa `PHYSFS_readBytes`. JeLli na buforze w pamieci, kopiuje dane z `m_strData` lub `m_data` i przesuwa wskaLsnik odczytu `m_pos`.
## `void FileStream::write(const void *buffer, uint32 count)`

Zapisuje dane do strumienia. Dla plikow uLLywa `PHYSFS_writeBytes`, a dla buforow w pamieci dodaje dane do `m_data`.
## `seek`, `skip`, `size`, `tell`, `eof`

Implementacje standardowych operacji na strumieniach, ktore deleguja wywoL'ania do odpowiednich funkcji PhysFS lub operuja na wewnetrznym wskaLsniku `m_pos` i rozmiarze bufora.
## Metody odczytu typow (`getU8`, `getU16`, `getString`, etc.)

Metody te sL'uLLa do odczytywania konkretnych typow danych ze strumienia. DziaL'aja zarowno na plikach PhysFS, jak i na buforach w pamieci. Wykonuja konwersje z porzadku bajtow Little Endian.
## `BinaryTreePtr FileStream::getBinaryTree()`

Rozpoczyna odczyt zagnieLLdLLonej struktury `BinaryTree` ze strumienia, sprawdzajac najpierw znacznik poczatku wezL'a.
## Metody zapisu typow (`addU8`, `addU16`, `addString`, etc.)

SL'uLLa do zapisywania danych do strumienia.
## `void FileStream::throwError(...)`

Metoda pomocnicza do generowania wyjatkow z dodatkowymi informacjami o nazwie pliku i bL'edzie PhysFS.
## ZaleLLnoLci i powiazania

-   `framework/core/filestream.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/core/binarytree.h`: ULLywana do odczytu i zapisu struktur `BinaryTree`.
-   `framework/core/application.h`: ULLywana do sprawdzania, czy aplikacja jest w trakcie zamykania.
-   **PhysFS**: Kluczowa zaleLLnoLc do operacji na plikach w wirtualnym systemie plikow.
-   **ZLIB**: ULLywana do dekompresji GZIP.
-   Jest tworzona i zarzadzana przez `ResourceManager` i uLLywana w caL'ym projekcie do odczytu zasobow.

---
# z"" filestream.h
## Opis ogolny

Plik `filestream.h` deklaruje klase `FileStream`, ktora jest kluczowym elementem systemu zarzadzania zasobami. Stanowi ona abstrakcje nad strumieniem danych, ktory moLLe pochodzic z pliku na dysku (obsL'ugiwanego przez PhysFS) lub bezpoLrednio z bufora w pamieci. Klasa dziedziczy po `LuaObject`, dzieki czemu moLLe byc uLLywana w skryptach Lua.
## Klasa `FileStream`
## Opis semantyczny
`FileStream` dostarcza interfejs podobny do standardowych strumieni plikow, umoLLliwiajac sekwencyjny odczyt i zapis roLLnych typow danych (liczby caL'kowite, stringi, dane binarne). Jest to podstawowe narzedzie do parsowania plikow binarnych i tekstowych w caL'ym projekcie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FileStream(...)` | Konstruktory tworzace strumieL" z uchwytu pliku PhysFS lub z bufora w pamieci. |
| `~FileStream()` | Destruktor. |
| `close()` | Zamyka strumieL" i zwalnia zasoby. |
| `flush()` | Wymusza zapis buforowanych danych do pliku (dla strumieni do zapisu). |
| `write(...)` | Zapisuje blok danych do strumienia. |
| `read(...)` | Odczytuje blok danych ze strumienia. |
| `seek(uint pos)` | Ustawia pozycje wskaLsnika w strumieniu. |
| `skip(uint len)` | Przesuwa wskaLsnik o `len` bajtow. |
| `size()` | Zwraca caL'kowity rozmiar strumienia. |
| `tell()` | Zwraca bieLLaca pozycje wskaLsnika. |
| `eof()` | Zwraca `true`, jeLli osiagnieto koniec strumienia. |
| `name()` | Zwraca nazwe/LsrodL'o strumienia. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby caL'kowite bez znaku. |
| `get8()`, `get16()`, `get32()`, `get64()` | Odczytuja liczby caL'kowite ze znakiem. |
| `getString()` | Odczytuje string (poprzedzony 2-bajtowa dL'ugoLcia). |
| `getBinaryTree()` | Odczytuje i zwraca obiekt `BinaryTree`. |
| `startNode(uint8 n)` | Rozpoczyna zapis nowego wezL'a w formacie `BinaryTree`. |
| `endNode()` | KoL"czy zapis wezL'a. |
| `addU8()`, ..., `addString()` | Zapisuja roLLne typy danych do strumienia. |
| `asFileStream()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
## Zmienne prywatne

-   `m_name`: Nazwa pliku lub LsrodL'a danych.
-   `m_fileHandle`: WskaLsnik na uchwyt pliku PhysFS (jeLli dotyczy).
-   `m_pos`: BieLLaca pozycja odczytu/zapisu w buforze pamieci.
-   `m_writeable`: Flaga wskazujaca, czy strumieL" jest otwarty do zapisu.
-   `m_caching`: Flaga wskazujaca, czy strumieL" operuje na buforze w pamieci.
-   `m_data`: Bufor danych (`DataBuffer<uint8_t>`) dla strumieni w pamieci.
-   `m_strData`: Bufor danych (`std::string`) dla strumieni w pamieci.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Definicje typow, np. `BinaryTreePtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `framework/util/databuffer.h`: ULLywa `DataBuffer` do przechowywania danych.
-   `framework/util/point.h`: Do zapisu i odczytu obiektow `Point`.
-   `physfs.h`: Wymagany do deklaracji `PHYSFS_File`.
-   Klasa jest oznaczona jako `@bindclass`, co oznacza, LLe jest dostepna w Lua. Jest to kluczowe dla moduL'ow, ktore musza parsowac niestandardowe formaty plikow ze skryptow.

---
# z"" graphicalapplication.cpp
## Opis ogolny

Plik `graphicalapplication.cpp` zawiera implementacje klasy `GraphicalApplication`, ktora jest konkretna implementacja `Application` dla aplikacji z interfejsem graficznym. Odpowiada za inicjalizacje, zarzadzanie i zamykanie wszystkich podsystemow graficznych, a takLLe za implementacje gL'ownej petli renderowania i logiki.
## Zmienne globalne
## `g_app`

Globalna instancja `GraphicalApplication`, ktora jest gL'ownym obiektem aplikacji, gdy kompilacja odbywa sie z flaga `FW_GRAPHICS`.

GraphicalApplication g_app;
```
## Klasa `GraphicalApplication`
## `void GraphicalApplication::init(std::vector<std::string>& args)`
## Opis semantyczny
Inicjalizuje aplikacje graficzna. WywoL'uje najpierw `Application::init()`, a nastepnie inicjalizuje wszystkie komponenty zwiazane z grafika.
## DziaL'anie
1.  WywoL'uje `Application::init(args)`.
2.  Inicjalizuje okno platformy (`g_window.init()`).
3.  Ustawia callbacki dla okna: `onResize`, `onInputEvent`, `onClose`.
4.  Inicjalizuje menedLLera myszy (`g_mouse.init()`).
5.  Inicjalizuje menedLLera UI (`g_ui.init()`).
6.  Inicjalizuje silnik graficzny (`g_graphics.init()`).
7.  WywoL'uje pierwsze zdarzenie zmiany rozmiaru.
8.  Inicjalizuje menedLLera dLswieku (`g_sounds.init()`), jeLli `FW_SOUND` jest zdefiniowane.
## `void GraphicalApplication::deinit()`

Deinicjalizuje aplikacje w odwrotnej kolejnoLci, ukrywajac okno i zwalniajac zasoby.
## `void GraphicalApplication::terminate()`

Finalizuje zamykanie podsystemow graficznych, w tym `g_ui`, `g_sounds`, `g_mouse` i `g_graphics`.
## `void GraphicalApplication::run()`
## Opis semantyczny
Implementuje gL'owna petle aplikacji, ktora jest podzielona na dwa rownolegL'e watki:
1.  **Watek logiki (`worker`)**: Odpowiada za aktualizacje stanu gry, przetwarzanie zdarzeL" i przygotowywanie kolejek rysowania (`DrawQueue`).
2.  **Watek renderowania (gL'owny watek)**: Odpowiada za przetwarzanie zdarzeL" okna, renderowanie zawartoLci przygotowanych kolejek na ekranie i synchronizacje klatek.
## DziaL'anie watku logiki (`worker`)
-   W nieskoL"czonej petli:
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Przetwarza zdarzenia (`poll()`).
    -   Czeka, jeLli poprzednia klatka nie zostaL'a jeszcze wyrenderowana.
    -   Renderuje UI do trzech osobnych kolejek: `MapBackgroundPane`, `MapForegroundPane`, `ForegroundPane`.
    -   Przekazuje gotowe kolejki do watku renderowania za pomoca mutexu.
    -   Usypia na 1ms, jeLli `m_maxFps > 0` lub wL'aczona jest synchronizacja pionowa.
## DziaL'anie watku renderowania (gL'ownego)
-   W nieskoL"czonej petli:
    -   Aktualizuje zegar i przetwarza zdarzenia graficzne (`pollGraphics()`).
    -   Czeka na gotowe kolejki rysowania z watku logiki.
    -   Aktualizuje `AdaptiveRenderer`.
    -   Synchronizuje klatki zgodnie z `m_maxFps`.
    -   Ustawia `FrameBuffer` do renderowania poza ekranem, jeLli skalowanie jest wL'aczone.
    -   Renderuje tL'o mapy do `m_mapFramebuffer`.
    -   Renderuje wL'aLciwa scene, L'aczac tL'o mapy, pierwszy plan mapy i interfejs uLLytkownika.
    -   JeLli wL'aczono skalowanie, rysuje zawartoLc `m_framebuffer` na ekranie.
    -   Rysuje grafy debugowania.
    -   Zamienia bufory (`g_window.swapBuffers()`).
## `void GraphicalApplication::poll()` i `void GraphicalApplication::pollGraphics()`

Metody pomocnicze wywoL'ywane w odpowiednich watkach do przetwarzania zdarzeL". `poll()` obsL'uguje dLswiek i logike, a `pollGraphics()` obsL'uguje zdarzenia okna i aktualizacje tekstow.
## Inne metody

-   `close()`: WywoL'ywana przy zamykaniu okna.
-   `resize()`: WywoL'ywana przy zmianie rozmiaru okna.
-   `inputEvent()`: Przekazuje zdarzenia wejLciowe do `UIManager`.
-   `doScreenshot()`: Robi zrzut ekranu i zapisuje go do pliku asynchronicznie.
-   `scaleUp()`, `scaleDown()`, `scale()`: Zarzadzaja skalowaniem interfejsu.
-   `setSmooth()`: WL'acza/wyL'acza wygL'adzanie dla `m_mapFramebuffer`.
-   `doMapScreenshot()`: Robi zrzut ekranu samej mapy.
## ZaleLLnoLci i powiazania

-   Jest to centralna klasa, ktora integruje prawie wszystkie moduL'y graficzne i rdzenia.
-   ZaleLLy od `Application`, `PlatformWindow`, `UIManager`, `Graphics`, `TextureManager`, `Painter`, `SoundManager` i innych.
-   ULLywa `std::thread` i `std::mutex` do implementacji wielowatkowej petli.

---
# z"" inputevent.h
## Opis ogolny

Plik `inputevent.h` deklaruje strukture `InputEvent`, ktora jest uLLywana do przekazywania informacji o zdarzeniach wejLciowych (z klawiatury i myszy) w systemie. Jest to prosta struktura danych, ktora agreguje wszystkie moLLliwe parametry zdarzenia.
## Struktura `InputEvent`
## Opis semantyczny
Struktura `InputEvent` jest uniwersalnym kontenerem na dane o zdarzeniach. W zaleLLnoLci od pola `type`, inne pola przechowuja odpowiednie informacje. Na przykL'ad, dla zdarzenia klawiatury (`KeyDownInputEvent`), pole `keyCode` bedzie miaL'o znaczenie, a dla zdarzenia myszy (`MouseMoveInputEvent`) - `mousePos` i `mouseMoved`.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `type` | `Fw::InputEventType` | Typ zdarzenia (np. wciLniecie klawisza, ruch myszy). |
| `wheelDirection` | `Fw::MouseWheelDirection` | Kierunek przewijania koL'kiem myszy (`MouseWheelUp` lub `MouseWheelDown`). |
| `mouseButton` | `Fw::MouseButton` | Przycisk myszy, ktory wywoL'aL' zdarzenie. |
| `keyCode` | `Fw::Key` | Kod wciLnietego klawisza. |
| `keyText` | `std::string` | Znak tekstowy odpowiadajacy wciLnietemu klawiszowi (dla `KeyTextInputEvent`). |
| `keyboardModifiers`| `int` | Flagi bitowe dla klawiszy modyfikujacych (Ctrl, Alt, Shift). |
| `mousePos` | `Point` | Aktualna pozycja kursora myszy. |
| `mouseMoved` | `Point` | Wektor przesuniecia kursora myszy od ostatniego zdarzenia. |
| `autoRepeatTicks`| `int` | Czas (w milisekundach), przez jaki klawisz jest przytrzymywany (dla `KeyPressInputEvent`). |
## Metody

-   **`InputEvent()`**: Konstruktor, inicjalizuje strukture.
-   **`reset(Fw::InputEventType eventType = Fw::NoInputEvent)`**: Resetuje wszystkie pola do wartoLci domyLlnych i ustawia nowy typ zdarzenia.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Podstawowe deklaracje.
-   Struktura ta jest tworzona w klasie `PlatformWindow` (np. `win32window.cpp`) na podstawie zdarzeL" systemowych, a nastepnie przekazywana do `GraphicalApplication` i dalej do `UIManager`, ktory rozsyL'a je do odpowiednich widgetow.

---
# z"" graphicalapplication.h
## Opis ogolny

Plik `graphicalapplication.h` deklaruje klase `GraphicalApplication`, ktora jest implementacja `Application` dla aplikacji z interfejsem graficznym. Jest to gL'owna klasa zarzadzajaca petla renderowania, zdarzeniami wejLciowymi i komponentami graficznymi.
## Klasa `GraphicalApplication`
## Opis semantyczny
Dziedziczy po `Application` i implementuje jej metody wirtualne, dodajac funkcjonalnoLc specyficzna dla aplikacji graficznej. Odpowiada za koordynacje miedzy oknem (`PlatformWindow`), menedLLerem UI (`UIManager`), silnikiem renderujacym (`Painter`) i innymi systemami. Implementuje wielowatkowa petle gL'owna, gdzie logika jest oddzielona od renderowania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init(...)` | Inicjalizuje podsystemy graficzne. |
| `void deinit()` | Zwalnia zasoby graficzne przed zamknieciem. |
| `void terminate()` | Finalizuje zamykanie podsystemow graficznych. |
| `void run()` | Uruchamia gL'owna, wielowatkowa petle aplikacji. |
| `void poll()` | Przetwarza zdarzenia logiki i dLswieku. |
| `void pollGraphics()` | Przetwarza zdarzenia okna i grafiki. |
| `void close()` | ObsL'uguje zdarzenie zamkniecia okna. |
| `bool willRepaint()` | Zwraca `true`, jeLli zaplanowano przemalowanie ekranu. |
| `void repaint()` | Wymusza przemalowanie ekranu w nastepnej klatce. |
| `void setMaxFps(int maxFps)` | Ustawia maksymalna liczbe klatek na sekunde. |
| `int getMaxFps()` | Zwraca ustawiony limit FPS. |
| `int getFps()` | Zwraca aktualny FPS renderowania. |
| `int getGraphicsFps()` | Zwraca FPS watku graficznego. |
| `int getProcessingFps()` | Zwraca FPS watku logiki. |
| `bool isOnInputEvent()` | Zwraca `true`, jeLli aplikacja jest w trakcie przetwarzania zdarzenia wejLciowego. |
| `int getIteration()` | Zwraca licznik iteracji gL'ownej petli. |
| `void doScreenshot(...)` | Robi zrzut caL'ego ekranu. |
| `void scaleUp()` / `scaleDown()` / `scale()` | Zarzadzaja skalowaniem interfejsu. |
| `void setSmooth(bool value)` | WL'acza/wyL'acza wygL'adzanie dla bufora ramki mapy. |
| `void doMapScreenshot(...)` | Robi zrzut ekranu samej mapy gry. |
## Metody chronione

-   `void resize(const Size& size)`: ObsL'uguje zdarzenie zmiany rozmiaru okna.
-   `void inputEvent(InputEvent event)`: Otrzymuje i przekazuje zdarzenia wejLciowe.
## Zmienne prywatne

-   `m_iteration`: Licznik klatek.
-   `m_scaling`, `m_lastScaling`: Aktualne i poprzednie skalowanie UI.
-   `m_maxFps`: Maksymalny limit FPS.
-   `m_onInputEvent`: Flaga aktywna podczas obsL'ugi zdarzenia wejLciowego.
-   `m_mustRepaint`: Flaga wymuszajaca przemalowanie.
-   `m_framebuffer`, `m_mapFramebuffer`: Bufory ramki do renderowania poza ekranem (off-screen rendering).
-   `m_graphicsFrames`, `m_processingFrames`: Liczniki klatek dla watku graficznego i logiki.
-   `m_windowPollTimer`: Timer do ograniczania czestotliwoLci odpytywania okna.
## Zmienne globalne

-   `g_app`: Globalna instancja `GraphicalApplication`.
## ZaleLLnoLci i powiazania

-   `framework/core/application.h`: Klasa bazowa.
-   `framework/graphics/declarations.h`: Deklaracje typow graficznych (np. `FrameBufferPtr`).
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/core/adaptiverenderer.h`: ULLywa `AdaptiveRenderer` do dynamicznego dostosowywania wydajnoLci.
-   `framework/util/framecounter.h`: ULLywa `FrameCounter` do Lledzenia FPS.

---
# z"" logger.h
## Opis ogolny

Plik `logger.h` deklaruje klase `Logger`, ktora implementuje system logowania dla caL'ej aplikacji. Jest to singleton (`g_logger`) zapewniajacy scentralizowany i bezpieczny watkowo mechanizm do zapisywania komunikatow o roLLnym poziomie waLLnoLci (debug, info, warning, error, fatal).
## Struktura `LogMessage`

Prosta struktura przechowujaca pojedyncza wiadomoLc logu.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `level` | `Fw::LogLevel` | Poziom waLLnoLci wiadomoLci. |
| `message`| `std::string` | TreLc wiadomoLci. |
| `when` | `std::size_t` | Czas (timestamp) utworzenia wiadomoLci. |
## Klasa `Logger`
## Opis semantyczny
`Logger` umoLLliwia logowanie komunikatow do standardowego wyjLcia (konsola), opcjonalnego pliku oraz przekazywanie ich do zarejestrowanego `callbacka` (np. w celu wyLwietlenia w interfejsie uLLytkownika). Przechowuje rownieLL historie ostatnich `MAX_LOG_HISTORY` wiadomoLci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void log(...)` | GL'owna metoda logujaca wiadomoLc z okreLlonym poziomem. |
| `void logFunc(...)` | Loguje wiadomoLc wraz z informacja o funkcji, z ktorej zostaL'a wywoL'ana (`__PRETTY_FUNCTION__`). |
| `void debug(..)` | Skrot do `log(Fw::LogDebug, ...)`. |
| `void info(...)` | Skrot do `log(Fw::LogInfo, ...)`. |
| `void warning(...)` | Skrot do `log(Fw::LogWarning, ...)`. |
| `void error(...)` | Skrot do `log(Fw::LogError, ...)`. |
| `void fatal(...)` | Skrot do `log(Fw::LogFatal, ...)`, ktory dodatkowo powoduje zamkniecie aplikacji. |
| `void fireOldMessages()` | WywoL'uje `callback` `m_onLog` dla wszystkich historycznych wiadomoLci. |
| `void setLogFile(...)` | Ustawia plik, do ktorego beda zapisywane logi. |
| `void setOnLog(...)` | Rejestruje funkcje zwrotna, ktora bedzie wywoL'ywana dla kaLLdej nowej wiadomoLci. |
| `std::string getLastLog()` | Zwraca ostatnio zalogowana wiadomoLc. |
| `void setTestingMode()` | Ustawia tryb testowy, w ktorym bL'edy (`LogError`) dziaL'aja jak bL'edy krytyczne (`LogFatal`). |
## Zmienne prywatne

-   `m_logMessages`: Lista ostatnich wiadomoLci.
-   `m_onLog`: WskaLsnik na funkcje zwrotna.
-   `m_outFile`: StrumieL" pliku do zapisu logow.
-   `m_mutex`: Mutex rekurencyjny zapewniajacy bezpieczeL"stwo watkowe.
-   `m_lastLog`: Przechowuje ostatnia wiadomoLc.
-   `m_testingMode`: Flaga trybu testowego.
## Makra pomocnicze

Plik definiuje makra uL'atwiajace logowanie z dodatkowymi informacjami o kontekLcie.

-   `trace()`: Loguje nazwe bieLLacej funkcji.
-   `traceDebug(a)`, `traceInfo(a)`, ...: Loguja wiadomoLc `a` wraz z nazwa funkcji i Lladem stosu.
-   `logTraceCounter()`: Loguje licznik wywoL'aL" co sekunde.
-   `logTraceFrameCounter()`: Loguje licznik wywoL'aL" co klatke.
## Zmienne globalne

-   `g_logger`: Globalna instancja `Logger`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/stdext/thread.h`: Zawiera `<mutex>` do synchronizacji.
-   `<fstream>`: Do obsL'ugi zapisu do pliku.
-   Jest uLLywany w caL'ym projekcie do raportowania stanu, bL'edow i informacji debugowania.

---
# z"" module.cpp
## Opis ogolny

Plik `module.cpp` zawiera implementacje klasy `Module`, ktora reprezentuje pojedynczy, L'adowalny moduL' funkcjonalnoLci w aplikacji. ModuL'y sa podstawa architektury wtyczek, pozwalajac na dynamiczne L'adowanie, odL'adowywanie i ponowne L'adowanie kodu (gL'ownie skryptow Lua) w trakcie dziaL'ania programu.
## Klasa `Module`
## `Module::Module(const std::string& name)`

Konstruktor. Ustawia nazwe moduL'u i tworzy dla niego nowe, odizolowane Lrodowisko Lua (piaskownice - sandbox) za pomoca `g_lua.newSandboxEnv()`.
## `bool Module::load()`
## Opis semantyczny
GL'owna metoda L'adujaca moduL'. Jest odpowiedzialna za sprawdzenie i zaL'adowanie zaleLLnoLci, a nastepnie wykonanie skryptow moduL'u.
## DziaL'anie
1.  Sprawdza, czy moduL' nie jest juLL zaL'adowany.
2.  Definiuje `errorHandler` do obsL'ugi bL'edow L'adowania.
3.  Dodaje Lrodowisko moduL'u do `package.loaded` w Lua, aby `require` dziaL'aL'o poprawnie.
4.  Iteruje po zaleLLnoLciach (`m_dependencies`):
    -   Sprawdza, czy moduL' nie zaleLLy sam od siebie.
    -   Sprawdza, czy zaleLLnoLc istnieje.
    -   Sprawdza, czy nie ma zaleLLnoLci cyklicznych.
    -   JeLli zaleLLnoLc nie jest zaL'adowana, probuje ja zaL'adowac.
5.  JeLli moduL' jest w piaskownicy (`m_sandboxed`), ustawia jego Lrodowisko jako globalne w Lua.
6.  Wykonuje wszystkie skrypty z listy `m_scripts`.
7.  Wykonuje skrypt z `m_onLoadFunc`, jeLli jest zdefiniowany.
8.  JeLli wystapiL' bL'ad, wywoL'uje `errorHandler` i zwraca `false`.
9.  Przywraca globalne Lrodowisko Lua, jeLli byL'o zmienione.
10. Ustawia flage `m_loaded` na `true` i aktualizuje kolejnoLc L'adowania moduL'ow.
11. Laduje moduL'y z listy `m_loadLaterModules`.
## `void Module::unload()`
## Opis semantyczny
OdL'adowuje moduL', wykonujac jego skrypt `onUnload` i czyszczac jego Lrodowisko Lua.
## DziaL'anie
1.  Sprawdza, czy moduL' jest zaL'adowany.
2.  JeLli tak, wykonuje skrypt `onUnload` (`m_onUnloadFunc`).
3.  CzyLci caL'a tabele Lrodowiska Lua moduL'u, aby zwolnic wszystkie referencje.
4.  Usuwa moduL' z `package.loaded` w Lua.
5.  Ustawia flage `m_loaded` na `false`.
## `bool Module::reload()`

OdL'adowuje i ponownie L'aduje moduL'.
## `bool Module::isDependent()`

Sprawdza, czy jakikolwiek inny zaL'adowany moduL' zaleLLy od tego moduL'u. Jest to uLLywane do okreLlenia, czy moduL' moLLna bezpiecznie odL'adowac.
## `bool Module::hasDependency(const std::string& name, bool recursive)`

Sprawdza, czy moduL' ma zaleLLnoLc o podanej nazwie. Opcja `recursive` pozwala na sprawdzanie zaleLLnoLci poLrednich.
## `int Module::getSandbox(LuaInterface* lua)`

Zwraca na stos Lua tabele Lrodowiska (piaskownice) tego moduL'u.
## `void Module::discover(const OTMLNodePtr& moduleNode)`

Parsuje wezeL' OTML (z pliku `.otmod`) i inicjalizuje pola moduL'u, takie jak opis, autor, wersja, zaleLLnoLci, lista skryptow, oraz skrypty `onLoad` i `onUnload`.
## ZaleLLnoLci i powiazania

-   `framework/core/module.h`: Plik nagL'owkowy.
-   `framework/core/modulemanager.h`: WspoL'pracuje z `ModuleManager` do zarzadzania zaleLLnoLciami i kolejnoLcia L'adowania.
-   `framework/core/resourcemanager.h`: ULLywany do rozwiazywania LcieLLek do skryptow.
-   `framework/otml/otml.h`: ULLywa `OTMLNode` do odczytu metadanych moduL'u.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do zarzadzania Lrodowiskiem i wykonywania skryptow.

---
# z"" modulemanager.cpp
## Opis ogolny

Plik `modulemanager.cpp` zawiera implementacje klasy `ModuleManager`, ktora jest singletonem (`g_modules`) odpowiedzialnym za zarzadzanie wszystkimi moduL'ami w aplikacji. Odpowiada za ich odkrywanie, L'adowanie, odL'adowywanie i ponowne L'adowanie, a takLLe za zarzadzanie zaleLLnoLciami miedzy nimi.
## Zmienne globalne
## `g_modules`

Globalna instancja `ModuleManager`.

ModuleManager g_modules;
```
## Klasa `ModuleManager`
## `void ModuleManager::clear()`

CzyLci wszystkie dane menedLLera, usuwajac liste moduL'ow i moduL'ow do automatycznego L'adowania.
## `void ModuleManager::discoverModules()`
## Opis semantyczny
Przeszukuje wirtualny system plikow (katalogi `/modules` i `/mods`) w poszukiwaniu plikow `.otmod`, parsuje je i tworzy obiekty `Module` dla kaLLdego znalezionego moduL'u. ModuL'y oznaczone jako `autoload` sa dodawane do specjalnej listy.
## `void ModuleManager::autoLoadModules(int maxPriority)`

Laduje wszystkie moduL'y z listy `m_autoLoadModules`, ktorych priorytet jest mniejszy lub rowny `maxPriority`. ModuL'y sa L'adowane w kolejnoLci rosnacego priorytetu.
## `ModulePtr ModuleManager::discoverModule(const std::string& moduleFile)`

Parsuje pojedynczy plik `.otmod`, tworzy lub aktualizuje obiekt `Module` i dodaje go do listy `m_modules`.
## `void ModuleManager::ensureModuleLoaded(const std::string& moduleName)`

Sprawdza, czy moduL' o podanej nazwie jest zaL'adowany. JeLli nie, probuje go zaL'adowac. JeLli L'adowanie sie nie powiedzie, aplikacja jest zamykana z bL'edem krytycznym.
## `void ModuleManager::unloadModules()`

OdL'adowuje wszystkie zaL'adowane moduL'y. ULLywa kopii listy moduL'ow, aby uniknac problemow z iteratorami podczas usuwania.
## `void ModuleManager::reloadModules()`
## Opis semantyczny
Implementuje mechanizm "hot-reloading" moduL'ow.
## DziaL'anie
1.  Tworzy liste moduL'ow do ponownego zaL'adowania (`toLoadList`).
2.  W petli (do 10 prob) probuje odL'adowac wszystkie moduL'y, ktore moga byc odL'adowane (`canUnload()`). ModuL'y sa odL'adowywane w odwrotnej kolejnoLci zaleLLnoLci.
3.  Po odL'adowaniu, L'aduje ponownie moduL'y z `toLoadList`.
## `ModulePtr ModuleManager::getModule(const std::string& moduleName)`

Wyszukuje i zwraca wskaLsnik do moduL'u o podanej nazwie.
## `void ModuleManager::updateModuleLoadOrder(ModulePtr module)`

Aktualizuje wewnetrzna liste moduL'ow (`m_modules`), aby zaL'adowane moduL'y znajdowaL'y sie na jej poczatku. Zapewnia to poprawna kolejnoLc odL'adowywania (odwrotna do L'adowania).
## ZaleLLnoLci i powiazania

-   `framework/core/modulemanager.h`: Plik nagL'owkowy.
-   `framework/core/resourcemanager.h`: ULLywany do przeszukiwania katalogow z moduL'ami.
-   `framework/otml/otml.h`: Do parsowania plikow `.otmod`.
-   `framework/core/application.h`: Do obsL'ugi bL'edow krytycznych.
-   Jest centralnym elementem architektury wtyczek i LciLle wspoL'pracuje z klasa `Module`.

---
# z"" logger.cpp
## Opis ogolny

Plik `logger.cpp` zawiera implementacje klasy `Logger`, ktora jest odpowiedzialna za system logowania w aplikacji. Zapewnia mechanizmy do zapisywania komunikatow o roLLnym poziomie waLLnoLci do konsoli, pliku oraz przekazywania ich do zarejestrowanych funkcji zwrotnych (callbackow).
## Zmienne globalne
## `g_logger`

Globalna, jedyna instancja klasy `Logger`.

Logger g_logger;
```
## Funkcje globalne
## `void fatalError(const char* error, const char* file, int line)`

Funkcja wywoL'ywana przez makro `VALIDATE`. Loguje bL'ad krytyczny za pomoca `g_logger.fatal`, zawierajacy komunikat, plik i numer linii, a nastepnie przerywa dziaL'anie aplikacji.
## Klasa `Logger`
## `void Logger::log(Fw::LogLevel level, const std::string& message)`
## Opis semantyczny
GL'owna, prywatna metoda logujaca. Jest bezpieczna watkowo dzieki uLLyciu `std::recursive_mutex`.
## DziaL'anie
1.  Blokuje mutex, aby zapewnic wyL'aczny dostep.
2.  W trybie `NDEBUG` (wydajnoLciowym) ignoruje wiadomoLci o poziomie `LogDebug`.
3.  Dodaje odpowiedni prefiks do wiadomoLci (np. "WARNING: ", "ERROR: ").
4.  Wypisuje sformatowana wiadomoLc na standardowe wyjLcie (`std::cout`) lub `__android_log_print` na Androidzie.
5.  JeLli ustawiono plik logu, zapisuje wiadomoLc do pliku.
6.  Dodaje wiadomoLc do wewnetrznej historii `m_logMessages`.
7.  JeLli zarejestrowano `callback` (`m_onLog`), dodaje zdarzenie do `g_dispatcher`, ktore wywoL'a ten `callback` w gL'ownym watku.
8.  JeLli poziom to `LogFatal` (lub `LogError` w trybie testowym), wyLwietla okno bL'edu (w wersji graficznej) i natychmiast koL"czy aplikacje.
## `void Logger::logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction)`

Metoda pomocnicza, ktora wzbogaca wiadomoLc o informacje o funkcji, z ktorej zostaL'a wywoL'ana, oraz o Llad stosu (traceback) z Lua i C++. ULLywana przez makra takie jak `traceError`.
## `void Logger::fireOldMessages()`

WywoL'uje `callback` `m_onLog` dla wszystkich wiadomoLci, ktore zostaL'y zalogowane przed jego zarejestrowaniem. Przydatne do wyLwietlania wczesnych logow w UI, gdy UI jest juLL gotowe.
## `void Logger::setLogFile(const std::string& file)`

Otwiera podany plik do zapisu logow. Przed otwarciem do dopisywania, odczytuje ostatnie 100 KB z istniejacego pliku do `m_lastLog`, aby moLLna byL'o przejrzec logi z poprzedniej sesji.
## ZaleLLnoLci i powiazania

-   `framework/core/logger.h`: Plik nagL'owkowy.
-   `framework/core/eventdispatcher.h`: ULLywa `g_dispatcher` do bezpiecznego wywoL'ywania `callbackow` w gL'ownym watku.
-   `framework/core/resourcemanager.h`: Potencjalnie uLLywany do rozwiazywania LcieLLek do plikow logow.
-   `framework/core/graphicalapplication.h`: W wersji graficznej, `g_window` jest uLLywane do wyLwietlania okna bL'edu krytycznego.
-   `framework/platform/platform.h`: ULLywa `g_platform` do generowania Lladu stosu C++.
-   `framework/luaengine/luainterface.h`: ULLywa `g_lua` do generowania Lladu stosu Lua.

---
# z"" module.h
## Opis ogolny

Plik `module.h` deklaruje klase `Module`, ktora jest podstawowym elementem systemu modularnoLci aplikacji. KaLLdy moduL' reprezentuje logicznie oddzielona czeLc funkcjonalnoLci (np. interfejs, mini-mapa, bot), ktora moLLe byc dynamicznie L'adowana i odL'adowywana.
## Klasa `Module`
## Opis semantyczny
`Module` enkapsuluje zestaw skryptow Lua, metadane (nazwa, autor, wersja), zaleLLnoLci od innych moduL'ow oraz wL'asne, izolowane Lrodowisko Lua (piaskownice - sandbox). Dziedziczy po `LuaObject`, dzieki czemu moLLe byc zarzadzany z poziomu skryptow Lua.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Module(const std::string& name)` | Konstruktor. |
| `bool load()` | Laduje moduL', wykonujac jego skrypty i zaleLLnoLci. |
| `void unload()` | OdL'adowuje moduL', wykonujac skrypt `onUnload`. |
| `bool reload()` | Ponownie L'aduje moduL'. |
| `bool canUnload()` | Zwraca `true`, jeLli moduL' jest przeL'adowywalny i LLaden inny moduL' od niego nie zaleLLy. |
| `bool canReload()` | Zwraca `true`, jeLli moduL' jest przeL'adowywalny i nie ma zaleLLnoLci. |
| `bool isLoaded()` | Zwraca `true`, jeLli moduL' jest zaL'adowany. |
| `bool isReloadable()` | Zwraca `true`, jeLli moduL' moLLna przeL'adowac. |
| `bool isDependent()` | Sprawdza, czy inny zaL'adowany moduL' zaleLLy od tego moduL'u. |
| `bool isSandboxed()` | Zwraca `true`, jeLli moduL' dziaL'a w odizolowanym Lrodowisku Lua. |
| `bool hasDependency(...)` | Sprawdza, czy moduL' ma dana zaleLLnoLc (opcjonalnie rekurencyjnie). |
| `int getSandbox(LuaInterface *lua)` | Umieszcza na stosie Lua tabele Lrodowiska tego moduL'u. |
| `std::string getDescription()`, `getName()`, `getAuthor()`, `getWebsite()`, `getVersion()` | Zwracaja metadane moduL'u. |
| `bool isAutoLoad()` | Zwraca `true`, jeLli moduL' powinien byc L'adowany automatycznie. |
| `int getAutoLoadPriority()` | Zwraca priorytet automatycznego L'adowania. |
## Metody chronione

-   `void discover(const OTMLNodePtr& moduleNode)`: Metoda wywoL'ywana przez `ModuleManager` do wczytania metadanych moduL'u z pliku `.otmod`.
## Zmienne prywatne

-   `m_loaded`, `m_autoLoad`, `m_reloadable`, `m_sandboxed`: Flagi stanu.
-   `m_autoLoadPriority`: Priorytet L'adowania.
-   `m_sandboxEnv`: Referencja do Lrodowiska Lua (piaskownicy).
-   `m_onLoadFunc`, `m_onUnloadFunc`: Przechowuja kod skryptow `onLoad` i `onUnload`.
-   `m_name`, `m_description`, ...: Metadane moduL'u.
-   `m_dependencies`, `m_scripts`, `m_loadLaterModules`: Listy zaleLLnoLci i skryptow.
## ZaleLLnoLci i powiazania

-   `framework/core/declarations.h`: Definicje wskaLsnikow.
-   `framework/otml/declarations.h`: ULLywa `OTMLNodePtr` do parsowania metadanych.
-   `framework/luaengine/luaobject.h`: Jest klasa pochodna `LuaObject`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami `Module` z poziomu Lua.
-   Jest zarzadzana przez `ModuleManager`.

---
# z"" modulemanager.h
## Opis ogolny

Plik `modulemanager.h` deklaruje klase `ModuleManager`, ktora jest singletonem (`g_modules`) odpowiedzialnym za zarzadzanie cyklem LLycia wszystkich moduL'ow w aplikacji.
## Klasa `ModuleManager`
## Opis semantyczny
`ModuleManager` peL'ni role centralnego rejestru moduL'ow. Odpowiada za ich odkrywanie (przez skanowanie katalogow w poszukiwaniu plikow `.otmod`), L'adowanie w odpowiedniej kolejnoLci (z uwzglednieniem zaleLLnoLci i priorytetow), a takLLe za ich odL'adowywanie i ponowne L'adowanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void clear()` | CzyLci liste moduL'ow. |
| `void discoverModules()` | Przeszukuje system plikow w poszukiwaniu plikow `.otmod` i tworzy dla nich obiekty `Module`. |
| `void autoLoadModules(int maxPriority)` | Laduje wszystkie moduL'y, ktore maja flage `autoload` i priorytet nie wiekszy niLL podany. |
| `ModulePtr discoverModule(...)` | Parsuje pojedynczy plik `.otmod` i tworzy lub aktualizuje obiekt `Module`. |
| `void ensureModuleLoaded(...)` | Upewnia sie, LLe dany moduL' jest zaL'adowany; jeLli nie, probuje go zaL'adowac, a w razie poraLLki koL"czy aplikacje. |
| `void unloadModules()` | OdL'adowuje wszystkie zaL'adowane moduL'y. |
| `void reloadModules()` | Probuje odL'adowac i ponownie zaL'adowac wszystkie moduL'y, ktore na to pozwalaja. |
| `ModulePtr getModule(...)` | Zwraca wskaLsnik do moduL'u o podanej nazwie. |
| `std::deque<ModulePtr> getModules()` | Zwraca liste wszystkich odkrytych moduL'ow. |
## Metody chronione

-   `void updateModuleLoadOrder(ModulePtr module)`: Aktualizuje wewnetrzna kolejke moduL'ow, aby zachowac poprawna kolejnoLc L'adowania/odL'adowywania.
## Zmienne prywatne

-   `m_modules`: Kolejka (`std::deque`) wszystkich odkrytych moduL'ow. ZaL'adowane moduL'y sa na poczatku.
-   `m_autoLoadModules`: Mapa (`std::multimap`) przechowujaca moduL'y do automatycznego zaL'adowania, posortowane wedL'ug priorytetu.
## Zmienne globalne

-   `g_modules`: Globalna instancja `ModuleManager`.
## ZaleLLnoLci i powiazania

-   `framework/core/module.h`: Definicja klasy `Module`, ktora zarzadza `ModuleManager`.
-   Jest oznaczona jako `@bindsingleton g_modules`, co udostepnia jej API w skryptach Lua.
-   WspoL'pracuje z `ResourceManager` do przeszukiwania systemu plikow i z `Application` do inicjalizacji i zamykania.

---
# z"" scheduledevent.cpp
## Opis ogolny

Plik `scheduledevent.cpp` zawiera implementacje klasy `ScheduledEvent`, ktora reprezentuje zdarzenie zaplanowane do wykonania w przyszL'oLci.
## Klasa `ScheduledEvent`
## `ScheduledEvent::ScheduledEvent(...)`

Konstruktor, ktory dziedziczy po `Event` i dodatkowo inicjalizuje parametry zwiazane z czasem.

-   **Parametry**:
    -   `function`, `callback`, `botSafe`: Przekazywane do konstruktora klasy bazowej `Event`.
    -   `delay`: Czas w milisekundach, po ktorym zdarzenie ma zostac wykonane po raz pierwszy.
    -   `maxCycles`: Maksymalna liczba wykonaL". `0` oznacza nieskoL"czonoLc.
-   **DziaL'anie**:
    -   Oblicza czas pierwszego wykonania: `m_ticks = g_clock.millis() + delay`.
    -   Zapisuje opoLsnienie, maksymalna liczbe cykli i zeruje licznik wykonanych cykli.
## `void ScheduledEvent::execute()`
## Opis semantyczny
Wykonuje `callback` zdarzenia, jeLli warunki sa speL'nione.
## DziaL'anie
1.  Sprawdza, czy zdarzenie nie jest anulowane, czy `callback` istnieje i czy nie przekroczono `maxCycles`.
2.  JeLli warunki sa speL'nione, wykonuje `callback` i ustawia `m_executed` na `true`. W przeciwieL"stwie do `Event`, nie resetuje `callback`, poniewaLL moLLe byc on potrzebny w nastepnym cyklu.
3.  JeLli warunki nie sa speL'nione (np. zdarzenie jednorazowe zostaL'o wykonane), resetuje `callback` do `nullptr`.
4.  Inkrementuje licznik `m_cyclesExecuted`.
## `bool ScheduledEvent::nextCycle()`
## Opis semantyczny
Przygotowuje zdarzenie do nastepnego cyklu. Jest wywoL'ywana przez `EventDispatcher` po wykonaniu zdarzenia.
## DziaL'anie
1.  Sprawdza, czy zdarzenie powinno byc wykonane ponownie (nieanulowane, nie przekroczono `maxCycles`).
2.  JeLli tak, przesuwa czas nastepnego wykonania o `m_delay`: `m_ticks += m_delay` i zwraca `true`.
3.  JeLli nie, resetuje `callback` do `nullptr` i zwraca `false`, co powoduje usuniecie zdarzenia z kolejki dyspozytora.
## ZaleLLnoLci i powiazania

-   `framework/core/scheduledevent.h`: Plik nagL'owkowy.
-   `framework/core/clock.h`: ULLywa `g_clock.millis()` do pobierania bieLLacego czasu.
-   Jest tworzona i zarzadzana przez `EventDispatcher`.

---
# z"" resourcemanager.cpp
## Opis ogolny

Plik `resourcemanager.cpp` zawiera implementacje klasy `ResourceManager`, ktora jest sercem systemu zarzadzania zasobami aplikacji. Implementuje ona logike wyszukiwania, L'adowania, odczytu i zapisu plikow, abstrakcjonujac LsrodL'o danych (dysk, archiwum, pamiec).
## Klasa `ResourceManager`
## `void ResourceManager::init(const char *argv0)`

Inicjalizuje biblioteke PhysFS i ustala LcieLLke do pliku wykonywalnego aplikacji na podstawie argumentu `argv0`.
## `bool ResourceManager::setupWriteDir(...)`

Konfiguruje katalog zapisu dla aplikacji, uLLywajac `PHYSFS_getPrefDir`. Ten katalog jest zazwyczaj zlokalizowany w folderze danych uLLytkownika (np. `%APPDATA%` na Windows, `~/.local/share` na Linux). Montuje ten katalog i ustawia go jako domyLlny katalog do zapisu.
## `bool ResourceManager::setup()`

Kluczowa metoda, ktora probuje zlokalizowac i zamontowac gL'owny katalog roboczy aplikacji. Przeszukuje kilka potencjalnych lokalizacji w nastepujacej kolejnoLci:
1.  Katalogi na dysku (katalog zapisu, bieLLacy katalog, katalog bazowy).
2.  Archiwum `data.zip` w tych samych lokalizacjach.
3.  Dane wbudowane w sam plik wykonywalny (`loadDataFromSelf`).
## `std::string ResourceManager::getCompactName()`

Metoda probujaca odgadnac "skrocona nazwe" aplikacji na podstawie zawartoLci pliku `init.lua`, ktory powinien zawierac definicje `APP_NAME`. Jest to uLLywane m.in. do tworzenia katalogu zapisu.
## `bool ResourceManager::loadDataFromSelf(...)`

Przeszukuje plik binarny aplikacji w poszukiwaniu sygnatury archiwum ZIP (`PK..`). JeLli znajdzie, traktuje reszte pliku jako archiwum i montuje je w pamieci za pomoca `PHYSFS_mountMemory`.
## `std::string ResourceManager::readFileContents(...)`

Odczytuje zawartoLc pliku. Po odczytaniu surowych bajtow, probuje je zdeszyfrowac za pomoca `decryptBuffer`. ObsL'uguje rownieLL specjalny wirtualny katalog `/downloads` do odczytu plikow pobranych przez `Http`.
## `bool ResourceManager::decryptBuffer(std::string& buffer)`

Deszyfruje bufor, jeLli jest on zaszyfrowany (rozpoznaje po nagL'owku "ENC3"). Proces deszyfracji obejmuje:
1.  Odczytanie metadanych (klucz, rozmiary, suma kontrolna).
2.  Deszyfracje za pomoca algorytmu `bdecrypt` (odmiana TEA/XTEA).
3.  Dekompresje za pomoca ZLIB.
4.  Weryfikacje sumy kontrolnej Adler-32.
## `bool ResourceManager::encryptBuffer(...)`

Szyfruje bufor, wykonujac operacje odwrotne do `decryptBuffer`: kompresja, szyfrowanie i dodanie nagL'owka. Dostepne tylko z flaga `WITH_ENCRYPTION`.
## `std::string ResourceManager::resolvePath(std::string path)`

Konwertuje LcieLLke wzgledna na LcieLLke absolutna w wirtualnym systemie plikow. ObsL'uguje LcieLLki wzgledne do bieLLacego skryptu Lua oraz specjalne LcieLLki dla layoutow UI (np. `/layouts/nazwa_layoutu/...`).
## `updateData(...)` i `updateExecutable(...)`

Metody sL'uLLace do aktualizacji klienta. `updateData` przebudowuje archiwum `data.zip` na podstawie pobranych plikow, a `updateExecutable` zastepuje plik binarny nowa wersja.
## `createArchive(...)` i `decompressArchive(...)`

Metody pomocnicze do tworzenia i rozpakowywania archiwow ZIP w pamieci przy uLLyciu biblioteki `libzip`.
## ZaleLLnoLci i powiazania

-   `framework/core/resourcemanager.h`: Plik nagL'owkowy.
-   **PhysFS**: Podstawowa zaleLLnoLc do obsL'ugi wirtualnego systemu plikow.
-   **ZLIB, LibZip**: Do obsL'ugi kompresji i archiwow.
-   `framework/platform/platform.h`: Do operacji specyficznych dla systemu, jak pobieranie bieLLacego katalogu.
-   `framework/util/crypt.h`: Do szyfrowania, deszyfrowania i obliczania sum kontrolnych.
-   `framework/http/http.h`: Do obsL'ugi wirtualnego katalogu `/downloads`.
-   `boost/process.hpp`: Do uruchamiania nowszej wersji klienta.

---
# z"" scheduledevent.h
## Opis ogolny

Plik `scheduledevent.h` deklaruje klase `ScheduledEvent`, ktora rozszerza funkcjonalnoLc `Event`, dodajac moLLliwoLc planowania wykonania w czasie, cyklicznoLci oraz obsL'ugi opoLsnieL".
## Klasa `ScheduledEvent`
## Opis semantyczny
`ScheduledEvent` to zdarzenie, ktore nie jest wykonywane natychmiast, lecz po upL'ywie okreLlonego czasu (`delay`). MoLLe byc jednorazowe lub cykliczne (`maxCycles`). Jest zarzadzane przez `EventDispatcher` w kolejce priorytetowej, gdzie priorytetem jest czas wykonania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ScheduledEvent(...)` | Konstruktor, ustawia parametry czasowe zdarzenia. |
| `void execute()` | Wykonuje `callback` i inkrementuje licznik wykonanych cykli. |
| `bool nextCycle()` | Przygotowuje zdarzenie do nastepnego cyklu, aktualizujac czas wykonania. Zwraca `false`, jeLli zdarzenie nie powinno byc ponownie wykonane. |
| `int ticks()` | Zwraca absolutny czas (w tickach), w ktorym zdarzenie ma zostac wykonane. |
| `int remainingTicks()` | Zwraca czas pozostaL'y do wykonania zdarzenia. |
| `int delay()` | Zwraca opoLsnienie miedzy cyklami. |
| `int cyclesExecuted()` | Zwraca liczbe dotychczasowych wykonaL". |
| `int maxCycles()` | Zwraca maksymalna liczbe wykonaL" (0 dla nieskoL"czonoLci). |
## Zmienne prywatne

-   `m_ticks`: Czas (w tickach systemowych), w ktorym ma nastapic nastepne wykonanie.
-   `m_delay`: OpoLsnienie miedzy kolejnymi wykonaniami.
-   `m_maxCycles`: Maksymalna liczba wykonaL".
-   `m_cyclesExecuted`: Licznik wykonanych cykli.
## Struktura `lessScheduledEvent`

Funktor (obiekt funkcyjny) uLLywany przez `std::priority_queue` w `EventDispatcher` do sortowania zdarzeL". Zapewnia, LLe zdarzenia z najwczeLniejszym czasem wykonania maja najwyLLszy priorytet.

struct lessScheduledEvent {
    bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b) {
        return  b->ticks() < a->ticks();
}
};
```
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/event.h`: Klasa bazowa `Event`.
-   `framework/core/clock.h`: ULLywa `g_clock` do pobierania bieLLacego czasu.
-   Jest tworzona przez `EventDispatcher` i zarzadzana w jego kolejce priorytetowej.
-   Oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami tego typu z poziomu Lua.

---
# z"" timer.cpp
## Opis ogolny

Plik `timer.cpp` zawiera implementacje prostych metod klasy `Timer`, ktora sL'uLLy do mierzenia upL'ywu czasu.
## Klasa `Timer`
## `void Timer::restart()`
## Opis semantyczny
Resetuje timer, ustawiajac jego punkt startowy na bieLLacy czas.
## DziaL'anie
1.  Pobiera aktualny czas w milisekundach za pomoca `g_clock.millis()`.
2.  Zapisuje te wartoLc do `m_startTicks`.
3.  Ustawia flage `m_stopped` na `false`.
## `ticks_t Timer::ticksElapsed()`
## Opis semantyczny
Oblicza i zwraca czas, jaki upL'ynaL' od ostatniego zresetowania timera.
## DziaL'anie
-   Zwraca roLLnice miedzy aktualnym czasem (`g_clock.millis()`) a zapisanym czasem startowym (`m_startTicks`).
## ZaleLLnoLci i powiazania

-   `framework/core/timer.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/core/clock.h`: ULLywa `g_clock` do pobierania bieLLacego czasu, co zapewnia spojnoLc z buforowanym czasem klatki.

---
# z"" timer.h
## Opis ogolny

Plik `timer.h` deklaruje klase `Timer`, ktora jest prostym, ale uLLytecznym narzedziem do mierzenia upL'ywajacego czasu. Jest to klasa pomocnicza, szeroko stosowana w caL'ym frameworku do obsL'ugi opoLsnieL", animacji i synchronizacji.
## Klasa `Timer`
## Opis semantyczny
`Timer` dziaL'a jak stoper. Po utworzeniu lub zresetowaniu (`restart()`) zapamietuje punkt w czasie. Nastepnie moLLna w dowolnym momencie sprawdzic, ile czasu upL'yneL'o od tego punktu za pomoca metod `ticksElapsed()` lub `timeElapsed()`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Timer()` | Konstruktor, ktory natychmiast wywoL'uje `restart()`. |
| `void restart()` | Resetuje timer, ustawiajac jego punkt startowy na bieLLacy czas. |
| `void stop()` | Zatrzymuje timer (ustawia flage `m_stopped`). |
| `void adjust(ticks_t value)` | Przesuwa punkt startowy o podana wartoLc, efektywnie "dodajac" lub "odejmujac" czas. |
| `ticks_t startTicks()` | Zwraca punkt startowy timera w tickach. |
| `ticks_t ticksElapsed()` | Zwraca czas, jaki upL'ynaL' od startu, w milisekundach. |
| `float timeElapsed()` | Zwraca czas, jaki upL'ynaL' od startu, w sekundach. |
| `bool running()` | Zwraca `true`, jeLli timer nie zostaL' zatrzymany. |
## Zmienne prywatne

-   `m_startTicks`: Czas (w tickach/milisekundach), w ktorym timer zostaL' uruchomiony/zresetowany.
-   `m_stopped`: Flaga wskazujaca, czy timer jest zatrzymany.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje, w tym `ticks_t`.
-   ULLywa `g_clock` (poprzez `ticksElapsed`) do pomiaru czasu.
-   Jest wykorzystywana w wielu miejscach, np. w `UIWidget` do obsL'ugi podwojnego klikniecia (`m_clickTimer`), w `PlatformWindow` do ograniczania czestotliwoLci sprawdzania klawiszy (`m_keyPressTimer`), oraz w animacjach.

---
# z"" consoleapplication.cpp
## Opis ogolny

Plik `consoleapplication.cpp` zawiera implementacje klasy `ConsoleApplication`, ktora jest wersja aplikacji przeznaczona do dziaL'ania w trybie tekstowym, bez interfejsu graficznego. Jest ona uLLywana, gdy projekt jest kompilowany bez flagi `FW_GRAPHICS`.
## Zmienne globalne
## `g_app`

Globalna instancja `ConsoleApplication`. Gdy framework jest kompilowany w trybie konsolowym, ta instancja staje sie gL'ownym obiektem aplikacji.

ConsoleApplication g_app;
```
## Klasa `ConsoleApplication`
## `void ConsoleApplication::run()`
## Opis semantyczny
Implementuje gL'owna petle aplikacji konsolowej. W przeciwieL"stwie do `GraphicalApplication`, jest to prosta petla, ktora regularnie przetwarza zdarzenia i usypia watek, aby nie zuLLywac 100% zasobow procesora.
## DziaL'anie
1.  Ustawia flage `m_running` na `true`.
2.  Wykonuje pierwsze wywoL'anie `poll()`, aby przetworzyc ewentualne poczatkowe zdarzenia.
3.  Aktualizuje zegar (`g_clock.update()`).
4.  WywoL'uje funkcje `onRun` w globalnym skrypcie Lua (`g_app.onRun`).
5.  Wchodzi w petle, ktora trwa, dopoki flaga `m_stopping` nie zostanie ustawiona na `true`.
6.  W kaLLdej iteracji petli:
    -   WywoL'uje `poll()` do przetworzenia zdarzeL" (np. sieciowych, zaplanowanych).
    -   Usypia gL'owny watek na 1 milisekunde (`stdext::millisleep(1)`).
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Aktualizuje licznik klatek/iteracji (`m_frameCounter.update()`).
7.  Po wyjLciu z petli, resetuje flagi `m_stopping` i `m_running`.

> **NOTE:** Pomimo braku grafiki, wciaLL istnieje pojecie "klatki" lub iteracji, ktore jest Lledzone przez `m_frameCounter`.
## ZaleLLnoLci i powiazania

-   `framework/core/consoleapplication.h`: Plik nagL'owkowy dla tej klasy.
-   `framework/core/clock.h`: ULLywa `g_clock` do aktualizacji czasu w kaLLdej iteracji.
-   `framework/luaengine/luainterface.h`: ULLywa `g_lua` do wywoL'ania `onRun`.
-   `framework/net/connection.h`: Metoda `poll()` wywoL'uje m.in. `Connection::poll()`, wiec aplikacja konsolowa moLLe obsL'ugiwac siec.

---
# z"" shaderprogram.h
## Opis ogolny

Plik `shaderprogram.h` deklaruje klase `ShaderProgram`, ktora jest obiektowym opakowaniem na program shadera w OpenGL. Zarzadza ona kompilacja, linkowaniem i aktywacja shaderow wierzchoL'kow i fragmentow.
## Klasa `ShaderProgram`
## Opis semantyczny
`ShaderProgram` agreguje obiekty `Shader` (reprezentujace pojedyncze shadery, np. wierzchoL'kow lub fragmentow), linkuje je w jeden wykonywalny program, ktory moLLe byc uLLyty w potoku renderowania OpenGL, i dostarcza interfejs do ustawiania uniformow i atrybutow. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ShaderProgram(const std::string& name)` | Konstruktor, tworzy program shadera. |
| `static PainterShaderProgramPtr create(...)` | Statyczna metoda fabryczna do tworzenia `PainterShaderProgram`. |
| `bool addShader(...)` | Dodaje skompilowany obiekt `Shader` do programu. |
| `bool addShaderFromSourceCode(...)` | Tworzy, kompiluje i dodaje shader z kodu LsrodL'owego. |
| `bool addShaderFromSourceFile(...)` | Tworzy, kompiluje i dodaje shader z pliku. |
| `void removeShader(...)` | Usuwa shader z programu. |
| `bool link()` | Linkuje wszystkie dodane shadery w jeden program. |
| `bool bind()` | Aktywuje ten program shadera w kontekLcie OpenGL. |
| `static void release()` | Deaktywuje jakikolwiek aktywny program shadera. |
| `std::string log()` | Zwraca logi z procesu linkowania. |
| `static void disableAttributeArray(...)` | WyL'acza tablice atrybutow wierzchoL'kow. |
| `static void enableAttributeArray(...)` | WL'acza tablice atrybutow wierzchoL'kow. |
| `int getAttributeLocation(...)` | Pobiera lokalizacje atrybutu o danej nazwie. |
| `void bindAttributeLocation(...)` | Przypisuje lokalizacje do atrybutu (przed linkowaniem). |
| `void bindUniformLocation(...)` | Wyszukuje i buforuje lokalizacje uniformu. |
| `void setAttributeArray(...)` | Ustawia wskaLsnik na dane dla tablicy atrybutow. |
| `void setAttributeValue(...)` | Ustawia wartoLc dla pojedynczego atrybutu. |
| `void setUniformValue(...)` | Ustawia wartoLc dla uniformu (przeciaLLona dla roLLnych typow: `int`, `float`, `Color`, `Matrix`). |
| `bool isLinked()` | Zwraca `true`, jeLli program zostaL' pomyLlnie zlinkowany. |
| `uint getProgramId()` | Zwraca ID programu OpenGL. |
| `ShaderList getShaders()` | Zwraca liste powiazanych shaderow. |
| `std::string getName()` | Zwraca nazwe programu. |
## Zmienne prywatne

-   `m_name`: Nazwa programu (dla celow identyfikacji).
-   `m_linked`: Flaga wskazujaca, czy program jest zlinkowany.
-   `m_programId`: ID programu w OpenGL.
-   `m_currentProgram`: Statyczna zmienna Lledzaca aktualnie aktywny program.
-   `m_shaders`: Lista powiazanych obiektow `Shader`.
-   `m_uniformLocations`: Tablica przechowujaca zbuforowane lokalizacje uniformow.
## ZaleLLnoLci i powiazania

-   `framework/graphics/shader.h`: Definicja klasy `Shader`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Jest klasa bazowa dla `PainterShaderProgram`, ktora rozszerza ja o uniformy specyficzne dla `Painter`.
-   Jest zarzadzana przez `ShaderManager`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami tego typu z poziomu Lua.

---
# z"" animatedtexture.cpp
## Opis ogolny

Plik `animatedtexture.cpp` zawiera implementacje klasy `AnimatedTexture`, ktora reprezentuje teksture skL'adajaca sie z wielu klatek, odtwarzanych w petli. Jest to podklasa `Texture`.
## Klasa `AnimatedTexture`
## `AnimatedTexture::AnimatedTexture(...)`

Konstruktor, ktory tworzy animowana teksture.

-   **Parametry**:
    -   `size`: Rozmiar pojedynczej klatki.
    -   `frames`: Wektor wskaLsnikow na obiekty `Image`, reprezentujace poszczegolne klatki animacji.
    -   `framesDelay`: Wektor czasow (w milisekundach), jak dL'ugo kaLLda klatka ma byc wyLwietlana.
    -   `buildMipmaps`, `compress`: Flagi przekazywane do konstruktora `Texture` dla kaLLdej klatki.
-   **DziaL'anie**:
    1.  Iteruje przez wektor `frames` i dla kaLLdego `Image` tworzy nowy obiekt `Texture`, ktory jest przechowywany w `m_frames`.
    2.  Inicjalizuje timer `m_animTimer` i ustawia bieLLaca klatke na 0.
## `bool AnimatedTexture::buildHardwareMipmaps()`

WL'acza generowanie mipmap dla wszystkich klatek animacji.
## `void AnimatedTexture::setSmooth(bool smooth)` i `void AnimatedTexture::setRepeat(bool repeat)`

Ustawiaja odpowiednio flagi wygL'adzania i powtarzania dla wszystkich tekstur-klatek.
## `void AnimatedTexture::update()`
## Opis semantyczny
Aktualizuje stan animacji. Ta metoda jest kluczowa i musi byc wywoL'ywana przed kaLLdym uLLyciem tekstury w petli renderowania.
## DziaL'anie
1.  Sprawdza, czy czas, jaki upL'ynaL' od ostatniej zmiany klatki (`m_animTimer.ticksElapsed()`) jest wiekszy lub rowny czasowi opoLsnienia dla bieLLacej klatki (`m_framesDelay[m_currentFrame]`).
2.  JeLli tak, przechodzi do nastepnej klatki, zapetlajac animacje (`m_currentFrame = (m_currentFrame + 1) % m_frames.size()`), i resetuje timer.
3.  WywoL'uje `update()` na teksturze bieLLacej klatki.
4.  Aktualizuje ID tekstury (`m_id`) i unikalne ID (`m_uniqueId`) klasy bazowej `Texture` na wartoLci z bieLLacej klatki. Dzieki temu reszta systemu renderujacego moLLe traktowac `AnimatedTexture` jak zwykL'a, statyczna teksture, nie wiedzac, LLe jej ID zmienia sie w czasie.
## ZaleLLnoLci i powiazania

-   `framework/graphics/animatedtexture.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do operacji na OpenGL.
-   `framework/core/eventdispatcher.h`: Potencjalnie do planowania aktualizacji.
-   Jest tworzona i zarzadzana przez `TextureManager` podczas L'adowania animowanych plikow PNG (APNG).

---
# z"" animatedtexture.h
## Opis ogolny

Plik `animatedtexture.h` deklaruje klase `AnimatedTexture`, ktora jest specjalizacja klasy `Texture`. Reprezentuje ona teksture, ktora zmienia swoj wyglad w czasie, odtwarzajac sekwencje klatek.
## Klasa `AnimatedTexture`
## Opis semantyczny
`AnimatedTexture` dziedziczy po `Texture` i przechowuje kolekcje tekstur (`std::vector<TexturePtr>`), ktore reprezentuja poszczegolne klatki animacji. Wewnetrzny timer (`m_animTimer`) kontroluje, ktora klatka jest aktualnie aktywna. Metoda `update()` jest odpowiedzialna za przeL'aczanie klatek i aktualizowanie ID tekstury w klasie bazowej, dzieki czemu dla systemu renderujacego wyglada ona jak pojedyncza, dynamicznie zmieniajaca sie tekstura.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `AnimatedTexture(...)` | Konstruktor, tworzy animowana teksture z wektora obrazow i czasow opoLsnieL". |
| `virtual ~AnimatedTexture()` | Destruktor. |
| `void replace(const ImagePtr& image)` | Pusta implementacja; zastepowanie animowanej tekstury pojedynczym obrazem nie jest obsL'ugiwane w ten sposob. |
| `void update()` | Aktualizuje bieLLaca klatke animacji. |
| `virtual bool isAnimatedTexture()` | Zwraca `true`, odroLLniajac te klase od `Texture`. |
## Metody chronione

-   `virtual bool buildHardwareMipmaps()`: WL'acza mipmapping dla wszystkich klatek.
-   `virtual void setSmooth(bool smooth)`: Ustawia wygL'adzanie dla wszystkich klatek.
-   `virtual void setRepeat(bool repeat)`: Ustawia powtarzanie dla wszystkich klatek.
## Zmienne prywatne

-   `m_frames`: Wektor wskaLsnikow na tekstury poszczegolnych klatek.
-   `m_framesDelay`: Wektor czasow opoLsnieL" dla kaLLdej klatki.
-   `m_currentFrame`: Indeks bieLLacej klatki.
-   `m_animTimer`: Timer do Lledzenia czasu wyLwietlania klatki.
## ZaleLLnoLci i powiazania

-   `framework/graphics/texture.h`: Klasa bazowa `Texture`.
-   `framework/core/timer.h`: ULLywa `Timer` do zarzadzania animacja.
-   Jest tworzona przez `TextureManager` podczas L'adowania plikow APNG (Animated PNG).

---
# z"" apngloader.cpp
## Opis ogolny

Plik `apngloader.cpp` zawiera implementacje funkcji do L'adowania animowanych plikow PNG (APNG) oraz do zapisu standardowych plikow PNG. Kod jest oparty na bibliotece APNG Disassembler 2.3 autorstwa Maxa Stepina i zostaL' dostosowany do potrzeb frameworka.
## Funkcje
## `load_apng(std::stringstream& file, struct apng_data *apng)`
## Opis semantyczny
GL'owna funkcja do parsowania pliku w formacie APNG. Odczytuje ona poszczegolne "chunki" (fragmenty) pliku PNG, takie jak `IHDR` (nagL'owek), `PLTE` (paleta), `tRNS` (przezroczystoLc), `acTL` (nagL'owek animacji), `fcTL` (kontrola klatki) oraz `IDAT`/`fdAT` (dane obrazu).
## DziaL'anie
1.  Sprawdza sygnature pliku PNG.
2.  Odczytuje nagL'owek `IHDR` w celu uzyskania wymiarow, gL'ebi kolorow i innych podstawowych informacji.
3.  Alokuje bufory na zdekompresowane dane obrazu.
4.  W petli odczytuje kolejne chunki:
    -   `PLTE` i `tRNS`: Wczytuje palete kolorow i informacje o przezroczystoLci.
    -   `acTL`: Identyfikuje plik jako animowany, odczytuje liczbe klatek i zapetleL".
    -   `fcTL`: Odczytuje metadane dla pojedynczej klatki, takie jak wymiary, przesuniecie, czas trwania i operacje mieszania (`blend_op`) oraz usuwania (`dispose_op`).
    -   `IDAT` i `fdAT`: Gromadzi skompresowane dane obrazu dla klatki.
5.  Po odczytaniu danych dla klatki (`fcTL` lub `IEND`), dekompresuje je za pomoca ZLIB (`inflate`), a nastepnie odfiltrowuje (usuwa filtry PNG takie jak Sub, Up, Average, Paeth).
6.  Komponuje finalny obraz klatki na podstawie poprzedniej klatki, stosujac operacje `dispose_op` (np. zostaw, wyczyLc do tL'a) i `blend_op` (np. zastap, naL'oLL).
7.  Wynikowe dane klatki w formacie RGBA sa zapisywane do bufora w strukturze `apng_data`.
8.  Zwraca 0 w przypadku sukcesu, -1 w przypadku bL'edu.
## `save_png(std::stringstream& f, unsigned int width, unsigned int height, int channels, unsigned char *pixels)`
## Opis semantyczny
Zapisuje dane obrazu do formatu PNG. Implementuje podstawowa kompresje z filtrowaniem, dynamicznie wybierajac najlepszy filtr dla kaLLdej linii obrazu w celu uzyskania lepszej kompresji.
## DziaL'anie
1.  Zapisuje sygnature PNG i nagL'owek `IHDR`.
2.  Inicjalizuje strumienie kompresji ZLIB.
3.  Dla kaLLdej linii obrazu:
    -   Testuje piec roLLnych filtrow PNG (None, Sub, Up, Average, Paeth).
    -   Wybiera filtr, ktory generuje dane o najmniejszej sumie wartoLci bezwzglednych bajtow (co zwykle prowadzi do lepszej kompresji).
    -   Kompresuje przefiltrowana linie za pomoca `deflate`.
4.  Zapisuje skompresowane dane w chunkach `IDAT`.
5.  Zapisuje chunk koL"cowy `IEND`.
## Funkcje pomocnicze

Plik zawiera wiele funkcji pomocniczych, m.in.:
-   `read32`, `read16`: Do odczytu liczb w porzadku big-endian.
-   `read_sub_row`, `read_up_row`, `read_average_row`, `read_paeth_row`: Do odfiltrowywania danych obrazu PNG.
-   `compose0`, `compose2`, `compose3`, `compose4`, `compose6`: Do kompozycji klatek animacji, konwertujac roLLne formaty pikseli na RGBA i stosujac operacje mieszania.
-   `unpack`: Dekompresuje i odfiltrowuje dane jednej klatki.
-   `write_chunk`, `write_IDATs`: Do zapisu chunkow PNG.
-   `free_apng`: Zwalnia pamiec zaalokowana w strukturze `apng_data`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/apngloader.h`: Plik nagL'owkowy.
-   **ZLIB**: ULLywana do kompresji i dekompresji danych obrazu.
-   Jest uLLywana przez `Image::loadPNG` do L'adowania obrazow i `Image::savePNG` do ich zapisu.

---
# z"" apngloader.h
## Opis ogolny

Plik `apngloader.h` jest plikiem nagL'owkowym, ktory deklaruje struktury danych i funkcje do obsL'ugi plikow w formacie APNG (Animated PNG). Definiuje on publiczny interfejs do L'adowania, zapisywania i zwalniania danych obrazu.
## Struktura `apng_data`
## Opis semantyczny
Struktura ta przechowuje wszystkie zdekompresowane i sparsowane dane z pliku APNG.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `pdata` | `unsigned char *` | WskaLsnik na surowe dane pikseli wszystkich klatek, w formacie RGBA, jedna po drugiej. |
| `width` | `unsigned int` | SzerokoLc obrazu w pikselach. |
| `height` | `unsigned int` | WysokoLc obrazu w pikselach. |
| `first_frame`| `unsigned int` | Indeks pierwszej klatki animacji (zwykle 0). |
| `last_frame` | `unsigned int` | Indeks ostatniej klatki animacji. |
| `bpp` | `unsigned char` | Liczba bajtow na piksel. |
| `coltype` | `unsigned char` | Typ koloru z nagL'owka PNG. |
| `num_frames` | `unsigned int` | CaL'kowita liczba klatek w animacji. |
| `num_plays` | `unsigned int` | Liczba powtorzeL" animacji (0 oznacza nieskoL"czonoLc). |
| `frames_delay`| `unsigned short *` | Tablica czasow wyLwietlania dla kaLLdej klatki, w milisekundach. |
## Funkcje publiczne

| Funkcja | Opis |
| :--- | :--- |
| `int load_apng(std::stringstream& file, struct apng_data *apng)` | Laduje i parsuje dane APNG ze strumienia `file` i zapisuje wyniki w strukturze `apng`. Zwraca 0 w przypadku sukcesu, -1 w przypadku bL'edu. |
| `void save_png(std::stringstream& file, ...)` | Zapisuje dane obrazu (pojedynczej klatki) do strumienia `file` w formacie PNG. |
| `void free_apng(struct apng_data *apng)` | Zwalnia pamiec zaalokowana dynamicznie w strukturze `apng_data` (tj. `pdata` i `frames_delay`). |
## ZaleLLnoLci i powiazania

-   `<sstream>`: ULLywa `std::stringstream` jako LsrodL'a danych wejLciowych i wyjLciowych.
-   Funkcje te sa wykorzystywane przez klase `Image` do implementacji metod `loadPNG` i `savePNG`.

---
# z"" atlas.cpp
## Opis ogolny

Plik `atlas.cpp` implementuje klase `Atlas`, ktora zarzadza tzw. "atlasem tekstur". Jest to technika optymalizacyjna, polegajaca na L'aczeniu wielu maL'ych tekstur w jedna duLLa teksture, aby zminimalizowac liczbe zmian stanu w potoku renderowania grafiki (zmiana tekstury jest kosztowna operacja).
## Zmienne globalne
## `g_atlas`

Globalna instancja klasy `Atlas`, zapewniajaca scentralizowany dostep do mechanizmu cachowania tekstur.

Atlas g_atlas;
```
## Klasa `Atlas`
## `void Atlas::init()`
## Opis semantyczny
Inicjalizuje atlas.
## DziaL'anie
1.  OkreLla maksymalny rozmiar tekstury atlasu, biorac pod uwage ograniczenia karty graficznej (`g_graphics.getMaxTextureSize()`), ale nie przekraczajac `4096x4096`.
2.  Tworzy dwa obiekty `FrameBuffer`:
    -   `m_atlas[0]`: GL'owny atlas dla ogolnych tekstur.
    -   `m_atlas[1]`: Atlas dla tekstur fontow.
3.  WiaLLe tekstury atlasow do jednostek teksturujacych `GL_TEXTURE6` i `GL_TEXTURE7`, aby byL'y globalnie dostepne dla shaderow.
4.  Resetuje oba atlasy, przygotowujac je do uLLycia.
## `void Atlas::reset()` i `void Atlas::resetAtlas(int location)`

Metody do czyszczenia atlasu. `reset()` czyLci gL'owny atlas i bufor `m_cache`. `resetAtlas()` przygotowuje konkretny atlas do ponownego uLLycia, czyszczac jego zawartoLc (wypeL'niajac przezroczystoLcia) i resetujac informacje o wolnych przestrzeniach (`m_locations`).
## `void Atlas::terminate()`

Zwalnia obiekty `FrameBuffer` atlasow.
## `Point Atlas::cache(uint64_t hash, const Size& size, bool& draw)`
## Opis semantyczny
GL'owna metoda do cachowania tekstury. Sprawdza, czy tekstura o danym hashu jest juLL w atlasie. JeLli nie, znajduje dla niej wolne miejsce.
## DziaL'anie
1.  JeLli `m_doReset` jest `true`, najpierw resetuje atlas.
2.  Sprawdza, czy hash istnieje w `m_cache`. JeLli tak, zwraca zapisana pozycje.
3.  JeLli nie, oblicza, jakiego rozmiaru bloku potrzebuje tekstura (`calculateIndex`).
4.  JeLli tekstura jest za duLLa, zwraca `Point(-1, -1)`.
5.  Probuje znaleLsc wolne miejsce w `m_locations`. JeLli go nie ma, wywoL'uje `findSpace` w celu podziaL'u wiekszego bloku.
6.  JeLli nie ma miejsca, ustawia `m_doReset = true` i zwraca `Point(-1, -1)`.
7.  JeLli miejsce sie znajdzie, zapisuje pozycje w `m_cache`, ustawia `draw = true` (sygnalizujac, LLe tekstura musi zostac narysowana w atlasie) i zwraca pozycje.
## `void Atlas::bind()` i `void Atlas::release()`

Metody do bindowania i zwalniania `FrameBuffer` gL'ownego atlasu, aby umoLLliwic rysowanie w nim nowych tekstur.
## `Point Atlas::cacheFont(const TexturePtr& fontTexture)`

Specjalna metoda do cachowania tekstur fontow w drugim atlasie (`m_atlas[1]`). DziaL'a podobnie do `cache`, ale od razu rysuje teksture fontu w znalezionym miejscu.
## `int Atlas::calculateIndex(const Size& size)`

Oblicza indeks (od 0 do 6) odpowiadajacy rozmiarowi bloku potrzebnego do przechowania tekstury (np. 32x32, 64x64, ..., 2048x2048).
## `bool Atlas::findSpace(int location, int index)`

Rekurencyjna metoda, ktora probuje znaleLsc wolne miejsce dla bloku o danym `index`. JeLli nie ma wolnych blokow tego rozmiaru, probuje znaleLsc i podzielic wiekszy blok (o `index + 1`).
## `std::string Atlas::getStats()`

Zwraca informacje debugowania o liczbie wolnych miejsc w poszczegolnych blokach atlasu.
## ZaleLLnoLci i powiazania

-   `framework/graphics/atlas.h`: Plik nagL'owkowy.
-   `framework/graphics/framebuffermanager.h`: ULLywa `FrameBufferManager` do tworzenia `FrameBuffer` dla atlasow.
-   `framework/graphics/painter.h`: ULLywa `Painter` do rysowania w atlasie.
-   `framework/graphics/graphics.h`: Do pobierania maksymalnego rozmiaru tekstury.
-   Jest uLLywany przez `DrawQueue` i `DrawCache` do optymalizacji renderowania.

---
# z"" bitmapfont.cpp
## Opis ogolny

Plik `bitmapfont.cpp` zawiera implementacje klasy `BitmapFont`, ktora zarzadza fontami opartymi na bitmapach (obrazach). Taki font skL'ada sie z pojedynczej tekstury zawierajacej wszystkie glify (znaki) uL'oLLone w siatce.
## Klasa `BitmapFont`
## `void BitmapFont::load(const OTMLNodePtr& fontNode)`
## Opis semantyczny
Laduje definicje fontu z wezL'a OTML (zazwyczaj z pliku `.otfont`).
## DziaL'anie
1.  Odczytuje z wezL'a OTML podstawowe atrybuty fontu:
    -   `texture`: LscieLLka do pliku z obrazem fontu.
    -   `glyph-size`: Rozmiar pojedynczego glifu w siatce.
    -   `height`: Rzeczywista wysokoLc glifu.
    -   `y-offset`: Przesuniecie w osi Y.
    -   `first-glyph`: Kod ASCII pierwszego znaku w siatce (zwykle 32 - spacja).
    -   `spacing`: Odstepy miedzy glifami.
2.  Oblicza szerokoLci poszczegolnych glifow:
    -   JeLli zdefiniowano `fixed-glyph-width`, wszystkie glify maja te sama szerokoLc.
    -   W przeciwnym razie wywoL'uje `calculateGlyphsWidthsAutomatically`, aby automatycznie wykryc szerokoLc kaLLdego znaku.
3.  Ustawia specjalne szerokoLci dla spacji (32) i znaku nowej linii (`\n`).
4.  Laduje teksture fontu za pomoca `g_textures.getTexture()`.
5.  JeLli fonty sa cachowane w atlasie (`!DONT_CACHE_FONTS`), wywoL'uje `g_atlas.cacheFont()` i ustawia teksture atlasu jako LsrodL'owa.
6.  Oblicza i zapisuje wspoL'rzedne tekstury dla kaLLdego glifu w `m_glyphsTextureCoords`.
## `void BitmapFont::drawText(...)`

Metody te nie rysuja tekstu bezpoLrednio, lecz dodaja zadanie rysowania do globalnej kolejki `g_drawQueue`.

-   **`drawText(..., const Color& color, ...)`**: Dodaje zadanie rysowania tekstu jednokolorowego.
-   **`drawColoredText(..., const std::vector<std::pair<int, Color>>& colors, ...)`**: Dodaje zadanie rysowania tekstu z wieloma kolorami.
## `void BitmapFont::calculateDrawTextCoords(...)`

Oblicza wspoL'rzedne ekranowe i tekstury dla kaLLdego glifu w podanym tekLcie, uwzgledniajac wyrownanie i przycinanie do podanego prostokata. Wyniki sa zapisywane w `CoordsBuffer`.
## `const std::vector<Point>& BitmapFont::calculateGlyphsPositions(...)`

Oblicza pozycje (lewy gorny rog) kaLLdego glifu w tekLcie, uwzgledniajad wyrownanie. ULLywa statycznych, lokalnych dla watku wektorow w celu optymalizacji. Zwraca rownieLL obliczony rozmiar caL'ego bloku tekstu.
## `Size BitmapFont::calculateTextRectSize(const std::string& text)`

Zwraca rozmiar prostokata, jaki zajmie podany tekst, uLLywajac `calculateGlyphsPositions`.
## `std::string BitmapFont::wrapText(...)`

Implementuje zawijanie tekstu. Dzieli tekst na linie, tak aby LLadna nie przekraczaL'a `maxWidth`. ObsL'uguje rownieLL przenoszenie definicji kolorow (`m_textColors`) do nowych linii.
## `void BitmapFont::calculateGlyphsWidthsAutomatically(...)`

Prywatna metoda, ktora analizuje obraz tekstury fontu piksel po pikselu. Dla kaLLdego glifu znajduje ostatnia nieprzezroczysta kolumne pikseli, aby precyzyjnie okreLlic jego szerokoLc.
## ZaleLLnoLci i powiazania

-   `framework/graphics/atlas.h`: ULLywa `g_atlas` do cachowania tekstur fontow.
-   `framework/graphics/bitmapfont.h`: Plik nagL'owkowy.
-   `framework/graphics/texturemanager.h`: ULLywa `g_textures` do L'adowania obrazu fontu.
-   `framework/graphics/image.h`: ULLywa `Image` do analizy pikseli w `calculateGlyphsWidthsAutomatically`.
-   `framework/graphics/drawqueue.h`: Dodaje zadania rysowania tekstu do `g_drawQueue`.
-   Jest zarzadzana przez `FontManager`.

---
# z"" atlas.h
## Opis ogolny

Plik `atlas.h` deklaruje interfejs klasy `Atlas`, ktora implementuje mechanizm atlasu tekstur. Celem atlasu jest optymalizacja renderowania poprzez grupowanie wielu maL'ych tekstur w jedna duLLa teksture, co redukuje liczbe wywoL'aL" `glBindTexture` w OpenGL.
## Klasa `Atlas`
## Opis semantyczny
`Atlas` zarzadza jednym lub kilkoma duLLymi obiektami `FrameBuffer`, ktore dziaL'aja jak "pL'otna". Kiedy system renderujacy potrzebuje narysowac maL'a teksture, `Atlas` znajduje dla niej wolne miejsce w jednym z pL'ocien, kopiuje tam jej zawartoLc (jeLli jeszcze jej tam nie ma) i zwraca wspoL'rzedne wewnatrz atlasu. PoLsniejsze odwoL'ania do tej samej tekstury uLLywaja juLL skopiowanej wersji z atlasu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje atlas, tworzac `FrameBuffer` o maksymalnym moLLliwym rozmiarze. |
| `void terminate()` | Zwalnia zasoby atlasu. |
| `void reload()` | Resetuje i czyLci zawartoLc atlasow. |
| `Point cache(uint64_t hash, const Size& size, bool& draw)` | GL'owna metoda cachujaca. Sprawdza, czy tekstura o danym hashu jest juLL w atlasie. JeLli nie, znajduje wolne miejsce i zwraca jego koordynaty. Parametr `draw` jest ustawiany na `true`, jeLli teksture trzeba narysowac w atlasie. |
| `Point cacheFont(const TexturePtr& fontTexture)` | Specjalna metoda do cachowania tekstur fontow w dedykowanym atlasie. |
| `TexturePtr get(int location)` | Zwraca wskaLsnik na teksture atlasu o danym indeksie (0 - gL'owny, 1 - fonty). |
| `void bind()` | Bindowanie `FrameBuffer` atlasu jako celu renderowania. |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `std::string getStats()` | Zwraca informacje diagnostyczne o stanie atlasu. |
## Zmienne prywatne

-   `m_atlas[2]`: Tablica wskaLsnikow na `FrameBuffer` (dla ogolnych tekstur i fontow).
-   `m_cache`: Mapa (`std::map`) przechowujaca hashe skachowanych tekstur i ich pozycje w atlasie.
-   `m_locations[2][7]`: Tablica list przechowujaca pozycje wolnych blokow o roLLnych rozmiarach (od 32x32 do 2048x2048) dla obu atlasow.
-   `m_size`: Rozmiar boku tekstury atlasu.
-   `m_doReset`: Flaga sygnalizujaca koniecznoLc zresetowania atlasu (gdy zabraknie miejsca).
## Zmienne globalne

-   `g_atlas`: Globalna instancja `Atlas`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/drawqueue.h`: Potencjalnie uLLywany, ale gL'ownie to `DrawQueue` uLLywa `Atlas`.
-   `framework/graphics/framebuffer.h`: ULLywa `FrameBuffer` jako "pL'otna" dla atlasu.
-   ULLywany przez system renderowania (`DrawQueue`, `DrawCache`) do optymalizacji rysowania.
-   `FontManager` uLLywa go do cachowania tekstur fontow.

---
# z"" bitmapfont.h
## Opis ogolny

Plik `bitmapfont.h` deklaruje klase `BitmapFont`, ktora reprezentuje font oparty na bitmapie. Jest to kluczowy element systemu renderowania tekstu w aplikacji.
## Klasa `BitmapFont`
## Opis semantyczny
`BitmapFont` zarzadza pojedynczym fontem, ktory jest zdefiniowany jako obraz (tekstura) zawierajacy siatke znakow (glifow). Klasa przechowuje informacje o rozmiarze glifow, ich pozycjach na teksturze oraz szerokoLciach poszczegolnych znakow. Dostarcza metody do rysowania tekstu (ktore w rzeczywistoLci deleguja zadanie do `DrawQueue`) oraz do obliczania wymiarow i zawijania tekstu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BitmapFont(const std::string& name)` | Konstruktor, ustawia nazwe fontu i unikalne ID. |
| `void load(const OTMLNodePtr& fontNode)` | Laduje definicje fontu z wezL'a OTML. |
| `void drawText(...)` | Dodaje do kolejki renderowania zadanie narysowania tekstu. |
| `void drawColoredText(...)` | Dodaje zadanie narysowania tekstu z wieloma kolorami. |
| `void calculateDrawTextCoords(...)` | Oblicza wspoL'rzedne wierzchoL'kow i tekstur dla renderowanego tekstu. |
| `const std::vector<Point>& calculateGlyphsPositions(...)` | Oblicza pozycje poszczegolnych glifow w tekLcie. |
| `Size calculateTextRectSize(...)` | Oblicza rozmiar prostokata zajmowanego przez tekst. |
| `std::string wrapText(...)` | ZL'amuje tekst na wiele linii, aby zmieLciL' sie w podanej szerokoLci. |
| `int getId()` | Zwraca unikalne ID fontu. |
| `std::string getName()` | Zwraca nazwe fontu. |
| `int getGlyphHeight()` | Zwraca wysokoLc glifow. |
| `const Rect* getGlyphsTextureCoords()` | Zwraca tablice wspoL'rzednych tekstur dla wszystkich glifow. |
| `const Size* getGlyphsSize()` | Zwraca tablice rozmiarow dla wszystkich glifow. |
| `const TexturePtr& getTexture()` | Zwraca teksture fontu (moLLe to byc tekstura atlasu). |
| `int getYOffset()` | Zwraca przesuniecie Y. |
| `Size getGlyphSpacing()` | Zwraca odstepy miedzy glifami. |
## Zmienne prywatne

-   `m_name`: Nazwa fontu.
-   `m_glyphHeight`: WysokoLc glifu.
-   `m_firstGlyph`: Kod ASCII pierwszego znaku.
-   `m_yOffset`: Przesuniecie w osi Y.
-   `m_id`: Unikalne ID fontu.
-   `m_glyphSpacing`: Odstepy miedzy glifami.
-   `m_texture`: WskaLsnik na teksture fontu.
-   `m_glyphsTextureCoords[256]`: Tablica wspoL'rzednych tekstur dla kaLLdego glifu.
-   `m_glyphsSize[256]`: Tablica rozmiarow dla kaLLdego glifu.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Deklaracje typow graficznych.
-   `framework/graphics/texture.h`: ULLywa `Texture` do przechowywania obrazu fontu.
-   `framework/otml/declarations.h`: ULLywa `OTMLNodePtr` w metodzie `load`.
-   `framework/graphics/coordsbuffer.h`: ULLywa `CoordsBuffer` do przechowywania geometrii tekstu.
-   Jest zarzadzana przez `FontManager`.
-   Jest uLLywana przez `UIWidget` i inne komponenty do renderowania tekstu.

---
# z"" cachedtext.cpp
## Opis ogolny

Plik `cachedtext.cpp` zawiera implementacje klasy `CachedText`, ktora sL'uLLy do optymalizacji renderowania tekstu, ktory nie zmienia sie czesto.
## Klasa `CachedText`
## `CachedText::CachedText()`

Konstruktor. Inicjalizuje domyLlny font, wyrownanie do Lrodka (`Fw::AlignCenter`) i inne wartoLci domyLlne.
## `void CachedText::draw(const Rect& rect, const Color& color)`
## Opis semantyczny
GL'owna metoda rysujaca. Renderuje tekst w podanym prostokacie z danym kolorem.
## DziaL'anie
1.  Sprawdza, czy font jest ustawiony.
2.  Sprawdza, czy tekst musi zostac "przekeshowany" (`m_textMustRecache`) lub czy zmieniL' sie prostokat docelowy (`m_textCachedScreenCoords`). JeLli tak, aktualizuje buforowane koordynaty.
3.  WywoL'uje metode `m_font->drawText()` lub `m_font->drawColoredText()` w celu dodania zadania rysowania do `DrawQueue`.

> NOTE: Nazwa "cached" moLLe byc nieco mylaca. Klasa nie renderuje tekstu do tekstury. Zamiast tego, "keszuje" obliczenia zwiazane z pozycjonowaniem glifow, ale samo rysowanie odbywa sie dynamicznie w kaLLdej klatce za pomoca `BitmapFont::drawText`.
## `void CachedText::setColoredText(const std::vector<std::string>& texts)`

Ustawia tekst skL'adajacy sie z fragmentow o roLLnych kolorach. Parsuje wektor, tworzac wewnetrzna reprezentacje `m_text` i `m_textColors`, a nastepnie wywoL'uje `update()`.
## `void CachedText::update()`

Prywatna metoda pomocnicza. Oblicza rozmiar tekstu za pomoca `m_font->calculateTextRectSize()` i ustawia flage `m_textMustRecache` na `true`, co wymusza przeliczenie geometrii przy nastepnym wywoL'aniu `draw()`.
## `void CachedText::wrapText(int maxWidth)`

Zawija tekst, aby zmieLciL' sie w podanej szerokoLci, uLLywajac metody `m_font->wrapText()`, a nastepnie wywoL'uje `update()`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/cachedtext.h`: Plik nagL'owkowy.
-   `framework/graphics/painter.h`: PoLrednio, poprzez `BitmapFont`.
-   `framework/graphics/fontmanager.h`: ULLywa `g_fonts` do pobrania domyLlnego fontu.
-   `framework/graphics/bitmapfont.h`: Kluczowa zaleLLnoLc; uLLywa `BitmapFont` do wszystkich operacji na tekLcie.

---
# z"" colorarray.h
## Opis ogolny

Plik `colorarray.h` deklaruje klase `ColorArray`, ktora jest prostym kontenerem na tablice kolorow w formacie `float`. Jest uLLywana do przekazywania kolorow dla poszczegolnych wierzchoL'kow do systemu renderujacego.
## Klasa `ColorArray`
## Opis semantyczny
`ColorArray` dziaL'a jako bufor dla kolorow. KaLLdy kolor jest reprezentowany przez cztery wartoLci `float` (R, G, B, A) w zakresie od 0.0 do 1.0. Klasa udostepnia metody do dodawania kolorow i dostepu do surowego wskaLsnika na dane, co jest potrzebne do przekazania ich do OpenGL.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addColor(float r, float g, float b, float a)` | Dodaje kolor do bufora, podajac skL'adowe jako `float`. |
| `void addColor(const Color& c)` | Dodaje kolor do bufora, pobierajac skL'adowe z obiektu `Color`. |
| `void clear()` | CzyLci bufor. |
| `float *colors() const` | Zwraca wskaLsnik na poczatek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaLsnik na surowe dane bufora. |
| `int colorCount() const` | Zwraca liczbe peL'nych kolorow w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbe kolorow. |
| `int size() const` | Zwraca caL'kowita liczbe wartoLci `float` w buforze (tj. `colorCount() * 4`). |
## Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, ktory przechowuje dane kolorow.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: ULLywa `DataBuffer` jako wewnetrznego kontenera.
-   Jest uLLywana przez `Painter` do przekazywania tablicy kolorow do shadera, co pozwala na rysowanie gradientow lub wielokolorowych ksztaL'tow.

---
# z"" cachedtext.h
## Opis ogolny

Plik `cachedtext.h` deklaruje klase `CachedText`, ktora jest opakowaniem (wrapperem) uL'atwiajacym zarzadzanie i renderowanie tekstu, ktory moLLe byc keszowany.
## Klasa `CachedText`
## Opis semantyczny
Klasa `CachedText` przechowuje tekst, font, wyrownanie i inne wL'aLciwoLci. Jej gL'ownym celem jest optymalizacja renderowania poprzez unikanie ponownych obliczeL" geometrii tekstu w kaLLdej klatce. Kiedy tekst lub jego parametry sie zmieniaja, metoda `update()` jest wywoL'ywana, aby przeliczyc rozmiar i ustawic flage koniecznoLci ponownego buforowania wspoL'rzednych.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CachedText()` | Konstruktor. |
| `void draw(const Rect& rect, const Color& color)` | Rysuje skeszowany tekst w podanym prostokacie. |
| `void wrapText(int maxWidth)` | Zawija tekst do podanej szerokoLci. |
| `void setFont(...)` | Ustawia font i aktualizuje tekst. |
| `void setText(...)` | Ustawia tekst i aktualizuje go. |
| `void setColoredText(...)` | Ustawia tekst skL'adajacy sie z fragmentow o roLLnych kolorach. |
| `void setAlign(...)` | Ustawia wyrownanie tekstu. |
| `Size getTextSize()` | Zwraca obliczony rozmiar tekstu. |
| `std::string getText() const` | Zwraca przechowywany tekst. |
| `BitmapFontPtr getFont() const` | Zwraca uLLywany font. |
| `Fw::AlignmentFlag getAlign() const` | Zwraca wyrownanie. |
| `bool hasText()` | Zwraca `true`, jeLli tekst nie jest pusty. |
## Zmienne prywatne

-   `m_text`: GL'owny, niezmieniony tekst.
-   `m_textColors`: Wektor par przechowujacy pozycje i kolory dla tekstu wielokolorowego.
-   `m_textSize`: Obliczony rozmiar tekstu.
-   `m_textMustRecache`: Flaga wskazujaca, LLe geometria tekstu musi zostac przeliczona.
-   `m_textCachedScreenCoords`: Ostatni prostokat, w ktorym tekst byL' rysowany.
-   `m_font`: ULLywany `BitmapFont`.
-   `m_align`: Wyrownanie tekstu.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/coordsbuffer.h`: PoLrednio, przez `BitmapFont`.
-   `framework/graphics/drawqueue.h`: PoLrednio, przez `BitmapFont`.
-   Klasa ta jest prawdopodobnie uLLywana w komponentach UI, ktore wyLwietlaja tekst, aby uproLcic i zoptymalizowac jego renderowanie.

---
# z"" coordsbuffer.h
## Opis ogolny

Plik `coordsbuffer.h` deklaruje klase `CoordsBuffer`, ktora jest specjalizowanym kontenerem do przechowywania wspoL'rzednych wierzchoL'kow (`vertex`) i tekstur (`texture coord`). Jest to kluczowy element optymalizacyjny, pozwalajacy na grupowanie geometrii wielu obiektow i rysowanie ich w jednym wywoL'aniu (batching).
## Klasa `CoordsBuffer`
## Opis semantyczny
`CoordsBuffer` przechowuje dwie tablice wierzchoL'kow (`VertexArray`): jedna dla pozycji na ekranie i druga dla pozycji na teksturze. Dostarcza metody do dodawania prostych prymitywow geometrycznych (trojkaty, prostokaty). Posiada mechanizm "keszowania" danych w sprzetowym buforze VBO (Vertex Buffer Object) w celu dalszej optymalizacji.

> **NOTE**: Mimo nazwy, `CoordsBuffer` jest jednorazowego uLLytku dla `DrawQueue`. Po przekazaniu do kolejki, jego zawartoLc jest przenoszona (`std::move`), a oryginaL' staje sie pusty. To zachowanie jest wymuszone przez usuniecie konstruktora kopiujacego i operatora przypisania, a zdefiniowanie konstruktora przenoszacego.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CoordsBuffer()` | Konstruktor, tworzy wewnetrzne obiekty `VertexArray`. |
| `~CoordsBuffer()` | Destruktor. |
| `CoordsBuffer(CoordsBuffer&& c)` | Konstruktor przenoszacy. |
| `void clear()` | CzyLci oba bufory wierzchoL'kow. |
| `void addTriangle(...)` | Dodaje trojkat (tylko wspoL'rzedne wierzchoL'kow). |
| `void addRect(const Rect& dest)` | Dodaje prostokat (tylko wspoL'rzedne wierzchoL'kow). |
| `void addRect(const Rect& dest, const Rect& src)` | Dodaje prostokat z tekstura. |
| `void addQuad(...)`, `addUpsideDownQuad(...)` | Dodaje czworokat (quad) - przydatne do renderowania w trybie `TriangleStrip`. |
| `void addBoudingRect(...)` | Dodaje geometrie ramki o okreLlonej gruboLci. |
| `void addRepeatedRects(...)` | WypeL'nia prostokat docelowy powtarzajaca sie tekstura. |
| `float *getVertexArray()` | Zwraca wskaLsnik na dane wierzchoL'kow. |
| `float *getTextureCoordArray()` | Zwraca wskaLsnik na dane wspoL'rzednych tekstury. |
| `int getVertexCount()` | Zwraca liczbe wierzchoL'kow. |
| `HardwareBuffer* getVertexHardwareCache()` | Zwraca wskaLsnik na sprzetowy bufor VBO dla wierzchoL'kow (jeLli istnieje). |
| `void cache()` | Tworzy i wypeL'nia sprzetowe bufory VBO na podstawie bieLLacych danych. |
| `Rect getTextureRect()`| Oblicza i zwraca prostokat ograniczajacy wszystkie wspoL'rzedne tekstury. |
## Zmienne prywatne

-   `m_locked`: Flaga uLLywana do optymalizacji (zapobiega niepotrzebnemu kopiowaniu danych).
-   `m_vertexArray`: WskaLsnik na `VertexArray` przechowujacy pozycje.
-   `m_textureCoordArray`: WskaLsnik na `VertexArray` przechowujacy wspoL'rzedne tekstury.
## ZaleLLnoLci i powiazania

-   `framework/graphics/vertexarray.h`: ULLywa `VertexArray` jako podstawowego kontenera na dane.
-   Jest intensywnie uLLywana przez `UIWidget` i jego podklasy do generowania geometrii, ktora nastepnie jest przekazywana do `DrawQueue` w celu renderowania.

---
# z"" deptharray.h
## Opis ogolny

Plik `deptharray.h` deklaruje klase `DepthArray`, ktora jest prostym kontenerem na tablice wartoLci gL'ebokoLci (depth) w formacie `float`. Jest to prawdopodobnie czeLc eksperymentalnego lub nie w peL'ni zaimplementowanego mechanizmu renderowania 3D lub sortowania gL'ebokoLci.
## Klasa `DepthArray`
## Opis semantyczny
`DepthArray` dziaL'a jako bufor dla wartoLci gL'ebokoLci (wspoL'rzedna Z). KaLLda wartoLc `float` w buforze odpowiada jednemu wierzchoL'kowi. Klasa udostepnia metody do dodawania wartoLci i dostepu do surowego wskaLsnika na dane, co jest potrzebne do przekazania ich do OpenGL jako atrybut wierzchoL'ka.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addDepth(float depth)` | Dodaje nowa wartoLc gL'ebokoLci do bufora. |
| `void clear()` | CzyLci bufor. |
| `float *depths() const` | Zwraca wskaLsnik na poczatek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaLsnik na surowe dane bufora. |
| `int depthCount() const` | Zwraca liczbe wartoLci w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbe wartoLci. |
| `int size() const` | Zwraca liczbe wartoLci. |
## Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, ktory przechowuje dane gL'ebokoLci.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: ULLywa `DataBuffer` jako wewnetrznego kontenera.
-   W obecnym kodzie jest uLLywana w `Painter`, ale funkcjonalnoLc zwiazana z buforem gL'ebi jest wykomentowana lub nie w peL'ni zaimplementowana (`WITH_DEPTH_BUFFER`).

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `graphics` sL'uLLy jako centralny punkt dla wczesnych deklaracji (forward declarations) i definicji typow (`typedef`) zwiazanych z systemem graficznym. Jego gL'ownym celem jest unikanie zaleLLnoLci cyklicznych miedzy plikami nagL'owkowymi i minimalizowanie liczby doL'aczanych plikow.
## Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastepujacych klas, co pozwala na uLLywanie wskaLsnikow i referencji do nich bez potrzeby doL'aczania ich peL'nych definicji:

-   `Texture`
-   `TextureManager`
-   `Image`
-   `AnimatedTexture`
-   `BitmapFont`
-   `CachedText`
-   `FrameBuffer`
-   `FrameBufferManager`
-   `Shader`
-   `ShaderProgram`
-   `PainterShaderProgram`
## Definicje typow (Typedefs)

Plik definiuje aliasy dla inteligentnych wskaLsnikow (`shared_object_ptr`) do klas graficznych, co uL'atwia ich uLLycie i poprawia czytelnoLc kodu.

-   `ImagePtr`: `stdext::shared_object_ptr<Image>`
-   `TexturePtr`: `stdext::shared_object_ptr<Texture>`
-   `AnimatedTexturePtr`: `stdext::shared_object_ptr<AnimatedTexture>`
-   `BitmapFontPtr`: `stdext::shared_object_ptr<BitmapFont>`
-   `CachedTextPtr`: `stdext::shared_object_ptr<CachedText>`
-   `FrameBufferPtr`: `stdext::shared_object_ptr<FrameBuffer>`
-   `ShaderPtr`: `stdext::shared_object_ptr<Shader>`
-   `ShaderProgramPtr`: `stdext::shared_object_ptr<ShaderProgram>`
-   `PainterShaderProgramPtr`: `stdext::shared_object_ptr<PainterShaderProgram>`
-   `ShaderList`: `std::vector<ShaderPtr>`
## ZaleLLnoLci i powiazania

-   `framework/global.h`: DoL'acza podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   `framework/graphics/glutil.h`: DoL'acza nagL'owki OpenGL/GLES.
-   Ten plik jest intensywnie uLLywany w caL'ym module graficznym i w innych moduL'ach, ktore wchodza w interakcje z grafika (np. `UI`).

---
# z"" coordsbuffer.cpp
## Opis ogolny

Plik `coordsbuffer.cpp` zawiera implementacje metod klasy `CoordsBuffer`, ktora jest buforem na dane geometryczne do renderowania.
## Klasa `CoordsBuffer`
## `CoordsBuffer::CoordsBuffer()`

Konstruktor. Inicjalizuje dwa wewnetrzne bufory: `m_vertexArray` (dla wspoL'rzednych pozycji) i `m_textureCoordArray` (dla wspoL'rzednych tekstury).
## `void CoordsBuffer::addBoudingRect(const Rect& dest, int innerLineWidth)`

Dodaje geometrie czterech prostokatow, ktore razem tworza ramke (border) wewnatrz podanego prostokata `dest` o gruboLci `innerLineWidth`.
## `void CoordsBuffer::addRepeatedRects(const Rect& dest, const Rect& src)`

WypeL'nia prostokat docelowy (`dest`) powtarzajacym sie wzorem z tekstury (`src`). Dzieli obszar `dest` na mniejsze prostokaty o rozmiarze `src` i dodaje je do bufora, odpowiednio przycinajac wspoL'rzedne tekstury na krawedziach.
## `void CoordsBuffer::unlock(bool clear)`

Metoda zwiazana z wewnetrznym mechanizmem "blokowania" bufora. Kiedy bufor jest zablokowany (`m_locked`), kaLLda operacja dodawania geometrii powoduje jego odblokowanie. Odblokowanie tworzy kopie wewnetrznych `VertexArray`, aby zapobiec modyfikacji danych, ktore mogL'y juLL zostac przesL'ane do VBO. JeLli `clear` jest `true`, zamiast kopiowania tworzone sa nowe, puste `VertexArray`.
## `Rect CoordsBuffer::getTextureRect()`

Przechodzi przez wszystkie wspoL'rzedne tekstury w buforze, aby znaleLsc minimalny i maksymalny punkt, a nastepnie zwraca prostokat ograniczajacy (bounding box) dla uLLywanego fragmentu tekstury.
## ZaleLLnoLci i powiazania

-   `framework/graphics/coordsbuffer.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Potencjalnie do funkcji zwiazanych z grafika.
-   Jest uLLywana do budowania geometrii przez klasy takie jak `UIWidget`, a nastepnie konsumowana przez `DrawQueue` i `Painter` do renderowania.

---
# z"" drawcache.cpp
## Opis ogolny

Plik `drawcache.cpp` implementuje klase `DrawCache`, ktora jest kluczowym elementem systemu optymalizacji renderowania. Jej zadaniem jest grupowanie (batching) operacji rysowania, ktore uLLywaja tej samej tekstury (atlasu), aby zminimalizowac liczbe wywoL'aL" rysujacych (draw calls) do OpenGL.
## Zmienne globalne
## `g_drawCache`

Globalna instancja `DrawCache`, uLLywana przez `DrawQueue` do buforowania operacji.

DrawCache g_drawCache;
```
## Klasa `DrawCache`
## `void DrawCache::draw()`
## Opis semantyczny
Wykonuje zgrupowane operacje rysowania.
## DziaL'anie
1.  Upewnia sie, LLe atlas tekstur jest odL'aczony (`release()`).
2.  JeLli bufor nie jest pusty (`m_size > 0`), wywoL'uje `g_painter->drawCache()`, przekazujac jej wszystkie zebrane dane wierzchoL'kow, wspoL'rzednych tekstur i kolorow.
3.  Resetuje licznik `m_size` do zera.
## `void DrawCache::bind()` i `void DrawCache::release()`

Metody te zarzadzaja bindowaniem i zwalnianiem `FrameBuffer` atlasu. `bind()` jest wywoL'ywane, gdy do atlasu musi zostac narysowana nowa tekstura. `release()` jest wywoL'ywane przed wykonaniem `draw()`.
## Metody dodawania do bufora

-   **`addRect(const Rect& dest, const Color& color)`**: Dodaje prostokat wypeL'niony jednolitym kolorem. WspoL'rzedne tekstury sa ustawiane na `(-10, -10)`, co jest sygnaL'em dla shadera, aby nie uLLywaL' tekstury.
-   **`addTexturedRect(const Rect& dest, const Rect& src, const Color& color)`**: Dodaje teksturowany prostokat.
-   **`addCoords(CoordsBuffer& coords, const Color& color)`**: Dodaje geometrie z `CoordsBuffer` (bez tekstury).
-   **`addTexturedCoords(CoordsBuffer& coords, const Point& offset, const Color& color)`**: Dodaje geometrie z `CoordsBuffer` z tekstura. Przesuwa wspoL'rzedne tekstury o podany `offset`, ktory jest pozycja tekstury w atlasie.
## Metody pomocnicze (`addRectRaw`, `addColorRaw`)

Prywatne metody `inline` do szybkiego zapisu danych do wewnetrznych wektorow (`m_destCoord`, `m_srcCoord`, `m_color`).
## ZaleLLnoLci i powiazania

-   `framework/graphics/drawcache.h`: Plik nagL'owkowy.
-   `framework/graphics/atlas.h`: LsciLle wspoL'pracuje z `g_atlas` w celu bindowania i zwalniania bufora ramki atlasu.
-   `framework/graphics/painter.h`: WywoL'uje `g_painter->drawCache()` do finalnego narysowania zgrupowanej geometrii.
-   Jest uLLywana przez `DrawQueueItem`, aby sprobowac zbuforowac operacje rysowania zamiast wykonywac ja natychmiast.

---
# z"" drawcache.h
## Opis ogolny

Plik `drawcache.h` deklaruje klase `DrawCache`, ktora sL'uLLy jako bufor dla operacji rysowania. Jest to mechanizm optymalizacyjny, ktory agreguje wiele maL'ych operacji rysowania (np. prostokatow) w jedno duLLe wywoL'anie, co znaczaco poprawia wydajnoLc renderowania.
## Klasa `DrawCache`
## Opis semantyczny
`DrawCache` przechowuje trzy duLLe, prealokowane wektory: na wspoL'rzedne wierzchoL'kow (`m_destCoord`), wspoL'rzedne tekstur (`m_srcCoord`) i kolory (`m_color`). Metody `add...` dodaja dane do tych buforow. Gdy bufor jest peL'ny lub gdy operacja rysowania nie moLLe byc zbuforowana, metoda `draw()` jest wywoL'ywana, aby oproLLnic bufor i narysowac jego zawartoLc za pomoca jednego wywoL'ania `g_painter->drawCache()`.
## StaL'e

-   `MAX_SIZE`: Maksymalna liczba wierzchoL'kow, jaka moLLe przechowac bufor (65536).
-   `HALF_MAX_SIZE`: PoL'owa maksymalnego rozmiaru, uLLywana jako prog do oproLLnienia bufora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw()` | Rysuje zawartoLc bufora na ekranie i go czyLci. |
| `void bind()` | Bindowanie `FrameBuffer` atlasu (gdy trzeba do niego coL dorysowac). |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `bool hasSpace(int size)` | Sprawdza, czy w buforze jest wystarczajaco miejsca na `size` wierzchoL'kow. |
| `inline int getSize()` | Zwraca aktualna liczbe wierzchoL'kow w buforze. |
| `void addRect(...)` | Dodaje prostokat wypeL'niony kolorem. |
| `void addTexturedRect(...)` | Dodaje teksturowany prostokat. |
| `void addCoords(...)` | Dodaje geometrie z `CoordsBuffer` (bez tekstury). |
| `void addTexturedCoords(...)` | Dodaje geometrie z `CoordsBuffer` (z tekstura). |
## Zmienne prywatne

-   `m_destCoord`: Wektor na wspoL'rzedne docelowe (pozycji).
-   `m_srcCoord`: Wektor na wspoL'rzedne LsrodL'owe (tekstury).
-   `m_color`: Wektor na kolory wierzchoL'kow.
-   `m_bound`: Flaga wskazujaca, czy atlas jest zbindowany.
-   `m_size`: Aktualna liczba wierzchoL'kow w buforze.
## Zmienne globalne

-   `g_drawCache`: Globalna instancja `DrawCache`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/atlas.h`: Do zarzadzania atlasem tekstur.
-   `framework/graphics/coordsbuffer.h`: Do przyjmowania geometrii.
-   `framework/graphics/graphics.h`, `painter.h`: Do operacji renderowania.
-   Jest uLLywana przez `DrawQueue`, aby grupowac operacje rysowania.

---
# z"" drawqueue.cpp
## Opis ogolny

Plik `drawqueue.cpp` implementuje logike dla `DrawQueue` oraz poszczegolnych typow zadaL" rysowania (`DrawQueueItem`). Jest to centralny element systemu renderowania, ktory kolekcjonuje wszystkie operacje rysowania w jednej klatce, a nastepnie wykonuje je w odpowiedniej kolejnoLci, z uwzglednieniem warunkow takich jak przycinanie, przezroczystoLc czy rotacja.
## Zmienne globalne
## `g_drawQueue`

Globalny wskaLsnik na aktualnie aktywna kolejke rysowania. Watek logiki tworzy nowe instancje `DrawQueue`, wypeL'nia je i przypisuje do tego wskaLsnika, a watek renderowania je konsumuje.
## Klasy `DrawQueueItem` (implementacje)

KaLLda klasa dziedziczaca po `DrawQueueItem` implementuje dwie kluczowe metody:

-   **`draw()`**: Wykonuje faktyczna operacje rysowania za pomoca `g_painter`.
-   **`cache()`**: Probuje zoptymalizowac operacje, dodajac ja do `g_drawCache` zamiast rysowac natychmiast. Zwraca `true`, jeLli keszowanie sie powiodL'o.
## PrzykL'ady implementacji:

-   **`DrawQueueItemTextureCoords::cache()`**:
    1.  Sprawdza, czy tekstura moLLe byc skeszowana.
    2.  Pobiera pozycje dla tekstury w atlasie za pomoca `g_atlas.cache()`.
    3.  JeLli tekstury nie byL'o w atlasie (`drawNow == true`), rysuje ja do atlasu.
    4.  JeLli w `g_drawCache` jest miejsce, dodaje do niego geometrie z przesunietymi wspoL'rzednymi tekstury.

-   **`DrawQueueItemFilledRect::cache()`**:
    1.  Sprawdza, czy jest miejsce w `g_drawCache`.
    2.  JeLli tak, dodaje prostokat za pomoca `g_drawCache.addRect()`.

-   **`DrawQueueItemText::draw()`**: WywoL'uje `g_text.drawText()`, ktora jest zoptymalizowana do renderowania tekstu.

-   **`DrawQueueCondition...::start()` i `end()`**: Implementuja zmiany stanu `g_painter` na poczatku i na koL"cu bloku warunkowego. Na przykL'ad `DrawQueueConditionClip` zmienia i przywraca prostokat przycinania.
## Klasa `DrawQueue`
## `void DrawQueue::setFrameBuffer(...)`

Konfiguruje `DrawQueue` do renderowania do bufora ramki (off-screen). Ustawia docelowy i LsrodL'owy prostokat oraz oblicza skalowanie, jeLli rozmiar bufora przekracza `2048x2048`.
## `void DrawQueue::addText(...)` i `void DrawQueue::addColoredText(...)`

Tworza zadanie rysowania tekstu. Najpierw dodaja tekst do `g_text` (systemu keszujacego geometrie tekstu), uzyskujac hash, a nastepnie tworza odpowiedni `DrawQueueItemText`.
## `void DrawQueue::correctOutfit(...)`

Specjalna metoda do skalowania i pozycjonowania wielu `DrawQueueItem` (czeLci stroju postaci), tak aby caL'oLc zmieLciL'a sie w podanym prostokacie docelowym, zachowujac proporcje.
## `void DrawQueue::draw(DrawType drawType)`
## Opis semantyczny
GL'owna metoda wykonujaca wszystkie zebrane zadania rysowania.
## DziaL'anie
1.  OkreLla zakres zadaL" do narysowania na podstawie `drawType` (wszystkie, przed mapa, po mapie).
2.  Sortuje warunki (`m_conditions`) po ich pozycjach poczatkowych.
3.  JeLli ustawiono skalowanie, modyfikuje macierz projekcji `g_painter`.
4.  Iteruje po zadaniach w kolejce (`m_queue`):
    -   Przed kaLLdym zadaniem, aktywuje i dezaktywuje odpowiednie warunki (`start()`/`end()`).
    -   Probuje skeszowac zadanie za pomoca `item->cache()`.
    -   JeLli keszowanie sie nie powiedzie, oproLLnia `g_drawCache` i probuje ponownie.
    -   JeLli ponowne keszowanie sie nie powiedzie, wykonuje `item->draw()`.
    -   Regularnie oproLLnia `g_drawCache`, gdy osiagnie poL'owe pojemnoLci.
5.  Po zakoL"czeniu petli, oproLLnia `g_drawCache` i deaktywuje wszystkie pozostaL'e warunki.
6.  Przywraca oryginalna macierz projekcji i stan `g_painter`.
## ZaleLLnoLci i powiazania

-   LsciLle wspoL'pracuje z `g_painter`, `g_atlas`, `g_drawCache` i `g_text`, orkiestrujac proces renderowania.
-   Jest tworzona i wypeL'niana przez `UIManager` i inne moduL'y logiki gry.
-   Jest konsumowana przez `GraphicalApplication` w watku renderowania.

---
# z"" fontmanager.cpp
## Opis ogolny

Plik `fontmanager.cpp` zawiera implementacje klasy `FontManager`, ktora jest singletonem (`g_fonts`) odpowiedzialnym za zarzadzanie wszystkimi fontami bitmapowymi w aplikacji.
## Zmienne globalne
## `g_fonts`

Globalna instancja `FontManager`.

FontManager g_fonts;
```
## Klasa `FontManager`
## `FontManager::FontManager()`

Konstruktor. Inicjalizuje domyLlny font (`m_defaultFont`) jako pusty obiekt `BitmapFont`, aby uniknac bL'edow, gdy LLaden font nie zostaL' jeszcze zaL'adowany.
## `void FontManager::terminate()`

Zwalnia wszystkie zaL'adowane fonty, czyszczac wektor `m_fonts` i resetujac wskaLsnik na domyLlny font.
## `void FontManager::clearFonts()`

CzyLci wszystkie zaL'adowane fonty i przywraca pusty font domyLlny. ULLywane np. przy przeL'adowywaniu zasobow.
## `void FontManager::importFont(std::string file)`
## Opis semantyczny
Laduje definicje fontu z pliku `.otfont`. Metoda jest bezpieczna watkowo - jeLli jest wywoL'ana z innego watku niLL graficzny, deleguje zadanie do `g_graphicsDispatcher`.
## DziaL'anie
1.  Rozwiazuje LcieLLke do pliku.
2.  Parsuje plik OTML.
3.  Odczytuje nazwe fontu z wezL'a `Font`.
4.  Sprawdza, czy font o tej nazwie juLL nie istnieje.
5.  Tworzy nowy obiekt `BitmapFont` i wywoL'uje jego metode `load()`.
6.  Dodaje nowo zaL'adowany font do wektora `m_fonts`.
7.  JeLli font jest oznaczony jako domyLlny (`default="true"`), ustawia go jako `m_defaultFont`.
## `bool FontManager::fontExists(const std::string& fontName)`

Sprawdza, czy font o podanej nazwie zostaL' juLL zaL'adowany.
## `BitmapFontPtr FontManager::getFont(const std::string& fontName)`

Wyszukuje i zwraca wskaLsnik do fontu o podanej nazwie. JeLli font nie zostanie znaleziony, loguje bL'ad i zwraca font domyLlny, aby zapobiec awarii.
## ZaleLLnoLci i powiazania

-   `framework/graphics/fontmanager.h`: Plik nagL'owkowy.
-   `framework/graphics/atlas.h`: PoLrednio, przez `BitmapFont`, ktory uLLywa atlasu do cachowania.
-   `framework/core/eventdispatcher.h`: ULLywa `g_graphicsDispatcher` do zapewnienia bezpieczeL"stwa watkowego.
-   `framework/core/resourcemanager.h`: Do znajdowania i odczytywania plikow `.otfont`.
-   `framework/otml/otml.h`: Do parsowania plikow definicji fontow.
-   Jest uLLywany przez `UIManager` i `UIWidget` do uzyskiwania dostepu do fontow potrzebnych do renderowania tekstu.

---
# z"" drawqueue.h
## Opis ogolny

Plik `drawqueue.h` deklaruje hierarchie klas `DrawQueueItem` oraz klase `DrawQueue`, ktore razem tworza system kolejkowania operacji rysowania. Jest to centralny mechanizm, ktory pozwala na zbieranie wszystkich poleceL" rysowania w jednej klatce, a nastepnie ich zoptymalizowane wykonanie.
## Typ wyliczeniowy `DrawType`

OkreLla, ktora czeLc kolejki ma zostac narysowana. ULLywane do renderowania warstwowego (np. interfejs za mapa i przed mapa).

| WartoLc | Opis |
| :--- | :--- |
| `DRAW_ALL` | Rysuje caL'a kolejke. |
| `DRAW_BEFORE_MAP` | Rysuje zadania dodane przed `markMapPosition()`. |
| `DRAW_AFTER_MAP` | Rysuje zadania dodane po `markMapPosition()`. |
## Hierarchia klas `DrawQueueItem`
## `struct DrawQueueItem` (baza)
Abstrakcyjna klasa bazowa dla wszystkich zadaL" w kolejce.

-   **`virtual void draw()`**: Metoda wirtualna do wykonania operacji rysowania.
-   **`virtual bool cache()`**: Metoda wirtualna do proby zbuforowania operacji w `DrawCache`.
## Klasy pochodne

KaLLda klasa reprezentuje konkretna operacje rysowania:
-   `DrawQueueItemTexturedRect`: Rysowanie prostokata z tekstura.
-   `DrawQueueItemTextureCoords`: Rysowanie geometrii z `CoordsBuffer` z tekstura.
-   `DrawQueueItemColoredTextureCoords`: Rysowanie geometrii z tekstura i wieloma kolorami.
-   `DrawQueueItemImageWithShader`: Rysowanie geometrii z tekstura i niestandardowym shaderem.
-   `DrawQueueItemFilledRect`: Rysowanie wypeL'nionego prostokata.
-   `DrawQueueItemClearRect`: Czyszczenie prostokatnego obszaru.
-   `DrawQueueItemFillCoords`: WypeL'nianie geometrii z `CoordsBuffer` kolorem.
-   `DrawQueueItemText`, `DrawQueueItemTextColored`: Rysowanie tekstu.
-   `DrawQueueItemLine`: Rysowanie linii.
## Hierarchia klas `DrawQueueCondition`
## `struct DrawQueueCondition` (baza)
Abstrakcyjna klasa bazowa dla warunkow modyfikujacych stan renderowania dla grupy zadaL".

-   **`m_start`, `m_end`**: Indeksy w `DrawQueue` okreLlajace zakres dziaL'ania warunku.
-   **`virtual void start(DrawQueue*)`**: Metoda wywoL'ywana przed pierwszym zadaniem objetym warunkiem.
-   **`virtual void end(DrawQueue*)`**: Metoda wywoL'ywana po ostatnim zadaniu objetym warunkiem.
## Klasy pochodne

-   `DrawQueueConditionClip`: Ustawia prostokat przycinania (clipping).
-   `DrawQueueConditionRotation`: Stosuje transformacje rotacji.
-   `DrawQueueConditionMark`: Specjalny warunek do rysowania zaznaczenia (np. na przedmiotach).
## Klasa `DrawQueue`
## Opis semantyczny
GL'owna klasa zarzadzajaca kolejka. Przechowuje liste zadaL" (`m_queue`) i warunkow (`m_conditions`). Dostarcza metody do dodawania roLLnych operacji rysowania i do finalnego wykonania caL'ej kolejki.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw(DrawType)` | Wykonuje wszystkie (lub czeLc) operacje rysowania z kolejki. |
| `add...(...)` | Metody do dodawania roLLnych typow `DrawQueueItem` do kolejki. |
| `setFrameBuffer(...)` | Konfiguruje renderowanie do bufora ramki. |
| `setOpacity(start, opacity)` | Stosuje przezroczystoLc do zadaL" od indeksu `start`. |
| `setClip(start, clip)` | Dodaje warunek `DrawQueueConditionClip` dla zadaL" od `start`. |
# z"" framebuffer.cpp
## Opis ogolny

Plik `framebuffer.cpp` zawiera implementacje klasy `FrameBuffer`, ktora jest opakowaniem (wrapperem) na obiekt bufora ramki (FBO) w OpenGL. UmoLLliwia renderowanie sceny do tekstury zamiast bezpoLrednio na ekran (tzw. off-screen rendering), co jest kluczowe dla efektow post-processingu, skalowania interfejsu i implementacji atlasu tekstur.
## Zmienne globalne
## `uint FrameBuffer::boundFbo`

Statyczna zmienna czL'onkowska, ktora Lledzi ID aktualnie zwiazanego (aktywnego) FBO. SL'uLLy do optymalizacji poprzez unikanie zbednych wywoL'aL"sk `glBindFramebuffer`, jeLli ten sam FBO jest juLL aktywny.

uint FrameBuffer::boundFbo = 0;
```
## Klasa `FrameBuffer`
## `FrameBuffer::FrameBuffer(bool withDepth)`

Konstruktor. WywoL'uje `internalCreate()` w celu utworzenia zasobow OpenGL.
-   **Parametr `withDepth`**: JeLli `true` i zdefiniowano `WITH_DEPTH_BUFFER`, tworzony jest rownieLL bufor gL'ebi, co pozwala na testowanie gL'ebi podczas renderowania do tego bufora.
## `FrameBuffer::~FrameBuffer()`

Destruktor. Zwalnia zasoby OpenGL (`glDeleteFramebuffers`, `glDeleteRenderbuffers`) w sposob bezpieczny watkowo, dodajac zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`).
## `void FrameBuffer::resize(const Size& size)`
## Opis semantyczny
Zmienia rozmiar bufora ramki. Tworzy nowa teksture o podanych wymiarach, ktora bedzie sL'uLLyc jako "pL'otno" do rysowania.
## DziaL'anie
1.  Sprawdza, czy zmiana rozmiaru jest konieczna.
2.  Tworzy nowy obiekt `Texture` o podanym rozmiarze.
3.  JeLli bufor gL'ebi jest wL'aczony, alokuje dla niego pamiec (`glRenderbufferStorage`).
4.  WiaLLe FBO, a nastepnie doL'acza do niego nowa teksture jako bufor koloru (`glFramebufferTexture2D`) oraz opcjonalnie bufor gL'ebi (`glFramebufferRenderbuffer`).
5.  Sprawdza status FBO (`glCheckFramebufferStatus`), aby upewnic sie, LLe jest on kompletny i gotowy do uLLycia.
## `void FrameBuffer::bind(const FrameBufferPtr& depthFramebuffer)`

Aktywuje bufor ramki jako cel renderowania. Wszystkie kolejne operacje rysowania beda kierowane do tekstury tego bufora.
-   Zapisuje i resetuje stan `Painter`.
-   WywoL'uje `internalBind()`.
-   Ustawia rozdzielczoLc `Painter` na rozmiar bufora.
## `void FrameBuffer::release()`

Deaktywuje bufor ramki i przywraca poprzedni cel renderowania (zazwyczaj bufor ekranu).
-   WywoL'uje `internalRelease()`.
-   Przywraca poprzedni stan `Painter`.
## `void FrameBuffer::draw(...)`

Metody te sL'uLLa do rysowania *zawartoLci* (tekstury) bufora ramki na aktualnie aktywnym celu renderowania.
-   `draw()`: Rysuje caL'a teksture.
-   `draw(const Rect& dest, const Rect& src)`: Rysuje fragment (`src`) tekstury w docelowym prostokacie (`dest`).
## `void FrameBuffer::doScreenshot(std::string fileName)`

Odczytuje zawartoLc pikseli z bufora ramki za pomoca `glReadPixels`, a nastepnie w osobnym watku (`g_asyncDispatcher`) zapisuje je do pliku PNG, odwracajac obraz w osi Y (konwersja z ukL'adu wspoL'rzednych OpenGL).
## Metody `internal...`

-   `internalCreate()`: Generuje obiekty FBO i RBO.
-   `internalBind()` / `internalRelease()`: BezpoLrednio wywoL'uja `glBindFramebuffer` i zarzadzaja statyczna zmienna `boundFbo`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/framebuffer.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bL'edow OpenGL i dostepu do `g_graphics`.
-   `framework/graphics/texture.h`: `FrameBuffer` uLLywa obiektu `Texture` jako swojego bufora koloru.
-   `framework/platform/platformwindow.h`: Dostep do `g_window` (potencjalnie).
-   `framework/core/asyncdispatcher.h`: ULLywany do asynchronicznego zapisu zrzutow ekranu.
-   Jest zarzadzana przez `FrameBufferManager`.

---
# z"" framebuffer.h
## Opis ogolny

Plik `framebuffer.h` deklaruje klase `FrameBuffer`, ktora jest obiektowym interfejsem do zarzadzania buforami ramki (FBO) w OpenGL. Pozwala na renderowanie sceny do tekstury zamiast bezpoLrednio na ekran.
## Klasa `FrameBuffer`
## Opis semantyczny
`FrameBuffer` enkapsuluje obiekt FBO z OpenGL oraz powiazana z nim teksture (jako bufor koloru) i opcjonalnie bufor gL'ebi. Udostepnia metody do bindowania (aktywacji), zwalniania, zmiany rozmiaru i rysowania zawartoLci bufora.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FrameBuffer(bool withDepth = false)` | Konstruktor. |
| `virtual ~FrameBuffer()` | Destruktor. |
| `void resize(const Size& size)` | Zmienia rozmiar bufora i powiazanej tekstury. |
| `void bind(...)` | Ustawia ten bufor jako aktywny cel renderowania. |
| `void release()` | Przywraca poprzedni cel renderowania. |
| `void draw()` / `draw(const Rect& dest)` / `draw(...)` | Rysuje teksture tego bufora na aktualnie aktywnym celu. |
| `void setSmooth(bool enabled)` | WL'acza/wyL'acza wygL'adzanie (filtrowanie liniowe) dla tekstury bufora. |
| `TexturePtr getTexture()` | Zwraca wskaLsnik do tekstury, do ktorej renderuje bufor. |
| `Size getSize()` | Zwraca rozmiar bufora. |
| `bool isSmooth()` | Zwraca stan wygL'adzania. |
| `uint getDepthRenderBuffer()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca ID bufora gL'ebi. |
| `bool hasDepth()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca `true`, jeLli bufor posiada bufor gL'ebi. |
| `std::vector<uint32_t> readPixels()` | Odczytuje zawartoLc bufora do pamieci systemowej. |
| `void doScreenshot(std::string fileName)` | Zapisuje zawartoLc bufora do pliku PNG. |
## Zmienne prywatne

-   `m_texture`: WskaLsnik na obiekt `Texture` uLLywany jako bufor koloru.
-   `m_fbo`: ID obiektu FBO w OpenGL.
-   `m_prevBoundFbo`: Przechowuje ID poprzednio aktywnego FBO, aby moLLna byL'o go przywrocic.
-   `m_smooth`: Flaga wygL'adzania.
-   `m_depthRbo`, `m_depth`: (Tylko z `WITH_DEPTH_BUFFER`) ID bufora gL'ebi i flaga jego istnienia.
-   `boundFbo`: Statyczna zmienna Lledzaca globalnie aktywny FBO.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Definicje typow, np. `TexturePtr`.
-   `framework/graphics/texture.h`: Wymaga peL'nej definicji `Texture`.
-   Jest tworzona i zarzadzana przez `FrameBufferManager`. ULLywana przez `Painter`, `Atlas` i w gL'ownej petli renderowania w `GraphicalApplication`.

---
# z"" framebuffermanager.cpp
## Opis ogolny

Plik `framebuffermanager.cpp` zawiera implementacje klasy `FrameBufferManager`, ktora jest singletonem (`g_framebuffers`) odpowiedzialnym za tworzenie i zarzadzanie obiektami `FrameBuffer`.
## Zmienne globalne
## `g_framebuffers`

Globalna instancja `FrameBufferManager`.

FrameBufferManager g_framebuffers;
```
## Klasa `FrameBufferManager`
## `void FrameBufferManager::init()`
## Opis semantyczny
Inicjalizuje menedLLera. Tworzy dwa predefiniowane, "tymczasowe" bufory ramki, ktore moga byc uLLywane przez roLLne czeLci systemu do krotkotrwaL'ych operacji renderowania poza ekranem, bez potrzeby tworzenia i niszczenia wL'asnych buforow.

-   `m_temporaryFramebuffer`: Ogolnego przeznaczenia.
-   `m_drawQueueTemporaryFramebuffer`: Prawdopodobnie uLLywany przez `DrawQueue` do specyficznych operacji.
## `void FrameBufferManager::terminate()`

Zwalnia wszystkie utworzone bufory ramki, w tym tymczasowe, czyszczac liste `m_framebuffers`.
## `FrameBufferPtr FrameBufferManager::createFrameBuffer(bool withDepth)`
## Opis semantyczny
Metoda fabryczna do tworzenia nowych obiektow `FrameBuffer`.
## DziaL'anie
1.  Tworzy nowa instancje `FrameBuffer`, przekazujac flage `withDepth`.
2.  Dodaje nowo utworzony bufor do wewnetrznej listy `m_framebuffers` w celu Lledzenia.
3.  Zwraca wskaLsnik na nowo utworzony obiekt.
## ZaleLLnoLci i powiazania

-   `framework/graphics/framebuffermanager.h`: Plik nagL'owkowy.
-   Klasa ta jest uLLywana przez `Atlas` do tworzenia swoich "pL'ocien" oraz przez `GraphicalApplication` do tworzenia buforow dla gL'ownej sceny i mapy.

---
# z"" graph.cpp
## Opis ogolny

Plik `graph.cpp` implementuje klase `Graph`, ktora sL'uLLy do wizualizacji danych w czasie rzeczywistym w formie prostego wykresu liniowego. Jest to narzedzie gL'ownie do celow debugowania i profilowania wydajnoLci.
## Zmienne globalne
## `g_graphs[GRAPH_LAST + 1]`

Globalna tablica instancji `Graph`, gdzie kaLLda instancja odpowiada za Lledzenie i rysowanie innego parametru (np. czasu klatki, liczby wywoL'aL" rysujacych, opoLsnienia sieciowego).

Graph g_graphs[GRAPH_LAST + 1] = {
    {"Total frame time"},
    // ... inne definicje
};
```
## Klasa `Graph`
## `Graph::Graph(const std::string& name, size_t capacity)`

Konstruktor. Inicjalizuje wykres z podana nazwa i maksymalna liczba probek do przechowywania.
## `void Graph::draw(const Rect& dest)`
## Opis semantyczny
Rysuje wykres w podanym prostokacie ekranu. Metoda musi byc wywoL'ywana z watku graficznego.
## DziaL'anie
1.  Rysuje tL'o i ramke wykresu.
2.  Rysuje nazwe wykresu.
3.  Pobiera `elements` ostatnich probek z `m_values` (tyle, ile zmieLci sie w `dest`).
4.  Znajduje minimalna i maksymalna wartoLc w pobranym zakresie.
5.  Normalizuje wartoLci i tworzy geometrie linii wykresu.
6.  Rysuje etykiety z wartoLcia minimalna, maksymalna i ostatnia.
7.  Rysuje linie wykresu za pomoca `g_painter->drawLine()`.
## `void Graph::clear()`

CzyLci wszystkie zebrane dane z wykresu.
## `void Graph::addValue(int value, bool ignoreSmallValues)`
## Opis semantyczny
Dodaje nowa probke danych do wykresu. Metoda jest bezpieczna watkowo dzieki uLLyciu `std::mutex`.
## DziaL'anie
1.  Opcjonalnie ignoruje maL'e, powtarzajace sie wartoLci, aby wykres byL' bardziej czytelny.
2.  Dodaje nowa wartoLc na koniec kolejki `m_values`.
3.  JeLli kolejka przekracza pojemnoLc, usuwa najstarsza wartoLc.
## ZaleLLnoLci i powiazania

-   `framework/graphics/graph.h`: Plik nagL'owkowy.
-   `framework/graphics/painter.h`: ULLywa `g_painter` do rysowania.
-   `framework/graphics/textrender.h`: ULLywa `g_text` do rysowania etykiet.
-   `framework/core/eventdispatcher.h`: ULLywany do walidacji watku.
-   Jest uLLywana w roLLnych czeLciach aplikacji (`GraphicalApplication`, `Protocol`) do zbierania danych o wydajnoLci, ktore sa nastepnie rysowane w gL'ownej petli renderowania.

---
# z"" graph.h
## Opis ogolny

Plik `graph.h` deklaruje klase `Graph` oraz powiazane z nia typy wyliczeniowe. Jest to narzedzie do wizualizacji danych w czasie rzeczywistym, przeznaczone do debugowania i profilowania.
## Typ wyliczeniowy `GraphType`

Definiuje staL'e dla roLLnych typow wykresow, ktore moga byc Lledzone w aplikacji.

| Nazwa | Opis |
| :--- | :--- |
| `GRAPH_TOTAL_FRAME_TIME` | CaL'kowity czas klatki. |
| `GRAPH_CPU_FRAME_TIME` | Czas renderowania po stronie CPU. |
| `GRAPH_GPU_CALLS` | Liczba wywoL'aL" do API graficznego. |
| `GRAPH_GPU_DRAWS` | Liczba operacji rysowania. |
| `GRAPH_PROCESSING_POLL` | Czas przetwarzania zdarzeL" w watku logiki. |
| `GRAPH_GRAPHICS_POLL` | Czas przetwarzania zdarzeL" w watku graficznym. |
| `GRAPH_DISPATCHER_EVENTS` | Liczba zdarzeL" w gL'ownym dyspozytorze. |
| `GRAPH_GRAPHICS_EVENTS` | Liczba zdarzeL" w dyspozytorze graficznym. |
| `GRAPH_LATENCY` | OpoLsnienie sieciowe (ping). |
## Klasa `Graph`
## Opis semantyczny
Klasa `Graph` przechowuje kolejke (`std::deque`) ostatnich wartoLci liczbowych i udostepnia metode do narysowania ich w postaci prostego wykresu liniowego. Jest bezpieczna watkowo przy dodawaniu wartoLci.
## StaL'e

-   `MAX_CAPACITY`: Maksymalna liczba probek, jaka moLLe przechowac wykres.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graph(...)` | Konstruktor. |
| `void draw(const Rect& dest)` | Rysuje wykres w podanym prostokacie. |
| `void clear()` | CzyLci dane wykresu. |
| `void addValue(int value, bool ignoreSmallValues = false)` | Dodaje nowa wartoLc do wykresu. |
## Zmienne prywatne

-   `m_name`: Nazwa wykresu, wyLwietlana jako tytuL'.
-   `m_capacity`: Maksymalna liczba przechowywanych probek.
-   `m_ignores`: Licznik ignorowanych maL'ych wartoLci.
-   `m_values`: Kolejka przechowujaca dane.
-   `m_mutex`: Mutex chroniacy dostep do `m_values`.
## Zmienne globalne

-   `g_graphs[GRAPH_LAST + 1]`: Globalna tablica, w ktorej przechowywane sa instancje `Graph` dla kaLLdego typu z `GraphType`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uLLywana przez `GraphicalApplication` do rysowania informacji debugowania. Dane sa do niej dodawane z roLLnych czeLci systemu, np. z petli gL'ownej, `Painter`, `EventDispatcher`, `Protocol`.

---
# z"" glutil.h
## Opis ogolny

Plik `glutil.h` (GL Utility) jest plikiem nagL'owkowym, ktorego jedynym zadaniem jest wL'aczenie odpowiednich nagL'owkow OpenGL, OpenGL ES, EGL lub GLEW, w zaleLLnoLci od platformy i opcji kompilacji. DziaL'a jako centralny punkt doL'aczania bibliotek graficznych, co upraszcza zarzadzanie zaleLLnoLciami w innych plikach.
## Logika warunkowego doL'aczania

Plik uLLywa dyrektyw preprocesora do wyboru odpowiednich nagL'owkow:

1.  **Android lub Emscripten (`ANDROID` || `__EMSCRIPTEN__`)**:
    -   DoL'aczane sa nagL'owki **OpenGL ES 2.0** (`<GLES2/gl2.h>`, `<GLES2/gl2ext.h>`) oraz **EGL** (`<EGL/egl.h>`, `<EGL/eglext.h>`). EGL jest interfejsem, ktory L'aczy API renderowania (jak OpenGL ES) z natywnym systemem okienkowym platformy.

2.  **Inne platformy z `OPENGL_ES`**:
    -   Podobnie jak wyLLej, doL'aczane sa nagL'owki OpenGL ES 2.0 i EGL. Definiowane sa rownieLL makra `GL_GLEXT_PROTOTYPES`, `EGL_EGL_PROTOTYPES`, aby zapewnic dostep do prototypow funkcji.

3.  **DomyLlnie (Desktop - Windows/Linux/macOS)**:
    -   DoL'aczana jest biblioteka **GLEW** (`<GL/glew.h>`). GLEW (OpenGL Extension Wrangler) jest biblioteka, ktora upraszcza zarzadzanie i L'adowanie rozszerzeL" OpenGL, co jest konieczne na platformach desktopowych.
    -   Na systemach innych niLL Windows, `GLEW_STATIC` jest definiowane, aby linkowac GLEW statycznie.
## ZaleLLnoLci i powiazania

-   Ten plik nie ma zaleLLnoLci od innych plikow projektu.
-   Jest doL'aczany przez `framework/graphics/declarations.h`, co sprawia, LLe definicje OpenGL sa dostepne we wszystkich plikach moduL'u graficznego.

---
# z"" graphics.cpp
## Opis ogolny

Plik `graphics.cpp` zawiera implementacje klasy `Graphics`, ktora jest singletonem (`g_graphics`) odpowiedzialnym za inicjalizacje i zarzadzanie globalnym stanem silnika graficznego opartego na OpenGL.
## Zmienne globalne
## `g_graphics`

Globalna instancja `Graphics`.

Graphics g_graphics;
```
## Klasa `Graphics`
## `Graphics::Graphics()`

Konstruktor. Inicjalizuje domyLlna maksymalna wielkoLc tekstury na `2048`.
## `void Graphics::init()`
## Opis semantyczny
GL'owna metoda inicjalizujaca. Uruchamia i konfiguruje kontekst OpenGL oraz inicjalizuje wszystkie pod-menedLLery graficzne.
## DziaL'anie
1.  Odczytuje i zapisuje informacje o sterowniku graficznym (`GL_VENDOR`, `GL_RENDERER`, `GL_VERSION`, `GL_EXTENSIONS`) za pomoca `glGetString`.
2.  Loguje te informacje.
3.  **Na platformach desktopowych**:
    -   Sprawdza, czy wersja OpenGL jest co najmniej 2.0.
    -   Inicjalizuje GLEW (`glewInit()`).
    -   Sprawdza, czy dostepne sa rozszerzenia FBO (Framebuffer Object) i w razie potrzeby mapuje funkcje `...EXT` na standardowe nazwy.
4.  WL'acza globalnie mieszanie kolorow (`glEnable(GL_BLEND)`).
5.  Pobiera maksymalny obsL'ugiwany rozmiar tekstury z `GL_MAX_TEXTURE_SIZE`.
6.  (Opcjonalnie) Sprawdza wsparcie dla bufora gL'ebi.
7.  Ustawia flage `m_ok` na `true`, sygnalizujac pomyLlna inicjalizacje.
8.  Tworzy i bindowanie globalny obiekt `Painter`.
9.  Inicjalizuje menedLLery: `g_textures`, `g_framebuffers`, `g_atlas`, `g_text`.
## `void Graphics::terminate()`

Zwalnia zasoby w odwrotnej kolejnoLci do inicjalizacji, wywoL'ujac `terminate()` na wszystkich pod-menedLLerach oraz niszczac obiekt `Painter`.
## `void Graphics::resize(const Size& size)`

Aktualizuje rozmiar viewportu. Ustawia `m_viewportSize` i przekazuje nowy rozmiar do `g_painter`, ktory z kolei aktualizuje macierz projekcji i `glViewport`.
## `void Graphics::checkForError(...)`

Metoda pomocnicza, ktora sprawdza bL'edy OpenGL za pomoca `glGetError()`. JeLli wystapiL' bL'ad, loguje go wraz z informacja o funkcji, pliku i numerze linii, w ktorej zostaL' wykryty. W trybie debugowania powoduje to bL'ad krytyczny.
## ZaleLLnoLci i powiazania

-   `framework/graphics/graphics.h`: Plik nagL'owkowy.
-   `fontmanager.h`, `painter.h`, `atlas.h`, `texturemanager.h`, `framebuffermanager.h`, `textrender.h`: Inicjalizuje i zarzadza tymi kluczowymi komponentami graficznymi.
-   `framework/platform/platformwindow.h`: PoLrednio, poprzez `g_window`, od ktorego zaleLLy kontekst OpenGL.
-   Jest to centralna klasa-menedLLer dla caL'ego podsystemu graficznego.

---
# z"" graphics.h
## Opis ogolny

Plik `graphics.h` deklaruje interfejs klasy `Graphics`, ktora jest singletonem (`g_graphics`) zarzadzajacym globalnym stanem i inicjalizacja silnika graficznego.
## Klasa `Graphics`
## Opis semantyczny
`Graphics` peL'ni role gL'ownego menedLLera podsystemu graficznego. Odpowiada za inicjalizacje OpenGL/GLES, odpytywanie o moLLliwoLci sprzetowe (wersja, rozszerzenia, maksymalny rozmiar tekstury) oraz za zarzadzanie cyklem LLycia innych menedLLerow graficznych, takich jak `Painter`, `TextureManager` czy `FontManager`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graphics()` | Konstruktor. |
| `void init()` | Inicjalizuje silnik graficzny (kontekst OpenGL, menedLLery). |
| `void terminate()` | Zwalnia zasoby silnika graficznego. |
| `void resize(const Size& size)` | Aktualizuje rozmiar viewportu. |
| `void checkDepthSupport()`| Sprawdza wsparcie dla bufora gL'ebi. |
| `int getMaxTextureSize()` | Zwraca maksymalny obsL'ugiwany rozmiar tekstury. |
| `const Size& getViewportSize()` | Zwraca aktualny rozmiar viewportu (okna/ekranu). |
| `std::string getVendor()` | Zwraca nazwe producenta karty graficznej. |
| `std::string getRenderer()` | Zwraca nazwe modelu karty graficznej/sterownika. |
| `std::string getVersion()` | Zwraca wersje OpenGL. |
| `std::string getExtensions()` | Zwraca liste dostepnych rozszerzeL" OpenGL. |
| `bool ok()` | Zwraca `true`, jeLli inicjalizacja grafiki przebiegL'a pomyLlnie. |
| `void checkForError(...)` | Sprawdza i loguje bL'edy OpenGL. |
## Zmienne prywatne

-   `m_viewportSize`: Aktualny rozmiar obszaru renderowania.
-   `m_vendor`, `m_renderer`, `m_version`, `m_extensions`: Informacje o sterowniku graficznym.
-   `m_maxTextureSize`: Maksymalny rozmiar tekstury obsL'ugiwany przez sprzet.
-   `m_ok`: Flaga pomyLlnej inicjalizacji.
## Zmienne globalne

-   `g_graphics`: Globalna instancja `Graphics`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`, `painter.h`: Podstawowe deklaracje i klasa `Painter`.
-   Jest oznaczona jako `@bindsingleton g_graphics`, co udostepnia jej metody (np. `getVendor`) w Lua.
-   Jest inicjalizowana i zamykana przez `GraphicalApplication`.

---
# z"" image.cpp
## Opis ogolny

Plik `image.cpp` zawiera implementacje klasy `Image`, ktora reprezentuje obraz rastrowy w pamieci RAM. Jest to podstawowa klasa do L'adowania, manipulowania i zapisywania danych obrazow, zanim zostana one przesL'ane do pamieci karty graficznej jako tekstury.
## Klasa `Image`
## `Image::Image(const Size& size, int bpp, uint8 *pixels)`

Konstruktor. Tworzy obiekt `Image` o podanych wymiarach i gL'ebi bitowej (bpp - bits per pixel). Opcjonalnie kopiuje dane pikseli z podanego bufora.
## `ImagePtr Image::load(std::string file)`

Statyczna metoda fabryczna do L'adowania obrazu z pliku. Obecnie obsL'uguje tylko format PNG, wywoL'ujac `loadPNG`.
## `ImagePtr Image::loadPNG(...)`

Statyczne metody do L'adowania obrazu w formacie PNG z pliku lub z bufora w pamieci. ULLywaja funkcji `load_apng` z `apngloader.cpp` do parsowania danych.
## `void Image::savePNG(const std::string& fileName)`

Zapisuje obraz do pliku w formacie PNG, uLLywajac funkcji `save_png` z `apngloader.cpp`.
## `void Image::blit(const Point& dest, const ImagePtr& other)`

Kopiuje piksele z innego obrazu (`other`) do tego obrazu w podane miejsce (`dest`). Kopiowanie odbywa sie z uwzglednieniem przezroczystoLci - piksele w peL'ni przezroczyste w obrazie LsrodL'owym nie sa kopiowane.
## `void Image::paste(const ImagePtr& other)`

NakL'ada inny obraz (`other`) na ten obraz, zastepujac istniejace piksele. Nie uwzglednia przezroczystoLci.
## `ImagePtr Image::upscale()`

Tworzy i zwraca nowy obraz, ktory jest dwukrotnie wiekszy od oryginalnego. KaLLdy piksel z obrazu LsrodL'owego jest powielany do bloku 2x2 w obrazie docelowym (skalowanie metoda "najbliLLszego sasiada").
## `bool Image::nextMipmap()`

Generuje nastepny, mniejszy poziom mipmapy na podstawie bieLLacych danych pikseli. Oblicza Lrednia z bloku 2x2 pikseli, aby stworzyc jeden piksel dla mniejszego obrazu. Jest to prosta implementacja filtrowania biliniowego. Zwraca `false`, gdy obraz osiagnie rozmiar 1x1.
## `ImagePtr Image::fromQRCode(const std::string& code, int border)`

Statyczna metoda fabryczna, ktora generuje obraz kodu QR na podstawie podanego tekstu, uLLywajac biblioteki `qrcodegen`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/image.h`: Plik nagL'owkowy.
-   `framework/core/resourcemanager.h`: Do otwierania i odczytywania plikow obrazow.
-   `framework/graphics/apngloader.h`: Do obsL'ugi formatu PNG/APNG.
-   `framework/util/qrcodegen.h`: Do generowania kodow QR.
-   Obiekty `Image` sa zazwyczaj krotkotrwaL'e - istnieja od momentu zaL'adowania z pliku do momentu utworzenia z nich obiektu `Texture` i przesL'ania danych do GPU.

---
# z"" hardwarebuffer.h
## Opis ogolny

Plik `hardwarebuffer.h` deklaruje klase `HardwareBuffer`, ktora jest opakowaniem na sprzetowe bufory wierzchoL'kow (Vertex Buffer Objects - VBO) w OpenGL. UmoLLliwia przechowywanie danych geometrycznych (np. wspoL'rzednych wierzchoL'kow) w pamieci karty graficznej w celu uzyskania wysokiej wydajnoLci renderowania.
## Klasa `HardwareBuffer`
## Opis semantyczny
`HardwareBuffer` enkapsuluje ID bufora VBO w OpenGL i dostarcza podstawowe metody do jego obsL'ugi: bindowania, odpinania i zapisu danych. ULLycie VBO jest znacznie wydajniejsze niLL przesyL'anie danych wierzchoL'kow z pamieci RAM do GPU w kaLLdej klatce.
## Typy wyliczeniowe (Enums)

-   **`enum Type`**: OkreLla typ bufora.
    -   `VertexBuffer` (`GL_ARRAY_BUFFER`): Przechowuje atrybuty wierzchoL'kow (np. pozycje, kolory, wspoL'rzedne tekstur).
    -   `IndexBuffer` (`GL_ELEMENT_ARRAY_BUFFER`): Przechowuje indeksy wierzchoL'kow (nieuLLywane w tym kodzie).
-   **`enum UsagePattern`**: Wskazowka dla sterownika OpenGL, jak dane beda uLLywane.
    -   `StreamDraw` (`GL_STREAM_DRAW`): Dane zmieniane czesto, uLLywane rzadko.
    -   `StaticDraw` (`GL_STATIC_DRAW`): Dane ustawiane raz, uLLywane czesto.
    -   `DynamicDraw` (`GL_DYNAMIC_DRAW`): Dane zmieniane i uLLywane czesto.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HardwareBuffer(Type type)` | Konstruktor, tworzy nowy obiekt bufora w OpenGL (`glGenBuffers`). |
| `~HardwareBuffer()` | Destruktor, zwalnia obiekt bufora (`glDeleteBuffers`). |
| `void bind()` | Bindowanie (aktywuje) bufor w kontekLcie OpenGL (`glBindBuffer`). |
| `static void unbind(Type type)` | Odpina jakikolwiek bufor danego typu. |
| `void write(...)` | Kopiuje dane z pamieci RAM do bufora w pamieci GPU (`glBufferData`). |
## Zmienne prywatne

-   `m_type`: Typ bufora (`VertexBuffer` lub `IndexBuffer`).
-   `m_id`: ID (uchwyt) bufora w OpenGL.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Zawiera `glutil.h` z definicjami OpenGL.
-   Jest uLLywana przez `VertexArray` (w `coordsbuffer.h`) do opcjonalnego keszowania geometrii na GPU.
-   `Painter` uLLywa `HardwareBuffer` do ustawiania atrybutow wierzchoL'kow podczas rysowania.

---
# z"" image.h
## Opis ogolny

Plik `image.h` deklaruje klase `Image`, ktora reprezentuje obraz rastrowy przechowywany w pamieci systemowej (RAM). Jest to podstawowa struktura danych do manipulacji pikselami przed ich wysL'aniem do karty graficznej jako tekstura.
## Klasa `Image`
## Opis semantyczny
`Image` to kontener na surowe dane pikseli. Przechowuje wymiary obrazu, liczbe bitow na piksel oraz sam bufor pikseli. Udostepnia metody do L'adowania obrazow z plikow, zapisywania ich, a takLLe do podstawowych operacji graficznych, takich jak kopiowanie fragmentow (`blit`), generowanie mipmap czy skalowanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Image(...)` | Konstruktor. |
| `static ImagePtr load(...)` | Statyczna metoda fabryczna do L'adowania obrazu z pliku (obecnie tylko PNG). |
| `static ImagePtr loadPNG(...)` | Laduje obraz PNG z pliku lub bufora w pamieci. |
| `void savePNG(...)` | Zapisuje obraz do pliku w formacie PNG. |
| `void blit(...)` | Kopiuje inny obraz na ten obraz z uwzglednieniem przezroczystoLci. |
| `void paste(...)` | NakL'ada inny obraz na ten obraz, zastepujac piksele. |
| `ImagePtr upscale()` | Zwraca nowa, dwukrotnie wieksza wersje obrazu. |
| `void resize(...)` | Zmienia rozmiar obrazu, realokujac bufor pikseli. |
| `bool nextMipmap()` | Generuje kolejny poziom mipmapy, zmniejszajac obraz o poL'owe. |
| `void setPixel(...)` | Ustawia kolor pojedynczego piksela. |
| `std::vector<uint8>& getPixels()` | Zwraca referencje do wektora pikseli. |
| `uint8* getPixelData()` | Zwraca surowy wskaLsnik na dane pikseli. |
| `int getPixelCount()` | Zwraca liczbe pikseli. |
| `const Size& getSize()` | Zwraca wymiary obrazu. |
| `int getBpp()` | Zwraca liczbe bajtow na piksel. |
| `static ImagePtr fromQRCode(...)` | Tworzy obraz z kodu QR. |
## Zmienne prywatne

-   `m_pixels`: Wektor przechowujacy dane pikseli.
-   `m_size`: Wymiary obrazu.
-   `m_bpp`: Liczba bajtow na piksel.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: Potencjalnie, chociaLL tutaj uLLywa `std::vector`.
-   Jest uLLywana przez `Texture` i `AnimatedTexture` jako LsrodL'o danych pikseli podczas tworzenia tekstur.
-   Wykorzystywana przez `PlatformWindow` do L'adowania ikon i kursorow.

---
# z"" framebuffermanager.h
## Opis ogolny

Plik `framebuffermanager.h` deklaruje klase `FrameBufferManager`, ktora jest singletonem (`g_framebuffers`) sL'uLLacym do zarzadzania i tworzenia obiektow `FrameBuffer`.
## Klasa `FrameBufferManager`
## Opis semantyczny
`FrameBufferManager` peL'ni role fabryki i menedLLera dla obiektow `FrameBuffer`. Upraszcza ich tworzenie i zarzadzanie cyklem LLycia. Udostepnia rownieLL dwa predefiniowane, "tymczasowe" bufory, ktore moga byc uLLywane w caL'ym systemie do krotkotrwaL'ych operacji renderowania poza ekranem, co pozwala uniknac kosztownego tworzenia i niszczenia FBO.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedLLera i tworzy tymczasowe bufory ramki. |
| `void terminate()` | Zwalnia wszystkie zarzadzane bufory ramki. |
| `void clear()` | (Brak implementacji) Prawdopodobnie miaL'a sL'uLLyc do zwolnienia wszystkich buforow poza tymczasowymi. |
| `FrameBufferPtr createFrameBuffer(bool withDepth = false)` | Metoda fabryczna tworzaca i zwracajaca nowy obiekt `FrameBuffer`. |
| `const FrameBufferPtr& getTemporaryFrameBuffer()` | Zwraca wskaLsnik do pierwszego tymczasowego bufora. |
| `const FrameBufferPtr& getDrawQueueTemporaryFrameBuffer()` | Zwraca wskaLsnik do drugiego tymczasowego bufora, prawdopodobnie uLLywanego przez `DrawQueue`. |
## Zmienne chronione

-   `m_temporaryFramebuffer`: Pierwszy tymczasowy `FrameBuffer`.
-   `m_drawQueueTemporaryFramebuffer`: Drugi tymczasowy `FrameBuffer`.
-   `m_framebuffers`: Wektor przechowujacy wskaLsniki do wszystkich utworzonych (i niezwolnionych) buforow ramki. |
## Zmienne globalne

-   `g_framebuffers`: Globalna instancja `FrameBufferManager`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/framebuffer.h`: Deklaracja klasy `FrameBuffer`.
-   Jest to kluczowy komponent, od ktorego zaleLLa inne czeLci systemu graficznego, takie jak `Atlas` i `GraphicalApplication`, ktore potrzebuja tworzyc wL'asne bufory ramki.

---
# z"" painter.h
## Opis ogolny

Plik `painter.h` deklaruje klase `Painter`, ktora jest centralnym interfejsem do wszystkich operacji rysowania w 2D. Abstrakcjonuje ona niskopoziomowe wywoL'ania OpenGL, dostarczajac prostsze API do rysowania prostokatow, tekstur, linii i zarzadzania stanem renderowania.
## Klasa `Painter`
## Opis semantyczny
`Painter` dziaL'a jak maszyna stanow. Przechowuje aktualny stan renderowania, taki jak macierze transformacji, kolor, tryb mieszania, aktywny shader, tekstura, itp. KaLLda operacja rysowania jest wykonywana w kontekLcie tego stanu. `Painter` zarzadza rownieLL wL'asnymi, domyLlnymi programami shaderow do podstawowych operacji.
## Typy wyliczeniowe (Enums)

-   `BlendEquation`: OkreLla, jak kolory sa mieszane (np. dodawanie, odejmowanie).
-   `CompositionMode`: Definiuje predefiniowane tryby mieszania (`glBlendFunc`), np. normalne (z przezroczystoLcia), addytywne, mnoLLenie.
-   `DepthFunc`: OkreLla funkcje testu gL'ebi.
-   `DrawMode`: OkreLla prymityw do rysowania (trojkaty, paski trojkatow).
## Struktura `PainterState`

Przechowuje peL'ny stan `Painter`, co pozwala na jego zapisywanie i przywracanie.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Zarzadzanie stanem** | |
| `resetState()` | Przywraca wszystkie ustawienia do wartoLci domyLlnych. |
| `saveState()` / `restoreSavedState()` | Zapisuje/przywraca stan na wewnetrznym stosie. |
| `setTransformMatrix(...)`, `setProjectionMatrix(...)`, ... | Ustawiaja poszczegolne elementy stanu (macierze, tryb mieszania, etc.). |
| `scale()`, `translate()`, `rotate()` | Modyfikuja bieLLaca macierz transformacji. |
| **Operacje rysowania** | |
| `clear(const Color& color)` | CzyLci caL'y bufor ramki. |
| `drawCoords(...)` | Niskopoziomowa metoda rysujaca geometrie z `CoordsBuffer`. |
| `drawFilledRect(const Rect& dest)` | Rysuje wypeL'niony prostokat. |
| `drawTexturedRect(...)` | Rysuje prostokat z tekstura. |
| `drawText(...)` | Rysuje tekst (przez `TextRender`). |
| `drawLine(...)` | Rysuje linie. |
| `drawCache(...)` | Rysuje dane zbuforowane w `DrawCache`. |
| **Gettery** | |
| `getTransformMatrix()`, `getColor()`, `getClipRect()`, ... | Zwracaja aktualne wartoLci stanu. |
| `draws()`, `calls()` | Zwracaja statystyki renderowania dla bieLLacej klatki. |
## Zmienne chronione/prywatne

-   `m_transformMatrix`, `m_projectionMatrix`, ...: Zmienne przechowujace aktualny stan.
-   `m_transformMatrixStack`: Stos do zapisywania macierzy transformacji.
-   `m_olderStates`: Stos do zapisywania peL'nego stanu `PainterState`.
-   `m_draw...Program`: WskaLsniki na domyLlne programy shaderow.
## Zmienne globalne

-   `g_painter`: Globalny wskaLsnik na instancje `Painter`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`, `coordsbuffer.h`, `paintershaderprogram.h`, `texture.h`, `colorarray.h`, `drawqueue.h`: Deklaracje typow, z ktorymi `Painter` wspoL'pracuje.
-   Jest to centralny komponent renderujacy, uLLywany bezpoLrednio lub poLrednio przez `DrawQueue`, `UIWidget`, `TextRender` i inne.

---
# z"" painter.cpp
## Opis ogolny

Plik `painter.cpp` zawiera implementacje klasy `Painter`, ktora jest sercem silnika renderujacego. Odpowiada za bezpoLrednia komunikacje z API graficznym (OpenGL) w celu rysowania prymitywow 2D.
## Zmienne globalne
## `g_painter`

Globalny wskaLsnik na jedyna instancje `Painter`. Jest inicjalizowany w `Graphics::init()`.

Painter* g_painter = nullptr;
```
## Klasa `Painter`
## `Painter::Painter()`

Konstruktor. Inicjalizuje domyLlne wartoLci stanu, takie jak macierze, kolory i tryby mieszania. Co najwaLLniejsze, tworzy i kompiluje zestaw domyLlnych programow shaderow, ktore sa uLLywane do podstawowych operacji rysowania:
-   `m_drawTexturedProgram`: Do rysowania tekstur.
-   `m_drawSolidColorProgram`: Do rysowania jednolitych kolorow.
-   `m_drawSolidColorOnTextureProgram`: Do rysowania jednolitego koloru na wierzchu tekstury.
-   `m_drawOutfitLayersProgram`: Specjalny shader do rysowania strojow postaci z kolorowaniem.
-   `m_drawNewProgram`: Shader uLLywany przez `DrawCache` do zoptymalizowanego rysowania wsadowego.
-   `m_drawTextProgram`, `m_drawLineProgram`: Specjalne shadery do rysowania tekstu i linii.
## `void Painter::bind()` i `void Painter::unbind()`

Metody wywoL'ywane na poczatku i na koL"cu cyklu LLycia `Painter`. `bind()` wL'acza podstawowe atrybuty wierzchoL'kow, ktore sa zawsze aktywne.
## `void Painter::resetState()`

Przywraca wszystkie parametry `Painter` (kolor, macierze, tryby mieszania itp.) do ich wartoLci domyLlnych.
## `void Painter::saveState()` i `void Painter::restoreSavedState()`

Implementuja mechanizm stosu do zapisywania i przywracania stanu renderowania. Pozwala to na tymczasowa zmiane stanu (np. ustawienie przycinania) i L'atwy powrot do poprzedniego stanu.
## Metody `updateGl...()`

Prywatne metody pomocnicze (`updateGlTexture`, `updateGlCompositionMode`, `updateGlClipRect` itd.), ktore aplikuja zmiany stanu `Painter` do rzeczywistego stanu OpenGL. Sa wywoL'ywane, gdy odpowiednia wL'aLciwoLc `Painter` (np. `m_compositionMode`) ulega zmianie.
## `void Painter::setResolution(const Size& resolution)`

Aktualizuje rozdzielczoLc renderowania. NajwaLLniejsza czeLcia jest przeliczenie macierzy projekcji (`m_projectionMatrix`), ktora mapuje wspoL'rzedne w pikselach na znormalizowane wspoL'rzedne urzadzenia OpenGL (-1 do 1).
## `void Painter::drawCoords(...)`

Niskopoziomowa metoda, ktora jest podstawa wiekszoLci operacji rysowania.
1.  Bindowanie i konfiguruje odpowiedni program shadera.
2.  Przekazuje do shadera uniformy (macierze, kolor, czas itp.).
3.  Ustawia wskaLsniki na dane atrybutow wierzchoL'kow (pozycja, wspoL'rzedne tekstury, kolor).
4.  WywoL'uje `glDrawArrays` w celu narysowania geometrii.
5.  Zlicza statystyki (`m_draws`, `m_calls`).
## Metody `draw...Rect(...)` i `draw...Coords(...)`

Wysokopoziomowe metody rysujace, ktore przygotowuja `CoordsBuffer` z odpowiednia geometria, a nastepnie wywoL'uja `drawCoords` do jej narysowania.
## `void Painter::drawCache(...)`

Specjalna, zoptymalizowana metoda do rysowania duLLej liczby wierzchoL'kow na raz. ULLywa dedykowanego shadera (`m_drawNewProgram`), ktory pobiera pozycje, wspoL'rzedne tekstury i kolor jako osobne atrybuty dla kaLLdego wierzchoL'ka.
## ZaleLLnoLci i powiazania

-   Jest to klasa niskiego poziomu, ktora bezpoLrednio zaleLLy od API graficznego (OpenGL/GLES/GLEW).
-   `framework/graphics/shaders/shaders.h`: Zawiera kod LsrodL'owy domyLlnych shaderow.
-   WspoL'pracuje z `Texture`, `CoordsBuffer`, `ShaderProgram`, `DrawCache`, `TextRender` i innymi komponentami graficznymi.
-   Jest uLLywana przez `DrawQueue` do wykonywania wszystkich operacji rysowania.

---
# z"" hardwarebuffer.cpp
## Opis ogolny

Plik `hardwarebuffer.cpp` zawiera implementacje klasy `HardwareBuffer`, ktora jest opakowaniem na bufory VBO (Vertex Buffer Object) w OpenGL.
## Klasa `HardwareBuffer`
## `HardwareBuffer::HardwareBuffer(Type type)`

Konstruktor.
-   **Parametr `type`**: OkreLla, czy ma to byc bufor na wierzchoL'ki (`VertexBuffer`) czy indeksy (`IndexBuffer`).
-   **DziaL'anie**:
    1.  Zapamietuje typ bufora.
    2.  WywoL'uje `glGenBuffers(1, &m_id)` w celu wygenerowania nowego, unikalnego ID dla bufora w kontekLcie OpenGL.
    3.  Sprawdza, czy operacja sie powiodL'a; w przeciwnym razie koL"czy aplikacje bL'edem krytycznym.
## `HardwareBuffer::~HardwareBuffer()`

Destruktor.
-   **DziaL'anie**:
    1.  Zwalnia zasob OpenGL w sposob bezpieczny watkowo.
    2.  Zamiast bezpoLrednio wywoL'ywac `glDeleteBuffers`, dodaje zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`). Gwarantuje to, LLe operacja usuniecia zostanie wykonana w watku, ktory ma aktywny kontekst OpenGL, nawet jeLli destruktor jest wywoL'ywany z innego watku.
## ZaleLLnoLci i powiazania

-   `framework/graphics/hardwarebuffer.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bL'edow OpenGL.
-   `framework/core/application.h`, `eventdispatcher.h`, `logger.h`: Do walidacji, planowania zdarzeL" i logowania.
-   Jest uLLywana przez `VertexArray` (w `coordsbuffer.h`) do przechowywania danych geometrycznych w pamieci karty graficznej, co znacznie przyspiesza renderowanie.

---
# z"" paintershaderprogram.cpp
## Opis ogolny

Plik `paintershaderprogram.cpp` zawiera implementacje klasy `PainterShaderProgram`, ktora jest specjalizacja `ShaderProgram`. Jest ona dostosowana do wspoL'pracy z klasa `Painter`, udostepniajac standardowy zestaw uniformow i atrybutow uLLywanych w procesie renderowania 2D.
## Klasa `PainterShaderProgram`
## `PainterShaderProgram::PainterShaderProgram(const std::string& name)`

Konstruktor. WywoL'uje konstruktor klasy bazowej i inicjalizuje dodatkowe zmienne, takie jak `m_startTime`, ktory jest uLLywany do animacji opartych na czasie w shaderach.
## `void PainterShaderProgram::setupUniforms()`
## Opis semantyczny
Wirtualna metoda, ktora po zlinkowaniu programu shadera wyszukuje lokalizacje standardowych uniformow (`u_TransformMatrix`, `u_ProjectionMatrix`, `u_Color`, `u_Tex0` itd.) i przypisuje im domyLlne wartoLci.
## `bool PainterShaderProgram::link()`

PrzesL'ania metode z `ShaderProgram`.
1.  Ustawia `m_startTime`.
2.  WiaLLe standardowe lokalizacje atrybutow (`VERTEX_ATTR`, `TEXCOORD_ATTR`, etc.) z ich nazwami w shaderze.
3.  WywoL'uje `ShaderProgram::link()`.
4.  JeLli linkowanie sie powiedzie, bindowanie program i wywoL'uje `setupUniforms()`.
## Metody `set...()`

Sa to metody do ustawiania wartoLci uniformow. KaLLda z nich:
1.  Sprawdza, czy nowa wartoLc roLLni sie od aktualnie przechowywanej, aby uniknac zbednych wywoL'aL" `glUniform...`.
2.  Bindowanie program shadera (`bind()`).
3.  Ustawia nowa wartoLc uniformu w OpenGL.
4.  Aktualizuje przechowywana wartoLc.

-   `setTransformMatrix`, `setProjectionMatrix`, `setTextureMatrix`: Ustawiaja macierze.
-   `setColor`: Ustawia gL'owny kolor.
-   `setMatrixColor`: Ustawia macierz kolorow (dla shadera strojow).
-   `setResolution`: Ustawia rozdzielczoLc (przydatne do efektow zaleLLnych od pikseli).
-   ... i inne.
## `void PainterShaderProgram::updateTime()`

Aktualizuje uniform `u_Time`, przekazujac do shadera czas, jaki upL'ynaL' od jego utworzenia. Pozwala to na tworzenie animowanych efektow w shaderach.
## `void PainterShaderProgram::addMultiTexture(...)` i `void PainterShaderProgram::bindMultiTextures()`

Metody do obsL'ugi dodatkowych tekstur (multi-texturing). `addMultiTexture` L'aduje teksture i dodaje ja do listy. `bindMultiTextures` aktywuje te tekstury na kolejnych jednostkach teksturujacych (od `GL_TEXTURE1` wzwyLL), aby mogL'y byc uLLywane w shaderze.
## ZaleLLnoLci i powiazania

-   `framework/graphics/paintershaderprogram.h`: Plik nagL'owkowy.
-   `framework/graphics/painter.h`: LsciLle wspoL'pracuje z `Painter`, ktory ustawia jej uniformy.
-   `framework/graphics/texture.h`, `texturemanager.h`: Do L'adowania i zarzadzania dodatkowymi teksturami.
-   `framework/core/clock.h`: Do Lledzenia czasu dla animacji.

---
# z"" paintershaderprogram.h
## Opis ogolny

Plik `paintershaderprogram.h` deklaruje klase `PainterShaderProgram`, ktora jest wyspecjalizowana wersja `ShaderProgram`, dostosowana do potrzeb `Painter`. Definiuje ona standardowy zestaw uniformow i atrybutow uLLywanych w shaderach 2D.
## Klasa `PainterShaderProgram`
## Opis semantyczny
`PainterShaderProgram` dziedziczy po `ShaderProgram` i dodaje do niej warstwe abstrakcji specyficzna dla `Painter`. Zamiast odwoL'ywac sie do uniformow po nazwach (stringach), udostepnia dedykowane metody `set...()`, ktore operuja na predefiniowanych, zbuforowanych lokalizacjach. Upraszcza to kod `Painter` i potencjalnie zwieksza wydajnoLc.
## Typy wyliczeniowe (Enums)

Definiuje staL'e dla lokalizacji standardowych atrybutow i uniformow, co pozwala na ich efektywne buforowanie.

-   **Atrybuty**: `VERTEX_ATTR`, `TEXCOORD_ATTR`, ...
-   **Uniformy**: `PROJECTION_MATRIX_UNIFORM`, `TEXTURE_MATRIX_UNIFORM`, `COLOR_UNIFORM`, `TEX0_UNIFORM`, ...
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PainterShaderProgram(...)`| Konstruktor. |
| `bool link()` | PrzesL'ania metode bazowa, aby dodatkowo zmapowac standardowe atrybuty i uniformy. |
| `setTransformMatrix(...)` | Ustawia macierz transformacji. |
| `setProjectionMatrix(...)`| Ustawia macierz projekcji. |
| `setTextureMatrix(...)` | Ustawia macierz tekstury. |
| `setColor(...)` | Ustawia gL'owny kolor. |
| `setMatrixColor(...)` | Ustawia macierz kolorow (dla shadera strojow). |
| `setDepth(...)` | Ustawia wartoLc gL'ebi. |
| `setResolution(...)` | Ustawia rozdzielczoLc renderowania. |
| `setOffset(...)` | Ustawia przesuniecie (offset). |
| `updateTime()` | Aktualizuje uniform czasu. |
| `addMultiTexture(...)` | Dodaje dodatkowa teksture do shadera. |
| `bindMultiTextures()` | Bindowanie wszystkie dodatkowe tekstury. |
| `clearMultiTextures()` | CzyLci liste dodatkowych tekstur. |
| `enableColorMatrix()` | WL'acza tryb macierzy kolorow (dla shadera strojow). |
## Zmienne prywatne

-   `m_startTime`: Czas utworzenia shadera.
-   `m_color`, `m_depth`, `m_transformMatrix`, ...: Przechowuja aktualne wartoLci uniformow, aby uniknac zbednych wywoL'aL" `glUniform...`.
-   `m_multiTextures`: Wektor dodatkowych tekstur.
-   `m_useColorMatrix`: Flaga wskazujaca, czy `u_Color` jest macierza 4x4.
## ZaleLLnoLci i powiazania

-   `framework/graphics/shaderprogram.h`: Klasa bazowa.
-   `framework/graphics/coordsbuffer.h`: PoLrednio, poprzez `Painter`.
-   Jest uLLywana przez `Painter` jako podstawa dla wszystkich operacji rysowania opartych na shaderach.

---
# z"" shader.cpp
## Opis ogolny

Plik `shader.cpp` zawiera implementacje klasy `Shader`, ktora jest opakowaniem na pojedynczy obiekt shadera w OpenGL (np. shader wierzchoL'kow lub shader fragmentow).
## Klasa `Shader`
## `Shader::Shader(Shader::ShaderType shaderType)`

Konstruktor.
-   **Parametr `shaderType`**: OkreLla, czy tworzony jest shader wierzchoL'kow (`Vertex`) czy fragmentow (`Fragment`).
-   **DziaL'anie**: WywoL'uje `glCreateShader` z odpowiednim typem, aby utworzyc obiekt shadera w sterowniku graficznym. W przypadku bL'edu, koL"czy aplikacje.
## `Shader::~Shader()`

Destruktor. Zwalnia zasob shadera w OpenGL, wywoL'ujac `glDeleteShader`.
## `bool Shader::compileSourceCode(const std::string& sourceCode)`
## Opis semantyczny
Kompiluje kod LsrodL'owy shadera.
## DziaL'anie
1.  Dla OpenGL ES, dodaje na poczatku kodu dyrektywe `precision highp float;`.
2.  Przekazuje kod LsrodL'owy do sterownika za pomoca `glShaderSource`.
3.  Kompiluje shader za pomoca `glCompileShader`.
4.  Sprawdza status kompilacji za pomoca `glGetShaderiv`.
5.  Zwraca `true` w przypadku sukcesu, `false` w przeciwnym razie.
## `bool Shader::compileSourceFile(const std::string& sourceFile)`

Laduje kod LsrodL'owy z pliku za pomoca `g_resources`, a nastepnie wywoL'uje `compileSourceCode`.
## `std::string Shader::log()`

Pobiera i zwraca logi kompilatora shadera (`glGetShaderInfoLog`), ktore zawieraja informacje o bL'edach lub ostrzeLLeniach.
## ZaleLLnoLci i powiazania

-   `framework/graphics/shader.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do dostepu do funkcji OpenGL.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   `framework/core/resourcemanager.h`: Do L'adowania shaderow z plikow.
-   Obiekty `Shader` sa tworzone i zarzadzane przez `ShaderProgram` (lub `PainterShaderProgram`), ktory nastepnie linkuje je w kompletny program shadera.

---
# z"" shadermanager.h
## Opis ogolny

Plik `shadermanager.h` deklaruje klase `ShaderManager`, ktora jest singletonem (`g_shaders`) odpowiedzialnym za zarzadzanie niestandardowymi programami shaderow tworzonymi w skryptach Lua.
## Klasa `ShaderManager`
## Opis semantyczny
`ShaderManager` dziaL'a jako repozytorium dla `PainterShaderProgram` tworzonych dynamicznie. Przechowuje je w mapie pod unikalnymi nazwami, co pozwala na ich poLsniejsze pobieranie i uLLywanie w trakcie renderowania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedLLera. |
| `void terminate()` | CzyLci i zwalnia wszystkie zaL'adowane shadery. |
| `void createShader(...)` | Tworzy, kompiluje i linkuje nowy `PainterShaderProgram` z podanego kodu LsrodL'owego (lub plikow). Zapisuje go pod dana nazwa. |
| `void createOutfitShader(...)` | Skrot do `createShader` z wL'aczona opcja macierzy kolorow, specjalnie dla shaderow strojow. |
| `void addTexture(...)` | Dodaje dodatkowa teksture do istniejacego programu shadera. |
| `PainterShaderProgramPtr getShader(...)` | Wyszukuje i zwraca wskaLsnik do programu shadera o podanej nazwie. |
## Zmienne prywatne

-   `m_shaders`: Mapa (`std::unordered_map`) przechowujaca wszystkie niestandardowe programy shaderow.
## Zmienne globalne

-   `g_shaders`: Globalna instancja `ShaderManager`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`, `paintershaderprogram.h`: Deklaracje klas shaderow.
-   Jest oznaczona jako `@bindsingleton g_shaders`, co udostepnia jej API (`createShader`, `addTexture`) w skryptach Lua.
-   Jest uLLywana przez `UIWidget` (w `uiwidgetimage.cpp`) do rysowania obrazow z niestandardowymi shaderami.
-   Wszystkie operacje tworzenia i modyfikacji shaderow sa delegowane do watku graficznego za pomoca `g_graphicsDispatcher`, aby zapewnic bezpieczeL"stwo watkowe.

---
# z"" shadermanager.cpp
## Opis ogolny

Plik `shadermanager.cpp` zawiera implementacje klasy `ShaderManager`, ktora zarzadza niestandardowymi programami shaderow.
## Zmienne globalne
## `g_shaders`

Globalna instancja `ShaderManager`.

ShaderManager g_shaders;
```
## Klasa `ShaderManager`
## `void ShaderManager::init()`

Inicjalizuje menedLLera. W obecnej implementacji wywoL'uje `PainterShaderProgram::release()`, aby upewnic sie, LLe LLaden shader nie jest aktywny.
## `void ShaderManager::terminate()`

CzyLci mape `m_shaders`, co powoduje zwolnienie wszystkich niestandardowych programow shaderow.
## `void ShaderManager::createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix)`
## Opis semantyczny
Tworzy nowy program shadera. Metoda jest asynchroniczna - dodaje zadanie do dyspozytora graficznego.
## DziaL'anie
1.  Sprawdza, czy podane stringi `vertex` i `fragment` sa kodem LsrodL'owym (zawieraja znak nowej linii) czy LcieLLkami do plikow.
2.  JeLli sa to LcieLLki, odczytuje zawartoLc plikow za pomoca `g_resources`.
3.  Dodaje do `g_graphicsDispatcher` zadanie (lambda), ktore:
    -   WywoL'uje `PainterShaderProgram::create` w celu skompilowania i zlinkowania shadera.
    -   JeLli operacja sie powiedzie, dodaje nowo utworzony program do mapy `m_shaders`.
## `void ShaderManager::addTexture(const std::string& name, const std::string& file)`

Dodaje dodatkowa teksture do istniejacego shadera. Podobnie jak `createShader`, operacja jest wykonywana asynchronicznie w watku graficznym.
## `PainterShaderProgramPtr ShaderManager::getShader(const std::string& name)`

Wyszukuje i zwraca program shadera o podanej nazwie. Ta metoda musi byc wywoL'ywana z watku graficznego, co jest zapewnione przez `VALIDATE_GRAPHICS_THREAD()`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/shadermanager.h`: Plik nagL'owkowy.
-   `framework/graphics/paintershaderprogram.h`: Do tworzenia obiektow shaderow.
-   `framework/core/resourcemanager.h`: Do L'adowania kodu shaderow z plikow.
-   `framework/core/eventdispatcher.h`: Do zapewnienia, LLe operacje na OpenGL sa wykonywane w watku graficznym.

---
# z"" shader.h
## Opis ogolny

Plik `shader.h` deklaruje klase `Shader`, ktora reprezentuje pojedynczy, skompilowany obiekt shadera w OpenGL (np. shader wierzchoL'kow lub fragmentow), ale jeszcze nie zlinkowany w peL'ny program.
## Klasa `Shader`
## Opis semantyczny
`Shader` jest niskopoziomowym opakowaniem na ID obiektu shadera w OpenGL. Jego gL'ownym zadaniem jest przyjecie kodu LsrodL'owego, skompilowanie go i przechowanie wyniku. Obiekty tej klasy sa nastepnie L'aczone w `ShaderProgram`.
## Typ wyliczeniowy `ShaderType`

-   `Vertex`: Oznacza shader wierzchoL'kow (`GL_VERTEX_SHADER`).
-   `Fragment`: Oznacza shader fragmentow/pikseli (`GL_FRAGMENT_SHADER`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Shader(ShaderType shaderType)` | Konstruktor, tworzy obiekt shadera w OpenGL. |
| `~Shader()` | Destruktor, zwalnia obiekt shadera. |
| `bool compileSourceCode(...)` | Kompiluje shader z podanego kodu LsrodL'owego. |
| `bool compileSourceFile(...)` | Laduje kod z pliku i go kompiluje. |
| `std::string log()` | Zwraca logi kompilatora shadera. |
| `uint getShaderId()` | Zwraca ID obiektu shadera w OpenGL. |
| `ShaderType getShaderType()` | Zwraca typ shadera. |
## Zmienne prywatne

-   `m_shaderId`: ID obiektu shadera w OpenGL.
-   `m_shaderType`: Typ shadera.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   Jest tworzona i uLLywana przez `ShaderProgram` w procesie budowania kompletnego programu shadera.

---
# z"" textrender.cpp
## Opis ogolny

Plik `textrender.cpp` implementuje klase `TextRender`, ktora jest systemem do optymalizacji renderowania tekstu. DziaL'a jako globalny cache dla geometrii tekstu, aby uniknac ponownego obliczania pozycji glifow w kaLLdej klatce dla tekstow, ktore sie nie zmieniaja.
## Zmienne globalne
## `g_text`

Globalna instancja `TextRender`.

TextRender g_text;
```
## Klasa `TextRender`
## Opis semantyczny
`TextRender` przechowuje mape (`m_cache`), w ktorej kluczem jest hash wygenerowany na podstawie treLci tekstu, jego rozmiaru, wyrownania i fontu. WartoLcia jest obiekt `TextRenderCache`, ktory przechowuje `CoordsBuffer` z gotowa geometria tekstu. Przy pierwszym LLadaniu narysowania danego tekstu, geometria jest obliczana i zapisywana w cache. Przy kolejnych LLadaniach, uLLywana jest juLL istniejaca geometria. System posiada rownieLL mechanizm czyszczenia nieuLLywanych wpisow z cache.
## `void TextRender::init()` i `void TextRender::terminate()`

Metody inicjalizujace i zwalniajace cache.
## `void TextRender::poll()`

Metoda wywoL'ywana okresowo. Jej zadaniem jest czyszczenie cache z wpisow, ktore nie byL'y uLLywane od pewnego czasu. Implementuje prosty mechanizm LRU (Least Recently Used) oparty na czasie ostatniego uLLycia (`lastUse`).
## `uint64_t TextRender::addText(...)`

Generuje unikalny hash dla kombinacji (font, tekst, rozmiar, wyrownanie) i tworzy dla niego wpis w cache, jeLli jeszcze nie istnieje. Zwraca wygenerowany hash.
## `void TextRender::drawText(...)`

Wysokopoziomowa metoda do rysowania tekstu. Najpierw wywoL'uje `addText`, aby uzyskac/stworzyc wpis w cache, a nastepnie wywoL'uje druga wersje `drawText` z hashem.
## `void TextRender::drawText(const Point& pos, uint64_t hash, ...)`

GL'owna metoda rysujaca.
1.  Znajduje wpis w cache na podstawie hasha.
2.  JeLli wpis jest nowy (`it->font` nie jest `nullptr`), wywoL'uje `font->calculateDrawTextCoords`, aby wygenerowac geometrie, keszuje ja w `CoordsBuffer` (`it->coords.cache()`) i zwalnia referencje do fontu i tekstu, aby oszczedzac pamiec.
3.  WywoL'uje `g_painter->drawText`, przekazujac mu gotowy `CoordsBuffer` z geometria.
4.  ObsL'uguje rownieLL rysowanie cienia.
## `void TextRender::drawColoredText(...)`

DziaL'a analogicznie do `drawText`, ale wywoL'uje `g_painter->drawText` w wersji dla tekstu wielokolorowego.
## ZaleLLnoLci i powiazania

-   `framework/graphics/textrender.h`: Plik nagL'owkowy.
-   `framework/graphics/painter.h`: ULLywa `g_painter` do finalnego rysowania.
-   `framework/core/eventdispatcher.h`: Do walidacji watku.
-   Jest uLLywana przez `DrawQueueItemText` do renderowania tekstu.

---
# z"" shaderprogram.cpp
## Opis ogolny

Plik `shaderprogram.cpp` zawiera implementacje klasy `ShaderProgram`, ktora jest podstawowym obiektem do zarzadzania programami shaderow w OpenGL.
## Zmienne globalne
## `uint ShaderProgram::m_currentProgram`

Statyczna zmienna czL'onkowska, ktora przechowuje ID aktualnie aktywnego (zbindowanego) programu shadera. SL'uLLy do unikania zbednych wywoL'aL" `glUseProgram`, jeLli ten sam program jest juLL aktywny.
## Klasa `ShaderProgram`
## `ShaderProgram::ShaderProgram(const std::string& name)`

Konstruktor. Inicjalizuje nazwe, ustawia flage `m_linked` na `false` i tworzy nowy, pusty obiekt programu shadera w OpenGL za pomoca `glCreateProgram()`.
## `ShaderProgram::~ShaderProgram()`

Destruktor. Zwalnia zasob programu shadera, wywoL'ujac `glDeleteProgram()`.
## `PainterShaderProgramPtr ShaderProgram::create(...)`

Statyczna metoda fabryczna, ktora tworzy i konfiguruje `PainterShaderProgram`. Jest to gL'owny sposob tworzenia shaderow w tym frameworku.
## DziaL'anie
1.  Tworzy nowy obiekt `PainterShaderProgram`.
2.  Dodaje i kompiluje shadery wierzchoL'kow i fragmentow.
3.  Opcjonalnie wL'acza tryb macierzy kolorow.
4.  Linkuje program.
5.  W przypadku bL'edow kompilacji lub linkowania, loguje szczegoL'owe informacje i zwraca `nullptr`.
## `bool ShaderProgram::addShader(...)`

DoL'acza wczeLniej skompilowany obiekt `Shader` do programu za pomoca `glAttachShader`.
## `bool ShaderProgram::addShaderFromSourceCode(...)` i `addShaderFromSourceFile(...)`

Metody pomocnicze, ktore tworza obiekt `Shader`, kompiluja go z kodu LsrodL'owego lub pliku, a nastepnie dodaja do programu.
## `bool ShaderProgram::link()`
## Opis semantyczny
Linkuje wszystkie doL'aczone shadery w jeden wykonywalny program.
## DziaL'anie
1.  WywoL'uje `glLinkProgram()`.
2.  Sprawdza status linkowania za pomoca `glGetProgramiv`.
3.  JeLli wystapi bL'ad, pobiera i loguje szczegoL'owy komunikat bL'edu z `glGetProgramInfoLog`.
4.  Zwraca `true` w przypadku sukcesu.
## `bool ShaderProgram::bind()`

Aktywuje program shadera w potoku renderowania OpenGL za pomoca `glUseProgram`. Dzieki `m_currentProgram`, faktyczne wywoL'anie `glUseProgram` nastepuje tylko wtedy, gdy zmieniany jest program.
## `void ShaderProgram::release()`

Deaktywuje jakikolwiek aktywny program shadera (`glUseProgram(0)`).
## Metody `...Location(...)` i `set...Value(...)`

Implementuja interfejs do pracy z atrybutami i uniformami w shaderze, opakowujac odpowiednie funkcje OpenGL (`glGetAttribLocation`, `glBindAttribLocation`, `glGetUniformLocation`, `glUniform...`, `glVertexAttrib...`).
## ZaleLLnoLci i powiazania

-   `framework/graphics/shaderprogram.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bL'edow i dostepu do informacji o sterowniku.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasa bazowa dla `PainterShaderProgram`.
-   Jest zarzadzana przez `ShaderManager`.

---
# z"" texture.cpp
## Opis ogolny

Plik `texture.cpp` zawiera implementacje klasy `Texture`, ktora jest obiektowym opakowaniem na teksture w OpenGL. Odpowiada za tworzenie, L'adowanie danych, ustawianie parametrow i zwalnianie zasobow tekstury w pamieci karty graficznej.
## Zmienne globalne
## `uint Texture::uniqueId`

Statyczny licznik uLLywany do przypisywania unikalnego ID kaLLdej nowo utworzonej teksturze. Jest to przydatne do szybkiego porownywania tekstur.
## Klasa `Texture`
## `Texture::Texture(...)`

Konstruktory.
-   **`Texture(const Size& size, ...)`**: Tworzy pusta teksture o podanych wymiarach.
-   **`Texture(const ImagePtr& image, ...)`**: Tworzy teksture na podstawie obiektu `Image`.
-   **DziaL'anie**: Inicjalizuja pola, przypisuja unikalne ID i zwiekszaja globalny licznik tekstur w `g_stats`.
## `Texture::~Texture()`

Destruktor. Dodaje zadanie usuniecia tekstury z pamieci GPU do kolejki dyspozytora graficznego (`g_graphicsDispatcher`), co zapewnia bezpieczeL"stwo watkowe. Zmniejsza globalny licznik tekstur.
## `void Texture::replace(const ImagePtr& image)`

Zastepuje zawartoLc tekstury nowym obrazem. Stara tekstura w OpenGL jest zwalniana, a nowa zostanie utworzona przy nastepnym wywoL'aniu `update()`.
## `void Texture::resize(const Size& size)`

Zmienia rozmiar istniejacej tekstury, ponownie alokujac dla niej pamiec w GPU za pomoca `glTexImage2D` z `nullptr` jako danymi pikseli.
## `void Texture::update()`
## Opis semantyczny
Kluczowa metoda, ktora dba o to, aby obiekt tekstury w OpenGL byL' poprawnie zainicjalizowany i skonfigurowany. Musi byc wywoL'ywana przed pierwszym uLLyciem tekstury.
## DziaL'anie
1.  **JeLli tekstura nie istnieje (`m_id == 0`)**:
    -   Generuje nowe ID tekstury (`glGenTextures`).
    -   Bindowanie teksture.
    -   JeLli `m_image` istnieje, przesyL'a jego dane pikseli do GPU za pomoca `setupPixels`, generujac mipmapy, jeLli to wymagane. Nastepnie zwalnia `m_image`, aby oszczedzac RAM.
    -   JeLli nie ma obrazu, tworzy pusta teksture.
2.  **JeLli `m_needsUpdate` jest `true`**:
    -   Bindowanie teksture.
    -   Ustawia parametry zawijania (`setupWrap`).
    -   Ustawia parametry filtrowania (`setupFilters`).
    -   Aktualizuje macierz transformacji (`setupTranformMatrix`).
    -   Resetuje flage `m_needsUpdate`.
## `void Texture::setSmooth(bool smooth)` i `void Texture::setRepeat(bool repeat)`

Ustawiaja flagi, ktore zostana zastosowane do parametrow tekstury (`GL_TEXTURE_MIN/MAG_FILTER`, `GL_TEXTURE_WRAP_S/T`) podczas nastepnego wywoL'ania `update()`.
## Metody `setup...()`

Prywatne metody pomocnicze, ktore wywoL'uja odpowiednie funkcje OpenGL do konfiguracji tekstury:
-   `setupSize()`: Sprawdza, czy rozmiar nie przekracza limitow GPU.
-   `setupWrap()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_WRAP_S/T`.
-   `setupFilters()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_MIN/MAG_FILTER`.
-   `setupTranformMatrix()`: Oblicza macierz do transformacji wspoL'rzednych tekstury (np. w celu odwrocenia jej w osi Y).
-   `setupPixels()`: WywoL'uje `glTexImage2D` do przesL'ania danych pikseli.
## ZaleLLnoLci i powiazania

-   `framework/graphics/texture.h`: Plik nagL'owkowy.
-   `framework/graphics/graphics.h`: Do operacji OpenGL i sprawdzania limitow.
-   `framework/graphics/image.h`: ULLywana jako LsrodL'o danych pikseli.
-   Jest klasa bazowa dla `AnimatedTexture`.
-   Jest tworzona i zarzadzana przez `TextureManager`.

---
# z"" texture.h
## Opis ogolny

Plik `texture.h` deklaruje klase `Texture`, ktora jest obiektowym interfejsem do zarzadzania teksturami w OpenGL.
## Klasa `Texture`
## Opis semantyczny
`Texture` enkapsuluje ID tekstury w OpenGL oraz jej wL'aLciwoLci, takie jak rozmiar, wygL'adzanie (filtrowanie), powtarzanie (wrapping) i mipmapy. Dostarcza metody do tworzenia tekstury z obiektu `Image` lub jako pustej tekstury (np. dla bufora ramki). Metoda `update()` jest kluczowa i synchronizuje stan obiektu C++ z rzeczywistym stanem tekstury w pamieci GPU.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Texture(...)` | Konstruktory. |
| `virtual ~Texture()` | Destruktor. |
| `virtual void replace(...)` | Zastepuje zawartoLc tekstury nowym obrazem. |
| `void resize(...)` | Zmienia rozmiar tekstury. |
| `virtual void update()` | Tworzy lub aktualizuje parametry tekstury w OpenGL. |
| `virtual void setUpsideDown(...)` | Ustawia, czy tekstura ma byc odwrocona. |
| `virtual void setSmooth(...)` | Ustawia wygL'adzanie (filtrowanie liniowe/najbliLLszego sasiada). |
| `virtual void setRepeat(...)` | Ustawia tryb powtarzania. |
| `virtual bool buildHardwareMipmaps()` | WL'acza generowanie mipmap przez GPU. |
| `uint getId()` | Zwraca ID tekstury w OpenGL. |
| `uint getUniqueId()` | Zwraca unikalne ID obiektu w aplikacji. |
| `const Size& getSize()` | Zwraca rozmiar tekstury. |
| `const Matrix3& getTransformMatrix()` | Zwraca macierz transformacji dla wspoL'rzednych tekstury. |
| `bool isEmpty()` | Sprawdza, czy tekstura jest pusta. |
| `bool canCache()` | Zwraca `true`, jeLli teksture moLLna umieLcic w atlasie. |
| `virtual bool isAnimatedTexture()` | Zwraca `false` (przesL'aniane przez `AnimatedTexture`). |
## Zmienne chronione

-   `m_id`: ID tekstury w OpenGL.
-   `m_uniqueId`: Unikalne ID w aplikacji.
-   `m_size`: Rozmiar tekstury.
-   `m_transformMatrix`: Macierz transformacji.
-   `m_hasMipmaps`, `m_smooth`, `m_upsideDown`, `m_repeat`, ...: Flagi stanu.
-   `m_image`: WskaLsnik na `Image`, uLLywany tylko podczas tworzenia tekstury.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Definicje typow, np. `ImagePtr`.
-   Jest klasa bazowa dla `AnimatedTexture`.
-   Jest tworzona i zarzadzana przez `TextureManager`.
-   Jest uLLywana przez `Painter`, `FrameBuffer`, `UIWidget` i inne komponenty do rysowania.

---
# z"" texturemanager.cpp
## Opis ogolny

Plik `texturemanager.cpp` zawiera implementacje klasy `TextureManager`, ktora jest singletonem (`g_textures`) odpowiedzialnym za zarzadzanie teksturami w aplikacji. DziaL'a jako cache, aby zapobiec wielokrotnemu L'adowaniu tych samych tekstur z dysku.
## Zmienne globalne
## `g_textures`

Globalna instancja `TextureManager`.

TextureManager g_textures;
```
## Klasa `TextureManager`
## `void TextureManager::init()` i `void TextureManager::terminate()`

Metody do inicjalizacji i zwalniania menedLLera. `terminate()` czyLci wszystkie zbuforowane tekstury.
## `void TextureManager::clearCache()`

CzyLci wszystkie zbuforowane tekstury, w tym animowane.
## `void TextureManager::reload()`

PrzeL'adowuje wszystkie zaL'adowane tekstury z ich oryginalnych plikow. Jest to przydatne do "hot-reloading" zasobow.
## `TexturePtr TextureManager::getTexture(const std::string& fileName)`
## Opis semantyczny
GL'owna metoda do pobierania tekstury. DziaL'a jak "get-or-load".
## DziaL'anie
1.  Sprawdza, czy tekstura o podanej nazwie (`fileName`) jest juLL w cache (`m_textures`). JeLli tak, zwraca ja.
2.  JeLli nie, rozwiazuje peL'na LcieLLke do pliku za pomoca `g_resources`.
3.  Ponownie sprawdza cache, tym razem z peL'na LcieLLka.
4.  JeLli tekstury wciaLL nie ma, probuje ja zaL'adowac z pliku:
    -   Odczytuje plik do strumienia w pamieci.
    -   WywoL'uje `loadTexture()`, aby sparsowac dane (APNG) i utworzyc obiekt `Texture` lub `AnimatedTexture`.
5.  JeLli L'adowanie sie powiedzie, dodaje nowa teksture do cache pod obiema nazwami (oryginalna i peL'na LcieLLka) i zwraca ja.
6.  W przypadku bL'edu, loguje go i zwraca `nullptr`.
## `TexturePtr TextureManager::loadTexture(std::stringstream& file, const std::string& source)`

Metoda pomocnicza, ktora parsuje strumieL" danych APNG za pomoca `load_apng`.
-   JeLli plik zawiera jedna klatke, tworzy `Texture`.
-   JeLli plik zawiera wiele klatek, tworzy `AnimatedTexture`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/texturemanager.h`: Plik nagL'owkowy.
-   `framework/graphics/animatedtexture.h`, `image.h`: Do tworzenia obiektow tekstur.
-   `framework/core/resourcemanager.h`: Do odczytywania plikow tekstur.
-   `framework/graphics/apngloader.h`: Do parsowania formatu APNG.
-   Jest uLLywana przez `UIWidget`, `BitmapFont` i inne komponenty, ktore potrzebuja wyLwietlac obrazy.

---
# z"" vertexarray.h
## Opis ogolny

Plik `vertexarray.h` deklaruje klase `VertexArray`, ktora jest prostym, dynamicznym buforem na wspoL'rzedne wierzchoL'kow (`float`). SL'uLLy do gromadzenia geometrii przed wysL'aniem jej do renderowania.
## Klasa `VertexArray`
## Opis semantyczny
`VertexArray` to opakowanie na `DataBuffer<float>`, zoptymalizowane do przechowywania par wspoL'rzednych (X, Y). Udostepnia metody do dodawania popularnych prymitywow 2D (trojkaty, prostokaty) i moLLe opcjonalnie przenieLc swoje dane do sprzetowego bufora VBO (`HardwareBuffer`) w celu zwiekszenia wydajnoLci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `VertexArray()` | Konstruktor. |
| `~VertexArray()` | Destruktor, zwalnia `m_hardwareBuffer`. |
| `VertexArray(VertexArray& c)` | Konstruktor kopiujacy (kopiuje tylko dane z `m_buffer`, nie `m_hardwareBuffer`). |
| `void addVertex(float x, float y)` | Dodaje pojedynczy wierzchoL'ek. |
| `void addTriangle(...)` | Dodaje trzy wierzchoL'ki tworzace trojkat. |
| `void addRect(...)` | Dodaje szeLc wierzchoL'kow tworzacych dwa trojkaty (prostokat). |
| `void addQuad(...)` | Dodaje cztery wierzchoL'ki tworzace czworokat (dla `TriangleStrip`). |
| `void clear()` | CzyLci bufor. |
| `float *vertices() const` | Zwraca wskaLsnik na surowe dane. |
| `int vertexCount() const` | Zwraca liczbe wierzchoL'kow. |
| `void cache()` | Kopiuje dane z bufora RAM do bufora VBO na karcie graficznej. |
| `bool isCached()` | Zwraca `true`, jeLli dane zostaL'y skopiowane do VBO. |
| `HardwareBuffer* getHardwareCache()` | Zwraca wskaLsnik na obiekt `HardwareBuffer`. |
## Zmienne prywatne

-   `m_buffer`: Bufor `DataBuffer<float>` przechowujacy wspoL'rzedne.
-   `m_hardwareBuffer`: WskaLsnik na opcjonalny bufor VBO.
## ZaleLLnoLci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/hardwarebuffer.h`: Do sprzetowego keszowania.
-   `framework/util/databuffer.h`: ULLywana jako wewnetrzny kontener.
-   Jest podstawowym skL'adnikiem `CoordsBuffer`, ktory uLLywa dwoch instancji `VertexArray` (jednej na pozycje, drugiej na wspoL'rzedne tekstur).

---
# z"" texturemanager.h
## Opis ogolny

Plik `texturemanager.h` deklaruje klase `TextureManager`, ktora jest singletonem (`g_textures`) odpowiedzialnym za zarzadzanie (L'adowanie, cachowanie, zwalnianie) teksturami w aplikacji.
## Klasa `TextureManager`
## Opis semantyczny
`TextureManager` dziaL'a jako centralne repozytorium tekstur. Gdy jakaL czeLc kodu prosi o teksture z pliku, menedLLer najpierw sprawdza, czy nie zostaL'a ona juLL zaL'adowana. JeLli tak, zwraca istniejaca instancje. JeLli nie, L'aduje ja z dysku, zapisuje w swojej pamieci podrecznej (cache) i zwraca. Zapobiega to wielokrotnemu L'adowaniu tych samych zasobow i marnowaniu pamieci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedLLera. |
| `void terminate()` | Zwalnia wszystkie zaL'adowane tekstury. |
| `void clearCache()` | CzyLci pamiec podreczna tekstur. |
| `void reload()` | PrzeL'adowuje wszystkie tekstury z plikow, umoLLliwiajac "hot-reloading". |
| `void preload(const std::string& fileName)` | Skrot do `getTexture`, ktory L'aduje teksture do cache, ale nie zwraca jej. |
| `TexturePtr getTexture(const std::string& fileName)` | Pobiera teksture. JeLli nie ma jej w cache, L'aduje ja. |
| `TexturePtr loadTexture(...)` | Niskopoziomowa metoda do tworzenia tekstury ze strumienia danych. |
## Zmienne prywatne

-   `m_textures`: Mapa (`std::unordered_map`) przechowujaca zaL'adowane tekstury, gdzie kluczem jest nazwa pliku.
-   `m_animatedTextures`: Wektor przechowujacy wskaLsniki do animowanych tekstur, prawdopodobnie w celu ich aktualizacji.
-   `m_liveReloadEvent`: WskaLsnik na zdarzenie, prawdopodobnie do implementacji "live reload".
## ZaleLLnoLci i powiazania

-   `framework/graphics/texture.h`: Definicja `Texture`.
-   `framework/core/declarations.h`: Deklaracje `ScheduledEventPtr`.
-   Jest to kluczowy menedLLer w systemie graficznym, uLLywany przez wszystkie komponenty, ktore musza wyLwietlac obrazy, takie jak `UIWidget` czy `BitmapFont`.

---
# z"" textrender.h
## Opis ogolny

Plik `textrender.h` deklaruje klase `TextRender`, ktora jest systemem do optymalizacji renderowania tekstu. DziaL'a jako globalny cache dla geometrii tekstu.
## Struktura `TextRenderCache`

Przechowuje wszystkie informacje potrzebne do narysowania tekstu, w tym gotowy `CoordsBuffer` z geometria.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `font` | `BitmapFontPtr` | Font uLLyty do wygenerowania geometrii (zwalniany po pierwszym uLLyciu). |
| `text` | `std::string` | Tekst (zwalniany po pierwszym uLLyciu). |
| `size` | `Size` | Rozmiar obszaru, w ktorym tekst ma byc rysowany. |
| `align` | `Fw::AlignmentFlag` | Wyrownanie tekstu. |
| `texture` | `TexturePtr` | Tekstura fontu. |
| `coords` | `CoordsBuffer` | Zbuforowana geometria tekstu. |
| `lastUse` | `ticks_t` | Czas ostatniego uLLycia (do czyszczenia cache). |
## Klasa `TextRender`
## Opis semantyczny
`TextRender` minimalizuje narzut na CPU zwiazany z obliczaniem pozycji poszczegolnych glifow dla czesto wyLwietlanych tekstow. Zamiast przeliczac geometrie w kaLLdej klatce, robi to tylko raz, a nastepnie przechowuje wynik w cache.
## StaL'e

-   `INDEXES`: Liczba "kubeL'kow" w hash mapie. ULLycie wielu map z osobnymi mutexami ma na celu zmniejszenie rywalizacji o zasoby w Lrodowisku wielowatkowym.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` / `terminate()` | Inicjalizuje i zwalnia system. |
| `void poll()` | CzyLci cache z nieuLLywanych wpisow. |
| `uint64_t addText(...)` | Generuje hash dla tekstu i tworzy dla niego wpis w cache. |
| `void drawText(...)` | Rysuje tekst, uLLywajac skeszowanej geometrii. |
| `void drawColoredText(...)` | Rysuje tekst wielokolorowy. |
## Zmienne prywatne

-   `m_cache[INDEXES]`: Tablica map, ktora przechowuje skeszowane dane.
-   `m_mutex[INDEXES]`: Tablica mutexow, po jednym dla kaLLdej mapy w `m_cache`.
## Zmienne globalne

-   `g_text`: Globalna instancja `TextRender`.
## ZaleLLnoLci i powiazania

-   `framework/graphics/bitmapfont.h`, `coordsbuffer.h`: Kluczowe struktury danych.
-   `framework/core/clock.h`: Do Lledzenia czasu ostatniego uLLycia.
-   Jest uLLywana przez `DrawQueueItemText` do renderowania tekstu w zoptymalizowany sposob.

---
# z"" outfits.h
## Opis ogolny

Plik `outfits.h` zawiera kod LsrodL'owy shaderow w postaci staL'ych stringow, ktore sa uLLywane do renderowania strojow postaci z niestandardowymi kolorami.
## Shadery
## `glslAdvancedOutfitVertexShader`
## Opis
Shader wierzchoL'kow dla zaawansowanego renderowania strojow.
## DziaL'anie
1.  **Atrybuty**: Przyjmuje pozycje wierzchoL'ka (`a_Vertex`) i jego wspoL'rzedne na teksturze (`a_TexCoord`).
2.  **Uniformy**:
    -   `u_ProjectionMatrix`, `u_TransformMatrix`: Standardowe macierze do transformacji pozycji.
    -   `u_TextureMatrix`: Do transformacji wspoL'rzednych tekstury.
    -   `u_Offset`, `u_Resolution`: Dodatkowe dane, prawdopodobnie do efektow.
3.  **Varying**:
    -   Przekazuje do shadera fragmentow trzy zestawy wspoL'rzednych tekstury:
        -   `v_TexCoord`: Podstawowe.
        -   `v_TexCoord2`: Przesuniete o `u_Offset`.
        -   `v_TexCoord3`: WspoL'rzedne oparte na rozdzielczoLci.
4.  Oblicza finalna pozycje wierzchoL'ka na ekranie (`gl_Position`).
## `glslAdvancedOutfitFragmentShader`
## Opis
Shader fragmentow (pikseli) dla zaawansowanego renderowania strojow.
## DziaL'anie
1.  Pobiera kolor piksela z gL'ownej tekstury (`u_Tex0`) na podstawie `v_TexCoord`.
2.  Sprawdza kolor piksela z tej samej tekstury, ale w przesunietym miejscu (`v_TexCoord2`). JeLli alfa tego piksela jest wieksza od progu, mnoLLy finalny kolor przez LLoL'ty (`vec4(1.0, 1.0, 0.0, 1.0)`), tworzac efekt podLwietlenia lub konturu.
3.  Odrzuca piksel (`discard`), jeLli jego alfa jest zbyt niska.

> **NOTE**: Kod shaderow w tym pliku wydaje sie byc eksperymentalny lub nie w peL'ni zaimplementowany w reszcie kodu. Prawdziwy shader do strojow znajduje sie w `shadersources.h`.
## ZaleLLnoLci i powiazania

-   Jest doL'aczany przez `shaders.h`.
-   Kod jest przeznaczony do uLLycia przez `PainterShaderProgram`.

---
# z"" newshader.h
## Opis ogolny

Plik `newshader.h` zawiera kod LsrodL'owy dla nowego, zoptymalizowanego systemu renderowania opartego na `DrawCache`. Definiuje shadery wierzchoL'kow i fragmentow do rysowania geometrii wsadowej, tekstu i linii.
## Shadery
## `newVertexShader`
## Opis
Shader wierzchoL'kow dla `DrawCache`.
## DziaL'anie
1.  **Atrybuty**: Przyjmuje pozycje (`a_Vertex`), wspoL'rzedne tekstury (`a_TexCoord`) i **kolor (`a_Color`)** dla kaLLdego wierzchoL'ka.
2.  **Varying**: Przekazuje wspoL'rzedne tekstury i kolor do shadera fragmentow.
3.  Oblicza pozycje wierzchoL'ka.
## `newFragmentShader`
## Opis
Shader fragmentow dla `DrawCache`.
## DziaL'anie
1.  Sprawdza, czy wspoL'rzedna X tekstury jest mniejsza od 0. JeLli tak, oznacza to, LLe wierzchoL'ek nie ma tekstury i jego kolorem jest po prostu `v_Color`.
2.  W przeciwnym razie, pobiera kolor z tekstury atlasu (`u_Atlas`) i mnoLLy go przez kolor wierzchoL'ka (`v_Color`).
## `textVertexShader` i `textFragmentShader`

Shadery zoptymalizowane do rysowania tekstu. WierzchoL'ki sa przesuwane o `u_Offset` (pozycja tekstu na ekranie), a kolor jest jednolity dla caL'ego tekstu (`u_Color`).
## `lineVertexShader` i `lineFragmentShader`

Proste shadery do rysowania linii. Shader fragmentow po prostu ustawia jednolity kolor `u_Color`.
## ZaleLLnoLci i powiazania

-   Jest doL'aczany przez `shaders.h`.
-   Shadery te sa kompilowane i uLLywane przez `Painter` do implementacji `drawCache`, `drawText` i `drawLine`.

---
# z"" shaders.h
## Opis ogolny

Plik `shaders.h` jest plikiem nagL'owkowym, ktory agreguje wszystkie pliki zawierajace kod LsrodL'owy shaderow. SL'uLLy jako pojedynczy punkt doL'aczania dla wszystkich predefiniowanych shaderow w systemie.
## ZawartoLc

DoL'acza nastepujace pliki:
-   `newshader.h`: Zawiera shadery dla nowego, wsadowego systemu renderowania (`DrawCache`).
-   `shadersources.h`: Zawiera kod LsrodL'owy dla standardowych shaderow uLLywanych przez `Painter` (rysowanie tekstur, jednolitych kolorow, strojow).
-   `outfits.h`: Zawiera eksperymentalne/alternatywne shadery do strojow.
## ZaleLLnoLci i powiazania

-   Jest doL'aczany przez `painter.cpp` w celu uzyskania dostepu do kodu LsrodL'owego shaderow, ktore sa kompilowane podczas inicjalizacji `Painter`.

---
# z"" shadersources.h
## Opis ogolny

Plik `shadersources.h` zawiera kod LsrodL'owy w GLSL dla standardowych shaderow uLLywanych przez klase `Painter`. Sa one zdefiniowane jako staL'e stringi i kompilowane w trakcie dziaL'ania programu.
## Shadery
## `glslMainVertexShader` i `glslMainWithTexCoordsVertexShader`

Sa to "szablony" dla shaderow wierzchoL'kow. Definiuja one funkcje `main`, ktora wywoL'uje `calculatePosition()`. Wersja `WithTexCoords` dodatkowo przekazuje wspoL'rzedne tekstury do shadera fragmentow.
## `glslPositionOnlyVertexShader`

Jest to implementacja `calculatePosition()`. Oblicza ona finalna pozycje wierzchoL'ka, mnoLLac jego pozycje przez macierze transformacji i projekcji. Uwzglednia rownieLL gL'ebie (`u_Depth`).
## `glslMainFragmentShader`

Szablon dla shaderow fragmentow. WywoL'uje `calculatePixel()` i odrzuca piksele o niskiej wartoLci alfa, jeLli `u_Depth > 0`.
## `glslTextureSrcFragmentShader`

Implementacja `calculatePixel()`, ktora pobiera kolor z tekstury (`u_Tex0`) i mnoLLy go przez jednolity kolor (`u_Color`).
## `glslSolidColorFragmentShader`

Implementacja `calculatePixel()`, ktora zwraca jednolity kolor (`u_Color`).
## `glslSolidColorOnTextureFragmentShader`

Implementacja `calculatePixel()`, ktora rysuje jednolity kolor (`u_Color`) tylko tam, gdzie tekstura (`u_Tex0`) nie jest w peL'ni przezroczysta.
## `glslOutfitVertexShader` i `glslOutfitFragmentShader`

Shadery do renderowania strojow.
-   **Shader wierzchoL'kow**: Przekazuje dwie pary wspoL'rzednych tekstury - normalne (`v_TexCoord`) i przesuniete o `u_Offset` (`v_TexCoord2`).
-   **Shader fragmentow**:
    1.  Pobiera kolor bazowy z `v_TexCoord`.
    2.  Pobiera kolor "maski" z `v_TexCoord2`.
    3.  Na podstawie koloru maski (sprawdzajac, ktory kanaL' R, G lub B jest dominujacy), mnoLLy kolor bazowy przez jeden z czterech kolorow przekazanych w macierzy `u_Color`. Pozwala to na dynamiczne kolorowanie roLLnych czeLci stroju.
## ZaleLLnoLci i powiazania

-   Jest doL'aczany przez `shaders.h`.
-   Kod jest uLLywany w `painter.cpp` do tworzenia domyLlnych programow shaderow.

---
# z"" http.cpp
## Opis ogolny

Plik `http.cpp` implementuje klase `Http`, ktora jest singletonem (`g_http`) odpowiedzialnym za obsL'uge zapytaL" HTTP/HTTPS oraz poL'aczeL" WebSocket. DziaL'a asynchronicznie, wykorzystujac biblioteke Boost.Asio do operacji sieciowych w osobnym watku.
## Zmienne globalne
## `g_http`

Globalna instancja `Http`.
## Klasa `Http`
## `void Http::init()`

Inicjalizuje menedLLera. Tworzy i uruchamia osobny watek, w ktorym bedzie dziaL'ac `boost::asio::io_service` (`m_ios`), obsL'ugujac wszystkie operacje sieciowe.
## `void Http::terminate()`

Zamyka menedLLera. Zatrzymuje `io_service`, anuluje wszystkie bieLLace operacje i czeka na zakoL"czenie watku sieciowego.
## `int Http::get(const std::string& url, int timeout)`
## Opis semantyczny
WysyL'a asynchroniczne zapytanie HTTP GET.
## DziaL'anie
1.  Generuje unikalne ID operacji.
2.  Dodaje zadanie do `m_ios`, ktore tworzy obiekt `HttpSession`.
3.  `HttpSession` wykonuje zapytanie w watku sieciowym.
4.  Wyniki (postep, bL'ad, odpowiedLs) sa przekazywane z powrotem do gL'ownego watku za pomoca `g_dispatcher` i wywoL'ywane sa odpowiednie callbacki w Lua (`g_http.onGetProgress`, `g_http.onGet`).
## `int Http::post(...)`

DziaL'a analogicznie do `get`, ale wysyL'a zapytanie HTTP POST z podanymi danymi (`data`).
## `int Http::download(...)`

Specjalna wersja `get`, ktora dodatkowo zapisuje pobrane dane w wewnetrznej mapie `m_downloads`. Pozwala to na dostep do pobranych plikow przez `ResourceManager` za pomoca wirtualnej LcieLLki `/downloads/...`.
## `int Http::ws(...)`

Inicjuje asynchroniczne poL'aczenie WebSocket. Tworzy obiekt `WebsocketSession`, ktory zarzadza cyklem LLycia poL'aczenia. Callbacki Lua (`onWsOpen`, `onWsMessage`, `onWsClose`, `onWsError`) sa wywoL'ywane w odpowiedzi na zdarzenia z gniazda.
## `bool Http::wsSend(int operationId, std::string message)`

WysyL'a wiadomoLc przez istniejace poL'aczenie WebSocket o danym `operationId`.
## `bool Http::cancel(int id)`

Anuluje operacje (HTTP lub WebSocket) o podanym ID.
## ZaleLLnoLci i powiazania

-   `framework/http/http.h`: Plik nagL'owkowy.
-   `framework/http/session.h`, `websocket.h`: Implementacje sesji HTTP i WebSocket (niedostepne dla Emscripten).
-   `framework/luaengine/luainterface.h`: Do wywoL'ywania callbackow w Lua.
-   `framework/core/eventdispatcher.h`: Do przekazywania wynikow z watku sieciowego do watku gL'ownego.
-   `boost/asio`, `boost/beast`: Podstawowe biblioteki do obsL'ugi sieci.

---
# z"" websocket.h
## Opis ogolny

Plik `websocket.h` deklaruje klase `WebsocketSession`, ktora zarzadza pojedynczym poL'aczeniem WebSocket. Plik ten (i jego implementacja) jest wyL'aczony z kompilacji dla Emscripten.
## Typy wyliczeniowe i definicje

-   `enum WebsocketCallbackType`: Definiuje typy zdarzeL" dla callbacka (`WEBSOCKET_OPEN`, `WEBSOCKET_MESSAGE`, `WEBSOCKET_ERROR`, `WEBSOCKET_CLOSE`).
-   `using WebsocketSession_cb`: Alias dla typu funkcji zwrotnej.
## Klasa `WebsocketSession`
## Opis semantyczny
`WebsocketSession` enkapsuluje caL'a logike zwiazana z nawiazywaniem, utrzymywaniem i zamykaniem poL'aczenia WebSocket, wL'aczajac w to obsL'uge protokoL'u (handshake) i szyfrowania (WSS). DziaL'a w peL'ni asynchronicznie w oparciu o Boost.Asio.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `WebsocketSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna proces nawiazywania poL'aczenia (rozwiazywanie nazwy DNS, L'aczenie, handshake). |
| `void send(std::string data)` | Dodaje wiadomoLc do kolejki wysyL'ania. |
| `void close()` | Zamyka poL'aczenie. |
## Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_resolver`: Do rozwiazywania nazw DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o zdarzeniach.
-   `m_result`: WskaLsnik na `HttpResult` do przechowywania stanu.
-   `m_timer`: Timer do obsL'ugi timeoutow.
-   `m_socket`: Gniazdo WebSocket dla poL'aczeL" nieszyfrowanych (WS).
-   `m_ssl`: Gniazdo WebSocket dla poL'aczeL" szyfrowanych (WSS).
-   `m_context`: Kontekst SSL.
-   `m_streambuf`: Bufor na przychodzace dane.
-   `m_sendQueue`: Kolejka wiadomoLci do wysL'ania.
## Metody prywatne (`on_...`)

-   Sa to handlery wywoL'ywane przez Boost.Asio po zakoL"czeniu operacji asynchronicznych (np. `on_resolve`, `on_connect`, `on_handshake`, `on_read`, `on_send`). Implementuja one logike maszyny stanow poL'aczenia.
-   `onError`: Centralna funkcja do obsL'ugi bL'edow.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   `boost/asio`, `boost/beast`: Kluczowe biblioteki do obsL'ugi sieci.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# z"" http.h
## Opis ogolny

Plik `http.h` deklaruje klase `Http`, ktora jest singletonem (`g_http`) i stanowi gL'owny interfejs do wykonywania operacji sieciowych opartych na protokoL'ach HTTP/HTTPS i WebSocket.
## Klasa `Http`
## Opis semantyczny
`Http` zarzadza pula operacji sieciowych, ktore sa wykonywane asynchronicznie w dedykowanym watku. Udostepnia proste API do wysyL'ania zapytaL" GET, POST, pobierania plikow oraz nawiazywania poL'aczeL" WebSocket. Interakcja z reszta aplikacji (gL'ownie ze skryptami Lua) odbywa sie poprzez system callbackow.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Http()` | Konstruktor, inicjalizuje `io_context` i `work_guard`. |
| `void init()` | Uruchamia watek sieciowy. |
| `void terminate()` | Zatrzymuje watek sieciowy i anuluje wszystkie operacje. |
| `int get(...)` | Inicjuje asynchroniczne zapytanie GET. |
| `int post(...)` | Inicjuje asynchroniczne zapytanie POST. |
| `int download(...)` | Inicjuje asynchroniczne pobieranie pliku. |
| `int ws(...)` | Inicjuje asynchroniczne poL'aczenie WebSocket. |
| `bool wsSend(...)` | WysyL'a dane przez istniejace poL'aczenie WebSocket. |
| `bool wsClose(...)` | Zamyka poL'aczenie WebSocket. |
| `bool cancel(int id)` | Anuluje operacje o podanym ID. |
| `const std::map<...>& downloads()` | Zwraca mape pobranych plikow. |
| `void clearDownloads()` | CzyLci mape pobranych plikow. |
| `HttpResult_ptr getFile(...)` | Pobiera dane pobranego pliku na podstawie jego LcieLLki. |
| `void setUserAgent(...)` | Ustawia nagL'owek User-Agent dla wszystkich zapytaL". |
## Zmienne prywatne

-   `m_working`: Flaga kontrolujaca dziaL'anie watku.
-   `m_operationId`: Licznik do generowania unikalnych ID dla operacji.
-   `m_thread`: Watek roboczy dla operacji sieciowych.
-   `m_ios`: Kontekst `io_context` z Boost.Asio.
-   `m_guard`: `work_guard` zapobiegajacy zakoL"czeniu `m_ios.run()`, dopoki nie ma pracy.
-   `m_operations`: Mapa przechowujaca stan wszystkich aktywnych operacji.
-   `m_websockets`: Mapa przechowujaca aktywne sesje WebSocket.
-   `m_downloads`: Mapa przechowujaca pobrane pliki.
-   `m_userAgent`: String User-Agent.
## Zmienne globalne

-   `g_http`: Globalna instancja `Http`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest uLLywana w skryptach Lua (poprzez bindowania w `luafunctions.cpp`) do komunikacji z serwerami WWW, np. do pobierania aktualizacji, sprawdzania statusu serwerow itp.
-   WspoL'pracuje z `ResourceManager` w celu udostepnienia pobranych plikow przez wirtualny system plikow.

---
# z"" result.h
## Opis ogolny

Plik `result.h` deklaruje strukture `HttpResult`, ktora sL'uLLy do przechowywania stanu i wyniku pojedynczej operacji HTTP lub WebSocket. Definiuje rownieLL aliasy typow dla inteligentnych wskaLsnikow i funkcji zwrotnych.
## Struktura `HttpResult`
## Opis semantyczny
`HttpResult` jest kontenerem danych przekazywanym miedzy watkiem sieciowym a watkiem gL'ownym. Agreguje wszystkie informacje zwiazane z danym zapytaniem, takie jak URL, status, postep, dane odpowiedzi i ewentualne bL'edy.
## Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `url` | `std::string` | Adres URL zapytania. |
| `operationId` | `int` | Unikalny identyfikator operacji. |
| `status` | `int` | Kod statusu odpowiedzi HTTP (np. 200, 404). |
| `size` | `int` | CaL'kowity rozmiar odpowiedzi (z nagL'owka Content-Length). |
| `progress` | `int` | Postep pobierania w procentach (0-100). |
| `redirects` | `int` | Licznik przekierowaL". |
| `connected` | `bool` | Flaga wskazujaca, czy poL'aczenie jest aktywne. |
| `finished` | `bool` | Flaga wskazujaca, czy operacja zostaL'a zakoL"czona. |
| `canceled` | `bool` | Flaga wskazujaca, czy operacja zostaL'a anulowana. |
| `postData` | `std::string` | Dane wysL'ane w zapytaniu POST. |
| `response` | `std::vector<uint8_t>`| Surowe bajty odpowiedzi. |
| `error` | `std::string` | Komunikat bL'edu, jeLli wystapiL'. |
| `session` | `std::weak_ptr<HttpSession>` | SL'aby wskaLsnik do obiektu sesji, aby uniknac cyklicznych referencji. |
## Definicje typow

-   `HttpResult_ptr`: Alias dla `std::shared_ptr<HttpResult>`.
-   `HttpResult_cb`: Alias dla `std::function<void(HttpResult_ptr)>`.
## ZaleLLnoLci i powiazania

-   Jest to podstawowa struktura danych uLLywana przez `Http`, `HttpSession` i `WebsocketSession` do komunikacji i przekazywania wynikow.
-   Zawiera `std::weak_ptr` do `HttpSession`, aby umoLLliwic anulowanie operacji z zewnatrz bez tworzenia cyklu referencji.

---
# z"" session.cpp
## Opis ogolny

Plik `session.cpp` zawiera implementacje klasy `HttpSession`, ktora zarzadza pojedyncza sesja HTTP/HTTPS. Jest on wyL'aczony z kompilacji dla platformy Emscripten.
## Klasa `HttpSession`
## `void HttpSession::start()`
## Opis semantyczny
Rozpoczyna proces wysyL'ania zapytania HTTP.
## DziaL'anie
1.  Sprawdza limit przekierowaL".
2.  Parsuje URL, aby uzyskac protokoL', domene, port i LcieLLke.
3.  Ustawia timer (`m_timer`) na obsL'uge timeoutu.
4.  Konfiguruje obiekt LLadania `boost::beast::http::request` (metoda, nagL'owki, treLc).
5.  Uruchamia asynchroniczne rozwiazywanie nazwy DNS za pomoca `m_resolver.async_resolve`.
## Metody `on_...()`

Sa to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio, ktore implementuja maszyne stanow sesji HTTP:

-   **`on_resolve`**: WywoL'ywana po rozwiazaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: WywoL'ywana po nawiazaniu poL'aczenia TCP.
    -   JeLli protokoL' to HTTPS, inicjalizuje kontekst SSL i wykonuje `async_handshake`.
    -   WysyL'a LLadanie HTTP za pomoca `boost::beast::http::async_write`.
-   **`on_request_sent`**: WywoL'ywana po wysL'aniu LLadania. Rozpoczyna odczytywanie nagL'owkow odpowiedzi za pomoca `async_read_header`.
-   **`on_read_header`**: WywoL'ywana po odczytaniu nagL'owkow.
    -   Sprawdza kod statusu.
    -   JeLli jest to przekierowanie (np. 301, 302), tworzy nowa `HttpSession` dla nowego URL.
    -   JeLli status jest niepoprawny, zgL'asza bL'ad.
    -   Rozpoczyna odczytywanie treLci odpowiedzi za pomoca `async_read_some`.
-   **`on_read`**: WywoL'ywana wielokrotnie podczas odczytywania treLci odpowiedzi.
    -   Aktualizuje postep pobierania i wywoL'uje `callback` progresu.
    -   Gdy caL'a treLc zostanie odczytana (`end_of_stream`), finalizuje operacje, zapisuje odpowiedLs w `m_result` i wywoL'uje `callback` koL"cowy.
-   **`onTimeout`**: Handler dla timera, ktory zgL'asza bL'ad timeoutu.
-   **`onError`**: Centralna funkcja do obsL'ugi bL'edow. Zamyka gniazdo, anuluje timer i wywoL'uje `callback` z informacja o bL'edzie.
## `void HttpSession::close()`

Zamyka poL'aczenie, anuluje timer i, w przypadku HTTPS, wykonuje `async_shutdown` dla strumienia SSL.
## ZaleLLnoLci i powiazania

-   `framework/http/session.h`: Plik nagL'owkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obsL'ugi sieci.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# z"" session.h
## Opis ogolny

Plik `session.h` deklaruje klase `HttpSession`, ktora enkapsuluje logike pojedynczej sesji HTTP/HTTPS. Plik ten jest wyL'aczony z kompilacji dla Emscripten.
## Klasa `HttpSession`
## Opis semantyczny
`HttpSession` zarzadza caL'ym cyklem LLycia zapytania HTTP, od rozwiazania nazwy DNS, przez nawiazanie poL'aczenia (w tym SSL/TLS handshake), wysL'anie LLadania, aLL po odczytanie odpowiedzi. Jest zaprojektowana do dziaL'ania asynchronicznego w ramach `boost::asio::io_service`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HttpSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna sesje HTTP. |
| `void cancel()` | Anuluje bieLLaca operacje. |
## Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_socket`: Gniazdo TCP.
-   `m_resolver`: Resolver DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o wyniku.
-   `m_result`: WskaLsnik na obiekt `HttpResult` przechowujacy stan.
-   `m_timer`: Timer do obsL'ugi timeoutow.
-   `m_timeout`: Czas timeoutu.
-   `m_isJson`: Flaga wskazujaca, czy treLc POST jest w formacie JSON.
-   `m_ssl`, `m_context`: Do obsL'ugi HTTPS.
-   `m_streambuf`: Bufor na dane przychodzace.
-   `m_request`: Obiekt LLadania z Boost.Beast.
-   `m_response`: Parser odpowiedzi z Boost.Beast.
## Metody prywatne (`on_...`, `close`, `onError`)

Deklaracje handlerow dla operacji asynchronicznych i funkcji pomocniczych.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest tworzona i uLLywana przez klase `Http` do realizacji zapytaL" GET i POST.

---
# z"" websocket.cpp
## Opis ogolny

Plik `websocket.cpp` zawiera implementacje klasy `WebsocketSession`, ktora zarzadza pojedynczym poL'aczeniem WebSocket. Plik ten jest wyL'aczony z kompilacji dla Emscripten.
## Klasa `WebsocketSession`
## `void WebsocketSession::start()`
## Opis semantyczny
Rozpoczyna proces nawiazywania poL'aczenia WebSocket.
## DziaL'anie
1.  Sprawdza limit przekierowaL".
2.  Parsuje URL, aby uzyskac protokoL', domene, port i LcieLLke.
3.  Ustawia timer na obsL'uge timeoutu.
4.  Tworzy odpowiedni obiekt gniazda (`m_socket` dla WS lub `m_ssl` dla WSS).
5.  Uruchamia asynchroniczne rozwiazywanie nazwy DNS.
## `void WebsocketSession::send(std::string data)`

Dodaje wiadomoLc do kolejki `m_sendQueue`. JeLli kolejka byL'a pusta i poL'aczenie jest aktywne, natychmiast inicjuje operacje wysyL'ania.
## Metody `on_...()`

Sa to handlery dla operacji asynchronicznych, ktore implementuja maszyne stanow poL'aczenia WebSocket:

-   **`on_resolve`**: WywoL'ywana po rozwiazaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: WywoL'ywana po nawiazaniu poL'aczenia TCP. W przypadku WSS, wykonuje handshake SSL. Nastepnie inicjuje handshake protokoL'u WebSocket za pomoca `async_handshake`.
-   **`on_handshake`**: WywoL'ywana po pomyLlnym handshake'u WebSocket. Ustawia stan na `connected`, wywoL'uje `callback` `WEBSOCKET_OPEN`, rozpoczyna nasL'uchiwanie wiadomoLci (`async_read`) i wysyL'a wiadomoLci z kolejki.
-   **`on_send`**: WywoL'ywana po wysL'aniu wiadomoLci. Usuwa wysL'ana wiadomoLc z kolejki i, jeLli kolejka nie jest pusta, inicjuje wysyL'anie nastepnej.
-   **`on_read`**: WywoL'ywana po otrzymaniu nowej wiadomoLci. Resetuje timer, wywoL'uje `callback` `WEBSOCKET_MESSAGE` i ponownie nasL'uchuje.
-   **`onTimeout`**: ZgL'asza bL'ad timeoutu.
-   **`onError`**: ObsL'uguje bL'edy i wywoL'uje `callback` `WEBSOCKET_ERROR`.
## `void WebsocketSession::close()`

Zamyka poL'aczenie, anuluje timer i wywoL'uje `callback` `WEBSOCKET_CLOSE`.
## ZaleLLnoLci i powiazania

-   `framework/http/websocket.h`: Plik nagL'owkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obsL'ugi sieci i protokoL'u WebSocket.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# z"" mouse.cpp
## Opis ogolny

Plik `mouse.cpp` implementuje klase `Mouse`, ktora jest singletonem (`g_mouse`) odpowiedzialnym za zarzadzanie kursorami myszy.
## Zmienne globalne
## `g_mouse`

Globalna instancja `Mouse`.
## Klasa `Mouse`
## `void Mouse::init()` i `void Mouse::terminate()`

Metody do inicjalizacji i zwalniania zasobow. `terminate()` czyLci liste zaL'adowanych kursorow.
## `void Mouse::loadCursors(std::string filename)`

Laduje definicje kursorow z pliku OTML. Parsuje plik i dla kaLLdego wpisu w sekcji `Cursors` wywoL'uje `addCursor`.
## `void Mouse::addCursor(const std::string& name, const std::string& file, const Point& hotSpot)`
## Opis semantyczny
Laduje obraz kursora z pliku i tworzy z niego natywny kursor systemowy. Jest bezpieczna watkowo.
## DziaL'anie
1.  JeLli jest wywoL'ana z watku innego niLL graficzny, deleguje zadanie do `g_graphicsDispatcher`.
2.  WywoL'uje `g_window.loadMouseCursor`, ktora wykonuje operacje specyficzne dla platformy.
3.  Zapisuje zwrocone ID kursora w mapie `m_cursors` pod podana nazwa.
## `void Mouse::pushCursor(const std::string& name)`
## Opis semantyczny
Ustawia nowy kursor i dodaje go na stos aktywnych kursorow.
## DziaL'anie
1.  Deleguje do watku graficznego, jeLli to konieczne.
2.  Znajduje ID kursora w `m_cursors`.
3.  WywoL'uje `g_window.setMouseCursor` z znalezionym ID.
4.  Dodaje ID na koniec stosu `m_cursorStack`.
## `void Mouse::popCursor(const std::string& name)`
## Opis semantyczny
Usuwa kursor ze stosu i przywraca poprzedni.
## DziaL'anie
1.  Deleguje do watku graficznego.
2.  JeLli `name` jest puste, usuwa ostatni kursor ze stosu.
3.  JeLli `name` jest podane, wyszukuje i usuwa konkretny kursor ze stosu.
4.  JeLli stos nie jest pusty, ustawia kursor, ktory jest teraz na jego szczycie.
5.  JeLli stos jest pusty, przywraca domyLlny kursor systemowy.
## `bool Mouse::isCursorChanged()`

Zwraca `true`, jeLli stos kursorow nie jest pusty, co oznacza, LLe aktualny kursor jest niestandardowy.
## `bool Mouse::isPressed(Fw::MouseButton mouseButton)`

Sprawdza i zwraca stan wciLniecia danego przycisku myszy, delegujac zapytanie do `g_window`.
## ZaleLLnoLci i powiazania

-   `framework/input/mouse.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Widgety moga zmieniac kursor.
-   `framework/platform/platformwindow.h`: ULLywa `g_window` do niskopoziomowych operacji na kursorach.
-   `framework/core/eventdispatcher.h`: Do zapewnienia bezpieczeL"stwa watkowego.
-   `framework/core/resourcemanager.h`: Do L'adowania plikow definicji kursorow.

---
# z"" mouse.h
## Opis ogolny

Plik `mouse.h` deklaruje klase `Mouse`, ktora jest interfejsem wysokiego poziomu do zarzadzania kursorami myszy w aplikacji.
## Klasa `Mouse`
## Opis semantyczny
`Mouse` zarzadza kolekcja niestandardowych kursorow, ktore moga byc L'adowane z plikow. Implementuje mechanizm stosu (`m_cursorStack`), ktory pozwala na tymczasowa zmiane kursora (np. gdy kursor znajduje sie nad widgetem) i L'atwy powrot do poprzedniego stanu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedLLera. |
| `void terminate()` | Zwalnia zasoby. |
| `void loadCursors(...)` | Laduje definicje kursorow z pliku OTML. |
| `void addCursor(...)` | Dodaje nowy niestandardowy kursor. |
| `void pushCursor(...)` | Ustawia nowy kursor, dodajac go na szczyt stosu. |
| `void popCursor(...)` | Usuwa kursor ze stosu i przywraca poprzedni. |
| `bool isCursorChanged()` | Sprawdza, czy aktualny kursor jest niestandardowy. |
| `bool isPressed(...)` | Sprawdza stan wciLniecia przycisku myszy. |
## Zmienne prywatne

-   `m_cursors`: Mapa przechowujaca nazwy kursorow i ich ID specyficzne dla platformy.
-   `m_cursorStack`: Stos (`std::deque`) przechowujacy ID aktywnych kursorow.
-   `m_mutex`: Mutex do ochrony dostepu do `m_cursorStack` z roLLnych watkow.
## Zmienne globalne

-   `g_mouse`: Globalna instancja `Mouse`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uLLywana przez `UIWidget` do zmiany wygladu kursora, gdy znajduje sie on nad widgetem.
-   WspoL'pracuje z `PlatformWindow` w celu faktycznego ustawiania kursora w systemie operacyjnym.

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `luaengine` sL'uLLy do wczesnych deklaracji (forward declarations) i definicji typow zwiazanych z silnikiem Lua. Jego celem jest unikanie zaleLLnoLci cyklicznych i zmniejszenie liczby doL'aczanych nagL'owkow.
## Wczesne deklaracje

-   `LuaInterface`: GL'owna klasa interfejsu Lua.
-   `LuaObject`: Bazowa klasa dla wszystkich obiektow eksportowanych do Lua.
## Definicje typow

-   **`LuaCppFunction`**: Alias dla `std::function<int(LuaInterface*)>`. Jest to typ funkcji C++, ktora moLLe byc wywoL'ana z Lua. Przyjmuje wskaLsnik do `LuaInterface` i zwraca liczbe wartoLci zwroconych na stos Lua.
-   **`LuaCppFunctionPtr`**: Alias dla `std::unique_ptr<LuaCppFunction>`. ULLywany wewnetrznie do zarzadzania czasem LLycia funkcji bindowanych.
-   **`LuaObjectPtr`**: Alias dla `stdext::shared_object_ptr<LuaObject>`. Standardowy sposob przekazywania i przechowywania obiektow C++ w Lua.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje.
-   `<memory>`: Dla `std::unique_ptr`.
-   Jest to fundamentalny plik dla caL'ego silnika Lua, doL'aczany przez `luainterface.h`, `luaobject.h` i inne.

---
# z"" lbitlib.cpp
## Opis ogolny

Plik `lbitlib.cpp` zawiera kod LsrodL'owy biblioteki `bit32` z Lua 5.2.0, przeniesiony (backported) do uLLytku z Lua 5.1.4 (lub LuaJIT, ktory jest kompatybilny z 5.1). Biblioteka ta dostarcza operacje bitowe na 32-bitowych liczbach caL'kowitych bez znaku.
## ZawartoLc

Plik skL'ada sie z kilku czeLci:

1.  **Adaptacje i definicje kompatybilnoLci**:
    -   Zawiera kod przeniesiony z `luaconf.h` i `llimits.h` z Lua 5.2, ktory definiuje makra (`lua_number2unsigned`) do bezpiecznej konwersji miedzy `lua_Number` (zwykle `double`) a `lua_Unsigned` (32-bitowy `unsigned int`). Jest to konieczne, poniewaLL Lua 5.1 nie ma wbudowanego typu caL'kowitoliczbowego.
    -   Definiuje funkcje `lua_pushunsigned` i `luaL_checkunsigned` do obsL'ugi tego typu na stosie Lua.
    -   Definiuje makro `luaL_newlib` dla kompatybilnoLci z `luaL_register` z Lua 5.1.

2.  **Oryginalny kod `lbitlib.c` z Lua 5.2.0**:
    -   Zawiera implementacje wszystkich funkcji z biblioteki `bit32`.
## Funkcje biblioteki `bit32`

| Funkcja Lua | Opis |
| :--- | :--- |
| `bit32.band(...)` | Wykonuje bitowe AND na wszystkich argumentach. |
| `bit32.btest(...)` | Wykonuje bitowe AND i zwraca `true`, jeLli wynik jest roLLny od zera. |
| `bit32.bor(...)` | Wykonuje bitowe OR na wszystkich argumentach. |
| `bit32.bxor(...)` | Wykonuje bitowe XOR na wszystkich argumentach. |
| `bit32.bnot(x)` | Wykonuje bitowa negacje. |
| `bit32.lshift(x, n)` | Przesuniecie bitowe w lewo. |
| `bit32.rshift(x, n)` | Przesuniecie bitowe w prawo (logiczne). |
| `bit32.arshift(x, n)`| Przesuniecie bitowe w prawo (arytmetyczne). |
| `bit32.lrotate(x, n)`| Rotacja bitowa w lewo. |
| `bit32.rrotate(x, n)`| Rotacja bitowa w prawo. |
| `bit32.extract(n, field, width)`| Ekstrahuje `width` bitow z liczby `n`, zaczynajac od bitu `field`. |
| `bit32.replace(n, v, field, width)`| Zastepuje bity w liczbie `n` bitami z `v`. |
## `int luaopen_bit32 (lua_State *L)`

GL'owna funkcja, ktora rejestruje biblioteke `bit32` w podanym stanie Lua.
## ZaleLLnoLci i powiazania

-   `lbitlib.h`: Plik nagL'owkowy.
-   NagL'owki Lua/LuaJIT (`lua.h`, `lualib.h`, `lauxlib.h`).
-   Jest L'adowana w `LuaInterface::createLuaState`, aby udostepnic operacje bitowe w skryptach.

---
# z"" lbitlib.h
## Opis ogolny

Plik `lbitlib.h` jest plikiem nagL'owkowym dla biblioteki `bit32` z Lua 5.2, ktora zostaL'a przeniesiona do uLLytku w tym projekcie.
## Deklaracje
## `int luaopen_bit32 (lua_State *L)`

Deklaruje funkcje, ktora jest punktem wejLcia do zaL'adowania biblioteki `bit32` w stanie Lua. Zgodnie z konwencja Lua, funkcje `luaopen_*` sa uLLywane do rejestrowania moduL'ow.
## ZaleLLnoLci i powiazania

-   Wymaga definicji `struct lua_State`.
-   Jest doL'aczany przez `luainterface.cpp`, aby umoLLliwic zaL'adowanie biblioteki `bit32` podczas inicjalizacji `LuaInterface`.

---
# z"" luabinder.h
## Opis ogolny

Plik `luabinder.h` jest sercem mechanizmu bindowania C++ do Lua. Zawiera on zestaw zaawansowanych szablonow metaprogramowania, ktore umoLLliwiaja automatyczne generowanie funkcji-opakowaL" (wrapperow) dla niemal dowolnych funkcji C++, w tym funkcji globalnych, statycznych, metod klas, funkcji `std::function` i lambd.
## Namespace `luabinder`
## Opis semantyczny
PrzestrzeL" nazw `luabinder` zawiera szablony, ktore dziaL'aja jak "fabryka" funkcji typu `LuaCppFunction`. Analizuja one sygnature funkcji C++ (typ zwracany i typy argumentow), a nastepnie generuja lambde, ktora:
1.  Pobiera argumenty z stosu Lua i konwertuje je na odpowiednie typy C++.
2.  WywoL'uje oryginalna funkcje C++ z tymi argumentami.
3.  Pobiera wartoLc zwracana przez funkcje C++.
4.  Konwertuje te wartoLc na typ zrozumiaL'y dla Lua i umieszcza ja na stosie.
5.  Zwraca liczbe wartoLci umieszczonych na stosie.
## GL'owne szablony

-   **`pack_values_into_tuple`**: Szablon rekurencyjny, ktory pobiera `N` wartoLci ze stosu Lua i umieszcza je w `std::tuple`.
-   **`expand_fun_arguments`**: Szablon rekurencyjny, ktory rozpakowuje `std::tuple` z argumentami i wywoL'uje z nimi docelowa funkcje C++.
-   **`call_fun_and_push_result`**: Szablon, ktory wywoL'uje funkcje i obsL'uguje wartoLc zwracana (specjalizacje dla `void` i typow nie-`void`).
-   **`bind_fun_specializer`**: GL'owny szablon, ktory L'aczy powyLLsze, generujac finalna lambde.
-   **`bind_fun(...)`**: PrzeciaLLone funkcje, ktore sa publicznym API tego namespace. Przyjmuja roLLne typy funkcji (wskaLsniki, `std::function`, lambdy) i przekierowuja je do odpowiednich specjalizacji.
-   **`make_mem_func(...)` i `make_mem_func_singleton(...)`**: Funkcje pomocnicze, ktore konwertuja wskaLsniki na metody klas na obiekty `std::function` (lambdy), ktore moLLna nastepnie zbindowac.
## ZaleLLnoLci i powiazania

-   Jest to plik wewnetrzny, doL'aczany tylko przez `luainterface.h`.
-   Intensywnie korzysta z zaawansowanych cech C++11/14/17, takich jak szablony wariadyczne, `std::tuple`, `std::function`, `std::enable_if`, `decltype`.
-   `framework/stdext/traits.h`: ULLywa `remove_const_ref` do normalizacji typow.
-   `luaexception.h`: MoLLe rzucac wyjatki w przypadku bL'edow (np. wywoL'anie metody na obiekcie `nullptr`).
-   Jest podstawa dla wszystkich metod `bind...` w `LuaInterface`, ktore automatyzuja proces tworzenia bindowaL".

---
# z"" luaexception.h
## Opis ogolny

Plik `luaexception.h` deklaruje hierarchie klas wyjatkow specyficznych dla interakcji z silnikiem Lua. Te klasy wyjatkow sa uLLywane do sygnalizowania bL'edow, ktore wystepuja podczas operacji na stosie Lua, rzutowania typow lub wywoL'ywania funkcji.
## Klasa `LuaException`
## Opis semantyczny
Jest to bazowa klasa dla wszystkich wyjatkow zwiazanych z Lua. Dziedziczy po `stdext::exception`. Jej gL'ownym zadaniem jest sformatowanie komunikatu o bL'edzie, opcjonalnie doL'aczajac do niego Llad stosu (traceback) z Lua.
## Metody

-   `LuaException(const std::string& error, int traceLevel = -1)`: Konstruktor, ktory generuje komunikat bL'edu.
-   `virtual const char* what() const throw()`: Zwraca sformatowany komunikat bL'edu.
## Klasa `LuaBadNumberOfArgumentsException`
## Opis semantyczny
Specjalistyczny wyjatek rzucany, gdy funkcja C++ bindowana do Lua zostanie wywoL'ana z nieprawidL'owa liczba argumentow.
## Metody

-   `LuaBadNumberOfArgumentsException(int expected = -1, int got = -1)`: Konstruktor, ktory tworzy odpowiedni komunikat o bL'edzie.
## Klasa `LuaBadValueCastException`
## Opis semantyczny
Specjalistyczny wyjatek rzucany, gdy proba rzutowania wartoLci ze stosu Lua na okreLlony typ C++ (`luavalue_cast`) nie powiedzie sie.
## Metody

-   `LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`: Konstruktor, ktory tworzy komunikat bL'edu informujacy o typach, miedzy ktorymi rzutowanie zawiodL'o.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa `stdext::exception`.
-   Wyjatki te sa rzucane przez `LuaInterface` i `luabinder`, a L'apane w bezpiecznych punktach wywoL'aL" (np. `luaCppFunctionCallback`), aby zapobiec awarii aplikacji i przekazac bL'ad do logow lub z powrotem do Lrodowiska Lua.

---
# z"" luaexception.cpp
## Opis ogolny

Plik `luaexception.cpp` zawiera implementacje klas wyjatkow zdefiniowanych w `luaexception.h`.
## Klasa `LuaException`
## `LuaException::LuaException(const std::string& error, int traceLevel)`

Konstruktor. Jego gL'ownym zadaniem jest wywoL'anie `generateLuaErrorMessage`, aby przygotowac peL'ny komunikat bL'edu.
## `void LuaException::generateLuaErrorMessage(const std::string& error, int traceLevel)`

Metoda ta formatuje finalny komunikat bL'edu, ktory bedzie dostepny przez `what()`.
-   JeLli `traceLevel` jest podany (wiekszy lub rowny 0), wywoL'uje `g_lua.traceback`, aby doL'aczyc do komunikatu Llad stosu wywoL'aL" Lua.
-   W przeciwnym razie, po prostu prefiksuje bL'ad napisem "LUA ERROR:".
## Klasa `LuaBadNumberOfArgumentsException`
## `LuaBadNumberOfArgumentsException::LuaBadNumberOfArgumentsException(int expected, int got)`

Konstruktor. Tworzy specyficzny komunikat bL'edu informujacy o nieprawidL'owej liczbie argumentow, a nastepnie wywoL'uje `generateLuaErrorMessage` z poziomem Lledzenia `1`, aby pokazac, ktora funkcja w Lua zostaL'a Lsle wywoL'ana.
## Klasa `LuaBadValueCastException`
## `LuaBadValueCastException::LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`

Konstruktor. Tworzy komunikat bL'edu informujacy o niemoLLnoLci rzutowania miedzy danym typem Lua a typem C++, a nastepnie wywoL'uje `generateLuaErrorMessage`.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/luaexception.h`: Plik nagL'owkowy.
-   `framework/luaengine/luainterface.h`: ULLywa `g_lua` do generowania Lladu stosu.
-   Implementuje logike formatowania bL'edow, ktora jest kluczowa dla debugowania skryptow Lua.

---
# z"" luainterface.cpp
## Opis ogolny

Plik `luainterface.cpp` zawiera implementacje klasy `LuaInterface`, ktora jest centralnym interfejsem do komunikacji z silnikiem Lua. Jest to jedna z najwaLLniejszych klas w caL'ym frameworku.
## Zmienne globalne
## `g_lua`

Globalna instancja `LuaInterface`.
## Klasa `LuaInterface`
## Inicjalizacja i zamykanie

-   **`init()`**: Inicjalizuje `LuaInterface`.
    1.  Tworzy nowy stan Lua (`createLuaState`).
    2.  Zapisuje referencje do globalnego Lrodowiska.
    3.  Rejestruje bazowa klase `LuaObject` i jej podstawowe metody.
-   **`terminate()`**: Zamyka stan Lua, co powoduje zwolnienie wszystkich zasobow i wywoL'anie garbage collectora.
-   **`createLuaState()`**: Tworzy stan Lua (`luaL_newstate`), L'aduje standardowe biblioteki (`luaL_openlibs`), L'aduje biblioteke `bit32`, tworzy specjalna "sL'aba" tabele do przechowywania referencji i instaluje niestandardowe loadery (`dofile`, `loadfile`).
## Rejestracja i bindowanie

-   **`registerSingletonClass(...)`**, **`registerClass(...)`**: Implementuja logike tworzenia tabel i metatabel w Lua, ktore reprezentuja klasy C++. `registerClass` dodatkowo ustawia dziedziczenie, linkujac metatabele klasy pochodnej do metatabeli klasy bazowej za pomoca metametody `__index`.
-   **`register...Function(...)`**, **`register...Field(...)`**: Metody te pobieraja odpowiednie tabele (klasy, metody, fieldmethods) z globalnego Lrodowiska Lua i umieszczaja w nich funkcje C++ opakowane w `LuaCppFunction`.
## Metody obsL'ugi metametod obiektow

-   **`luaObjectGetEvent(__index)`**: Handler wywoL'ywany przy probie odczytu pola z obiektu C++ w Lua. Wyszukuje on kolejno: metode "get", pole w tabeli `fields` obiektu, metode w tabeli metod klasy.
-   **`luaObjectSetEvent(__newindex)`**: Handler wywoL'ywany przy probie zapisu pola. Wyszukuje i wywoL'uje metode "set" lub zapisuje wartoLc w tabeli `fields`.
-   **`luaObjectEqualEvent(__eq)`**: Porownuje dwa obiekty C++.
-   **`luaObjectCollectEvent(__gc)`**: Handler wywoL'ywany przez garbage collector Lua. Zwalnia `shared_ptr` do obiektu, dekrementujac jego licznik referencji.
## Wykonywanie skryptow

-   **`runScript(...)`**, **`loadScript(...)`**, **`runBuffer(...)`**: Metody do L'adowania i wykonywania skryptow Lua z plikow lub buforow w pamieci. `loadScript` uLLywa `g_resources` do znalezienia i odczytania pliku.
-   **`safeCall(...)`**: Kluczowa metoda do bezpiecznego wywoL'ywania funkcji Lua. Ustawia `luaErrorHandler` jako funkcje obsL'ugi bL'edow, a nastepnie wywoL'uje `lua_pcall`. W przypadku bL'edu, L'apie go i zwraca jako string lub rzuca wyjatek `LuaException`.
-   **`signalCall(...)`**: Wysokopoziomowa metoda, ktora opakowuje `safeCall` i dodatkowo obsL'uguje wywoL'ywanie tabeli funkcji.
## Inne

-   **`traceback(...)`**: Generuje Llad stosu wywoL'aL" Lua.
-   **`getCurrentSourcePath(...)`**: Zwraca LcieLLke do pliku skryptu, w ktorym aktualnie wykonywany jest kod.
-   **`newSandboxEnv()`**: Tworzy nowe, odizolowane Lrodowisko Lua.
-   **`lua...` (funkcje statyczne)**: Implementacje funkcji C, ktore sa bezpoLrednio rejestrowane w Lua (np. `lua_dofile`).
-   **`...Callback`**: Implementacje handlerow dla `lua_pcall` i `__gc`.
-   **Metody opakowujace API Lua**: Plik zawiera dziesiatki metod (`getTop`, `pushNil`, `toString`, `isTable`, etc.), ktore sa cienkimi, ale bezpieczniejszymi (dzieki `VALIDATE`) opakowaniami na funkcje z biblioteki Lua C API.
## ZaleLLnoLci i powiazania

-   Jest to centralna klasa, ktora L'aczy C++ z Lua. ZaleLLy od `lua.h`, `lualib.h`, `lauxlib.h`.
-   LsciLle wspoL'pracuje z `LuaObject`, `luabinder.h`, `luavaluecasts.h`.
-   ULLywa `g_resources` do L'adowania skryptow.
-   ULLywana przez `Application` do inicjalizacji, `ModuleManager` do L'adowania moduL'ow i `UIWidget` do wywoL'ywania callbackow.

---
# z"" luainterface.h
## Opis ogolny

Plik `luainterface.h` deklaruje klase `LuaInterface`, ktora jest gL'ownym interfejsem do interakcji z silnikiem Lua. Jest to klasa singletonowa (`g_lua`), ktora enkapsuluje stan Lua (`lua_State*`) i dostarcza bogaty zestaw metod do manipulacji stosem, wywoL'ywania funkcji, bindowania kodu C++ i zarzadzania obiektami.
## Klasa `LuaInterface`
## Opis semantyczny
`LuaInterface` stanowi most miedzy kodem C++ a skryptami Lua. Udostepnia wysokopoziomowe API, ktore ukrywa zL'oLLonoLc bezpoLredniej pracy z Lua C API. Wszystkie operacje, takie jak umieszczanie wartoLci na stosie, odczytywanie ich, wywoL'ywanie funkcji czy rejestrowanie klas, sa opakowane w metody tej klasy.
## Metody publiczne (wybrane)
## Inicjalizacja i zarzadzanie
-   `init()` / `terminate()`: Uruchamia i zamyka silnik Lua.
-   `collectGarbage()`: Wymusza uruchomienie garbage collectora.
## Rejestracja i bindowanie
-   `registerSingletonClass(...)`: Rejestruje globalny obiekt (singleton) w Lua.
-   `registerClass(...)`: Rejestruje klase C++ w Lua, umoLLliwiajac tworzenie jej instancji.
-   `bind...Function(...)`, `bind...Field(...)`: Szablonowe metody do bindowania funkcji i pol klas.
## Wykonywanie skryptow
-   `safeRunScript(...)`: Bezpiecznie wykonuje skrypt z pliku.
-   `runScript(...)`, `runBuffer(...)`: Wykonuja skrypt z pliku lub bufora.
-   `loadScript(...)`, `loadFunction(...)`: Laduja skrypt/funkcje na stos bez jej wykonywania.
-   `safeCall(...)`: Bezpiecznie wywoL'uje funkcje na stosie, z obsL'uga bL'edow.
-   `signalCall(...)`: Wysokopoziomowa wersja `safeCall` z dodatkowymi funkcjami.
-   `callGlobalField<R, ...T>(...)`: Wygodna metoda do wywoL'ywania globalnej funkcji Lua z C++ i otrzymywania wyniku.
## Manipulacja stosem i typami
-   `push...()` / `pop...()` / `to...()` / `is...()`: Zestaw metod do pracy ze stosem Lua dla roLLnych typow danych (np. `pushInteger`, `isString`, `toObject`).
-   `getTop()`: Zwraca rozmiar stosu.
-   `ref()` / `unref()`: Do tworzenia i zwalniania trwaL'ych referencji do wartoLci Lua.
-   `polymorphicPush<T>(...)`: Szablonowa metoda do umieszczania na stosie dowolnego typu, dla ktorego zdefiniowano `push_luavalue`.
-   `castValue<T>(...)`: Szablonowa metoda do rzutowania wartoLci ze stosu na typ C++, uLLywajac `luavalue_cast`.
## Zmienne prywatne

-   `L`: WskaLsnik na `lua_State`.
-   `m_weakTableRef`: Referencja do tabeli ze sL'abymi referencjami.
-   `m_cppCallbackDepth`: Licznik zagnieLLdLLenia wywoL'aL" zwrotnych C++.
-   `m_totalObjRefs`, `m_totalFuncRefs`: Liczniki do Lledzenia alokacji.
-   `m_globalEnv`: Referencja do globalnego Lrodowiska Lua.
## DoL'aczane pliki
Plik ten na koL"cu doL'acza trzy kluczowe pliki, ktore sa od niego zaleLLne i rozszerzaja jego funkcjonalnoLc:
-   `luaexception.h`: Definicje wyjatkow.
-   `luabinder.h`: Maszyneria do bindowania funkcji.
-   `luavaluecasts.h`: Implementacje `push_luavalue` i `luavalue_cast` dla roLLnych typow.
## ZaleLLnoLci i powiazania

-   Jest to centralny plik dla caL'ego podsystemu Lua.
-   ZaleLLny od `framework/luaengine/declarations.h`.
-   ULLywany przez praktycznie kaLLda czeLc aplikacji, ktora wchodzi w interakcje z Lua.

---
# z"" luaobject.cpp
## Opis ogolny

Plik `luaobject.cpp` zawiera implementacje klasy `LuaObject`, ktora jest klasa bazowa dla wszystkich obiektow C++, ktore maja byc dostepne w Lrodowisku Lua.
## Klasa `LuaObject`
## `LuaObject::LuaObject()`

Konstruktor. Inicjalizuje `m_fieldsTableRef` na -1, co oznacza, LLe obiekt nie ma jeszcze przypisanej tabeli pol w Lua.
## `LuaObject::~LuaObject()`

Destruktor. WywoL'uje `releaseLuaFieldsTable()`, aby zwolnic referencje do tabeli pol w Lua, co pozwala garbage collectorowi na jej usuniecie. Sprawdza rownieLL, czy nie jest wywoL'ywany podczas zamykania aplikacji.
## `bool LuaObject::hasLuaField(const std::string& field)`

Sprawdza, czy obiekt posiada pole o danej nazwie w swojej tabeli pol Lua.
## `void LuaObject::releaseLuaFieldsTable()`

Zwalnia referencje do tabeli pol (`m_fieldsTableRef`), jeLli istnieje.
## `void LuaObject::luaSetField(const std::string& key)`
## Opis semantyczny
Ustawia pole w tabeli Lua powiazanej z tym obiektem. WartoLc do ustawienia musi znajdowac sie na szczycie stosu Lua.
## DziaL'anie
1.  JeLli obiekt nie ma jeszcze tabeli pol (`m_fieldsTableRef == -1`), tworzy nowa tabele w Lua i zapisuje do niej referencje.
2.  Pobiera tabele pol na stos Lua.
3.  Przenosi wartoLc ze szczytu stosu na odpowiednie miejsce.
4.  Ustawia pole w tabeli za pomoca `g_lua.setField(key)`.
5.  Zdejmuje tabele pol ze stosu.
## `void LuaObject::luaGetField(const std::string& key)`

Pobiera wartoLc pola z tabeli Lua obiektu i umieszcza ja na szczycie stosu. JeLli tabela pol nie istnieje, umieszcza `nil`.
## `void LuaObject::luaGetMetatable()`

Pobiera i umieszcza na stosie metatabele dla klasy tego obiektu. ULLywa statycznej mapy (`metatableMap`) do cachowania referencji do metatabel dla kaLLdego typu klasy, aby uniknac wielokrotnego wyszukiwania ich w globalnym Lrodowisku Lua.
## `void LuaObject::luaGetFieldsTable()`

Umieszcza na stosie tabele pol tego obiektu, lub `nil`, jeLli ona nie istnieje.
## `int LuaObject::getUseCount()`

Zwraca liczbe referencji do obiektu (`shared_object::ref_count()`).
## `std::string LuaObject::getClassName()`

Zwraca zdemanglowana nazwe klasy obiektu, ktora jest uLLywana do znalezienia odpowiedniej metatabeli w Lua.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/luaobject.h`: Plik nagL'owkowy.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do wszystkich operacji na stanie Lua.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasa bazowa dla setek innych klas w projekcie, ktore sa eksportowane do Lua.

---
# z"" luaobject.h
## Opis ogolny

Plik `luaobject.h` deklaruje klase `LuaObject`, ktora jest fundamentalna klasa bazowa dla wszystkich obiektow C++, ktore maja byc widoczne i zarzadzane przez silnik Lua.
## Klasa `LuaObject`
## Opis semantyczny
`LuaObject` dziedziczy po `stdext::shared_object`, co zapewnia zarzadzanie czasem LLycia obiektu za pomoca licznika referencji. Dodaje funkcjonalnoLc, ktora pozwala na dynamiczne doL'aczanie do obiektu C++ pol i metod z poziomu Lua. KaLLda instancja `LuaObject` moLLe posiadac wL'asna, unikalna tabele w Lua (`m_fieldsTableRef`), w ktorej przechowywane sa te dynamiczne dane.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Szablonowe metody do interakcji z Lua** | |
| `connectLuaField(...)`| Laczy funkcje C++ (`std::function`) z polem Lua, tworzac lub rozszerzajac tabele callbackow. |
| `luaCallLuaField(...)`| WywoL'uje funkcje przechowywana w polu Lua tego obiektu. |
| `callLuaField(...)`| Wysokopoziomowe opakowanie na `luaCallLuaField`, ktore obsL'uguje konwersje typow zwracanych. |
| `hasLuaField(...)` | Sprawdza, czy obiekt ma pole o danej nazwie w swojej tabeli Lua. |
| `setLuaField(...)` | Ustawia wartoLc pola w tabeli Lua. |
| `getLuaField(...)` | Pobiera wartoLc pola z tabeli Lua. |
| **Niskopoziomowe metody do interakcji z Lua** | |
| `releaseLuaFieldsTable()`| Zwalnia referencje do tabeli pol. |
| `luaSetField(...)` | Ustawia pole, pobierajac wartoLc ze szczytu stosu Lua. |
| `luaGetField(...)` | Pobiera pole i umieszcza jego wartoLc na stosie Lua. |
| `luaGetMetatable()` | Pobiera i umieszcza na stosie metatabele klasy. |
| `luaGetFieldsTable()`| Umieszcza na stosie tabele pol obiektu. |
| **Metody pomocnicze** | |
| `getUseCount()` | Zwraca liczbe referencji do obiektu. |
| `getClassName()` | Zwraca nazwe klasy. |
## Zmienne prywatne

-   `m_fieldsTableRef`: Przechowuje referencje (indeks w rejestrze Lua) do tabeli pol tego obiektu.
## Funkcje globalne (`connect`)

Szablonowe funkcje globalne, ktore sa wygodnym opakowaniem na `LuaObject::connectLuaField`, pozwalajac na L'atwe L'aczenie zarowno `std::function`, jak i lambd z polami obiektow.
## ZaleLLnoLci i powiazania

-   `framework/util/stats.h`: Potencjalnie do statystyk.
-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   Jest klasa bazowa dla prawie kaLLdej klasy w projekcie, ktora jest eksportowana do Lua (np. `UIWidget`, `Protocol`, `Module`).
-   Oznaczona jako `@bindclass`, jej podstawowe metody (`getUseCount`, `getClassName`, `getFieldsTable`) sa dostepne w Lua.

---
# z"" luavaluecasts.cpp
## Opis ogolny

Plik `luavaluecasts.cpp` zawiera implementacje specjalizacji szablonow `push_luavalue` i `luavalue_cast` dla podstawowych typow danych. Te funkcje sa sercem systemu konwersji typow miedzy C++ a Lua.
## Funkcje `push_luavalue`
## Opis semantyczny
KaLLda funkcja `push_luavalue` przyjmuje wartoLc typu C++ i umieszcza jej odpowiednik na szczycie stosu Lua. Zwraca liczbe wartoLci umieszczonych na stosie (zwykle 1).
## Implementacje:
-   `bool`: `g_lua.pushBoolean(b)`
-   `int`: `g_lua.pushInteger(i)`
-   `double`: `g_lua.pushNumber(d)`
-   `const char*`, `std::string`: `g_lua.pushString(str)`
-   `LuaCppFunction`: `g_lua.pushCppFunction(func)`
-   **Typy zL'oLLone (`Color`, `Rect`, `Point`, `Size`)**: Tworza nowa tabele w Lua i wypeL'niaja ja odpowiednimi polami (np. `r`, `g`, `b`, `a` dla `Color`).
-   **`OTMLNodePtr`**: Konwertuje wezeL' OTML na tabele Lua, rekurencyjnie przetwarzajac jego dzieci.
## Funkcje `luavalue_cast`
## Opis semantyczny
KaLLda funkcja `luavalue_cast` probuje odczytac wartoLc z podanego indeksu na stosie Lua i skonwertowac ja na odpowiedni typ C++. Zwraca `true` w przypadku sukcesu.
## Implementacje:
-   `bool`: `g_lua.toBoolean(index)`
-   `int`, `double`: `g_lua.toInteger(index)`, `g_lua.toNumber(index)`. Sprawdzaja dodatkowo, czy wartoLc na stosie jest faktycznie liczba.
-   `std::string`: `g_lua.toString(index)`
-   **Typy zL'oLLone (`Color`, `Rect`, ...)**: Sprawdzaja, czy na stosie jest tabela z odpowiednimi polami lub string, ktory moLLna sparsowac. Odczytuja wartoLci z tabeli i przypisuja je do obiektu C++.
-   **`OTMLNodePtr`**: Konwertuje tabele Lua z powrotem na strukture wezL'ow OTML.
-   **`LuaObjectPtr`**: Sprawdza, czy na stosie jest `userdata` i rzutuje je na odpowiedni typ wskaLsnika.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/luavaluecasts.h`: Plik nagL'owkowy.
-   `framework/luaengine/luainterface.h`: ULLywaja metod `g_lua` do interakcji ze stosem.
-   `framework/otml/otmlnode.h`: Do konwersji wezL'ow OTML.
-   Sa to funkcje niskiego poziomu, uLLywane przez `LuaInterface::polymorphicPush` i `LuaInterface::castValue` do automatycznej konwersji typow.

---
# z"" luavaluecasts.h
## Opis ogolny

Plik `luavaluecasts.h` deklaruje zestaw szablonowych funkcji `push_luavalue` i `luavalue_cast`, ktore definiuja, w jaki sposob roLLne typy danych C++ sa konwertowane do i z wartoLci Lua. Jest to kluczowy element systemu bindowania, ktory umoLLliwia automatyczna konwersje argumentow funkcji i wartoLci zwracanych.
## Szablony i funkcje
## `push_luavalue<T>(const T& v)`
## Opis
Szablon funkcji, ktory przyjmuje wartoLc typu `T` i umieszcza jej reprezentacje na stosie Lua. Dla kaLLdego typu, ktory ma byc przekazywany miedzy C++ a Lua, musi istniec specjalizacja tej funkcji.
## `luavalue_cast<T>(int index, T& v)`
## Opis
Szablon funkcji, ktory probuje odczytac wartoLc z podanego indeksu `index` na stosie Lua i skonwertowac ja do typu `T`. Zwraca `true`, jeLli konwersja sie powiedzie.
## Zadeklarowane specjalizacje

Plik deklaruje (a w przypadku typow prostych, rownieLL definiuje `inline`) specjalizacje dla:
-   **Typow prostych**: `bool`, `int`, `double`, `float`, liczby caL'kowite o staL'ym rozmiarze (`int8`, `uint16`, itp.).
-   **Stringow**: `const char*`, `std::string`.
-   **Funkcji C++**: `LuaCppFunction`, `std::function`.
-   **Struktur frameworka**: `Color`, `Rect`, `Point`, `Size`.
-   **WezL'ow OTML**: `OTMLNodePtr`.
-   **Typow wyliczeniowych (enum)**.
-   **Obiektow C++**: `LuaObjectPtr` i wskaLsniki do klas pochodnych.
-   **Kontenerow STL**: `std::list`, `std::vector`, `std::set`, `std::deque`, `std::map`.
-   **Krotek**: `std::tuple`.
## PrzykL'ad dziaL'ania

// C++
void myFunction(int a, const std::string& b) { /* ... */ }

// Lua
myFunction(10, "hello")
```
Gdy `myFunction` jest wywoL'ywana z Lua, `luabinder` uLLyje:
-   `luavalue_cast(1, int&)` do konwersji `10` z Lua na `int` w C++.
-   `luavalue_cast(2, std::string&)` do konwersji `"hello"` z Lua na `std::string` w C++.
## ZaleLLnoLci i powiazania

-   Jest to plik wewnetrzny, doL'aczany tylko przez `luainterface.h`.
-   Wymaga definicji `LuaInterface`, `LuaObject`, `LuaException`.
-   Jest podstawa caL'ego systemu automatycznej konwersji typow, uLLywanego przez `luabinder`.

---
# z"" connection.cpp
## Opis ogolny

Plik `connection.cpp` zawiera implementacje klasy `Connection`, ktora jest niskopoziomowym opakowaniem na asynchroniczne gniazdo TCP (TCP socket) z biblioteki Boost.Asio. Zarzadza ona cyklem LLycia poL'aczenia, operacjami odczytu i zapisu oraz obsL'uga bL'edow.
## Zmienne globalne

-   `g_ioService`: Globalna instancja `boost::asio::io_service`, ktora jest sercem petli zdarzeL" dla wszystkich operacji sieciowych.
-   `Connection::m_outputStreams`: Statyczna lista, ktora dziaL'a jak pula buforow wyjLciowych. ZuLLyte bufory sa do niej zwracane, co pozwala na ich ponowne wykorzystanie i redukuje alokacje pamieci.
## Klasa `Connection`
## `Connection::Connection()`

Konstruktor. Inicjalizuje obiekty Boost.Asio (`timer`, `resolver`, `socket`) powiazane z `g_ioService`.
## `void Connection::poll()` i `void Connection::terminate()`

Statyczne metody, ktore zarzadzaja globalnym `g_ioService`. `poll()` przetwarza zdarzenia sieciowe, a `terminate()` zatrzymuje `io_service`.
## `void Connection::close()`

Zamyka poL'aczenie. Anuluje wszystkie aktywne operacje asynchroniczne, zamyka gniazdo i resetuje callbacki.
## `void Connection::connect(...)`

Rozpoczyna proces nawiazywania poL'aczenia. WywoL'uje `m_resolver.async_resolve` w celu przetL'umaczenia nazwy hosta na adres IP.
## `void Connection::write(uint8* buffer, size_t size)`

Dodaje dane do bufora wyjLciowego (`m_outputStream`). Aby uniknac zatorow (congestion), faktyczne wysL'anie danych jest opoLsniane o 0 milisekund za pomoca `m_delayedWriteTimer`. Oznacza to, LLe wysL'anie nastapi w nastepnej iteracji petli `io_service`, co pozwala na zgrupowanie wielu maL'ych zapisow w jeden wiekszy.
## Metody `read(...)`, `read_until(...)`, `read_some(...)`

Inicjuja asynchroniczne operacje odczytu danych z gniazda. Ustawiaja `m_recvCallback`, ktory zostanie wywoL'any po otrzymaniu danych, oraz `m_readTimer` do obsL'ugi timeoutu.
## Metody `on...()`

Sa to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio:
-   `onResolve`: WywoL'ywana po rozwiazaniu nazwy DNS. Inicjuje poL'aczenie.
-   `onConnect`: WywoL'ywana po nawiazaniu poL'aczenia. Ustawia opcje gniazda (np. `no_delay` - wyL'aczenie algorytmu Nagle'a) i wywoL'uje `m_connectCallback`.
-   `onCanWrite`: WywoL'ywana przez `m_delayedWriteTimer`. Inicjuje faktyczne wysL'anie danych.
-   `onWrite`: WywoL'ywana po zakoL"czeniu operacji zapisu. Zwraca bufor do puli.
-   `onRecv`: WywoL'ywana po otrzymaniu danych. Przekazuje dane do `m_recvCallback`.
-   `onTimeout`: WywoL'ywana, gdy upL'ynie czas oczekiwania na operacje.
## `void Connection::handleError(...)`

Centralna funkcja do obsL'ugi bL'edow sieciowych. Zapisuje bL'ad, wywoL'uje `m_errorCallback` i zamyka poL'aczenie.
## ZaleLLnoLci i powiazania

-   `framework/net/connection.h`: Plik nagL'owkowy.
-   `framework/core/application.h`, `eventdispatcher.h`: Do walidacji i planowania zdarzeL".
-   `boost/asio`: Kluczowa zaleLLnoLc do obsL'ugi sieci.
-   Jest uLLywana przez klase `Protocol` do implementacji protokoL'u komunikacyjnego z serwerem gry.

---
# z"" server.h
## Opis ogolny

Plik `server.h` deklaruje klase `Server`, ktora jest prostym opakowaniem na `boost::asio::ip::tcp::acceptor`. UmoLLliwia tworzenie serwera TCP, ktory nasL'uchuje na przychodzace poL'aczenia na okreLlonym porcie.
## Klasa `Server`
## Opis semantyczny
`Server` dziedziczy po `LuaObject`, co pozwala na tworzenie i zarzadzanie serwerami z poziomu skryptow Lua. Jego gL'ownym zadaniem jest akceptowanie nowych poL'aczeL" i przekazywanie ich do obsL'ugi (np. w formie obiektu `Connection`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Server(int port)` | Konstruktor, tworzy i bindowanie akceptor do podanego portu. |
| `static ServerPtr create(int port)` | Metoda fabryczna, ktora tworzy `Server` i opakowuje go w `shared_ptr`. |
| `bool isOpen()` | Zwraca `true`, jeLli serwer nasL'uchuje. |
| `void close()` | Zamyka akceptor, przestajac nasL'uchiwac. |
| `void acceptNext()` | Inicjuje asynchroniczna operacje oczekiwania na nastepne poL'aczenie. Po jego nadejLciu, wywoL'ywany jest `callback` `onAccept` w Lua. |
## Zmienne prywatne

-   `m_isOpen`: Flaga wskazujaca, czy serwer jest aktywny.
-   `m_acceptor`: Obiekt `tcp::acceptor` z Boost.Asio.
## ZaleLLnoLci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `boost/asio`: ULLywa `tcp::acceptor`.
-   Jest uLLywana do implementacji serwerow nasL'uchujacych w Lua, np. do niestandardowych narzedzi lub protokoL'ow.

---
# z"" connection.h
## Opis ogolny

Plik `connection.h` deklaruje klase `Connection`, ktora jest interfejsem do asynchronicznego poL'aczenia TCP. Jest to kluczowy element podsystemu sieciowego.
## Klasa `Connection`
## Opis semantyczny
`Connection` enkapsuluje `boost::asio::ip::tcp::socket` i zarzadza caL'ym cyklem LLycia poL'aczenia: od nawiazywania, przez wysyL'anie i odbieranie danych, aLL po zamykanie i obsL'uge bL'edow. DziaL'a w peL'ni asynchronicznie, integrujac sie z globalna petla zdarzeL" `g_ioService`. Dziedziczy po `LuaObject`, co umoLLliwia jej uLLycie w Lua.
## StaL'e

-   `READ_TIMEOUT`, `WRITE_TIMEOUT`: Czas (w sekundach) na zakoL"czenie operacji odczytu/zapisu.
-   `SEND_BUFFER_SIZE`, `RECV_BUFFER_SIZE`: Rozmiary buforow.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Statyczne** | |
| `static void poll()` | Przetwarza zdarzenia w globalnym `g_ioService`. |
| `static void terminate()` | Zatrzymuje `g_ioService`. |
| **Cykl LLycia** | |
| `void connect(...)` | Rozpoczyna asynchroniczne nawiazywanie poL'aczenia. |
| `void close()` | Zamyka poL'aczenie. |
| **Operacje I/O** | |
| `void write(...)` | Dodaje dane do kolejki wysyL'ania. |
| `void read(...)` | Rozpoczyna asynchroniczny odczyt okreLlonej liczby bajtow. |
| `void read_until(...)` | Odczytuje dane aLL do napotkania okreLlonego separatora. |
| `void read_some(...)` | Odczytuje dowolna iloLc dostepnych danych (nie wiecej niLL rozmiar bufora). |
| **Callbacki i stan** | |
| `void setErrorCallback(...)`| Ustawia funkcje zwrotna dla bL'edow. |
| `int getIp()` | Zwraca adres IP zdalnego hosta. |
| `boost::system::error_code getError()` | Zwraca ostatni bL'ad. |
| `bool isConnecting()` | Zwraca `true`, jeLli trwa nawiazywanie poL'aczenia. |
| `bool isConnected()` | Zwraca `true`, jeLli poL'aczenie jest aktywne. |
| `ticks_t getElapsedTicksSinceLastRead()` | Zwraca czas od ostatniej operacji odczytu (do wykrywania timeoutow na wyLLszym poziomie). |
## Zmienne chronione

-   `m_connectCallback`, `m_errorCallback`, `m_recvCallback`: Funkcje zwrotne.
-   `m_readTimer`, `m_writeTimer`, ...: Obiekty Boost.Asio (timery, resolver, socket).
-   `m_outputStream`, `m_inputStream`: Bufory do zapisu i odczytu.
-   `m_connected`, `m_connecting`: Flagi stanu.
## ZaleLLnoLci i powiazania

-   `framework/net/declarations.h`: Deklaracje typow.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/core/timer.h`: Do Lledzenia aktywnoLci.
-   Jest uLLywana przez `Protocol` do komunikacji z serwerem gry.
-   Jest zwracana przez `Server` po zaakceptowaniu nowego poL'aczenia.

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `net` sL'uLLy do wczesnych deklaracji (forward declarations) i definicji typow wskaLsnikow dla klas zwiazanych z obsL'uga sieci. Pomaga to unikac zaleLLnoLci cyklicznych i skraca czas kompilacji.
## Deklaracje
## `namespace asio`

Deklaruje, LLe `asio` jest aliasem dla `boost::asio`.
## Wczesne deklaracje klas

-   `InputMessage`
-   `OutputMessage`
-   `Connection`
-   `Protocol`
-   `Server`
-   `PacketPlayer`
-   `PacketRecorder`
## Definicje typow

Definiuje aliasy dla inteligentnych wskaLsnikow (`shared_object_ptr`) do klas sieciowych.

-   `InputMessagePtr`
-   `OutputMessagePtr`
-   `ConnectionPtr`
-   `ProtocolPtr`
-   `ServerPtr`
-   `PacketPlayerPtr`
-   `PacketRecorderPtr`
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doL'aczany przez wiekszoLc plikow nagL'owkowych w module `net`.

---
# z"" inputmessage.h
## Opis ogolny

Plik `inputmessage.h` deklaruje klase `InputMessage`, ktora jest narzedziem do parsowania przychodzacych pakietow sieciowych.
## Klasa `InputMessage`
## Opis semantyczny
`InputMessage` dziaL'a jak bufor z wskaLsnikiem odczytu. Przechowuje surowe dane pakietu i udostepnia metody do sekwencyjnego odczytywania z niego roLLnych typow danych (np. `getU8`, `getU16`, `getString`). Zarzadza rownieLL pozycja nagL'owka, co pozwala na oddzielenie metadanych pakietu (rozmiar, suma kontrolna) od jego wL'aLciwej zawartoLci (ciaL'a).
## StaL'e

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_HEADER_SIZE`: Maksymalny rozmiar nagL'owka (rezerwowane miejsce na poczatku bufora).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setBuffer(...)` | Kopiuje dane z `std::string` do wewnetrznego bufora. |
| `getBuffer()` | Zwraca caL'y pakiet (nagL'owek + ciaL'o) jako `std::string`. |
| `getBodyBuffer()`| Zwraca tylko ciaL'o pakietu. |
| `skipBytes(uint32 bytes)` | Przesuwa wskaLsnik odczytu. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby caL'kowite bez znaku. |
| `getString()` | Odczytuje string (poprzedzony dL'ugoLcia U16). |
| `getDouble()` | Odczytuje liczbe zmiennoprzecinkowa w niestandardowym formacie. |
| `peekU8()`, ... | Odczytuja wartoLc bez przesuwania wskaLsnika. |
| `decryptRsa(...)` | Deszyfruje fragment bufora za pomoca RSA. |
| `getHeaderSize()`, `getMessageSize()`, `getUnreadSize()` | Zwracaja informacje o rozmiarach. |
| `eof()` | Zwraca `true`, jeLli wszystkie dane zostaL'y odczytane. |
## Metody chronione (uLLywane przez `Protocol`)

-   `reset()`: Resetuje stan wiadomoLci.
-   `fillBuffer(...)`: Dopisuje dane do bufora.
-   `setHeaderSize(...)`: Ustawia rozmiar nagL'owka.
-   `readChecksum()`: Odczytuje i weryfikuje sume kontrolna.
## Zmienne prywatne

-   `m_headerPos`: Pozycja startowa nagL'owka.
-   `m_readPos`: Aktualna pozycja odczytu.
-   `m_messageSize`: CaL'kowity rozmiar wiadomoLci (bez nagL'owka).
-   `m_buffer`: Bufor na dane.
## ZaleLLnoLci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostepna w Lua.
-   Jest tworzona i zarzadzana przez `Protocol` do parsowania danych otrzymanych z `Connection`.

---
# z"" outputmessage.cpp
## Opis ogolny

Plik `outputmessage.cpp` zawiera implementacje klasy `OutputMessage`, ktora sL'uLLy do budowania wychodzacych pakietow sieciowych.
## Klasa `OutputMessage`
## `OutputMessage::OutputMessage()`

Konstruktor, wywoL'uje `reset()`.
## `void OutputMessage::reset()`

Resetuje stan wiadomoLci, ustawiajac wskaLsnik zapisu (`m_writePos`) i pozycje nagL'owka (`m_headerPos`) na poczatek obszaru na ciaL'o wiadomoLci.
## `void OutputMessage::setBuffer(const std::string& buffer)`

Kopiuje dane z `std::string` do bufora wiadomoLci.
## Metody `add...()`

SL'uLLa do dodawania roLLnych typow danych na koniec wiadomoLci.
-   `addU8`, `addU16`, `addU32`, `addU64`: Dodaja liczby caL'kowite, konwertujac je do porzadku Little Endian.
-   `addString`: Dodaje `std::string`, poprzedzajac go 2-bajtowa dL'ugoLcia.
-   `addRawString`: Dodaje `std::string` bez informacji o dL'ugoLci.
-   `addPaddingBytes`: Dodaje okreLlona liczbe bajtow wypeL'niajacych.
-   KaLLda z tych metod wywoL'uje `checkWrite` w celu sprawdzenia, czy jest wystarczajaco miejsca w buforze.
## `void OutputMessage::encryptRsa()`

Szyfruje ostatnie `N` bajtow bufora za pomoca klucza publicznego RSA, gdzie `N` to rozmiar klucza.
## Metody `write...()`

Metody te operuja na zarezerwowanym miejscu na nagL'owek (przed ciaL'em wiadomoLci):
-   `writeChecksum()`: Oblicza sume kontrolna Adler-32 dla ciaL'a wiadomoLci i zapisuje ja w nagL'owku.
-   `writeSequence()`: Zapisuje numer sekwencyjny pakietu.
-   `writeMessageSize()`: Zapisuje caL'kowity rozmiar ciaL'a wiadomoLci w nagL'owku.
## `void OutputMessage::checkWrite(int bytes)`

Sprawdza, czy dodanie `bytes` bajtow nie przekroczy maksymalnego rozmiaru bufora. JeLli tak, rzuca wyjatek.
## ZaleLLnoLci i powiazania

-   `framework/net/outputmessage.h`: Plik nagL'owkowy.
-   `framework/util/crypt.h`: ULLywa `g_crypt` do szyfrowania RSA i `stdext::adler32` do sum kontrolnych.
-   Jest tworzona przez kod logiki gry, wypeL'niana danymi, a nastepnie przekazywana do `Protocol::send()` w celu wysL'ania.

---
# z"" outputmessage.h
## Opis ogolny

Plik `outputmessage.h` deklaruje klase `OutputMessage`, ktora jest narzedziem do konstruowania wychodzacych pakietow sieciowych.
## Klasa `OutputMessage`
## Opis semantyczny
`OutputMessage` dziaL'a jak bufor z wskaLsnikiem zapisu. Udostepnia metody do dodawania roLLnych typow danych (`addU8`, `addString`, itp.), ktore sa doL'aczane na koL"cu bufora. Posiada rownieLL zarezerwowane miejsce na poczatku bufora na nagL'owek, ktory jest wypeL'niany tuLL przed wysL'aniem (np. rozmiarem wiadomoLci, suma kontrolna).
## StaL'e

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_STRING_LENGTH`: Maksymalna dL'ugoLc stringa.
-   `MAX_HEADER_SIZE`: Rozmiar zarezerwowanego miejsca na nagL'owek.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `reset()` | Resetuje wiadomoLc do stanu poczatkowego. |
| `setBuffer(...)` | Ustawia zawartoLc ciaL'a wiadomoLci. |
| `getBuffer()` | Zwraca gotowy pakiet (nagL'owek + ciaL'o) jako `std::string`. |
| `addU8()`, ..., `addString()` | Dodaja dane do ciaL'a wiadomoLci. |
| `encryptRsa()` | Szyfruje czeLc wiadomoLci za pomoca RSA. |
| `getWritePos()` | Zwraca aktualna pozycje zapisu. |
| `getMessageSize()` | Zwraca aktualny rozmiar ciaL'a wiadomoLci. |
| `setWritePos(...)`, `setMessageSize(...)` | Ustawiaja pozycje zapisu i rozmiar. |
## Metody chronione (uLLywane przez `Protocol`)

-   `getHeaderBuffer()`: Zwraca wskaLsnik na poczatek gotowego pakietu (poczatek nagL'owka).
-   `writeChecksum()`, `writeSequence()`, `writeMessageSize()`: WypeL'niaja nagL'orek odpowiednimi metadanymi.
## Zmienne prywatne

-   `m_headerPos`: Aktualna pozycja poczatku nagL'owka.
-   `m_writePos`: Aktualna pozycja zapisu w ciele wiadomoLci.
-   `m_messageSize`: Rozmiar caL'ego pakietu (nagL'owek + ciaL'o).
-   `m_buffer`: Bufor na dane.
## ZaleLLnoLci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostepna w Lua do tworzenia pakietow.
-   Jest uLLywana przez `Protocol` do przygotowania pakietow do wysL'ania przez `Connection`.

---
# z"" packet_player.cpp
## Opis ogolny

Plik `packet_player.cpp` zawiera implementacje klasy `PacketPlayer`, ktora umoLLliwia odtwarzanie wczeLniej nagranych sesji sieciowych. Jest to narzedzie do debugowania i testowania.
## Klasa `PacketPlayer`
## `PacketPlayer::PacketPlayer(const std::string& file)`

Konstruktor.
-   **DziaL'anie**:
    1.  Otwiera plik nagrania z katalogu `records/`.
    2.  Czyta plik linia po linii.
    3.  KaLLda linia zawiera typ pakietu (`<` dla przychodzacego, `>` dla wychodzacego), sygnature czasowa i dane pakietu w formacie heksadecymalnym.
    4.  Dekoduje dane heksadecymalne do postaci binarnej i zapisuje pakiety w odpowiednich kolejkach (`m_input` lub `m_output`).
## `PacketPlayer::~PacketPlayer()`

Destruktor. Anuluje zaplanowane zdarzenie (`m_event`), jeLli istnieje.
## `void PacketPlayer::start(...)`

Rozpoczyna odtwarzanie.
-   **DziaL'anie**:
    1.  Zapisuje czas startu (`m_start`).
    2.  Zapisuje callbacki do obsL'ugi "otrzymanych" pakietow i zdarzenia rozL'aczenia.
    3.  Planuje pierwsze wywoL'anie metody `process()` za 50ms.
## `void PacketPlayer::stop()`

Zatrzymuje odtwarzanie, anulujac zdarzenie.
## `void PacketPlayer::onOutputPacket(const OutputMessagePtr& packet)`

Metoda wywoL'ywana przez `Protocol`, gdy probuje on wysL'ac pakiet. W trybie odtwarzania, pakiety wychodzace sa analizowane (np. w celu wykrycia wylogowania), ale nie sa nigdzie wysyL'ane.
## `void PacketPlayer::process()`
## Opis semantyczny
GL'owna metoda petli odtwarzacza.
## DziaL'anie
1.  Iteruje po kolejce pakietow przychodzacych (`m_input`).
2.  Sprawdza sygnature czasowa kaLLdego pakietu. JeLli czas odtworzenia pakietu (`packet.first + m_start`) juLL minaL', wywoL'uje `m_recvCallback` z danymi pakietu i usuwa go z kolejki.
3.  JeLli kolejka nie jest pusta, planuje swoje nastepne wywoL'anie z opoLsnieniem rownym roLLnicy czasu do nastepnego pakietu.
4.  JeLli kolejka jest pusta, wywoL'uje `m_disconnectCallback`, symulujac koniec sesji.
## ZaleLLnoLci i powiazania

-   `framework/net/packet_player.h`: Plik nagL'owkowy.
-   `framework/core/clock.h`, `eventdispatcher.h`: Do zarzadzania czasem i planowania zdarzeL".
-   `boost/algorithm/hex.hpp`: Do dekodowania danych z formatu heksadecymalnego.
-   Jest uLLywana przez `Protocol` w trybie odtwarzania.

---
# z"" packet_player.h
## Opis ogolny

Plik `packet_player.h` deklaruje klase `PacketPlayer`, ktora sL'uLLy do odtwarzania nagranych sesji sieciowych z plikow.
## Klasa `PacketPlayer`
## Opis semantyczny
`PacketPlayer` odczytuje plik z zarejestrowanymi pakietami i ich sygnaturami czasowymi. Po uruchomieniu, symuluje przychodzace pakiety sieciowe, wywoL'ujac `callback` w odpowiednich odstepach czasu, zgodnie z nagraniem. Pozwala to na debugowanie i testowanie logiki klienta bez potrzeby L'aczenia sie z serwerem. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketPlayer(const std::string& file)` | Konstruktor, L'aduje nagranie z pliku. |
| `virtual ~PacketPlayer()` | Destruktor. |
| `void start(...)` | Rozpoczyna odtwarzanie sesji. Przyjmuje callbacki na otrzymanie pakietu i na rozL'aczenie. |
| `void stop()` | Zatrzymuje odtwarzanie. |
| `void onOutputPacket(...)` | Przechwytuje pakiety, ktore normalnie byL'yby wysL'ane, w celu symulacji (np. wykrycia wylogowania). |
## Zmienne prywatne

-   `m_start`: Czas rozpoczecia odtwarzania.
-   `m_event`: WskaLsnik na zaplanowane zdarzenie do przetwarzania pakietow.
-   `m_input`, `m_output`: Kolejki (`std::deque`) przechowujace pary (czas, dane pakietu) dla pakietow przychodzacych i wychodzacych.
-   `m_recvCallback`: `Callback` wywoL'ywany z danymi "otrzymanego" pakietu.
-   `m_disconnectCallback`: `Callback` wywoL'ywany na koniec sesji.
## ZaleLLnoLci i powiazania

-   `framework/core/eventdispatcher.h`: Do planowania zdarzeL".
-   `framework/net/outputmessage.h`: Do analizy pakietow wychodzacych.
-   Jest tworzona i uLLywana przez `Protocol` w trybie odtwarzania.

---
# z"" protocol.h
## Opis ogolny

Plik `protocol.h` deklaruje klase `Protocol`, ktora jest klasa bazowa do implementacji protokoL'ow komunikacji sieciowej.
## Klasa `Protocol`
## Opis semantyczny
`Protocol` jest abstrakcja wysokiego poziomu, ktora zarzadza poL'aczeniem (`Connection`) i implementuje logike specyficzna dla danego protokoL'u, taka jak szyfrowanie XTEA, obsL'uga sum kontrolnych, kompresja i sekwencjonowanie pakietow. Przetwarza surowe dane z `Connection` na obiekty `InputMessage` i przygotowuje `OutputMessage` do wysL'ania. Dziedziczy po `LuaObject`, co pozwala na tworzenie implementacji protokoL'ow w Lua.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `connect(...)` | Nawiazuje poL'aczenie z serwerem. |
| `disconnect()` | Zamyka poL'aczenie. |
| `setRecorder(...)` / `playRecord(...)` | WL'acza tryb nagrywania lub odtwarzania sesji. |
| `bool isConnected()` / `isConnecting()` | Zwracaja stan poL'aczenia. |
| `ConnectionPtr getConnection()` | Zwraca obiekt `Connection`. |
| **Konfiguracja protokoL'u** | |
| `generateXteaKey()`, `setXteaKey(...)`, `enableXteaEncryption()` | Zarzadzaja szyfrowaniem XTEA. |
| `enableChecksum()`, `enabledSequencedPackets()`, `enableBigPackets()`, `enableCompression()` | WL'aczaja roLLne cechy protokoL'u. |
| **Operacje I/O** | |
| `virtual void send(...)` | WysyL'a `OutputMessage`, opcjonalnie szyfrujac i dodajac nagL'owki. |
| `virtual void recv()` | Inicjuje proces odbierania nastepnego pakietu. |
## Metody chronione

-   `onConnect()`: Wirtualna metoda wywoL'ywana po nawiazaniu poL'aczenia. DomyLlnie wywoL'uje `onConnect` w Lua.
-   `onRecv(...)`: Wirtualna metoda wywoL'ywana po otrzymaniu i zdeserializowaniu peL'nego pakietu. DomyLlnie wywoL'uje `onRecv` w Lua.
-   `onError(...)`: Wirtualna metoda wywoL'ywana w przypadku bL'edu sieciowego.
## Zmienne

-   `m_xteaKey`: Klucz XTEA.
-   `m_packetNumber`: Licznik dla pakietow sekwencyjnych.
-   `m_player`, `m_recorder`: WskaLsniki na obiekty do odtwarzania/nagrywania.
-   `m_checksumEnabled`, `m_xteaEncryptionEnabled`, ...: Flagi konfiguracji protokoL'u.
-   `m_connection`: WskaLsnik na obiekt `Connection`.
-   `m_inputMessage`: Bufor na przychodzace dane.
-   `m_zstream`: StrumieL" ZLIB do dekompresji.
## ZaleLLnoLci i powiazania

-   `framework/net/declarations.h`, `inputmessage.h`, `outputmessage.h`, `connection.h`: Podstawowe klasy sieciowe.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/proxy/proxy.h`: Do integracji z systemem proxy.
-   Oznaczona jako `@bindclass`, jest kluczowym elementem do implementacji logiki sieciowej w Lua.

---
# z"" packet_recorder.cpp
## Opis ogolny

Plik `packet_recorder.cpp` zawiera implementacje klasy `PacketRecorder`, ktora sL'uLLy do nagrywania sesji sieciowej do pliku tekstowego.
## Klasa `PacketRecorder`
## `PacketRecorder::PacketRecorder(const std::string& file)`

Konstruktor.
-   **DziaL'anie**:
    1.  Zapisuje czas startu nagrywania (`m_start`).
    2.  Tworzy katalog `records/`, jeLli nie istnieje.
    3.  Otwiera plik o podanej nazwie w tym katalogu do zapisu.
## `void PacketRecorder::addInputPacket(const InputMessagePtr& packet)`

Nagrywa pakiet przychodzacy.
-   **DziaL'anie**:
    1.  Zapisuje do pliku znacznik `<`.
    2.  Zapisuje roLLnice czasu od startu nagrywania.
    3.  Zapisuje zawartoLc ciaL'a pakietu w formacie heksadecymalnym.
    4.  Dodaje znak nowej linii.
## `void PacketRecorder::addOutputPacket(const OutputMessagePtr& packet)`

Nagrywa pakiet wychodzacy.
-   **DziaL'anie**:
    1.  Ignoruje pierwszy pakiet wychodzacy (ktory zazwyczaj zawiera login i hasL'o), aby nie zapisywac wraLLliwych danych.
    2.  Zapisuje do pliku znacznik `>`.
    3.  Zapisuje roLLnice czasu.
    4.  Zapisuje caL'a zawartoLc pakietu (wraz z nagL'owkiem) w formacie heksadecymalnym.
    5.  Dodaje znak nowej linii.
## ZaleLLnoLci i powiazania

-   `framework/net/packet_recorder.h`: Plik nagL'owkowy.
-   `framework/core/clock.h`, `resourcemanager.h`: Do zarzadzania czasem i plikami.
-   `boost/algorithm/hex.hpp`: Do konwersji danych binarnych na format heksadecymalny.
-   Jest uLLywana przez `Protocol`, gdy wL'aczony jest tryb nagrywania.

---
# z"" protocol.cpp
## Opis ogolny

Plik `protocol.cpp` zawiera implementacje klasy `Protocol`, ktora stanowi baze dla protokoL'ow komunikacyjnych. Implementuje ona logike niskiego poziomu, taka jak szyfrowanie, sumy kontrolne i kompresje, delegujac obsL'uge samych pakietow do skryptow Lua.
## Klasa `Protocol`
## `Protocol::Protocol()`

Konstruktor. Inicjalizuje domyLlne flagi protokoL'u na `false` i przygotowuje strumieL" ZLIB do dekompresji.
## `void Protocol::connect(const std::string& host, uint16 port)`

Rozpoczyna poL'aczenie. JeLli `host` to "proxy" lub inny specjalny adres, uLLywa `g_proxy`. W przeciwnym razie tworzy nowy `Connection`.
## `void Protocol::disconnect()`

Zamyka poL'aczenie, zwalniajac `Connection` lub sesje proxy.
## `void Protocol::send(const OutputMessagePtr& outputMessage, bool rawPacket)`
## Opis semantyczny
Przygotowuje i wysyL'a pakiet.
## DziaL'anie
1.  JeLli wL'aczone jest nagrywanie, zapisuje pakiet.
2.  JeLli `rawPacket` jest `false`:
    -   Szyfruje pakiet za pomoca XTEA, jeLli wL'aczone.
    -   Dodaje sume kontrolna lub numer sekwencyjny.
    -   Dodaje rozmiar pakietu na poczatku.
3.  WysyL'a gotowy pakiet przez `Connection` lub `Proxy`.
4.  Resetuje `outputMessage`, aby mogL' byc ponownie uLLyty.
## `void Protocol::recv()`

Rozpoczyna proces odbierania nowego pakietu, instruujac `Connection`, aby najpierw odczytaL' nagL'owek o odpowiedniej dL'ugoLci.
## `void Protocol::internalRecvHeader(...)` i `internalRecvData(...)`

Handlery wywoL'ywane przez `Connection`. `internalRecvHeader` odczytuje rozmiar ciaL'a pakietu, a `internalRecvData` odczytuje reszte danych. `internalRecvData` nastepnie wykonuje deszyfrowanie, weryfikacje sumy kontrolnej i dekompresje, a na koL"cu wywoL'uje `onRecv` z gotowym `InputMessage`.
## `void Protocol::generateXteaKey()` i `setXteaKey(...)`

Metody do zarzadzania kluczem szyfrowania XTEA.
## `bool Protocol::xteaDecrypt(...)` i `void Protocol::xteaEncrypt(...)`

Implementacje algorytmu XTEA do szyfrowania i deszyfrowania buforow wiadomoLci.
## `void Protocol::onConnect()`, `onRecv(...)`, `onError(...)`

Metody wirtualne, ktore domyLlnie wywoL'uja odpowiednie funkcje w Lua (`onConnect`, `onRecv`, `onError`), przekazujac im kontrole nad logika protokoL'u.
## ZaleLLnoLci i powiazania

-   `framework/net/protocol.h`: Plik nagL'owkowy.
-   `framework/net/connection.h`, `packet_player.h`, `packet_recorder.h`: Komponenty sieciowe.
-   `framework/proxy/proxy.h`: Do integracji z proxy.
-   **ZLIB**: Do kompresji/dekompresji.
-   Jest to kluczowa klasa, ktora jest dziedziczona (w Lua) w celu zaimplementowania konkretnego protokoL'u gry.

---
# z"" server.cpp
## Opis ogolny

Plik `server.cpp` zawiera implementacje klasy `Server`, ktora umoLLliwia tworzenie prostych serwerow TCP nasL'uchujacych na przychodzace poL'aczenia.
## Zmienne globalne
## `g_ioService`

Globalny `io_service` z Boost.Asio, uLLywany rownieLL przez `Connection`, na ktorym dziaL'a akceptor serwera.
## Klasa `Server`
## `Server::Server(int port)`

Konstruktor. Tworzy i otwiera obiekt `boost::asio::ip::tcp::acceptor`, bindowanie go do wszystkich interfejsow (`tcp::v4()`) na podanym porcie.
## `ServerPtr Server::create(int port)`

Statyczna metoda fabryczna. Tworzy obiekt `Server`, opakowujac go w `shared_ptr`. ObsL'uguje wyjatki, ktore moga wystapic, jeLli port jest juLL zajety.
## `void Server::close()`

Zamyka serwer. Anuluje wszystkie oczekujace operacje akceptowania i zamyka akceptor.
## `void Server::acceptNext()`
## Opis semantyczny
Rozpoczyna asynchroniczne oczekiwanie na nowe poL'aczenie.
## DziaL'anie
1.  Tworzy nowy, pusty obiekt `Connection`.
2.  WywoL'uje `m_acceptor.async_accept`, przekazujac jej gniazdo nowego `Connection` oraz `callback` (lambde).
3.  Gdy nowe poL'aczenie zostanie nawiazane, `callback` jest wywoL'ywany.
4.  `Callback` ustawia stan `Connection` na `connected` i wywoL'uje funkcje `onAccept` w skrypcie Lua, przekazujac jej nowy obiekt `Connection` oraz ewentualny kod bL'edu.
## ZaleLLnoLci i powiazania

-   `framework/net/server.h`: Plik nagL'owkowy.
-   `framework/net/connection.h`: Tworzy obiekty `Connection` dla nowych poL'aczeL".
-   `boost/asio`: ULLywa `tcp::acceptor`.
-   Jest przeznaczona do uLLytku w Lua, co pozwala na tworzenie np. prostych serwerow pomocniczych, serwerow proxy lub narzedzi deweloperskich.

---
# z"" inputmessage.cpp
## Opis ogolny

Plik `inputmessage.cpp` zawiera implementacje klasy `InputMessage`, ktora jest narzedziem do parsowania przychodzacych pakietow sieciowych.
## Klasa `InputMessage`
## `InputMessage::InputMessage()`

Konstruktor, wywoL'uje `reset()`.
## `void InputMessage::reset()`

Resetuje stan wiadomoLci do wartoLci poczatkowych, ustawiajac pozycje odczytu i nagL'owka na `MAX_HEADER_SIZE`.
## `void InputMessage::setBuffer(const std::string& buffer)`

Ustawia zawartoLc ciaL'a wiadomoLci, kopiujac dane z `std::string` do wewnetrznego bufora.
## Metody `get...()`

Odczytuja dane z bufora, zaczynajac od bieLLacej pozycji `m_readPos`.
-   KaLLda metoda najpierw wywoL'uje `checkRead`, aby upewnic sie, LLe jest wystarczajaco duLLo danych do odczytania.
-   Nastepnie odczytuje dane z bufora, konwertujac je z porzadku Little Endian, jeLli to konieczne.
-   Na koniec przesuwa wskaLsnik `m_readPos`.
-   `getString` najpierw odczytuje 2-bajtowa dL'ugoLc, a potem sam string.
-   `getDouble` odczytuje niestandardowy format liczby zmiennoprzecinkowej.
## `bool InputMessage::decryptRsa(int size)`

Deszyfruje `size` bajtow z bieLLacej pozycji za pomoca klucza prywatnego RSA. Zwraca `true`, jeLli pierwszy zdeszyfrowany bajt to 0.
## `void InputMessage::fillBuffer(...)`

Dopisuje surowe dane do bufora w bieLLacej pozycji odczytu (uLLywane przez `Protocol` podczas odbierania danych z gniazda).
## `void InputMessage::setHeaderSize(uint32 size)`

Ustawia pozycje poczatku nagL'owka (`m_headerPos`), co efektywnie okreLla jego rozmiar.
## `bool InputMessage::readChecksum()`

Odczytuje 4-bajtowa sume kontrolna z bufora, oblicza sume kontrolna Adler-32 dla reszty danych i porownuje je.
## `void InputMessage::checkRead(int bytes)`

Prywatna metoda, ktora rzuca wyjatek, jeLli proba odczytu `bytes` bajtow wykroczyL'aby poza granice wiadomoLci.
## ZaleLLnoLci i powiazania

-   `framework/net/inputmessage.h`: Plik nagL'owkowy.
-   `framework/util/crypt.h`: Do deszyfracji RSA.
-   `client/map.h`: Potencjalna zaleLLnoLc, byc moLLe z starszej wersji.
-   Jest uLLywana przez `Protocol` do reprezentowania i parsowania przychodzacych pakietow.

---
# z"" packet_recorder.h
## Opis ogolny

Plik `packet_recorder.h` deklaruje klase `PacketRecorder`, ktora sL'uLLy do nagrywania sesji sieciowej do pliku tekstowego w celu poLsniejszej analizy lub odtworzenia.
## Klasa `PacketRecorder`
## Opis semantyczny
`PacketRecorder` przechwytuje pakiety przychodzace (`InputMessage`) i wychodzace (`OutputMessage`) i zapisuje je w czytelnym formacie do pliku. KaLLdy wpis zawiera znacznik kierunku (`<` lub `>`), sygnature czasowa i zawartoLc pakietu w postaci heksadecymalnej. Dziedziczy po `LuaObject`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketRecorder(const std::string& file)` | Konstruktor, otwiera plik do zapisu. |
| `virtual ~PacketRecorder()` | Destruktor. |
| `void addInputPacket(...)` | Zapisuje pakiet przychodzacy do pliku. |
| `void addOutputPacket(...)` | Zapisuje pakiet wychodzacy do pliku. |
## Zmienne prywatne

-   `m_start`: Czas rozpoczecia nagrywania.
-   `m_stream`: StrumieL" pliku do zapisu.
-   `m_firstOutput`: Flaga uLLywana do pominiecia pierwszego pakietu wychodzacego (zwykle zawierajacego hasL'o).
## ZaleLLnoLci i powiazania

-   `framework/net/inputmessage.h`, `outputmessage.h`: Przyjmuje obiekty tych typow do nagrania.
-   Jest tworzona i uLLywana przez `Protocol`, gdy wL'aczony jest tryb nagrywania.

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `otml` sL'uLLy do wczesnych deklaracji (forward declarations) i definicji typow dla klas zwiazanych z parserem OTML.
## Wczesne deklaracje

-   `OTMLNode`
-   `OTMLDocument`
-   `OTMLParser`
-   `OTMLEmitter`
## Definicje typow

-   `OTMLNodePtr`: `stdext::shared_object_ptr<OTMLNode>`
-   `OTMLDocumentPtr`: `stdext::shared_object_ptr<OTMLDocument>`
-   `OTMLNodeList`: `std::vector<OTMLNodePtr>`
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doL'aczany przez wszystkie pliki nagL'owkowe w module `otml`.

---
# z"" otmlparser.h
## Opis ogolny

Plik `otmlparser.h` deklaruje klase `OTMLParser`, ktora jest odpowiedzialna za parsowanie dokumentow w formacie OTML (OTClient Markup Language).
## Klasa `OTMLParser`
## Opis semantyczny
`OTMLParser` odczytuje dane linia po linii ze strumienia wejLciowego, analizuje wciecia (ktore definiuja hierarchie), a nastepnie parsuje tagi i wartoLci, budujac drzewo obiektow `OTMLNode`.
## Metody publiczne

-   `OTMLParser(OTMLDocumentPtr doc, std::istream& in)`: Konstruktor.
-   `void parse()`: GL'owna metoda rozpoczynajaca proces parsowania.
## Metody prywatne

-   `std::string getNextLine()`: Odczytuje nastepna linie ze strumienia.
-   `int getLineDepth(...)`: Oblicza poziom zagnieLLdLLenia na podstawie liczby spacji na poczatku linii.
-   `void parseLine(...)`: Przetwarza pojedyncza linie (sprawdza wciecia, komentarze, puste linie).
-   `void parseNode(...)`: Parsuje tag i wartoLc z linii i tworzy nowy `OTMLNode`.
## Zmienne prywatne

-   `currentDepth`, `currentLine`: Lsledza pozycje w pliku.
-   `doc`: WskaLsnik na dokument, ktory jest budowany.
-   `currentParent`: WskaLsnik na bieLLacy wezeL'-rodzica.
-   `parentMap`: Mapa do Lledzenia hierarchii.
-   `previousNode`: WskaLsnik na ostatnio dodany wezeL'.
-   `in`: Referencja do strumienia wejLciowego.
## ZaleLLnoLci i powiazania

-   `framework/otml/declarations.h`: Definicje typow.
-   Jest uLLywana przez `OTMLDocument::parse`.

---
# z"" otml.h
## Opis ogolny

Plik `otml.h` jest gL'ownym plikiem nagL'owkowym dla moduL'u OTML. Jego jedynym zadaniem jest doL'aczenie dwoch najwaLLniejszych plikow tego moduL'u: `otmldocument.h` i `otmlnode.h`.
## ZawartoLc

# include "otmldocument.h"
# include "otmlnode.h"
```
## ZaleLLnoLci i powiazania

-   UL'atwia doL'aczanie podstawowych funkcjonalnoLci OTML w innych czeLciach projektu, ktore potrzebuja zarowno `OTMLDocument`, jak i `OTMLNode`.

---
# z"" otmldocument.cpp
## Opis ogolny

Plik `otmldocument.cpp` zawiera implementacje klasy `OTMLDocument`, ktora reprezentuje caL'y dokument OTML i jest korzeniem drzewa wezL'ow.
## Klasa `OTMLDocument`
## `OTMLDocumentPtr OTMLDocument::create()`

Statyczna metoda fabryczna. Tworzy nowy, pusty dokument z domyLlnym tagiem "doc".
## `OTMLDocumentPtr OTMLDocument::parse(const std::string& fileName)`

Statyczna metoda, ktora L'aduje i parsuje dokument OTML z pliku. ULLywa `g_resources` do odczytania pliku do strumienia, a nastepnie wywoL'uje `parse(std::istream&, ...)`.
## `OTMLDocumentPtr OTMLDocument::parseString(const std::string& data, const std::string& source)`

Parsuje dokument z `std::string`.
## `OTMLDocumentPtr OTMLDocument::parse(std::istream& in, const std::::string& source)`

GL'owna metoda parsujaca.
1.  Tworzy nowy `OTMLDocument`.
2.  Tworzy `OTMLParser` dla tego dokumentu i strumienia.
3.  WywoL'uje `parser.parse()` w celu zbudowania drzewa wezL'ow.
4.  Zwraca gotowy dokument.
## `std::string OTMLDocument::emit()`

Konwertuje caL'e drzewo wezL'ow OTML z powrotem na format tekstowy, uLLywajac `OTMLEmitter`.
## `bool OTMLDocument::save(const std::string& fileName)`

Zapisuje wyemitowany dokument do pliku za pomoca `g_resources`.
## ZaleLLnoLci i powiazania

-   `framework/otml/otmldocument.h`: Plik nagL'owkowy.
-   `framework/otml/otmlparser.h`, `otmlemitter.h`: ULLywa parsera i emittera.
-   `framework/core/resourcemanager.h`: Do operacji na plikach.

---
# z"" otmldocument.h
## Opis ogolny

Plik `otmldocument.h` deklaruje klase `OTMLDocument`, ktora jest specjalizacja `OTMLNode` i reprezentuje korzeL" dokumentu OTML.
## Klasa `OTMLDocument`
## Opis semantyczny
`OTMLDocument` dziedziczy po `OTMLNode`, wiec jest jednoczeLnie wezL'em (korzeniem) i caL'ym dokumentem. Dodaje funkcjonalnoLc zwiazana z plikami: parsowanie z pliku/stringu i zapisywanie do pliku. Przechowuje rownieLL informacje o Lsrodle (`source`), z ktorego zostaL' zaL'adowany.
## Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static OTMLDocumentPtr create()` | Tworzy pusty dokument. |
| `static OTMLDocumentPtr parse(...)` | Parsuje dokument z pliku, stringu lub strumienia. |
## Metody publiczne (instancji)

| Metoda | Opis |
| :--- | :--- |
| `std::string emit()` | Konwertuje dokument na string w formacie OTML. |
| `bool save(const std::string& fileName)` | Zapisuje dokument do pliku. |
## ZaleLLnoLci i powiazania

-   `framework/otml/otmlnode.h`: Klasa bazowa.
-   Jest uLLywana jako punkt wejLcia do tworzenia i L'adowania struktur OTML w caL'ej aplikacji (np. w `UIManager`, `ConfigManager`).

---
# z"" otmlemitter.cpp
## Opis ogolny

Plik `otmlemitter.cpp` zawiera implementacje klasy `OTMLEmitter`, ktora jest odpowiedzialna za konwersje drzewa `OTMLNode` z powrotem do formatu tekstowego OTML.
## Klasa `OTMLEmitter`
## `std::string OTMLEmitter::emitNode(const OTMLNodePtr& node, int currentDepth)`
## Opis semantyczny
Rekurencyjna, statyczna metoda, ktora generuje tekstowa reprezentacje pojedynczego wezL'a i wszystkich jego dzieci.
## DziaL'anie
1.  Dodaje wciecie (2 spacje na poziom) odpowiednie dla `currentDepth`.
2.  Zapisuje tag wezL'a. JeLli wezeL' ma wartoLc lub jest unikalny, dodaje `:`. JeLli nie ma tagu, zapisuje `-`.
3.  Zapisuje wartoLc wezL'a:
    -   JeLli wartoLc to `null` (`m_null`), zapisuje `~`.
    -   JeLli wartoLc zawiera znaki nowej linii, formatuje ja jako blok wieloliniowy, uLLywajac `|`, `|-` lub `|+` w zaleLLnoLci od tego, jak maja byc traktowane koL"cowe znaki nowej linii.
    -   W przeciwnym razie, zapisuje wartoLc w tej samej linii.
4.  Rekurencyjnie wywoL'uje `emitNode` dla wszystkich dzieci, zwiekszajac `currentDepth`.
## ZaleLLnoLci i powiazania

-   `framework/otml/otmlemitter.h`: Plik nagL'owkowy.
-   `framework/otml/otmldocument.h`: ULLywana przez `OTMLDocument::emit()`.

---
# z"" otmlexception.cpp
## Opis ogolny

Plik `otmlexception.cpp` zawiera implementacje klasy `OTMLException`, ktora jest uLLywana do sygnalizowania bL'edow podczas parsowania lub przetwarzania dokumentow OTML.
## Klasa `OTMLException`
## Konstruktory

-   **`OTMLException(const OTMLNodePtr& node, const std::string& error)`**: Tworzy wyjatek zwiazany z konkretnym wezL'em. Komunikat bL'edu bedzie zawieraL' informacje o Lsrodle (`source`) tego wezL'a.
-   **`OTMLException(const OTMLDocumentPtr& doc, const std::string& error, int line)`**: Tworzy wyjatek zwiazany z caL'ym dokumentem, opcjonalnie podajac numer linii, w ktorej wystapiL' bL'ad parsowania.
## DziaL'anie
Oba konstruktory buduja szczegoL'owy komunikat bL'edu w `std::stringstream`, ktory jest nastepnie zapisywany w `m_what` i dostepny przez metode `what()`.
## ZaleLLnoLci i powiazania

-   `framework/otml/otmlexception.h`: Plik nagL'owkowy.
-   `framework/otml/otmldocument.h`: Do dostepu do LsrodL'a dokumentu.
-   Jest rzucana przez `OTMLParser` w przypadku bL'edow skL'adniowych i przez `OTMLNode` w przypadku bL'edow logicznych (np. brak wymaganego dziecka).

---
# z"" otmlexception.h
## Opis ogolny

Plik `otmlexception.h` deklaruje klase `OTMLException`, ktora jest typem wyjatku uLLywanym do sygnalizowania bL'edow zwiazanych z OTML.
## Klasa `OTMLException`
## Opis semantyczny
Dziedziczy po `stdext::exception`. Jest tworzona z informacja o kontekLcie bL'edu (wezeL' lub dokument oraz numer linii), co pozwala na generowanie precyzyjnych komunikatow o bL'edach, uL'atwiajacych debugowanie plikow OTML.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OTMLException(...)` | Konstruktory. |
| `virtual ~OTMLException()` | Destruktor. |
| `virtual const char* what() const throw()` | Zwraca sformatowany komunikat bL'edu. |
## Zmienne chronione

-   `m_what`: `std::string` przechowujaca komunikat bL'edu.
## ZaleLLnoLci i powiazania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa.
-   Jest rzucana przez `OTMLParser` i `OTMLNode`.

---
# z"" otmlemitter.h
## Opis ogolny

Plik `otmlemitter.h` deklaruje klase `OTMLEmitter`, ktora jest odpowiedzialna za proces "emitowania", czyli konwersji drzewa wezL'ow OTML z powrotem do jego tekstowej reprezentacji.
## Klasa `OTMLEmitter`
## Opis semantyczny
`OTMLEmitter` zawiera jedna statyczna metode, ktora rekurencyjnie przechodzi przez drzewo `OTMLNode` i buduje sformatowany `std::string` zgodny ze skL'adnia OTML, uwzgledniajac wciecia, tagi, wartoLci (w tym wieloliniowe) i hierarchie.
## Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static std::string emitNode(...)` | Generuje tekstowa reprezentacje podanego wezL'a i wszystkich jego dzieci. |
## ZaleLLnoLci i powiazania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   Jest uLLywana przez `OTMLDocument::emit()` i `OTMLNode::emit()`.

---
# z"" otmlparser.cpp
## Opis ogolny

Plik `otmlparser.cpp` zawiera implementacje klasy `OTMLParser`, ktora jest sercem mechanizmu parsowania jezyka OTML.
## Klasa `OTMLParser`
## `OTMLParser::OTMLParser(...)`

Konstruktor. Inicjalizuje stan parsera, ustawiajac bieLLacy wezeL'-rodzica na korzeL" dokumentu.
## `void OTMLParser::parse()`

GL'owna metoda, ktora w petli odczytuje kolejne linie ze strumienia (`getNextLine()`) i przekazuje je do `parseLine()`, aLL do koL"ca pliku.
## `int OTMLParser::getLineDepth(...)`

Oblicza poziom wciecia linii, liczac spacje na jej poczatku. Wymusza, aby wciecie byL'o wielokrotnoLcia dwoch spacji i zabrania uLLywania tabulatorow.
## `void OTMLParser::parseLine(std::string line)`

Przetwarza pojedyncza linie.
1.  Oblicza jej gL'ebokoLc.
2.  Usuwa biaL'e znaki z poczatku i koL"ca.
3.  Ignoruje puste linie i komentarze (`//`).
4.  Na podstawie roLLnicy miedzy bieLLaca gL'ebokoLcia a gL'ebokoLcia linii, aktualizuje `currentParent`, wchodzac w gL'ab hierarchii lub wracajac na wyLLszy poziom.
5.  WywoL'uje `parseNode` w celu sparsowania wL'aLciwej zawartoLci linii.
## `void OTMLParser::parseNode(const std::string& data)`

Parsuje tag i wartoLc z podanego ciagu znakow.
1.  Dzieli ciag na tag i wartoLc na podstawie separatora `:`.
2.  ObsL'uguje specjalny przypadek `-` dla wezL'ow bez tagu.
3.  ObsL'uguje wartoLci wieloliniowe (rozpoczynajace sie od `|`, `|-`, `|+`), odczytujac kolejne linie, dopoki wciecie sie zgadza.
4.  ObsL'uguje listy w nawiasach kwadratowych (`[...]`), dzielac je na osobne wartoLci.
5.  Tworzy nowy obiekt `OTMLNode`, ustawia jego wL'aLciwoLci (tag, wartoLc, LsrodL'o) i dodaje go do `currentParent`.
## ZaleLLnoLci i powiazania

-   `framework/otml/otmlparser.h`: Plik nagL'owkowy.
-   `framework/otml/otmldocument.h`, `otmlexception.h`: Do tworzenia i obsL'ugi bL'edow.
-   `boost/tokenizer.hpp`: Do parsowania list w nawiasach kwadratowych.

---
# z"" otmlnode.h
## Opis ogolny

Plik `otmlnode.h` deklaruje klase `OTMLNode`, ktora jest podstawowym budulcem drzewa dokumentu OTML. Reprezentuje pojedynczy wezeL', ktory moLLe miec tag, wartoLc i liste dzieci.
## Klasa `OTMLNode`
## Opis semantyczny
`OTMLNode` to uniwersalny kontener na dane w strukturze drzewiastej. Jest uLLywany do reprezentowania zarowno stylow UI, jak i samych widgetow w plikach `.otui`, a takLLe moduL'ow w `.otmod` i konfiguracji w plikach `.otml`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `static OTMLNodePtr create(...)` | Metody fabryczne do tworzenia nowych wezL'ow. |
| `tag()`, `size()`, `source()`, `rawValue()` | Gettery dla podstawowych wL'aLciwoLci. |
| `isUnique()`, `isNull()`, `hasTag()`, `hasValue()`, `hasChildren()` | Metody sprawdzajace stan wezL'a. |
| `setTag(...)`, `setValue(...)`, ... | Settery dla wL'aLciwoLci. |
| `get(const std::string& childTag)` | Zwraca pierwszy wezeL'-dziecko o danym tagu. |
| `at(const std::string& childTag)` | To samo co `get`, ale rzuca wyjatek, jeLli dziecko nie istnieje. |
| `addChild(...)`, `removeChild(...)` | Dodaje/usuwa dziecko. `addChild` obsL'uguje logike L'aczenia (merge) dla unikalnych wezL'ow. |
| `copy(...)`, `merge(...)`, `clear()`, `clone()` | Metody do manipulacji struktura wezL'a. |
| `children()` | Zwraca liste wszystkich dzieci. |
| **Szablonowe metody `value...`** | |
| `value<T>()` | Zwraca wartoLc wezL'a, rzutowana na typ `T`. |
| `valueAt<T>(...)` | Zwraca wartoLc dziecka o danym tagu. |
| `valueAtIndex<T>(...)` | Zwraca wartoLc dziecka o danym indeksie. |
| **Szablonowe metody `write...`** | |
| `write<T>(...)` | Ustawia wartoLc wezL'a. |
| `writeAt<T>(...)` | Tworzy i dodaje unikalne dziecko z dana wartoLcia. |
| `writeIn<T>(...)` | Tworzy i dodaje nie-unikalne dziecko z dana wartoLcia. |
| `emit()` | Konwertuje wezeL' i jego dzieci na string. |
## Zmienne chronione

-   `m_children`: Mapa przechowujaca dzieci pogrupowane wedL'ug tagow.
-   `m_tag`, `m_value`, `m_source`: Podstawowe wL'aLciwoLci.
-   `m_unique`, `m_null`: Flagi stanu.
## ZaleLLnoLci i powiazania

-   `framework/otml/declarations.h`: Definicje typow.
-   `framework/otml/otmlexception.h`: Do rzucania wyjatkow.
-   Jest to podstawowa klasa moduL'u OTML, uLLywana przez `OTMLParser`, `OTMLEmitter` i `OTMLDocument`.

---
# z"" otmlnode.cpp
## Opis ogolny

Plik `otmlnode.cpp` zawiera implementacje metod klasy `OTMLNode`.
## Klasa `OTMLNode`
## `OTMLNodePtr OTMLNode::create(...)`

Metody fabryczne, ktore tworza nowy `OTMLNode` i ustawiaja jego poczatkowe wL'aLciwoLci.
## `bool OTMLNode::hasChildren()`

Sprawdza, czy wezeL' ma jakiekolwiek dzieci, ktore nie sa `null`.
## `OTMLNodePtr OTMLNode::get(const std::string& childTag)`

Wyszukuje w mapie `m_children` pierwsze dziecko o podanym tagu, ktore nie jest `null`, i je zwraca.
## `void OTMLNode::addChild(const OTMLNodePtr& newChild)`

Dodaje nowe dziecko. Implementuje kluczowa logike:
-   JeLli nowe dziecko ma tag i jest unikalne (`isUnique()`), a dziecko o takim samym tagu juLL istnieje, to nowe dziecko jest L'aczone (`merge`) ze starym, effectively nadpisujac/dodajac wL'aLciwoLci.
-   W przeciwnym razie, jest po prostu dodawane do listy dzieci o danym tagu.
-   KaLLdemu dziecku nadawany jest unikalny, rosnacy indeks, aby zachowac kolejnoLc wstawiania.
## `bool OTMLNode::removeChild(...)`

Usuwa podane dziecko z listy.
## `void OTMLNode::copy(const OTMLNodePtr& node)`

GL'eboko kopiuje wszystkie wL'aLciwoLci i dzieci z innego wezL'a, zastepujac wL'asna zawartoLc.
## `void OTMLNode::merge(const OTMLNodePtr& node)`

Laczy zawartoLc innego wezL'a z bieLLacym. W przeciwieL"stwie do `copy`, nie czyLci istniejacych dzieci, lecz dodaje nowe (lub L'aczy, jeLli sa unikalne).
## `OTMLNodeList OTMLNode::children()`

Zwraca liste wszystkich nie-nullowych dzieci, posortowana wedL'ug ich indeksu wstawienia.
## `OTMLNodePtr OTMLNode::clone()`

Tworzy i zwraca gL'eboka kopie wezL'a i wszystkich jego dzieci.
## ZaleLLnoLci i powiazania

-   `framework/otml/otmlnode.h`: Plik nagL'owkowy.
-   `framework/otml/otmlemitter.h`: ULLywany w metodzie `emit()`.
-   Jest to implementacja centralnej struktury danych dla systemu OTML.

---
# z"" androidplatform.cpp
## Opis ogolny

Plik `androidplatform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla systemu Android. Jest kompilowany tylko wtedy, gdy zdefiniowano makro `ANDROID`.
## Klasa `Platform` (implementacja dla Androida)

Wiele metod jest pustymi implementacjami lub zwraca domyLlne wartoLci, poniewaLL ich funkcjonalnoLc nie jest dostepna lub nie ma sensu na platformie Android w taki sam sposob, jak na desktopie.

| Metoda | Implementacja na Androidzie |
| :--- | :--- |
| `processArgs(...)` | Pusta (argumenty sa obsL'ugiwane inaczej). |
| `spawnProcess(...)`| Zwraca `false`. |
| `getProcessId()` | Zwraca `getpid()`. |
| `isProcessRunning(...)` | Zwraca `false`. |
| `killProcess(...)` | Zwraca `false`. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | Zwraca wynik `getcwd()`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Puste/zwracaja `true`/`false`. Operacje na plikach sa obsL'ugiwane przez `ResourceManager`. |
| `getFileModificationTime(...)` | Zwraca 0. |
| `openUrl(std::string url, ...)` | Deleguje zadanie do `AndroidWindow::openUrl` poprzez `g_graphicsDispatcher`, aby zapewnic wykonanie w odpowiednim watku. |
| `openDir(...)` | Zwraca `true`. |
| `getCPUName()` | Zwraca pusty string. |
| `getTotalSystemMemory()` | Zwraca 0. |
| `getMemoryUsage()` | Zwraca 0. |
| `getOSName()` | Zwraca `"android"`. |
| `traceback(...)` | Zwraca pusty string (brak `backtrace` w standardzie). |
| `getMacAddresses()` | Zwraca pusty wektor. |
| `getUserName()` | Zwraca `"android"`. |
| `getDlls()`, `getProcesses()`, `getWindows()` | Zwracaja puste wektory. |
## ZaleLLnoLci i powiazania

-   `framework/platform/platform.h`: Plik nagL'owkowy.
-   `framework/platform/androidwindow.h`: Do otwierania URL.
-   `framework/core/eventdispatcher.h`: Do bezpiecznego watkowo wywoL'ywania metod z `AndroidWindow`.

---
# z"" androidwindow.cpp
## Opis ogolny

Plik `androidwindow.cpp` zawiera implementacje klasy `AndroidWindow`, ktora jest specyficzna dla platformy Android implementacja `PlatformWindow`. Zarzadza ona cyklem LLycia okna, obsL'uga wejLcia (dotyk, klawiatura) oraz kontekstem graficznym EGL/OpenGL ES.
## Zmienne globalne
## `g_androidWindow`

Globalna instancja `AndroidWindow`.
## Klasa `AndroidWindow`
## `AndroidWindow::AndroidWindow()`

Konstruktor. Inicjalizuje mape klawiszy (`m_keyMap`), tL'umaczac kody klawiszy Android (`AKEYCODE_*`) na wewnetrzne kody `Fw::Key`.
## `void AndroidWindow::internalInitGL()` i `internalDestroyGL()`

Metody do zarzadzania kontekstem graficznym EGL.
-   `internalInitGL`: Pobiera domyLlny wyLwietlacz EGL, wybiera konfiguracje, tworzy powierzchnie renderowania (`EGLSurface`) na podstawie natywnego okna Android i tworzy kontekst OpenGL ES 2.0.
-   `internalDestroyGL`: Zwalnia powierzchnie i kontekst EGL.
## `void AndroidWindow::init(struct android_app* app)`

GL'owna metoda inicjalizujaca. Zapisuje wskaLsnik na `android_app` i ustawia `callbacki` dla zdarzeL" cyklu LLycia aplikacji i zdarzeL" wejLciowych.
## `void AndroidWindow::poll()`

Przetwarza zdarzenia systemowe z kolejki Androida za pomoca `ALooper_pollAll`.
## `void AndroidWindow::swapBuffers()`

Zamienia bufory ekranu za pomoca `eglSwapBuffers`.
## `void AndroidWindow::handleCmd(int32_t cmd)`

Handler dla zdarzeL" cyklu LLycia aplikacji Android (np. `APP_CMD_INIT_WINDOW`, `APP_CMD_GAINED_FOCUS`). W odpowiedzi na te zdarzenia, tworzy lub niszczy kontekst GL i aktualizuje stan widocznoLci.
## `int AndroidWindow::handleInput(AInputEvent* event)`

Handler dla zdarzeL" wejLciowych.
-   **`AINPUT_EVENT_TYPE_MOTION` (dotyk)**:
    -   TL'umaczy zdarzenia dotyku (`ACTION_DOWN`, `ACTION_UP`, `ACTION_MOVE`) na zdarzenia myszy (`MousePress`, `MouseRelease`, `MouseMove`).
    -   Implementuje logike do symulacji klikniecia lewym i prawym przyciskiem myszy oraz przeciagania na ekranie dotykowym.
    -   ObsL'uguje wielodotyk, mapujac drugi i trzeci palec na `Fw::MouseTouch2` i `Fw::MouseTouch3`.
-   **`AINPUT_EVENT_TYPE_KEY` (klawiatura)**:
    -   TL'umaczy kod klawisza Android na kod `Fw::Key`.
    -   WywoL'uje `processKeyDown` lub `processKeyUp`.
## `void AndroidWindow::showTextEditor(...)`

WywoL'uje metode Javy (`showTextEdit`) za pomoca JNI, aby wyLwietlic natywna klawiature i pole edycji tekstu Androida.
## `void AndroidWindow::openUrl(std::string url)`

Otwiera URL za pomoca intencji Androida, wywoL'ujac metode Javy przez JNI.
## Funkcja `JNIEXPORT ... commitText(...)`

Funkcja C wywoL'ywana z kodu Javy, ktora przekazuje tekst wpisany na klawiaturze Androida z powrotem do aplikacji.
## ZaleLLnoLci i powiazania

-   NagL'owki NDK Androida (`android_native_app_glue.h`, `jni.h`).
-   NagL'owki EGL i GLES.
-   WspoL'pracuje z `GraphicalApplication` poprzez `callbacki` `m_onInputEvent`, `m_onResize`, `m_onClose`.

---
# z"" androidwindow.h
## Opis ogolny

Plik `androidwindow.h` deklaruje klase `AndroidWindow`, ktora jest implementacja `PlatformWindow` dla systemu Android.
## Klasa `AndroidWindow`
## Opis semantyczny
`AndroidWindow` integruje aplikacje z natywnym cyklem LLycia i systemem zdarzeL" Androida za pomoca struktury `android_app` z NDK. Zarzadza kontekstem graficznym EGL/GLES i tL'umaczy natywne zdarzenia wejLciowe (dotyk, klawisze sprzetowe) na wewnetrzny format `InputEvent`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Zarzadzanie cyklem LLycia** | |
| `init(struct android_app* app)` | Inicjalizuje okno, L'aczac je ze struktura `android_app`. |
| `handleCmd(int32_t cmd)` | ObsL'uguje komendy cyklu LLycia aplikacji od systemu Android. |
| `handleInput(AInputEvent* event)` | Przetwarza natywne zdarzenia wejLciowe. |
| **Interfejs `PlatformWindow`** | |
| `poll()` | Przetwarza zdarzenia z kolejki systemowej. |
| `swapBuffers()` | Zamienia bufory EGL. |
| `getDisplaySize()` | Zwraca rozmiar okna. |
| `showTextEditor(...)` | WyLwietla natywna klawiature Androida. |
| `openUrl(...)` | Otwiera URL. |
| ... | Implementacje innych metod `PlatformWindow`, czesto puste, poniewaLL pojecia takie jak "minimalizacja" czy "zmiana tytuL'u okna" nie maja bezpoLredniego odpowiednika na Androidzie. |
## Zmienne prywatne

-   `m_egl...`: Uchwyty do zasobow EGL (Display, Context, Surface, Config).
-   `m_multiInputEvent[3]`: Bufory na zdarzenia wielodotykowe.
## Zmienne globalne

-   `g_androidWindow`: Globalna instancja `AndroidWindow`.
## ZaleLLnoLci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Wymaga `android_native_app_glue.h` i nagL'owkow JNI/EGL/GLES, ktore sa czeLcia Android NDK.
-   W `platformwindow.cpp` wskaLsnik `g_window` jest przypisywany do `g_androidWindow`, gdy kompilacja odbywa sie dla Androida.

---
# z"" crashhandler.h
## Opis ogolny

Plik `crashhandler.h` deklaruje funkcje do instalacji i deinstalacji globalnego mechanizmu obsL'ugi awarii (crash handler).
## Funkcje
## `void installCrashHandler()`

Rejestruje handlery dla sygnaL'ow lub wyjatkow systemowych (w zaleLLnoLci od platformy), ktore sa wywoL'ywane w przypadku krytycznego bL'edu aplikacji (np. naruszenie ochrony pamieci).
## `void uninstallCrashHandler()`

Odinstalowuje wczeLniej zarejestrowane handlery.
## Dyrektywa preprocesora

CaL'a zawartoLc pliku jest objeta dyrektywa `#ifdef CRASH_HANDLER`, co oznacza, LLe funkcje te sa dostepne tylko wtedy, gdy opcja `CRASH_HANDLER` jest wL'aczona w CMake.
## ZaleLLnoLci i powiazania

-   Funkcje te sa implementowane w plikach specyficznych dla platformy: `unixcrashhandler.cpp` i `win32crashhandler.cpp`.
-   `installCrashHandler` jest zazwyczaj wywoL'ywana na samym poczatku dziaL'ania aplikacji.

---
# z"" platform.cpp
## Opis ogolny

Plik `platform.cpp` ma za zadanie jedynie zdefiniowac globalna instancje klasy `Platform`.
## Zmienne globalne
## `g_platform`

Globalna, jedyna instancja klasy `Platform`, ktora dostarcza interfejs do funkcji specyficznych dla systemu operacyjnego.

Platform g_platform;
```
## ZaleLLnoLci i powiazania

-   `framework/platform/platform.h`: Plik nagL'owkowy, ktory deklaruje klase `Platform`.
-   WL'aLciwa implementacja metod tej klasy znajduje sie w plikach `win32platform.cpp`, `unixplatform.cpp` i `androidplatform.cpp`, z ktorych tylko jeden jest kompilowany w zaleLLnoLci od docelowej platformy.

---
# z"" platformwindow.cpp
## Opis ogolny

Plik `platformwindow.cpp` jest kluczowym plikiem, ktory zarzadza implementacja okna specyficzna dla danej platformy. Jego gL'ownym zadaniem jest doL'aczenie odpowiedniego pliku nagL'owkowego (np. `win32window.h` lub `x11window.h`) i zdefiniowanie globalnego wskaLsnika `g_window`, ktory bedzie wskazywaL' na wL'aLciwa, platformowa instancje okna.
## Zmienne globalne
## `g_window`

Globalna referencja do obiektu okna. Jest to centralny punkt dostepu do wszystkich operacji zwiazanych z oknem w caL'ym frameworku. W zaleLLnoLci od platformy, wskazuje na instancje `WIN32Window`, `X11Window`, `AndroidWindow` lub `SDLWindow`.

# ifdef ANDROID
PlatformWindow& g_window = g_androidWindow;
# else
PlatformWindow& g_window = window; // gdzie 'window' to globalna instancja np. WIN32Window
# endif
```
## Klasa `PlatformWindow`
## `int PlatformWindow::loadMouseCursor(...)`

Laduje obraz kursora, sprawdza jego poprawnoLc (rozmiar 32x32, 4 kanaL'y kolorow) i deleguje wL'aLciwe tworzenie kursora do metody wirtualnej `internalLoadMouseCursor`, ktora jest zaimplementowana w klasach pochodnych.
## `void PlatformWindow::updateUnmaximizedCoords()`

Zapisuje aktualna pozycje i rozmiar okna, ale tylko wtedy, gdy okno nie jest zmaksymalizowane ani w trybie peL'noekranowym. SL'uLLy do przywracania poprzedniego stanu okna.
## `void PlatformWindow::processKeyDown(Fw::Key keyCode)`

ObsL'uguje zdarzenie wciLniecia klawisza.
-   Aktualizuje stan modyfikatorow (Ctrl, Alt, Shift).
-   Sprawdza, czy klawisz nie jest juLL wciLniety (obsL'uga auto-powtarzania).
-   Ustawia stan klawisza na wciLniety (`m_keysState`).
-   WysyL'a zdarzenia `KeyDownInputEvent` i `KeyPressInputEvent` do zarejestrowanego `callbacka`.
## `void PlatformWindow::processKeyUp(Fw::Key keyCode)`

ObsL'uguje zdarzenie zwolnienia klawisza.
-   Aktualizuje stan modyfikatorow.
-   Ustawia stan klawisza na zwolniony.
-   WysyL'a zdarzenie `KeyUpInputEvent`.
## `void PlatformWindow::releaseAllKeys()`

Resetuje stan wszystkich wciLnietych klawiszy i przyciskow myszy. WywoL'ywana np. gdy okno traci fokus.
## `void PlatformWindow::fireKeysPress()`

Metoda wywoL'ywana cyklicznie. Sprawdza, ktore klawisze sa wciLniete i od odpowiednio dL'ugiego czasu, a nastepnie generuje zdarzenia `KeyPressInputEvent` (auto-powtarzanie).
## ZaleLLnoLci i powiazania

-   WL'acza jeden z plikow nagL'owkowych specyficznych dla platformy (`win32window.h`, `x11window.h`, etc.).
-   `framework/core/eventdispatcher.h`: ULLywa `g_dispatcher` do bezpiecznego watkowo przetwarzania zdarzeL".
-   `framework/graphics/image.h`: Do L'adowania obrazow kursorow.
-   Jest to implementacja czeLci wspolnej dla wszystkich platform, podczas gdy specyfika jest w klasach pochodnych.

---
# z"" platform.h
## Opis ogolny

Plik `platform.h` deklaruje klase `Platform`, ktora jest interfejsem do funkcji specyficznych dla systemu operacyjnego. Zapewnia abstrakcje nad roLLnicami miedzy platformami (Windows, Linux, macOS, Android).
## Klasa `Platform`
## Opis semantyczny
`Platform` dostarcza zestaw statycznych metod do interakcji z systemem operacyjnym. Implementacja tych metod znajduje sie w plikach specyficznych dla platformy (np. `win32platform.cpp`, `unixplatform.cpp`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void processArgs(...)` | Przetwarza argumenty wiersza poleceL", konwertujac je do UTF-8. |
| `bool spawnProcess(...)` | Uruchamia nowy proces. |
| `int getProcessId()` | Zwraca ID bieLLacego procesu. |
| `bool isProcessRunning(...)` | Sprawdza, czy proces o danej nazwie jest uruchomiony. |
| `bool killProcess(...)` | Zamyka proces o danej nazwie. |
| `std::string getTempPath()` | Zwraca LcieLLke do katalogu tymczasowego. |
| `std::string getCurrentDir()` | Zwraca bieLLacy katalog roboczy. |
| `bool copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Podstawowe operacje na plikach. |
| `ticks_t getFileModificationTime(...)` | Zwraca czas ostatniej modyfikacji pliku. |
| `bool openUrl(...)` | Otwiera URL w domyLlnej przegladarce. |
| `bool openDir(...)` | Otwiera katalog w menedLLerze plikow. |
| `std::string getCPUName()` | Zwraca nazwe procesora. |
| `double getTotalSystemMemory()`| Zwraca caL'kowita iloLc pamieci RAM. |
| `double getMemoryUsage()` | Zwraca uLLycie pamieci przez bieLLacy proces. |
| `std::string getOSName()` | Zwraca nazwe systemu operacyjnego. |
| `std::string traceback(...)` | Generuje Llad stosu wywoL'aL" C++. |
| `std::vector<std::string> getMacAddresses()` | Zwraca liste adresow MAC. |
| `std::string getUserName()` | Zwraca nazwe zalogowanego uLLytkownika. |
| `std::vector<std::string> getDlls()` | (Windows) Zwraca liste zaL'adowanych bibliotek DLL. |
| `std::vector<std::string> getProcesses()` | Zwraca liste uruchomionych procesow. |
| `std::vector<std::string> getWindows()` | (Windows) Zwraca liste tytuL'ow otwartych okien. |
## Zmienne globalne

-   `g_platform`: Globalna instancja `Platform`.
## ZaleLLnoLci i powiazania

-   ULLywana w caL'ym projekcie do operacji, ktore wymagaja interakcji z systemem operacyjnym.
-   Jej implementacja jest dostarczana przez pliki `*.cpp` specyficzne dla platformy.

---
# z"" platformwindow.h
## Opis ogolny

Plik `platformwindow.h` deklaruje abstrakcyjna klase bazowa `PlatformWindow`, ktora definiuje wspolny interfejs do zarzadzania oknem aplikacji na roLLnych systemach operacyjnych.
## Klasa `PlatformWindow`
## Opis semantyczny
`PlatformWindow` jest klasa abstrakcyjna, ktora ukrywa szczegoL'y implementacyjne zwiazane z tworzeniem okna, obsL'uga zdarzeL" i zarzadzaniem kontekstem graficznym. KaLLda platforma (Windows, Linux, Android) dostarcza wL'asna, konkretna implementacje tej klasy.
## Metody czysto wirtualne (do implementacji przez klasy pochodne)

-   `init()`, `terminate()`: Cykl LLycia okna.
-   `move()`, `resize()`, `show()`, `hide()`, `minimize()`, `maximize()`: Zarzadzanie stanem okna.
-   `poll()`: Przetwarzanie zdarzeL" systemowych.
-   `swapBuffers()`: Zamiana buforow graficznych.
-   `set...()`: Metody do ustawiania wL'aLciwoLci okna (tytuL', ikona, VSync, etc.).
-   `get...()`: Metody do pobierania informacji (rozmiar ekranu, tekst ze schowka).
## Metody z implementacja

-   `loadMouseCursor(...)`: Laduje kursor z pliku.
-   `processKeyDown()`, `processKeyUp()`, `releaseAllKeys()`, `fireKeysPress()`: Implementuja logike obsL'ugi stanu klawiatury, ktora jest wspolna dla wszystkich platform.
-   Gettery dla stanu okna (`getSize`, `getPosition`, `isVisible`, `isKeyPressed`, etc.).
## Zmienne chronione

-   `m_keyMap`: Mapa tL'umaczaca kody klawiszy specyficzne dla platformy na wewnetrzne kody `Fw::Key`.
-   `m_keysState`, `m_lastKeysPress`: Mapy do Lledzenia stanu klawiszy.
-   `m_size`, `m_position`, `m_minimumSize`: WL'aLciwoLci geometryczne okna.
-   `m_inputEvent`: Obiekt do przechowywania danych o bieLLacym zdarzeniu wejLciowym.
-   `m_visible`, `m_focused`, `m_fullscreen`, `m_maximized`: Flagi stanu okna.
-   `m_onClose`, `m_onResize`, `m_onInputEvent`: Callbacki do powiadamiania `GraphicalApplication` o zdarzeniach.
## Zmienne globalne

-   `g_window`: Globalna referencja do aktywnej instancji `PlatformWindow`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/graphics/declarations.h`: Deklaracje typow graficznych.
-   Jest klasa bazowa dla `WIN32Window`, `X11Window`, `AndroidWindow`, `SDLWindow`.
-   Jest uLLywana przez `GraphicalApplication` do wszystkich operacji na oknie.

---
# z"" sdlwindow.cpp
## Opis ogolny

Plik `sdlwindow.cpp` zawiera implementacje klasy `SDLWindow`, ktora jest wersja `PlatformWindow` dla platformy Emscripten (WebAssembly), oparta na bibliotece SDL.

> **NOTE:** Implementacja jest w wiekszoLci pusta. Sugeruje to, LLe obsL'uga okna i zdarzeL" w Emscripten jest realizowana w inny sposob, prawdopodobnie poprzez gL'owna petle Emscripten i bezpoLrednie wywoL'ania JavaScript, a ta klasa jest jedynie "zaLlepka" (placeholderem), aby kod sie kompilowaL'.
## Klasa `SDLWindow`

Wszystkie metody implementujace interfejs `PlatformWindow` sa puste. Oznacza to, LLe operacje takie jak `resize`, `move`, `setTitle`, `poll` czy `swapBuffers` nie maja tutaj LLadnego efektu i musza byc obsL'ugiwane przez zewnetrzny kod (prawdopodobnie w gL'ownej petli `emscripten_set_main_loop`).
## `SDLWindow::SDLWindow()`

Konstruktor. Inicjalizuje domyLlne rozmiary i stan.
## `std::string SDLWindow::getPlatformType()`

Zwraca `"WASM"`.
## ZaleLLnoLci i powiazania

-   `framework/platform/sdlwindow.h`: Plik nagL'owkowy.
-   W `platformwindow.cpp` (niezaL'aczony, ale moLLna sie domyLlac), `g_window` jest ustawiane na instancje `SDLWindow` gdy kompilacja odbywa sie dla Emscripten.

---
# z"" sdlwindow.h
## Opis ogolny

Plik `sdlwindow.h` deklaruje klase `SDLWindow`, ktora jest implementacja `PlatformWindow` dla platformy Emscripten (WebAssembly), oparta na bibliotece SDL.
## Klasa `SDLWindow`
## Opis semantyczny
`SDLWindow` jest klasa-zaLlepka, ktora speL'nia kontrakt interfejsu `PlatformWindow`, ale wiekszoLc jej metod jest pusta. Logika okna dla Emscripten jest zazwyczaj obsL'ugiwana przez gL'owna petle zdefiniowana w `emscripten.h` i interakcje z API przegladarki, a nie przez tradycyjny model okienkowy.
## Metody publiczne
Deklaruje wszystkie metody wirtualne z `PlatformWindow` z pustymi implementacjami.
## Zmienne prywatne
-   `m_egl...`: Pola zwiazane z EGL, odziedziczone po logice Androida, ale prawdopodobnie nieuLLywane w kontekLcie Emscripten/SDL.
## ZaleLLnoLci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Jest to implementacja `PlatformWindow` uLLywana, gdy zdefiniowano `__EMSCRIPTEN__`.

---
# z"" unixcrashhandler.cpp
## Opis ogolny

Plik `unixcrashhandler.cpp` zawiera implementacje mechanizmu obsL'ugi awarii (crash handler) dla systemow uniksowych (Linux, macOS). Jest kompilowany tylko wtedy, gdy zdefiniowano `CRASH_HANDLER` i platforma nie jest Windows ani Emscripten.
## Funkcje
## `void crashHandler(int signum, siginfo_t* info, void* secret)`
## Opis semantyczny
Jest to funkcja obsL'ugi sygnaL'u, ktora jest wywoL'ywana przez system operacyjny w momencie wystapienia krytycznego bL'edu (np. bL'ad segmentacji). Jej zadaniem jest zebranie jak najwiekszej iloLci informacji o stanie programu w momencie awarii i zapisanie ich do logu.
## DziaL'anie
1.  Loguje komunikat "Application crashed".
2.  Tworzy strumieL" `stringstream` do budowy raportu.
3.  Zapisuje podstawowe informacje o aplikacji (nazwa, wersja, data kompilacji itp.).
4.  Pobiera kontekst procesora (`ucontext_t`) i zapisuje wartoLci rejestrow (np. `rip`, `rax` dla x64; `eip`, `eax` dla x86).
5.  Generuje Llad stosu wywoL'aL" (backtrace) za pomoca `backtrace()` i `backtrace_symbols()`.
6.  Opcjonalnie (jeLli zdefiniowano `DEMANGLE_BACKTRACE_SYMBOLS`), probuje zdemanglowac nazwy funkcji C++ w Lladzie stosu.
7.  Zapisuje caL'y raport do pliku `crash_report.log` i do gL'ownego logu aplikacji.
8.  Przywraca domyLlna obsL'uge sygnaL'ow, aby umoLLliwic systemowi operacyjnemu dokoL"czenie procesu zamykania aplikacji.
## `void installCrashHandler()`

Rejestruje funkcje `crashHandler` jako handler dla sygnaL'ow:
-   `SIGILL`: Nielegalna instrukcja.
-   `SIGSEGV`: Naruszenie ochrony pamieci.
-   `SIGFPE`: BL'ad operacji zmiennoprzecinkowej.
-   `SIGABRT`: SygnaL' przerwania (np. z `assert`).
## `void uninstallCrashHandler()`

Pusta funkcja, deinstalacja nie jest zaimplementowana.
## ZaleLLnoLci i powiazania

-   `framework/platform/crashhandler.h`: Plik nagL'owkowy.
-   `framework/global.h`, `framework/core/application.h`: Do pobierania informacji o aplikacji.
-   NagL'owki systemowe: `execinfo.h`, `ucontext.h`, `signal.h`.

---
# z"" unixplatform.cpp
## Opis ogolny

Plik `unixplatform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla systemow uniksowych (Linux, macOS). Jest kompilowany, gdy platforma nie jest ani Windows, ani Emscripten.
## Klasa `Platform` (implementacja dla Uniksa)

| Metoda | Implementacja na Uniksie |
| :--- | :--- |
| `spawnProcess(...)` | ULLywa `fork()` i `execv()` do uruchomienia nowego procesu. |
| `getProcessId()` | ULLywa `getpid()`. |
| `isProcessRunning(...)`, `killProcess(...)` | Puste implementacje. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | ULLywa `getcwd()`. |
| `copyFile(...)` | WywoL'uje systemowa komende `cp`. |
| `fileExists(...)` | ULLywa `stat()`. |
| `removeFile(...)` | ULLywa `unlink()`. |
| `getFileModificationTime(...)`| ULLywa `stat()` do odczytania `st_mtime`. |
| `openUrl(...)`, `openDir(...)` | WywoL'uje systemowa komende `xdg-open`. MoLLe to zrobic natychmiast lub w `EventDispatcher`. |
| `getCPUName()` | Parsuje plik `/proc/cpuinfo`. |
| `getTotalSystemMemory()` | Parsuje plik `/proc/meminfo`. |
| `getMemoryUsage()` | Pusta implementacja. |
| `getOSName()` | Parsuje plik `/etc/issue`. |
| `traceback(...)` | ULLywa `backtrace()` i `backtrace_symbols()` do generowania Lladu stosu, z opcjonalnym demanglowaniem nazw funkcji. |
| `getMacAddresses()` | Pusta implementacja. |
| `getUserName()` | ULLywa `getlogin_r()`. |
| `getDlls()`, `getProcesses()`, `getWindows()` | Puste implementacje (brak bezpoLrednich odpowiednikow). |
## ZaleLLnoLci i powiazania

-   `framework/platform/platform.h`: Plik nagL'owkowy.
-   NagL'owki systemowe POSIX (`unistd.h`, `sys/stat.h`, `execinfo.h`).
-   `framework/core/eventdispatcher.h`: Do asynchronicznego otwierania URL/katalogow.

---
# z"" win32crashhandler.cpp
## Opis ogolny

Plik `win32crashhandler.cpp` zawiera implementacje mechanizmu obsL'ugi awarii (crash handler) dla systemu Windows. Jest kompilowany, gdy zdefiniowano `WIN32` i `CRASH_HANDLER`.
## Funkcje
## `const char *getExceptionName(DWORD exceptionCode)`

Funkcja pomocnicza, ktora tL'umaczy kod wyjatku Windows (np. `EXCEPTION_ACCESS_VIOLATION`)  czytelna nazwe.
## `void Stacktrace(LPEXCEPTION_POINTERS e, std::stringstream& ss)`

Generuje Llad stosu wywoL'aL". ULLywa funkcji z biblioteki `DbgHelp.dll` (`StackWalk`, `SymGetModuleBase`, `SymGetSymFromAddr`), aby przejLc przez stos i odczytac nazwy funkcji i moduL'ow.
## `LONG CALLBACK ExceptionHandler(PEXCEPTION_POINTERS e)`

Starsza wersja handlera. Generuje raport tekstowy podobny do wersji uniksowej, zapisuje go do pliku i wyLwietla `MessageBox` z informacja o awarii.
## `LONG WINAPI UnhandledExceptionFilter2(PEXCEPTION_POINTERS exception)`

Nowsza, gL'owna funkcja obsL'ugi wyjatkow.
-   **DziaL'anie**:
    1.  Tworzy i zapisuje **minidump** awarii do plikow (`exception.dmp`, `exception_full.dmp`). Minidump to plik, ktory moLLna otworzyc w debuggerze (np. Visual Studio, WinDbg) w celu poLmiertnej analizy stanu programu.
    2.  JeLli `quiet_crash` jest `true` (ustawiane przez `uninstallCrashHandler`), cicho zamyka aplikacje.
    3.  W przeciwnym razie, wywoL'uje `ExceptionHandler` w celu wygenerowania raportu tekstowego i wyLwietlenia komunikatu.
## `void installCrashHandler()`

Rejestruje `UnhandledExceptionFilter2` jako globalny handler nieobsL'uLLonych wyjatkow za pomoca `SetUnhandledExceptionFilter`.
## `void uninstallCrashHandler()`

Ustawia flage `quiet_crash` na `true`. Jest to uLLywane np. podczas aktualizacji, aby cicho zamknac stara wersje klienta bez wyLwietlania okna bL'edu.
## ZaleLLnoLci i powiazania

-   `framework/platform/crashhandler.h`: Plik nagL'owkowy.
-   `framework/global.h`, `core/application.h`, `core/resourcemanager.h`.
-   NagL'owki Windows (`windows.h`, `imagehlp.h`, `DbgHelp.h`).

---
# z"" win32platform.cpp
## Opis ogolny

Plik `win32platform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla systemu Windows.
## Klasa `Platform` (implementacja dla Windows)

| Metoda | Implementacja na Windows |
| :--- | :--- |
| `processArgs(...)` | ULLywa `CommandLineToArgvW` do poprawnego sparsowania argumentow wiersza poleceL" (z obsL'uga Unicode). |
| `spawnProcess(...)`| ULLywa `ShellExecuteW`. |
| `getProcessId()` | ULLywa `GetCurrentProcessId()`. |
| `isProcessRunning(...)` | ULLywa `FindWindowA`. |
| `killProcess(...)` | ULLywa `FindWindowA`, `GetProcessId` i `TerminateProcess`. |
| `getTempPath()` | ULLywa `GetTempPathW`. |
| `getCurrentDir()` | ULLywa `GetCurrentDirectoryW`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | ULLywaja odpowiednikow z WinAPI (`CopyFileW`, `GetFileAttributesW`, `DeleteFileW`). |
| `getFileModificationTime(...)`| ULLywa `GetFileAttributesExW`. |
| `openUrl(...)`, `openDir(...)` | ULLywaja `ShellExecuteW`. |
| `getCPUName()` | Odczytuje wartoLc z rejestru systemowego. |
| `getTotalSystemMemory()`| ULLywa `GlobalMemoryStatusEx`. |
| `getMemoryUsage()` | ULLywa `GetProcessMemoryInfo`. |
| `getOSName()` | ULLywa `VerifyVersionInfo` i `GetProductInfo` do uzyskania szczegoL'owej nazwy wersji Windows. |
| `traceback(...)` | Prosta implementacja, zwraca tylko informacje o miejscu wywoL'ania. |
| `getMacAddresses()` | ULLywa `GetAdaptersInfo`. |
| `getUserName()` | ULLywa `GetUserNameA`. |
| `getDlls()` | ULLywa `EnumProcessModules`. |
| `getProcesses()` | ULLywa `CreateToolhelp32Snapshot` do iteracji po procesach. |
| `getWindows()` | ULLywa `EnumWindows` do iteracji po otwartych oknach. |
## ZaleLLnoLci i powiazania

-   `framework/platform/platform.h`: Plik nagL'owkowy.
-   NagL'owki WinAPI.
-   `boost/algorithm/string.hpp`: Do operacji na stringach.

---
# z"" win32window.cpp
## Opis ogolny

Plik `win32window.cpp` zawiera implementacje klasy `WIN32Window`, ktora jest specyficzna dla Windows implementacja `PlatformWindow`. Zarzadza ona natywnym oknem WinAPI, obsL'uga zdarzeL" i kontekstem graficznym (WGL dla OpenGL lub EGL dla OpenGL ES/DirectX).
## Klasa `WIN32Window`
## `WIN32Window::WIN32Window()`

Konstruktor. Inicjalizuje mape klawiszy (`m_keyMap`), tL'umaczac wirtualne kody klawiszy Windows (`VK_*`) na wewnetrzne kody `Fw::Key`.
## `void WIN32Window::init()`

Inicjalizuje okno, wywoL'ujac kolejno:
1.  `internalSetupTimerAccuracy()`: Zwieksza precyzje systemowego timera.
2.  `internalCreateWindow()`: Rejestruje klase okna i tworzy okno za pomoca `CreateWindowExA`.
3.  `internalCreateGLContext()`: Tworzy kontekst graficzny (WGL lub EGL).
4.  `internalRestoreGLContext()`: Aktywuje kontekst.
## `void WIN32Window::internalCreateGLContext()`

Implementacja tworzenia kontekstu graficznego:
-   **Dla OpenGL ES (`OPENGL_ES`)**: ULLywa EGL (ANGLE), probujac kolejno backendow D3D11, D3D9 i WARP, aby zapewnic maksymalna kompatybilnoLc.
-   **Dla standardowego OpenGL**: ULLywa WGL. Tworzy `PIXELFORMATDESCRIPTOR`, wybiera format pikseli i tworzy kontekst za pomoca `wglCreateContext`.
## `LRESULT WIN32Window::windowProc(...)`

GL'owna funkcja obsL'ugi zdarzeL" okna (Window Procedure). Odbiera komunikaty od systemu Windows.
-   Przekazuje zdarzenia do `dispatcherWindowProc` w celu obsL'ugi w gL'ownym watku aplikacji.
-   BezpoLrednio obsL'uguje niektore komunikaty, ktore musza byc przetworzone synchronicznie (np. `WM_SETCURSOR`, `WM_GETMINMAXINFO`).
## `LRESULT WIN32Window::dispatcherWindowProc(...)`

Metoda wywoL'ywana przez `g_dispatcher` w gL'ownym watku. TL'umaczy komunikaty Windows (`WM_KEYDOWN`, `WM_LBUTTONDOWN`, `WM_MOUSEMOVE` itp.) na wewnetrzne `InputEvent` i przekazuje je do `m_onInputEvent` (czyli do `GraphicalApplication`).
## `void WIN32Window::poll()`

Przetwarza kolejke komunikatow Windows za pomoca `PeekMessage`, `TranslateMessage` i `DispatchMessage`.
## `void WIN32Window::swapBuffers()`

Zamienia bufory ekranu za pomoca `SwapBuffers` (dla WGL) lub `eglSwapBuffers` (dla EGL).
## `void WIN32Window::setVerticalSync(bool enable)`

WL'acza/wyL'acza synchronizacje pionowa, uLLywajac rozszerzeL" WGL (`WGL_EXT_swap_control`).
## Inne metody

Implementuja interfejs `PlatformWindow`, opakowujac odpowiednie funkcje WinAPI (np. `SetWindowTextW` dla `setTitle`, `ShellExecuteW` dla `openUrl`).
## ZaleLLnoLci i powiazania

-   NagL'owki WinAPI.
-   NagL'owki OpenGL/EGL/WGL.
-   WspoL'pracuje z `GraphicalApplication` i `Mouse`.

---
# z"" win32window.h
## Opis ogolny

Plik `win32window.h` deklaruje klase `WIN32Window`, ktora jest implementacja `PlatformWindow` dla systemu Windows.
## Klasa `WIN32Window`
## Opis semantyczny
`WIN32Window` enkapsuluje uchwyty i logike zwiazana z natywnym oknem WinAPI. Zarzadza jego cyklem LLycia, obsL'uga komunikatow systemowych i tworzeniem kontekstu graficznego (WGL dla OpenGL lub EGL dla OpenGL ES przez ANGLE).
## Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnetrznego zarzadzania oknem i kontekstem GL.
-   `windowProc(...)`: GL'owna funkcja obsL'ugi komunikatow Windows.
-   `dispatcherWindowProc(...)`: Handler komunikatow wykonywany w gL'ownym watku.
-   `retranslateVirtualKey(...)`: TL'umaczy kody klawiszy WinAPI.
-   `getClientRect()`, `getWindowRect()`, `adjustWindowRect()`: Metody pomocnicze do geometrii okna.
## Zmienne prywatne

-   `m_window`: Uchwyt `HWND` do okna.
-   `m_instance`: Uchwyt `HINSTANCE` do moduL'u aplikacji.
-   `m_deviceContext`: Uchwyt `HDC` do kontekstu urzadzenia.
-   `m_cursors`: Wektor uchwytow `HCURSOR`.
-   `m_cursor`, `m_defaultCursor`: Aktywny i domyLlny kursor.
-   `m_hidden`: Flaga ukrycia okna.
-   `m_egl...` / `m_wglContext`: Uchwyty do zasobow EGL lub WGL.
## ZaleLLnoLci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   NagL'owki WinAPI i OpenGL/EGL.

---
# z"" x11window.h
## Opis ogolny

Plik `x11window.h` deklaruje klase `X11Window`, ktora jest implementacja `PlatformWindow` dla systemow uniksowych uLLywajacych serwera X11 (gL'ownie Linux).
## Klasa `X11Window`
## Opis semantyczny
`X11Window` zarzadza natywnym oknem X11, obsL'uga jego zdarzeL" oraz tworzeniem kontekstu graficznego (GLX dla OpenGL lub EGL dla OpenGL ES).
## Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnetrznego zarzadzania oknem i kontekstem GL.
-   `getExtensionProcAddress(...)`, `isExtensionSupported(...)`: Do obsL'ugi rozszerzeL" GLX/EGL.
## Zmienne prywatne

-   `m_display`: WskaLsnik na `Display` (poL'aczenie z serwerem X11).
-   `m_visual`: Informacje o wizualu (gL'ebia kolorow itp.).
-   `m_window`: ID okna.
-   `m_rootWindow`: ID okna gL'ownego.
-   `m_colormap`: Mapa kolorow.
-   `m_cursors`: Wektor kursorow.
-   `m_cursor`, `m_hiddenCursor`: Aktywny i ukryty kursor.
-   `m_xim`, `m_xic`: Do obsL'ugi metod wprowadzania tekstu.
-   `m_wmDelete`: Atom do obsL'ugi zdarzenia zamkniecia okna.
-   `m_glxContext` / `m_egl...`: Uchwyty do zasobow GLX lub EGL.
## ZaleLLnoLci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   NagL'owki X11, GLX, EGL.

---
# z"" x11window.cpp
## Opis ogolny

Plik `x11window.cpp` zawiera implementacje klasy `X11Window` dla systemow uniksowych z X11.
## Klasa `X11Window`
## `X11Window::X11Window()`

Konstruktor. Inicjalizuje mape klawiszy, tL'umaczac `KeySym` z X11 na `Fw::Key`.
## `void X11Window::init()`

Inicjalizuje okno, wywoL'ujac kolejno:
1.  `internalOpenDisplay()`: Otwiera poL'aczenie z serwerem X11.
2.  `internalCheckGL()`: Sprawdza dostepnoLc GLX/EGL.
3.  `internalChooseGLVisual()`: Wybiera odpowiedni format wizualny.
4.  `internalCreateGLContext()`: Tworzy kontekst graficzny.
5.  `internalCreateWindow()`: Tworzy okno X11.
## `void X11Window::internalCreateWindow()`

Tworzy okno za pomoca `XCreateWindow`, ustawia atrybuty, w tym maske zdarzeL", i przygotowuje obsL'uge zamkniecia okna przez menedLLera okien. Inicjalizuje rownieLL XIM/XIC do obsL'ugi wprowadzania tekstu.
## `void X11Window::poll()`

Przetwarza kolejke zdarzeL" X11 za pomoca `XPending` i `XNextEvent`. TL'umaczy zdarzenia X11 (`KeyPress`, `ButtonPress`, `MotionNotify`, `ConfigureNotify` itp.) na wewnetrzne `InputEvent` i wywoL'uje odpowiednie `callbacki` w `g_dispatcher`. ObsL'uguje rownieLL logike auto-powtarzania klawiszy i wprowadzania tekstu.
## `void X11Window::swapBuffers()`

Zamienia bufory ekranu za pomoca `glXSwapBuffers` (dla GLX) lub `eglSwapBuffers` (dla EGL).
## `void X11Window::setFullscreen(bool fullscreen)`

Zmienia stan okna na peL'noekranowy, wysyL'ajac odpowiedni komunikat `_NET_WM_STATE` do menedLLera okien.
## `void X11Window::setClipboardText(...)` i `getClipboardText()`

Implementuja obsL'uge schowka za pomoca mechanizmu selekcji X11.
## Inne metody

Implementuja interfejs `PlatformWindow`, opakowujac odpowiednie funkcje X11 (np. `XStoreName` dla `setTitle`, `XMoveWindow` dla `move`).
## ZaleLLnoLci i powiazania

-   NagL'owki X11, GLX, EGL.
-   WspoL'pracuje z `GraphicalApplication`.

---
# z"" proxy.cpp
## Opis ogolny

Plik `proxy.cpp` zawiera implementacje klasy `ProxyManager`, ktora zarzadza systemem proxy do komunikacji z serwerem gry.
## Zmienne globalne
## `g_proxy`

Globalna instancja `ProxyManager`.
## Klasa `ProxyManager`
## `void ProxyManager::init()` i `terminate()`

Uruchamiaja i zatrzymuja dedykowany watek sieciowy, w ktorym dziaL'a `io_context` dla operacji proxy.
## `void ProxyManager::clear()`

Zamyka wszystkie aktywne sesje i poL'aczenia z serwerami proxy.
## `bool ProxyManager::isActive()`

Zwraca `true`, jeLli skonfigurowano co najmniej jeden serwer proxy.
## `void ProxyManager::addProxy(...)`

Dodaje nowy serwer proxy do puli. Tworzy obiekt `Proxy` i uruchamia go.
## `void ProxyManager::removeProxy(...)`

Usuwa serwer proxy z puli.
## `uint32_t ProxyManager::addSession(...)`

Tworzy nowa sesje proxy dla poL'aczenia z serwerem gry. Tworzy obiekt `Session` i zwraca jego unikalne ID.
## `void ProxyManager::removeSession(...)`

Zamyka sesje o danym ID.
## `void ProxyManager::send(...)`

WysyL'a pakiet w ramach danej sesji. Znajduje odpowiedni obiekt `Session` i przekazuje mu pakiet.
## `int ProxyManager::getPing()`

Zwraca najlepszy (najniLLszy) ping spoLrod wszystkich aktywnych i poL'aczonych serwerow proxy.
## ZaleLLnoLci i powiazania

-   `framework/proxy/proxy.h`: Plik nagL'owkowy.
-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`.
-   Jest uLLywana przez `Protocol` do tunelowania poL'aczenia przez serwery proxy.

---
# z"" proxy.h
## Opis ogolny

Plik `proxy.h` deklaruje klase `ProxyManager`, ktora jest singletonem (`g_proxy`) odpowiedzialnym za zarzadzanie caL'ym systemem poL'aczeL" proxy. Stanowi on gL'owny punkt wejLcia do konfiguracji i wykorzystania tunelowania ruchu sieciowego.
## Klasa `ProxyManager`
## Opis semantyczny
`ProxyManager` zarzadza pula dostepnych serwerow proxy (obiekty `Proxy`) oraz pula aktywnych sesji klienta (obiekty `Session`). Jego zadaniem jest koordynacja miedzy sesjami a serwerami proxy, dynamiczne wybieranie najlepszych serwerow do tunelowania ruchu oraz dostarczanie interfejsu do zarzadzania tym procesem z poziomu aplikacji i skryptow Lua. DziaL'a w dedykowanym watku sieciowym, aby nie blokowac gL'ownego watku aplikacji.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Uruchamia i zatrzymuje watek sieciowy `ProxyManager`. |
| `clear()` | Zamyka wszystkie aktywne sesje i poL'aczenia z serwerami proxy. |
| `setMaxActiveProxies(int value)` | Ustawia, przez ile najlepszych (pod wzgledem pingu) serwerow proxy ma byc jednoczeLnie tunelowany ruch dla kaLLdej sesji. |
| `isActive()` | Zwraca `true`, jeLli co najmniej jeden serwer proxy jest skonfigurowany. |
| `addProxy(...)` / `removeProxy(...)` | Dodaje lub usuwa serwer proxy z puli dostepnych serwerow. |
| `uint32_t addSession(...)` | Tworzy nowa sesje proxy dla poL'aczenia z serwerem gry. Zwraca unikalne ID sesji. |
| `void removeSession(uint32_t sessionId)` | Zamyka i usuwa sesje o podanym ID. |
| `void send(uint32_t sessionId, ProxyPacketPtr packet)` | WysyL'a pakiet w ramach okreLlonej sesji. `ProxyManager` przekazuje go do odpowiedniego obiektu `Session`. |
| `std::map<...> getProxies()` | Zwraca mape dostepnych serwerow proxy wraz z ich pingiem. |
| `std::map<...> getProxiesDebugInfo()` | Zwraca szczegoL'owe informacje diagnostyczne o kaLLdym proxy. |
| `int getPing()` | Zwraca najniLLszy ping spoLrod wszystkich aktywnych serwerow proxy. |
## Zmienne prywatne

-   `m_io`: Kontekst `io_context` z Boost.Asio, na ktorym dziaL'aja wszystkie operacje sieciowe proxy.
-   `m_guard`: Obiekt `work_guard`, ktory zapobiega zakoL"czeniu dziaL'ania `m_io`, dopoki `ProxyManager` jest aktywny.
-   `m_working`: Flaga kontrolujaca dziaL'anie watku.
-   `m_thread`: Dedykowany watek dla operacji sieciowych proxy.
-   `m_maxActiveProxies`: Maksymalna liczba proxy uLLywanych przez jedna sesje.
-   `m_proxies`: Lista wskaLsnikow na dostepne obiekty `Proxy`.
-   `m_sessions`: Lista wskaLsnikow na aktywne obiekty `Session`.
## Zmienne globalne

-   `g_proxy`: Globalna instancja `ProxyManager`.
## ZaleLLnoLci i powiazania

-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`, ktorymi zarzadza.
-   Jest uLLywana przez `Protocol` do tworzenia tunelowanych poL'aczeL".
-   Jej API jest dostepne w Lua (przez `luafunctions.cpp`), co pozwala na dynamiczna konfiguracje proxy ze skryptow.

---
# z"" proxy_client.h
## Opis ogolny

Plik `proxy_client.h` deklaruje dwie kluczowe klasy dla systemu proxy: `Proxy` i `Session`. Te klasy implementuja logike klienta, ktory L'aczy sie z serwerami proxy i tuneluje przez nie ruch sieciowy.
## Definicje typow

-   `ProxyPacket`: Alias dla `std::vector<uint8_t>`, reprezentuje pojedynczy pakiet.
-   `ProxyPacketPtr`: Alias dla `std::shared_ptr<ProxyPacket>`.
-   `Session`, `SessionPtr`: Wczesna deklaracja i alias dla wskaLsnika na `Session`.
## Klasa `Proxy`
## Opis semantyczny
`Proxy` reprezentuje pojedyncze, trwaL'e poL'aczenie z jednym serwerem proxy. Jego zadaniem jest utrzymanie poL'aczenia, monitorowanie jego jakoLci (ping), przesyL'anie pakietow dla wielu sesji oraz raportowanie swojego stanu do `ProxyManager`.
## StaL'e i typy wyliczeniowe

-   `CHECK_INTERVAL`: InterwaL' (w ms) sprawdzania stanu poL'aczenia i wysyL'ania pingow.
-   `BUFFER_SIZE`: Rozmiar bufora odczytu.
-   `enum ProxyState`: Definiuje stany, w jakich moLLe znajdowac sie poL'aczenie z proxy (np. `STATE_NOT_CONNECTED`, `STATE_CONNECTING`, `STATE_CONNECTED`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Proxy(...)` | Konstruktor. |
| `void start()` | Inicjuje cykl LLycia obiektu, dodajac go do globalnej puli i uruchamiajac petle `check`. |
| `void terminate()` | Zamyka poL'aczenie i usuwa obiekt z globalnej puli. |
| `uint32_t getPing()` | Zwraca opoLsnienie do serwera proxy, uwzgledniajac priorytet. |
| `uint32_t getRealPing()` | Zwraca rzeczywiste opoLsnienie (bez priorytetu). |
| `bool isConnected()` | Zwraca `true`, jeLli poL'aczenie jest w stanie `STATE_CONNECTED`. |
| `std::string getDebugInfo()`| Zwraca informacje diagnostyczne. |
| `bool isActive()` | Zwraca `true`, jeLli przez to proxy przechodzi ruch co najmniej jednej sesji. |
| `void addSession(...)` | WysyL'a do serwera proxy polecenie utworzenia nowej sesji tunelowania. |
| `void removeSession(...)` | WysyL'a polecenie zamkniecia sesji. |
| `void send(...)` | Dodaje pakiet do kolejki wysyL'ania do serwera proxy. |
## Klasa `Session`
## Opis semantyczny
`Session` reprezentuje pojedyncza sesje klienta z serwerem gry, ktora jest tunelowana przez jeden lub wiecej serwerow proxy. MoLLe dziaL'ac w dwoch trybach: jako serwer (akceptujac lokalne poL'aczenie od klienta gry) lub jako klient (gdy jest tworzona bezpoLrednio przez `Protocol`). Odpowiada za dynamiczne wybieranie najlepszych `Proxy` do wysyL'ania pakietow oraz za re-asemblacje pakietow przychodzacych, ktore moga docierac z roLLnych `Proxy` i w roLLnej kolejnoLci.
## StaL'e

-   `CHECK_INTERVAL`: InterwaL' (w ms) sprawdzania stanu sesji i wyboru proxy.
-   `BUFFER_SIZE`: Rozmiar bufora.
-   `TIMEOUT`: Czas (w ms) braku aktywnoLci, po ktorym sesja jest zamykana.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Session(...)` | Konstruktory dla trybu serwera i klienta. |
| `uint32_t getId()` | Zwraca unikalne ID sesji. |
| `void start(...)` | Uruchamia sesje, rozpoczynajac petle `check` i (w trybie serwera) nasL'uchiwanie na pakiety od klienta. |
| `void terminate(...)` | Zamyka sesje, informujac powiazane `Proxy` i klienta. |
| `void onPacket(...)` | Handler dla pakietow przychodzacych **od klienta gry**. Opakowuje je w protokoL' proxy i wysyL'a. |
| `void onProxyPacket(...)` | Handler dla pakietow przychodzacych **od serwerow proxy**. Odpakowuje je, sprawdza kolejnoLc i przekazuje do klienta gry. |
## ZaleLLnoLci i powiazania

-   **Boost.Asio**: Fundamentalna zaleLLnoLc do wszystkich operacji sieciowych.
-   Klasy `Proxy` i `Session` sa ze soba LciLle powiazane. `Session` utrzymuje zbior `Proxy`, przez ktore wysyL'a dane. `Proxy` jest Lwiadome sesji, ktore obsL'uguje.
-   Obie klasy sa zarzadzane przez `ProxyManager`.
-   W projekcie istnieja globalne, dostepne w watku `io_context` kontenery `g_sessions` i `g_proxies` do wzajemnej komunikacji.

---
# z"" proxy_client.cpp
## Opis ogolny

Plik `proxy_client.cpp` zawiera implementacje logiki dla klas `Proxy` i `Session`, ktore razem tworza system klienta proxy. Kod jest w peL'ni asynchroniczny i oparty na Boost.Asio.
## Zmienne globalne

-   `g_sessions`: Globalna mapa (`std::map`) przechowujaca sL'abe wskaLsniki (`std::weak_ptr`) do aktywnych sesji, indeksowane po ich ID.
-   `g_proxies`: Globalny zbior (`std::set`) przechowujacy wskaLsniki do aktywnych obiektow `Proxy`.
-   `UID`: Unikalny identyfikator tej instancji klienta, uLLywany w pakietach ping.
## Klasa `Proxy` (implementacja)
## `void Proxy::check(...)`

GL'owna metoda cyklu LLycia `Proxy`. DziaL'a jak maszyna stanow, wywoL'ywana cyklicznie przez `m_timer`.
-   W stanie `STATE_NOT_CONNECTED`, inicjuje `connect()`.
-   W stanie `STATE_CONNECTING`, sprawdza timeout dla poL'aczenia.
-   W stanie `STATE_CONNECTED`, wysyL'a pakiety ping, jeLli nie oczekuje na odpowiedLs.
-   W stanie `STATE_CONNECTING_WAIT_FOR_PING`, czeka na pierwsza odpowiedLs ping.
## `void Proxy::connect()`

Asynchronicznie rozwiazuje nazwe hosta, a nastepnie L'aczy sie z serwerem proxy. Po pomyLlnym poL'aczeniu, ustawia opcje gniazda (`no_delay`, rozmiary buforow), rozpoczyna odczyt nagL'owkow i wysyL'a pierwszy ping.
## `void Proxy::disconnect()`

Zamyka gniazdo i resetuje stan do `STATE_NOT_CONNECTED`.
## `void Proxy::ping()`

WysyL'a pakiet kontrolny "ping" do serwera proxy. Pakiet zawiera unikalne ID klienta (`UID`) i ostatni zmierzony ping.
## `void Proxy::onPing(uint32_t packetId)`

Handler odpowiedzi na ping. Oblicza nowy ping na podstawie czasu wysL'ania i odebrania pakietu. JeLli to byL' pierwszy ping, zmienia stan na `STATE_CONNECTED`.
## `void Proxy::readHeader()` i `onHeader(...)`

Implementuja dwuetapowy odczyt pakietu: najpierw odczytywany jest 2-bajtowy nagL'owek z rozmiarem, a nastepnie reszta pakietu.
## `void Proxy::onPacket(...)`

Przetwarza przychodzacy pakiet. Na podstawie `sessionId` decyduje, czy jest to pakiet danych dla sesji, czy pakiet kontrolny (ping, zamkniecie sesji). Znajduje odpowiednia sesje w `g_sessions` i przekazuje jej dane.
## `void Proxy::send(...)`

Implementuje kolejke wysyL'ania. Dodaje pakiet do `m_sendQueue` i rozpoczyna operacje `async_write`, jeLli kolejka byL'a pusta.
## Klasa `Session` (implementacja)
## `void Session::start(int maxConnections)`

Dodaje sesje do globalnej mapy `g_sessions`, uruchamia petle `check` i, w trybie serwera, rozpoczyna odczyt danych od klienta gry.
## `void Session::terminate(...)`

Zamyka sesje, informuje wszystkie powiazane `Proxy` o zamknieciu, zamyka gniazdo (jeLli jest) i wywoL'uje `callback` rozL'aczenia.
## `void Session::check(...)`

Metoda cykliczna. Sprawdza timeout braku aktywnoLci i wywoL'uje `selectProxies` w celu optymalizacji routingu.
## `void Session::selectProxies()`

Inteligentny algorytm wyboru proxy.
1.  Iteruje po wszystkich globalnie dostepnych, poL'aczonych `Proxy`.
2.  Znajduje najlepsze `Proxy`, ktore nie jest jeszcze uLLywane przez te sesje.
3.  JeLli liczba aktywnych proxy dla tej sesji jest mniejsza niLL `m_maxConnections`, dodaje najlepsze znalezione `Proxy`.
4.  JeLli liczba jest rowna `m_maxConnections`, a znalezione `Proxy` jest znacznie lepsze niLL najgorsze z aktualnie uLLywanych, zastepuje najgorsze nowym.
5.  Po dodaniu nowego `Proxy`, wysyL'a do niego wszystkie pakiety z kolejki `m_proxySendQueue` (pakiety, ktore mogL'y zostac utracone przez poprzednie `Proxy`).
## `void Session::onProxyPacket(...)`

Handler dla pakietow przychodzacych od proxy.
-   Sprawdza numer sekwencyjny (`packetId`). Odrzuca stare pakiety.
-   Usuwa z `m_proxySendQueue` pakiety wychodzace, ktorych otrzymanie potwierdziL' serwer proxy (`lastRecivedPacketId`).
-   Dodaje przychodzacy pakiet do kolejki `m_sendQueue` (ktora tutaj dziaL'a jako bufor odbiorczy do re-asemblacji).
-   JeLli pakiet jest tym, na ktory czeka (`packetId == m_inputPacketId`), przetwarza go (i wszystkie nastepne w kolejce), wywoL'ujac `m_recvCallback` lub wysyL'ajac do klienta gry.
## `void Session::onPacket(...)`

Handler dla pakietow przychodzacych od klienta gry.
1.  Generuje nowy numer sekwencyjny (`m_outputPacketId`).
2.  Opakowuje pakiet w nagL'owek protokoL'u proxy.
3.  Dodaje opakowany pakiet do `m_proxySendQueue` (bufor do retransmisji).
4.  WysyL'a pakiet do wszystkich aktywnych `Proxy`.

---
# z"" combinedsoundsource.cpp
## Opis ogolny

Plik `combinedsoundsource.cpp` zawiera implementacje klasy `CombinedSoundSource`, ktora jest specjalnym rodzajem LsrodL'a dLswieku.
## Klasa `CombinedSoundSource`
## Opis semantyczny
`CombinedSoundSource` dziaL'a jak kontener na wiele innych obiektow `SoundSource`. Wszystkie operacje wykonane na `CombinedSoundSource` (np. `play()`, `stop()`, `setGain()`) sa delegowane i wykonywane na kaLLdym z podrzednych LsrodeL' dLswieku, ktore przechowuje. Jest to uLLyteczne do tworzenia zL'oLLonych efektow dLswiekowych lub do implementacji obejLc (workarounds), jak w przypadku problemu z dLswiekiem stereo na Linuksie (gdzie dLswiek stereo jest symulowany przez dwa LsrodL'a mono).
## `CombinedSoundSource::CombinedSoundSource()`

Konstruktor. WywoL'uje konstruktor klasy bazowej `SoundSource` z ID 0, poniewaLL sam nie reprezentuje rzeczywistego LsrodL'a w OpenAL.
## `void CombinedSoundSource::addSource(const SoundSourcePtr& source)`

Dodaje nowe podrzedne LsrodL'o dLswieku do wewnetrznego wektora `m_sources`.
## Metody operacyjne (`play`, `stop`, `setLooping`, `setGain`, etc.)

KaLLda z tych metod jest prosta petla, ktora iteruje po wektorze `m_sources` i wywoL'uje odpowiednia metode na kaLLdym z podrzednych obiektow `SoundSource`.

void CombinedSoundSource::play()
{
    for(const SoundSourcePtr& source : m_sources)
        source->play();
}

void CombinedSoundSource::setGain(float gain)
{
    for(const SoundSourcePtr& source : m_sources)
        source->setGain(gain);
}
// ... i tak dalej
```
## Metody sprawdzajace stan (`isBuffering`, `isPlaying`)

Zwracaja `true`, jeLli **ktorekolwiek** z podrzednych LsrodeL' speL'nia dany warunek.

bool CombinedSoundSource::isPlaying()
{
    for(const SoundSourcePtr& source : m_sources) {
        if(source->isPlaying())
            return true;
}
    return false;
}
```
## `void CombinedSoundSource::update()`

Metoda wywoL'ywana w petli `SoundManager::poll()`. WywoL'uje `update()` na wszystkich podrzednych LsrodL'ach, co jest potrzebne np. do obsL'ugi pL'ynnego wyciszania/zgL'aLniania (fading).
## ZaleLLnoLci i powiazania

-   `framework/sound/combinedsoundsource.h`: Plik nagL'owkowy.
-   ULLywana w `SoundManager` jako obejLcie problemu z dLswiekiem stereo na Linuksie.

---
# z"" combinedsoundsource.h
## Opis ogolny

Plik `combinedsoundsource.h` deklaruje klase `CombinedSoundSource`, ktora jest kompozytem wielu LsrodeL' dLswieku, zachowujacym sie jak jedno.
## Klasa `CombinedSoundSource`
## Opis semantyczny
`CombinedSoundSource` implementuje wzorzec projektowy "Kompozyt". Pozwala traktowac grupe obiektow `SoundSource` w ten sam sposob, co pojedynczy obiekt. Wszystkie operacje sa delegowane do wewnetrznej kolekcji LsrodeL'. Dziedziczy po `SoundSource`, aby zachowac zgodnoLc interfejsu.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CombinedSoundSource()` | Konstruktor. |
| `void addSource(...)` | Dodaje podrzedne LsrodL'o dLswieku. |
| `std::vector<...> getSources()` | Zwraca liste podrzednych LsrodeL'. |
| `play()`, `stop()`, `setLooping()`, `setGain()`, `setPosition()`, etc. | Metody delegujace operacje do wszystkich podrzednych LsrodeL'. |
| `isBuffering()`, `isPlaying()` | Sprawdzaja stan, zwracajac `true`, jeLli co najmniej jedno podrzedne LsrodL'o jest w danym stanie. |
## Metody chronione

-   `virtual void update()`: PrzesL'ania metode z `SoundSource` i wywoL'uje `update()` na wszystkich dzieciach.
## Zmienne prywatne

-   `m_sources`: Wektor (`std::vector`) przechowujacy wskaLsniki na podrzedne obiekty `SoundSource`.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundsource.h`: Klasa bazowa i typ przechowywanych obiektow.
-   Jest tworzona i uLLywana przez `SoundManager`.

---
# z"" oggsoundfile.cpp
## Opis ogolny

Plik `oggsoundfile.cpp` zawiera implementacje klasy `OggSoundFile`, ktora jest odpowiedzialna za odczytywanie i dekodowanie plikow dLswiekowych w formacie Ogg Vorbis.
## Klasa `OggSoundFile`
## `OggSoundFile::OggSoundFile(const FileStreamPtr& fileStream)`

Konstruktor. WywoL'uje konstruktor klasy bazowej `SoundFile`.
## `OggSoundFile::~OggSoundFile()`

Destruktor. Zwalnia zasoby zwiazane z biblioteka Vorbis, wywoL'ujac `ov_clear()`.
## `bool OggSoundFile::prepareOgg()`
## Opis semantyczny
Inicjalizuje proces dekodowania pliku Ogg Vorbis.
## DziaL'anie
1.  Tworzy strukture `ov_callbacks` z wskaLsnikami na statyczne metody `cb_...`, ktore beda uLLywane przez biblioteke Vorbis do odczytu danych ze strumienia `FileStream`.
2.  WywoL'uje `ov_open_callbacks`, przekazujac `FileStream` jako LsrodL'o danych.
3.  Pobiera informacje o pliku (liczba kanaL'ow, czestotliwoLc probkowania) za pomoca `ov_info`.
4.  Zapisuje te informacje w polach klasy bazowej (`m_channels`, `m_rate`).
5.  Oblicza caL'kowity rozmiar zdekompresowanych danych za pomoca `ov_pcm_total`.
## `int OggSoundFile::read(void *buffer, int bufferSize)`

Odczytuje i dekoduje fragment pliku dLswiekowego do podanego bufora. WywoL'uje `ov_read`, ktora wykonuje caL'a prace zwiazana z dekodowaniem.
## `void OggSoundFile::reset()`

Przewija strumieL" dLswiekowy na poczatek za pomoca `ov_pcm_seek()`.
## Statyczne metody `cb_...`

Sa to funkcje zwrotne (callbacks) C, ktore opakowuja metody obiektu `FileStream`, tL'umaczac interfejs wymagany przez `libvorbisfile` na interfejs `FileStream`.
-   `cb_read`: opakowuje `file->read()`
-   `cb_seek`: opakowuje `file->seek()`
-   `cb_close`: opakowuje `file->close()`
-   `cb_tell`: opakowuje `file->tell()`
## ZaleLLnoLci i powiazania

-   `framework/sound/oggsoundfile.h`: Plik nagL'owkowy.
-   **libvorbisfile**: Kluczowa zaleLLnoLc do dekodowania plikow Ogg Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`, gdy wykryty zostanie plik w formacie Ogg.

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `sound` sL'uLLy do wczesnych deklaracji klas i definicji typow wskaLsnikow zwiazanych z systemem dLswieku. Jest on kompilowany tylko wtedy, gdy zdefiniowano flage `FW_SOUND`.
## Wczesne deklaracje

-   `SoundManager`
-   `SoundSource`
-   `SoundBuffer`
-   `SoundFile`
-   `SoundChannel`
-   `StreamSoundSource`
-   `CombinedSoundSource`
-   `OggSoundFile`
## Definicje typow

-   `SoundSourcePtr`
-   `SoundFilePtr`
-   `SoundBufferPtr`
-   `SoundChannelPtr`
-   `StreamSoundSourcePtr`
-   `CombinedSoundSourcePtr`
-   `OggSoundFilePtr`
## DoL'aczanie nagL'owkow OpenAL

Plik doL'acza nagL'owki biblioteki OpenAL (`al.h`, `alc.h`), ktora jest podstawa caL'ego systemu dLswieku.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doL'aczany przez wszystkie pliki nagL'owkowe w module `sound`.

---
# z"" oggsoundfile.h
## Opis ogolny

Plik `oggsoundfile.h` deklaruje klase `OggSoundFile`, ktora jest konkretna implementacja `SoundFile` do obsL'ugi plikow w formacie Ogg Vorbis.
## Klasa `OggSoundFile`
## Opis semantyczny
`OggSoundFile` dziedziczy po `SoundFile` i implementuje jej wirtualne metody, uLLywajac biblioteki `libvorbisfile` do dekodowania danych. Enkapsuluje ona strukture `OggVorbis_File` i dostarcza `callbacki` C, ktore pozwalaja bibliotece Vorbis na odczyt danych ze strumienia `FileStream`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OggSoundFile(...)` | Konstruktor. |
| `virtual ~OggSoundFile()` | Destruktor. |
| `bool prepareOgg()` | Inicjalizuje dekoder Vorbis i odczytuje metadane pliku. |
| `int read(...)` | Odczytuje i dekoduje fragment danych. |
| `void reset()` | Przewija strumieL" na poczatek. |
## Metody prywatne (statyczne)

-   `cb_read`, `cb_seek`, `cb_close`, `cb_tell`: Statyczne funkcje zwrotne dla `libvorbisfile`.
## Zmienne prywatne

-   `m_vorbisFile`: Uchwyt do struktur `libvorbisfile`.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundfile.h`: Klasa bazowa.
-   `vorbis/vorbisfile.h`: NagL'owek biblioteki Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`.

---
# z"" soundbuffer.cpp
## Opis ogolny

Plik `soundbuffer.cpp` zawiera implementacje klasy `SoundBuffer`, ktora jest opakowaniem na bufor audio w OpenAL.
## Klasa `SoundBuffer`
## Opis semantyczny
`SoundBuffer` reprezentuje blok danych audio (probek dLswiekowych) zaL'adowany do pamieci, gotowy do odtworzenia przez OpenAL. KaLLdy `SoundBuffer` ma unikalne ID w OpenAL. Jest uLLywany do przechowywania krotkich, czesto odtwarzanych dLswiekow, ktore opL'aca sie trzymac w pamieci.
## `SoundBuffer::SoundBuffer()`

Konstruktor. Generuje nowy bufor OpenAL za pomoca `alGenBuffers()` i zapisuje jego ID.
## `SoundBuffer::~SoundBuffer()`

Destruktor. Zwalnia bufor OpenAL za pomoca `alDeleteBuffers()`.
## `bool SoundBuffer::fillBuffer(const SoundFilePtr& soundFile)`

WypeL'nia bufor danymi z obiektu `SoundFile`.
1.  Pobiera format, rozmiar i czestotliwoLc probkowania z `soundFile`.
2.  Odczytuje caL'a zawartoLc pliku dLswiekowego do tymczasowego bufora w RAM.
3.  WywoL'uje druga wersje `fillBuffer` w celu przesL'ania danych do OpenAL.
## `bool SoundBuffer::fillBuffer(ALenum sampleFormat, const DataBuffer<char>& data, int size, int rate)`

PrzesyL'a surowe dane probek dLswiekowych do bufora OpenAL za pomoca `alBufferData()`.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundbuffer.h`: Plik nagL'owkowy.
-   `framework/sound/soundfile.h`: Do pobierania danych z plikow.
-   Jest tworzona i zarzadzana przez `SoundManager`, ktory przechowuje je w cache.
-   Jest uLLywana przez `SoundSource` jako LsrodL'o danych do odtwarzania.

---
# z"" soundbuffer.h
## Opis ogolny

Plik `soundbuffer.h` deklaruje klase `SoundBuffer`, ktora jest opakowaniem na bufor audio OpenAL.
## Klasa `SoundBuffer`
## Opis semantyczny
`SoundBuffer` enkapsuluje ID bufora OpenAL i dostarcza metody do wypeL'niania go danymi dLswiekowymi. Jest to obiekt przechowujacy dane audio, ktory moLLe byc nastepnie przypisany do jednego lub wielu `SoundSource` w celu odtwarzania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundBuffer()` / `~SoundBuffer()` | Konstruktor i destruktor zarzadzajace zasobem OpenAL. |
| `bool fillBuffer(const SoundFilePtr& soundFile)` | WypeL'nia bufor danymi z pliku dLswiekowego. |
| `bool fillBuffer(...)` | WypeL'nia bufor surowymi danymi z pamieci. |
| `uint getBufferId()` | Zwraca ID bufora w OpenAL. |
## Zmienne prywatne

-   `m_bufferId`: ID (uchwyt) bufora w OpenAL.
## ZaleLLnoLci i powiazania

-   `framework/sound/declarations.h`: Definicje typow.
-   `framework/util/databuffer.h`: Do pracy z buforami danych.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# z"" soundfile.cpp
## Opis ogolny

Plik `soundfile.cpp` zawiera implementacje klasy `SoundFile`, ktora jest abstrakcyjna klasa bazowa do odczytu roLLnych formatow plikow dLswiekowych.
## Klasa `SoundFile`
## `SoundFile::SoundFile(const FileStreamPtr& fileStream)`

Konstruktor. Zapisuje wskaLsnik do strumienia pliku.
## `SoundFilePtr SoundFile::loadSoundFile(const std::string& filename)`
## Opis semantyczny
Statyczna metoda fabryczna, ktora probuje zaL'adowac plik dLswiekowy. Automatycznie wykrywa format pliku i tworzy odpowiednia podklase `SoundFile`.
## DziaL'anie
1.  Otwiera plik za pomoca `g_resources.openFile()`.
2.  Odczytuje pierwsze 4 bajty ("magiczne bajty"), aby zidentyfikowac format.
3.  JeLli plik to Ogg Vorbis (zaczyna sie od "OggS"), tworzy instancje `OggSoundFile` i wywoL'uje jej metode `prepareOgg()`.
4.  W przypadku nieznanego formatu rzuca wyjatek.
## `ALenum SoundFile::getSampleFormat()`

Konwertuje wewnetrzne informacje o liczbie kanaL'ow i bitach na sekunde na format zrozumiaL'y dla OpenAL (np. `AL_FORMAT_STEREO16`).
## ZaleLLnoLci i powiazania

-   `framework/sound/soundfile.h`: Plik nagL'owkowy.
-   `framework/sound/oggsoundfile.h`: Implementacja dla formatu Ogg.
-   `framework/core/resourcemanager.h`: Do otwierania plikow.
-   Jest uLLywana przez `SoundBuffer` i `StreamSoundSource` jako LsrodL'o danych audio.

---
# z"" soundchannel.cpp
## Opis ogolny

Plik `soundchannel.cpp` zawiera implementacje klasy `SoundChannel`, ktora reprezentuje kanaL' dLswiekowy, umoLLliwiajacy odtwarzanie dLswiekow w sposob zorganizowany i kontrolowany.
## Klasa `SoundChannel`
## `SoundSourcePtr SoundChannel::play(...)`

Odtwarza nowy dLswiek na tym kanale. JeLli inny dLswiek jest juLL odtwarzany, zostaje on zatrzymany. WywoL'uje `g_sounds.play`, aby utworzyc i uruchomic nowe LsrodL'o dLswieku.
## `void SoundChannel::stop(float fadetime)`

Zatrzymuje bieLLacy dLswiek i czyLci kolejke. Opcjonalnie moLLe to zrobic z efektem wyciszania (`fadetime`).
## `void SoundChannel::enqueue(...)`

Dodaje plik dLswiekowy do kolejki odtwarzania. Gdy bieLLacy dLswiek sie skoL"czy, `update()` automatycznie odtworzy nastepny z kolejki. Kolejka jest tasowana, aby zapewnic losowa kolejnoLc odtwarzania.
## `void SoundChannel::update()`

Metoda wywoL'ywana cyklicznie przez `SoundManager`.
-   Sprawdza, czy bieLLace LsrodL'o dLswieku zakoL"czyL'o odtwarzanie. JeLli tak, zwalnia je.
-   JeLli nie ma bieLLacego LsrodL'a, a kolejka nie jest pusta, pobiera nastepny utwor z kolejki i go odtwarza.
## `void SoundChannel::setEnabled(bool enable)`

WL'acza lub wyL'acza kanaL'. WyL'aczenie kanaL'u natychmiast zatrzymuje odtwarzany dLswiek i zapobiega odtwarzaniu nowych.
## `void SoundChannel::setGain(float gain)`

Ustawia ogolna gL'oLnoLc dla kanaL'u. GL'oLnoLc ta jest mnoLLona przez gL'oLnoLc poszczegolnych dLswiekow odtwarzanych na tym kanale.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundchannel.h`: Plik nagL'owkowy.
-   `framework/sound/streamsoundsource.h`: ULLywane do efektow wyciszania.
-   `framework/sound/soundmanager.h`: ULLywa `g_sounds` do tworzenia LsrodeL' dLswieku.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# z"" soundchannel.h
## Opis ogolny

Plik `soundchannel.h` deklaruje klase `SoundChannel`, ktora reprezentuje logiczny kanaL' audio.
## Klasa `SoundChannel`
## Opis semantyczny
`SoundChannel` pozwala na grupowanie i zarzadzanie odtwarzaniem dLswiekow. KaLLdy kanaL' moLLe odtwarzac tylko jeden dLswiek naraz, ale posiada kolejke, ktora pozwala na automatyczne odtwarzanie kolejnych utworow. UmoLLliwia globalna kontrole nad grupa dLswiekow, np. ustawienie gL'oLnoLci dla caL'ej muzyki w grze.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundChannel(int id)` | Konstruktor. |
| `SoundSourcePtr play(...)`| Odtwarza dLswiek na tym kanale, przerywajac poprzedni. |
| `void stop(...)` | Zatrzymuje odtwarzanie i czyLci kolejke. |
| `void enqueue(...)` | Dodaje dLswiek do kolejki odtwarzania. |
| `void enable()` / `disable()` | WL'acza/wyL'acza kanaL'. |
| `void setGain(float gain)` | Ustawia gL'oLnoLc kanaL'u. |
| `float getGain()` | Zwraca gL'oLnoLc kanaL'u. |
| `bool isEnabled()` | Sprawdza, czy kanaL' jest wL'aczony. |
| `int getId()` | Zwraca ID kanaL'u. |
## Metody chronione

-   `void update()`: Metoda cykliczna do zarzadzania kolejka.
## Zmienne prywatne

-   `m_queue`: Kolejka (`std::deque`) utworow do odtworzenia.
-   `m_currentSource`: WskaLsnik na aktualnie odtwarzane LsrodL'o dLswieku.
-   `m_enabled`: Flaga wL'aczenia kanaL'u.
-   `m_id`: ID kanaL'u.
-   `m_gain`: GL'oLnoLc kanaL'u.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundsource.h`: ULLywa `SoundSourcePtr`.
-   Jest oznaczona jako `@bindclass`, co udostepnia jej API w Lua.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# z"" soundfile.h
## Opis ogolny

Plik `soundfile.h` deklaruje abstrakcyjna klase bazowa `SoundFile`, ktora definiuje wspolny interfejs do odczytu danych z roLLnych formatow plikow dLswiekowych.
## Klasa `SoundFile`
## Opis semantyczny
`SoundFile` jest abstrakcja nad plikiem dLswiekowym. Ukrywa szczegoL'y konkretnego formatu (np. Ogg, WAV), dostarczajac ujednolicony sposob na odczytywanie zdekompresowanych probek audio.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundFile(...)` | Konstruktor. |
| `static SoundFilePtr loadSoundFile(...)`| Statyczna metoda fabryczna, ktora wykrywa format pliku i tworzy odpowiednia podklase. |
| `virtual int read(...) = 0` | Czysto wirtualna metoda do odczytu zdekompresowanych danych. |
| `virtual void reset() = 0` | Czysto wirtualna metoda do przewiniecia strumienia na poczatek. |
| `bool eof()` | Sprawdza, czy osiagnieto koniec pliku. |
| `ALenum getSampleFormat()` | Konwertuje format (kanaL'y, bity) na format OpenAL. |
| `getChannels()`, `getRate()`, `getBpp()`, `getSize()`, `getName()`| Gettery dla metadanych pliku. |
## Zmienne chronione

-   `m_file`: WskaLsnik na `FileStream`, z ktorego odczytywane sa dane.
-   `m_channels`, `m_rate`, `m_bps`, `m_size`: Metadane dLswieku.
## ZaleLLnoLci i powiazania

-   `framework/sound/declarations.h`: Deklaracje.
-   `framework/core/filestream.h`: ULLywa `FileStream` jako LsrodL'a danych.
-   Jest klasa bazowa dla `OggSoundFile` i potencjalnie innych klas dla roLLnych formatow.

---
# z"" soundmanager.cpp
## Opis ogolny

Plik `soundmanager.cpp` zawiera implementacje klasy `SoundManager`, ktora jest singletonem (`g_sounds`) i centralnym punktem zarzadzania caL'ym podsystemem dLswieku.
## Zmienne globalne
## `g_sounds`

Globalna instancja `SoundManager`.
## Klasa `SoundManager`
## `void SoundManager::init()`

Inicjalizuje system dLswieku.
1.  Otwiera domyLlne urzadzenie audio za pomoca `alcOpenDevice`.
2.  Tworzy kontekst OpenAL za pomoca `alcCreateContext`.
3.  Ustawia ten kontekst jako aktywny za pomoca `alcMakeContextCurrent`.
## `void SoundManager::terminate()`

Zamyka system dLswieku. Zwalnia wszystkie zasoby (LsrodL'a, bufory, kanaL'y), niszczy kontekst i zamyka urzadzenie audio.
## `void SoundManager::poll()`

Metoda wywoL'ywana cyklicznie w gL'ownej petli aplikacji.
-   Aktualizuje wszystkie aktywne LsrodL'a dLswieku (`m_sources`).
-   Aktualizuje wszystkie kanaL'y dLswiekowe (`m_channels`), co pozwala na zarzadzanie kolejkami odtwarzania.
-   Przetwarza asynchronicznie L'adowane pliki dLswiekowe.
## `void SoundManager::setAudioEnabled(bool enable)`

Globalnie wL'acza lub wyL'acza dLswiek. WyL'aczenie powoduje zatrzymanie wszystkich odtwarzanych dLswiekow.
## `void SoundManager::preload(std::string filename)`

Laduje plik dLswiekowy do pamieci i tworzy z niego `SoundBuffer`. Jest to optymalizacja dla krotkich, czesto uLLywanych dLswiekow. Bufor jest przechowywany w cache (`m_buffers`).
## `SoundSourcePtr SoundManager::play(...)`

GL'owna metoda do odtwarzania dLswieku.
1.  Tworzy odpowiednie LsrodL'o dLswieku (`SoundSource` dla skeszowanych plikow lub `StreamSoundSource` dla strumieniowanych).
2.  Ustawia jego parametry (gL'oLnoLc, fadetime).
3.  Rozpoczyna odtwarzanie i dodaje LsrodL'o do listy aktywnych LsrodeL'.
## `SoundChannelPtr SoundManager::getChannel(int channel)`

Zwraca obiekt kanaL'u o danym ID. JeLli kanaL' nie istnieje, jest tworzony.
## `SoundSourcePtr SoundManager::createSoundSource(...)`

Metoda pomocnicza, ktora decyduje, czy utworzyc `SoundSource` (z bufora) czy `StreamSoundSource` (strumieniowanie z pliku). Dla Linuksa implementuje obejLcie problemu z dLswiekiem stereo, tworzac `CombinedSoundSource` z dwoma LsrodL'ami mono.
## `void SoundManager::ensureContext()`

Upewnia sie, LLe kontekst OpenAL jest aktywny w bieLLacym watku.
## ZaleLLnoLci i powiazania

-   **OpenAL**: Podstawowa biblioteka do obsL'ugi dLswieku.
-   WspoL'pracuje ze wszystkimi klasami z moduL'u `sound`.
-   `framework/core/asyncdispatcher.h`: ULLywany do asynchronicznego L'adowania plikow dLswiekowych.

---
# z"" soundmanager.h
## Opis ogolny

Plik `soundmanager.h` deklaruje klase `SoundManager`, ktora jest singletonem (`g_sounds`) zarzadzajacym caL'ym systemem dLswieku w aplikacji.
## Klasa `SoundManager`
## Opis semantyczny
`SoundManager` jest centralnym interfejsem do odtwarzania dLswiekow. Odpowiada za inicjalizacje i zamykanie OpenAL, zarzadzanie LsrodL'ami dLswieku (`SoundSource`), buforami (`SoundBuffer`) i kanaL'ami (`SoundChannel`). Posiada mechanizm cachowania dla maL'ych plikow dLswiekowych i strumieniowania dla wiekszych.
## StaL'e

-   `MAX_CACHE_SIZE`: Maksymalny rozmiar pliku (w bajtach), ktory bedzie cachowany w pamieci.
-   `POLL_DELAY`: Minimalny interwaL' (w ms) miedzy wywoL'aniami `poll()`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Inicjalizuja i zamykaja system dLswieku. |
| `poll()` | Aktualizuje stan wszystkich aktywnych LsrodeL' i kanaL'ow. |
| `setAudioEnabled(...)`, `enableAudio()`, `disableAudio()` | Globalnie wL'aczaja/wyL'aczaja dLswiek. |
| `stopAll()` | Zatrzymuje wszystkie odtwarzane dLswieki. |
| `void preload(...)` | Laduje dLswiek do pamieci podrecznej. |
| `SoundSourcePtr play(...)` | Odtwarza dLswiek z pliku. |
| `SoundChannelPtr getChannel(...)` | Pobiera lub tworzy kanaL' dLswiekowy. |
| `std::string resolveSoundFile(...)` | Rozwiazuje LcieLLke do pliku dLswiekowego. |
| `void ensureContext()` | Upewnia sie, LLe kontekst OpenAL jest aktywny. |
## Zmienne prywatne

-   `m_device`, `m_context`: Uchwyty do urzadzenia i kontekstu OpenAL.
-   `m_streamFiles`: Mapa do zarzadzania asynchronicznym L'adowaniem plikow strumieniowanych.
-   `m_buffers`: Cache dla `SoundBuffer`.
-   `m_sources`: Lista aktywnych LsrodeL' dLswieku.
-   `m_audioEnabled`: Globalna flaga wL'aczenia dLswieku.
-   `m_channels`: Mapa kanaL'ow dLswiekowych.
## Zmienne globalne

-   `g_sounds`: Globalna instancja `SoundManager`.
## ZaleLLnoLci i powiazania

-   `framework/sound/declarations.h`, `soundchannel.h`.
-   Oznaczona jako `@bindsingleton g_sounds`, udostepnia swoje API w Lua.

---
# z"" soundsource.cpp
## Opis ogolny

Plik `soundsource.cpp` zawiera implementacje klasy `SoundSource`, ktora jest opakowaniem na LsrodL'o dLswieku w OpenAL.
## Klasa `SoundSource`
## `SoundSource::SoundSource()`

Konstruktor. Generuje nowe LsrodL'o w OpenAL za pomoca `alGenSources()` i ustawia domyLlne parametry, takie jak dystans referencyjny.
## `SoundSource::~SoundSource()`

Destruktor. Zatrzymuje odtwarzanie i zwalnia zasob LsrodL'a w OpenAL za pomoca `alDeleteSources()`.
## `void SoundSource::play()`

Rozpoczyna odtwarzanie dLswieku za pomoca `alSourcePlay()`.
## `void SoundSource::stop()`

Zatrzymuje odtwarzanie (`alSourceStop()`) i odL'acza bufor od LsrodL'a.
## `bool SoundSource::isBuffering()`

Sprawdza, czy LsrodL'o jest w stanie innym niLL `AL_STOPPED` (czyli `AL_PLAYING` lub `AL_PAUSED`).
## Metody `set...()`

Sa to opakowania na funkcje `alSource...()`, ktore ustawiaja roLLne wL'aLciwoLci LsrodL'a dLswieku:
-   `setBuffer`: Przypisuje `SoundBuffer` do LsrodL'a.
-   `setLooping`: Ustawia zapetlanie.
-   `setRelative`: Ustawia, czy pozycja LsrodL'a jest wzgledna do sL'uchacza.
-   `setGain`: Ustawia gL'oLnoLc.
-   `setPitch`: Ustawia wysokoLc dLswieku.
-   `setPosition`, `setVelocity`: Ustawiaja wL'aLciwoLci 3D dLswieku.
## `void SoundSource::setFading(...)`

Inicjuje proces pL'ynnego zgL'aLniania (`FadingOn`) lub wyciszania (`FadingOff`) dLswieku w okreLlonym czasie. Zapisuje stan i czas rozpoczecia.
## `void SoundSource::update()`

Metoda wywoL'ywana cyklicznie przez `SoundManager`. Implementuje logike "fadingu", aktualizujac gL'oLnoLc LsrodL'a w kaLLdej klatce na podstawie upL'ywajacego czasu.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundsource.h`: Plik nagL'owkowy.
-   `framework/sound/soundbuffer.h`: ULLywa `SoundBuffer` jako LsrodL'a danych.
-   `framework/core/clock.h`: Do obsL'ugi czasu w mechanizmie "fading".

---
# z"" streamsoundsource.cpp
## Opis ogolny

Plik `streamsoundsource.cpp` zawiera implementacje klasy `StreamSoundSource`, ktora jest specjalizacja `SoundSource` do odtwarzania dLswiekow strumieniowo z plikow.
## Klasa `StreamSoundSource`
## Opis semantyczny
`StreamSoundSource` jest przeznaczona do odtwarzania dL'ugich plikow dLswiekowych (np. muzyki), ktore nie sa w caL'oLci L'adowane do pamieci. Zamiast tego, uLLywa mechanizmu kolejkowania maL'ych buforow w OpenAL. Dane sa odczytywane z pliku i dekodowane w locie, a nastepnie umieszczane w buforach, ktore sa dodawane do kolejki odtwarzania LsrodL'a.
## `StreamSoundSource::StreamSoundSource()`

Konstruktor. Tworzy `STREAM_FRAGMENTS` (zwykle 4) maL'ych obiektow `SoundBuffer`, ktore beda uLLywane do kolejkowania.
## `void StreamSoundSource::setSoundFile(...)`

Ustawia plik dLswiekowy, z ktorego beda strumieniowane dane. JeLli LsrodL'o czekaL'o na plik, rozpoczyna odtwarzanie.
## `void StreamSoundSource::play()`

Rozpoczyna odtwarzanie. JeLli plik dLswiekowy nie zostaL' jeszcze zaL'adowany (bo L'adowanie odbywa sie asynchronicznie), ustawia flage `m_waitingFile`. W przeciwnym razie, wywoL'uje `queueBuffers()` i `SoundSource::play()`.
## `void StreamSoundSource::stop()`

Zatrzymuje odtwarzanie i czyLci kolejke buforow za pomoca `unqueueBuffers()`.
## `void StreamSoundSource::update()`

Metoda wywoL'ywana cyklicznie.
1.  Sprawdza, ile buforow zostaL'o juLL przetworzonych (odtworzonych) przez OpenAL.
2.  Odkolejkowuje przetworzone bufory.
3.  WypeL'nia je nowymi danymi z pliku i ponownie dodaje do kolejki.
4.  ObsL'uguje zapetlanie i sprawdza, czy odtwarzanie nie zostaL'o przerwane przez "buffer underrun" (gdy OpenAL skoL"czy odtwarzac, a nie ma nowych buforow w kolejce).
## `bool StreamSoundSource::fillBufferAndQueue(uint buffer)`

Kluczowa metoda.
1.  Odczytuje fragment danych z `m_soundFile`.
2.  ObsL'uguje zapetlanie, resetujac plik po dojLciu do koL"ca.
3.  Opcjonalnie wykonuje "down-mix" z stereo do mono, jeLli `m_downMix` jest ustawione.
4.  WypeL'nia podany bufor OpenAL nowymi danymi.
5.  Dodaje bufor do kolejki odtwarzania LsrodL'a.
## ZaleLLnoLci i powiazania

-   `framework/sound/streamsoundsource.h`: Plik nagL'owkowy.
-   `framework/sound/soundbuffer.h`, `soundfile.h`: ULLywa tych klas do zarzadzania buforami i odczytu plikow.
-   Jest tworzona przez `SoundManager` dla plikow, ktore nie sa cachowane.

---
# z"" streamsoundsource.h
## Opis ogolny

Plik `streamsoundsource.h` deklaruje klase `StreamSoundSource`, ktora jest implementacja `SoundSource` do strumieniowego odtwarzania dLswieku.
## Klasa `StreamSoundSource`
## Opis semantyczny
`StreamSoundSource` pozwala na odtwarzanie dL'ugich plikow dLswiekowych bez potrzeby L'adowania ich w caL'oLci do pamieci. DziaL'a poprzez dzielenie dLswieku na maL'e fragmenty, ktore sa dynamicznie L'adowane do kolejki buforow OpenAL w trakcie odtwarzania.
## StaL'e

-   `STREAM_BUFFER_SIZE`: CaL'kowity rozmiar bufora cyklicznego w pamieci.
-   `STREAM_FRAGMENTS`: Liczba fragmentow (buforow OpenAL), na ktore jest podzielony bufor cykliczny.
-   `STREAM_FRAGMENT_SIZE`: Rozmiar pojedynczego fragmentu.
## Typ wyliczeniowy `DownMix`

OkreLla, czy i jak konwertowac dLswiek stereo na mono (tylko lewy kanaL', tylko prawy, lub brak konwersji).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `StreamSoundSource()` | Konstruktor, tworzy bufory. |
| `virtual ~StreamSoundSource()` | Destruktor. |
| `void play()` | Rozpoczyna strumieniowanie i odtwarzanie. |
| `void stop()` | Zatrzymuje odtwarzanie i czyLci kolejke buforow. |
| `bool isPlaying()` | Zwraca, czy LsrodL'o jest w stanie odtwarzania. |
| `void setSoundFile(...)` | Ustawia plik dLswiekowy do strumieniowania. |
| `void downMix(...)` | Ustawia tryb konwersji na mono. |
| `void update()` | Aktualizuje kolejke buforow (metoda cykliczna). |
## Zmienne prywatne

-   `m_soundFile`: WskaLsnik na plik dLswiekowy.
-   `m_buffers`: Tablica buforow OpenAL uLLywanych w kolejce.
-   `m_downMix`: Tryb konwersji na mono.
-   `m_looping`, `m_playing`, `m_eof`, `m_waitingFile`: Flagi stanu.
## ZaleLLnoLci i powiazania

-   `framework/sound/soundsource.h`: Klasa bazowa.
-   Jest tworzona przez `SoundManager` do odtwarzania duLLych plikow dLswiekowych.

---
# z"" soundsource.h
## Opis ogolny

Plik `soundsource.h` deklaruje klase `SoundSource`, ktora jest abstrakcyjnym opakowaniem na LsrodL'o dLswieku w OpenAL.
## Klasa `SoundSource`
## Opis semantyczny
`SoundSource` reprezentuje punkt w przestrzeni, z ktorego wydobywa sie dLswiek. Enkapsuluje ona ID LsrodL'a OpenAL i dostarcza interfejs do kontrolowania jego wL'aLciwoLci, takich jak gL'oLnoLc, wysokoLc dLswieku, pozycja, zapetlanie i stan odtwarzania. Dziedziczy po `LuaObject`.
## Typ wyliczeniowy `FadeState`

-   `NoFading`: Brak efektu.
-   `FadingOn`: DLswiek jest w trakcie zgL'aLniania.
-   `FadingOff`: DLswiek jest w trakcie wyciszania.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundSource()` | Konstruktor. |
| `virtual ~SoundSource()` | Destruktor. |
| `virtual void play()` | Rozpoczyna odtwarzanie. |
| `virtual void stop()` | Zatrzymuje odtwarzanie. |
| `virtual bool isBuffering()` | Sprawdza stan LsrodL'a w OpenAL. |
| `virtual bool isPlaying()` | DomyLlnie to samo co `isBuffering`. |
| `void setName(...)` | Ustawia nazwe (do identyfikacji). |
| `virtual void setLooping(...)` | WL'acza/wyL'acza zapetlanie. |
| `virtual void setRelative(...)` | Ustawia, czy pozycja jest wzgledna do sL'uchacza. |
| `virtual void setReferenceDistance(...)` | Ustawia dystans referencyjny dla tL'umienia dLswieku 3D. |
| `virtual void setGain(...)` | Ustawia gL'oLnoLc. |
| `virtual void setPitch(...)` | Ustawia wysokoLc dLswieku. |
| `virtual void setPosition(...)` / `setVelocity(...)` | Ustawiaja wL'aLciwoLci 3D. |
| `virtual void setFading(...)` | Inicjuje efekt pL'ynnego zgL'aLniania/wyciszania. |
## Metody chronione

-   `void setBuffer(...)`: Przypisuje `SoundBuffer` do LsrodL'a.
-   `virtual void update()`: Metoda cykliczna do obsL'ugi np. "fadingu".
## Zmienne

-   `m_sourceId`: ID LsrodL'a w OpenAL.
-   `m_name`: Nazwa.
-   `m_buffer`: WskaLsnik na `SoundBuffer` (dla LsrodeL' nie-strumieniowych).
-   `m_fade...`: Zmienne do obsL'ugi "fadingu".
-   `m_gain`: Aktualna gL'oLnoLc.
## ZaleLLnoLci i powiazania

-   `framework/sound/declarations.h`, `soundbuffer.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasa bazowa dla `StreamSoundSource` i `CombinedSoundSource`.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# z"" any.h
## Opis ogolny

Plik `any.h` zawiera implementacje klasy `stdext::any`, ktora jest prosta, wL'asna wersja `std::any` (dostepnego od C++17) lub `boost::any`. Pozwala na przechowywanie wartoLci dowolnego typu w sposob bezpieczny typowo.
## Klasa `any`
## Opis semantyczny
`any` dziaL'a jak polimorficzny kontener. Wewnatrz przechowuje wskaLsnik na obiekt-opakowanie (`placeholder`), ktory jest tworzony na stercie. Obiekt-opakowanie jest szablonem (`holder<T>`), ktory przechowuje rzeczywista wartoLc i informacje o jej typie (`type_info`).
## Struktury wewnetrzne

-   **`placeholder`**: Abstrakcyjna klasa bazowa dla opakowaL". Definiuje wirtualny interfejs do pobierania `type_info` i klonowania.
-   **`holder<T>`**: Szablonowa klasa pochodna, ktora faktycznie przechowuje wartoLc typu `T`.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `any()` | Konstruktor domyLlny (pusty). |
| `any(const any& other)` | Konstruktor kopiujacy (gL'eboka kopia). |
| `template<typename T> any(const T& value)` | Konstruktor szablonowy, tworzy `holder<T>`. |
| `~any()` | Destruktor, zwalnia `placeholder`. |
| `any& swap(any& rhs)` | Zamienia zawartoLc dwoch obiektow `any`. |
| `operator=` | Operatory przypisania. |
| `bool empty()` | Zwraca `true`, jeLli `any` nie przechowuje wartoLci. |
| `template<typename T> const T& cast() const` | Rzutuje i zwraca przechowywana wartoLc. Rzuca `VALIDATE` error, jeLli typ jest nieprawidL'owy. |
| `const std::type_info & type() const` | Zwraca `type_info` przechowywanej wartoLci. |
## Funkcja `any_cast`

Funkcja pomocnicza, ktora wykonuje bezpieczne rzutowanie. Sprawdza, czy typ przechowywany w `any` zgadza sie z typem docelowym.
## ZaleLLnoLci i powiazania

-   `<algorithm>`, `<typeinfo>`: Standardowe nagL'owki C++.
-   Jest uLLywana w `dynamic_storage` do przechowywania wartoLci roLLnych typow.

---
# z"" cast.h
## Opis ogolny

Plik `cast.h` zawiera zestaw szablonowych funkcji i klas do konwersji (rzutowania) miedzy roLLnymi typami danych, gL'ownie z i do `std::string`.
## Funkcje `cast`
## `template<typename T, typename R> bool cast(const T& in, R& out)`

GL'owna, szablonowa funkcja. ULLywa `std::stringstream` do konwersji. Zwraca `true`, jeLli konwersja sie powiodL'a.
## Specjalizacje

Plik zawiera specjalizacje dla typowych i problematycznych konwersji, aby byL'y one bardziej wydajne i niezawodne:
-   `string` do `string`: Proste przypisanie.
-   `string` do `bool`: ObsL'uguje tylko "true" i "false".
-   `string` do `char`: Tylko dla stringow o dL'ugoLci 1.
-   `string` do `long`, `int`, `double`, `float`: ULLywaja `atol` i `atof`, ale z dodatkowa walidacja znakow, aby uniknac nieprawidL'owych konwersji (np. "123a" nie zostanie skonwertowane).
-   `bool` do `string`: Konwertuje na "true" lub "false".
## Klasa `cast_exception`

Wyjatek rzucany przez `safe_cast`, gdy konwersja sie nie powiedzie.
## Funkcje `safe_cast` i `unsafe_cast`

-   **`safe_cast<R, T>(...)`**: Opakowanie na `cast`, ktore rzuca `cast_exception` w przypadku niepowodzenia.
-   **`unsafe_cast<R, T>(...)`**: Opakowanie na `safe_cast`, ktore L'apie wyjatek, loguje bL'ad i zwraca wartoLc domyLlna.
## ZaleLLnoLci i powiazania

-   `stdext/exception.h`, `demangle.h`: Do obsL'ugi bL'edow i nazw typow.
-   Sa to fundamentalne narzedzia uLLywane w caL'ym projekcie, szczegolnie do parsowania wartoLci z plikow OTML i konwersji typow dla Lua.

---
# z"" demangle.cpp
## Opis ogolny

Plik `demangle.cpp` zawiera implementacje funkcji `demangle_name`, ktora konwertuje "znieksztaL'cone" (mangled) nazwy typow C++ na ich czytelna forme.
## Funkcja `demangle_name`
## `const char* demangle_name(const char* name)`
## Opis semantyczny
Nazwy typow C++ (szczegolnie w przypadku szablonow i przestrzeni nazw) sa przez kompilator zamieniane na unikalne, ale nieczytelne identyfikatory (np. `N6stdext11cast_exceptionE`). Funkcja ta odwraca ten proces, uLLywajac narzedzi specyficznych dla danego kompilatora.
## Implementacja
-   **Dla MSVC (`_MSC_VER`)**: ULLywa funkcji `UnDecorateSymbolName` z biblioteki `DbgHelp.dll`.
-   **Dla GCC/Clang**: ULLywa funkcji `abi::__cxa_demangle` z biblioteki `cxxabi`.
## ZaleLLnoLci i powiazania

-   `framework/stdext/demangle.h`: Plik nagL'owkowy.
-   NagL'owki specyficzne dla platformy (`dbghelp.h` lub `cxxabi.h`).
-   Jest uLLywana w systemie rzutowania (`cast_exception`) i w logowaniu, aby dostarczac czytelne nazwy typow w komunikatach o bL'edach.

---
# z"" compiler.h
## Opis ogolny

Plik `compiler.h` zawiera makra i dyrektywy preprocesora specyficzne dla kompilatora. Jego celem jest ujednolicenie obsL'ugi roLLnych kompilatorow (GCC, Clang, MSVC) i zapewnienie kompatybilnoLci.
## ZawartoLc
## `BUILD_COMPILER`

Makro, ktore jest definiowane jako string zawierajacy nazwe i wersje uLLywanego kompilatora. Jest to ustalane na podstawie predefiniowanych makr kompilatora (`__clang__`, `__GNUC__`, `_MSC_VER`).
## Sprawdzanie wersji kompilatora

Plik zawiera dyrektywy `#error`, ktore zatrzymaja kompilacje, jeLli wersja kompilatora jest zbyt stara (wymagany GCC >= 4.6, MSVC >= 2013).
## WyL'aczanie ostrzeLLeL" (MSVC)

Dla kompilatora MSVC, wyL'acza szereg czesto wystepujacych, ale zazwyczaj nieszkodliwych ostrzeLLeL" (`#pragma warning(disable: ...)`), aby utrzymac czysty output kompilacji.
## `__PRETTY_FUNCTION__`

Dla MSVC, definiuje `__PRETTY_FUNCTION__` jako alias dla `__FUNCDNAME__`, aby ujednolicic sposob uzyskiwania "ozdobnej" nazwy funkcji.
## `likely(x)` i `unlikely(x)`

Makra do optymalizacji podpowiedzi dla kompilatora (branch prediction). Dla GCC/Clang uLLywaja `__builtin_expect`. Dla innych kompilatorow sa puste.
## Sprawdzanie wsparcia C++0x

Sprawdza, czy kompilator wspiera wymagany standard C++ (C++11 lub nowszy).
## ZaleLLnoLci i powiazania

-   Jest to jeden z najbardziej fundamentalnych plikow nagL'owkowych, doL'aczany przez `global.h`, i wpL'ywa na kompilacje caL'ego projektu.

---
# z"" demangle.h
## Opis ogolny

Plik `demangle.h` deklaruje funkcje pomocnicze do "demanglowania" (odkodowywania) nazw typow C++, ktore sa znieksztaL'cane przez kompilator w procesie kompilacji.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `const char* demangle_name(const char* name)` | Przyjmuje znieksztaL'cona nazwe i zwraca jej czytelna wersje. |
| `template<typename T> std::string demangle_class()`| Szablonowa funkcja, ktora zwraca czytelna nazwe klasy dla danego typu `T`. |
| `template<typename T> std::string demangle_type()` | Szablonowa funkcja, ktora zwraca czytelna nazwe dowolnego typu `T`. |
## ZaleLLnoLci i powiazania

-   `<typeinfo>`, `<string>`: Standardowe nagL'owki.
-   Jest uLLywana do generowania czytelnych komunikatow o bL'edach, np. w `cast_exception` i `LuaBadValueCastException`.

---
# z"" boolean.h
## Opis ogolny

Plik `boolean.h` deklaruje prosta klase szablonowa `stdext::boolean`, ktora jest opakowaniem na typ `bool` z moLLliwoLcia zdefiniowania wartoLci domyLlnej.
## Klasa `boolean`
## `template<bool def>`

-   **Parametr szablonu `def`**: OkreLla domyLlna wartoLc (`true` lub `false`).
## Opis semantyczny
`boolean` zachowuje sie jak standardowy `bool`, ale jego konstruktor domyLlny inicjalizuje go wartoLcia `def`. Jest to przydatne do inicjalizacji pol w klasach, gdzie domyLlna wartoLc `bool` (ktora jest nieokreLlona) mogL'aby prowadzic do bL'edow.
## PrzykL'ad uLLycia

class MyWidget {
    stdext::boolean<true> m_visible; // DomyLlnie true
    stdext::boolean<false> m_enabled; // DomyLlnie false
};
```
## Operatory

Klasa przeciaLLa operatory `operator bool&`, `operator bool const&` i `operator=`, co pozwala na uLLywanie jej w taki sam sposob, jak standardowego `bool`.
## ZaleLLnoLci i powiazania

-   Jest to prosta klasa narzedziowa, uLLywana w wielu miejscach w projekcie (np. w `UIWidget`) do definiowania flag stanu.

---
# z"" dumper.h
## Opis ogolny

Plik `dumper.h` zawiera proste narzedzie do szybkiego debugowania, ktore pozwala na wypisywanie wartoLci wielu zmiennych na standardowe wyjLcie w jednej linii.
## Zmienne globalne
## `dump`

Globalny obiekt o specjalnej strukturze, ktory przeciaLLa operator `<<`.
## Opis semantyczny
ULLycie `dump` pozwala na tworzenie L'aL"cuchowych wywoL'aL", ktore wypisuja wartoLci oddzielone spacjami, a na koL"cu automatycznie dodaja znak nowej linii.
## PrzykL'ad uLLycia
int x = 10;
std::string y = "hello";
dump << "WartoLci:" << x << y;
```
**WyjLcie:**
WartoLci: 10 hello 
```
## Implementacja
-   Tworzy globalny obiekt, ktorego `operator<<` zwraca tymczasowy obiekt `dumper_dummy`.
-   `dumper_dummy` ma przeciaLLony `operator<<` do wypisywania wartoLci i destruktor, ktory wypisuje znak nowej linii.
## ZaleLLnoLci i powiazania

-   `<iostream>`: Do wypisywania na `std::cout`.
-   Jest to narzedzie wyL'acznie do celow debugowania.

---
# z"" dynamic_storage.h
## Opis ogolny

Plik `dynamic_storage.h` deklaruje klase szablonowa `dynamic_storage`, ktora implementuje dynamiczny kontener asocjacyjny, gdzie kluczem jest typ caL'kowitoliczbowy, a wartoLcia moLLe byc dowolny typ (przechowywany za pomoca `stdext::any`).
## Klasa `dynamic_storage`
## Opis semantyczny
`dynamic_storage` dziaL'a jak mapa, ale jest zaimplementowana w oparciu o `std::vector<stdext::any>`. Klucz (`Key`) jest uLLywany jako indeks w wektorze. Jest to wydajne, jeLli klucze sa maL'ymi, kolejnymi liczbami caL'kowitymi. Pozwala na przechowywanie heterogenicznych danych w jednym kontenerze.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `template<typename T> void set(...)` | Ustawia wartoLc dla danego klucza. W razie potrzeby rozszerza wektor. |
| `bool remove(...)` | Usuwa wartoLc dla danego klucza (zastepujac ja pustym `any`). |
| `template<typename T> T get(...) const` | Pobiera wartoLc dla danego klucza, rzutujac ja na typ `T`. Zwraca wartoLc domyLlna, jeLli klucz nie istnieje. |
| `bool has(...) const` | Sprawdza, czy klucz istnieje i ma przypisana wartoLc. |
| `std::size_t size() const` | Zwraca liczbe niepustych elementow. |
| `void clear()` | CzyLci kontener. |
## Zmienne prywatne

-   `m_data`: Wektor `stdext::any`, ktory przechowuje dane.
## ZaleLLnoLci i powiazania

-   `stdext/types.h`, `stdext/any.h`: Wymagane definicje.
-   `<unordered_map>`: NagL'owek jest doL'aczony, ale nie jest uLLywany.
-   MoLLe byc uLLywana do implementacji niestandardowych systemow atrybutow lub wL'aLciwoLci dla obiektow.

---
# z"" exception.h
## Opis ogolny

Plik `exception.h` deklaruje klase `stdext::exception`, ktora jest bazowa klasa dla wszystkich niestandardowych wyjatkow w projekcie.
## Klasa `exception`
## Opis semantyczny
Dziedziczy po `std::exception` i rozszerza ja o konstruktor przyjmujacy `std::string` oraz o przechowywanie komunikatu bL'edu w `m_what`. Upraszcza to tworzenie i rzucanie wyjatkow z niestandardowymi komunikatami.
## Metody

-   `exception(const std::string& what)`: Konstruktor.
-   `virtual const char* what() const throw()`: Zwraca komunikat bL'edu.
## Funkcja `throw_exception`

Funkcja pomocnicza, ktora tworzy i rzuca `stdext::exception`.

inline void throw_exception(const std::string& what) { throw exception(what); }
```
## ZaleLLnoLci i powiazania

-   Jest klasa bazowa dla `cast_exception` i `LuaException`.
-   Jest uLLywana w caL'ym projekcie do sygnalizowania bL'edow, ktore moga byc przechwycone i obsL'uLLone na wyLLszym poziomie.

---
# z"" fastrand.h
## Opis ogolny

Plik `fastrand.h` zawiera implementacje prostej i szybkiej funkcji do generowania liczb pseudolosowych.
## Funkcja `fastrand`
## `static int fastrand()`
## Opis semantyczny
Implementuje liniowy generator kongruentny (Linear Congruential Generator - LCG). Jest to bardzo prosty i szybki algorytm, ale o niskiej jakoLci losowoLci w porownaniu do nowoczeLniejszych generatorow (jak Mersenne Twister). Jest odpowiedni do zastosowaL", gdzie wydajnoLc jest waLLniejsza niLL jakoLc losowoLci (np. proste efekty wizualne).
## DziaL'anie
-   ULLywa statycznej zmiennej `g_seed` jako stanu.
-   W kaLLdym wywoL'aniu, aktualizuje `g_seed` wedL'ug wzoru: `g_seed = (a * g_seed + c)`.
-   Zwraca 15 najbardziej znaczacych bitow z wyLLszych 16 bitow wyniku.
## ZaleLLnoLci i powiazania

-   Jest to samodzielna funkcja narzedziowa.

---
# z"" math.cpp
## Opis ogolny

Plik `math.cpp` zawiera implementacje funkcji matematycznych i losowych zadeklarowanych w `math.h`.
## Funkcje
## `uint32_t stdext::adler32(...)`

Implementuje algorytm sumy kontrolnej Adler-32, ktory jest szybszy, ale mniej niezawodny niLL CRC32.
## `long stdext::random_range(long min, long max)`

Generuje losowa liczbe caL'kowita z podanego zakresu (wL'acznie). ULLywa generatora Mersenne Twister (`std::mt19937`) zasilanego przez `std::random_device`, co zapewnia wysoka jakoLc losowoLci.
## `float stdext::random_range(float min, float max)`

Generuje losowa liczbe zmiennoprzecinkowa z podanego zakresu.
## `double stdext::round(double r)`

Implementuje zaokraglanie matematyczne (od .5 w gore).
## ZaleLLnoLci i powiazania

-   `framework/stdext/math.h`: Plik nagL'owkowy.
-   `<random>`: Do generowania liczb losowych.

---
# z"" math.h
## Opis ogolny

Plik `math.h` deklaruje zestaw funkcji pomocniczych zwiazanych z matematyka, operacjami bitowymi i losowoLcia.
## Funkcje

-   **`is_power_of_two(v)`**: Sprawdza, czy liczba jest potega dwojki.
-   **`to_power_of_two(v)`**: Zwraca najbliLLsza potege dwojki, ktora jest wieksza lub rowna `v`.
-   **`readULE16`, `readULE32`, `readULE64`**: Odczytuja liczby caL'kowite bez znaku w porzadku Little Endian z bufora.
-   **`writeULE16`, `writeULE32`, `writeULE64`**: Zapisuja liczby do bufora w porzadku Little Endian.
-   **`readSLE...`, `writeSLE...`**: Analogiczne funkcje dla liczb ze znakiem.
-   **`adler32(...)`**: Deklaracja funkcji sumy kontrolnej.
-   **`random_range(...)`**: Deklaracje funkcji do generowania liczb losowych.
-   **`round(...)`**: Deklaracja funkcji zaokraglajacej.
-   **`clamp(...)`**: Szablonowa funkcja ograniczajaca wartoLc do podanego zakresu.
## ZaleLLnoLci i powiazania

-   Sa to podstawowe funkcje narzedziowe, uLLywane w wielu miejscach, szczegolnie w obsL'udze sieci (odczyt/zapis pakietow) i grafice (operacje na potegach dwojki dla tekstur).

---
# z"" net.h
## Opis ogolny

Plik `net.h` deklaruje funkcje pomocnicze zwiazane z operacjami na adresach IP.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `std::string ip_to_string(uint32 ip)` | Konwertuje 32-bitowy adres IP (w porzadku sieciowym) na jego reprezentacje tekstowa (np. "127.0.0.1"). |
| `uint32 string_to_ip(const std::string& string)` | Konwertuje adres IP w formacie tekstowym na jego 32-bitowa reprezentacje w porzadku sieciowym. |
| `std::vector<uint32> listSubnetAddresses(...)` | Generuje liste wszystkich adresow IP w danej podsieci. |
## ZaleLLnoLci i powiazania

-   `stdext/types.h`.
-   Implementacja w `net.cpp` uLLywa Boost.Asio do konwersji.
-   Funkcje te sa uLLywane w logice sieciowej, np. do logowania adresow IP.

---
# z"" packed_any.h
## Opis ogolny

Plik `packed_any.h` deklaruje klase `stdext::packed_any`, ktora jest zoptymalizowana pod katem pamieci wersja `stdext::any`.
## Klasa `packed_any`
## Opis semantyczny
`packed_any` dziaL'a podobnie do `any`, ale wprowadza optymalizacje dla maL'ych, trywialnych typow (takich jak `int`, `bool`, `enum`, wskaLsniki). Zamiast alokowac pamiec na stercie dla `holdera`, wartoLci takich typow sa przechowywane bezpoLrednio w wskaLsniku `content` poprzez rzutowanie. Flaga `scalar` odroLLnia te dwa tryby przechowywania. Zmniejsza to fragmentacje pamieci i narzut na alokacje dla czesto uLLywanych, maL'ych typow.
## Szablon `can_pack_in_any`

Szablon pomocniczy, ktory w czasie kompilacji okreLla, czy dany typ `T` moLLe byc "spakowany" bezpoLrednio we wskaLsniku. Warunkiem jest, aby `sizeof(T)` byL' mniejszy lub rowny `sizeof(void*)` i aby typ byL' trywialnie kopiowalny.
## Metody i pola

Sa analogiczne do `stdext::any`, z dodatkowym polem `scalar` do rozroLLniania trybu.
## Funkcja `packed_any_cast`

Posiada dwie specjalizacje: jedna dla typow "pakowalnych" (ktora rzutuje wskaLsnik z powrotem na wartoLc) i druga dla typow nie-pakowalnych (ktora dziaL'a jak `any_cast`).
## ZaleLLnoLci i powiazania

-   Jest uLLywana w `packed_storage` jako mechanizm przechowywania wartoLci.

---
# z"" shared_object.h
## Opis ogolny

Plik `shared_object.h` zawiera implementacje wL'asnego, intruzywnego inteligentnego wskaLsnika (`shared_object_ptr`) i powiazanej z nim klasy bazowej (`shared_object`).
## Klasa `shared_object`
## Opis semantyczny
Jest to klasa bazowa, po ktorej musza dziedziczyc wszystkie klasy, ktore chca byc zarzadzane przez `shared_object_ptr`. Zawiera ona licznik referencji (`refs`) i metody do jego inkrementacji i dekrementacji. Jest to tzw. "intruzywny" wskaLsnik, poniewaLL sam obiekt przechowuje swoj licznik referencji.
## Metody

-   `add_ref()`: Inkrementuje licznik.
-   `dec_ref()`: Dekrementuje licznik. JeLli osiagnie 0, obiekt usuwa sam siebie (`delete this`).
-   `ref_count()`: Zwraca liczbe referencji.
-   `..._self_cast()`: Metody pomocnicze do bezpiecznego rzutowania `this` na `shared_object_ptr`.
## Klasa `shared_object_ptr`
## Opis semantyczny
Jest to szablonowa klasa inteligentnego wskaLsnika, ktora naLladuje zachowanie `std::shared_ptr`, ale wspoL'pracuje z `shared_object`. Zarzadza czasem LLycia obiektu, na ktory wskazuje, automatycznie wywoL'ujac `add_ref` i `dec_ref`.
## Metody i operatory

Implementuje wszystkie standardowe operacje dla inteligentnych wskaLsnikow: konstruktory, destruktor, operatory przypisania, dereferencji (`*`, `->`), porownania, a takLLe konwersje do `bool`.
## Funkcje pomocnicze

-   `get_pointer`, `static_pointer_cast`, `const_pointer_cast`, `dynamic_pointer_cast`, `make_shared_object`: Funkcje globalne naLladujace te znane z `<memory>`.
## ZaleLLnoLci i powiazania

-   Jest to fundamentalny element frameworka. Prawie wszystkie klasy, ktore sa dynamicznie alokowane i przekazywane miedzy roLLnymi czeLciami systemu (szczegolnie do i z Lua), dziedzicza po `shared_object` i sa zarzadzane przez `shared_object_ptr`.

---
# z"" stdext.h
## Opis ogolny

Plik `stdext.h` jest gL'ownym plikiem nagL'owkowym dla moduL'u `stdext` (standard extensions). Jego jedynym zadaniem jest doL'aczenie wszystkich innych plikow nagL'owkowych z tego moduL'u w jednym miejscu.
## ZawartoLc

DoL'acza wszystkie pliki z `framework/stdext/`, w tym:
-   `compiler.h`
-   `dumper.h`
-   `types.h`
-   `exception.h`
-   `demangle.h`
-   `cast.h`
-   `math.h`
-   `string.h`
-   `time.h`
-   `boolean.h`
-   `shared_object.h`
-   `any.h`
-   `packed_any.h`
-   `dynamic_storage.h`
-   `packed_storage.h`
-   `format.h`
## ZaleLLnoLci i powiazania

-   Jest doL'aczany przez `global.h`, co sprawia, LLe wszystkie narzedzia z `stdext` sa dostepne w caL'ym projekcie.

---
# z"" packed_storage.h
## Opis ogolny

Plik `packed_storage.h` deklaruje klase szablonowa `packed_storage`, ktora jest kontenerem asocjacyjnym zoptymalizowanym pod katem minimalnego zuLLycia pamieci.
## Klasa `packed_storage`
## Opis semantyczny
`packed_storage` dziaL'a jak mapa, ale zamiast zL'oLLonych struktur drzewiastych lub tablic hashujacych, przechowuje swoje elementy w prostej, dynamicznie alokowanej tablicy par `(klucz, wartoLc)`. WartoLci sa przechowywane w `packed_any`, co dodatkowo minimalizuje zuLLycie pamieci. Jest to rozwiazanie kompromisowe: zuLLywa bardzo maL'o pamieci, ale operacje wyszukiwania, dodawania i usuwania maja zL'oLLonoLc liniowa O(n). Jest odpowiednia dla maL'ej liczby elementow.
## Metody publiczne

Sa analogiczne do `dynamic_storage`: `set`, `remove`, `get`, `has`, `clear`, `size`.
## Zmienne prywatne

-   `m_values`: WskaLsnik na tablice `value_pair`.
-   `m_size`: Aktualna liczba elementow.
## ZaleLLnoLci i powiazania

-   `stdext/types.h`, `stdext/packed_any.h`.
-   MoLLe byc uLLywana tam, gdzie liczy sie kaLLdy bajt pamieci, a liczba przechowywanych elementow jest niewielka.

---
# z"" thread.h
## Opis ogolny

Plik `thread.h` jest prostym plikiem nagL'owkowym, ktory doL'acza standardowe nagL'owki C++ zwiazane z wielowatkowoLcia.
## ZawartoLc

# include <thread>
# include <condition_variable>
# include <mutex>
```
## ZaleLLnoLci i powiazania

-   SL'uLLy jako centralny punkt doL'aczania nagL'owkow wielowatkowoLci, co uL'atwia zarzadzanie zaleLLnoLciami.
-   Jest uLLywany przez klasy takie jak `AsyncDispatcher`, `Logger`, `ProxyManager`.

---
# z"" time.h
## Opis ogolny

Plik `time.h` deklaruje zestaw funkcji i klas do obsL'ugi czasu, stanowiac opakowanie na `std::chrono`.
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `ticks_t time()` | Zwraca czas w sekundach od epoki (Unix timestamp). |
| `ticks_t millis()` | Zwraca czas w milisekundach od uruchomienia aplikacji. |
| `ticks_t micros()` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `void millisleep(size_t ms)` | Usypia bieLLacy watek na `ms` milisekund. |
| `void microsleep(size_t us)` | Usypia bieLLacy watek na `us` mikrosekund. |
## Struktura `timer`

Prosta klasa-stoper, podobna do `Timer` z moduL'u `core`, ale dziaL'ajaca na "rzeczywistym" czasie z `stdext::micros()`, a nie na buforowanym czasie z `g_clock`.
## ZaleLLnoLci i powiazania

-   `stdext/types.h`.
-   Implementacja w `time.cpp` uLLywa `std::chrono` i `std::this_thread`.
-   Sa to niskopoziomowe funkcje czasowe, na ktorych bazuje `Clock`.

---
# z"" traits.h
## Opis ogolny

Plik `traits.h` zawiera szablony metaprogramowania (type traits), ktore sa uLLywane do manipulacji i analizy typow w czasie kompilacji.
## Namespace `stdext`
## Szablony

-   **`replace_extent`**: Usuwa wymiar tablicy z typu i zastepuje go wskaLsnikiem. Np. `int[10]` staje sie `const int*`.
-   **`remove_const_ref`**: Metafunkcja, ktora z danego typu `T` usuwa kwalifikatory `const` oraz referencje, zwracajac "czysty" typ. Np. `const std::string&` staje sie `std::string`.
## ZaleLLnoLci i powiazania

-   `<type_traits>`: Standardowy nagL'owek C++.
-   Sa to zaawansowane narzedzia metaprogramowania, uLLywane gL'ownie w `luabinder.h` do analizy sygnatur funkcji i w `format.h` do obsL'ugi argumentow.

---
# z"" string.h
## Opis ogolny

Plik `string.h` deklaruje zestaw funkcji pomocniczych do manipulacji i konwersji ciagow znakow (`std::string`).
## Namespace `stdext`
## Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `to_string<T>(...)` / `from_string<T>(...)` | Skroty do `unsafe_cast` dla konwersji z/do stringa. |
| `resolve_path(...)` | Laczy LcieLLke do pliku ze LcieLLka LsrodL'owa. |
| `date_time_string()` | Zwraca sformatowana date i czas. |
| `dec_to_hex(...)` / `hex_to_dec(...)` | Konwersje miedzy systemem dziesietnym a szesnastkowym. |
| `tolower(...)`, `toupper(...)`, `trim(...)`, `ucwords(...)` | Standardowe operacje na stringach. |
| `ends_with(...)`, `starts_with(...)`, `replace_all(...)` | Operacje wyszukiwania i zamiany. |
| `is_valid_utf8(...)` | Sprawdza, czy string jest poprawnym ciagiem UTF-8. |
| `utf8_to_latin1(...)`, `latin1_to_utf8(...)` | Konwersje kodowania znakow. |
| `utf8_to_utf16(...)`, `utf16_to_utf8(...)` | (Windows) Konwersje do/z UTF-16 (`std::wstring`). |
| `split(...)` | Dzieli string na wektor stringow na podstawie separatorow. |
## ZaleLLnoLci i powiazania

-   `stdext/types.h`, `cast.h`.
-   Implementacja w `string.cpp` uLLywa biblioteki Boost.StringAlgo do niektorych operacji.
-   Sa to podstawowe funkcje narzedziowe uLLywane w caL'ym projekcie.

---
# z"" time.cpp
## Opis ogolny

Plik `time.cpp` zawiera implementacje funkcji czasowych zadeklarowanych w `time.h`.
## Namespace `stdext`
## `startup_time`

Statyczna zmienna, ktora przechowuje czas uruchomienia aplikacji. Jest uLLywana jako punkt odniesienia dla `millis()` i `micros()`.

const static auto startup_time = std::chrono::high_resolution_clock::now();
```
## Implementacje funkcji

-   **`time()`**: ULLywa `std::time(NULL)`.
-   **`millis()`**, **`micros()`**: Obliczaja roLLnice miedzy bieLLacym czasem a `startup_time` za pomoca `std::chrono` i konwertuja wynik na odpowiednia jednostke.
-   **`millisleep()`**, **`microsleep()`**: ULLywaja `std::this_thread::sleep_for`.
## ZaleLLnoLci i powiazania

-   `stdext/time.h`: Plik nagL'owkowy.
-   `<chrono>`, `<ctime>`, `<thread>`: Standardowe biblioteki C++.

---
# z"" uri.h
## Opis ogolny

Plik `uri.h` deklaruje strukture `ParsedURI` oraz funkcje do parsowania adresow URL.
## Struktura `ParsedURI`

Przechowuje rozbity na czeLci adres URL.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `protocol` | `std::string` | ProtokoL' (np. "http", "wss"). |
| `domain` | `std::string` | Domena (np. "example.com"). |
| `port` | `std::string` | Port. |
| `query` | `std::string` | LscieLLka i zapytanie (np. "/path?a=1"). |
## Funkcja `parseURI`
## `ParsedURI parseURI(const std::string& url)`

Parsuje podany URL i zwraca strukture `ParsedURI` z jego komponentami.
## ZaleLLnoLci i powiazania

-   Jest uLLywana przez `HttpSession` i `WebsocketSession` do analizy podanego adresu URL.

---
# z"" net.cpp
## Opis ogolny

Plik `net.cpp` zawiera implementacje funkcji pomocniczych do operacji na adresach IP, zadeklarowanych w `net.h`.
## Namespace `stdext`
## `std::string ip_to_string(uint32 ip)`

Konwertuje 32-bitowy adres IP z porzadku sieciowego na porzadek hosta, a nastepnie na `std::string` za pomoca `boost::asio::ip::address_v4`.
## `uint32 string_to_ip(const std::string& string)`

Konwertuje `std::string` na obiekt `address_v4`, a nastepnie na 32-bitowa liczbe w porzadku sieciowym.
## `std::vector<uint32> listSubnetAddresses(uint32 address, uint8 mask)`

Generuje liste wszystkich adresow IP w podanej podsieci. Oblicza maske bitowa i iteruje po wszystkich moLLliwych adresach w zakresie, dodajac je do listy.
## ZaleLLnoLci i powiazania

-   `framework/stdext/net.h`: Plik nagL'owkowy.
-   `boost/asio`: ULLywana do konwersji adresow IP.
-   Sa to funkcje narzedziowe uLLywane w logice sieciowej.

---
# z"" uri.cpp
## Opis ogolny

Plik `uri.cpp` zawiera implementacje funkcji `parseURI` do parsowania adresow URL.
## Funkcja `parseURI`
## `ParsedURI parseURI(const std::string& url)`

ULLywa wyraLLenia regularnego (`std::regex`) do rozbicia adresu URL na jego komponenty: protokoL', domene, port i LcieLLke/zapytanie. ObsL'uguje protokoL'y "http", "https", "ws", "wss" i poprawnie ustawia domyLlne porty (80 dla http/ws, 443 dla https/wss).
## ZaleLLnoLci i powiazania

-   `framework/stdext/uri.h`: Plik nagL'owkowy.
-   `<regex>`: Do parsowania.
-   `boost/algorithm/string.hpp`: Do konwersji na maL'e litery.
-   Jest uLLywana przez `HttpSession` i `WebsocketSession`.

---
# z"" types.h
## Opis ogolny

Plik `types.h` definiuje zestaw aliasow dla typow caL'kowitoliczbowych o staL'ym rozmiarze oraz inne podstawowe typy uLLywane w caL'ym frameworku.
## Definicje typow

-   **Skroty**: `uchar`, `ushort`, `uint`, `ulong`.
-   **Liczby o staL'ym rozmiarze**: `uint64`, `uint32`, `uint16`, `uint8` oraz ich wersje ze znakiem (`int...`).
-   **`ticks_t`**: Alias dla `int64`, uLLywany do przechowywania czasu w milisekundach lub mikrosekundach.
-   **`refcount_t`**: Typ dla licznika referencji.
-   **`size_t`, `ptrdiff_t`**: Importuje typy ze `std`.
## ZaleLLnoLci i powiazania

-   `<cstdint>`, `<cstddef>`: Standardowe nagL'owki.
-   Jest to fundamentalny plik, doL'aczany przez `stdext.h` i `global.h`, zapewniajacy spojne i przenoLne typy danych w caL'ym projekcie.

---
# z"" format.h
## Opis ogolny

Plik `format.h` zawiera implementacje funkcji `stdext::format`, ktora jest bezpieczna typowo alternatywa dla `sprintf`, podobna do `boost::format` lub `fmt::format`.
## Funkcje
## `stdext::print(...)`

Funkcja debugujaca, ktora wypisuje na konsole dowolna liczbe argumentow, oddzielajac je tabulatorami, podobnie jak `print` w Lua.
## `stdext::snprintf(...)`

Opakowanie na `snprintf` / `_snprintf`, ktore potrafi obsL'ugiwac typy niestandardowe, takie jak `std::string`, poprzez `sprintf_cast`.
## `stdext::format(...)`

GL'owna funkcja.
-   **DziaL'anie**:
    1.  WywoL'uje `snprintf` z `NULL` jako buforem, aby obliczyc wymagana dL'ugoLc wynikowego stringa.
    2.  Alokuje `std::string` o odpowiednim rozmiarze.
    3.  WywoL'uje `snprintf` ponownie, tym razem zapisujac wynik do bufora stringa.
-   **Zalety**: Jest w peL'ni bezpieczna (brak przepeL'nienia bufora) i obsL'uguje roLLne typy danych.
## ZaleLLnoLci i powiazania

-   `stdext/traits.h`: Do analizy typow.
-   `<tuple>`, `<sstream>`: Do metaprogramowania i formatowania.
-   Jest to kluczowe narzedzie uLLywane w caL'ym projekcie do formatowania stringow, szczegolnie w logach i komunikatach o bL'edach.

---
# z"" string.cpp
## Opis ogolny

Plik `string.cpp` zawiera implementacje funkcji pomocniczych do manipulacji stringami, zadeklarowanych w `string.h`.
## Funkcje

-   **`resolve_path(...)`**: Implementuje logike L'aczenia LcieLLek, obsL'ugujac LcieLLki absolutne i wzgledne.
-   **`date_time_string()`, `timestamp_to_date(...)`**: ULLywaja `std::localtime` i `std::strftime` do formatowania daty i czasu.
-   **`dec_to_hex(...)`, `hex_to_dec(...)`**: ULLywaja `std::stringstream` do konwersji.
-   **Konwersje kodowania**: `is_valid_utf8` implementuje walidacje bajt po bajcie. `utf8_to_latin1` i `latin1_to_utf8` implementuja uproszczona konwersje. Wersje dla Windows (`..._to_utf16`) uLLywaja funkcji WinAPI `MultiByteToWideChar` i `WideCharToMultiByte`.
-   **Inne operacje**: `tolower`, `toupper`, `trim`, `ends_with`, `starts_with`, `replace_all`, `split` sa opakowaniami na odpowiednie funkcje z biblioteki Boost.StringAlgo.
## ZaleLLnoLci i powiazania

-   `framework/stdext/string.h`, `format.h`.
-   `boost/algorithm/string.hpp`: Kluczowa zaleLLnoLc dla wielu operacji.
-   `physfs.h`: Potencjalnie, choc nie jest bezpoLrednio uLLywany.
-   NagL'owki WinAPI (dla konwersji kodowania).

---
# z"" declarations.h
## Opis ogolny

Plik `declarations.h` w module `ui` jest plikiem nagL'owkowym do wczesnych deklaracji (forward declarations) i definicji typow dla klas interfejsu uLLytkownika.
## Wczesne deklaracje

-   `UIManager`
-   `UIWidget`
-   `UITextEdit`
-   `UILayout` i wszystkie jego podklasy (`UIBoxLayout`, `UIGridLayout`, etc.)
-   `UIAnchor`, `UIAnchorGroup`, `UIAnchorLayout`
## Definicje typow

-   `UIWidgetPtr`, `UITextEditPtr`, `UILayoutPtr`, ...: Aliasy dla `shared_object_ptr` do klas UI.
-   `UIWidgetList`: Alias dla `std::deque<UIWidgetPtr>`.
-   `UIAnchorList`: Alias dla `std::vector<UIAnchorPtr>`.
## ZaleLLnoLci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest doL'aczany przez wszystkie pliki nagL'owkowe w module `ui`.

---
# z"" ui.h
## Opis ogolny

Plik `ui.h` jest gL'ownym, zbiorczym plikiem nagL'owkowym dla moduL'u UI. Jego zadaniem jest doL'aczenie wszystkich najwaLLniejszych nagL'owkow zwiazanych z interfejsem uLLytkownika w jednym miejscu.
## ZawartoLc

DoL'acza wszystkie podstawowe komponenty UI:
-   `uimanager.h`
-   `uiwidget.h`
-   `uitextedit.h`
-   `uilayout.h` i jego pochodne (`uihorizontallayout.h`, `uiverticallayout.h`, `uigridlayout.h`, `uianchorlayout.h`).
## ZaleLLnoLci i powiazania

-   UL'atwia doL'aczanie caL'ego podsystemu UI w innych czeLciach projektu, ktore go potrzebuja (np. w plikach moduL'ow gry).

---
# z"" uiboxlayout.cpp
## Opis ogolny

Plik `uiboxlayout.cpp` zawiera implementacje klasy `UIBoxLayout`, ktora jest abstrakcyjna klasa bazowa dla layoutow ukL'adajacych widgety w jednej linii (poziomo lub pionowo).
## Klasa `UIBoxLayout`
## `UIBoxLayout::UIBoxLayout(UIWidgetPtr parentWidget)`

Konstruktor. WywoL'uje konstruktor `UILayout` i inicjalizuje `m_spacing` na 0.
## `void UIBoxLayout::applyStyle(const OTMLNodePtr& styleNode)`

Parsuje atrybuty specyficzne dla `UIBoxLayout` z wezL'a OTML.
-   `spacing`: Odstep miedzy widgetami.
-   `fit-children`: Flaga okreLlajaca, czy layout powinien dostosowac rozmiar rodzica do sumarycznego rozmiaru dzieci.
## `addWidget` i `removeWidget`

Te metody po prostu wywoL'uja `update()`, poniewaLL kaLLda zmiana w liczbie dzieci wymaga ponownego przeliczenia layoutu.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiboxlayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   Jest klasa bazowa dla `UIHorizontalLayout` i `UIVerticalLayout`.

---
# z"" uiboxlayout.h
## Opis ogolny

Plik `uiboxlayout.h` deklaruje klase `UIBoxLayout`, ktora jest abstrakcyjna klasa bazowa dla layoutow liniowych.
## Klasa `UIBoxLayout`
## Opis semantyczny
`UIBoxLayout` dziedziczy po `UILayout` i dodaje wspolna funkcjonalnoLc dla layoutow horyzontalnych i wertykalnych, a mianowicie:
-   `spacing`: Odstep miedzy kolejnymi elementami.
-   `fit-children`: MoLLliwoLc automatycznego dostosowania rozmiaru widgetu-rodzica, aby zmieLciL' wszystkie swoje dzieci.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setSpacing(int spacing)` | Ustawia odstep miedzy widgetami. |
| `setFitChildren(bool fitParent)` | WL'acza/wyL'acza dopasowywanie rozmiaru rodzica. |
## Zmienne chronione

-   `m_fitChildren`: Flaga `fit-children`.
-   `m_spacing`: WartoLc odstepu.
## ZaleLLnoLci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Jest klasa bazowa dla `UIHorizontalLayout` i `UIVerticalLayout`.
-   Oznaczona jako `@bindclass`, jej metody sa dostepne w Lua.

---
# z"" uigridlayout.cpp
## Opis ogolny

Plik `uigridlayout.cpp` zawiera implementacje klasy `UIGridLayout`, ktora ukL'ada widgety w siatce o staL'ym rozmiarze komorek.
## Klasa `UIGridLayout`
## `UIGridLayout::UIGridLayout(...)`

Konstruktor, ustawia domyLlne wartoLci (rozmiar komorki 16x16, 1 kolumna).
## `void UIGridLayout::applyStyle(...)`

Parsuje atrybuty specyficzne dla siatki z wezL'a OTML, takie jak `cell-size`, `cell-spacing`, `num-columns`, `flow`.
## `bool UIGridLayout::internalUpdate()`
## Opis semantyczny
GL'owna metoda przeliczajaca pozycje widgetow w siatce.
## DziaL'anie
1.  Pobiera liste dzieci od rodzica.
2.  **Tryb `flow`**: JeLli wL'aczony, dynamicznie oblicza liczbe kolumn (`numColumns`), tak aby zmieLciL'y sie w szerokoLci rodzica. Na podstawie tego oblicza liczbe wierszy.
3.  **Tryb `auto-spacing`**: JeLli wL'aczony, dynamicznie oblicza odstep miedzy komorkami (`cellSpacing`), aby rownomiernie rozL'oLLyc je na caL'ej szerokoLci rodzica.
4.  W petli przechodzi przez wszystkie widoczne widgety:
    -   Oblicza wiersz i kolumne dla bieLLacego widgetu.
    -   Na tej podstawie oblicza jego pozycje.
    -   Ustawia docelowy prostokat (`Rect`) widgetu na rozmiar komorki w obliczonej pozycji.
5.  **Tryb `fit-children`**: JeLli wL'aczony, oblicza wymagana wysokoLc rodzica, aby zmieLcic wszystkie wiersze, i planuje jej ustawienie w `EventDispatcher` (aby uniknac problemow z rekurencyjnymi aktualizacjami).
## ZaleLLnoLci i powiazania

-   `framework/ui/uigridlayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokoLci rodzica.

---
# z"" uigridlayout.h
## Opis ogolny

Plik `uigridlayout.h` deklaruje klase `UIGridLayout`, ktora implementuje layout siatkowy.
## Klasa `UIGridLayout`
## Opis semantyczny
`UIGridLayout` ukL'ada swoje widgety w regularnej siatce. MoLLe miec staL'a liczbe kolumn lub dynamicznie dostosowywac ja do dostepnej przestrzeni (`flow`). Posiada rownieLL opcje automatycznego dostosowywania odstepow i rozmiaru rodzica.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setCellSize(...)` | Ustawia rozmiar pojedynczej komorki siatki. |
| `setCellSpacing(...)` | Ustawia odstep miedzy komorkami. |
| `setNumColumns(...)` | Ustawia staL'a liczbe kolumn. |
| `setNumLines(...)` | Ustawia maksymalna liczbe wierszy. |
| `setFlow(bool enable)` | WL'acza/wyL'acza tryb "pL'ynny", w ktorym liczba kolumn jest dynamiczna. |
| `setAutoSpacing(bool enable)`| WL'acza/wyL'acza automatyczne obliczanie odstepow. |
| `setFitChildren(bool enable)`| WL'acza/wyL'acza dopasowywanie wysokoLci rodzica. |
## Zmienne prywatne

-   `m_cellSize`: Rozmiar komorki.
-   `m_cellSpacing`: Odstep miedzy komorkami.
-   `m_numColumns`, `m_numLines`: Liczba kolumn i wierszy.
-   `m_autoSpacing`, `m_fitChildren`, `m_flow`: Flagi trybow.
## ZaleLLnoLci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# z"" uihorizontallayout.cpp
## Opis ogolny

Plik `uihorizontallayout.cpp` zawiera implementacje klasy `UIHorizontalLayout`, ktora ukL'ada widgety w jednym rzedzie, od lewej do prawej lub od prawej do lewej.
## Klasa `UIHorizontalLayout`
## `void UIHorizontalLayout::applyStyle(...)`

Parsuje atrybut `align-right` z wezL'a OTML.
## `bool UIHorizontalLayout::internalUpdate()`
## Opis semantyczny
GL'owna metoda przeliczajaca pozycje widgetow.
## DziaL'anie
1.  Pobiera liste dzieci. JeLli `m_alignRight` jest `true`, odwraca kolejnoLc listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycje `x` na podstawie pozycji i szerokoLci poprzedniego widgetu oraz odstepow (`spacing`, `margin`).
    -   Oblicza pozycje `y` w zaleLLnoLci od wyrownania pionowego widgetu (`AlignTop`, `AlignBottom`, `AlignCenter`) wewnatrz wysokoLci rodzica.
    -   JeLli widget nie ma staL'ego rozmiaru, jego wysokoLc jest rozciagana do wysokoLci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumaryczna, preferowana szerokoLc (`preferredWidth`).
4.  JeLli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie szerokoLci rodzica na `preferredWidth`.
## ZaleLLnoLci i powiazania

-   `framework/ui/uihorizontallayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania szerokoLci rodzica.

---
# z"" uihorizontallayout.h
## Opis ogolny

Plik `uihorizontallayout.h` deklaruje klase `UIHorizontalLayout`, ktora implementuje layout horyzontalny.
## Klasa `UIHorizontalLayout`
## Opis semantyczny
`UIHorizontalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukL'adania widgetow w pojedynczym rzedzie. MoLLe ukL'adac elementy od lewej do prawej (domyLlnie) lub od prawej do lewej (`align-right`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignRight(bool alignRight)` | WL'acza/wyL'acza ukL'adanie od prawej do lewej. |
## Zmienne chronione

-   `m_alignRight`: Flaga trybu wyrownania do prawej.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# z"" uilayout.cpp
## Opis ogolny

Plik `uilayout.cpp` zawiera implementacje klasy `UILayout`, ktora jest abstrakcyjna klasa bazowa dla wszystkich menedLLerow layoutu.
## Klasa `UILayout`
## `void UILayout::update()`
## Opis semantyczny
GL'owna metoda publiczna inicjujaca aktualizacje layoutu.
## DziaL'anie
1.  Sprawdza, czy aktualizacje nie sa wyL'aczone (`m_updateDisabled`).
2.  Sprawdza, czy aktualizacja nie jest juLL w toku (`m_updating`), aby zapobiec rekurencji. JeLli tak, planuje aktualizacje na poLsniej (`updateLater()`).
3.  Ustawia flage `m_updating` na `true`.
4.  WywoL'uje wirtualna metode `internalUpdate()`, gdzie klasy pochodne implementuja swoja logike.
5.  WywoL'uje `callback` `onLayoutUpdate` na widLLecie-rodzicu.
6.  Resetuje flage `m_updating`.
## `void UILayout::updateLater()`

Planuje wykonanie `update()` w nastepnej iteracji petli `EventDispatcher`. Jest to mechanizm zapobiegajacy wielokrotnym, zbednym przeliczeniom layoutu w tej samej klatce.
## ZaleLLnoLci i powiazania

-   `framework/ui/uilayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: KaLLdy layout jest powiazany z widgetem-rodzicem.
-   `framework/core/eventdispatcher.h`: Do planowania opoLsnionych aktualizacji.

---
# z"" uilayout.h
## Opis ogolny

Plik `uilayout.h` deklaruje abstrakcyjna klase bazowa `UILayout`, ktora definiuje wspolny interfejs dla wszystkich klas zarzadzajacych pozycja i rozmiarem widgetow-dzieci.
## Klasa `UILayout`
## Opis semantyczny
`UILayout` jest powiazany z jednym widgetem-rodzicem (`m_parentWidget`). Jego zadaniem jest automatyczne zarzadzanie geometria dzieci tego widgetu. KaLLda podklasa (`UIAnchorLayout`, `UIBoxLayout` itd.) implementuje inny algorytm ukL'adania elementow. Posiada mechanizmy do wL'aczania/wyL'aczania aktualizacji oraz do unikania rekurencyjnych i zbednych przeliczeL".
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `UILayout(UIWidgetPtr parentWidget)`| Konstruktor. |
| `void update()` | Natychmiast LLada przeliczenia layoutu. |
| `void updateLater()` | Planuje przeliczenie layoutu w najbliLLszej przyszL'oLci. |
| `virtual void applyStyle(...)` | Stosuje wL'aLciwoLci layoutu z wezL'a OTML. |
| `virtual void addWidget(...)` | Powiadamia layout o dodaniu nowego widgetu. |
| `virtual void removeWidget(...)` | Powiadamia layout o usunieciu widgetu. |
| `void disableUpdates()` / `enableUpdates()`| Tymczasowo wstrzymuje/wznawia aktualizacje layoutu. |
| `void setParent(...)` / `getParentWidget()` | Zarzadza powiazaniem z widgetem-rodzicem. |
| `bool isUpdating()` | Zwraca `true`, jeLli layout jest w trakcie aktualizacji. |
| `isUI...Layout()` | Metody RTTI (Run-Time Type Information) do identyfikacji typu layoutu. |
## Zmienne chronione

-   `m_updateDisabled`: Licznik blokad aktualizacji.
-   `m_updating`, `m_updateScheduled`: Flagi zapobiegajace rekurencji i wielokrotnym aktualizacjom.
-   `m_parentWidget`: WskaLsnik do widgetu, ktorego dziecmi zarzadza layout.
## ZaleLLnoLci i powiazania

-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/otml/otml.h`: Do parsowania stylow.
-   Jest klasa bazowa dla wszystkich konkretnych implementacji layoutow.
-   KaLLdy `UIWidget` moLLe miec jeden `UILayout`.

---
# z"" uimanager.h
## Opis ogolny

Plik `uimanager.h` deklaruje klase `UIManager`, ktora jest singletonem (`g_ui`) i centralnym punktem zarzadzania caL'ym interfejsem uLLytkownika.
## Klasa `UIManager`
## Opis semantyczny
`UIManager` zarzadza hierarchia widgetow, poczynajac od korzenia (`m_rootWidget`). Odpowiada za propagacje zdarzeL" wejLciowych (mysz, klawiatura), renderowanie, zarzadzanie stylami OTML oraz Lledzenie globalnych stanow UI, takich jak aktualnie wciLniety, najechany czy przeciagany widget.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia menedLLera. |
| `void render(Fw::DrawPane)`| Rozpoczyna proces renderowania UI dla danej warstwy. |
| `void resize(const Size&)` | Aktualizuje rozmiar `m_rootWidget`. |
| `void inputEvent(...)` | GL'owny punkt wejLcia dla wszystkich zdarzeL" wejLciowych. |
| `void clearStyles()` | CzyLci zaL'adowane style. |
| `bool importStyle(...)` | Laduje style z pliku `.otui`. |
| `OTMLNodePtr getStyle(...)` | Zwraca definicje stylu o podanej nazwie. |
| `UIWidgetPtr loadUI(...)` | Laduje i tworzy hierarchie widgetow z pliku `.otui`. |
| `UIWidgetPtr createWidget(...)` | Tworzy widget na podstawie nazwy stylu. |
| `setMouseReceiver(...)` / `setKeyboardReceiver(...)` | Ustawia widget, ktory "przechwytuje" zdarzenia myszy/klawiatury. |
| `get...Widget()` | Zwracaja wskaLsniki na widgety w okreLlonych stanach (przeciagany, najechany, wciLniety). |
## Metody chronione (wywoL'ywane przez `UIWidget`)

-   `onWidgetAppear(...)`, `onWidgetDisappear(...)`, `onWidgetDestroy(...)`: Callbacki informujace menedLLera o zmianach w drzewie widgetow, co pozwala na aktualizacje globalnych stanow (np. `m_hoveredWidget`).
## Zmienne prywatne

-   `m_rootWidget`: KorzeL" drzewa widgetow, wypeL'nia caL'e okno.
-   `m_mouseReceiver`, `m_keyboardReceiver`: Widgety przechwytujace zdarzenia.
-   `m_draggingWidget`, `m_hoveredWidget`, `m_pressedWidget`: Lsledza globalne stany myszy.
-   `m_styles`: Mapa przechowujaca wszystkie zaL'adowane style.
-   `m_destroyedWidgets`: Lista do Lledzenia niszczonych widgetow w celach debugowania wyciekow pamieci.
## Zmienne globalne

-   `g_ui`: Globalna instancja `UIManager`.
## ZaleLLnoLci i powiazania

-   `framework/ui/declarations.h`, `uiwidget.h`.
-   `framework/core/inputevent.h`.
-   LsciLle wspoL'pracuje z `GraphicalApplication` (ktora przekazuje jej zdarzenia) i `PlatformWindow`.
-   Zarzadza cyklem LLycia i interakcjami wszystkich `UIWidget`.

---
# z"" uitextedit.cpp
## Opis ogolny

Plik `uitextedit.cpp` zawiera implementacje klasy `UITextEdit`, ktora jest specjalizowanym widgetem do wprowadzania i edycji tekstu.
## Klasa `UITextEdit`
## `UITextEdit::UITextEdit()`

Konstruktor. Inicjalizuje wszystkie pola zwiazane z edycja tekstu do wartoLci domyLlnych (np. kursor na pozycji 0, widoczny, tekst edytowalny).
## `void UITextEdit::drawSelf(...)`

PrzesL'onieta metoda rysujaca.
1.  Rysuje tL'o, ramke, obraz i ikone (dziedziczone z `UIWidget`).
2.  JeLli tekst jest pusty, rysuje `placeholder`.
3.  Rysuje tekst, uLLywajac `CoordsBuffer` (`m_glyphsTextCoordsBuffer`) do zbuforowania geometrii.
4.  Rysuje zaznaczenie, najpierw rysujac tL'o zaznaczenia, a potem tekst w innym kolorze na wierzchu.
5.  Rysuje migajacy kursor w odpowiedniej pozycji.
## `void UITextEdit::update(bool focusCursor)`

Kluczowa metoda, ktora przelicza caL'a geometrie tekstu.
1.  Pobiera tekst do wyLwietlenia (zwykL'y lub ukryty `*`).
2.  Zawija tekst, jeLli `m_textWrap` jest wL'aczone.
3.  Oblicza pozycje wszystkich glifow za pomoca `m_font->calculateGlyphsPositions`.
4.  JeLli `m_autoScroll` i `focusCursor` sa `true`, automatycznie przewija widok, tak aby kursor byL' zawsze widoczny.
5.  Przelicza, ktore glify sa widoczne w obszarze widgetu, i generuje dla nich wspoL'rzedne w `m_glyphsCoords`.
## Metody edycji tekstu

-   `setCursorPos`, `setSelection`, `clearSelection`, `selectAll`: Zarzadzaja pozycja kursora i zaznaczeniem.
-   `appendText`, `appendCharacter`, `removeCharacter`: Modyfikuja tekst.
-   `del`, `paste`, `copy`, `cut`: Implementuja standardowe operacje edycyjne.
## `int UITextEdit::getTextPos(Point pos)`

Konwertuje pozycje myszy (w pikselach) na indeks znaku w tekLcie.
## ObsL'uga zdarzeL" (`on...`)

PrzesL'ania metody obsL'ugi zdarzeL" z `UIWidget`, aby zaimplementowac logike edycji tekstu:
-   `onKeyPress`: ObsL'uguje nawigacje (strzaL'ki, Home, End), usuwanie (Delete, Backspace), zaznaczanie (Shift + strzaL'ki), kopiowanie/wklejanie (Ctrl+C/V).
-   `onKeyText`: Wstawia wprowadzony tekst.
-   `onMousePress`, `onMouseMove`, `onDoubleClick`: ObsL'uguja ustawianie kursora i zaznaczanie tekstu mysza.
## ZaleLLnoLci i powiazania

-   `framework/ui/uitextedit.h`: Plik nagL'owkowy.
-   `framework/graphics/bitmapfont.h`: Intensywnie uLLywa `Bitmapfont` do obliczeL".
-   `framework/platform/platformwindow.h`: Do interakcji ze schowkiem.
-   Na Androidzie, zamiast wL'asnego renderowania, wywoL'uje natywne pole edycji tekstu.

---
# z"" uimanager.cpp
## Opis ogolny

Plik `uimanager.cpp` zawiera implementacje klasy `UIManager`, ktora jest centralnym menedLLerem interfejsu uLLytkownika.
## Klasa `UIManager`
## `void UIManager::init()`

Inicjalizuje menedLLera, tworzac gL'owny, niewidoczny widget (`m_rootWidget`), ktory jest korzeniem caL'ego drzewa UI i zajmuje caL'a powierzchnie okna.
## `void UIManager::render(Fw::DrawPane drawPane)`

Rozpoczyna proces renderowania, wywoL'ujac metode `draw()` na `m_rootWidget` dla okreLlonej warstwy rysowania.
## `void UIManager::resize(const Size& size)`

Aktualizuje rozmiar `m_rootWidget`, co powoduje rekurencyjne przeliczenie layoutu dla wszystkich widgetow potomnych.
## `void UIManager::inputEvent(const InputEvent& event)`
## Opis semantyczny
GL'owny punkt wejLcia dla wszystkich zdarzeL" wejLciowych. TL'umaczy surowe zdarzenia na akcje w UI.
## DziaL'anie
-   Dla zdarzeL" klawiatury, przekazuje je do `m_keyboardReceiver`.
-   Dla wciLniecia przycisku myszy:
    1.  Identyfikuje widget pod kursorem.
    2.  Aktualizuje `m_pressedWidget`.
    3.  Propaguje zdarzenie `onMousePress` w doL' drzewa.
-   Dla zwolnienia przycisku myszy:
    1.  JeLli trwaL'o przeciaganie, koL"czy je i obsL'uguje "upuszczenie".
    2.  Propaguje zdarzenie `onMouseRelease`.
    3.  JeLli zwolnienie nastapiL'o nad pierwotnie wciLnietym widgetem, generuje zdarzenie `onClick`.
-   Dla ruchu myszy:
    1.  Aktualizuje `m_hoveredWidget`.
    2.  JeLli jakiL widget jest wciLniety i przeciagalny, rozpoczyna przeciaganie.
    3.  Propaguje zdarzenie `onMouseMove`.
-   Dla koL'ka myszy, propaguje zdarzenie.
## `void UIManager::update...Widget(...)`

Metody te zarzadzaja globalnym stanem UI:
-   `updatePressedWidget`: Zmienia, ktory widget jest aktualnie wciLniety.
-   `updateDraggingWidget`: Rozpoczyna lub koL"czy przeciaganie widgetu.
-   `updateHoveredWidget`: Aktualizuje, nad ktorym widgetem znajduje sie kursor.
## `bool UIManager::importStyle(...)`

Laduje i parsuje plik `.otui` ze stylami, dodajac je do `m_styles`.
## `UIWidgetPtr UIManager::loadUI(...)` i `createWidgetFromOTML(...)`

Implementuja logike tworzenia widgetow na podstawie plikow i wezL'ow OTML. `createWidgetFromOTML` jest kluczowa metoda, ktora:
1.  Znajduje styl bazowy.
2.  Laczy (merge) go ze stylem zdefiniowanym w pliku UI.
3.  Na podstawie atrybutu `__class`, wywoL'uje w Lua funkcje fabryczna (`create`) dla danego typu widgetu.
4.  Stosuje styl i rekurencyjnie tworzy dzieci.
## `void UIManager::onWidgetDestroy(...)`

Callback wywoL'ywany przez `UIWidget`. CzyLci wszystkie globalne referencje do niszczonego widgetu (np. `m_hoveredWidget`, `m_pressedWidget`). W trybie debugowania, planuje sprawdzenie, czy nie pozostaL'y LLadne wiszace referencje do widgetu po jego zniszczeniu.
## ZaleLLnoLci i powiazania

-   Jest to centralna klasa UI, ktora L'aczy `PlatformWindow` (LsrodL'o zdarzeL") z `UIWidget` (odbiorcy zdarzeL").
-   Zarzadza caL'ym drzewem widgetow.
-   WspoL'pracuje z `OTML` do parsowania stylow i layoutow.

---
# z"" uitextedit.h
## Opis ogolny

Plik `uitextedit.h` deklaruje klase `UITextEdit`, ktora jest widgetem sL'uLLacym do wprowadzania i edycji tekstu przez uLLytkownika.
## Klasa `UITextEdit`
## Opis semantyczny
`UITextEdit` dziedziczy po `UIWidget` i rozszerza jego funkcjonalnoLc o logike obsL'ugi kursora, zaznaczania tekstu, wprowadzania z klawiatury, kopiowania/wklejania i zawijania wierszy. Jest to jeden z najbardziej zL'oLLonych widgetow w podstawowym zestawie.
## Metody publiczne
## Zarzadzanie tekstem i kursorem
-   `setCursorPos(...)`: Ustawia pozycje kursora.
-   `setSelection(...)`: Ustawia zaznaczenie.
-   `setTextHidden(...)`: WL'acza tryb "hasL'a" (wyLwietla `*`).
-   `setMaxLength(...)`: Ustawia maksymalna dL'ugoLc tekstu.
-   `appendText(...)`: Dodaje tekst w pozycji kursora.
-   `del()`, `paste()`, `copy()`, `cut()`: Standardowe operacje edycyjne.
-   `selectAll()`, `clearSelection()`: Zarzadzanie zaznaczeniem.
## Konfiguracja
-   `setEditable(...)`: WL'acza/wyL'acza moLLliwoLc edycji.
-   `setMultiline(...)`: WL'acza/wyL'acza tryb wieloliniowy.
-   `setValidCharacters(...)`: Ogranicza dozwolone znaki.
-   `setPlaceholder(...)`: Ustawia tekst wyLwietlany, gdy pole jest puste.
## Gettery
-   `getCursorPos()`, `getSelection()`, `getTextPos(...)`, ...: Zwracaja informacje o stanie edytora.
## Zmienne prywatne

-   `m_cursorPos`: Pozycja kursora.
-   `m_selectionStart`, `m_selectionEnd`: Granice zaznaczenia.
-   `m_textHidden`, `m_multiline`, `m_editable`, ...: Flagi konfiguracyjne.
-   `m_glyphsCoords`, `m_glyphsTexCoords`: Wektory przechowujace geometrie renderowanego tekstu.
-   `m_glyphsTextCoordsBuffer`, `m_glyphsSelectCoordsBuffer`: Bufory `CoordsBuffer` dla tekstu i zaznaczenia.
-   `m_placeholder`, `m_placeholderColor`, ...: WL'aLciwoLci placeholdera.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiwidget.h`: Klasa bazowa.
-   Jest oznaczona jako `@bindclass`, co udostepnia jej bogate API w Lua.
-   Jest jednym z podstawowych, predefiniowanych typow widgetow tworzonych przez `UIManager`.

---
# z"" uitranslator.cpp
## Opis ogolny

Plik `uitranslator.cpp` zawiera implementacje funkcji, ktore tL'umacza tekstowe reprezentacje roLLnych enumow uLLywanych w UI na ich faktyczne wartoLci liczbowe.
## Namespace `Fw`
## `Fw::AlignmentFlag Fw::translateAlignment(std::string aligment)`

Konwertuje string (np. "top-left", "center") na odpowiednia flage z `Fw::AlignmentFlag`. ULLywa `boost::to_lower` i `boost::erase_all` do normalizacji wejLcia.
## `Fw::AnchorEdge Fw::translateAnchorEdge(std::string anchorEdge)`

Konwertuje string (np. "left", "horizontal-center") na odpowiednia wartoLc z `Fw::AnchorEdge`.
## `Fw::WidgetState Fw::translateState(std::string state)`

Konwertuje string (np. "hover", "pressed") na odpowiednia flage z `Fw::WidgetState`.
## `Fw::AutoFocusPolicy Fw::translateAutoFocusPolicy(std::string policy)`

Konwertuje string (np. "first", "last") na odpowiednia wartoLc z `Fw::AutoFocusPolicy`.
## ZaleLLnoLci i powiazania

-   `framework/ui/uitranslator.h`: Plik nagL'owkowy.
-   `boost/algorithm/string.hpp`: Do normalizacji stringow.
-   Funkcje te sa uLLywane przez `UIWidget` i jego podklasy podczas parsowania stylow z OTML, aby przekonwertowac wartoLci tekstowe na enumy.

---
# z"" uitranslator.h
## Opis ogolny

Plik `uitranslator.h` deklaruje zestaw funkcji pomocniczych do konwersji stringow na wartoLci wyliczeniowe (enum) uLLywane w systemie UI.
## Namespace `Fw`
## Deklaracje funkcji

| Funkcja | Opis |
| :--- | :--- |
| `AlignmentFlag translateAlignment(...)`| Konwertuje string na `Fw::AlignmentFlag`. |
| `AnchorEdge translateAnchorEdge(...)` | Konwertuje string na `Fw::AnchorEdge`. |
| `WidgetState translateState(...)` | Konwertuje string na `Fw::WidgetState`. |
| `AutoFocusPolicy translateAutoFocusPolicy(...)`| Konwertuje string na `Fw::AutoFocusPolicy`. |
## ZaleLLnoLci i powiazania

-   `framework/const.h`: Definicje enumow.
-   `<string>`: Do operacji na stringach.
-   Te funkcje sa kluczowe dla parsowania plikow OTML, gdzie wL'aLciwoLci takie jak wyrownanie sa zdefiniowane za pomoca sL'ow kluczowych.

---
# z"" uiverticallayout.cpp
## Opis ogolny

Plik `uiverticallayout.cpp` zawiera implementacje klasy `UIVerticalLayout`, ktora ukL'ada widgety w jednej kolumnie, od gory do doL'u lub od doL'u do gory.
## Klasa `UIVerticalLayout`
## `void UIVerticalLayout::applyStyle(...)`

Parsuje atrybut `align-bottom` z wezL'a OTML.
## `bool UIVerticalLayout::internalUpdate()`
## Opis semantyczny
GL'owna metoda przeliczajaca pozycje widgetow. DziaL'a analogicznie do `UIHorizontalLayout::internalUpdate`, ale operuje na osi Y.
## DziaL'anie
1.  Pobiera liste dzieci. JeLli `m_alignBottom` jest `true`, odwraca kolejnoLc listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycje `y` na podstawie pozycji i wysokoLci poprzedniego widgetu oraz odstepow.
    -   Oblicza pozycje `x` w zaleLLnoLci od wyrownania poziomego widgetu (`AlignLeft`, `AlignRight`, `AlignCenter`) wewnatrz szerokoLci rodzica.
    -   JeLli widget nie ma staL'ego rozmiaru, jego szerokoLc jest rozciagana do szerokoLci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumaryczna, preferowana wysokoLc (`preferredHeight`).
4.  JeLli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie wysokoLci rodzica na `preferredHeight`.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiverticallayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokoLci rodzica.

---
# z"" uiverticallayout.h
## Opis ogolny

Plik `uiverticallayout.h` deklaruje klase `UIVerticalLayout`, ktora implementuje layout wertykalny.
## Klasa `UIVerticalLayout`
## Opis semantyczny
`UIVerticalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukL'adania widgetow w pojedynczej kolumnie. MoLLe ukL'adac elementy od gory do doL'u (domyLlnie) lub od doL'u do gory (`align-bottom`).
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignBottom(bool alignBottom)` | WL'acza/wyL'acza ukL'adanie od doL'u do gory. |
| `isAlignBottom()` | Zwraca stan flagi `align-bottom`. |
## Zmienne chronione

-   `m_alignBottom`: Flaga trybu wyrownania do doL'u.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# z"" uiwidget.cpp
## Opis ogolny

Plik `uiwidget.cpp` jest gL'ownym plikiem implementacyjnym dla klasy `UIWidget`. Zawiera on logike dla podstawowych operacji na widgetach, takich jak zarzadzanie dziecmi, obsL'uga layoutow, zdarzeL", stanow i stylow.
## Klasa `UIWidget`
## `UIWidget::UIWidget()`

Konstruktor. Inicjalizuje wszystkie pola do wartoLci domyLlnych, w tym podstawowy styl, wL'aLciwoLci tekstu i obrazu. Co waLLne, zapisuje LcieLLke do skryptu Lua, w ktorym widget zostaL' utworzony (`m_source`), co jest niezwykle przydatne do debugowania.
## `void UIWidget::draw(...)`

GL'owna metoda renderujaca. Jest rekurencyjna.
1.  WywoL'uje `drawSelf()` do narysowania samego widgetu.
2.  JeLli wL'aczone jest przycinanie (`m_clipping`), ustawia odpowiedni `DrawQueueConditionClip`.
3.  WywoL'uje `drawChildren()` do narysowania wszystkich widocznych dzieci.
4.  Stosuje globalne efekty dla widgetu i jego dzieci, takie jak przezroczystoLc (`setOpacity`) i rotacja (`setRotation`), dodajac odpowiednie warunki do `DrawQueue`.
## `void UIWidget::addChild(...)`, `insertChild(...)`, `removeChild(...)`

Metody do zarzadzania hierarchia widgetow. Poza modyfikacja `m_children`, dbaja o:
-   Ustawienie/zresetowanie wskaLsnika `m_parent` w dziecku.
-   Dodanie/usuniecie widgetu z layoutu rodzica.
-   Aktualizacje stanu fokusu, jeLli usuwane jest dziecko z fokusem.
-   Aktualizacje stanow indeksowych (`FirstState`, `LastState`) u rodzeL"stwa.
-   Powiadomienie `UIManager` o pojawieniu sie/zniknieciu widgetu.
## `void UIWidget::focusChild(...)`, `focusNextChild(...)`, `focusPreviousChild(...)`

Implementuja logike zarzadzania fokusem wewnatrz widgetu. `focusChild` zmienia `m_focusedChild` i wywoL'uje callbacki `onFocusChange`. `focusNext/PreviousChild` implementuja nawigacje (np. klawiszem Tab).
## `void UIWidget::applyStyle(const OTMLNodePtr& styleNode)`

Aplikuje wL'aLciwoLci z wezL'a stylu do widgetu. WywoL'uje `onStyleApply` oraz `onStyleApply` w Lua.
## `void UIWidget::updateState(Fw::WidgetState state)`

Kluczowa metoda, ktora aktualizuje pojedyncza flage stanu (np. `HoverState`). Oblicza, czy widget powinien miec dany stan (np. dla `HoverState` sprawdza, czy `g_ui.getHoveredWidget() == this`), a nastepnie wywoL'uje `setState`.
## `void UIWidget::updateStates()`

WywoL'uje `updateState` dla wszystkich moLLliwych stanow, synchronizujac peL'ny stan widgetu.
## `void UIWidget::updateStyle()`

Gdy stan widgetu sie zmienia, ta metoda jest wywoL'ywana. Przebudowuje ona tymczasowy wezeL' stylu (`m_stateStyle`), L'aczac style z warunkow (`$!hover`, `$checked`, itp.), a nastepnie wywoL'uje `applyStyle` z tym nowym, poL'aczonym stylem.
## Metody `on...` i `propagateOn...`

Implementuja domyLlna obsL'uge i propagacje zdarzeL" w drzewie widgetow. Metody `propagate...` decyduja, do ktorych dzieci przekazac zdarzenie, a nastepnie wywoL'uja metode `on...` na samym widgecie.
## ZaleLLnoLci i powiazania

-   Jest to centralna klasa moduL'u UI, ktora zaleLLy od prawie wszystkich innych jego czeLci (`UIManager`, `UILayout`, `UITranslator`) oraz wielu moduL'ow frameworka (`Graphics`, `LuaInterface`, `EventDispatcher`, `OTML`).

---
# z"" uiwidget.h
## Opis ogolny

Plik `uiwidget.h` deklaruje klase `UIWidget`, ktora jest fundamentalna klasa bazowa dla wszystkich elementow interfejsu uLLytkownika.
## Struktura `EdgeGroup`

Szablonowa struktura pomocnicza do przechowywania wartoLci dla czterech krawedzi (gora, prawo, doL', lewo), uLLywana dla `margin`, `padding`, `border-width` i `border-color`.
## Klasa `UIWidget`
## Opis semantyczny
`UIWidget` jest obiektowym odpowiednikiem elementu DOM. Reprezentuje prostokatny obszar na ekranie, ktory moLLe byc rysowany, reagowac na zdarzenia i zawierac inne widgety. Implementuje model drzewa (rodzic-dzieci), system zdarzeL" (propagacja i obsL'uga), system stanow (aktywny, najechany, etc.), zarzadzanie layoutem oraz integracje z OTML i Lua.
## PodziaL' interfejsu (w pliku `.h`)

Interfejs klasy jest podzielony na sekcje tematyczne:
-   **Widget Core**: Podstawowe metody do zarzadzania hierarchia, layoutem, stylami i stanami.
-   **State Management**: Metody do zarzadzania stanami (`setState`, `hasState`).
-   **Event Processing**: Wirtualne metody `on...` do obsL'ugi zdarzeL".
-   **Function Shortcuts**: Wygodne metody opakowujace (`hide`, `show`, `enable`).
-   **Base Style**: Pola i metody zwiazane z podstawowymi wL'aLciwoLciami wizualnymi (tL'o, ramka, ikona, przezroczystoLc).
-   **Image**: Pola i metody zwiazane z wyLwietlaniem obrazu (`m_imageTexture`, `setImageSource`).
-   **Text**: Pola i metody zwiazane z wyLwietlaniem tekstu (`m_text`, `m_font`, `setText`).
## Kluczowe wL'aLciwoLci

-   **Hierarchia**: `m_parent`, `m_children`.
-   **Geometria**: `m_rect`.
-   **Styl**: `m_style` (wezeL' OTML), `m_states`.
-   **Layout**: `m_layout`.
-   **Zdarzenia**: Zestaw wirtualnych metod `on...` (np. `onMousePress`, `onKeyPress`).
-   **Wyglad**: `m_backgroundColor`, `m_borderColor`, `m_imageTexture`, `m_text`, `m_font`, etc.
## ZaleLLnoLci i powiazania

-   `framework/ui/declarations.h`, `uilayout.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasa bazowa dla wszystkich innych widgetow, np. `UITextEdit`.
-   Jest zarzadzana przez `UIManager`.

---
# z"" uiwidgetimage.cpp
## Opis ogolny

Plik `uiwidgetimage.cpp` zawiera implementacje czeLci klasy `UIWidget` odpowiedzialnej za obsL'uge i renderowanie obrazu tL'a.

> **NOTE:** To nie jest osobna klasa, lecz czeLc implementacji `UIWidget`, wydzielona do osobnego pliku dla lepszej organizacji kodu.
## Klasa `UIWidget` (czeLc implementacji)
## `void UIWidget::initImage()`

Inicjalizuje pola zwiazane z obrazem do wartoLci domyLlnych.
## `void UIWidget::parseImageStyle(const OTMLNodePtr& styleNode)`

Parsuje z wezL'a OTML wszystkie atrybuty zwiazane z obrazem (`image-source`, `image-clip`, `image-color`, `image-border`, `image-shader` itp.) i wywoL'uje odpowiednie settery.
## `void UIWidget::drawImage(const Rect& screenCoords)`
## Opis semantyczny
GL'owna metoda rysujaca obraz.
## DziaL'anie
1.  Sprawdza, czy tekstura obrazu istnieje.
2.  JeLli geometria (`screenCoords`) lub wL'aLciwoLci obrazu ulegL'y zmianie (`m_imageMustRecache`), przelicza i buforuje wspoL'rzedne wierzchoL'kow i tekstur w `m_imageCoordsBuffer`.
    -   ObsL'uguje roLLne tryby: proste skalowanie, zachowanie proporcji (`m_imageFixedRatio`), powtarzanie (`m_imageRepeated`) oraz zL'oLLone rysowanie z ramka (`m_imageBordered`), ktore dzieli obraz na 9 czeLci i odpowiednio je skaluje/powtarza.
3.  Dodaje zadanie rysowania do `g_drawQueue`. JeLli zdefiniowano `m_shader`, uLLywa specjalnego `DrawQueueItemImageWithShader`.
## `void UIWidget::setQRCode(...)`

Generuje obraz kodu QR, tworzy z niego teksture i ustawia ja jako `m_imageTexture`.
## `void UIWidget::setImageSource(const std::string& source)`

Laduje teksture z pliku za pomoca `g_textures` i ustawia ja jako `m_imageTexture`. JeLli wL'aczone jest `m_imageAutoResize`, dostosowuje rozmiar widgetu do rozmiaru obrazu.
## `void UIWidget::setImageSourceBase64(...)`

Dekoduje obraz zakodowany w Base64, tworzy z niego teksture i ustawia ja.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiwidget.h`: Plik nagL'owkowy klasy, ktora implementuje.
-   `framework/graphics/painter.h`, `image.h`, `texture.h`, `texturemanager.h`: Komponenty graficzne.
-   `framework/util/crypt.h`: Do dekodowania Base64.

---
# z"" uianchorlayout.h
## Opis ogolny

Plik `uianchorlayout.h` deklaruje klasy `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, ktore razem implementuja system layoutu oparty na "kotwicach" (anchors).
## Klasa `UIAnchor`
## Opis semantyczny
Reprezentuje pojedyncza reguL'e "kotwiczenia", ktora wiaLLe jedna krawedLs widgetu z krawedzia innego widgetu (lub rodzica).

-   **Pola**: `m_anchoredEdge` (krawedLs tego widgetu), `m_hookedWidgetId` (ID widgetu docelowego), `m_hookedEdge` (krawedLs widgetu docelowego).
## Klasa `UIAnchorGroup`
## Opis semantyczny
Kontener na wszystkie kotwice (`UIAnchor`) przypisane do jednego widgetu. Posiada rownieLL flage `m_updated` uLLywana przez algorytm layoutu.
## Klasa `UIAnchorLayout`
## Opis semantyczny
`UIAnchorLayout` to menedLLer layoutu, ktory pozycjonuje i skaluje swoje widgety-dzieci na podstawie zdefiniowanych dla nich reguL' kotwiczenia. Pozwala to na tworzenie elastycznych i responsywnych interfejsow, ktore dostosowuja sie do zmian rozmiaru okna.
## Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `addAnchor(...)` | Dodaje nowa reguL'e kotwiczenia dla widgetu. |
| `removeAnchors(...)` | Usuwa wszystkie kotwice z widgetu. |
| `hasAnchors(...)` | Sprawdza, czy widget ma jakiekolwiek kotwice. |
| `centerIn(...)` | Skrot do dodania kotwic centrujacych widget. |
| `fill(...)` | Skrot do dodania kotwic rozciagajacych widget na caL'y obszar innego widgetu. |
## Zmienne prywatne

-   `m_anchorsGroups`: Mapa przechowujaca `UIAnchorGroup` dla kaLLdego zarzadzanego widgetu.
## ZaleLLnoLci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.
-   Jest jednym z najczeLciej uLLywanych layoutow w projekcie.

---
# z"" uiwidgettext.cpp
## Opis ogolny

Plik `uiwidgettext.cpp` zawiera implementacje czeLci klasy `UIWidget` odpowiedzialnej za obsL'uge i renderowanie tekstu.

> **NOTE:** To nie jest osobna klasa, lecz czeLc implementacji `UIWidget`, wydzielona do osobnego pliku.
## Klasa `UIWidget` (czeLc implementacji)
## `void UIWidget::initText()`

Inicjalizuje pola zwiazane z tekstem do wartoLci domyLlnych (np. domyLlny font, wyrownanie do Lrodka).
## `void UIWidget::updateText()`

Metoda wywoL'ywana po kaLLdej zmianie tekstu lub jego wL'aLciwoLci.
1.  JeLli zawijanie jest wL'aczone, wywoL'uje `m_font->wrapText()`, aby przygotowac tekst do wyLwietlenia (`m_drawText`).
2.  JeLli wL'aczone jest `m_textAutoResize`, oblicza nowy, preferowany rozmiar widgetu na podstawie rozmiaru tekstu i go ustawia.
3.  Ustawia flage `m_textMustRecache`, aby geometria zostaL'a przeliczona przy nastepnym rysowaniu.
## `void UIWidget::parseTextStyle(...)`

Parsuje z wezL'a OTML wszystkie atrybuty zwiazane z tekstem (`text`, `font`, `text-align`, `text-wrap` itp.).
## `void UIWidget::drawText(const Rect& screenCoords)`

Dodaje zadanie rysowania tekstu do `g_drawQueue`. ULLywa `m_font` do wykonania wL'aLciwej operacji rysowania, przekazujac mu tekst (`m_drawText`), obszar (`m_textCachedScreenCoords`), wyrownanie, kolor i ewentualne informacje o wielu kolorach.
## `void UIWidget::onTextChange(...)` i `onFontChange(...)`

Wirtualne metody, ktore domyLlnie wywoL'uja odpowiednie `callbacki` w Lua.
## `void UIWidget::setText(std::string text, ...)`

GL'owny setter dla tekstu. JeLli `m_textOnlyUpperCase` jest `true`, konwertuje tekst na wielkie litery. Aktualizuje `m_text`, wywoL'uje `updateText()` i `onTextChange`.
## `void UIWidget::setColoredText(...)`

Setter dla tekstu wielokolorowego. Parsuje wektor stringow, budujac `m_text` i `m_textColors`.
## `void UIWidget::setFont(...)`

Ustawia font, pobierajac go z `g_fonts`.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `text-align`.
-   `framework/graphics/fontmanager.h`: Do pobierania fontow.

---
# z"" uiwidgetbasestyle.cpp
## Opis ogolny

Plik `uiwidgetbasestyle.cpp` zawiera implementacje czeLci klasy `UIWidget` odpowiedzialnej za podstawowy styl, czyli wL'aLciwoLci wspolne dla wszystkich widgetow, takie jak tL'o, ramka, ikona i ogolne atrybuty.
## Klasa `UIWidget` (czeLc implementacji)
## `void UIWidget::initBaseStyle()`

Inicjalizuje podstawowe wL'aLciwoLci stylu do wartoLci domyLlnych (np. przezroczyste tL'o, biaL'y kolor, brak ramki).
## `void UIWidget::parseBaseStyle(const OTMLNodePtr& styleNode)`

GL'owna metoda parsujaca styl.
1.  Najpierw parsuje pola i `callbacki` Lua (`@` i `&`), aby byL'y dostepne podczas parsowania innych atrybutow.
2.  Nastepnie parsuje wszystkie podstawowe atrybuty, takie jak `color`, `x`, `y`, `width`, `height`, `background-color`, `opacity`, `rotation`, `enabled`, `visible`, `margin`, `padding`, `border`, `icon`, etc.
3.  ObsL'uguje rownieLL definicje layoutu (`layout: ...`) oraz deklaracje kotwic (`anchors.left: ...`).
## `void UIWidget::drawBackground(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadanie narysowania prostokata wypeL'nionego kolorem `m_backgroundColor`.
## `void UIWidget::drawBorder(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadania narysowania czterech prostokatow tworzacych ramke, kaLLdy z odpowiednim kolorem i gruboLcia.
## `void UIWidget::drawIcon(const Rect& screenCoords)`

JeLli `m_icon` jest ustawiony, dodaje do `g_drawQueue` zadanie narysowania tekstury ikony w odpowiednim miejscu, uwzgledniajac `m_iconAlign`, `m_iconOffset` i `m_iconColor`.
## `void UIWidget::setIcon(const std::string& iconFile)`

Laduje teksture ikony za pomoca `g_textures` i ustawia jej domyLlny `clip-rect`.
## ZaleLLnoLci i powiazania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `icon-align`.
-   `framework/graphics/texturemanager.h`: Do L'adowania tekstur ikon.
-   `framework/graphics/painter.h`: PoLrednio, poprzez `g_drawQueue`.

---
# z"" uianchorlayout.cpp
## Opis ogolny

Plik `uianchorlayout.cpp` zawiera implementacje klas `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, ktore razem tworza system layoutu opartego na kotwicach.
## Klasa `UIAnchor`
## `UIWidgetPtr UIAnchor::getHookedWidget(...)`

Znajduje widget, do ktorego dana kotwica jest "przyczepiona". ObsL'uguje specjalne identyfikatory:
-   `parent`: widget-rodzic.
-   `next`: nastepne rodzeL"stwo.
-   `prev`: poprzednie rodzeL"stwo.
-   Inne: szuka dziecka o danym ID w rodzicu.
## `int UIAnchor::getHookedPoint(...)`

Oblicza wspoL'rzedna (X lub Y) krawedzi widgetu, do ktorego kotwica jest przyczepiona.
## Klasa `UIAnchorGroup`
## `void UIAnchorGroup::addAnchor(...)`

Dodaje nowa kotwice do grupy. JeLli kotwica dla tej samej krawedzi juLL istnieje, jest ona zastepowana.
## Klasa `UIAnchorLayout`
## `void UIAnchorLayout::addAnchor(...)`

GL'owna metoda do tworzenia i dodawania nowej reguL'y kotwiczenia. Tworzy obiekt `UIAnchor` i dodaje go do odpowiedniej `UIAnchorGroup`.
## `bool UIAnchorLayout::updateWidget(...)`
## Opis semantyczny
Rekurencyjna metoda, ktora oblicza nowy `Rect` dla pojedynczego widgetu na podstawie jego kotwic.
## DziaL'anie
1.  JeLli widget, do ktorego sie kotwiczymy, sam nie zostaL' jeszcze zaktualizowany, wywoL'uje `updateWidget` rekurencyjnie dla niego.
2.  Iteruje po wszystkich kotwicach widgetu.
3.  Dla kaLLdej kotwicy, oblicza docelowy punkt (`point`) na podstawie `getHookedPoint`.
4.  Modyfikuje `newRect` widgetu, ustawiajac lub przesuwajac odpowiednia krawedLs (`moveLeft`, `setRight`, `moveVerticalCenter`, itp.).
5.  Po przetworzeniu wszystkich kotwic, ustawia nowy `Rect` dla widgetu.
## `bool UIAnchorLayout::internalUpdate()`

GL'owna metoda aktualizacji layoutu.
1.  Resetuje flagi `m_updated` we wszystkich `UIAnchorGroup`.
2.  W petli przechodzi przez wszystkie widgety zarzadzane przez ten layout i, jeLli nie zostaL'y jeszcze zaktualizowane, wywoL'uje dla nich `updateWidget`. Petla zapewnia, LLe wszystkie zaleLLnoLci zostana rozwiazane.
## ZaleLLnoLci i powiazania

-   `framework/ui/uianchorlayout.h`: Plik nagL'owkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.

---
# Meta-dokumenty
## z"' Spis treLci

-   **`const.h`**: Definicje globalnych staL'ych, makr i typow wyliczeniowych.
-   **`CMakeLists.txt`**: Skrypt konfiguracyjny budowania projektu.
-   **`global.h`**: Centralny plik nagL'owkowy, agregujacy podstawowe zaleLLnoLci.
-   **`pch.h`**: Prekompilowany nagL'owek ze standardowymi bibliotekami.
-   **`luafunctions.cpp`**: Implementacja bindowaL" C++ do Lua.
-   **`resourcemanager.h`**: Deklaracja menedLLera zasobow.
-   **`adaptiverenderer.cpp`**: Implementacja renderera adaptacyjnego.
-   **`adaptiverenderer.h`**: Deklaracja renderera adaptacyjnego.
-   **`application.cpp`**: Implementacja bazowej klasy aplikacji.
-   **`application.h`**: Deklaracja bazowej klasy aplikacji.
-   **`asyncdispatcher.h`**: Deklaracja dyspozytora zadaL" asynchronicznych.
-   **`binarytree.cpp`**: Implementacja czytnika/writera formatu binarnego drzewa.
-   **`asyncdispatcher.cpp`**: Implementacja dyspozytora zadaL" asynchronicznych.
-   **`clock.h`**: Deklaracja klasy zegara.
-   **`binarytree.h`**: Deklaracja klas do obsL'ugi formatu binarnego drzewa.
-   **`config.cpp`**: Implementacja klasy do zarzadzania pojedyncza konfiguracja.
-   **`configmanager.cpp`**: Implementacja menedLLera konfiguracji.
-   **`configmanager.h`**: Deklaracja menedLLera konfiguracji.
-   **`config.h`**: Deklaracja klasy `Config`.
-   **`clock.cpp`**: Implementacja klasy zegara.
-   **`consoleapplication.h`**: Deklaracja aplikacji konsolowej.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `core`.
-   **`event.cpp`**: Implementacja klasy `Event`.
-   **`event.h`**: Deklaracja klasy `Event`.
-   **`eventdispatcher.cpp`**: Implementacja dyspozytora zdarzeL".
-   **`eventdispatcher.h`**: Deklaracja dyspozytora zdarzeL".
-   **`filestream.cpp`**: Implementacja strumienia plikowego.
-   **`filestream.h`**: Deklaracja strumienia plikowego.
-   **`graphicalapplication.cpp`**: Implementacja aplikacji graficznej.
-   **`inputevent.h`**: Deklaracja struktury `InputEvent`.
-   **`graphicalapplication.h`**: Deklaracja aplikacji graficznej.
-   **`logger.h`**: Deklaracja klasy `Logger`.
-   **`module.cpp`**: Implementacja klasy `Module`.
-   **`modulemanager.cpp`**: Implementacja menedLLera moduL'ow.
-   **`logger.cpp`**: Implementacja klasy `Logger`.
-   **`module.h`**: Deklaracja klasy `Module`.
-   **`modulemanager.h`**: Deklaracja menedLLera moduL'ow.
-   **`scheduledevent.cpp`**: Implementacja zdarzenia zaplanowanego.
-   **`resourcemanager.cpp`**: Implementacja menedLLera zasobow.
-   **`scheduledevent.h`**: Deklaracja zdarzenia zaplanowanego.
-   **`timer.cpp`**: Implementacja timera.
-   **`timer.h`**: Deklaracja timera.
-   **`consoleapplication.cpp`**: Implementacja aplikacji konsolowej.
-   **`shaderprogram.h`**: Deklaracja programu shadera.
-   **`animatedtexture.cpp`**: Implementacja tekstury animowanej.
-   **`animatedtexture.h`**: Deklaracja tekstury animowanej.
-   **`apngloader.cpp`**: Implementacja L'adowarki APNG.
-   **`apngloader.h`**: Deklaracja L'adowarki APNG.
-   **`atlas.cpp`**: Implementacja atlasu tekstur.
-   **`bitmapfont.cpp`**: Implementacja fontu bitmapowego.
-   **`atlas.h`**: Deklaracja atlasu tekstur.
-   **`bitmapfont.h`**: Deklaracja fontu bitmapowego.
-   **`cachedtext.cpp`**: Implementacja keszowanego tekstu.
-   **`colorarray.h`**: Deklaracja tablicy kolorow.
-   **`cachedtext.h`**: Deklaracja keszowanego tekstu.
-   **`coordsbuffer.h`**: Deklaracja bufora wspoL'rzednych.
-   **`deptharray.h`**: Deklaracja tablicy gL'ebokoLci.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `graphics`.
-   **`coordsbuffer.cpp`**: Implementacja bufora wspoL'rzednych.
-   **`drawcache.cpp`**: Implementacja cache'a rysowania.
-   **`drawcache.h`**: Deklaracja cache'a rysowania.
-   **`drawqueue.cpp`**: Implementacja kolejki rysowania.
-   **`fontmanager.cpp`**: Implementacja menedLLera fontow.
-   **`fontmanager.h`**: Deklaracja menedLLera fontow.
-   **`drawqueue.h`**: Deklaracja kolejki rysowania.
-   **`framebuffer.cpp`**: Implementacja bufora ramki.
-   **`framebuffer.h`**: Deklaracja bufora ramki.
-   **`framebuffermanager.cpp`**: Implementacja menedLLera buforow ramki.
-   **`graph.cpp`**: Implementacja wykresu debugujacego.
-   **`graph.h`**: Deklaracja wykresu debugujacego.
-   **`glutil.h`**: Narzedzia OpenGL.
-   **`graphics.cpp`**: Implementacja menedLLera grafiki.
-   **`graphics.h`**: Deklaracja menedLLera grafiki.
-   **`image.cpp`**: Implementacja klasy `Image`.
-   **`hardwarebuffer.h`**: Deklaracja bufora sprzetowego.
-   **`image.h`**: Deklaracja klasy `Image`.
-   **`framebuffermanager.h`**: Deklaracja menedLLera buforow ramki.
-   **`painter.h`**: Deklaracja klasy `Painter`.
-   **`painter.cpp`**: Implementacja klasy `Painter`.
-   **`hardwarebuffer.cpp`**: Implementacja bufora sprzetowego.
-   **`paintershaderprogram.cpp`**: Implementacja programu shadera dla `Painter`.
-   **`paintershaderprogram.h`**: Deklaracja programu shadera dla `Painter`.
-   **`shader.cpp`**: Implementacja klasy `Shader`.
-   **`shadermanager.h`**: Deklaracja menedLLera shaderow.
-   **`shadermanager.cpp`**: Implementacja menedLLera shaderow.
-   **`shader.h`**: Deklaracja klasy `Shader`.
-   **`textrender.cpp`**: Implementacja renderera tekstu.
-   **`shaderprogram.cpp`**: Implementacja programu shadera.
-   **`texture.cpp`**: Implementacja klasy `Texture`.
-   **`texture.h`**: Deklaracja klasy `Texture`.
-   **`texturemanager.cpp`**: Implementacja menedLLera tekstur.
-   **`vertexarray.h`**: Deklaracja tablicy wierzchoL'kow.
-   **`texturemanager.h`**: Deklaracja menedLLera tekstur.
-   **`textrender.h`**: Deklaracja renderera tekstu.
-   **`outfits.h`**: Shadery dla strojow.
-   **`newshader.h`**: Nowe shadery.
-   **`shaders.h`**: Agregacja shaderow.
-   **`shadersources.h`**: LarodL'a standardowych shaderow.
-   **`http.cpp`**: Implementacja klienta HTTP/WebSocket.
-   **`websocket.h`**: Deklaracja sesji WebSocket.
-   **`http.h`**: Deklaracja klienta HTTP/WebSocket.
-   **`result.h`**: Deklaracja struktury `HttpResult`.
-   **`session.cpp`**: Implementacja sesji HTTP.
-   **`session.h`**: Deklaracja sesji HTTP.
-   **`websocket.cpp`**: Implementacja sesji WebSocket.
-   **`mouse.cpp`**: Implementacja menedLLera myszy.
-   **`mouse.h`**: Deklaracja menedLLera myszy.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `luaengine`.
-   **`lbitlib.cpp`**: Implementacja biblioteki `bit32` dla Lua.
-   **`lbitlib.h`**: Deklaracja biblioteki `bit32`.
-   **`luabinder.h`**: Mechanizm bindowania C++ do Lua.
-   **`luaexception.h`**: Deklaracja wyjatkow Lua.
-   **`luaexception.cpp`**: Implementacja wyjatkow Lua.
-   **`luainterface.cpp`**: Implementacja interfejsu Lua.
-   **`luainterface.h`**: Deklaracja interfejsu Lua.
-   **`luaobject.cpp`**: Implementacja `LuaObject`.
-   **`luaobject.h`**: Deklaracja `LuaObject`.
-   **`luavaluecasts.cpp`**: Implementacja konwersji typow Lua.
-   **`luavaluecasts.h`**: Deklaracja konwersji typow Lua.
-   **`connection.cpp`**: Implementacja poL'aczenia TCP.
-   **`server.h`**: Deklaracja serwera TCP.
-   **`connection.h`**: Deklaracja poL'aczenia TCP.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `net`.
-   **`inputmessage.h`**: Deklaracja wiadomoLci przychodzacej.
-   **`outputmessage.cpp`**: Implementacja wiadomoLci wychodzacej.
-   **`outputmessage.h`**: Deklaracja wiadomoLci wychodzacej.
-   **`packet_player.cpp`**: Implementacja odtwarzacza pakietow.
-   **`packet_player.h`**: Deklaracja odtwarzacza pakietow.
-   **`protocol.h`**: Deklaracja protokoL'u sieciowego.
-   **`packet_recorder.cpp`**: Implementacja nagrywarki pakietow.
-   **`protocol.cpp`**: Implementacja protokoL'u sieciowego.
-   **`server.cpp`**: Implementacja serwera TCP.
-   **`inputmessage.cpp`**: Implementacja wiadomoLci przychodzacej.
-   **`packet_recorder.h`**: Deklaracja nagrywarki pakietow.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `otml`.
-   **`otmlparser.h`**: Deklaracja parsera OTML.
-   **`otml.h`**: Agregacja nagL'owkow OTML.
-   **`otmldocument.cpp`**: Implementacja dokumentu OTML.
-   **`otmldocument.h`**: Deklaracja dokumentu OTML.
-   **`otmlemitter.cpp`**: Implementacja emittera OTML.
-   **`otmlexception.cpp`**: Implementacja wyjatkow OTML.
-   **`otmlexception.h`**: Deklaracja wyjatkow OTML.
-   **`otmlemitter.h`**: Deklaracja emittera OTML.
-   **`otmlparser.cpp`**: Implementacja parsera OTML.
-   **`otmlnode.h`**: Deklaracja wezL'a OTML.
-   **`otmlnode.cpp`**: Implementacja wezL'a OTML.
-   **`androidplatform.cpp`**: Implementacja platformy dla Androida.
-   **`androidwindow.cpp`**: Implementacja okna dla Androida.
-   **`androidwindow.h`**: Deklaracja okna dla Androida.
-   **`crashhandler.h`**: Deklaracja obsL'ugi awarii.
-   **`platform.cpp`**: Implementacja globalnej instancji platformy.
-   **`platformwindow.cpp`**: Implementacja bazowej klasy okna.
-   **`platform.h`**: Deklaracja klasy `Platform`.
-   **`platformwindow.h`**: Deklaracja bazowej klasy okna.
-   **`sdlwindow.cpp`**: Implementacja okna SDL (WASM).
-   **`sdlwindow.h`**: Deklaracja okna SDL.
-   **`unixcrashhandler.cpp`**: Implementacja obsL'ugi awarii dla Uniksa.
-   **`unixplatform.cpp`**: Implementacja platformy dla Uniksa.
-   **`win32crashhandler.cpp`**: Implementacja obsL'ugi awarii dla Windows.
-   **`win32platform.cpp`**: Implementacja platformy dla Windows.
-   **`win32window.cpp`**: Implementacja okna dla Windows.
-   **`win32window.h`**: Deklaracja okna dla Windows.
-   **`x11window.h`**: Deklaracja okna X11.
-   **`x11window.cpp`**: Implementacja okna X11.
-   **`proxy.cpp`**: Implementacja menedLLera proxy.
-   **`proxy.h`**: Deklaracja menedLLera proxy.
-   **`proxy_client.h`**: Deklaracja klienta proxy.
-   **`proxy_client.cpp`**: Implementacja klienta proxy.
-   **`combinedsoundsource.cpp`**: Implementacja zL'oLLonego LsrodL'a dLswieku.
-   **`combinedsoundsource.h`**: Deklaracja zL'oLLonego LsrodL'a dLswieku.
-   **`oggsoundfile.cpp`**: Implementacja pliku dLswiekowego OGG.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `sound`.
-   **`oggsoundfile.h`**: Deklaracja pliku dLswiekowego OGG.
-   **`soundbuffer.cpp`**: Implementacja bufora dLswieku.
-   **`soundbuffer.h`**: Deklaracja bufora dLswieku.
-   **`soundfile.cpp`**: Implementacja pliku dLswiekowego.
-   **`soundchannel.cpp`**: Implementacja kanaL'u dLswiekowego.
-   **`soundchannel.h`**: Deklaracja kanaL'u dLswiekowego.
-   **`soundfile.h`**: Deklaracja pliku dLswiekowego.
-   **`soundmanager.cpp`**: Implementacja menedLLera dLswieku.
-   **`soundmanager.h`**: Deklaracja menedLLera dLswieku.
-   **`soundsource.cpp`**: Implementacja LsrodL'a dLswieku.
-   **`streamsoundsource.cpp`**: Implementacja strumieniowego LsrodL'a dLswieku.
-   **`streamsoundsource.h`**: Deklaracja strumieniowego LsrodL'a dLswieku.
-   **`soundsource.h`**: Deklaracja LsrodL'a dLswieku.
-   **`any.h`**: Implementacja `stdext::any`.
-   **`cast.h`**: Funkcje do rzutowania typow.
-   **`demangle.cpp`**: Implementacja demanglowania nazw.
-   **`compiler.h`**: Makra specyficzne dla kompilatora.
-   **`demangle.h`**: Deklaracja demanglowania nazw.
-   **`boolean.h`**: Implementacja `stdext::boolean`.
-   **`dumper.h`**: Narzedzie do debugowania.
-   **`dynamic_storage.h`**: Implementacja `dynamic_storage`.
-   **`exception.h`**: Deklaracja `stdext::exception`.
-   **`fastrand.h`**: Szybki generator liczb losowych.
-   **`math.cpp`**: Implementacja funkcji matematycznych.
-   **`math.h`**: Deklaracja funkcji matematycznych.
-   **`net.h`**: Deklaracja narzedzi sieciowych.
-   **`packed_any.h`**: Implementacja `packed_any`.
-   **`shared_object.h`**: Implementacja `shared_object` i `shared_object_ptr`.
-   **`stdext.h`**: Agregacja nagL'owkow `stdext`.
-   **`packed_storage.h`**: Implementacja `packed_storage`.
-   **`thread.h`**: Agregacja nagL'owkow watkow.
-   **`time.h`**: Deklaracja funkcji czasowych.
-   **`traits.h`**: Narzedzia metaprogramowania.
-   **`string.h`**: Deklaracja funkcji do stringow.
-   **`time.cpp`**: Implementacja funkcji czasowych.
-   **`uri.h`**: Deklaracja parsera URI.
-   **`net.cpp`**: Implementacja narzedzi sieciowych.
-   **`uri.cpp`**: Implementacja parsera URI.
-   **`types.h`**: Definicje typow.
-   **`format.h`**: Implementacja `stdext::format`.
-   **`string.cpp`**: Implementacja funkcji do stringow.
-   **`declarations.h`**: Wczesne deklaracje dla moduL'u `ui`.
-   **`ui.h`**: Agregacja nagL'owkow UI.
-   **`uiboxlayout.cpp`**: Implementacja `UIBoxLayout`.
-   **`uiboxlayout.h`**: Deklaracja `UIBoxLayout`.
-   **`uigridlayout.cpp`**: Implementacja `UIGridLayout`.
-   **`uigridlayout.h`**: Deklaracja `UIGridLayout`.
-   **`uihorizontallayout.cpp`**: Implementacja `UIHorizontalLayout`.
-   **`uihorizontallayout.h`**: Deklaracja `UIHorizontalLayout`.
-   **`uilayout.cpp`**: Implementacja `UILayout`.
-   **`uilayout.h`**: Deklaracja `UILayout`.
-   **`uimanager.h`**: Deklaracja `UIManager`.
-   **`uitextedit.cpp`**: Implementacja `UITextEdit`.
-   **`uimanager.cpp`**: Implementacja `UIManager`.
-   **`uitextedit.h`**: Deklaracja `UITextEdit`.
-   **`uitranslator.cpp`**: Implementacja translatorow UI.
-   **`uitranslator.h`**: Deklaracja translatorow UI.
-   **`uiverticallayout.cpp`**: Implementacja `UIVerticalLayout`.
-   **`uiverticallayout.h`**: Deklaracja `UIVerticalLayout`.
-   **`uiwidget.cpp`**: Implementacja `UIWidget`.
-   **`uiwidget.h`**: Deklaracja `UIWidget`.
-   **`uiwidgetimage.cpp`**: Implementacja czeLci `UIWidget` (obraz).
-   **`uianchorlayout.h`**: Deklaracja `UIAnchorLayout`.
-   **`uiwidgettext.cpp`**: Implementacja czeLci `UIWidget` (tekst).
-   **`uiwidgetbasestyle.cpp`**: Implementacja czeLci `UIWidget` (styl).
-   **`uianchorlayout.cpp`**: Implementacja `UIAnchorLayout`.
-   **`color.cpp`**: Implementacja klasy `Color`.
-   **`color.h`**: Deklaracja klasy `Color`.
-   **`crypt.cpp`**: Implementacja narzedzi kryptograficznych.
-   **`databuffer.h`**: Implementacja `DataBuffer`.
-   **`crypt.h`**: Deklaracja narzedzi kryptograficznych.
-   **`extras.cpp`**: Implementacja `Extras`.
-   **`extras.h`**: Deklaracja `Extras`.
-   **`framecounter.h`**: Implementacja licznika klatek.
-   **`matrix.h`**: Implementacja macierzy.
-   **`pngunpacker.cpp`**: Implementacja unpackera PNG.
-   **`pngunpacker.h`**: Deklaracja unpackera PNG.
-   **`point.h`**: Implementacja `Point`.
-   **`qrcodegen.c`**: Implementacja generatora kodow QR.
-   **`qrcodegen.h`**: Deklaracja generatora kodow QR.
-   **`rect.h`**: Implementacja `Rect`.
-   **`size.h`**: Implementacja `Size`.
-   **`stats.cpp`**: Implementacja systemu statystyk.
-   **`stats.h`**: Deklaracja systemu statystyk.
-   **`tinystr.cpp`**: Implementacja `TiXmlString`.
-   **`tinyxmlparser.cpp`**: Implementacja parsera TinyXML.
-   **`tinystr.h`**: Deklaracja `TiXmlString`.
-   **`tinyxml.cpp`**: Implementacja TinyXML.
-   **`tinyxmlerror.cpp`**: BL'edy TinyXML.
-   **`tinyxml.h`**: Deklaracja TinyXML.

---
## z"T Indeks funkcji/metod
*W przygotowaniu*

---
## z Mapa zaleLLnoLci

graph TD
    subgraph Aplikacja
        Application --dziedziczy--> GraphicalApplication
        Application --dziedziczy--> ConsoleApplication
        GraphicalApplication --> PlatformWindow
        GraphicalApplication --> UIManager
        GraphicalApplication --> Graphics
        GraphicalApplication --> SoundManager
    end

    subgraph Framework_Core
        Application --> EventDispatcher
        Application --> ModuleManager
        Application --> ResourceManager
        Application --> ConfigManager
        Application --> Logger
        EventDispatcher --> Event
        Event --dziedziczy--> ScheduledEvent
        Clock & Timer
    end

    subgraph Framework_UI
        UIManager --> UIWidget
        UIWidget --> UILayout
        UILayout --dziedziczy--> UIAnchorLayout
        UILayout --dziedziczy--> UIBoxLayout
        UIBoxLayout --dziedziczy--> UIHorizontalLayout
        UIBoxLayout --dziedziczy--> UIVerticalLayout
        UIWidget --> BitmapFont
        UIWidget --> Painter
    end

    subgraph Framework_Graphics
        Graphics --> Painter
        Graphics --> TextureManager
        Graphics --> FrameBufferManager
        Graphics --> ShaderManager
        Painter --> ShaderProgram
        TextureManager --> Texture
        Texture --dziedziczy--> AnimatedTexture
        Texture --> Image
    end

    subgraph Framework_Platform
        PlatformWindow --implementuje--> WIN32Window
        PlatformWindow --implementuje--> X11Window
        PlatformWindow --implementuje--> AndroidWindow
        PlatformWindow --implementuje--> SDLWindow
        Platform
    end

    subgraph Framework_Lua
        LuaInterface --> LuaObject
        LuaInterface --> luabinder
        UIWidget --dziedziczy--> LuaObject
        Protocol --dziedziczy--> LuaObject
    end

    subgraph Framework_Net
        Protocol --> Connection
        Protocol --> InputMessage & OutputMessage
        ProxyManager --> Proxy & Session
        Connection & Proxy & Session --> Boost.Asio
    end

    subgraph ZaleLLnoLci_Zewnetrzne
        Boost.Asio
        Boost.Beast
        Boost.Process
        OpenGL/GLES/GLEW
        OpenAL
        Lua/LuaJIT
        PhysFS
        ZLIB
        OpenSSL
        TinyXML
    end

    Application --> Framework_Core
    GraphicalApplication --> Framework_Graphics
    GraphicalApplication --> Framework_UI
    GraphicalApplication --> Framework_Platform
    Application --> Framework_Lua
    Application --> Framework_Net

    Framework_Graphics --> OpenGL/GLES/GLEW
    Framework_Net --> ZaleLLnoLci_Zewnetrzne
    ResourceManager --> PhysFS
```
## z Architektura systemu

System `otclient` jest zbudowany w oparciu o architekture moduL'owa i warstwowa, ktora oddziela rdzeL" frameworka od logiki specyficznej dla klienta gry.
## Warstwy

1.  **Warstwa platformy (`framework/platform`)**
    -   **Opis**: NajniLLsza warstwa, ktora abstrakcjonuje interakcje z systemem operacyjnym. Zawiera implementacje dla Windows (WinAPI), Linux/macOS (X11) i Android (NDK/JNI).
    -   **Komponenty**: `Platform` (operacje na plikach, procesach), `PlatformWindow` (zarzadzanie oknem, wejLciem, kontekstem graficznym), `CrashHandler`.
    -   **Cel**: Zapewnienie przenoLnoLci kodu miedzy roLLnymi systemami.

2.  **Warstwa rozszerzeL" standardowych (`framework/stdext`)**
    -   **Opis**: Zbior narzedzi i rozszerzeL" do standardowej biblioteki C++, ktore sa uLLywane w caL'ym projekcie.
    -   **Komponenty**: `shared_object_ptr` (inteligentne wskaLsniki), `cast` (bezpieczne rzutowanie typow), `format` (formatowanie stringow), `string` (narzedzia do stringow), `time` (obsL'uga czasu).
    -   **Cel**: Dostarczenie spojnego i rozbudowanego zestawu narzedzi podstawowych.

3.  **Warstwa rdzenia frameworka (`framework/core`)**
    -   **Opis**: Serce aplikacji. Implementuje gL'owne petle, system zdarzeL", zarzadzanie zasobami, moduL'ami i konfiguracja.
    -   **Komponenty**: `Application` (i pochodne), `EventDispatcher`, `ResourceManager`, `ModuleManager`, `ConfigManager`, `Logger`.
    -   **Cel**: Zapewnienie solidnej podstawy i infrastruktury dla dziaL'ania aplikacji.

4.  **Warstwa silnikow (Framework Engines)**
    -   **Opis**: Zbior wyspecjalizowanych podsystemow (silnikow), ktore realizuja kluczowe funkcjonalnoLci.
    -   **Komponenty**:
        -   **Silnik graficzny (`framework/graphics`, `framework/ui`)**: `Graphics`, `Painter`, `TextureManager`, `UIManager`, `UIWidget`. Odpowiada za caL'e renderowanie 2D i interfejs uLLytkownika.
        -   **Silnik Lua (`framework/luaengine`)**: `LuaInterface`, `luabinder`. Most miedzy C++ a Lua, umoLLliwiajacy skryptowanie.
        -   **Silnik sieciowy (`framework/net`, `framework/proxy`)**: `Protocol`, `Connection`, `ProxyManager`. ObsL'uguje komunikacje z serwerem.
        -   **Silnik dLswieku (`framework/sound`)**: `SoundManager`. ObsL'uguje odtwarzanie dLswieku.
    -   **Cel**: Enkapsulacja zL'oLLonych funkcjonalnoLci w oddzielne, zarzadzalne moduL'y.

5.  **Warstwa logiki klienta (`src/client`)**
    -   **Opis**: NajwyLLsza warstwa, ktora zawiera logike specyficzna dla klienta gry Tibii. Implementuje ona mechanike gry, renderowanie Lwiata, postaci, przedmiotow itp.
    -   **Komponenty**: (NiezaL'aczone w promptcie) `Game`, `Map`, `Creature`, `Item`, `ProtocolGame`.
    -   **Cel**: Implementacja wL'aLciwej gry. Ta warstwa intensywnie korzysta z API dostarczanego przez niLLsze warstwy frameworka.

6.  **Warstwa skryptowa (ModuL'y Lua)**
    -   **Opis**: Zewnetrzna warstwa, ktora pozwala na rozszerzanie i modyfikowanie klienta bez potrzeby rekompilacji kodu C++. Skrypty Lua maja dostep do API frameworka i logiki klienta za poLrednictwem bindowaL".
    -   **Komponenty**: Pliki `.lua` i `.otmod` w katalogach `modules/` i `mods/`.
    -   **Cel**: UmoLLliwienie tworzenia wtyczek, modyfikacji interfejsu i dodawania nowej funkcjonalnoLci.
## PrzepL'yw danych i interakcje

-   **Start aplikacji**: `main()` tworzy instancje `GraphicalApplication`, ktora inicjalizuje warstwy od doL'u do gory (Platforma -> RdzeL" -> Silniki).
-   **GL'owna petla**: `GraphicalApplication::run()` uruchamia wielowatkowa petle. Watek logiki (`worker`) aktualizuje stan gry i przygotowuje dane do rysowania. Watek renderowania (gL'owny) rysuje te dane na ekranie i odbiera zdarzenia od `PlatformWindow`.
-   **Zdarzenia wejLciowe**: `PlatformWindow` -> `GraphicalApplication` -> `UIManager` -> `UIWidget` -> Skrypt Lua (callback `onClick` itp.).
-   **Komunikacja sieciowa**: Skrypt Lua (np. `g_game.login(...)`) -> `ProtocolGame` (Lua) -> `Protocol` (C++) -> `Connection` (C++) -> Siec. Pakiety przychodzace ida w odwrotna strone.
-   **Renderowanie**: Logika klienta (C++ lub Lua) tworzy widgety i ustawia ich wL'aLciwoLci -> `UIManager` i `UIWidget` przygotowuja `DrawQueue` -> `GraphicalApplication` przekazuje `DrawQueue` do `Painter` -> `Painter` wykonuje wywoL'ania OpenGL.
