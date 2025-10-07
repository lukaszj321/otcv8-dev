?# src framework
# # Ponizej znajduje sie kompletna dokumentacja techniczna dla repozytorium, src/framework
# # Opis og�lny

Plik `const.h` pelni role centralnego repozytorium dla stalych, makr i typ�w wyliczeniowych (enum) uzywanych w calym frameworku. Definiuje on kluczowe wartosci, takie jak kody klawiszy, poziomy logowania, flagi wyr�wnania, przyciski myszy, a takze stale matematyczne i makra kompilacji. Jest to fundamentalny plik nagl�wkowy, kt�ry zapewnia sp�jnosc i czytelnosc kodu poprzez zdefiniowanie nazwanych stalych zamiast "magicznych liczb".
# # Definicje i Makra
# # # Makra matematyczne

-   `DEG_TO_RAD`: Sluzy do konwersji stopni na radiany.
    ```cpp
# define DEG_TO_RAD (acos(-1)/180.0)
    ```
-   `RAD_TO_DEC`: Sluzy do konwersji radian�w na stopnie.
    ```cpp
# define RAD_TO_DEC (180.0/acos(-1))
    ```
# # # Makra budowania (Build Macros)

Makra te sa definiowane podczas kompilacji i dostarczaja informacji o wersji i srodowisku budowania.

-   `BUILD_COMMIT`: Przechowuje hash commita Git. Domyslnie "dev".
    ```cpp
# ifndef BUILD_COMMIT
# define BUILD_COMMIT "dev"
# endif
    ```
-   `BUILD_REVISION`: Przechowuje numer rewizji. Domyslnie 0.
    ```cpp
# ifndef BUILD_REVISION
# define BUILD_REVISION 0
# endif
    ```
-   `BUILD_TYPE`: Okresla typ budowania (np. "release", "debug"). Domyslnie "unknown".
    ```cpp
# ifndef BUILD_TYPE
# define BUILD_TYPE "unknown"
# endif
    ```
-   `BUILD_ARCH`: Okresla architekture procesora (x64, x86). Wykrywane automatycznie, jesli nie jest zdefiniowane.
    ```cpp
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
# # Namespace `Fw`

Przestrzen nazw `Fw` (skr�t od Framework) grupuje wszystkie stale i typy wyliczeniowe, aby uniknac konflikt�w nazw w globalnej przestrzeni nazw.
# # # Zmienne globalne

-   `pi`: Stala matematyczna przechowujaca przyblizona wartosc liczby Pi.
    ```cpp
    static const float pi = 3.14159265;
    ```
-   `MIN_ALPHA`: Minimalna wartosc alfa (przezroczystosci), ponizej kt�rej obiekty moga byc uznawane za w pelni przezroczyste.
    ```cpp
    static const float MIN_ALPHA = 0.003f;
    ```
# # # Typy wyliczeniowe (Enums)
# # # # `enum Key`

Definiuje kody klawiszy klawiatury. Wartosci liczbowe dla klawiszy drukowalnych odpowiadaja ich kodom ASCII.

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `KeyUnknown` | 0 | Nieznany klawisz |
| `KeyEscape` | 1 | Klawisz Escape |
| `KeyTab` | 2 | Klawisz Tab |
| `KeyBackspace` | 3 | Klawisz Backspace |
| `KeyEnter` | 5 | Klawisz Enter/Return |
| ... | ... | ... |
| `KeyNumpad9` | 150 | Klawisz 9 na klawiaturze numerycznej |
# # # # `enum LogLevel`

Definiuje poziomy waznosci dla komunikat�w w systemie logowania.

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `LogDebug` | 0 | Wiadomosci debugowania |
| `LogInfo` | 1 | Informacje og�lne |
| `LogWarning` | 2 | Ostrzezenia |
| `LogError` | 3 | Bledy |
| `LogFatal` | 4 | Bledy krytyczne, powodujace zamkniecie aplikacji |
# # # # `enum AspectRatioMode`

Okresla, w jaki spos�b zachowac proporcje obrazu podczas skalowania.

| Nazwa | Opis |
| :--- | :--- |
| `IgnoreAspectRatio` | Ignoruje proporcje, rozciagajac obraz do pelnego rozmiaru. |
| `KeepAspectRatio` | Zachowuje proporcje, dopasowujac obraz do mniejszego wymiaru. |
| `KeepAspectRatioByExpanding` | Zachowuje proporcje, wypelniajac caly obszar (moze przyciac obraz). |
# # # # `enum AlignmentFlag`

Flagi bitowe uzywane do okreslania wyr�wnania tekstu lub widget�w w kontenerze. Mozna je laczyc za pomoca operatora `|`.

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `AlignNone` | 0 | Brak wyr�wnania |
| `AlignLeft` | 1 | Wyr�wnanie do lewej |
| `AlignRight` | 2 | Wyr�wnanie do prawej |
| `AlignTop` | 4 | Wyr�wnanie do g�ry |
| `AlignBottom` | 8 | Wyr�wnanie do dolu |
| `AlignHorizontalCenter` | 16 | Wysrodkowanie w poziomie |
| `AlignVerticalCenter` | 32 | Wysrodkowanie w pionie |
| `AlignCenter` | 48 | Pelne wysrodkowanie (kombinacja `HorizontalCenter` i `VerticalCenter`) |
| ... | ... | Inne kombinacje |
# # # # `enum AnchorEdge`

Definiuje krawedzie, do kt�rych mozna "zakotwiczyc" widget w layoucie typu `UIAnchorLayout`.

| Nazwa | Opis |
| :--- | :--- |
| `AnchorNone` | Brak zakotwiczenia |
| `AnchorTop` | G�rna krawedz |
| `AnchorBottom` | Dolna krawedz |
| ... | ... |
# # # # `enum FocusReason`

Okresla przyczyne, dla kt�rej widget otrzymal fokus.

| Nazwa | Opis |
| :--- | :--- |
| `MouseFocusReason` | Fokus uzyskany przez klikniecie mysza. |
| `KeyboardFocusReason` | Fokus uzyskany przez nawigacje klawiatura (np. Tab). |
| `ActiveFocusReason` | Fokus ustawiony programowo. |
| `OtherFocusReason` | Inna przyczyna. |
# # # # `enum AutoFocusPolicy`

Definiuje, jak widget-rodzic powinien automatycznie ustawiac fokus na swoich dzieciach.

| Nazwa | Opis |
| :--- | :--- |
| `AutoFocusNone` | Brak automatycznego fokusa. |
| `AutoFocusFirst` | Ustawia fokus na pierwszym dziecku, kt�re moze go otrzymac. |
| `AutoFocusLast` | Ustawia fokus na ostatnim dziecku, kt�re moze go otrzymac. |
# # # # `enum InputEventType`

Definiuje typy zdarzen wejsciowych (klawiatura, mysz).

| Nazwa | Opis |
| :--- | :--- |
| `NoInputEvent` | Brak zdarzenia. |
| `KeyTextInputEvent` | Zdarzenie wprowadzenia tekstu. |
| `KeyDownInputEvent` | Zdarzenie wcisniecia klawisza. |
| `KeyPressInputEvent` | Zdarzenie przytrzymania klawisza (auto-powtarzanie). |
| ... | ... |
# # # # `enum MouseButton`

Definiuje przyciski myszy oraz dotyk.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoButton` | Brak przycisku. |
| `MouseLeftButton` | Lewy przycisk myszy. |
| ... | ... |
# # # # `enum MouseWheelDirection`

Definiuje kierunek przewijania k�lkiem myszy.

| Nazwa | Opis |
| :--- | :--- |
| `MouseNoWheel` | Brak przewijania. |
| `MouseWheelUp` | Przewijanie w g�re. |
| `MouseWheelDown` | Przewijanie w d�l. |
# # # # `enum KeyboardModifier`

Flagi bitowe dla klawiszy modyfikujacych (Ctrl, Alt, Shift).

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `KeyboardNoModifier` | 0 | Brak modyfikatora. |
| `KeyboardCtrlModifier` | 1 | Wcisniety Ctrl. |
| `KeyboardAltModifier` | 2 | Wcisniety Alt. |
| `KeyboardShiftModifier` | 4 | Wcisniety Shift. |
# # # # `enum WidgetState`

Flagi bitowe definiujace stan widgetu (np. aktywny, najechany, wcisniety). Uzywane do dynamicznego stylowania widget�w.

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `InvalidState` | -1 | Nieprawidlowy stan. |
| `DefaultState` | 0 | Stan domyslny. |
| `ActiveState` | 1 | Widget jest aktywny. |
| `FocusState` | 2 | Widget ma fokus. |
| `HoverState` | 4 | Kursor myszy jest nad widgetem. |
| ... | ... | ... |
# # # # `enum DrawPane`

Okresla warstwe rysowania dla widget�w, co pozwala na kontrolowanie kolejnosci renderowania.

| Nazwa | Wartosc | Opis |
| :--- | :--- | :--- |
| `ForegroundPane` | 1 | Warstwa pierwszoplanowa (interfejs uzytkownika). |
| `MapBackgroundPane` | 2 | Tlo mapy gry. |
| `MapForegroundPane` | 3 | Pierwszy plan mapy gry (np. efekty nad postaciami). |
# # Zaleznosci i powiazania

-   `framework/stdext/compiler.h`: Plik ten dostarcza makr i definicji specyficznych dla kompilatora (np. `BUILD_COMPILER`).

---
# ?? CMakeLists.txt
# # Opis og�lny

Plik `CMakeLists.txt` jest gl�wnym skryptem konfiguracyjnym dla systemu budowania CMake. Jego rola jest zdefiniowanie, jak projekt `otclient` ma byc kompilowany. Okresla on flagi kompilatora, zaleznosci od bibliotek zewnetrznych, liste plik�w zr�dlowych oraz opcje konfiguracyjne, kt�re pozwalaja dostosowac proces budowania do r�znych platform (Windows, Linux, Apple, WebAssembly) i potrzeb (np. wlaczenie/wylaczenie obslugi dzwieku, grafiki, sieci).
# # Opcje budowania

Skrypt definiuje kilka opcji, kt�re mozna kontrolowac podczas generowania projektu.

| Opcja | Domyslnie | Opis |
| :--- | :--- | :--- |
| `LUAJIT` | `ON` | Uzywa LuaJIT zamiast standardowej biblioteki Lua. |
| `CRASH_HANDLER` | `ON` (poza Apple) | Wlacza generowanie raport�w po awarii aplikacji. |
| `USE_STATIC_LIBS`| `ON` (poza Apple) | Linkuje biblioteki statycznie zamiast dynamicznie (DLL). |
| `USE_LIBCPP` | `OFF` (dla Apple `ON`)| Uzywa `libc++` zamiast `stdc++`. |
| `USE_LTO` | `OFF` | Wlacza optymalizacje w czasie linkowania (Link Time Optimizations). |
| `OPENGLES` | `OFF` | Uzywa OpenGL ES zamiast standardowego OpenGL. Dostepne wersje "1.0", "2.0". |
| `WINDOWS_CONSOLE`| `OFF` | Wlacza okno konsoli w systemie Windows. |
# # Flagi frameworka

Skrypt uzywa flag preprocesora do warunkowej kompilacji modul�w:
-   `FRAMEWORK_SOUND`: Wlacza kompilacje modulu dzwieku.
-   `FRAMEWORK_GRAPHICS`: Wlacza kompilacje modulu grafiki.
-   `FRAMEWORK_NET`: Wlacza kompilacje modulu sieciowego.
-   `FRAMEWORK_XML`: Wlacza kompilacje modulu do parsowania XML (TinyXML).
-   `FRAMEWORK_THREAD_SAFE`: Dodaje definicje `THREAD_SAFE`, prawdopodobnie dla kodu wielowatkowego.
# # Struktura projektu (pliki zr�dlowe)

Plik definiuje liste wszystkich plik�w zr�dlowych (`.h`, `.cpp`, `.c`) skladajacych sie na framework. Sa one pogrupowane w logiczne moduly:

-   **Gl�wne pliki**: `const.h`, `global.h`, `pch.h`, `luafunctions.cpp`
-   **`util`**: Narzedzia pomocnicze (kolory, kryptografia, obsluga PNG, struktury danych jak `Rect`, `Point`).
-   **`stdext`**: Rozszerzenia standardowej biblioteki C++ (obsluga string�w, czasu, rzutowania typ�w, watk�w).
-   **`core`**: Rdzen aplikacji (petla gl�wna, obsluga zdarzen, logowanie, zarzadzanie modulami i zasobami).
-   **`luaengine`**: Silnik Lua i mechanizmy bindowania C++ do Lua.
-   **`otml`**: Parser i emiter dla jezyka OTML (OTClient Markup Language).
-   **`platform`**: Kod specyficzny dla platformy (obsluga okien, obsluga awarii).
-   **`graphics` (warunkowo)**: Silnik graficzny (OpenGL, shadery, tekstury, fonty, UI).
-   **`sound` (warunkowo)**: Silnik dzwieku (OpenAL, obsluga OGG Vorbis).
-   **`net` (warunkowo)**: Obsluga sieci (polaczenia, protokoly, serwer, proxy).
-   **`xml` (warunkowo)**: Parser TinyXML.
# # Zaleznosci i powiazania

Skrypt wyszukuje i linkuje nastepujace biblioteki zewnetrzne:
-   **Boost** (`system`, `filesystem`): Uzywane do operacji na systemie plik�w i innych podstawowych funkcjonalnosci.
-   **ZLIB, BZip2, LibZip**: Do kompresji i dekompresji danych.
-   **LuaJIT** lub **Lua**: Silnik skryptowy.
-   **PhysFS**: Wirtualny system plik�w, do obslugi zasob�w w archiwach.
-   **OpenSSL**: Do funkcji kryptograficznych (RSA, SHA, MD5).
-   **OpenGL/OpenGLES, EGL**: Do renderowania grafiki.
-   **GLEW**: Do zarzadzania rozszerzeniami OpenGL.
-   **OpenAL, Vorbis, Ogg**: Do obslugi dzwieku.
# # # Konfiguracja dla WebAssembly (WASM)
Specjalny blok `if(WASM)` dostosowuje kompilacje dla platformy WebAssembly przy uzyciu Emscripten. Ustawia specyficzne flagi (`-s USE_ZLIB=1`, etc.), linkuje prekompilowane biblioteki (`.a`) i dolacza zr�dla Lua bezposrednio do projektu, zamiast linkowac je jako zewnetrzna biblioteke.
# # # Flagi kompilatora
Skrypt ustawia r�zne flagi kompilatora w zaleznosci od typu budowania (`CMAKE_BUILD_TYPE`):
-   **Debug**: `-O0 -g` (niska optymalizacja, pelne informacje debugowania).
-   **Release**: `-O2` (wysoka optymalizacja, brak informacji debugowania).
-   **RelWithDebInfo**: `-O1 -g` (srednia optymalizacja z informacjami debugowania).
-   **Performance**: `-Ofast -march=native` (najwyzsze optymalizacje, specyficzne dla architektury).

---
# ?? global.h
# # Opis og�lny

Plik `global.h` jest jednym z kluczowych plik�w nagl�wkowych w frameworku. Jego gl�wnym zadaniem jest wlaczenie najwazniejszych, globalnie uzywanych definicji i nagl�wk�w w jednym miejscu. Dzieki temu inne pliki moga dolaczyc tylko ten jeden plik, aby uzyskac dostep do podstawowych typ�w danych, stalych, makr i narzedzi.
# # Definicje i Makra
# # # `VALIDATE(expression)`

Jest to makro asercji, kt�re jest aktywne tylko w trybie debugowania (gdy `NDEBUG` nie jest zdefiniowane). Jesli wyrazenie (expression) jest falszywe, makro wywoluje funkcje `fatalError`, kt�ra przerywa dzialanie programu i wyswietla komunikat o bledzie zawierajacy nazwe pliku i numer linii. W trybie wydajnosciowym (`NDEBUG` zdefiniowane) makro jest puste i nie generuje zadnego kodu.

```cpp
# if defined(NDEBUG)
# define VALIDATE(expression) ((void)0)
# else
extern void fatalError(const char* error, const char* file, int line);
# define VALIDATE(expression) { if(!(expression)) fatalError(#expression, __FILE__, __LINE__); };
# endif
```
-   **Uzycie**: Sluzy do sprawdzania warunk�w, kt�re musza byc zawsze prawdziwe w trakcie dzialania programu, np. sprawdzania, czy wskaznik nie jest `nullptr`.
# # Zaleznosci i powiazania

Plik `global.h` wlacza nastepujace nagl�wki, udostepniajac ich zawartosc wszystkim plikom, kt�re go dolaczaja:

-   `framework/stdext/compiler.h`: Zawiera definicje specyficzne dla kompilatora.
-   `framework/pch.h`: Prekompilowany nagl�wek, kt�ry zawiera standardowe biblioteki C/C++ oraz biblioteki firm trzecich, takie jak Boost.
-   `framework/const.h`: Definiuje globalne stale, makra i typy wyliczeniowe (enumy).
-   `framework/stdext/stdext.h`: Zawiera rozszerzenia standardowej biblioteki C++, takie jak dodatkowe algorytmy.
-   `framework/util/point.h`, `color.h`, `rect.h`, `size.h`, `matrix.h`: Definiuja podstawowe struktury danych uzywane w grafice i logice.
-   `framework/core/logger.h`: Udostepnia globalny obiekt `g_logger` do logowania komunikat�w.

Dzieki temu `global.h` dziala jako centralny punkt dostepu do najczesciej uzywanych element�w frameworka.

---
# ?? pch.h
# # Opis og�lny

`pch.h` (Precompiled Header) to plik nagl�wkowy, kt�rego celem jest przyspieszenie procesu kompilacji. Zawiera on dyrektywy `#include` dla nagl�wk�w, kt�re sa czesto uzywane w calym projekcie, ale rzadko sie zmieniaja. Kompilator moze wstepnie przetworzyc ten plik i zapisac jego stan, co pozwala na ponowne wykorzystanie go podczas kompilacji innych plik�w zr�dlowych, zamiast parsowac te same nagl�wki wielokrotnie.
# # Zawartosc pliku

Plik ten jest podzielony na kilka sekcji, grupujacych nagl�wki wedlug ich pochodzenia i przeznaczenia.
# # # Standardowe nagl�wki C

Zawiera podstawowe nagl�wki z biblioteki standardowej C, takie jak `cstdio`, `cstdlib`, `cstring`, `cmath`.

```cpp
# include <cstdio>
# include <cstdlib>
# include <cstddef>
# include <cstring>
# include <cmath>
```
# # # Standardowe nagl�wki STL (C++)

Wlacza najwazniejsze i najczesciej uzywane kontenery, strumienie i algorytmy z biblioteki standardowej C++.

```cpp
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
# # # Nowoczesne nagl�wki C++ (C++11 i nowsze)

Wlacza nagl�wki zwiazane z wielowatkowoscia, inteligentnymi wskaznikami, czasem i losowoscia, wprowadzone w nowszych standardach C++. Plik `filesystem` jest dolaczany warunkowo (poza Androidem).

```cpp
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
# # # Biblioteka Boost

Wlacza nagl�wki z biblioteki Boost, gl�wnie z modul�w **Asio** (do operacji sieciowych) i **Beast** (do obslugi protokol�w HTTP i WebSocket).

-   `boost/system/config.hpp`, `error_code.hpp`: Podstawowe elementy systemu Boost.
-   `boost/asio.hpp`, `beast.hpp`: Gl�wne nagl�wki dla Asio i Beast.
-   Nagl�wki warunkowe dla SSL (`__EMSCRIPTEN__` wylacza je, poniewaz obsluga SSL w przegladarce jest inna).
-   `boost/algorithm/hex.hpp`: Do operacji na systemie szesnastkowym.

```cpp
# ifdef ANDROID
# define BOOST_UUID_RANDOM_PROVIDER_FORCE_POSIX
# endif
# include <boost/system/config.hpp>
// ... (inne nagl�wki boost)
```
# # Zaleznosci i powiazania

Plik `pch.h` jest plikiem "lisciem" w hierarchii zaleznosci - sam nie zalezy od innych plik�w projektu. Jednakze, jest on dolaczany przez `global.h`, co czyni go posrednia zaleznoscia dla niemal kazdego pliku w projekcie. Zapewnia on dostep do szerokiej gamy narzedzi z biblioteki standardowej C++ i Boost.

---
# ?? luafunctions.cpp
# # Opis og�lny

Plik `luafunctions.cpp` implementuje metode `Application::registerLuaFunctions()`, kt�ra jest kluczowym elementem integracji silnika C++ z Lua. Funkcja ta jest odpowiedzialna za zarejestrowanie (zbindowanie) klas, funkcji i obiekt�w singletonowych z C++ w globalnym srodowisku Lua. Dzieki temu skrypty Lua moga wywolywac funkcje C++, tworzyc obiekty C++ (np. widgety UI) i manipulowac nimi, co stanowi podstawe modularnosci i rozszerzalnosci klienta.
# # `Application::registerLuaFunctions()`
# # # Opis semantyczny

Metoda ta jest wywolywana jednorazowo podczas inicjalizacji aplikacji (`Application::init`). Przechodzi przez wszystkie gl�wne moduly frameworka (takie jak `Platform`, `Application`, `Crypt`, `ResourceManager`, `UIManager` itd.) i udostepnia ich publiczne API w srodowisku Lua. Kazdy zarejestrowany element staje sie dostepny w Lua jako zmienna globalna (np. `g_app`, `g_crypt`) lub jako klasa (np. `UIWidget`).
# # # Zarejestrowane elementy

Ponizej znajduje sie lista zarejestrowanych element�w pogrupowanych wedlug modul�w.
# # # # Konwersje i narzedzia globalne

Rejestruje globalne funkcje pomocnicze w Lua do konwersji typ�w danych miedzy stringami a obiektami C++ oraz inne narzedzia.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `torect` | `stdext::from_string<Rect>` | Konwertuje string na obiekt `Rect`. |
| `topoint` | `stdext::from_string<Point>` | Konwertuje string na obiekt `Point`. |
| `ucwords` | `stdext::ucwords` | Zamienia pierwsza litere kazdego slowa na wielka. |
| `regexMatch` | `lambda` | Wyszukuje dopasowania wyrazen regularnych w stringu. |
| ... | ... | ... |
# # # # Platform (`g_platform`)

Udostepnia funkcje zwiazane z systemem operacyjnym. Niekt�re funkcje sa dostepne tylko gdy zdefiniowano `UNSAFE_LUA_FUNCTIONS`.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `spawnProcess` | `Platform::spawnProcess` | Uruchamia nowy proces (niebezpieczne). |
| `getProcessId` | `Platform::getProcessId` | Zwraca ID biezacego procesu. |
| `openUrl` | `Platform::openUrl` | Otwiera podany URL w domyslnej przegladarce. |
| `getOSName` | `Platform::getOSName` | Zwraca nazwe systemu operacyjnego. |
| ... | ... | ... |
# # # # Application (`g_app`)

Udostepnia API do zarzadzania gl�wnym obiektem aplikacji.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `setName` | `Application::setName` | Ustawia nazwe aplikacji. |
| `isRunning` | `Application::isRunning` | Sprawdza, czy aplikacja jest uruchomiona. |
| `exit` | `Application::exit` | Inicjuje proces zamykania aplikacji. |
| `getBuildCompiler`| `Application::getBuildCompiler`| Zwraca nazwe kompilatora uzytego do budowy. |
| `isMobile` | `Application::isMobile` | Sprawdza, czy aplikacja dziala w trybie mobilnym. |
| ... | ... | ... |
# # # # Crypt (`g_crypt`)

Udostepnia funkcje kryptograficzne.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `genUUID` | `Crypt::genUUID` | Generuje unikalny identyfikator UUID. |
| `sha1Encode` | `Crypt::sha1Encode` | Koduje string za pomoca SHA1. |
| `rsaGenerateKey`| `Crypt::rsaGenerateKey` | Generuje klucze RSA. |
| ... | ... | ... |
# # # # Clock (`g_clock`)

Udostepnia funkcje zwiazane z czasem i zegarem systemowym.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `micros` | `Clock::micros` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `millis` | `Clock::millis` | Zwraca czas w milisekundach. |
| `seconds` | `Clock::seconds` | Zwraca czas w sekundach. |
| ... | ... | ... |
# # # # ConfigManager (`g_configs`)

API do zarzadzania plikami konfiguracyjnymi.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `getSettings` | `ConfigManager::getSettings` | Zwraca gl�wny obiekt konfiguracyjny. |
| `load` | `ConfigManager::load` | Laduje plik konfiguracyjny. |
| ... | ... | ... |
# # # # Logger (`g_logger`)

API do logowania wiadomosci.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `log` | `Logger::log` | Loguje wiadomosc z podanym poziomem. |
| `debug` | `Logger::debug` | Loguje wiadomosc na poziomie `LogDebug`. |
| ... | ... | ... |
# # # # ResourceManager (`g_resources`)

Zarzadzanie plikami i zasobami.

| Nazwa w Lua | Funkcja C++ | Opis |
| :--- | :--- | :--- |
| `fileExists` | `ResourceManager::fileExists` | Sprawdza, czy plik istnieje. |
| `readFileContents`| `ResourceManager::readFileContentsSafe` | Odczytuje zawartosc pliku. |
| `writeFileContents`|`ResourceManager::writeFileContents` | Zapisuje zawartosc do pliku. |
| `createArchive` | `ResourceManager::createArchive` | Tworzy archiwum ZIP z podanych plik�w. |
| ... | ... | ... |
# # # # UI i Grafika (zalezne od `FW_GRAPHICS`)

Rejestruje klasy i funkcje zwiazane z interfejsem uzytkownika, oknem, grafika i fontami. To najobszerniejsza sekcja.

-   **`g_app` (metody graficzne)**: `setMaxFps`, `getFps`, `doScreenshot`
-   **`g_window`**: Zarzadzanie oknem aplikacji (`move`, `resize`, `setTitle`, `setFullscreen`).
-   **`g_mouse`**: Zarzadzanie kursorami myszy.
-   **`g_graphics`**: Informacje o sterowniku graficznym.
-   **`g_textures`**: Zarzadzanie teksturami.
-   **`g_shaders`**: Tworzenie i zarzadzanie shaderami.
-   **`g_ui`**: Gl�wny menedzer UI (`loadUI`, `createWidget`).
-   **`g_fonts`**: Zarzadzanie fontami.
-   **`UIWidget`**: Rejestracja klasy bazowej dla wszystkich widget�w z ogromna liczba metod (np. `addChild`, `setRect`, `setText`, `setImageSource`).
-   **`UILayout` i pochodne**: Rejestracja klas layout�w (`UIBoxLayout`, `UIVerticalLayout`, `UIGridLayout`, `UIAnchorLayout`).
-   **`UITextEdit`**: Rejestracja widgetu do edycji tekstu.
# # # # Siec (zalezne od `FW_NET`)

Rejestruje klasy do obslugi sieci.

-   **`Server`**: Do tworzenia serwer�w nasluchujacych.
-   **`Connection`**: Reprezentuje polaczenie TCP.
-   **`Protocol`**: Implementuje protok�l komunikacyjny.
-   **`InputMessage` / `OutputMessage`**: Do odczytu i zapisu pakiet�w.
-   **`g_proxy`**: Menedzer proxy.
-   **`g_http`**: Do zapytan HTTP/HTTPS i WebSocket.
# # # # Dzwiek (zalezne od `FW_SOUND`)

Rejestruje klasy i funkcje do obslugi dzwieku.

-   **`g_sounds`**: Menedzer dzwieku (`play`, `stopAll`).
-   **`SoundChannel`**: Kanaly dzwiekowe.
-   **`SoundSource`**: Zr�dla dzwieku.
# # Zaleznosci i powiazania

Plik ten jest silnie powiazany z praktycznie kazdym modulem frameworka, poniewaz jego zadaniem jest udostepnienie ich funkcjonalnosci w Lua. Wlacza nagl�wki z:
-   `framework/core`
-   `framework/luaengine`
-   `framework/otml`
-   `framework/util`
-   `framework/graphics` (jesli `FW_GRAPHICS` jest zdefiniowane)
-   `framework/sound` (jesli `FW_SOUND` jest zdefiniowane)
-   `framework/net`
-   `framework/http`
-   `framework/proxy`
-   `framework/input`

Jest to centralny punkt laczacy warstwe C++ z warstwa skryptowa Lua.

---
# ?? resourcemanager.h
# # Opis og�lny

Plik `resourcemanager.h` deklaruje klase `ResourceManager`, kt�ra jest singletonem (`g_resources`) odpowiedzialnym za zarzadzanie wszystkimi zasobami plik�w w aplikacji. Abstrakcjonuje dostep do plik�w, umozliwiajac ich odczyt zar�wno z fizycznego systemu plik�w, jak i z wirtualnych archiw�w (np. `data.zip`) lub nawet z pamieci (dane wbudowane w plik wykonywalny). Jest to kluczowy element, kt�ry umozliwia latwe zarzadzanie zasobami gry, takimi jak grafiki, dzwieki, skrypty i pliki konfiguracyjne.
# # Klasa `ResourceManager`
# # # Opis semantyczny

`ResourceManager` inicjalizuje wirtualny system plik�w oparty na bibliotece **PhysFS**. Okresla on katalogi robocze (`work dir`) i katalogi do zapisu (`write dir`), montuje archiwa z danymi i dostarcza ujednolicony interfejs do operacji na plikach. Klasa ta obsluguje r�wniez szyfrowanie i deszyfrowanie plik�w w locie oraz mechanizmy aktualizacji klienta.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init(const char *argv0)` | Inicjalizuje PhysFS i ustawia sciezke do pliku binarnego aplikacji. |
| `terminate()` | Deinicjalizuje PhysFS. |
| `launchCorrect(...)` | Sprawdza, czy istnieje nowsza wersja pliku wykonywalnego w katalogu zapisu i ja uruchamia (tylko Windows). |
| `setupWriteDir(...)` | Konfiguruje i montuje katalog zapisu dla danych uzytkownika. |
| `setup()` | Wyszukuje i montuje gl�wny katalog roboczy (np. z plikiem `init.lua` lub archiwum `data.zip`). |
| `loadDataFromSelf(...)` | Pr�buje zaladowac dane (archiwum) wbudowane w sam plik wykonywalny. |
| `fileExists(...)` | Sprawdza, czy plik istnieje w wirtualnym systemie plik�w. |
| `directoryExists(...)` | Sprawdza, czy katalog istnieje. |
| `readFileContents(...)` | Odczytuje zawartosc pliku jako string, opcjonalnie deszyfrujac go. |
| `writeFileContents(...)` | Zapisuje string do pliku w katalogu zapisu. |
| `openFile(...)` | Otwiera plik i zwraca wskaznik do `FileStream` do odczytu. |
| `createFile(...)` | Tworzy plik i zwraca wskaznik do `FileStream` do zapisu. |
| `deleteFile(...)` | Usuwa plik. |
| `makeDir(...)` | Tworzy katalog. |
| `listDirectoryFiles(...)` | Zwraca liste plik�w w danym katalogu. |
| `resolvePath(...)` | Tlumaczy sciezke relatywna (np. wzgledem biezacego skryptu Lua) na sciezke absolutna w wirtualnym systemie plik�w. |
| `getWorkDir()` | Zwraca gl�wny katalog roboczy (zawsze "/"). |
| `getWriteDir()` | Zwraca sciezke do katalogu zapisu. |
| `getBinaryName()` | Zwraca nazwe pliku wykonywalnego aplikacji. |
| `fileChecksum(...)` | Oblicza sume kontrolna CRC32 dla pliku. |
| `filesChecksums()` | Zwraca mape sum kontrolnych dla wszystkich plik�w w zamontowanym archiwum. |
| `selfChecksum()` | Oblicza sume kontrolna CRC32 dla samego pliku wykonywalnego. |
| `updateData(...)` | Aktualizuje pliki w gl�wnym archiwum `data.zip`. |
| `updateExecutable(...)` | Zastepuje plik wykonywalny nowa wersja (np. po aktualizacji). |
| `createArchive(...)` | Tworzy archiwum ZIP w pamieci z podanej mapy plik�w. |
| `decompressArchive(...)` | Dekompresuje archiwum ZIP (z pliku lub danych w pamieci) i zwraca mape plik�w. |
| `encrypt(...)` | (Tylko z `WITH_ENCRYPTION`) Szyfruje pliki w katalogach `data`, `modules` itp. |
| `setLayout(...)` | Ustawia aktywny layout UI, co wplywa na rozwiazywanie sciezek do zasob�w. |
# # # Zmienne prywatne

-   `m_binaryPath`: Sciezka do pliku wykonywalnego.
-   `m_writeDir`: Sciezka do katalogu zapisu.
-   `m_loadedFromMemory`: Flaga wskazujaca, czy zasoby zostaly zaladowane z pamieci.
-   `m_loadedFromArchive`: Flaga wskazujaca, czy zasoby zostaly zaladowane z archiwum.
-   `m_memoryData`: Wskaznik na dane archiwum w pamieci.
-   `m_customEncryption`: Klucz do niestandardowego szyfrowania.
-   `m_layout`: Nazwa aktywnego layoutu.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Definicje podstawowych typ�w w rdzeniu frameworka.
-   **PhysFS**: Biblioteka do obslugi wirtualnego systemu plik�w jest kluczowa zaleznoscia.
-   **ZLIB, LibZip**: Uzywane do obslugi archiw�w ZIP.
-   `FileStream`: Klasa `ResourceManager` tworzy i zwraca obiekty `FileStream` do operacji na plikach.
-   `Application`: Uzywane do sprawdzania stanu aplikacji (np. czy jest zamykana).
-   `Logger`: Do logowania bled�w i informacji.
-   `Crypt`: Do obliczania sum kontrolnych i (de)szyfrowania.
-   `Http`: Uzywane w kontekscie pobierania plik�w (`/downloads`).

---
# ?? adaptiverenderer.cpp
# # Opis og�lny

Plik `adaptiverenderer.cpp` zawiera implementacje klasy `AdaptiveRenderer`, kt�ra jest odpowiedzialna za dynamiczne dostosowywanie jakosci i wydajnosci renderowania grafiki w zaleznosci od aktualnej liczby klatek na sekunde (FPS). Celem tego mechanizmu jest utrzymanie plynnosci dzialania aplikacji, zwlaszcza na slabszych komputerach, poprzez redukcje liczby renderowanych obiekt�w lub obnizenie czestotliwosci aktualizacji, gdy FPS spada.
# # Zmienne globalne
# # # `g_adaptiveRenderer`

Globalna instancja klasy `AdaptiveRenderer`, dostepna w calym projekcie.

```cpp
AdaptiveRenderer g_adaptiveRenderer;
```
# # Klasa `AdaptiveRenderer`
# # # `void newFrame()`
# # # # Opis semantyczny
Metoda wywolywana na poczatku kazdej klatki renderowania. Rejestruje czas biezacej klatki i na podstawie liczby klatek z ostatnich 5 sekund decyduje, czy nalezy zmienic poziom wydajnosci (zwiekszyc lub zmniejszyc).
# # # # Dzialanie
1.  Dodaje biezacy czas (w milisekundach) do kolejki `m_frames`.
2.  Usuwa z kolejki klatki starsze niz 5 sekund.
3.  Jesli poziom wydajnosci jest narzucony (`m_forcedSpeed`), metoda konczy dzialanie.
4.  Co 5 sekund (`m_update + 5000 > now`):
    -   Pobiera maksymalny docelowy FPS z `g_app.getMaxFps()`.
    -   Jesli aktualna liczba klatek jest nizsza niz pr�g, zwieksza poziom `m_speed` (obniza jakosc).
    -   Jesli aktualna liczba klatek jest wyzsza niz pr�g, zmniejsza poziom `m_speed` (zwieksza jakosc).
    -   Poziom `m_speed` jest ograniczony do przedzialu `[1, RenderSpeeds - 1]`.
# # # `void refresh()`
# # # # Opis semantyczny
Resetuje czas ostatniej aktualizacji poziomu wydajnosci, co powoduje, ze kolejna ocena FPS nastapi dopiero za 5 sekund.

```cpp
void AdaptiveRenderer::refresh() {
    m_update = stdext::millis();
}
```
# # # Metody limitujace
# # # # Opis semantyczny
Grupa metod zwracajacych limity dla r�znych aspekt�w renderowania w zaleznosci od aktualnego poziomu `m_speed`. Im wyzszy `m_speed`, tym nizsze limity i wieksze interwaly, co przeklada sie na mniejsze obciazenie procesora i karty graficznej.

-   **`effetsLimit()`**: Zwraca maksymalna liczbe efekt�w do renderowania.
-   **`creaturesLimit()`**: Zwraca maksymalna liczbe stworzen.
-   **`itemsLimit()`**: Zwraca maksymalna liczbe przedmiot�w.
-   **`mapRenderInterval()`**: Zwraca interwal (w milisekundach) ponownego renderowania mapy. `0` oznacza renderowanie w kazdej klatce.
-   **`textsLimit()`**: Zwraca maksymalna liczbe tekst�w.
-   **`creaturesRenderInterval()`**: Zwraca interwal renderowania stworzen (obecnie nieuzywane).
-   **`allowFading()`**: Zwraca `true`, jesli dozwolone jest plynne zanikanie/pojawianie sie obiekt�w (tylko na wyzszych poziomach jakosci).
-   **`foregroundUpdateInterval()`**: Zwraca interwal aktualizacji pierwszego planu.
# # # `std::string getDebugInfo()`
# # # # Opis semantyczny
Zwraca sformatowany ciag znak�w z informacjami debugowania, takimi jak aktualna liczba klatek, biezacy poziom `m_speed` i narzucony poziom `m_forcedSpeed`.
# # Zaleznosci i powiazania

-   `framework/core/graphicalapplication.h`: Uzywa `g_app.getMaxFps()` do okreslenia docelowej liczby klatek.
-   `framework/stdext/format.h`: Do formatowania stringa w `getDebugInfo`.
-   `framework/util/extras.h`: Potencjalnie do flag debugowania.
-   `framework/core/logger.h`: Do logowania.

---
# ?? adaptiverenderer.h
# # Opis og�lny

Plik `adaptiverenderer.h` jest plikiem nagl�wkowym dla klasy `AdaptiveRenderer`. Deklaruje on interfejs tej klasy, stale oraz globalna instancje `g_adaptiveRenderer`. Umozliwia to innym czesciom systemu odpytywanie o aktualne limity i ustawienia wydajnosci renderowania.
# # Definicje i Makra
# # # `constexpr int RenderSpeeds`

Definiuje liczbe dostepnych poziom�w wydajnosci renderowania.

```cpp
constexpr int RenderSpeeds = 5;
```
# # Klasa `AdaptiveRenderer`
# # # Opis semantyczny
Klasa `AdaptiveRenderer` zarzadza dynamicznym skalowaniem jakosci grafiki w celu utrzymania plynnosci dzialania aplikacji. Implementuje mechanizm, kt�ry na podstawie biezacej liczby klatek na sekunde (FPS) dostosowuje r�zne parametry renderowania, takie jak limity renderowanych obiekt�w czy czestotliwosc odswiezania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void newFrame()` | Rejestruje nowa klatke i aktualizuje poziom wydajnosci, jesli to konieczne. |
| `void refresh()` | Resetuje zegar aktualizacji, op�zniajac nastepna ocene wydajnosci. |
| `int effetsLimit()` | Zwraca limit dla renderowanych efekt�w. |
| `int creaturesLimit()` | Zwraca limit dla renderowanych stworzen. |
| `int itemsLimit()` | Zwraca limit dla renderowanych przedmiot�w. |
| `int textsLimit()` | Zwraca limit dla renderowanych tekst�w. |
| `int mapRenderInterval()` | Zwraca interwal (op�znienie) ponownego renderowania mapy. |
| `int creaturesRenderInterval()` | Zwraca interwal renderowania stworzen. |
| `bool allowFading()` | Sprawdza, czy dozwolone jest renderowanie efekt�w przejscia (fading). |
| `int getLevel()` | Zwraca aktualny poziom wydajnosci (`m_speed`). |
| `int foregroundUpdateInterval()` | Zwraca interwal aktualizacji pierwszego planu. |
| `std::string getDebugInfo()` | Zwraca informacje debugowania jako string. |
| `void setForcedLevel(int value)` | Umozliwia reczne ustawienie (narzucenie) poziomu wydajnosci. |
# # # Zmienne prywatne

-   `m_forcedSpeed`: Narzucony poziom wydajnosci (-1 oznacza automatyczny).
-   `m_speed`: Aktualny, automatycznie wyliczony poziom wydajnosci (od 0 do `RenderSpeeds-1`).
-   `m_update`: Czas ostatniej aktualizacji poziomu wydajnosci.
-   `m_frames`: Lista czas�w ostatnich klatek, uzywana do obliczania FPS.
# # # Zmienne globalne

-   `g_adaptiveRenderer`: Globalna instancja klasy `AdaptiveRenderer`.
# # Zaleznosci i powiazania

-   Plik wlacza `<list>` do przechowywania czas�w klatek.
-   Klasa jest uzywana przez silnik renderujacy (np. w `client/mapview.cpp` - niezalaczony, ale mozna sie domyslac), aby dynamicznie ograniczac liczbe rysowanych obiekt�w.

---
# ?? application.cpp
# # Opis og�lny

Plik `application.cpp` zawiera implementacje klasy `Application`, kt�ra jest bazowa klasa dla calej aplikacji. Odpowiada za podstawowy cykl zycia programu, w tym inicjalizacje, de-inicjalizacje, obsluge sygnal�w systemowych oraz zarzadzanie gl�wnymi komponentami frameworka, takimi jak menedzer zasob�w, menedzer modul�w, silnik Lua i polaczenia sieciowe.
# # Funkcje globalne
# # # `exitSignalHandler(int sig)`

Funkcja obslugujaca sygnaly systemowe `SIGTERM` i `SIGINT` (np. zamkniecie terminala lub Ctrl+C). Po otrzymaniu sygnalu, dodaje do kolejki zdarzen wywolanie metody `Application::close()`, co pozwala na bezpieczne zamkniecie aplikacji.

```cpp
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
# # Klasa `Application`
# # # `Application::Application()`

Konstruktor, kt�ry ustawia domyslne wartosci dla nazwy aplikacji, wersji, kodowania znak�w oraz flag stanu. Wykrywa r�wniez, czy aplikacja dziala na platformie mobilnej (Android).
# # # `void Application::init(std::vector<std::string>& args)`
# # # # Opis semantyczny
Metoda inicjalizujaca kluczowe komponenty aplikacji. Jest wywolywana na samym poczatku dzialania programu.
# # # # Dzialanie
1.  Rejestruje `exitSignalHandler` do obslugi sygnal�w zamkniecia.
2.  Ustawia globalne locale.
3.  Przetwarza argumenty wiersza polecen za pomoca `g_platform`.
4.  Inicjalizuje `g_asyncDispatcher` do zadan asynchronicznych.
5.  Zapisuje opcje startowe i sprawdza, czy wlaczono tryb mobilny (`-mobile`).
6.  Inicjalizuje menedzera konfiguracji (`g_configs`).
7.  Inicjalizuje silnik Lua (`g_lua`) i rejestruje funkcje C++ (`registerLuaFunctions`).
8.  Inicjalizuje menedzera proxy (`g_proxy`).
# # # `void Application::deinit()`
# # # # Opis semantyczny
Metoda de-inicjalizujaca, wywolywana przed zamknieciem aplikacji. Dba o poprawne zwolnienie zasob�w w odwrotnej kolejnosci do inicjalizacji.
# # # # Dzialanie
1.  Wywoluje lua `g_app.onTerminate`.
2.  Odladowuje wszystkie moduly.
3.  Uruchamia garbage collector Lua, aby zwolnic referencje do obiekt�w.
4.  Przetwarza pozostale zdarzenia z kolejki.
5.  Wylacza `g_dispatcher`.
# # # `void Application::terminate()`
# # # # Opis semantyczny
Finalny etap zamykania aplikacji. Zwalnia zasoby, kt�re musza byc zwolnione jako ostatnie.
# # # # Dzialanie
1.  Zamyka wszystkie polaczenia sieciowe.
2.  Terminuje menedzera konfiguracji.
3.  Terminuje menedzera zasob�w.
4.  Terminuje silnik Lua.
5.  Terminuje menedzera proxy.
6.  Resetuje obsluge sygnal�w systemowych do domyslnej.
# # # `void Application::poll()`
# # # # Opis semantyczny
Przetwarza zdarzenia sieciowe i zdarzenia z gl�wnej kolejki (`g_dispatcher`). Jest to serce petli zdarzen aplikacji.
# # # `void Application::exit()`

Inicjuje proces zamykania aplikacji poprzez ustawienie flagi `m_stopping` i wywolanie lua `g_app.onExit`.
# # # `void Application::quick_exit()`

Natychmiastowo zamyka aplikacje z kodem 0, bez zwalniania zasob�w.
# # # `void Application::close()`

Pr�buje zamknac aplikacje, wywolujac lua `g_app.onClose`. Jesli skrypt zwr�ci `false` (lub nic), wywolywana jest metoda `exit()`.
# # # `void Application::restart()` i `void Application::restartArgs(const std::vector<std::string>& args)`

Metody do restartowania aplikacji. Uruchamiaja nowa instancje procesu i natychmiast zamykaja biezaca. Uzywaja `boost::process` do stworzenia nowego procesu. Niedostepne na Androidzie i w wersji `FREE_VERSION`.
# # # `std::string Application::getOs()`

Zwraca nazwe biezacego systemu operacyjnego ("android", "windows", "mac", "linux").
# # Zaleznosci i powiazania

-   `framework/core/clock.h`: Do operacji na czasie.
-   `framework/core/resourcemanager.h`, `modulemanager.h`, `eventdispatcher.h`, `configmanager.h`: Gl�wne moduly frameworka, kt�rymi zarzadza.
-   `asyncdispatcher.h`: Do obslugi zadan w tle.
-   `framework/luaengine/luainterface.h`: Do interakcji z Lua.
-   `framework/platform/platform.h`: Do operacji specyficznych dla platformy.
-   `framework/http/http.h`: Do obslugi HTTP.
-   `framework/net/connection.h`: Do zarzadzania polaczeniami sieciowymi.
-   `framework/proxy/proxy.h`: Do zarzadzania proxy.
-   `boost/process.hpp`: Do restartowania aplikacji.

---
# ?? application.h
# # Opis og�lny

Plik `application.h` jest plikiem nagl�wkowym dla klasy `Application`. Deklaruje on interfejs tej klasy, jej skladowe oraz zawiera dyrektywy dolaczajace jedna z dw�ch mozliwych implementacji aplikacji: `GraphicalApplication` lub `ConsoleApplication`, w zaleznosci od tego, czy zdefiniowano flage `FW_GRAPHICS`.
# # Klasa `Application`
# # # Opis semantyczny
`Application` jest abstrakcyjna klasa bazowa, kt�ra definiuje podstawowy interfejs i cykl zycia aplikacji. Zawiera metody do inicjalizacji, de-inicjalizacji, zamykania, restartowania oraz dostarcza informacji o samej aplikacji, takich jak nazwa, wersja czy system operacyjny.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `virtual void init(...)` | Inicjalizuje aplikacje. |
| `virtual void deinit()` | Zwalnia zasoby przed zamknieciem. |
| `virtual void terminate()` | Finalizuje zamykanie aplikacji. |
| `virtual void run() = 0` | Czysto wirtualna metoda, kt�ra musi byc zaimplementowana przez klasy pochodne. Zawiera gl�wna petle programu. |
| `virtual void poll()` | Przetwarza zdarzenia. |
| `virtual void exit()` | Rozpoczyna proces zamykania. |
| `virtual void quick_exit()` | Natychmiastowe zamkniecie programu. |
| `virtual void close()` | Pr�buje zamknac program (moze byc przerwane przez skrypt Lua). |
| `void restart()` | Restartuje aplikacje. |
| `void restartArgs(...)` | Restartuje aplikacje z nowymi argumentami. |
| `void setName(...)` | Ustawia nazwe aplikacji. |
| `void setCompactName(...)` | Ustawia skr�cona nazwe aplikacji. |
| `void setVersion(...)` | Ustawia wersje aplikacji. |
| `bool isRunning()` | Zwraca `true`, jesli aplikacja jest w gl�wnej petli. |
| `bool isStopping()` | Zwraca `true`, jesli trwa proces zamykania. |
| `bool isTerminated()`| Zwraca `true`, jesli aplikacja zostala zakonczona. |
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
| `bool isMobile()` | Zwraca `true`, jesli aplikacja dziala w trybie mobilnym. |
# # # Metody chronione

-   `void registerLuaFunctions()`: Deklaracja metody odpowiedzialnej za bindowanie funkcji C++ do Lua.
# # # Zmienne chronione

-   `m_charset`: Kodowanie znak�w.
-   `m_appName`, `m_appCompactName`, `m_appVersion`: Informacje o aplikacji.
-   `m_startupOptions`: Opcje startowe.
-   `m_running`, `m_stopping`, `m_terminated`, `m_mobile`: Flagi stanu aplikacji.
# # # Dolaczanie implementacji

W zaleznosci od flagi `FW_GRAPHICS`, dolaczany jest jeden z dw�ch plik�w:
-   `graphicalapplication.h`: Jesli `FW_GRAPHICS` jest zdefiniowane, aplikacja bedzie miala interfejs graficzny.
-   `consoleapplication.h`: W przeciwnym razie, bedzie to aplikacja konsolowa.

```cpp
# ifdef FW_GRAPHICS
# include "graphicalapplication.h"
# else
# include "consoleapplication.h"
# endif
```
# # Zaleznosci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje i nagl�wki uzywane w calym projekcie.
-   Klasa jest oznaczona adnotacja `@bindsingleton g_app`, co sugeruje, ze jej instancja bedzie dostepna w Lua pod globalna nazwa `g_app`.

---
# ?? asyncdispatcher.h
# # Opis og�lny

Plik `asyncdispatcher.h` deklaruje klase `AsyncDispatcher`, kt�ra zarzadza pula watk�w roboczych do wykonywania zadan asynchronicznie. Jest to kluczowy komponent do odciazenia gl�wnego watku aplikacji (watku zdarzen) z operacji, kt�re moga zajac duzo czasu, takich jak operacje wejscia/wyjscia na plikach, zapytania sieciowe czy intensywne obliczenia.
# # Klasa `AsyncDispatcher`
# # # Opis semantyczny
`AsyncDispatcher` implementuje prosty model producent-konsument. Zadania (funkcje do wykonania) sa dodawane do kolejki, a watki robocze pobieraja je i wykonuja. Klasa uzywa `std::thread`, `std::mutex` i `std::condition_variable` do synchronizacji.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje dyspozytor i tworzy pierwszy watek roboczy. |
| `void terminate()` | Zatrzymuje wszystkie watki i czysci kolejke zadan. |
| `void spawn_thread()` | Tworzy i uruchamia nowy watek roboczy. |
| `void stop()` | Zatrzymuje dzialanie wszystkich watk�w roboczych. |
| `template<class F> schedule(const F& task)` | Planuje wykonanie zadania i zwraca `std::shared_future`, kt�re pozwoli uzyskac wynik zadania w przyszlosci. Uzywa `std::promise` do przekazania wyniku. |
| `void dispatch(std::function<void()> f)` | Dodaje zadanie do kolejki bez oczekiwania na wynik (fire-and-forget). |
# # # # Przyklad uzycia `schedule`
```cpp
// Watek gl�wny
auto future = g_asyncDispatcher.schedule([]() -> int {
    // Dlugotrwala operacja
    std::this_thread::sleep_for(std::chrono::seconds(2));
    return 42;
});

// P�zniej, w watku gl�wnym
int result = future.get(); // Czeka na zakonczenie zadania i pobiera wynik
```
# # # # Przyklad uzycia `dispatch`
```cpp
// Watek gl�wny
g_asyncDispatcher.dispatch([]() {
    // Operacja w tle, kt�rej wynik nie jest bezposrednio potrzebny
    save_game_state();
});
```
# # # Metody chronione

-   `void exec_loop()`: Gl�wna petla wykonywana przez kazdy watek roboczy. Czeka na zadania w kolejce i wykonuje je.
# # # Zmienne prywatne

-   `m_tasks`: Lista (kolejka) zadan do wykonania.
-   `m_threads`: Lista watk�w roboczych.
-   `m_mutex`: Mutex do ochrony dostepu do `m_tasks`.
-   `m_condition`: Zmienna warunkowa do powiadamiania watk�w o nowych zadaniach.
-   `m_running`: Flaga kontrolujaca, czy watki powinny kontynuowac prace.
# # # Zmienne globalne

-   `g_asyncDispatcher`: Globalna instancja klasy `AsyncDispatcher`.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Podstawowe deklaracje frameworka.
-   `framework/stdext/thread.h`: Zawiera nagl�wki `<thread>`, `<mutex>`, `<condition_variable>`.
-   Jest uzywany przez inne moduly do wykonywania operacji w tle, np. `ResourceManager` do zapisu zrzut�w ekranu, czy `Http` do zapytan sieciowych (chociaz `Http` uzywa wlasnego `io_service` Boost.Asio, `AsyncDispatcher` moze byc uzywany do przetwarzania wynik�w).

---
# ?? binarytree.cpp
# # Opis og�lny

Plik `binarytree.cpp` zawiera implementacje klas `BinaryTree` i `OutputBinaryTree`. Te klasy sluza do odczytu i zapisu danych w niestandardowym, hierarchicznym formacie binarnym, kt�ry przypomina drzewo. Format ten jest uzywany w kliencie Tibii do przechowywania danych, np. plik�w map (`.otbm`).
# # Klasa `BinaryTree`
# # # `BinaryTree::BinaryTree(const FileStreamPtr& fin)`

Konstruktor, kt�ry przyjmuje wskaznik do strumienia pliku (`FileStream`) i zapamietuje pozycje startowa, od kt�rej zaczyna sie wezel drzewa.
# # # `void BinaryTree::skipNodes()`

Metoda pomocnicza, kt�ra przeskakuje przez zagniezdzone wezly w strumieniu danych, aby szybko przejsc do konca biezacego wezla bez potrzeby jego pelnego parsowania.
# # # `void BinaryTree::unserialize()`
# # # # Opis semantyczny
To kluczowa metoda, kt�ra odczytuje "plaskie" dane (wlasciwosci) biezacego wezla ze strumienia pliku i zapisuje je do wewnetrznego bufora (`m_buffer`). Operacja ta jest wykonywana tylko raz (lazy loading), przy pierwszym dostepie do danych wezla. Deserializacja polega na odczytywaniu bajt�w az do napotkania znacznika konca wezla (`BINARYTREE_NODE_END`), z uwzglednieniem znak�w specjalnych (`BINARYTREE_ESCAPE_CHAR`).
# # # `BinaryTreeVec BinaryTree::getChildren()`

Zwraca wektor wskaznik�w do `BinaryTree`, reprezentujacych wszystkie bezposrednie dzieci biezacego wezla. Przeszukuje strumien w poszukiwaniu znacznik�w poczatku wezla (`BINARYTREE_NODE_START`).
# # # Metody odczytu danych (`getU8`, `getU16`, `getString`, etc.)

Sa to metody do odczytywania konkretnych typ�w danych z wewnetrznego, zdeserializowanego bufora. Kazde wywolanie przesuwa wskaznik odczytu (`m_pos`). Jesli bufor nie zostal jeszcze wypelniony, najpierw wywolywana jest metoda `unserialize()`.
# # Klasa `OutputBinaryTree`
# # # `OutputBinaryTree::OutputBinaryTree(const FileStreamPtr& fin)`

Konstruktor, kt�ry przyjmuje strumien pliku do zapisu i natychmiast rozpoczyna nowy wezel, zapisujac znacznik `BINARYTREE_NODE_START`.
# # # Metody zapisu danych (`addU8`, `addU16`, `addString`, etc.)

Metody te sluza do zapisywania danych do strumienia. Uzywaja metody `write`, aby zapewnic poprawne "uciekanie" (escaping) znak�w specjalnych (`0xFD`, `0xFE`, `0xFF`).
# # # `void OutputBinaryTree::startNode(uint8 node)`

Rozpoczyna nowy, zagniezdzony wezel wewnatrz biezacego wezla.
# # # `void OutputBinaryTree::endNode()`

Konczy biezacy wezel, zapisujac znacznik `BINARYTREE_NODE_END`.
# # # `void OutputBinaryTree::write(const uint8* data, size_t size)`

Prywatna metoda pomocnicza, kt�ra zapisuje surowe dane do strumienia, dodajac znak `BINARYTREE_ESCAPE_CHAR` przed kazdym bajtem, kt�ry jest znakiem specjalnym.
# # Zaleznosci i powiazania

-   `framework/core/binarytree.h`: Plik nagl�wkowy dla tych klas.
-   `framework/core/filestream.h`: Uzywa `FileStream` do operacji na plikach.
-   Format danych, kt�ry obsluguja te klasy, jest specyficzny dla klienta Tibii i jest uzywany m.in. do parsowania plik�w `.otbm` (mapy).

---
# ?? asyncdispatcher.cpp
# # Opis og�lny

Plik `asyncdispatcher.cpp` zawiera implementacje klasy `AsyncDispatcher`, kt�ra zarzadza asynchronicznym wykonywaniem zadan w tle. Jest to realizacja mechanizmu puli watk�w, kt�ry pozwala na odciazenie gl�wnego watku aplikacji.
# # Zmienne globalne
# # # `g_asyncDispatcher`

Globalna instancja klasy `AsyncDispatcher`, zapewniajaca scentralizowany dostep do puli watk�w z dowolnego miejsca w aplikacji.

```cpp
AsyncDispatcher g_asyncDispatcher;
```
# # Klasa `AsyncDispatcher`
# # # `void AsyncDispatcher::init()`
# # # # Opis semantyczny
Inicjalizuje dyspozytor, wywolujac `spawn_thread()` w celu utworzenia i uruchomienia pierwszego watku roboczego.
# # # `void AsyncDispatcher::terminate()`
# # # # Opis semantyczny
Zamyka dyspozytor. Zatrzymuje wszystkie watki robocze i czysci kolejke zadan.
# # # `void AsyncDispatcher::spawn_thread()`
# # # # Opis semantyczny
Tworzy nowy `std::thread`, kt�ry rozpoczyna wykonywanie petli `exec_loop()`. Watek jest dodawany do listy `m_threads`. Ustawia flage `m_running` na `true`.
# # # `void AsyncDispatcher::stop()`
# # # # Opis semantyczny
Bezpiecznie zatrzymuje wszystkie watki robocze. Ustawia flage `m_running` na `false`, powiadamia wszystkie oczekujace watki za pomoca `m_condition.notify_all()`, a nastepnie czeka na ich zakonczenie za pomoca `thread.join()`.
# # # `void AsyncDispatcher::exec_loop()`
# # # # Opis semantyczny
Jest to gl�wna funkcja petli dla kazdego watku roboczego.
# # # # Dzialanie
1.  Watek wchodzi w nieskonczona petle i blokuje mutex `m_mutex`.
2.  Czeka na zmiennej warunkowej `m_condition`, az w kolejce `m_tasks` pojawi sie zadanie lub flaga `m_running` zostanie ustawiona na `false`.
3.  Gdy zostanie obudzony i flaga `m_running` jest `true`, pobiera pierwsze zadanie z kolejki `m_tasks`.
4.  Odblokowuje mutex, aby inne watki mogly dodawac lub pobierac zadania.
5.  Wykonuje pobrane zadanie (`task()`).
6.  Ponownie blokuje mutex i wraca na poczatek petli.
7.  Jesli flaga `m_running` jest `false`, watek konczy dzialanie.
# # Zaleznosci i powiazania

-   `asyncdispatcher.h`: Plik nagl�wkowy dla tej klasy.
-   Klasa intensywnie korzysta z narzedzi wielowatkowosci z biblioteki standardowej C++ (`<thread>`, `<mutex>`, `<condition_variable>`).
-   Jest uzywana przez r�zne moduly, kt�re potrzebuja wykonywac operacje w tle, np. `ResourceManager` do zapisu plik�w, `Http` do przetwarzania pobranych danych.

---
# ?? clock.h
# # Opis og�lny

Plik `clock.h` deklaruje klase `Clock`, kt�ra jest singletonem (`g_clock`) odpowiedzialnym za zarzadzanie czasem w aplikacji. Zapewnia buforowany, sp�jny czas dla jednej klatki oraz dostep do "rzeczywistego" czasu systemowego.
# # Klasa `Clock`
# # # Opis semantyczny
Klasa `Clock` ma dwa gl�wne zadania:
1.  Dostarczac "buforowany" czas, kt�ry jest staly w obrebie jednej iteracji gl�wnej petli. Metoda `update()` jest wywolywana raz na klatke, a metody `micros()`, `millis()`, `seconds()` zwracaja te sama, zapisana wartosc czasu przez cala klatke. Zapewnia to sp�jnosc obliczen zaleznych od czasu.
2.  Dostarczac "rzeczywisty" czas systemowy za pomoca metod `realMicros()` i `realMillis()`, kt�re zawsze odczytuja aktualny czas systemowy.

Wszystkie skladowe przechowujace czas sa typu `std::atomic`, co zapewnia bezpieczenstwo watkowe przy odczycie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Clock()` | Konstruktor, inicjalizuje czas na 0. |
| `void update()` | Aktualizuje buforowany czas (`m_currentMicros`, `m_currentMillis`, `m_currentSeconds`) na podstawie aktualnego czasu systemowego. Powinna byc wywolywana raz na klatke. |
| `ticks_t micros()` | Zwraca buforowany czas w mikrosekundach. |
| `ticks_t millis()` | Zwraca buforowany czas w milisekundach. |
| `float seconds()` | Zwraca buforowany czas w sekundach (jako `float`). |
| `ticks_t realMicros()` | Zwraca aktualny, "rzeczywisty" czas systemowy w mikrosekundach. |
| `ticks_t realMillis()` | Zwraca aktualny, "rzeczywisty" czas systemowy w milisekundach. |
# # # Zmienne prywatne

-   `m_currentMicros`: Atomowy licznik przechowujacy buforowany czas w mikrosekundach.
-   `m_currentMillis`: Atomowy licznik przechowujacy buforowany czas w milisekundach.
-   `m_currentSeconds`: Atomowa zmienna przechowujaca buforowany czas w sekundach.
# # # Zmienne globalne

-   `g_clock`: Globalna instancja klasy `Clock`.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Definicje podstawowych typ�w, w tym `ticks_t`.
-   `framework/stdext/time.h`: Uzywa funkcji `stdext::micros()` i `stdext::millis()` do pobierania czasu systemowego.
-   Klasa jest kluczowa dla calego systemu, szczeg�lnie dla `EventDispatcher` (do planowania zdarzen), animacji i logiki gry. Metoda `update()` jest wywolywana w gl�wnej petli aplikacji (w `GraphicalApplication::run()` i `ConsoleApplication::run()`).

---
# ?? binarytree.h
# # Opis og�lny

Plik `binarytree.h` deklaruje interfejsy dla klas `BinaryTree` i `OutputBinaryTree`. Klasy te sluza do obslugi niestandardowego, hierarchicznego formatu binarnego, uzywanego do serializacji danych w strukturze drzewa. Format ten jest charakterystyczny dla plik�w `.otbm` (OTClient Binary Map).
# # Definicje i Makra
# # # Znaczniki binarne

Zdefiniowano trzy specjalne bajty, kt�re kontroluja strukture drzewa w strumieniu binarnym:
-   `BINARYTREE_ESCAPE_CHAR` (0xFD): Znak "ucieczki", uzywany do kodowania bajt�w, kt�re maja taka sama wartosc jak inne znaki specjalne.
-   `BINARYTREE_NODE_START` (0xFE): Znacznik poczatku nowego wezla (dziecka).
-   `BINARYTREE_NODE_END` (0xFF): Znacznik konca biezacego wezla.
# # Klasa `BinaryTree`
# # # Opis semantyczny
Klasa `BinaryTree` reprezentuje pojedynczy wezel w drzewie danych i sluzy do **odczytu** danych z tego wezla. Dziala na strumieniu `FileStream` i implementuje mechanizm leniwego odczytu (lazy loading) - dane wlasciwosci wezla sa deserializowane do wewnetrznego bufora dopiero przy pierwszej pr�bie dostepu do nich.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumien wejsciowy. |
| `seek(uint pos)` | Ustawia pozycje odczytu w zdeserializowanym buforze. |
| `skip(uint len)` | Przeskakuje o `len` bajt�w w buforze. |
| `tell()` | Zwraca biezaca pozycje odczytu w buforze. |
| `size()` | Zwraca rozmiar zdeserializowanych danych wezla. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby calkowite bez znaku. |
| `getString(uint16 len = 0)` | Odczytuje ciag znak�w (dlugosc podana lub odczytana jako U16). |
| `getPoint()` | Odczytuje obiekt `Point`. |
| `getChildren()` | Zwraca wektor `BinaryTreePtr` zawierajacy wszystkie dzieci biezacego wezla. |
| `canRead()` | Sprawdza, czy mozna jeszcze odczytywac dane z bufora. |
# # Klasa `OutputBinaryTree`
# # # Opis semantyczny
Klasa `OutputBinaryTree` jest odpowiednikiem `BinaryTree` do **zapisu** danych w formacie drzewa binarnego. Umozliwia tworzenie wezl�w i zapisywanie do nich wlasciwosci, dbajac o poprawne formatowanie i "uciekanie" (escaping) znak�w specjalnych.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OutputBinaryTree(const FileStreamPtr& fin)` | Konstruktor, przyjmuje strumien wyjsciowy. |
| `addU8()`, `addU16()`, `addU32()` | Zapisuja liczby calkowite bez znaku. |
| `addString(const std::string& v)` | Zapisuje ciag znak�w (z dlugoscia). |
| `addPos(uint16 x, uint16 y, uint8 z)` | Zapisuje pozycje (x, y, z). |
| `addPoint(const Point& point)` | Zapisuje obiekt `Point`. |
| `startNode(uint8 node)` | Rozpoczyna nowy zagniezdzony wezel z danym typem (atrybutem). |
| `endNode()` | Konczy biezacy wezel. |
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Definicje wskaznik�w, np. `FileStreamPtr`.
-   `framework/util/databuffer.h`: Wewnetrzny bufor w `BinaryTree` jest typu `DataBuffer`.
-   Jest uzywana przez moduly, kt�re musza przetwarzac dane w formacie `.otbm`, np. edytor map lub sam klient do wczytywania mapy gry.

---
# ?? config.cpp
# # Opis og�lny

Plik `config.cpp` zawiera implementacje klasy `Config`, kt�ra jest opakowaniem na dokument OTML (`OTMLDocument`). Sluzy do zarzadzania pojedynczym plikiem konfiguracyjnym, umozliwiajac latwy odczyt, zapis i modyfikacje wartosci w formacie `key-value` oraz bardziej zlozonych struktur zagniezdzonych.
# # Klasa `Config`
# # # `Config::Config()`

Konstruktor. Inicjalizuje pusty dokument OTML (`m_confsDoc`) i zeruje nazwe pliku (`m_fileName`).
# # # `bool Config::load(const std::string& file)`
# # # # Opis semantyczny
Laduje i parsuje plik konfiguracyjny w formacie OTML.
# # # # Dzialanie
1.  Zapamietuje nazwe pliku w `m_fileName`.
2.  Sprawdza, czy plik istnieje za pomoca `g_resources.fileExists`.
3.  Jesli plik istnieje, parsuje go za pomoca `OTMLDocument::parse`.
4.  W przypadku sukcesu, zastepuje wewnetrzny dokument (`m_confsDoc`) nowo sparsowanym.
5.  W przypadku bledu parsowania, loguje blad i zwraca `false`.
# # # `bool Config::unload()`

Zwalnia wewnetrzny dokument OTML i resetuje nazwe pliku. Zwraca `true`, jesli obiekt byl zaladowany.
# # # `bool Config::save()`

Zapisuje biezaca zawartosc dokumentu OTML do pliku, kt�rego nazwa jest przechowywana w `m_fileName`. Uzywa do tego metody `m_confsDoc->save()`.
# # # `void Config::clear()`

Czysci wszystkie wezly z wewnetrznego dokumentu OTML.
# # # `void Config::setValue(const std::string& key, const std::string& value)`

Ustawia wartosc dla danego klucza. Jesli wartosc jest pusta, klucz jest usuwany. W przeciwnym razie tworzony jest nowy wezel OTML (`OTMLNode`) i dodawany do dokumentu. Istniejace wezly o tym samym kluczu sa nadpisywane.
# # # `void Config::setList(const std::string& key, const std::vector<std::string>& list)`

Zapisuje wektor string�w jako liste w dokumencie OTML. Tworzy wezel gl�wny o nazwie `key`, a nastepnie dodaje kazdy element wektora jako jego dziecko bez nazwy.
# # # `bool Config::exists(const std::string& key)`

Sprawdza, czy w dokumencie istnieje wezel o podanym kluczu.
# # # `std::string Config::getValue(const std::string& key)`

Zwraca wartosc stringowa dla podanego klucza. Jesli klucz nie istnieje, zwraca pusty string.
# # # `std::vector<std::string> Config::getList(const std::string& key)`

Odczytuje liste string�w z wezla o podanym kluczu. Zwraca pusty wektor, jesli klucz nie istnieje.
# # # `void Config::remove(const std::string& key)`

Usuwa wezel o podanym kluczu z dokumentu.
# # # `void Config::setNode(const std::string& key, const OTMLNodePtr& node)`

Zastepuje istniejacy wezel nowym wezlem OTML. Najpierw usuwa stary wezel, a nastepnie dodaje sklonowana wersje nowego.
# # # `void Config::mergeNode(const std::string& key, const OTMLNodePtr& node)`

Laczy podany wezel z istniejacym (lub tworzy nowy). Dziala podobnie do `setNode`, ale jest uzywane do dodawania/aktualizowania danych bez usuwania calego wezla.
# # # `OTMLNodePtr Config::getNode(const std::string& key)`

Zwraca wskaznik do wezla OTML o podanym kluczu.
# # # `int Config::getNodeSize(const std::string& key)`

Zwraca liczbe dzieci wezla o podanym kluczu. Zwraca 0, jesli wezel nie istnieje.
# # # `bool Config::isLoaded()`

Zwraca `true`, jesli obiekt `Config` jest powiazany z plikiem i ma zaladowana zawartosc.
# # Zaleznosci i powiazania

-   `framework/core/config.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/core/resourcemanager.h`: Uzywany do sprawdzania istnienia plik�w.
-   `framework/core/configmanager.h`: `ConfigManager` zarzadza instancjami klasy `Config`.
-   `framework/otml/otml.h`: Intensywnie korzysta z `OTMLDocument` i `OTMLNode` do przechowywania i manipulowania danymi konfiguracyjnymi.

---
# ?? configmanager.cpp
# # Opis og�lny

Plik `configmanager.cpp` zawiera implementacje klasy `ConfigManager`, kt�ra jest singletonem (`g_configs`) sluzacym do zarzadzania wieloma plikami konfiguracyjnymi (`Config`) w aplikacji. Umozliwia ladowanie, tworzenie, pobieranie i zwalnianie konfiguracji na zadanie.
# # Zmienne globalne
# # # `g_configs`

Globalna instancja `ConfigManager`, zapewniajaca centralny punkt dostepu do wszystkich konfiguracji.

```cpp
ConfigManager g_configs;
```
# # Klasa `ConfigManager`
# # # `void ConfigManager::init()`
# # # # Opis semantyczny
Inicjalizuje menedzera. Tworzy gl�wny obiekt konfiguracyjny, zwany "settings" (`m_settings`), kt�ry jest przeznaczony do przechowywania ustawien samej aplikacji.
# # # `void ConfigManager::terminate()`
# # # # Opis semantyczny
Zwalnia wszystkie zarzadzane obiekty `Config`. Zapewnia, ze gl�wna konfiguracja (`m_settings`) jest zapisywana przed zamknieciem.
# # # # Dzialanie
1.  Zapisuje gl�wny plik ustawien (`m_settings->save()`).
2.  Odladowuje (`unload()`) gl�wny obiekt ustawien.
3.  Iteruje po wszystkich pozostalych zaladowanych konfiguracjach i je odladowuje.
4.  Czysci liste `m_configs`.
# # # `ConfigPtr ConfigManager::getSettings()`

Zwraca wskaznik do gl�wnego obiektu konfiguracyjnego `m_settings`.
# # # `ConfigPtr ConfigManager::get(const std::string& file)`

Wyszukuje i zwraca wskaznik do juz zaladowanego obiektu `Config` na podstawie nazwy pliku. Jesli konfiguracja nie jest zaladowana, zwraca `nullptr`.
# # # `ConfigPtr ConfigManager::loadSettings(const std::string file)`

Laduje gl�wny plik ustawien z podanej sciezki. Zastepuje domyslny, pusty obiekt `m_settings`.
# # # `ConfigPtr ConfigManager::create(const std::string& file)`

Laduje plik konfiguracyjny, a jesli on nie istnieje, tworzy go. Jest to przydatne do tworzenia domyslnych plik�w konfiguracyjnych przy pierwszym uruchomieniu.
# # # # Dzialanie
1.  Pr�buje zaladowac plik za pomoca `load(file)`.
2.  Jesli ladowanie sie nie powiedzie (plik nie istnieje), tworzy nowy obiekt `Config`, laduje go (co tworzy pusty dokument), zapisuje go na dysku (tworzac plik) i dodaje do listy zarzadzanych konfiguracji.
# # # `ConfigPtr ConfigManager::load(const std::string& file)`

Laduje plik konfiguracyjny. Jesli plik byl juz zaladowany, zwraca istniejaca instancje. W przeciwnym razie tworzy nowy obiekt `Config`, pr�buje zaladowac plik z dysku i, jesli sie powiedzie, dodaje go do listy zarzadzanych konfiguracji.
# # # `bool ConfigManager::unload(const std::string& file)`

Znajduje obiekt `Config` po nazwie pliku, odladowuje go (zwalniajac pamiec) i usuwa z listy zarzadzanych konfiguracji.
# # # `void ConfigManager::remove(const ConfigPtr config)`

Usuwa podany obiekt `Config` z listy `m_configs`.
# # Zaleznosci i powiazania

-   `framework/core/configmanager.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/core/config.h`: `ConfigManager` zarzadza obiektami typu `Config`.
-   `framework/core/logger.h`: Uzywany do logowania bled�w, np. gdy nie mozna zaladowac pliku.
-   Jest kluczowym komponentem rdzenia aplikacji, uzywanym przez moduly do odczytu i zapisu swoich konfiguracji.

---
# ?? configmanager.h
# # Opis og�lny

Plik `configmanager.h` deklaruje interfejs klasy `ConfigManager`, kt�ra pelni role centralnego menedzera plik�w konfiguracyjnych w formacie OTML. Umozliwia zarzadzanie cyklem zycia wielu obiekt�w `Config`, w tym ich ladowanie, tworzenie i zwalnianie.
# # Klasa `ConfigManager`
# # # Opis semantyczny
`ConfigManager` to klasa singletonowa (`g_configs`), kt�ra przechowuje liste wszystkich aktywnych obiekt�w `Config`. Wyr�znia jeden specjalny obiekt konfiguracyjny, `m_settings`, przeznaczony na gl�wne ustawienia aplikacji. Pozostale konfiguracje sa zarzadzane w liscie `m_configs` i identyfikowane po nazwie pliku.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedzera, tworzac domyslny obiekt `m_settings`. |
| `void terminate()` | Zwalnia wszystkie zaladowane konfiguracje, zapisujac wczesniej `m_settings`. |
| `ConfigPtr getSettings()` | Zwraca wskaznik do gl�wnego obiektu ustawien aplikacji. |
| `ConfigPtr get(const std::string& file)` | Wyszukuje i zwraca wskaznik do zaladowanej konfiguracji o podanej nazwie pliku. |
| `ConfigPtr create(const std::string& file)` | Laduje konfiguracje z pliku lub tworzy nowy, pusty plik, jesli nie istnieje. |
| `ConfigPtr loadSettings(const std::string file)` | Laduje gl�wny plik ustawien aplikacji z podanej sciezki. |
| `ConfigPtr load(const std::string& file)` | Laduje dodatkowy plik konfiguracyjny. |
| `bool unload(const std::string& file)` | Zwalnia i usuwa z menedzera konfiguracje o podanej nazwie pliku. |
| `void remove(const ConfigPtr config)` | Usuwa podany obiekt `Config` z wewnetrznej listy. |
# # # Zmienne chronione

-   `m_settings`: Wskaznik na gl�wny obiekt `Config` przechowujacy ustawienia aplikacji.
# # # Zmienne prywatne

-   `m_configs`: Lista wskaznik�w na wszystkie dodatkowe zaladowane obiekty `Config`.
# # # Zmienne globalne

-   `g_configs`: Globalna instancja singletonu `ConfigManager`.
# # Zaleznosci i powiazania

-   `framework/core/config.h`: Deklaracja klasy `Config`, kt�ra zarzadza `ConfigManager`.
-   Jest oznaczona adnotacja `@bindsingleton g_configs`, co oznacza, ze jej funkcjonalnosc jest dostepna w skryptach Lua pod globalna nazwa `g_configs`.
-   Wsp�lpracuje z `Application` (kt�ra wywoluje `init` i `terminate`) oraz z modulami, kt�re potrzebuja dostepu do swoich plik�w konfiguracyjnych.

---
# ?? config.h
# # Opis og�lny

Plik `config.h` deklaruje klase `Config`, kt�ra jest obiektowym interfejsem do odczytu, zapisu i manipulacji danymi w plikach konfiguracyjnych formatu OTML. Klasa ta dziedziczy po `LuaObject`, co oznacza, ze jej instancje moga byc tworzone i uzywane w skryptach Lua.
# # Klasa `Config`
# # # Opis semantyczny
`Config` dziala jako opakowanie (wrapper) na `OTMLDocument`. Kazda instancja tej klasy reprezentuje jeden plik konfiguracyjny. Umozliwia operacje takie jak ustawianie wartosci (`setValue`), list (`setList`), a takze bardziej zlozonych struktur (`setNode`, `mergeNode`). Wszystkie dane sa przechowywane wewnetrznie jako drzewo wezl�w OTML.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Config()` | Konstruktor domyslny. |
| `bool load(const std::string& file)` | Laduje i parsuje konfiguracje z pliku OTML. |
| `bool unload()` | Zwalnia zaladowana konfiguracje. |
| `bool save()` | Zapisuje biezacy stan konfiguracji do pliku. |
| `void clear()` | Usuwa wszystkie dane z konfiguracji. |
| `void setValue(...)` | Ustawia wartosc dla danego klucza. |
| `void setList(...)` | Ustawia liste wartosci dla danego klucza. |
| `std::string getValue(...)` | Odczytuje wartosc dla danego klucza. |
| `std::vector<std::string> getList(...)` | Odczytuje liste wartosci dla danego klucza. |
| `void setNode(...)` | Zastepuje wezel o danym kluczu nowym wezlem OTML. |
| `void mergeNode(...)` | Laczy (merge) podany wezel z istniejacym wezlem o danym kluczu. |
| `OTMLNodePtr getNode(...)` | Zwraca wskaznik do wezla OTML o podanym kluczu. |
| `int getNodeSize(...)` | Zwraca liczbe dzieci wezla o danym kluczu. |
| `bool exists(const std::string& key)` | Sprawdza, czy klucz istnieje. |
| `void remove(const std::string& key)` | Usuwa klucz i jego wartosc. |
| `std::string getFileName()` | Zwraca nazwe pliku powiazanego z ta konfiguracja. |
| `bool isLoaded()` | Zwraca `true`, jesli konfiguracja zostala zaladowana z pliku. |
| `ConfigPtr asConfig()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
# # # Zmienne prywatne

-   `m_fileName`: Nazwa pliku konfiguracyjnego.
-   `m_confsDoc`: Wskaznik na `OTMLDocument`, kt�ry przechowuje dane konfiguracyjne.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Deklaracje typ�w, w tym `ConfigPtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`, aby byc dostepna w Lua.
-   `framework/otml/declarations.h`: Uzywa `OTMLDocumentPtr` i `OTMLNodePtr` do przechowywania danych.
-   Jest oznaczona jako `@bindclass`, co oznacza, ze metody tej klasy sa dostepne do wywolania z poziomu skrypt�w Lua na instancjach obiekt�w `Config`.
-   Instancje tej klasy sa tworzone i zarzadzane przez `ConfigManager`.

---
# ?? clock.cpp
# # Opis og�lny

Plik `clock.cpp` zawiera implementacje metod klasy `Clock`. Odpowiada za dostarczanie mechanizm�w pomiaru czasu, kt�re sa kluczowe dla petli gl�wnej aplikacji, planowania zdarzen i animacji.
# # Zmienne globalne
# # # `g_clock`

Globalna instancja klasy `Clock`, kt�ra jest uzywana w calym frameworku do uzyskiwania sp�jnych informacji o czasie.

```cpp
Clock g_clock;
```
# # Klasa `Clock`
# # # `Clock::Clock()`

Konstruktor klasy. Inicjalizuje wszystkie liczniki czasu na 0.
# # # `void Clock::update()`
# # # # Opis semantyczny
Aktualizuje wewnetrzne, "buforowane" liczniki czasu. Ta metoda powinna byc wywolywana raz na kazda iteracje gl�wnej petli aplikacji. Dzieki temu wszystkie operacje wewnatrz jednej klatki (np. logika gry, animacje, fizyka) bazuja na tej samej wartosci czasu, co zapobiega niesp�jnosciom.
# # # # Dzialanie
1.  Pobiera aktualny czas systemowy w mikrosekundach za pomoca `stdext::micros()`.
2.  Zapisuje te wartosc do atomowej zmiennej `m_currentMicros`.
3.  Oblicza i zapisuje czas w milisekundach (`m_currentMillis`) i sekundach (`m_currentSeconds`).
# # # `ticks_t Clock::realMicros()`

Zwraca "na zywo" aktualny czas systemowy w mikrosekundach. W przeciwienstwie do `micros()`, ta metoda nie korzysta z buforowanej wartosci i przy kazdym wywolaniu odpytuje system operacyjny.
# # # `ticks_t Clock::realMillis()`

Zwraca "na zywo" aktualny czas systemowy w milisekundach. Podobnie jak `realMicros()`, odczytuje aktualny czas.
# # Zaleznosci i powiazania

-   `framework/core/clock.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/stdext/time.h`: Uzywa funkcji `stdext::micros()` i `stdext::millis()`, kt�re sa opakowaniem na `std::chrono` do pobierania czasu o wysokiej precyzji.
-   Jest uzywana przez `EventDispatcher` do planowania zdarzen, `GraphicalApplication` do synchronizacji petli renderowania oraz przez wiele innych komponent�w do mierzenia czasu trwania operacji.

---
# ?? consoleapplication.h
# # Opis og�lny

Plik `consoleapplication.h` deklaruje klase `ConsoleApplication`, kt�ra jest konkretna implementacja klasy `Application` dla aplikacji dzialajacej w trybie konsolowym, bez interfejsu graficznego. Jest uzywana, gdy flaga `FW_GRAPHICS` nie jest zdefiniowana podczas kompilacji.
# # Klasa `ConsoleApplication`
# # # Opis semantyczny
`ConsoleApplication` dziedziczy po `Application` i implementuje jej czysto wirtualna metode `run()`. Ta implementacja zawiera prosta petle gl�wna, kt�ra przetwarza zdarzenia i usypia watek na kr�tki czas, aby uniknac 100% uzycia procesora.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void run()` | Implementuje gl�wna petle aplikacji konsolowej. |
# # # Zmienne globalne

-   `g_app`: Globalna instancja `ConsoleApplication`, kt�ra staje sie gl�wnym obiektem aplikacji, gdy kompilacja odbywa sie bez wsparcia dla grafiki.
# # Zaleznosci i powiazania

-   `framework/core/application.h`: Klasa bazowa, z kt�rej dziedziczy `ConsoleApplication`.
-   Jest to jedna z dw�ch mozliwych implementacji aplikacji, wybierana w `application.h` za pomoca dyrektyw preprocesora.

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `core` jest plikiem nagl�wkowym sluzacym do wczesnych deklaracji (forward declarations) klas i definicji typ�w wskaznik�w (`typedef`) dla rdzennych komponent�w frameworka. Jego celem jest rozwiazanie problemu zaleznosci cyklicznych miedzy plikami nagl�wkowymi oraz zmniejszenie ilosci dolaczanych nagl�wk�w w plikach, kt�re potrzebuja jedynie znac istnienie danego typu, a nie jego pelna definicje.
# # Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastepujacych klas, nie definiujac ich zawartosci:

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
# # Definicje typ�w (Typedefs)

Na podstawie wczesnych deklaracji, plik definiuje typy inteligentnych wskaznik�w (`shared_object_ptr`), kt�re sa uzywane w calym frameworku. Upraszcza to skladnie i zapewnia sp�jnosc.

-   `ModulePtr`: `stdext::shared_object_ptr<Module>`
-   `ConfigPtr`: `stdext::shared_object_ptr<Config>`
-   `EventPtr`: `stdext::shared_object_ptr<Event>`
-   `ScheduledEventPtr`: `stdext::shared_object_ptr<ScheduledEvent>`
-   `FileStreamPtr`: `stdext::shared_object_ptr<FileStream>`
-   `BinaryTreePtr`: `stdext::shared_object_ptr<BinaryTree>`
-   `OutputBinaryTreePtr`: `stdext::shared_object_ptr<OutputBinaryTree>`
-   `BinaryTreeVec`: `std::vector<BinaryTreePtr>`
# # Zaleznosci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   Ten plik jest dolaczany przez wiele innych plik�w nagl�wkowych w module `core` i poza nim, aby umozliwic deklarowanie zmiennych i parametr�w funkcji bez koniecznosci dolaczania pelnych definicji klas.

---
# ?? event.cpp
# # Opis og�lny

Plik `event.cpp` zawiera implementacje klasy `Event`, kt�ra jest podstawowym obiektem reprezentujacym jednorazowe, op�znione lub cykliczne zdarzenie w systemie.
# # Klasa `Event`
# # # `Event::Event(const std::string& function, const std::function<void()>& callback, bool botSafe)`

Konstruktor, kt�ry inicjalizuje zdarzenie.

-   **Parametry**:
    -   `function`: Nazwa funkcji (lub opis), uzywana do cel�w debugowania i statystyk.
    -   `callback`: Funkcja (lambda lub `std::function`), kt�ra zostanie wykonana.
    -   `botSafe`: Flaga okreslajaca, czy zdarzenie moze byc wywolane przez bota (uzywane do filtrowania w niekt�rych kontekstach).
-   **Dzialanie**: Inicjalizuje flagi `m_canceled` i `m_executed` na `false` oraz przechowuje podane parametry.
# # # `Event::~Event()`

Destruktor. W trybie debugowania, `VALIDATE(m_callback == nullptr)` sprawdza, czy `callback` zostal poprawnie zwolniony, aby zapobiec wyciekom pamieci lub wiszacym referencjom.
# # # `void Event::execute()`
# # # # Opis semantyczny
Wykonuje `callback` powiazany ze zdarzeniem.
# # # # Dzialanie
1.  Sprawdza, czy zdarzenie nie zostalo anulowane (`!m_canceled`) i czy nie zostalo juz wykonane (`!m_executed`).
2.  Jesli warunki sa spelnione i `callback` istnieje, wywoluje go.
3.  Ustawia flage `m_executed` na `true`.
4.  Resetuje `m_callback` do `nullptr`, aby zwolnic wszelkie zasoby (np. obiekty przechwycone przez lambde).
# # # `void Event::cancel()`
# # # # Opis semantyczny
Anuluje zdarzenie, zapobiegajac jego przyszlemu wykonaniu.
# # # # Dzialanie
1.  Ustawia flage `m_canceled` na `true`.
2.  Resetuje `m_callback` do `nullptr`, aby natychmiast zwolnic zasoby.
# # Zaleznosci i powiazania

-   `framework/core/event.h`: Plik nagl�wkowy dla tej klasy.
-   Jest klasa bazowa dla `ScheduledEvent`.
-   Jest zarzadzana przez `EventDispatcher`, kt�ry przechowuje instancje `Event` w kolejce i wywoluje ich metode `execute()`.

---
# ?? event.h
# # Opis og�lny

Plik `event.h` deklaruje klase `Event`, kt�ra jest podstawowa klasa do obslugi zdarzen w systemie opartym na kolejce zdarzen. Reprezentuje pojedyncze zadanie, kt�re ma zostac wykonane w przyszlosci przez `EventDispatcher`.
# # Klasa `Event`
# # # Opis semantyczny
`Event` to obiekt, kt�ry enkapsuluje funkcje zwrotna (`callback`) do wykonania. Dziedziczy po `LuaObject`, co pozwala na przekazywanie go do skrypt�w Lua. Posiada mechanizmy do wykonania, anulowania i sprawdzania jego stanu.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Event(...)` | Konstruktor. |
| `virtual ~Event()` | Destruktor. |
| `virtual void execute()` | Wykonuje `callback`, jesli zdarzenie nie jest anulowane. |
| `void cancel()` | Anuluje zdarzenie, zapobiegajac jego wykonaniu. |
| `bool isCanceled()` | Zwraca `true`, jesli zdarzenie zostalo anulowane. |
| `bool isExecuted()` | Zwraca `true`, jesli zdarzenie zostalo juz wykonane. |
| `bool isBotSafe()` | Zwraca `true`, jesli zdarzenie jest bezpieczne do wykonania w kontekscie bota. |
| `const std::string& getFunction()` | Zwraca nazwe/opis funkcji powiazanej ze zdarzeniem. |
# # # Zmienne chronione

-   `m_function`: `std::string` przechowujaca nazwe funkcji dla cel�w debugowania.
-   `m_callback`: `std::function<void()>` zawierajaca kod do wykonania.
-   `m_canceled`: Flaga wskazujaca, czy zdarzenie zostalo anulowane.
-   `m_executed`: Flaga wskazujaza, czy zdarzenie zostalo wykonane.
-   `m_botSafe`: Flaga bezpieczenstwa.
# # Zaleznosci i powiazania

-   `framework/luaengine/luaobject.h`: Jest klasa pochodna `LuaObject`.
-   Jest uzywana przez `EventDispatcher` do tworzenia i zarzadzania kolejka zdarzen.
-   Jest klasa bazowa dla `ScheduledEvent`.
-   Oznaczona jako `@bindclass`, co oznacza, ze jest dostepna w Lua, a jej metody (`cancel`, `execute` itd.) moga byc wywolywane ze skrypt�w.

---
# ?? eventdispatcher.cpp
# # Opis og�lny

Plik `eventdispatcher.cpp` zawiera implementacje klasy `EventDispatcher`, kt�ra jest sercem systemu zdarzen. Odpowiada za zarzadzanie kolejka zdarzen natychmiastowych oraz kolejka priorytetowa zdarzen zaplanowanych w czasie.
# # Zmienne globalne

-   `g_dispatcher`: Globalna instancja `EventDispatcher` dla gl�wnego watku aplikacji (logika gry, siec).
-   `g_graphicsDispatcher`: Globalna instancja `EventDispatcher` dla watku graficznego.
-   `g_mainThreadId`, `g_graphicsThreadId`, `g_dispatcherThreadId`: Przechowuja identyfikatory watk�w w celu weryfikacji, czy dana operacja jest wykonywana w odpowiednim watku.
# # Klasa `EventDispatcher`
# # # `void EventDispatcher::shutdown()`
# # # # Opis semantyczny
Zamyka dyspozytor, przetwarzajac wszystkie pozostale zdarzenia i anulujac zaplanowane.
# # # # Dzialanie
1.  Przetwarza wszystkie zdarzenia z `m_eventList` za pomoca `poll()`.
2.  Iteruje po wszystkich zdarzeniach w `m_scheduledEventList`, anuluje je i usuwa z kolejki.
3.  Ustawia flage `m_disabled` na `true`, aby zapobiec dodawaniu nowych zdarzen.
# # # `void EventDispatcher::poll()`
# # # # Opis semantyczny
Gl�wna metoda przetwarzajaca zdarzenia. Wywolywana regularnie w petli aplikacji.
# # # # Dzialanie
1.  **Przetwarzanie zdarzen zaplanowanych (`m_scheduledEventList`)**:
    -   Sprawdza kolejke priorytetowa i wykonuje wszystkie zdarzenia, dla kt�rych minal czas (`remainingTicks() <= 0`).
    -   Jesli zdarzenie jest cykliczne (`nextCycle()` zwraca `true`), jest ponownie dodawane do kolejki z nowym czasem wykonania.
2.  **Przetwarzanie zdarzen natychmiastowych (`m_eventList`)**:
    -   Wchodzi w petle, kt�ra wykonuje wszystkie zdarzenia z `m_eventList`.
    -   Petla jest powtarzana, jesli w trakcie wykonywania zdarzen zostaly dodane nowe (np. zdarzenie A dodaje zdarzenie B), aby zapewnic, ze wszystkie zdarzenia zwiazane z biezaca klatka zostana wykonane przed jej zakonczeniem.
    -   Posiada zabezpieczenie przed nieskonczona petla (jesli zdarzenia ciagle dodaja nowe zdarzenia).
3.  Zapisuje statystyki dotyczace liczby przetworzonych zdarzen.
# # # `ScheduledEventPtr EventDispatcher::scheduleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe jednorazowe zdarzenie zaplanowane, kt�re zostanie wykonane po uplywie `delay` milisekund.
# # # `ScheduledEventPtr EventDispatcher::cycleEventEx(...)`

Tworzy i dodaje do kolejki priorytetowej nowe cykliczne zdarzenie zaplanowane, kt�re bedzie wykonywane co `delay` milisekund.
# # # `EventPtr EventDispatcher::addEventEx(...)`

Dodaje nowe zdarzenie do kolejki zdarzen natychmiastowych. Jesli `pushFront` jest `true`, zdarzenie jest dodawane na poczatek kolejki, co gwarantuje jego wykonanie w biezacej iteracji petli `poll()`.
# # Zaleznosci i powiazania

-   `framework/core/eventdispatcher.h`: Plik nagl�wkowy.
-   `framework/core/clock.h`: Uzywa `g_clock` do sprawdzania czasu dla zdarzen zaplanowanych.
-   `framework/core/graphicalapplication.h`: Uzywa `g_app.isOnInputEvent()` do oznaczenia, czy zdarzenie zostalo wywolane w trakcie obslugi zdarzenia wejsciowego.
-   `framework/graphics/graph.h`: Zapisuje statystyki do `g_graphs`.
-   `framework/util/stats.h`: Uzywa `AutoStat` do profilowania.
-   `framework/core/timer.h`: Uzywany do zabezpieczenia przed nieskonczonymi petlami.
-   Jest kluczowym komponentem, uzywanym przez niemal kazda czesc aplikacji do planowania i wykonywania operacji w spos�b asynchroniczny (wzgledem gl�wnej petli).

---
# ?? eventdispatcher.h
# # Opis og�lny

Plik `eventdispatcher.h` deklaruje interfejs klasy `EventDispatcher` oraz powiazane z nia globalne instancje i makra. Definiuje on publiczne API do zarzadzania kolejka zdarzen w aplikacji.
# # Definicje i Makra
# # # Makra pomocnicze do dodawania zdarzen

Upraszczaja one wywolania metod `...Ex`, automatycznie dodajac nazwe biezacej funkcji (`__FUNCTION__`) jako opis zdarzenia dla cel�w debugowania.

-   `addEvent(...)`: Opakowanie na `addEventEx(__FUNCTION__, ...)`
-   `scheduleEvent(...)`: Opakowanie na `scheduleEventEx(__FUNCTION__, ...)`
-   `cycleEvent(...)`: Opakowanie na `cycleEventEx(__FUNCTION__, ...)`
# # # Makra do walidacji watk�w

Sluza do sprawdzania, czy dana funkcja jest wywolywana w odpowiednim watku, co jest kluczowe dla bezpieczenstwa w srodowisku wielowatkowym.

-   `VALIDATE_GRAPHICS_THREAD()`: Sprawdza, czy biezacy watek to watek graficzny.
-   `VALIDATE_DISPATCHER_THREAD()`: Sprawdza, czy biezacy watek to watek dyspozytora (gl�wny watek logiki).
# # Klasa `EventDispatcher`
# # # Opis semantyczny
`EventDispatcher` jest centralnym mechanizmem do zarzadzania i wykonywania zadan w spos�b asynchroniczny, ale w ramach jednego, okreslonego watku. Posiada dwie kolejki: jedna dla zdarzen natychmiastowych i druga (priorytetowa) dla zdarzen zaplanowanych w czasie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void shutdown()` | Zamyka dyspozytor, czyszczac i anulujac wszystkie zdarzenia. |
| `void poll()` | Przetwarza zdarzenia, kt�re sa gotowe do wykonania. |
| `EventPtr addEventEx(...)` | Dodaje zdarzenie do wykonania w nastepnej iteracji petli `poll()`. |
| `ScheduledEventPtr scheduleEventEx(...)` | Planuje jednorazowe wykonanie zdarzenia po okreslonym czasie. |
| `ScheduledEventPtr cycleEventEx(...)` | Planuje cykliczne wykonywanie zdarzenia co okreslony czas. |
| `bool isBotSafe()` | Zwraca, czy aktualnie wykonywane zdarzenie jest oznaczone jako "bezpieczne dla bota". |
# # # Zmienne prywatne

-   `m_eventList`: Lista (`std::list`) zdarzen do natychmiastowego wykonania.
-   `m_pollEventsSize`: Rozmiar `m_eventList` na poczatku petli `poll()`, aby obsluzyc zdarzenia dodane w trakcie.
-   `m_disabled`: Flaga blokujaca dodawanie nowych zdarzen po wywolaniu `shutdown()`.
-   `m_botSafe`: Flaga stanu dla aktualnie wykonywanego zdarzenia.
-   `m_mutex`: Mutex rekurencyjny do ochrony kolejek.
-   `m_scheduledEventList`: Kolejka priorytetowa (`std::priority_queue`) dla zdarzen zaplanowanych w czasie.
# # # Zmienne globalne

-   `g_dispatcher`: Globalny dyspozytor dla gl�wnego watku.
-   `g_graphicsDispatcher`: Globalny dyspozytor dla watku graficznego.
-   `g_mainThreadId`, `g_dispatcherThreadId`, `g_graphicsThreadId`: Identyfikatory watk�w.
# # Zaleznosci i powiazania

-   `framework/core/clock.h`: Wymagany do obslugi czasu.
-   `framework/core/scheduledevent.h`: Definicja `ScheduledEvent` i komparatora `lessScheduledEvent`.
-   `<queue>`: Uzywany do implementacji kolejki priorytetowej.

---
# ?? filestream.cpp
# # Opis og�lny

Plik `filestream.cpp` zawiera implementacje klasy `FileStream`, kt�ra jest opakowaniem (wrapperem) na operacje plikowe, gl�wnie z wykorzystaniem biblioteki **PhysFS**. Umozliwia zar�wno odczyt z plik�w na dysku, jak i z danych w pamieci (np. z wbudowanego archiwum lub zdekompresowanych danych).
# # Klasa `FileStream`
# # # Konstruktory

-   **`FileStream::FileStream(const std::string& name, PHYSFS_File *fileHandle, bool writeable)`**: Tworzy strumien na podstawie otwartego uchwytu pliku PhysFS.
-   **`FileStream::FileStream(const std::string& name, std::string&& buffer)`**: Tworzy strumien na podstawie bufora danych w pamieci (`std::string`). Pr�buje r�wniez zdekompresowac bufor, jesli jest on w formacie GZIP.
# # # `bool FileStream::initFromGzip(const std::string& buffer)`

Prywatna metoda pomocnicza, kt�ra sprawdza, czy bufor danych jest skompresowany za pomoca GZIP (na podstawie "magicznych bajt�w"). Jesli tak, dekompresuje go za pomoca biblioteki ZLIB i zapisuje wynik do wewnetrznego bufora `m_data`.
# # # `FileStream::~FileStream()` i `void FileStream::close()`

Destruktor i metoda `close()` zwalniaja zasoby. Jesli strumien byl otwarty z pliku PhysFS, zamyka uchwyt `m_fileHandle`. Czysci r�wniez wewnetrzne bufory danych (`m_data`, `m_strData`).
# # # `void FileStream::flush()`

W przypadku strumienia do zapisu, zapisuje zawartosc bufora `m_data` na dysk za pomoca `PHYSFS_writeBytes`.
# # # `int FileStream::read(void* buffer, uint32 size, uint32 nmemb)`

Odczytuje dane ze strumienia. Jesli strumien jest oparty na pliku, uzywa `PHYSFS_readBytes`. Jesli na buforze w pamieci, kopiuje dane z `m_strData` lub `m_data` i przesuwa wskaznik odczytu `m_pos`.
# # # `void FileStream::write(const void *buffer, uint32 count)`

Zapisuje dane do strumienia. Dla plik�w uzywa `PHYSFS_writeBytes`, a dla bufor�w w pamieci dodaje dane do `m_data`.
# # # `seek`, `skip`, `size`, `tell`, `eof`

Implementacje standardowych operacji na strumieniach, kt�re deleguja wywolania do odpowiednich funkcji PhysFS lub operuja na wewnetrznym wskazniku `m_pos` i rozmiarze bufora.
# # # Metody odczytu typ�w (`getU8`, `getU16`, `getString`, etc.)

Metody te sluza do odczytywania konkretnych typ�w danych ze strumienia. Dzialaja zar�wno na plikach PhysFS, jak i na buforach w pamieci. Wykonuja konwersje z porzadku bajt�w Little Endian.
# # # `BinaryTreePtr FileStream::getBinaryTree()`

Rozpoczyna odczyt zagniezdzonej struktury `BinaryTree` ze strumienia, sprawdzajac najpierw znacznik poczatku wezla.
# # # Metody zapisu typ�w (`addU8`, `addU16`, `addString`, etc.)

Sluza do zapisywania danych do strumienia.
# # # `void FileStream::throwError(...)`

Metoda pomocnicza do generowania wyjatk�w z dodatkowymi informacjami o nazwie pliku i bledzie PhysFS.
# # Zaleznosci i powiazania

-   `framework/core/filestream.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/core/binarytree.h`: Uzywana do odczytu i zapisu struktur `BinaryTree`.
-   `framework/core/application.h`: Uzywana do sprawdzania, czy aplikacja jest w trakcie zamykania.
-   **PhysFS**: Kluczowa zaleznosc do operacji na plikach w wirtualnym systemie plik�w.
-   **ZLIB**: Uzywana do dekompresji GZIP.
-   Jest tworzona i zarzadzana przez `ResourceManager` i uzywana w calym projekcie do odczytu zasob�w.

---
# ?? filestream.h
# # Opis og�lny

Plik `filestream.h` deklaruje klase `FileStream`, kt�ra jest kluczowym elementem systemu zarzadzania zasobami. Stanowi ona abstrakcje nad strumieniem danych, kt�ry moze pochodzic z pliku na dysku (obslugiwanego przez PhysFS) lub bezposrednio z bufora w pamieci. Klasa dziedziczy po `LuaObject`, dzieki czemu moze byc uzywana w skryptach Lua.
# # Klasa `FileStream`
# # # Opis semantyczny
`FileStream` dostarcza interfejs podobny do standardowych strumieni plik�w, umozliwiajac sekwencyjny odczyt i zapis r�znych typ�w danych (liczby calkowite, stringi, dane binarne). Jest to podstawowe narzedzie do parsowania plik�w binarnych i tekstowych w calym projekcie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FileStream(...)` | Konstruktory tworzace strumien z uchwytu pliku PhysFS lub z bufora w pamieci. |
| `~FileStream()` | Destruktor. |
| `close()` | Zamyka strumien i zwalnia zasoby. |
| `flush()` | Wymusza zapis buforowanych danych do pliku (dla strumieni do zapisu). |
| `write(...)` | Zapisuje blok danych do strumienia. |
| `read(...)` | Odczytuje blok danych ze strumienia. |
| `seek(uint pos)` | Ustawia pozycje wskaznika w strumieniu. |
| `skip(uint len)` | Przesuwa wskaznik o `len` bajt�w. |
| `size()` | Zwraca calkowity rozmiar strumienia. |
| `tell()` | Zwraca biezaca pozycje wskaznika. |
| `eof()` | Zwraca `true`, jesli osiagnieto koniec strumienia. |
| `name()` | Zwraca nazwe/zr�dlo strumienia. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby calkowite bez znaku. |
| `get8()`, `get16()`, `get32()`, `get64()` | Odczytuja liczby calkowite ze znakiem. |
| `getString()` | Odczytuje string (poprzedzony 2-bajtowa dlugoscia). |
| `getBinaryTree()` | Odczytuje i zwraca obiekt `BinaryTree`. |
| `startNode(uint8 n)` | Rozpoczyna zapis nowego wezla w formacie `BinaryTree`. |
| `endNode()` | Konczy zapis wezla. |
| `addU8()`, ..., `addString()` | Zapisuja r�zne typy danych do strumienia. |
| `asFileStream()` | Zwraca `shared_ptr` do siebie (`static_self_cast`). |
# # # Zmienne prywatne

-   `m_name`: Nazwa pliku lub zr�dla danych.
-   `m_fileHandle`: Wskaznik na uchwyt pliku PhysFS (jesli dotyczy).
-   `m_pos`: Biezaca pozycja odczytu/zapisu w buforze pamieci.
-   `m_writeable`: Flaga wskazujaca, czy strumien jest otwarty do zapisu.
-   `m_caching`: Flaga wskazujaca, czy strumien operuje na buforze w pamieci.
-   `m_data`: Bufor danych (`DataBuffer<uint8_t>`) dla strumieni w pamieci.
-   `m_strData`: Bufor danych (`std::string`) dla strumieni w pamieci.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Definicje typ�w, np. `BinaryTreePtr`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `framework/util/databuffer.h`: Uzywa `DataBuffer` do przechowywania danych.
-   `framework/util/point.h`: Do zapisu i odczytu obiekt�w `Point`.
-   `physfs.h`: Wymagany do deklaracji `PHYSFS_File`.
-   Klasa jest oznaczona jako `@bindclass`, co oznacza, ze jest dostepna w Lua. Jest to kluczowe dla modul�w, kt�re musza parsowac niestandardowe formaty plik�w ze skrypt�w.

---
# ?? graphicalapplication.cpp
# # Opis og�lny

Plik `graphicalapplication.cpp` zawiera implementacje klasy `GraphicalApplication`, kt�ra jest konkretna implementacja `Application` dla aplikacji z interfejsem graficznym. Odpowiada za inicjalizacje, zarzadzanie i zamykanie wszystkich podsystem�w graficznych, a takze za implementacje gl�wnej petli renderowania i logiki.
# # Zmienne globalne
# # # `g_app`

Globalna instancja `GraphicalApplication`, kt�ra jest gl�wnym obiektem aplikacji, gdy kompilacja odbywa sie z flaga `FW_GRAPHICS`.

```cpp
GraphicalApplication g_app;
```
# # Klasa `GraphicalApplication`
# # # `void GraphicalApplication::init(std::vector<std::string>& args)`
# # # # Opis semantyczny
Inicjalizuje aplikacje graficzna. Wywoluje najpierw `Application::init()`, a nastepnie inicjalizuje wszystkie komponenty zwiazane z grafika.
# # # # Dzialanie
1.  Wywoluje `Application::init(args)`.
2.  Inicjalizuje okno platformy (`g_window.init()`).
3.  Ustawia callbacki dla okna: `onResize`, `onInputEvent`, `onClose`.
4.  Inicjalizuje menedzera myszy (`g_mouse.init()`).
5.  Inicjalizuje menedzera UI (`g_ui.init()`).
6.  Inicjalizuje silnik graficzny (`g_graphics.init()`).
7.  Wywoluje pierwsze zdarzenie zmiany rozmiaru.
8.  Inicjalizuje menedzera dzwieku (`g_sounds.init()`), jesli `FW_SOUND` jest zdefiniowane.
# # # `void GraphicalApplication::deinit()`

Deinicjalizuje aplikacje w odwrotnej kolejnosci, ukrywajac okno i zwalniajac zasoby.
# # # `void GraphicalApplication::terminate()`

Finalizuje zamykanie podsystem�w graficznych, w tym `g_ui`, `g_sounds`, `g_mouse` i `g_graphics`.
# # # `void GraphicalApplication::run()`
# # # # Opis semantyczny
Implementuje gl�wna petle aplikacji, kt�ra jest podzielona na dwa r�wnolegle watki:
1.  **Watek logiki (`worker`)**: Odpowiada za aktualizacje stanu gry, przetwarzanie zdarzen i przygotowywanie kolejek rysowania (`DrawQueue`).
2.  **Watek renderowania (gl�wny watek)**: Odpowiada za przetwarzanie zdarzen okna, renderowanie zawartosci przygotowanych kolejek na ekranie i synchronizacje klatek.
# # # # Dzialanie watku logiki (`worker`)
-   W nieskonczonej petli:
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Przetwarza zdarzenia (`poll()`).
    -   Czeka, jesli poprzednia klatka nie zostala jeszcze wyrenderowana.
    -   Renderuje UI do trzech osobnych kolejek: `MapBackgroundPane`, `MapForegroundPane`, `ForegroundPane`.
    -   Przekazuje gotowe kolejki do watku renderowania za pomoca mutexu.
    -   Usypia na 1ms, jesli `m_maxFps > 0` lub wlaczona jest synchronizacja pionowa.
# # # # Dzialanie watku renderowania (gl�wnego)
-   W nieskonczonej petli:
    -   Aktualizuje zegar i przetwarza zdarzenia graficzne (`pollGraphics()`).
    -   Czeka na gotowe kolejki rysowania z watku logiki.
    -   Aktualizuje `AdaptiveRenderer`.
    -   Synchronizuje klatki zgodnie z `m_maxFps`.
    -   Ustawia `FrameBuffer` do renderowania poza ekranem, jesli skalowanie jest wlaczone.
    -   Renderuje tlo mapy do `m_mapFramebuffer`.
    -   Renderuje wlasciwa scene, laczac tlo mapy, pierwszy plan mapy i interfejs uzytkownika.
    -   Jesli wlaczono skalowanie, rysuje zawartosc `m_framebuffer` na ekranie.
    -   Rysuje grafy debugowania.
    -   Zamienia bufory (`g_window.swapBuffers()`).
# # # `void GraphicalApplication::poll()` i `void GraphicalApplication::pollGraphics()`

Metody pomocnicze wywolywane w odpowiednich watkach do przetwarzania zdarzen. `poll()` obsluguje dzwiek i logike, a `pollGraphics()` obsluguje zdarzenia okna i aktualizacje tekst�w.
# # # Inne metody

-   `close()`: Wywolywana przy zamykaniu okna.
-   `resize()`: Wywolywana przy zmianie rozmiaru okna.
-   `inputEvent()`: Przekazuje zdarzenia wejsciowe do `UIManager`.
-   `doScreenshot()`: Robi zrzut ekranu i zapisuje go do pliku asynchronicznie.
-   `scaleUp()`, `scaleDown()`, `scale()`: Zarzadzaja skalowaniem interfejsu.
-   `setSmooth()`: Wlacza/wylacza wygladzanie dla `m_mapFramebuffer`.
-   `doMapScreenshot()`: Robi zrzut ekranu samej mapy.
# # Zaleznosci i powiazania

-   Jest to centralna klasa, kt�ra integruje prawie wszystkie moduly graficzne i rdzenia.
-   Zalezy od `Application`, `PlatformWindow`, `UIManager`, `Graphics`, `TextureManager`, `Painter`, `SoundManager` i innych.
-   Uzywa `std::thread` i `std::mutex` do implementacji wielowatkowej petli.

---
# ?? inputevent.h
# # Opis og�lny

Plik `inputevent.h` deklaruje strukture `InputEvent`, kt�ra jest uzywana do przekazywania informacji o zdarzeniach wejsciowych (z klawiatury i myszy) w systemie. Jest to prosta struktura danych, kt�ra agreguje wszystkie mozliwe parametry zdarzenia.
# # Struktura `InputEvent`
# # # Opis semantyczny
Struktura `InputEvent` jest uniwersalnym kontenerem na dane o zdarzeniach. W zaleznosci od pola `type`, inne pola przechowuja odpowiednie informacje. Na przyklad, dla zdarzenia klawiatury (`KeyDownInputEvent`), pole `keyCode` bedzie mialo znaczenie, a dla zdarzenia myszy (`MouseMoveInputEvent`) - `mousePos` i `mouseMoved`.
# # # Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `type` | `Fw::InputEventType` | Typ zdarzenia (np. wcisniecie klawisza, ruch myszy). |
| `wheelDirection` | `Fw::MouseWheelDirection` | Kierunek przewijania k�lkiem myszy (`MouseWheelUp` lub `MouseWheelDown`). |
| `mouseButton` | `Fw::MouseButton` | Przycisk myszy, kt�ry wywolal zdarzenie. |
| `keyCode` | `Fw::Key` | Kod wcisnietego klawisza. |
| `keyText` | `std::string` | Znak tekstowy odpowiadajacy wcisnietemu klawiszowi (dla `KeyTextInputEvent`). |
| `keyboardModifiers`| `int` | Flagi bitowe dla klawiszy modyfikujacych (Ctrl, Alt, Shift). |
| `mousePos` | `Point` | Aktualna pozycja kursora myszy. |
| `mouseMoved` | `Point` | Wektor przesuniecia kursora myszy od ostatniego zdarzenia. |
| `autoRepeatTicks`| `int` | Czas (w milisekundach), przez jaki klawisz jest przytrzymywany (dla `KeyPressInputEvent`). |
# # # Metody

-   **`InputEvent()`**: Konstruktor, inicjalizuje strukture.
-   **`reset(Fw::InputEventType eventType = Fw::NoInputEvent)`**: Resetuje wszystkie pola do wartosci domyslnych i ustawia nowy typ zdarzenia.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Podstawowe deklaracje.
-   Struktura ta jest tworzona w klasie `PlatformWindow` (np. `win32window.cpp`) na podstawie zdarzen systemowych, a nastepnie przekazywana do `GraphicalApplication` i dalej do `UIManager`, kt�ry rozsyla je do odpowiednich widget�w.

---
# ?? graphicalapplication.h
# # Opis og�lny

Plik `graphicalapplication.h` deklaruje klase `GraphicalApplication`, kt�ra jest implementacja `Application` dla aplikacji z interfejsem graficznym. Jest to gl�wna klasa zarzadzajaca petla renderowania, zdarzeniami wejsciowymi i komponentami graficznymi.
# # Klasa `GraphicalApplication`
# # # Opis semantyczny
Dziedziczy po `Application` i implementuje jej metody wirtualne, dodajac funkcjonalnosc specyficzna dla aplikacji graficznej. Odpowiada za koordynacje miedzy oknem (`PlatformWindow`), menedzerem UI (`UIManager`), silnikiem renderujacym (`Painter`) i innymi systemami. Implementuje wielowatkowa petle gl�wna, gdzie logika jest oddzielona od renderowania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init(...)` | Inicjalizuje podsystemy graficzne. |
| `void deinit()` | Zwalnia zasoby graficzne przed zamknieciem. |
| `void terminate()` | Finalizuje zamykanie podsystem�w graficznych. |
| `void run()` | Uruchamia gl�wna, wielowatkowa petle aplikacji. |
| `void poll()` | Przetwarza zdarzenia logiki i dzwieku. |
| `void pollGraphics()` | Przetwarza zdarzenia okna i grafiki. |
| `void close()` | Obsluguje zdarzenie zamkniecia okna. |
| `bool willRepaint()` | Zwraca `true`, jesli zaplanowano przemalowanie ekranu. |
| `void repaint()` | Wymusza przemalowanie ekranu w nastepnej klatce. |
| `void setMaxFps(int maxFps)` | Ustawia maksymalna liczbe klatek na sekunde. |
| `int getMaxFps()` | Zwraca ustawiony limit FPS. |
| `int getFps()` | Zwraca aktualny FPS renderowania. |
| `int getGraphicsFps()` | Zwraca FPS watku graficznego. |
| `int getProcessingFps()` | Zwraca FPS watku logiki. |
| `bool isOnInputEvent()` | Zwraca `true`, jesli aplikacja jest w trakcie przetwarzania zdarzenia wejsciowego. |
| `int getIteration()` | Zwraca licznik iteracji gl�wnej petli. |
| `void doScreenshot(...)` | Robi zrzut calego ekranu. |
| `void scaleUp()` / `scaleDown()` / `scale()` | Zarzadzaja skalowaniem interfejsu. |
| `void setSmooth(bool value)` | Wlacza/wylacza wygladzanie dla bufora ramki mapy. |
| `void doMapScreenshot(...)` | Robi zrzut ekranu samej mapy gry. |
# # # Metody chronione

-   `void resize(const Size& size)`: Obsluguje zdarzenie zmiany rozmiaru okna.
-   `void inputEvent(InputEvent event)`: Otrzymuje i przekazuje zdarzenia wejsciowe.
# # # Zmienne prywatne

-   `m_iteration`: Licznik klatek.
-   `m_scaling`, `m_lastScaling`: Aktualne i poprzednie skalowanie UI.
-   `m_maxFps`: Maksymalny limit FPS.
-   `m_onInputEvent`: Flaga aktywna podczas obslugi zdarzenia wejsciowego.
-   `m_mustRepaint`: Flaga wymuszajaca przemalowanie.
-   `m_framebuffer`, `m_mapFramebuffer`: Bufory ramki do renderowania poza ekranem (off-screen rendering).
-   `m_graphicsFrames`, `m_processingFrames`: Liczniki klatek dla watku graficznego i logiki.
-   `m_windowPollTimer`: Timer do ograniczania czestotliwosci odpytywania okna.
# # # Zmienne globalne

-   `g_app`: Globalna instancja `GraphicalApplication`.
# # Zaleznosci i powiazania

-   `framework/core/application.h`: Klasa bazowa.
-   `framework/graphics/declarations.h`: Deklaracje typ�w graficznych (np. `FrameBufferPtr`).
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/core/adaptiverenderer.h`: Uzywa `AdaptiveRenderer` do dynamicznego dostosowywania wydajnosci.
-   `framework/util/framecounter.h`: Uzywa `FrameCounter` do sledzenia FPS.

---
# ?? logger.h
# # Opis og�lny

Plik `logger.h` deklaruje klase `Logger`, kt�ra implementuje system logowania dla calej aplikacji. Jest to singleton (`g_logger`) zapewniajacy scentralizowany i bezpieczny watkowo mechanizm do zapisywania komunikat�w o r�znym poziomie waznosci (debug, info, warning, error, fatal).
# # Struktura `LogMessage`

Prosta struktura przechowujaca pojedyncza wiadomosc logu.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `level` | `Fw::LogLevel` | Poziom waznosci wiadomosci. |
| `message`| `std::string` | Tresc wiadomosci. |
| `when` | `std::size_t` | Czas (timestamp) utworzenia wiadomosci. |
# # Klasa `Logger`
# # # Opis semantyczny
`Logger` umozliwia logowanie komunikat�w do standardowego wyjscia (konsola), opcjonalnego pliku oraz przekazywanie ich do zarejestrowanego `callbacka` (np. w celu wyswietlenia w interfejsie uzytkownika). Przechowuje r�wniez historie ostatnich `MAX_LOG_HISTORY` wiadomosci.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void log(...)` | Gl�wna metoda logujaca wiadomosc z okreslonym poziomem. |
| `void logFunc(...)` | Loguje wiadomosc wraz z informacja o funkcji, z kt�rej zostala wywolana (`__PRETTY_FUNCTION__`). |
| `void debug(..)` | Skr�t do `log(Fw::LogDebug, ...)`. |
| `void info(...)` | Skr�t do `log(Fw::LogInfo, ...)`. |
| `void warning(...)` | Skr�t do `log(Fw::LogWarning, ...)`. |
| `void error(...)` | Skr�t do `log(Fw::LogError, ...)`. |
| `void fatal(...)` | Skr�t do `log(Fw::LogFatal, ...)`, kt�ry dodatkowo powoduje zamkniecie aplikacji. |
| `void fireOldMessages()` | Wywoluje `callback` `m_onLog` dla wszystkich historycznych wiadomosci. |
| `void setLogFile(...)` | Ustawia plik, do kt�rego beda zapisywane logi. |
| `void setOnLog(...)` | Rejestruje funkcje zwrotna, kt�ra bedzie wywolywana dla kazdej nowej wiadomosci. |
| `std::string getLastLog()` | Zwraca ostatnio zalogowana wiadomosc. |
| `void setTestingMode()` | Ustawia tryb testowy, w kt�rym bledy (`LogError`) dzialaja jak bledy krytyczne (`LogFatal`). |
# # # Zmienne prywatne

-   `m_logMessages`: Lista ostatnich wiadomosci.
-   `m_onLog`: Wskaznik na funkcje zwrotna.
-   `m_outFile`: Strumien pliku do zapisu log�w.
-   `m_mutex`: Mutex rekurencyjny zapewniajacy bezpieczenstwo watkowe.
-   `m_lastLog`: Przechowuje ostatnia wiadomosc.
-   `m_testingMode`: Flaga trybu testowego.
# # # Makra pomocnicze

Plik definiuje makra ulatwiajace logowanie z dodatkowymi informacjami o kontekscie.

-   `trace()`: Loguje nazwe biezacej funkcji.
-   `traceDebug(a)`, `traceInfo(a)`, ...: Loguja wiadomosc `a` wraz z nazwa funkcji i sladem stosu.
-   `logTraceCounter()`: Loguje licznik wywolan co sekunde.
-   `logTraceFrameCounter()`: Loguje licznik wywolan co klatke.
# # # Zmienne globalne

-   `g_logger`: Globalna instancja `Logger`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/stdext/thread.h`: Zawiera `<mutex>` do synchronizacji.
-   `<fstream>`: Do obslugi zapisu do pliku.
-   Jest uzywany w calym projekcie do raportowania stanu, bled�w i informacji debugowania.

---
# ?? module.cpp
# # Opis og�lny

Plik `module.cpp` zawiera implementacje klasy `Module`, kt�ra reprezentuje pojedynczy, ladowalny modul funkcjonalnosci w aplikacji. Moduly sa podstawa architektury wtyczek, pozwalajac na dynamiczne ladowanie, odladowywanie i ponowne ladowanie kodu (gl�wnie skrypt�w Lua) w trakcie dzialania programu.
# # Klasa `Module`
# # # `Module::Module(const std::string& name)`

Konstruktor. Ustawia nazwe modulu i tworzy dla niego nowe, odizolowane srodowisko Lua (piaskownice - sandbox) za pomoca `g_lua.newSandboxEnv()`.
# # # `bool Module::load()`
# # # # Opis semantyczny
Gl�wna metoda ladujaca modul. Jest odpowiedzialna za sprawdzenie i zaladowanie zaleznosci, a nastepnie wykonanie skrypt�w modulu.
# # # # Dzialanie
1.  Sprawdza, czy modul nie jest juz zaladowany.
2.  Definiuje `errorHandler` do obslugi bled�w ladowania.
3.  Dodaje srodowisko modulu do `package.loaded` w Lua, aby `require` dzialalo poprawnie.
4.  Iteruje po zaleznosciach (`m_dependencies`):
    -   Sprawdza, czy modul nie zalezy sam od siebie.
    -   Sprawdza, czy zaleznosc istnieje.
    -   Sprawdza, czy nie ma zaleznosci cyklicznych.
    -   Jesli zaleznosc nie jest zaladowana, pr�buje ja zaladowac.
5.  Jesli modul jest w piaskownicy (`m_sandboxed`), ustawia jego srodowisko jako globalne w Lua.
6.  Wykonuje wszystkie skrypty z listy `m_scripts`.
7.  Wykonuje skrypt z `m_onLoadFunc`, jesli jest zdefiniowany.
8.  Jesli wystapil blad, wywoluje `errorHandler` i zwraca `false`.
9.  Przywraca globalne srodowisko Lua, jesli bylo zmienione.
10. Ustawia flage `m_loaded` na `true` i aktualizuje kolejnosc ladowania modul�w.
11. Laduje moduly z listy `m_loadLaterModules`.
# # # `void Module::unload()`
# # # # Opis semantyczny
Odladowuje modul, wykonujac jego skrypt `onUnload` i czyszczac jego srodowisko Lua.
# # # # Dzialanie
1.  Sprawdza, czy modul jest zaladowany.
2.  Jesli tak, wykonuje skrypt `onUnload` (`m_onUnloadFunc`).
3.  Czysci cala tabele srodowiska Lua modulu, aby zwolnic wszystkie referencje.
4.  Usuwa modul z `package.loaded` w Lua.
5.  Ustawia flage `m_loaded` na `false`.
# # # `bool Module::reload()`

Odladowuje i ponownie laduje modul.
# # # `bool Module::isDependent()`

Sprawdza, czy jakikolwiek inny zaladowany modul zalezy od tego modulu. Jest to uzywane do okreslenia, czy modul mozna bezpiecznie odladowac.
# # # `bool Module::hasDependency(const std::string& name, bool recursive)`

Sprawdza, czy modul ma zaleznosc o podanej nazwie. Opcja `recursive` pozwala na sprawdzanie zaleznosci posrednich.
# # # `int Module::getSandbox(LuaInterface* lua)`

Zwraca na stos Lua tabele srodowiska (piaskownice) tego modulu.
# # # `void Module::discover(const OTMLNodePtr& moduleNode)`

Parsuje wezel OTML (z pliku `.otmod`) i inicjalizuje pola modulu, takie jak opis, autor, wersja, zaleznosci, lista skrypt�w, oraz skrypty `onLoad` i `onUnload`.
# # Zaleznosci i powiazania

-   `framework/core/module.h`: Plik nagl�wkowy.
-   `framework/core/modulemanager.h`: Wsp�lpracuje z `ModuleManager` do zarzadzania zaleznosciami i kolejnoscia ladowania.
-   `framework/core/resourcemanager.h`: Uzywany do rozwiazywania sciezek do skrypt�w.
-   `framework/otml/otml.h`: Uzywa `OTMLNode` do odczytu metadanych modulu.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do zarzadzania srodowiskiem i wykonywania skrypt�w.

---
# ?? modulemanager.cpp
# # Opis og�lny

Plik `modulemanager.cpp` zawiera implementacje klasy `ModuleManager`, kt�ra jest singletonem (`g_modules`) odpowiedzialnym za zarzadzanie wszystkimi modulami w aplikacji. Odpowiada za ich odkrywanie, ladowanie, odladowywanie i ponowne ladowanie, a takze za zarzadzanie zaleznosciami miedzy nimi.
# # Zmienne globalne
# # # `g_modules`

Globalna instancja `ModuleManager`.

```cpp
ModuleManager g_modules;
```
# # Klasa `ModuleManager`
# # # `void ModuleManager::clear()`

Czysci wszystkie dane menedzera, usuwajac liste modul�w i modul�w do automatycznego ladowania.
# # # `void ModuleManager::discoverModules()`
# # # # Opis semantyczny
Przeszukuje wirtualny system plik�w (katalogi `/modules` i `/mods`) w poszukiwaniu plik�w `.otmod`, parsuje je i tworzy obiekty `Module` dla kazdego znalezionego modulu. Moduly oznaczone jako `autoload` sa dodawane do specjalnej listy.
# # # `void ModuleManager::autoLoadModules(int maxPriority)`

Laduje wszystkie moduly z listy `m_autoLoadModules`, kt�rych priorytet jest mniejszy lub r�wny `maxPriority`. Moduly sa ladowane w kolejnosci rosnacego priorytetu.
# # # `ModulePtr ModuleManager::discoverModule(const std::string& moduleFile)`

Parsuje pojedynczy plik `.otmod`, tworzy lub aktualizuje obiekt `Module` i dodaje go do listy `m_modules`.
# # # `void ModuleManager::ensureModuleLoaded(const std::string& moduleName)`

Sprawdza, czy modul o podanej nazwie jest zaladowany. Jesli nie, pr�buje go zaladowac. Jesli ladowanie sie nie powiedzie, aplikacja jest zamykana z bledem krytycznym.
# # # `void ModuleManager::unloadModules()`

Odladowuje wszystkie zaladowane moduly. Uzywa kopii listy modul�w, aby uniknac problem�w z iteratorami podczas usuwania.
# # # `void ModuleManager::reloadModules()`
# # # # Opis semantyczny
Implementuje mechanizm "hot-reloading" modul�w.
# # # # Dzialanie
1.  Tworzy liste modul�w do ponownego zaladowania (`toLoadList`).
2.  W petli (do 10 pr�b) pr�buje odladowac wszystkie moduly, kt�re moga byc odladowane (`canUnload()`). Moduly sa odladowywane w odwrotnej kolejnosci zaleznosci.
3.  Po odladowaniu, laduje ponownie moduly z `toLoadList`.
# # # `ModulePtr ModuleManager::getModule(const std::string& moduleName)`

Wyszukuje i zwraca wskaznik do modulu o podanej nazwie.
# # # `void ModuleManager::updateModuleLoadOrder(ModulePtr module)`

Aktualizuje wewnetrzna liste modul�w (`m_modules`), aby zaladowane moduly znajdowaly sie na jej poczatku. Zapewnia to poprawna kolejnosc odladowywania (odwrotna do ladowania).
# # Zaleznosci i powiazania

-   `framework/core/modulemanager.h`: Plik nagl�wkowy.
-   `framework/core/resourcemanager.h`: Uzywany do przeszukiwania katalog�w z modulami.
-   `framework/otml/otml.h`: Do parsowania plik�w `.otmod`.
-   `framework/core/application.h`: Do obslugi bled�w krytycznych.
-   Jest centralnym elementem architektury wtyczek i scisle wsp�lpracuje z klasa `Module`.

---
# ?? logger.cpp
# # Opis og�lny

Plik `logger.cpp` zawiera implementacje klasy `Logger`, kt�ra jest odpowiedzialna za system logowania w aplikacji. Zapewnia mechanizmy do zapisywania komunikat�w o r�znym poziomie waznosci do konsoli, pliku oraz przekazywania ich do zarejestrowanych funkcji zwrotnych (callback�w).
# # Zmienne globalne
# # # `g_logger`

Globalna, jedyna instancja klasy `Logger`.

```cpp
Logger g_logger;
```
# # Funkcje globalne
# # # `void fatalError(const char* error, const char* file, int line)`

Funkcja wywolywana przez makro `VALIDATE`. Loguje blad krytyczny za pomoca `g_logger.fatal`, zawierajacy komunikat, plik i numer linii, a nastepnie przerywa dzialanie aplikacji.
# # Klasa `Logger`
# # # `void Logger::log(Fw::LogLevel level, const std::string& message)`
# # # # Opis semantyczny
Gl�wna, prywatna metoda logujaca. Jest bezpieczna watkowo dzieki uzyciu `std::recursive_mutex`.
# # # # Dzialanie
1.  Blokuje mutex, aby zapewnic wylaczny dostep.
2.  W trybie `NDEBUG` (wydajnosciowym) ignoruje wiadomosci o poziomie `LogDebug`.
3.  Dodaje odpowiedni prefiks do wiadomosci (np. "WARNING: ", "ERROR: ").
4.  Wypisuje sformatowana wiadomosc na standardowe wyjscie (`std::cout`) lub `__android_log_print` na Androidzie.
5.  Jesli ustawiono plik logu, zapisuje wiadomosc do pliku.
6.  Dodaje wiadomosc do wewnetrznej historii `m_logMessages`.
7.  Jesli zarejestrowano `callback` (`m_onLog`), dodaje zdarzenie do `g_dispatcher`, kt�re wywola ten `callback` w gl�wnym watku.
8.  Jesli poziom to `LogFatal` (lub `LogError` w trybie testowym), wyswietla okno bledu (w wersji graficznej) i natychmiast konczy aplikacje.
# # # `void Logger::logFunc(Fw::LogLevel level, const std::string& message, std::string prettyFunction)`

Metoda pomocnicza, kt�ra wzbogaca wiadomosc o informacje o funkcji, z kt�rej zostala wywolana, oraz o slad stosu (traceback) z Lua i C++. Uzywana przez makra takie jak `traceError`.
# # # `void Logger::fireOldMessages()`

Wywoluje `callback` `m_onLog` dla wszystkich wiadomosci, kt�re zostaly zalogowane przed jego zarejestrowaniem. Przydatne do wyswietlania wczesnych log�w w UI, gdy UI jest juz gotowe.
# # # `void Logger::setLogFile(const std::string& file)`

Otwiera podany plik do zapisu log�w. Przed otwarciem do dopisywania, odczytuje ostatnie 100 KB z istniejacego pliku do `m_lastLog`, aby mozna bylo przejrzec logi z poprzedniej sesji.
# # Zaleznosci i powiazania

-   `framework/core/logger.h`: Plik nagl�wkowy.
-   `framework/core/eventdispatcher.h`: Uzywa `g_dispatcher` do bezpiecznego wywolywania `callback�w` w gl�wnym watku.
-   `framework/core/resourcemanager.h`: Potencjalnie uzywany do rozwiazywania sciezek do plik�w log�w.
-   `framework/core/graphicalapplication.h`: W wersji graficznej, `g_window` jest uzywane do wyswietlania okna bledu krytycznego.
-   `framework/platform/platform.h`: Uzywa `g_platform` do generowania sladu stosu C++.
-   `framework/luaengine/luainterface.h`: Uzywa `g_lua` do generowania sladu stosu Lua.

---
# ?? module.h
# # Opis og�lny

Plik `module.h` deklaruje klase `Module`, kt�ra jest podstawowym elementem systemu modularnosci aplikacji. Kazdy modul reprezentuje logicznie oddzielona czesc funkcjonalnosci (np. interfejs, mini-mapa, bot), kt�ra moze byc dynamicznie ladowana i odladowywana.
# # Klasa `Module`
# # # Opis semantyczny
`Module` enkapsuluje zestaw skrypt�w Lua, metadane (nazwa, autor, wersja), zaleznosci od innych modul�w oraz wlasne, izolowane srodowisko Lua (piaskownice - sandbox). Dziedziczy po `LuaObject`, dzieki czemu moze byc zarzadzany z poziomu skrypt�w Lua.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Module(const std::string& name)` | Konstruktor. |
| `bool load()` | Laduje modul, wykonujac jego skrypty i zaleznosci. |
| `void unload()` | Odladowuje modul, wykonujac skrypt `onUnload`. |
| `bool reload()` | Ponownie laduje modul. |
| `bool canUnload()` | Zwraca `true`, jesli modul jest przeladowywalny i zaden inny modul od niego nie zalezy. |
| `bool canReload()` | Zwraca `true`, jesli modul jest przeladowywalny i nie ma zaleznosci. |
| `bool isLoaded()` | Zwraca `true`, jesli modul jest zaladowany. |
| `bool isReloadable()` | Zwraca `true`, jesli modul mozna przeladowac. |
| `bool isDependent()` | Sprawdza, czy inny zaladowany modul zalezy od tego modulu. |
| `bool isSandboxed()` | Zwraca `true`, jesli modul dziala w odizolowanym srodowisku Lua. |
| `bool hasDependency(...)` | Sprawdza, czy modul ma dana zaleznosc (opcjonalnie rekurencyjnie). |
| `int getSandbox(LuaInterface *lua)` | Umieszcza na stosie Lua tabele srodowiska tego modulu. |
| `std::string getDescription()`, `getName()`, `getAuthor()`, `getWebsite()`, `getVersion()` | Zwracaja metadane modulu. |
| `bool isAutoLoad()` | Zwraca `true`, jesli modul powinien byc ladowany automatycznie. |
| `int getAutoLoadPriority()` | Zwraca priorytet automatycznego ladowania. |
# # # Metody chronione

-   `void discover(const OTMLNodePtr& moduleNode)`: Metoda wywolywana przez `ModuleManager` do wczytania metadanych modulu z pliku `.otmod`.
# # # Zmienne prywatne

-   `m_loaded`, `m_autoLoad`, `m_reloadable`, `m_sandboxed`: Flagi stanu.
-   `m_autoLoadPriority`: Priorytet ladowania.
-   `m_sandboxEnv`: Referencja do srodowiska Lua (piaskownicy).
-   `m_onLoadFunc`, `m_onUnloadFunc`: Przechowuja kod skrypt�w `onLoad` i `onUnload`.
-   `m_name`, `m_description`, ...: Metadane modulu.
-   `m_dependencies`, `m_scripts`, `m_loadLaterModules`: Listy zaleznosci i skrypt�w.
# # Zaleznosci i powiazania

-   `framework/core/declarations.h`: Definicje wskaznik�w.
-   `framework/otml/declarations.h`: Uzywa `OTMLNodePtr` do parsowania metadanych.
-   `framework/luaengine/luaobject.h`: Jest klasa pochodna `LuaObject`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami `Module` z poziomu Lua.
-   Jest zarzadzana przez `ModuleManager`.

---
# ?? modulemanager.h
# # Opis og�lny

Plik `modulemanager.h` deklaruje klase `ModuleManager`, kt�ra jest singletonem (`g_modules`) odpowiedzialnym za zarzadzanie cyklem zycia wszystkich modul�w w aplikacji.
# # Klasa `ModuleManager`
# # # Opis semantyczny
`ModuleManager` pelni role centralnego rejestru modul�w. Odpowiada za ich odkrywanie (przez skanowanie katalog�w w poszukiwaniu plik�w `.otmod`), ladowanie w odpowiedniej kolejnosci (z uwzglednieniem zaleznosci i priorytet�w), a takze za ich odladowywanie i ponowne ladowanie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void clear()` | Czysci liste modul�w. |
| `void discoverModules()` | Przeszukuje system plik�w w poszukiwaniu plik�w `.otmod` i tworzy dla nich obiekty `Module`. |
| `void autoLoadModules(int maxPriority)` | Laduje wszystkie moduly, kt�re maja flage `autoload` i priorytet nie wiekszy niz podany. |
| `ModulePtr discoverModule(...)` | Parsuje pojedynczy plik `.otmod` i tworzy lub aktualizuje obiekt `Module`. |
| `void ensureModuleLoaded(...)` | Upewnia sie, ze dany modul jest zaladowany; jesli nie, pr�buje go zaladowac, a w razie porazki konczy aplikacje. |
| `void unloadModules()` | Odladowuje wszystkie zaladowane moduly. |
| `void reloadModules()` | Pr�buje odladowac i ponownie zaladowac wszystkie moduly, kt�re na to pozwalaja. |
| `ModulePtr getModule(...)` | Zwraca wskaznik do modulu o podanej nazwie. |
| `std::deque<ModulePtr> getModules()` | Zwraca liste wszystkich odkrytych modul�w. |
# # # Metody chronione

-   `void updateModuleLoadOrder(ModulePtr module)`: Aktualizuje wewnetrzna kolejke modul�w, aby zachowac poprawna kolejnosc ladowania/odladowywania.
# # # Zmienne prywatne

-   `m_modules`: Kolejka (`std::deque`) wszystkich odkrytych modul�w. Zaladowane moduly sa na poczatku.
-   `m_autoLoadModules`: Mapa (`std::multimap`) przechowujaca moduly do automatycznego zaladowania, posortowane wedlug priorytetu.
# # # Zmienne globalne

-   `g_modules`: Globalna instancja `ModuleManager`.
# # Zaleznosci i powiazania

-   `framework/core/module.h`: Definicja klasy `Module`, kt�ra zarzadza `ModuleManager`.
-   Jest oznaczona jako `@bindsingleton g_modules`, co udostepnia jej API w skryptach Lua.
-   Wsp�lpracuje z `ResourceManager` do przeszukiwania systemu plik�w i z `Application` do inicjalizacji i zamykania.

---
# ?? scheduledevent.cpp
# # Opis og�lny

Plik `scheduledevent.cpp` zawiera implementacje klasy `ScheduledEvent`, kt�ra reprezentuje zdarzenie zaplanowane do wykonania w przyszlosci.
# # Klasa `ScheduledEvent`
# # # `ScheduledEvent::ScheduledEvent(...)`

Konstruktor, kt�ry dziedziczy po `Event` i dodatkowo inicjalizuje parametry zwiazane z czasem.

-   **Parametry**:
    -   `function`, `callback`, `botSafe`: Przekazywane do konstruktora klasy bazowej `Event`.
    -   `delay`: Czas w milisekundach, po kt�rym zdarzenie ma zostac wykonane po raz pierwszy.
    -   `maxCycles`: Maksymalna liczba wykonan. `0` oznacza nieskonczonosc.
-   **Dzialanie**:
    -   Oblicza czas pierwszego wykonania: `m_ticks = g_clock.millis() + delay`.
    -   Zapisuje op�znienie, maksymalna liczbe cykli i zeruje licznik wykonanych cykli.
# # # `void ScheduledEvent::execute()`
# # # # Opis semantyczny
Wykonuje `callback` zdarzenia, jesli warunki sa spelnione.
# # # # Dzialanie
1.  Sprawdza, czy zdarzenie nie jest anulowane, czy `callback` istnieje i czy nie przekroczono `maxCycles`.
2.  Jesli warunki sa spelnione, wykonuje `callback` i ustawia `m_executed` na `true`. W przeciwienstwie do `Event`, nie resetuje `callback`, poniewaz moze byc on potrzebny w nastepnym cyklu.
3.  Jesli warunki nie sa spelnione (np. zdarzenie jednorazowe zostalo wykonane), resetuje `callback` do `nullptr`.
4.  Inkrementuje licznik `m_cyclesExecuted`.
# # # `bool ScheduledEvent::nextCycle()`
# # # # Opis semantyczny
Przygotowuje zdarzenie do nastepnego cyklu. Jest wywolywana przez `EventDispatcher` po wykonaniu zdarzenia.
# # # # Dzialanie
1.  Sprawdza, czy zdarzenie powinno byc wykonane ponownie (nieanulowane, nie przekroczono `maxCycles`).
2.  Jesli tak, przesuwa czas nastepnego wykonania o `m_delay`: `m_ticks += m_delay` i zwraca `true`.
3.  Jesli nie, resetuje `callback` do `nullptr` i zwraca `false`, co powoduje usuniecie zdarzenia z kolejki dyspozytora.
# # Zaleznosci i powiazania

-   `framework/core/scheduledevent.h`: Plik nagl�wkowy.
-   `framework/core/clock.h`: Uzywa `g_clock.millis()` do pobierania biezacego czasu.
-   Jest tworzona i zarzadzana przez `EventDispatcher`.

---
# ?? resourcemanager.cpp
# # Opis og�lny

Plik `resourcemanager.cpp` zawiera implementacje klasy `ResourceManager`, kt�ra jest sercem systemu zarzadzania zasobami aplikacji. Implementuje ona logike wyszukiwania, ladowania, odczytu i zapisu plik�w, abstrakcjonujac zr�dlo danych (dysk, archiwum, pamiec).
# # Klasa `ResourceManager`
# # # `void ResourceManager::init(const char *argv0)`

Inicjalizuje biblioteke PhysFS i ustala sciezke do pliku wykonywalnego aplikacji na podstawie argumentu `argv0`.
# # # `bool ResourceManager::setupWriteDir(...)`

Konfiguruje katalog zapisu dla aplikacji, uzywajac `PHYSFS_getPrefDir`. Ten katalog jest zazwyczaj zlokalizowany w folderze danych uzytkownika (np. `%APPDATA%` na Windows, `~/.local/share` na Linux). Montuje ten katalog i ustawia go jako domyslny katalog do zapisu.
# # # `bool ResourceManager::setup()`

Kluczowa metoda, kt�ra pr�buje zlokalizowac i zamontowac gl�wny katalog roboczy aplikacji. Przeszukuje kilka potencjalnych lokalizacji w nastepujacej kolejnosci:
1.  Katalogi na dysku (katalog zapisu, biezacy katalog, katalog bazowy).
2.  Archiwum `data.zip` w tych samych lokalizacjach.
3.  Dane wbudowane w sam plik wykonywalny (`loadDataFromSelf`).
# # # `std::string ResourceManager::getCompactName()`

Metoda pr�bujaca odgadnac "skr�cona nazwe" aplikacji na podstawie zawartosci pliku `init.lua`, kt�ry powinien zawierac definicje `APP_NAME`. Jest to uzywane m.in. do tworzenia katalogu zapisu.
# # # `bool ResourceManager::loadDataFromSelf(...)`

Przeszukuje plik binarny aplikacji w poszukiwaniu sygnatury archiwum ZIP (`PK..`). Jesli znajdzie, traktuje reszte pliku jako archiwum i montuje je w pamieci za pomoca `PHYSFS_mountMemory`.
# # # `std::string ResourceManager::readFileContents(...)`

Odczytuje zawartosc pliku. Po odczytaniu surowych bajt�w, pr�buje je zdeszyfrowac za pomoca `decryptBuffer`. Obsluguje r�wniez specjalny wirtualny katalog `/downloads` do odczytu plik�w pobranych przez `Http`.
# # # `bool ResourceManager::decryptBuffer(std::string& buffer)`

Deszyfruje bufor, jesli jest on zaszyfrowany (rozpoznaje po nagl�wku "ENC3"). Proces deszyfracji obejmuje:
1.  Odczytanie metadanych (klucz, rozmiary, suma kontrolna).
2.  Deszyfracje za pomoca algorytmu `bdecrypt` (odmiana TEA/XTEA).
3.  Dekompresje za pomoca ZLIB.
4.  Weryfikacje sumy kontrolnej Adler-32.
# # # `bool ResourceManager::encryptBuffer(...)`

Szyfruje bufor, wykonujac operacje odwrotne do `decryptBuffer`: kompresja, szyfrowanie i dodanie nagl�wka. Dostepne tylko z flaga `WITH_ENCRYPTION`.
# # # `std::string ResourceManager::resolvePath(std::string path)`

Konwertuje sciezke wzgledna na sciezke absolutna w wirtualnym systemie plik�w. Obsluguje sciezki wzgledne do biezacego skryptu Lua oraz specjalne sciezki dla layout�w UI (np. `/layouts/nazwa_layoutu/...`).
# # # `updateData(...)` i `updateExecutable(...)`

Metody sluzace do aktualizacji klienta. `updateData` przebudowuje archiwum `data.zip` na podstawie pobranych plik�w, a `updateExecutable` zastepuje plik binarny nowa wersja.
# # # `createArchive(...)` i `decompressArchive(...)`

Metody pomocnicze do tworzenia i rozpakowywania archiw�w ZIP w pamieci przy uzyciu biblioteki `libzip`.
# # Zaleznosci i powiazania

-   `framework/core/resourcemanager.h`: Plik nagl�wkowy.
-   **PhysFS**: Podstawowa zaleznosc do obslugi wirtualnego systemu plik�w.
-   **ZLIB, LibZip**: Do obslugi kompresji i archiw�w.
-   `framework/platform/platform.h`: Do operacji specyficznych dla systemu, jak pobieranie biezacego katalogu.
-   `framework/util/crypt.h`: Do szyfrowania, deszyfrowania i obliczania sum kontrolnych.
-   `framework/http/http.h`: Do obslugi wirtualnego katalogu `/downloads`.
-   `boost/process.hpp`: Do uruchamiania nowszej wersji klienta.

---
# ?? scheduledevent.h
# # Opis og�lny

Plik `scheduledevent.h` deklaruje klase `ScheduledEvent`, kt�ra rozszerza funkcjonalnosc `Event`, dodajac mozliwosc planowania wykonania w czasie, cyklicznosci oraz obslugi op�znien.
# # Klasa `ScheduledEvent`
# # # Opis semantyczny
`ScheduledEvent` to zdarzenie, kt�re nie jest wykonywane natychmiast, lecz po uplywie okreslonego czasu (`delay`). Moze byc jednorazowe lub cykliczne (`maxCycles`). Jest zarzadzane przez `EventDispatcher` w kolejce priorytetowej, gdzie priorytetem jest czas wykonania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ScheduledEvent(...)` | Konstruktor, ustawia parametry czasowe zdarzenia. |
| `void execute()` | Wykonuje `callback` i inkrementuje licznik wykonanych cykli. |
| `bool nextCycle()` | Przygotowuje zdarzenie do nastepnego cyklu, aktualizujac czas wykonania. Zwraca `false`, jesli zdarzenie nie powinno byc ponownie wykonane. |
| `int ticks()` | Zwraca absolutny czas (w tickach), w kt�rym zdarzenie ma zostac wykonane. |
| `int remainingTicks()` | Zwraca czas pozostaly do wykonania zdarzenia. |
| `int delay()` | Zwraca op�znienie miedzy cyklami. |
| `int cyclesExecuted()` | Zwraca liczbe dotychczasowych wykonan. |
| `int maxCycles()` | Zwraca maksymalna liczbe wykonan (0 dla nieskonczonosci). |
# # # Zmienne prywatne

-   `m_ticks`: Czas (w tickach systemowych), w kt�rym ma nastapic nastepne wykonanie.
-   `m_delay`: Op�znienie miedzy kolejnymi wykonaniami.
-   `m_maxCycles`: Maksymalna liczba wykonan.
-   `m_cyclesExecuted`: Licznik wykonanych cykli.
# # Struktura `lessScheduledEvent`

Funktor (obiekt funkcyjny) uzywany przez `std::priority_queue` w `EventDispatcher` do sortowania zdarzen. Zapewnia, ze zdarzenia z najwczesniejszym czasem wykonania maja najwyzszy priorytet.

```cpp
struct lessScheduledEvent {
    bool operator()(const ScheduledEventPtr& a, const ScheduledEventPtr& b) {
        return  b->ticks() < a->ticks();
}
};
```
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/event.h`: Klasa bazowa `Event`.
-   `framework/core/clock.h`: Uzywa `g_clock` do pobierania biezacego czasu.
-   Jest tworzona przez `EventDispatcher` i zarzadzana w jego kolejce priorytetowej.
-   Oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami tego typu z poziomu Lua.

---
# ?? timer.cpp
# # Opis og�lny

Plik `timer.cpp` zawiera implementacje prostych metod klasy `Timer`, kt�ra sluzy do mierzenia uplywu czasu.
# # Klasa `Timer`
# # # `void Timer::restart()`
# # # # Opis semantyczny
Resetuje timer, ustawiajac jego punkt startowy na biezacy czas.
# # # # Dzialanie
1.  Pobiera aktualny czas w milisekundach za pomoca `g_clock.millis()`.
2.  Zapisuje te wartosc do `m_startTicks`.
3.  Ustawia flage `m_stopped` na `false`.
# # # `ticks_t Timer::ticksElapsed()`
# # # # Opis semantyczny
Oblicza i zwraca czas, jaki uplynal od ostatniego zresetowania timera.
# # # # Dzialanie
-   Zwraca r�znice miedzy aktualnym czasem (`g_clock.millis()`) a zapisanym czasem startowym (`m_startTicks`).
# # Zaleznosci i powiazania

-   `framework/core/timer.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/core/clock.h`: Uzywa `g_clock` do pobierania biezacego czasu, co zapewnia sp�jnosc z buforowanym czasem klatki.

---
# ?? timer.h
# # Opis og�lny

Plik `timer.h` deklaruje klase `Timer`, kt�ra jest prostym, ale uzytecznym narzedziem do mierzenia uplywajacego czasu. Jest to klasa pomocnicza, szeroko stosowana w calym frameworku do obslugi op�znien, animacji i synchronizacji.
# # Klasa `Timer`
# # # Opis semantyczny
`Timer` dziala jak stoper. Po utworzeniu lub zresetowaniu (`restart()`) zapamietuje punkt w czasie. Nastepnie mozna w dowolnym momencie sprawdzic, ile czasu uplynelo od tego punktu za pomoca metod `ticksElapsed()` lub `timeElapsed()`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Timer()` | Konstruktor, kt�ry natychmiast wywoluje `restart()`. |
| `void restart()` | Resetuje timer, ustawiajac jego punkt startowy na biezacy czas. |
| `void stop()` | Zatrzymuje timer (ustawia flage `m_stopped`). |
| `void adjust(ticks_t value)` | Przesuwa punkt startowy o podana wartosc, efektywnie "dodajac" lub "odejmujac" czas. |
| `ticks_t startTicks()` | Zwraca punkt startowy timera w tickach. |
| `ticks_t ticksElapsed()` | Zwraca czas, jaki uplynal od startu, w milisekundach. |
| `float timeElapsed()` | Zwraca czas, jaki uplynal od startu, w sekundach. |
| `bool running()` | Zwraca `true`, jesli timer nie zostal zatrzymany. |
# # # Zmienne prywatne

-   `m_startTicks`: Czas (w tickach/milisekundach), w kt�rym timer zostal uruchomiony/zresetowany.
-   `m_stopped`: Flaga wskazujaca, czy timer jest zatrzymany.
# # Zaleznosci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje, w tym `ticks_t`.
-   Uzywa `g_clock` (poprzez `ticksElapsed`) do pomiaru czasu.
-   Jest wykorzystywana w wielu miejscach, np. w `UIWidget` do obslugi podw�jnego klikniecia (`m_clickTimer`), w `PlatformWindow` do ograniczania czestotliwosci sprawdzania klawiszy (`m_keyPressTimer`), oraz w animacjach.

---
# ?? consoleapplication.cpp
# # Opis og�lny

Plik `consoleapplication.cpp` zawiera implementacje klasy `ConsoleApplication`, kt�ra jest wersja aplikacji przeznaczona do dzialania w trybie tekstowym, bez interfejsu graficznego. Jest ona uzywana, gdy projekt jest kompilowany bez flagi `FW_GRAPHICS`.
# # Zmienne globalne
# # # `g_app`

Globalna instancja `ConsoleApplication`. Gdy framework jest kompilowany w trybie konsolowym, ta instancja staje sie gl�wnym obiektem aplikacji.

```cpp
ConsoleApplication g_app;
```
# # Klasa `ConsoleApplication`
# # # `void ConsoleApplication::run()`
# # # # Opis semantyczny
Implementuje gl�wna petle aplikacji konsolowej. W przeciwienstwie do `GraphicalApplication`, jest to prosta petla, kt�ra regularnie przetwarza zdarzenia i usypia watek, aby nie zuzywac 100% zasob�w procesora.
# # # # Dzialanie
1.  Ustawia flage `m_running` na `true`.
2.  Wykonuje pierwsze wywolanie `poll()`, aby przetworzyc ewentualne poczatkowe zdarzenia.
3.  Aktualizuje zegar (`g_clock.update()`).
4.  Wywoluje funkcje `onRun` w globalnym skrypcie Lua (`g_app.onRun`).
5.  Wchodzi w petle, kt�ra trwa, dop�ki flaga `m_stopping` nie zostanie ustawiona na `true`.
6.  W kazdej iteracji petli:
    -   Wywoluje `poll()` do przetworzenia zdarzen (np. sieciowych, zaplanowanych).
    -   Usypia gl�wny watek na 1 milisekunde (`stdext::millisleep(1)`).
    -   Aktualizuje zegar (`g_clock.update()`).
    -   Aktualizuje licznik klatek/iteracji (`m_frameCounter.update()`).
7.  Po wyjsciu z petli, resetuje flagi `m_stopping` i `m_running`.

> **NOTE:** Pomimo braku grafiki, wciaz istnieje pojecie "klatki" lub iteracji, kt�re jest sledzone przez `m_frameCounter`.
# # Zaleznosci i powiazania

-   `framework/core/consoleapplication.h`: Plik nagl�wkowy dla tej klasy.
-   `framework/core/clock.h`: Uzywa `g_clock` do aktualizacji czasu w kazdej iteracji.
-   `framework/luaengine/luainterface.h`: Uzywa `g_lua` do wywolania `onRun`.
-   `framework/net/connection.h`: Metoda `poll()` wywoluje m.in. `Connection::poll()`, wiec aplikacja konsolowa moze obslugiwac siec.

---
# ?? shaderprogram.h
# # Opis og�lny

Plik `shaderprogram.h` deklaruje klase `ShaderProgram`, kt�ra jest obiektowym opakowaniem na program shadera w OpenGL. Zarzadza ona kompilacja, linkowaniem i aktywacja shader�w wierzcholk�w i fragment�w.
# # Klasa `ShaderProgram`
# # # Opis semantyczny
`ShaderProgram` agreguje obiekty `Shader` (reprezentujace pojedyncze shadery, np. wierzcholk�w lub fragment�w), linkuje je w jeden wykonywalny program, kt�ry moze byc uzyty w potoku renderowania OpenGL, i dostarcza interfejs do ustawiania uniform�w i atrybut�w. Dziedziczy po `LuaObject`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `ShaderProgram(const std::string& name)` | Konstruktor, tworzy program shadera. |
| `static PainterShaderProgramPtr create(...)` | Statyczna metoda fabryczna do tworzenia `PainterShaderProgram`. |
| `bool addShader(...)` | Dodaje skompilowany obiekt `Shader` do programu. |
| `bool addShaderFromSourceCode(...)` | Tworzy, kompiluje i dodaje shader z kodu zr�dlowego. |
| `bool addShaderFromSourceFile(...)` | Tworzy, kompiluje i dodaje shader z pliku. |
| `void removeShader(...)` | Usuwa shader z programu. |
| `bool link()` | Linkuje wszystkie dodane shadery w jeden program. |
| `bool bind()` | Aktywuje ten program shadera w kontekscie OpenGL. |
| `static void release()` | Deaktywuje jakikolwiek aktywny program shadera. |
| `std::string log()` | Zwraca logi z procesu linkowania. |
| `static void disableAttributeArray(...)` | Wylacza tablice atrybut�w wierzcholk�w. |
| `static void enableAttributeArray(...)` | Wlacza tablice atrybut�w wierzcholk�w. |
| `int getAttributeLocation(...)` | Pobiera lokalizacje atrybutu o danej nazwie. |
| `void bindAttributeLocation(...)` | Przypisuje lokalizacje do atrybutu (przed linkowaniem). |
| `void bindUniformLocation(...)` | Wyszukuje i buforuje lokalizacje uniformu. |
| `void setAttributeArray(...)` | Ustawia wskaznik na dane dla tablicy atrybut�w. |
| `void setAttributeValue(...)` | Ustawia wartosc dla pojedynczego atrybutu. |
| `void setUniformValue(...)` | Ustawia wartosc dla uniformu (przeciazona dla r�znych typ�w: `int`, `float`, `Color`, `Matrix`). |
| `bool isLinked()` | Zwraca `true`, jesli program zostal pomyslnie zlinkowany. |
| `uint getProgramId()` | Zwraca ID programu OpenGL. |
| `ShaderList getShaders()` | Zwraca liste powiazanych shader�w. |
| `std::string getName()` | Zwraca nazwe programu. |
# # # Zmienne prywatne

-   `m_name`: Nazwa programu (dla cel�w identyfikacji).
-   `m_linked`: Flaga wskazujaca, czy program jest zlinkowany.
-   `m_programId`: ID programu w OpenGL.
-   `m_currentProgram`: Statyczna zmienna sledzaca aktualnie aktywny program.
-   `m_shaders`: Lista powiazanych obiekt�w `Shader`.
-   `m_uniformLocations`: Tablica przechowujaca zbuforowane lokalizacje uniform�w.
# # Zaleznosci i powiazania

-   `framework/graphics/shader.h`: Definicja klasy `Shader`.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Jest klasa bazowa dla `PainterShaderProgram`, kt�ra rozszerza ja o uniformy specyficzne dla `Painter`.
-   Jest zarzadzana przez `ShaderManager`.
-   Jest oznaczona jako `@bindclass`, co pozwala na interakcje z obiektami tego typu z poziomu Lua.

---
# ?? animatedtexture.cpp
# # Opis og�lny

Plik `animatedtexture.cpp` zawiera implementacje klasy `AnimatedTexture`, kt�ra reprezentuje teksture skladajaca sie z wielu klatek, odtwarzanych w petli. Jest to podklasa `Texture`.
# # Klasa `AnimatedTexture`
# # # `AnimatedTexture::AnimatedTexture(...)`

Konstruktor, kt�ry tworzy animowana teksture.

-   **Parametry**:
    -   `size`: Rozmiar pojedynczej klatki.
    -   `frames`: Wektor wskaznik�w na obiekty `Image`, reprezentujace poszczeg�lne klatki animacji.
    -   `framesDelay`: Wektor czas�w (w milisekundach), jak dlugo kazda klatka ma byc wyswietlana.
    -   `buildMipmaps`, `compress`: Flagi przekazywane do konstruktora `Texture` dla kazdej klatki.
-   **Dzialanie**:
    1.  Iteruje przez wektor `frames` i dla kazdego `Image` tworzy nowy obiekt `Texture`, kt�ry jest przechowywany w `m_frames`.
    2.  Inicjalizuje timer `m_animTimer` i ustawia biezaca klatke na 0.
# # # `bool AnimatedTexture::buildHardwareMipmaps()`

Wlacza generowanie mipmap dla wszystkich klatek animacji.
# # # `void AnimatedTexture::setSmooth(bool smooth)` i `void AnimatedTexture::setRepeat(bool repeat)`

Ustawiaja odpowiednio flagi wygladzania i powtarzania dla wszystkich tekstur-klatek.
# # # `void AnimatedTexture::update()`
# # # # Opis semantyczny
Aktualizuje stan animacji. Ta metoda jest kluczowa i musi byc wywolywana przed kazdym uzyciem tekstury w petli renderowania.
# # # # Dzialanie
1.  Sprawdza, czy czas, jaki uplynal od ostatniej zmiany klatki (`m_animTimer.ticksElapsed()`) jest wiekszy lub r�wny czasowi op�znienia dla biezacej klatki (`m_framesDelay[m_currentFrame]`).
2.  Jesli tak, przechodzi do nastepnej klatki, zapetlajac animacje (`m_currentFrame = (m_currentFrame + 1) % m_frames.size()`), i resetuje timer.
3.  Wywoluje `update()` na teksturze biezacej klatki.
4.  Aktualizuje ID tekstury (`m_id`) i unikalne ID (`m_uniqueId`) klasy bazowej `Texture` na wartosci z biezacej klatki. Dzieki temu reszta systemu renderujacego moze traktowac `AnimatedTexture` jak zwykla, statyczna teksture, nie wiedzac, ze jej ID zmienia sie w czasie.
# # Zaleznosci i powiazania

-   `framework/graphics/animatedtexture.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do operacji na OpenGL.
-   `framework/core/eventdispatcher.h`: Potencjalnie do planowania aktualizacji.
-   Jest tworzona i zarzadzana przez `TextureManager` podczas ladowania animowanych plik�w PNG (APNG).

---
# ?? animatedtexture.h
# # Opis og�lny

Plik `animatedtexture.h` deklaruje klase `AnimatedTexture`, kt�ra jest specjalizacja klasy `Texture`. Reprezentuje ona teksture, kt�ra zmienia sw�j wyglad w czasie, odtwarzajac sekwencje klatek.
# # Klasa `AnimatedTexture`
# # # Opis semantyczny
`AnimatedTexture` dziedziczy po `Texture` i przechowuje kolekcje tekstur (`std::vector<TexturePtr>`), kt�re reprezentuja poszczeg�lne klatki animacji. Wewnetrzny timer (`m_animTimer`) kontroluje, kt�ra klatka jest aktualnie aktywna. Metoda `update()` jest odpowiedzialna za przelaczanie klatek i aktualizowanie ID tekstury w klasie bazowej, dzieki czemu dla systemu renderujacego wyglada ona jak pojedyncza, dynamicznie zmieniajaca sie tekstura.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `AnimatedTexture(...)` | Konstruktor, tworzy animowana teksture z wektora obraz�w i czas�w op�znien. |
| `virtual ~AnimatedTexture()` | Destruktor. |
| `void replace(const ImagePtr& image)` | Pusta implementacja; zastepowanie animowanej tekstury pojedynczym obrazem nie jest obslugiwane w ten spos�b. |
| `void update()` | Aktualizuje biezaca klatke animacji. |
| `virtual bool isAnimatedTexture()` | Zwraca `true`, odr�zniajac te klase od `Texture`. |
# # # Metody chronione

-   `virtual bool buildHardwareMipmaps()`: Wlacza mipmapping dla wszystkich klatek.
-   `virtual void setSmooth(bool smooth)`: Ustawia wygladzanie dla wszystkich klatek.
-   `virtual void setRepeat(bool repeat)`: Ustawia powtarzanie dla wszystkich klatek.
# # # Zmienne prywatne

-   `m_frames`: Wektor wskaznik�w na tekstury poszczeg�lnych klatek.
-   `m_framesDelay`: Wektor czas�w op�znien dla kazdej klatki.
-   `m_currentFrame`: Indeks biezacej klatki.
-   `m_animTimer`: Timer do sledzenia czasu wyswietlania klatki.
# # Zaleznosci i powiazania

-   `framework/graphics/texture.h`: Klasa bazowa `Texture`.
-   `framework/core/timer.h`: Uzywa `Timer` do zarzadzania animacja.
-   Jest tworzona przez `TextureManager` podczas ladowania plik�w APNG (Animated PNG).

---
# ?? apngloader.cpp
# # Opis og�lny

Plik `apngloader.cpp` zawiera implementacje funkcji do ladowania animowanych plik�w PNG (APNG) oraz do zapisu standardowych plik�w PNG. Kod jest oparty na bibliotece APNG Disassembler 2.3 autorstwa Maxa Stepina i zostal dostosowany do potrzeb frameworka.
# # Funkcje
# # # `load_apng(std::stringstream& file, struct apng_data *apng)`
# # # # Opis semantyczny
Gl�wna funkcja do parsowania pliku w formacie APNG. Odczytuje ona poszczeg�lne "chunki" (fragmenty) pliku PNG, takie jak `IHDR` (nagl�wek), `PLTE` (paleta), `tRNS` (przezroczystosc), `acTL` (nagl�wek animacji), `fcTL` (kontrola klatki) oraz `IDAT`/`fdAT` (dane obrazu).
# # # # Dzialanie
1.  Sprawdza sygnature pliku PNG.
2.  Odczytuje nagl�wek `IHDR` w celu uzyskania wymiar�w, glebi kolor�w i innych podstawowych informacji.
3.  Alokuje bufory na zdekompresowane dane obrazu.
4.  W petli odczytuje kolejne chunki:
    -   `PLTE` i `tRNS`: Wczytuje palete kolor�w i informacje o przezroczystosci.
    -   `acTL`: Identyfikuje plik jako animowany, odczytuje liczbe klatek i zapetlen.
    -   `fcTL`: Odczytuje metadane dla pojedynczej klatki, takie jak wymiary, przesuniecie, czas trwania i operacje mieszania (`blend_op`) oraz usuwania (`dispose_op`).
    -   `IDAT` i `fdAT`: Gromadzi skompresowane dane obrazu dla klatki.
5.  Po odczytaniu danych dla klatki (`fcTL` lub `IEND`), dekompresuje je za pomoca ZLIB (`inflate`), a nastepnie odfiltrowuje (usuwa filtry PNG takie jak Sub, Up, Average, Paeth).
6.  Komponuje finalny obraz klatki na podstawie poprzedniej klatki, stosujac operacje `dispose_op` (np. zostaw, wyczysc do tla) i `blend_op` (np. zastap, nal�z).
7.  Wynikowe dane klatki w formacie RGBA sa zapisywane do bufora w strukturze `apng_data`.
8.  Zwraca 0 w przypadku sukcesu, -1 w przypadku bledu.
# # # `save_png(std::stringstream& f, unsigned int width, unsigned int height, int channels, unsigned char *pixels)`
# # # # Opis semantyczny
Zapisuje dane obrazu do formatu PNG. Implementuje podstawowa kompresje z filtrowaniem, dynamicznie wybierajac najlepszy filtr dla kazdej linii obrazu w celu uzyskania lepszej kompresji.
# # # # Dzialanie
1.  Zapisuje sygnature PNG i nagl�wek `IHDR`.
2.  Inicjalizuje strumienie kompresji ZLIB.
3.  Dla kazdej linii obrazu:
    -   Testuje piec r�znych filtr�w PNG (None, Sub, Up, Average, Paeth).
    -   Wybiera filtr, kt�ry generuje dane o najmniejszej sumie wartosci bezwzglednych bajt�w (co zwykle prowadzi do lepszej kompresji).
    -   Kompresuje przefiltrowana linie za pomoca `deflate`.
4.  Zapisuje skompresowane dane w chunkach `IDAT`.
5.  Zapisuje chunk koncowy `IEND`.
# # # Funkcje pomocnicze

Plik zawiera wiele funkcji pomocniczych, m.in.:
-   `read32`, `read16`: Do odczytu liczb w porzadku big-endian.
-   `read_sub_row`, `read_up_row`, `read_average_row`, `read_paeth_row`: Do odfiltrowywania danych obrazu PNG.
-   `compose0`, `compose2`, `compose3`, `compose4`, `compose6`: Do kompozycji klatek animacji, konwertujac r�zne formaty pikseli na RGBA i stosujac operacje mieszania.
-   `unpack`: Dekompresuje i odfiltrowuje dane jednej klatki.
-   `write_chunk`, `write_IDATs`: Do zapisu chunk�w PNG.
-   `free_apng`: Zwalnia pamiec zaalokowana w strukturze `apng_data`.
# # Zaleznosci i powiazania

-   `framework/graphics/apngloader.h`: Plik nagl�wkowy.
-   **ZLIB**: Uzywana do kompresji i dekompresji danych obrazu.
-   Jest uzywana przez `Image::loadPNG` do ladowania obraz�w i `Image::savePNG` do ich zapisu.

---
# ?? apngloader.h
# # Opis og�lny

Plik `apngloader.h` jest plikiem nagl�wkowym, kt�ry deklaruje struktury danych i funkcje do obslugi plik�w w formacie APNG (Animated PNG). Definiuje on publiczny interfejs do ladowania, zapisywania i zwalniania danych obrazu.
# # Struktura `apng_data`
# # # Opis semantyczny
Struktura ta przechowuje wszystkie zdekompresowane i sparsowane dane z pliku APNG.
# # # Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `pdata` | `unsigned char *` | Wskaznik na surowe dane pikseli wszystkich klatek, w formacie RGBA, jedna po drugiej. |
| `width` | `unsigned int` | Szerokosc obrazu w pikselach. |
| `height` | `unsigned int` | Wysokosc obrazu w pikselach. |
| `first_frame`| `unsigned int` | Indeks pierwszej klatki animacji (zwykle 0). |
| `last_frame` | `unsigned int` | Indeks ostatniej klatki animacji. |
| `bpp` | `unsigned char` | Liczba bajt�w na piksel. |
| `coltype` | `unsigned char` | Typ koloru z nagl�wka PNG. |
| `num_frames` | `unsigned int` | Calkowita liczba klatek w animacji. |
| `num_plays` | `unsigned int` | Liczba powt�rzen animacji (0 oznacza nieskonczonosc). |
| `frames_delay`| `unsigned short *` | Tablica czas�w wyswietlania dla kazdej klatki, w milisekundach. |
# # Funkcje publiczne

| Funkcja | Opis |
| :--- | :--- |
| `int load_apng(std::stringstream& file, struct apng_data *apng)` | Laduje i parsuje dane APNG ze strumienia `file` i zapisuje wyniki w strukturze `apng`. Zwraca 0 w przypadku sukcesu, -1 w przypadku bledu. |
| `void save_png(std::stringstream& file, ...)` | Zapisuje dane obrazu (pojedynczej klatki) do strumienia `file` w formacie PNG. |
| `void free_apng(struct apng_data *apng)` | Zwalnia pamiec zaalokowana dynamicznie w strukturze `apng_data` (tj. `pdata` i `frames_delay`). |
# # Zaleznosci i powiazania

-   `<sstream>`: Uzywa `std::stringstream` jako zr�dla danych wejsciowych i wyjsciowych.
-   Funkcje te sa wykorzystywane przez klase `Image` do implementacji metod `loadPNG` i `savePNG`.

---
# ?? atlas.cpp
# # Opis og�lny

Plik `atlas.cpp` implementuje klase `Atlas`, kt�ra zarzadza tzw. "atlasem tekstur". Jest to technika optymalizacyjna, polegajaca na laczeniu wielu malych tekstur w jedna duza teksture, aby zminimalizowac liczbe zmian stanu w potoku renderowania grafiki (zmiana tekstury jest kosztowna operacja).
# # Zmienne globalne
# # # `g_atlas`

Globalna instancja klasy `Atlas`, zapewniajaca scentralizowany dostep do mechanizmu cachowania tekstur.

```cpp
Atlas g_atlas;
```
# # Klasa `Atlas`
# # # `void Atlas::init()`
# # # # Opis semantyczny
Inicjalizuje atlas.
# # # # Dzialanie
1.  Okresla maksymalny rozmiar tekstury atlasu, biorac pod uwage ograniczenia karty graficznej (`g_graphics.getMaxTextureSize()`), ale nie przekraczajac `4096x4096`.
2.  Tworzy dwa obiekty `FrameBuffer`:
    -   `m_atlas[0]`: Gl�wny atlas dla og�lnych tekstur.
    -   `m_atlas[1]`: Atlas dla tekstur font�w.
3.  Wiaze tekstury atlas�w do jednostek teksturujacych `GL_TEXTURE6` i `GL_TEXTURE7`, aby byly globalnie dostepne dla shader�w.
4.  Resetuje oba atlasy, przygotowujac je do uzycia.
# # # `void Atlas::reset()` i `void Atlas::resetAtlas(int location)`

Metody do czyszczenia atlasu. `reset()` czysci gl�wny atlas i bufor `m_cache`. `resetAtlas()` przygotowuje konkretny atlas do ponownego uzycia, czyszczac jego zawartosc (wypelniajac przezroczystoscia) i resetujac informacje o wolnych przestrzeniach (`m_locations`).
# # # `void Atlas::terminate()`

Zwalnia obiekty `FrameBuffer` atlas�w.
# # # `Point Atlas::cache(uint64_t hash, const Size& size, bool& draw)`
# # # # Opis semantyczny
Gl�wna metoda do cachowania tekstury. Sprawdza, czy tekstura o danym hashu jest juz w atlasie. Jesli nie, znajduje dla niej wolne miejsce.
# # # # Dzialanie
1.  Jesli `m_doReset` jest `true`, najpierw resetuje atlas.
2.  Sprawdza, czy hash istnieje w `m_cache`. Jesli tak, zwraca zapisana pozycje.
3.  Jesli nie, oblicza, jakiego rozmiaru bloku potrzebuje tekstura (`calculateIndex`).
4.  Jesli tekstura jest za duza, zwraca `Point(-1, -1)`.
5.  Pr�buje znalezc wolne miejsce w `m_locations`. Jesli go nie ma, wywoluje `findSpace` w celu podzialu wiekszego bloku.
6.  Jesli nie ma miejsca, ustawia `m_doReset = true` i zwraca `Point(-1, -1)`.
7.  Jesli miejsce sie znajdzie, zapisuje pozycje w `m_cache`, ustawia `draw = true` (sygnalizujac, ze tekstura musi zostac narysowana w atlasie) i zwraca pozycje.
# # # `void Atlas::bind()` i `void Atlas::release()`

Metody do bindowania i zwalniania `FrameBuffer` gl�wnego atlasu, aby umozliwic rysowanie w nim nowych tekstur.
# # # `Point Atlas::cacheFont(const TexturePtr& fontTexture)`

Specjalna metoda do cachowania tekstur font�w w drugim atlasie (`m_atlas[1]`). Dziala podobnie do `cache`, ale od razu rysuje teksture fontu w znalezionym miejscu.
# # # `int Atlas::calculateIndex(const Size& size)`

Oblicza indeks (od 0 do 6) odpowiadajacy rozmiarowi bloku potrzebnego do przechowania tekstury (np. 32x32, 64x64, ..., 2048x2048).
# # # `bool Atlas::findSpace(int location, int index)`

Rekurencyjna metoda, kt�ra pr�buje znalezc wolne miejsce dla bloku o danym `index`. Jesli nie ma wolnych blok�w tego rozmiaru, pr�buje znalezc i podzielic wiekszy blok (o `index + 1`).
# # # `std::string Atlas::getStats()`

Zwraca informacje debugowania o liczbie wolnych miejsc w poszczeg�lnych blokach atlasu.
# # Zaleznosci i powiazania

-   `framework/graphics/atlas.h`: Plik nagl�wkowy.
-   `framework/graphics/framebuffermanager.h`: Uzywa `FrameBufferManager` do tworzenia `FrameBuffer` dla atlas�w.
-   `framework/graphics/painter.h`: Uzywa `Painter` do rysowania w atlasie.
-   `framework/graphics/graphics.h`: Do pobierania maksymalnego rozmiaru tekstury.
-   Jest uzywany przez `DrawQueue` i `DrawCache` do optymalizacji renderowania.

---
# ?? bitmapfont.cpp
# # Opis og�lny

Plik `bitmapfont.cpp` zawiera implementacje klasy `BitmapFont`, kt�ra zarzadza fontami opartymi na bitmapach (obrazach). Taki font sklada sie z pojedynczej tekstury zawierajacej wszystkie glify (znaki) ulozone w siatce.
# # Klasa `BitmapFont`
# # # `void BitmapFont::load(const OTMLNodePtr& fontNode)`
# # # # Opis semantyczny
Laduje definicje fontu z wezla OTML (zazwyczaj z pliku `.otfont`).
# # # # Dzialanie
1.  Odczytuje z wezla OTML podstawowe atrybuty fontu:
    -   `texture`: Sciezka do pliku z obrazem fontu.
    -   `glyph-size`: Rozmiar pojedynczego glifu w siatce.
    -   `height`: Rzeczywista wysokosc glifu.
    -   `y-offset`: Przesuniecie w osi Y.
    -   `first-glyph`: Kod ASCII pierwszego znaku w siatce (zwykle 32 - spacja).
    -   `spacing`: Odstepy miedzy glifami.
2.  Oblicza szerokosci poszczeg�lnych glif�w:
    -   Jesli zdefiniowano `fixed-glyph-width`, wszystkie glify maja te sama szerokosc.
    -   W przeciwnym razie wywoluje `calculateGlyphsWidthsAutomatically`, aby automatycznie wykryc szerokosc kazdego znaku.
3.  Ustawia specjalne szerokosci dla spacji (32) i znaku nowej linii (`\n`).
4.  Laduje teksture fontu za pomoca `g_textures.getTexture()`.
5.  Jesli fonty sa cachowane w atlasie (`!DONT_CACHE_FONTS`), wywoluje `g_atlas.cacheFont()` i ustawia teksture atlasu jako zr�dlowa.
6.  Oblicza i zapisuje wsp�lrzedne tekstury dla kazdego glifu w `m_glyphsTextureCoords`.
# # # `void BitmapFont::drawText(...)`

Metody te nie rysuja tekstu bezposrednio, lecz dodaja zadanie rysowania do globalnej kolejki `g_drawQueue`.

-   **`drawText(..., const Color& color, ...)`**: Dodaje zadanie rysowania tekstu jednokolorowego.
-   **`drawColoredText(..., const std::vector<std::pair<int, Color>>& colors, ...)`**: Dodaje zadanie rysowania tekstu z wieloma kolorami.
# # # `void BitmapFont::calculateDrawTextCoords(...)`

Oblicza wsp�lrzedne ekranowe i tekstury dla kazdego glifu w podanym tekscie, uwzgledniajac wyr�wnanie i przycinanie do podanego prostokata. Wyniki sa zapisywane w `CoordsBuffer`.
# # # `const std::vector<Point>& BitmapFont::calculateGlyphsPositions(...)`

Oblicza pozycje (lewy g�rny r�g) kazdego glifu w tekscie, uwzgledniajad wyr�wnanie. Uzywa statycznych, lokalnych dla watku wektor�w w celu optymalizacji. Zwraca r�wniez obliczony rozmiar calego bloku tekstu.
# # # `Size BitmapFont::calculateTextRectSize(const std::string& text)`

Zwraca rozmiar prostokata, jaki zajmie podany tekst, uzywajac `calculateGlyphsPositions`.
# # # `std::string BitmapFont::wrapText(...)`

Implementuje zawijanie tekstu. Dzieli tekst na linie, tak aby zadna nie przekraczala `maxWidth`. Obsluguje r�wniez przenoszenie definicji kolor�w (`m_textColors`) do nowych linii.
# # # `void BitmapFont::calculateGlyphsWidthsAutomatically(...)`

Prywatna metoda, kt�ra analizuje obraz tekstury fontu piksel po pikselu. Dla kazdego glifu znajduje ostatnia nieprzezroczysta kolumne pikseli, aby precyzyjnie okreslic jego szerokosc.
# # Zaleznosci i powiazania

-   `framework/graphics/atlas.h`: Uzywa `g_atlas` do cachowania tekstur font�w.
-   `framework/graphics/bitmapfont.h`: Plik nagl�wkowy.
-   `framework/graphics/texturemanager.h`: Uzywa `g_textures` do ladowania obrazu fontu.
-   `framework/graphics/image.h`: Uzywa `Image` do analizy pikseli w `calculateGlyphsWidthsAutomatically`.
-   `framework/graphics/drawqueue.h`: Dodaje zadania rysowania tekstu do `g_drawQueue`.
-   Jest zarzadzana przez `FontManager`.

---
# ?? atlas.h
# # Opis og�lny

Plik `atlas.h` deklaruje interfejs klasy `Atlas`, kt�ra implementuje mechanizm atlasu tekstur. Celem atlasu jest optymalizacja renderowania poprzez grupowanie wielu malych tekstur w jedna duza teksture, co redukuje liczbe wywolan `glBindTexture` w OpenGL.
# # Klasa `Atlas`
# # # Opis semantyczny
`Atlas` zarzadza jednym lub kilkoma duzymi obiektami `FrameBuffer`, kt�re dzialaja jak "pl�tna". Kiedy system renderujacy potrzebuje narysowac mala teksture, `Atlas` znajduje dla niej wolne miejsce w jednym z pl�cien, kopiuje tam jej zawartosc (jesli jeszcze jej tam nie ma) i zwraca wsp�lrzedne wewnatrz atlasu. P�zniejsze odwolania do tej samej tekstury uzywaja juz skopiowanej wersji z atlasu.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje atlas, tworzac `FrameBuffer` o maksymalnym mozliwym rozmiarze. |
| `void terminate()` | Zwalnia zasoby atlasu. |
| `void reload()` | Resetuje i czysci zawartosc atlas�w. |
| `Point cache(uint64_t hash, const Size& size, bool& draw)` | Gl�wna metoda cachujaca. Sprawdza, czy tekstura o danym hashu jest juz w atlasie. Jesli nie, znajduje wolne miejsce i zwraca jego koordynaty. Parametr `draw` jest ustawiany na `true`, jesli teksture trzeba narysowac w atlasie. |
| `Point cacheFont(const TexturePtr& fontTexture)` | Specjalna metoda do cachowania tekstur font�w w dedykowanym atlasie. |
| `TexturePtr get(int location)` | Zwraca wskaznik na teksture atlasu o danym indeksie (0 - gl�wny, 1 - fonty). |
| `void bind()` | Bindowanie `FrameBuffer` atlasu jako celu renderowania. |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `std::string getStats()` | Zwraca informacje diagnostyczne o stanie atlasu. |
# # # Zmienne prywatne

-   `m_atlas[2]`: Tablica wskaznik�w na `FrameBuffer` (dla og�lnych tekstur i font�w).
-   `m_cache`: Mapa (`std::map`) przechowujaca hashe skachowanych tekstur i ich pozycje w atlasie.
-   `m_locations[2][7]`: Tablica list przechowujaca pozycje wolnych blok�w o r�znych rozmiarach (od 32x32 do 2048x2048) dla obu atlas�w.
-   `m_size`: Rozmiar boku tekstury atlasu.
-   `m_doReset`: Flaga sygnalizujaca koniecznosc zresetowania atlasu (gdy zabraknie miejsca).
# # # Zmienne globalne

-   `g_atlas`: Globalna instancja `Atlas`.
# # Zaleznosci i powiazania

-   `framework/graphics/drawqueue.h`: Potencjalnie uzywany, ale gl�wnie to `DrawQueue` uzywa `Atlas`.
-   `framework/graphics/framebuffer.h`: Uzywa `FrameBuffer` jako "pl�tna" dla atlasu.
-   Uzywany przez system renderowania (`DrawQueue`, `DrawCache`) do optymalizacji rysowania.
-   `FontManager` uzywa go do cachowania tekstur font�w.

---
# ?? bitmapfont.h
# # Opis og�lny

Plik `bitmapfont.h` deklaruje klase `BitmapFont`, kt�ra reprezentuje font oparty na bitmapie. Jest to kluczowy element systemu renderowania tekstu w aplikacji.
# # Klasa `BitmapFont`
# # # Opis semantyczny
`BitmapFont` zarzadza pojedynczym fontem, kt�ry jest zdefiniowany jako obraz (tekstura) zawierajacy siatke znak�w (glif�w). Klasa przechowuje informacje o rozmiarze glif�w, ich pozycjach na teksturze oraz szerokosciach poszczeg�lnych znak�w. Dostarcza metody do rysowania tekstu (kt�re w rzeczywistosci deleguja zadanie do `DrawQueue`) oraz do obliczania wymiar�w i zawijania tekstu.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `BitmapFont(const std::string& name)` | Konstruktor, ustawia nazwe fontu i unikalne ID. |
| `void load(const OTMLNodePtr& fontNode)` | Laduje definicje fontu z wezla OTML. |
| `void drawText(...)` | Dodaje do kolejki renderowania zadanie narysowania tekstu. |
| `void drawColoredText(...)` | Dodaje zadanie narysowania tekstu z wieloma kolorami. |
| `void calculateDrawTextCoords(...)` | Oblicza wsp�lrzedne wierzcholk�w i tekstur dla renderowanego tekstu. |
| `const std::vector<Point>& calculateGlyphsPositions(...)` | Oblicza pozycje poszczeg�lnych glif�w w tekscie. |
| `Size calculateTextRectSize(...)` | Oblicza rozmiar prostokata zajmowanego przez tekst. |
| `std::string wrapText(...)` | Zlamuje tekst na wiele linii, aby zmiescil sie w podanej szerokosci. |
| `int getId()` | Zwraca unikalne ID fontu. |
| `std::string getName()` | Zwraca nazwe fontu. |
| `int getGlyphHeight()` | Zwraca wysokosc glif�w. |
| `const Rect* getGlyphsTextureCoords()` | Zwraca tablice wsp�lrzednych tekstur dla wszystkich glif�w. |
| `const Size* getGlyphsSize()` | Zwraca tablice rozmiar�w dla wszystkich glif�w. |
| `const TexturePtr& getTexture()` | Zwraca teksture fontu (moze to byc tekstura atlasu). |
| `int getYOffset()` | Zwraca przesuniecie Y. |
| `Size getGlyphSpacing()` | Zwraca odstepy miedzy glifami. |
# # # Zmienne prywatne

-   `m_name`: Nazwa fontu.
-   `m_glyphHeight`: Wysokosc glifu.
-   `m_firstGlyph`: Kod ASCII pierwszego znaku.
-   `m_yOffset`: Przesuniecie w osi Y.
-   `m_id`: Unikalne ID fontu.
-   `m_glyphSpacing`: Odstepy miedzy glifami.
-   `m_texture`: Wskaznik na teksture fontu.
-   `m_glyphsTextureCoords[256]`: Tablica wsp�lrzednych tekstur dla kazdego glifu.
-   `m_glyphsSize[256]`: Tablica rozmiar�w dla kazdego glifu.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Deklaracje typ�w graficznych.
-   `framework/graphics/texture.h`: Uzywa `Texture` do przechowywania obrazu fontu.
-   `framework/otml/declarations.h`: Uzywa `OTMLNodePtr` w metodzie `load`.
-   `framework/graphics/coordsbuffer.h`: Uzywa `CoordsBuffer` do przechowywania geometrii tekstu.
-   Jest zarzadzana przez `FontManager`.
-   Jest uzywana przez `UIWidget` i inne komponenty do renderowania tekstu.

---
# ?? cachedtext.cpp
# # Opis og�lny

Plik `cachedtext.cpp` zawiera implementacje klasy `CachedText`, kt�ra sluzy do optymalizacji renderowania tekstu, kt�ry nie zmienia sie czesto.
# # Klasa `CachedText`
# # # `CachedText::CachedText()`

Konstruktor. Inicjalizuje domyslny font, wyr�wnanie do srodka (`Fw::AlignCenter`) i inne wartosci domyslne.
# # # `void CachedText::draw(const Rect& rect, const Color& color)`
# # # # Opis semantyczny
Gl�wna metoda rysujaca. Renderuje tekst w podanym prostokacie z danym kolorem.
# # # # Dzialanie
1.  Sprawdza, czy font jest ustawiony.
2.  Sprawdza, czy tekst musi zostac "przekeshowany" (`m_textMustRecache`) lub czy zmienil sie prostokat docelowy (`m_textCachedScreenCoords`). Jesli tak, aktualizuje buforowane koordynaty.
3.  Wywoluje metode `m_font->drawText()` lub `m_font->drawColoredText()` w celu dodania zadania rysowania do `DrawQueue`.

> NOTE: Nazwa "cached" moze byc nieco mylaca. Klasa nie renderuje tekstu do tekstury. Zamiast tego, "keszuje" obliczenia zwiazane z pozycjonowaniem glif�w, ale samo rysowanie odbywa sie dynamicznie w kazdej klatce za pomoca `BitmapFont::drawText`.
# # # `void CachedText::setColoredText(const std::vector<std::string>& texts)`

Ustawia tekst skladajacy sie z fragment�w o r�znych kolorach. Parsuje wektor, tworzac wewnetrzna reprezentacje `m_text` i `m_textColors`, a nastepnie wywoluje `update()`.
# # # `void CachedText::update()`

Prywatna metoda pomocnicza. Oblicza rozmiar tekstu za pomoca `m_font->calculateTextRectSize()` i ustawia flage `m_textMustRecache` na `true`, co wymusza przeliczenie geometrii przy nastepnym wywolaniu `draw()`.
# # # `void CachedText::wrapText(int maxWidth)`

Zawija tekst, aby zmiescil sie w podanej szerokosci, uzywajac metody `m_font->wrapText()`, a nastepnie wywoluje `update()`.
# # Zaleznosci i powiazania

-   `framework/graphics/cachedtext.h`: Plik nagl�wkowy.
-   `framework/graphics/painter.h`: Posrednio, poprzez `BitmapFont`.
-   `framework/graphics/fontmanager.h`: Uzywa `g_fonts` do pobrania domyslnego fontu.
-   `framework/graphics/bitmapfont.h`: Kluczowa zaleznosc; uzywa `BitmapFont` do wszystkich operacji na tekscie.

---
# ?? colorarray.h
# # Opis og�lny

Plik `colorarray.h` deklaruje klase `ColorArray`, kt�ra jest prostym kontenerem na tablice kolor�w w formacie `float`. Jest uzywana do przekazywania kolor�w dla poszczeg�lnych wierzcholk�w do systemu renderujacego.
# # Klasa `ColorArray`
# # # Opis semantyczny
`ColorArray` dziala jako bufor dla kolor�w. Kazdy kolor jest reprezentowany przez cztery wartosci `float` (R, G, B, A) w zakresie od 0.0 do 1.0. Klasa udostepnia metody do dodawania kolor�w i dostepu do surowego wskaznika na dane, co jest potrzebne do przekazania ich do OpenGL.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addColor(float r, float g, float b, float a)` | Dodaje kolor do bufora, podajac skladowe jako `float`. |
| `void addColor(const Color& c)` | Dodaje kolor do bufora, pobierajac skladowe z obiektu `Color`. |
| `void clear()` | Czysci bufor. |
| `float *colors() const` | Zwraca wskaznik na poczatek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaznik na surowe dane bufora. |
| `int colorCount() const` | Zwraca liczbe pelnych kolor�w w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbe kolor�w. |
| `int size() const` | Zwraca calkowita liczbe wartosci `float` w buforze (tj. `colorCount() * 4`). |
# # # Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, kt�ry przechowuje dane kolor�w.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: Uzywa `DataBuffer` jako wewnetrznego kontenera.
-   Jest uzywana przez `Painter` do przekazywania tablicy kolor�w do shadera, co pozwala na rysowanie gradient�w lub wielokolorowych ksztalt�w.

---
# ?? cachedtext.h
# # Opis og�lny

Plik `cachedtext.h` deklaruje klase `CachedText`, kt�ra jest opakowaniem (wrapperem) ulatwiajacym zarzadzanie i renderowanie tekstu, kt�ry moze byc keszowany.
# # Klasa `CachedText`
# # # Opis semantyczny
Klasa `CachedText` przechowuje tekst, font, wyr�wnanie i inne wlasciwosci. Jej gl�wnym celem jest optymalizacja renderowania poprzez unikanie ponownych obliczen geometrii tekstu w kazdej klatce. Kiedy tekst lub jego parametry sie zmieniaja, metoda `update()` jest wywolywana, aby przeliczyc rozmiar i ustawic flage koniecznosci ponownego buforowania wsp�lrzednych.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CachedText()` | Konstruktor. |
| `void draw(const Rect& rect, const Color& color)` | Rysuje skeszowany tekst w podanym prostokacie. |
| `void wrapText(int maxWidth)` | Zawija tekst do podanej szerokosci. |
| `void setFont(...)` | Ustawia font i aktualizuje tekst. |
| `void setText(...)` | Ustawia tekst i aktualizuje go. |
| `void setColoredText(...)` | Ustawia tekst skladajacy sie z fragment�w o r�znych kolorach. |
| `void setAlign(...)` | Ustawia wyr�wnanie tekstu. |
| `Size getTextSize()` | Zwraca obliczony rozmiar tekstu. |
| `std::string getText() const` | Zwraca przechowywany tekst. |
| `BitmapFontPtr getFont() const` | Zwraca uzywany font. |
| `Fw::AlignmentFlag getAlign() const` | Zwraca wyr�wnanie. |
| `bool hasText()` | Zwraca `true`, jesli tekst nie jest pusty. |
# # # Zmienne prywatne

-   `m_text`: Gl�wny, niezmieniony tekst.
-   `m_textColors`: Wektor par przechowujacy pozycje i kolory dla tekstu wielokolorowego.
-   `m_textSize`: Obliczony rozmiar tekstu.
-   `m_textMustRecache`: Flaga wskazujaca, ze geometria tekstu musi zostac przeliczona.
-   `m_textCachedScreenCoords`: Ostatni prostokat, w kt�rym tekst byl rysowany.
-   `m_font`: Uzywany `BitmapFont`.
-   `m_align`: Wyr�wnanie tekstu.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/coordsbuffer.h`: Posrednio, przez `BitmapFont`.
-   `framework/graphics/drawqueue.h`: Posrednio, przez `BitmapFont`.
-   Klasa ta jest prawdopodobnie uzywana w komponentach UI, kt�re wyswietlaja tekst, aby uproscic i zoptymalizowac jego renderowanie.

---
# ?? coordsbuffer.h
# # Opis og�lny

Plik `coordsbuffer.h` deklaruje klase `CoordsBuffer`, kt�ra jest specjalizowanym kontenerem do przechowywania wsp�lrzednych wierzcholk�w (`vertex`) i tekstur (`texture coord`). Jest to kluczowy element optymalizacyjny, pozwalajacy na grupowanie geometrii wielu obiekt�w i rysowanie ich w jednym wywolaniu (batching).
# # Klasa `CoordsBuffer`
# # # Opis semantyczny
`CoordsBuffer` przechowuje dwie tablice wierzcholk�w (`VertexArray`): jedna dla pozycji na ekranie i druga dla pozycji na teksturze. Dostarcza metody do dodawania prostych prymityw�w geometrycznych (tr�jkaty, prostokaty). Posiada mechanizm "keszowania" danych w sprzetowym buforze VBO (Vertex Buffer Object) w celu dalszej optymalizacji.

> **NOTE**: Mimo nazwy, `CoordsBuffer` jest jednorazowego uzytku dla `DrawQueue`. Po przekazaniu do kolejki, jego zawartosc jest przenoszona (`std::move`), a oryginal staje sie pusty. To zachowanie jest wymuszone przez usuniecie konstruktora kopiujacego i operatora przypisania, a zdefiniowanie konstruktora przenoszacego.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CoordsBuffer()` | Konstruktor, tworzy wewnetrzne obiekty `VertexArray`. |
| `~CoordsBuffer()` | Destruktor. |
| `CoordsBuffer(CoordsBuffer&& c)` | Konstruktor przenoszacy. |
| `void clear()` | Czysci oba bufory wierzcholk�w. |
| `void addTriangle(...)` | Dodaje tr�jkat (tylko wsp�lrzedne wierzcholk�w). |
| `void addRect(const Rect& dest)` | Dodaje prostokat (tylko wsp�lrzedne wierzcholk�w). |
| `void addRect(const Rect& dest, const Rect& src)` | Dodaje prostokat z tekstura. |
| `void addQuad(...)`, `addUpsideDownQuad(...)` | Dodaje czworokat (quad) - przydatne do renderowania w trybie `TriangleStrip`. |
| `void addBoudingRect(...)` | Dodaje geometrie ramki o okreslonej grubosci. |
| `void addRepeatedRects(...)` | Wypelnia prostokat docelowy powtarzajaca sie tekstura. |
| `float *getVertexArray()` | Zwraca wskaznik na dane wierzcholk�w. |
| `float *getTextureCoordArray()` | Zwraca wskaznik na dane wsp�lrzednych tekstury. |
| `int getVertexCount()` | Zwraca liczbe wierzcholk�w. |
| `HardwareBuffer* getVertexHardwareCache()` | Zwraca wskaznik na sprzetowy bufor VBO dla wierzcholk�w (jesli istnieje). |
| `void cache()` | Tworzy i wypelnia sprzetowe bufory VBO na podstawie biezacych danych. |
| `Rect getTextureRect()`| Oblicza i zwraca prostokat ograniczajacy wszystkie wsp�lrzedne tekstury. |
# # # Zmienne prywatne

-   `m_locked`: Flaga uzywana do optymalizacji (zapobiega niepotrzebnemu kopiowaniu danych).
-   `m_vertexArray`: Wskaznik na `VertexArray` przechowujacy pozycje.
-   `m_textureCoordArray`: Wskaznik na `VertexArray` przechowujacy wsp�lrzedne tekstury.
# # Zaleznosci i powiazania

-   `framework/graphics/vertexarray.h`: Uzywa `VertexArray` jako podstawowego kontenera na dane.
-   Jest intensywnie uzywana przez `UIWidget` i jego podklasy do generowania geometrii, kt�ra nastepnie jest przekazywana do `DrawQueue` w celu renderowania.

---
# ?? deptharray.h
# # Opis og�lny

Plik `deptharray.h` deklaruje klase `DepthArray`, kt�ra jest prostym kontenerem na tablice wartosci glebokosci (depth) w formacie `float`. Jest to prawdopodobnie czesc eksperymentalnego lub nie w pelni zaimplementowanego mechanizmu renderowania 3D lub sortowania glebokosci.
# # Klasa `DepthArray`
# # # Opis semantyczny
`DepthArray` dziala jako bufor dla wartosci glebokosci (wsp�lrzedna Z). Kazda wartosc `float` w buforze odpowiada jednemu wierzcholkowi. Klasa udostepnia metody do dodawania wartosci i dostepu do surowego wskaznika na dane, co jest potrzebne do przekazania ich do OpenGL jako atrybut wierzcholka.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void addDepth(float depth)` | Dodaje nowa wartosc glebokosci do bufora. |
| `void clear()` | Czysci bufor. |
| `float *depths() const` | Zwraca wskaznik na poczatek danych (alias dla `data()`). |
| `float *data() const` | Zwraca wskaznik na surowe dane bufora. |
| `int depthCount() const` | Zwraca liczbe wartosci w buforze (alias dla `count()`). |
| `int count() const` | Zwraca liczbe wartosci. |
| `int size() const` | Zwraca liczbe wartosci. |
# # # Zmienne prywatne

-   `m_buffer`: Obiekt `DataBuffer<float>`, kt�ry przechowuje dane glebokosci.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: Uzywa `DataBuffer` jako wewnetrznego kontenera.
-   W obecnym kodzie jest uzywana w `Painter`, ale funkcjonalnosc zwiazana z buforem glebi jest wykomentowana lub nie w pelni zaimplementowana (`WITH_DEPTH_BUFFER`).

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `graphics` sluzy jako centralny punkt dla wczesnych deklaracji (forward declarations) i definicji typ�w (`typedef`) zwiazanych z systemem graficznym. Jego gl�wnym celem jest unikanie zaleznosci cyklicznych miedzy plikami nagl�wkowymi i minimalizowanie liczby dolaczanych plik�w.
# # Wczesne deklaracje (Forward Declarations)

Plik deklaruje istnienie nastepujacych klas, co pozwala na uzywanie wskaznik�w i referencji do nich bez potrzeby dolaczania ich pelnych definicji:

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
# # Definicje typ�w (Typedefs)

Plik definiuje aliasy dla inteligentnych wskaznik�w (`shared_object_ptr`) do klas graficznych, co ulatwia ich uzycie i poprawia czytelnosc kodu.

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
# # Zaleznosci i powiazania

-   `framework/global.h`: Dolacza podstawowe definicje i typy, w tym `stdext::shared_object_ptr`.
-   `framework/graphics/glutil.h`: Dolacza nagl�wki OpenGL/GLES.
-   Ten plik jest intensywnie uzywany w calym module graficznym i w innych modulach, kt�re wchodza w interakcje z grafika (np. `UI`).

---
# ?? coordsbuffer.cpp
# # Opis og�lny

Plik `coordsbuffer.cpp` zawiera implementacje metod klasy `CoordsBuffer`, kt�ra jest buforem na dane geometryczne do renderowania.
# # Klasa `CoordsBuffer`
# # # `CoordsBuffer::CoordsBuffer()`

Konstruktor. Inicjalizuje dwa wewnetrzne bufory: `m_vertexArray` (dla wsp�lrzednych pozycji) i `m_textureCoordArray` (dla wsp�lrzednych tekstury).
# # # `void CoordsBuffer::addBoudingRect(const Rect& dest, int innerLineWidth)`

Dodaje geometrie czterech prostokat�w, kt�re razem tworza ramke (border) wewnatrz podanego prostokata `dest` o grubosci `innerLineWidth`.
# # # `void CoordsBuffer::addRepeatedRects(const Rect& dest, const Rect& src)`

Wypelnia prostokat docelowy (`dest`) powtarzajacym sie wzorem z tekstury (`src`). Dzieli obszar `dest` na mniejsze prostokaty o rozmiarze `src` i dodaje je do bufora, odpowiednio przycinajac wsp�lrzedne tekstury na krawedziach.
# # # `void CoordsBuffer::unlock(bool clear)`

Metoda zwiazana z wewnetrznym mechanizmem "blokowania" bufora. Kiedy bufor jest zablokowany (`m_locked`), kazda operacja dodawania geometrii powoduje jego odblokowanie. Odblokowanie tworzy kopie wewnetrznych `VertexArray`, aby zapobiec modyfikacji danych, kt�re mogly juz zostac przeslane do VBO. Jesli `clear` jest `true`, zamiast kopiowania tworzone sa nowe, puste `VertexArray`.
# # # `Rect CoordsBuffer::getTextureRect()`

Przechodzi przez wszystkie wsp�lrzedne tekstury w buforze, aby znalezc minimalny i maksymalny punkt, a nastepnie zwraca prostokat ograniczajacy (bounding box) dla uzywanego fragmentu tekstury.
# # Zaleznosci i powiazania

-   `framework/graphics/coordsbuffer.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Potencjalnie do funkcji zwiazanych z grafika.
-   Jest uzywana do budowania geometrii przez klasy takie jak `UIWidget`, a nastepnie konsumowana przez `DrawQueue` i `Painter` do renderowania.

---
# ?? drawcache.cpp
# # Opis og�lny

Plik `drawcache.cpp` implementuje klase `DrawCache`, kt�ra jest kluczowym elementem systemu optymalizacji renderowania. Jej zadaniem jest grupowanie (batching) operacji rysowania, kt�re uzywaja tej samej tekstury (atlasu), aby zminimalizowac liczbe wywolan rysujacych (draw calls) do OpenGL.
# # Zmienne globalne
# # # `g_drawCache`

Globalna instancja `DrawCache`, uzywana przez `DrawQueue` do buforowania operacji.

```cpp
DrawCache g_drawCache;
```
# # Klasa `DrawCache`
# # # `void DrawCache::draw()`
# # # # Opis semantyczny
Wykonuje zgrupowane operacje rysowania.
# # # # Dzialanie
1.  Upewnia sie, ze atlas tekstur jest odlaczony (`release()`).
2.  Jesli bufor nie jest pusty (`m_size > 0`), wywoluje `g_painter->drawCache()`, przekazujac jej wszystkie zebrane dane wierzcholk�w, wsp�lrzednych tekstur i kolor�w.
3.  Resetuje licznik `m_size` do zera.
# # # `void DrawCache::bind()` i `void DrawCache::release()`

Metody te zarzadzaja bindowaniem i zwalnianiem `FrameBuffer` atlasu. `bind()` jest wywolywane, gdy do atlasu musi zostac narysowana nowa tekstura. `release()` jest wywolywane przed wykonaniem `draw()`.
# # # Metody dodawania do bufora

-   **`addRect(const Rect& dest, const Color& color)`**: Dodaje prostokat wypelniony jednolitym kolorem. Wsp�lrzedne tekstury sa ustawiane na `(-10, -10)`, co jest sygnalem dla shadera, aby nie uzywal tekstury.
-   **`addTexturedRect(const Rect& dest, const Rect& src, const Color& color)`**: Dodaje teksturowany prostokat.
-   **`addCoords(CoordsBuffer& coords, const Color& color)`**: Dodaje geometrie z `CoordsBuffer` (bez tekstury).
-   **`addTexturedCoords(CoordsBuffer& coords, const Point& offset, const Color& color)`**: Dodaje geometrie z `CoordsBuffer` z tekstura. Przesuwa wsp�lrzedne tekstury o podany `offset`, kt�ry jest pozycja tekstury w atlasie.
# # # Metody pomocnicze (`addRectRaw`, `addColorRaw`)

Prywatne metody `inline` do szybkiego zapisu danych do wewnetrznych wektor�w (`m_destCoord`, `m_srcCoord`, `m_color`).
# # Zaleznosci i powiazania

-   `framework/graphics/drawcache.h`: Plik nagl�wkowy.
-   `framework/graphics/atlas.h`: Scisle wsp�lpracuje z `g_atlas` w celu bindowania i zwalniania bufora ramki atlasu.
-   `framework/graphics/painter.h`: Wywoluje `g_painter->drawCache()` do finalnego narysowania zgrupowanej geometrii.
-   Jest uzywana przez `DrawQueueItem`, aby spr�bowac zbuforowac operacje rysowania zamiast wykonywac ja natychmiast.

---
# ?? drawcache.h
# # Opis og�lny

Plik `drawcache.h` deklaruje klase `DrawCache`, kt�ra sluzy jako bufor dla operacji rysowania. Jest to mechanizm optymalizacyjny, kt�ry agreguje wiele malych operacji rysowania (np. prostokat�w) w jedno duze wywolanie, co znaczaco poprawia wydajnosc renderowania.
# # Klasa `DrawCache`
# # # Opis semantyczny
`DrawCache` przechowuje trzy duze, prealokowane wektory: na wsp�lrzedne wierzcholk�w (`m_destCoord`), wsp�lrzedne tekstur (`m_srcCoord`) i kolory (`m_color`). Metody `add...` dodaja dane do tych bufor�w. Gdy bufor jest pelny lub gdy operacja rysowania nie moze byc zbuforowana, metoda `draw()` jest wywolywana, aby opr�znic bufor i narysowac jego zawartosc za pomoca jednego wywolania `g_painter->drawCache()`.
# # # Stale

-   `MAX_SIZE`: Maksymalna liczba wierzcholk�w, jaka moze przechowac bufor (65536).
-   `HALF_MAX_SIZE`: Polowa maksymalnego rozmiaru, uzywana jako pr�g do opr�znienia bufora.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw()` | Rysuje zawartosc bufora na ekranie i go czysci. |
| `void bind()` | Bindowanie `FrameBuffer` atlasu (gdy trzeba do niego cos dorysowac). |
| `void release()` | Odpinanie `FrameBuffer` atlasu. |
| `bool hasSpace(int size)` | Sprawdza, czy w buforze jest wystarczajaco miejsca na `size` wierzcholk�w. |
| `inline int getSize()` | Zwraca aktualna liczbe wierzcholk�w w buforze. |
| `void addRect(...)` | Dodaje prostokat wypelniony kolorem. |
| `void addTexturedRect(...)` | Dodaje teksturowany prostokat. |
| `void addCoords(...)` | Dodaje geometrie z `CoordsBuffer` (bez tekstury). |
| `void addTexturedCoords(...)` | Dodaje geometrie z `CoordsBuffer` (z tekstura). |
# # # Zmienne prywatne

-   `m_destCoord`: Wektor na wsp�lrzedne docelowe (pozycji).
-   `m_srcCoord`: Wektor na wsp�lrzedne zr�dlowe (tekstury).
-   `m_color`: Wektor na kolory wierzcholk�w.
-   `m_bound`: Flaga wskazujaca, czy atlas jest zbindowany.
-   `m_size`: Aktualna liczba wierzcholk�w w buforze.
# # # Zmienne globalne

-   `g_drawCache`: Globalna instancja `DrawCache`.
# # Zaleznosci i powiazania

-   `framework/graphics/atlas.h`: Do zarzadzania atlasem tekstur.
-   `framework/graphics/coordsbuffer.h`: Do przyjmowania geometrii.
-   `framework/graphics/graphics.h`, `painter.h`: Do operacji renderowania.
-   Jest uzywana przez `DrawQueue`, aby grupowac operacje rysowania.

---
# ?? drawqueue.cpp
# # Opis og�lny

Plik `drawqueue.cpp` implementuje logike dla `DrawQueue` oraz poszczeg�lnych typ�w zadan rysowania (`DrawQueueItem`). Jest to centralny element systemu renderowania, kt�ry kolekcjonuje wszystkie operacje rysowania w jednej klatce, a nastepnie wykonuje je w odpowiedniej kolejnosci, z uwzglednieniem warunk�w takich jak przycinanie, przezroczystosc czy rotacja.
# # Zmienne globalne
# # # `g_drawQueue`

Globalny wskaznik na aktualnie aktywna kolejke rysowania. Watek logiki tworzy nowe instancje `DrawQueue`, wypelnia je i przypisuje do tego wskaznika, a watek renderowania je konsumuje.
# # Klasy `DrawQueueItem` (implementacje)

Kazda klasa dziedziczaca po `DrawQueueItem` implementuje dwie kluczowe metody:

-   **`draw()`**: Wykonuje faktyczna operacje rysowania za pomoca `g_painter`.
-   **`cache()`**: Pr�buje zoptymalizowac operacje, dodajac ja do `g_drawCache` zamiast rysowac natychmiast. Zwraca `true`, jesli keszowanie sie powiodlo.
# # # Przyklady implementacji:

-   **`DrawQueueItemTextureCoords::cache()`**:
    1.  Sprawdza, czy tekstura moze byc skeszowana.
    2.  Pobiera pozycje dla tekstury w atlasie za pomoca `g_atlas.cache()`.
    3.  Jesli tekstury nie bylo w atlasie (`drawNow == true`), rysuje ja do atlasu.
    4.  Jesli w `g_drawCache` jest miejsce, dodaje do niego geometrie z przesunietymi wsp�lrzednymi tekstury.

-   **`DrawQueueItemFilledRect::cache()`**:
    1.  Sprawdza, czy jest miejsce w `g_drawCache`.
    2.  Jesli tak, dodaje prostokat za pomoca `g_drawCache.addRect()`.

-   **`DrawQueueItemText::draw()`**: Wywoluje `g_text.drawText()`, kt�ra jest zoptymalizowana do renderowania tekstu.

-   **`DrawQueueCondition...::start()` i `end()`**: Implementuja zmiany stanu `g_painter` na poczatku i na koncu bloku warunkowego. Na przyklad `DrawQueueConditionClip` zmienia i przywraca prostokat przycinania.
# # Klasa `DrawQueue`
# # # `void DrawQueue::setFrameBuffer(...)`

Konfiguruje `DrawQueue` do renderowania do bufora ramki (off-screen). Ustawia docelowy i zr�dlowy prostokat oraz oblicza skalowanie, jesli rozmiar bufora przekracza `2048x2048`.
# # # `void DrawQueue::addText(...)` i `void DrawQueue::addColoredText(...)`

Tworza zadanie rysowania tekstu. Najpierw dodaja tekst do `g_text` (systemu keszujacego geometrie tekstu), uzyskujac hash, a nastepnie tworza odpowiedni `DrawQueueItemText`.
# # # `void DrawQueue::correctOutfit(...)`

Specjalna metoda do skalowania i pozycjonowania wielu `DrawQueueItem` (czesci stroju postaci), tak aby calosc zmiescila sie w podanym prostokacie docelowym, zachowujac proporcje.
# # # `void DrawQueue::draw(DrawType drawType)`
# # # # Opis semantyczny
Gl�wna metoda wykonujaca wszystkie zebrane zadania rysowania.
# # # # Dzialanie
1.  Okresla zakres zadan do narysowania na podstawie `drawType` (wszystkie, przed mapa, po mapie).
2.  Sortuje warunki (`m_conditions`) po ich pozycjach poczatkowych.
3.  Jesli ustawiono skalowanie, modyfikuje macierz projekcji `g_painter`.
4.  Iteruje po zadaniach w kolejce (`m_queue`):
    -   Przed kazdym zadaniem, aktywuje i dezaktywuje odpowiednie warunki (`start()`/`end()`).
    -   Pr�buje skeszowac zadanie za pomoca `item->cache()`.
    -   Jesli keszowanie sie nie powiedzie, opr�znia `g_drawCache` i pr�buje ponownie.
    -   Jesli ponowne keszowanie sie nie powiedzie, wykonuje `item->draw()`.
    -   Regularnie opr�znia `g_drawCache`, gdy osiagnie polowe pojemnosci.
5.  Po zakonczeniu petli, opr�znia `g_drawCache` i deaktywuje wszystkie pozostale warunki.
6.  Przywraca oryginalna macierz projekcji i stan `g_painter`.
# # Zaleznosci i powiazania

-   Scisle wsp�lpracuje z `g_painter`, `g_atlas`, `g_drawCache` i `g_text`, orkiestrujac proces renderowania.
-   Jest tworzona i wypelniana przez `UIManager` i inne moduly logiki gry.
-   Jest konsumowana przez `GraphicalApplication` w watku renderowania.

---
# ?? fontmanager.cpp
# # Opis og�lny

Plik `fontmanager.cpp` zawiera implementacje klasy `FontManager`, kt�ra jest singletonem (`g_fonts`) odpowiedzialnym za zarzadzanie wszystkimi fontami bitmapowymi w aplikacji.
# # Zmienne globalne
# # # `g_fonts`

Globalna instancja `FontManager`.

```cpp
FontManager g_fonts;
```
# # Klasa `FontManager`
# # # `FontManager::FontManager()`

Konstruktor. Inicjalizuje domyslny font (`m_defaultFont`) jako pusty obiekt `BitmapFont`, aby uniknac bled�w, gdy zaden font nie zostal jeszcze zaladowany.
# # # `void FontManager::terminate()`

Zwalnia wszystkie zaladowane fonty, czyszczac wektor `m_fonts` i resetujac wskaznik na domyslny font.
# # # `void FontManager::clearFonts()`

Czysci wszystkie zaladowane fonty i przywraca pusty font domyslny. Uzywane np. przy przeladowywaniu zasob�w.
# # # `void FontManager::importFont(std::string file)`
# # # # Opis semantyczny
Laduje definicje fontu z pliku `.otfont`. Metoda jest bezpieczna watkowo - jesli jest wywolana z innego watku niz graficzny, deleguje zadanie do `g_graphicsDispatcher`.
# # # # Dzialanie
1.  Rozwiazuje sciezke do pliku.
2.  Parsuje plik OTML.
3.  Odczytuje nazwe fontu z wezla `Font`.
4.  Sprawdza, czy font o tej nazwie juz nie istnieje.
5.  Tworzy nowy obiekt `BitmapFont` i wywoluje jego metode `load()`.
6.  Dodaje nowo zaladowany font do wektora `m_fonts`.
7.  Jesli font jest oznaczony jako domyslny (`default="true"`), ustawia go jako `m_defaultFont`.
# # # `bool FontManager::fontExists(const std::string& fontName)`

Sprawdza, czy font o podanej nazwie zostal juz zaladowany.
# # # `BitmapFontPtr FontManager::getFont(const std::string& fontName)`

Wyszukuje i zwraca wskaznik do fontu o podanej nazwie. Jesli font nie zostanie znaleziony, loguje blad i zwraca font domyslny, aby zapobiec awarii.
# # Zaleznosci i powiazania

-   `framework/graphics/fontmanager.h`: Plik nagl�wkowy.
-   `framework/graphics/atlas.h`: Posrednio, przez `BitmapFont`, kt�ry uzywa atlasu do cachowania.
-   `framework/core/eventdispatcher.h`: Uzywa `g_graphicsDispatcher` do zapewnienia bezpieczenstwa watkowego.
-   `framework/core/resourcemanager.h`: Do znajdowania i odczytywania plik�w `.otfont`.
-   `framework/otml/otml.h`: Do parsowania plik�w definicji font�w.
-   Jest uzywany przez `UIManager` i `UIWidget` do uzyskiwania dostepu do font�w potrzebnych do renderowania tekstu.

---
# ?? drawqueue.h
# # Opis og�lny

Plik `drawqueue.h` deklaruje hierarchie klas `DrawQueueItem` oraz klase `DrawQueue`, kt�re razem tworza system kolejkowania operacji rysowania. Jest to centralny mechanizm, kt�ry pozwala na zbieranie wszystkich polecen rysowania w jednej klatce, a nastepnie ich zoptymalizowane wykonanie.
# # Typ wyliczeniowy `DrawType`

Okresla, kt�ra czesc kolejki ma zostac narysowana. Uzywane do renderowania warstwowego (np. interfejs za mapa i przed mapa).

| Wartosc | Opis |
| :--- | :--- |
| `DRAW_ALL` | Rysuje cala kolejke. |
| `DRAW_BEFORE_MAP` | Rysuje zadania dodane przed `markMapPosition()`. |
| `DRAW_AFTER_MAP` | Rysuje zadania dodane po `markMapPosition()`. |
# # Hierarchia klas `DrawQueueItem`
# # # `struct DrawQueueItem` (baza)
Abstrakcyjna klasa bazowa dla wszystkich zadan w kolejce.

-   **`virtual void draw()`**: Metoda wirtualna do wykonania operacji rysowania.
-   **`virtual bool cache()`**: Metoda wirtualna do pr�by zbuforowania operacji w `DrawCache`.
# # # Klasy pochodne

Kazda klasa reprezentuje konkretna operacje rysowania:
-   `DrawQueueItemTexturedRect`: Rysowanie prostokata z tekstura.
-   `DrawQueueItemTextureCoords`: Rysowanie geometrii z `CoordsBuffer` z tekstura.
-   `DrawQueueItemColoredTextureCoords`: Rysowanie geometrii z tekstura i wieloma kolorami.
-   `DrawQueueItemImageWithShader`: Rysowanie geometrii z tekstura i niestandardowym shaderem.
-   `DrawQueueItemFilledRect`: Rysowanie wypelnionego prostokata.
-   `DrawQueueItemClearRect`: Czyszczenie prostokatnego obszaru.
-   `DrawQueueItemFillCoords`: Wypelnianie geometrii z `CoordsBuffer` kolorem.
-   `DrawQueueItemText`, `DrawQueueItemTextColored`: Rysowanie tekstu.
-   `DrawQueueItemLine`: Rysowanie linii.
# # Hierarchia klas `DrawQueueCondition`
# # # `struct DrawQueueCondition` (baza)
Abstrakcyjna klasa bazowa dla warunk�w modyfikujacych stan renderowania dla grupy zadan.

-   **`m_start`, `m_end`**: Indeksy w `DrawQueue` okreslajace zakres dzialania warunku.
-   **`virtual void start(DrawQueue*)`**: Metoda wywolywana przed pierwszym zadaniem objetym warunkiem.
-   **`virtual void end(DrawQueue*)`**: Metoda wywolywana po ostatnim zadaniu objetym warunkiem.
# # # Klasy pochodne

-   `DrawQueueConditionClip`: Ustawia prostokat przycinania (clipping).
-   `DrawQueueConditionRotation`: Stosuje transformacje rotacji.
-   `DrawQueueConditionMark`: Specjalny warunek do rysowania zaznaczenia (np. na przedmiotach).
# # Klasa `DrawQueue`
# # # Opis semantyczny
Gl�wna klasa zarzadzajaca kolejka. Przechowuje liste zadan (`m_queue`) i warunk�w (`m_conditions`). Dostarcza metody do dodawania r�znych operacji rysowania i do finalnego wykonania calej kolejki.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void draw(DrawType)` | Wykonuje wszystkie (lub czesc) operacje rysowania z kolejki. |
| `add...(...)` | Metody do dodawania r�znych typ�w `DrawQueueItem` do kolejki. |
| `setFrameBuffer(...)` | Konfiguruje renderowanie do bufora ramki. |
| `setOpacity(start, opacity)` | Stosuje przezroczystosc do zadan od indeksu `start`. |
| `setClip(start, clip)` | Dodaje warunek `DrawQueueConditionClip` dla zadan od `start`. |
# ?? framebuffer.cpp
# # Opis og�lny

Plik `framebuffer.cpp` zawiera implementacje klasy `FrameBuffer`, kt�ra jest opakowaniem (wrapperem) na obiekt bufora ramki (FBO) w OpenGL. Umozliwia renderowanie sceny do tekstury zamiast bezposrednio na ekran (tzw. off-screen rendering), co jest kluczowe dla efekt�w post-processingu, skalowania interfejsu i implementacji atlasu tekstur.
# # Zmienne globalne
# # # `uint FrameBuffer::boundFbo`

Statyczna zmienna czlonkowska, kt�ra sledzi ID aktualnie zwiazanego (aktywnego) FBO. Sluzy do optymalizacji poprzez unikanie zbednych wywolansk `glBindFramebuffer`, jesli ten sam FBO jest juz aktywny.

```cpp
uint FrameBuffer::boundFbo = 0;
```
# # Klasa `FrameBuffer`
# # # `FrameBuffer::FrameBuffer(bool withDepth)`

Konstruktor. Wywoluje `internalCreate()` w celu utworzenia zasob�w OpenGL.
-   **Parametr `withDepth`**: Jesli `true` i zdefiniowano `WITH_DEPTH_BUFFER`, tworzony jest r�wniez bufor glebi, co pozwala na testowanie glebi podczas renderowania do tego bufora.
# # # `FrameBuffer::~FrameBuffer()`

Destruktor. Zwalnia zasoby OpenGL (`glDeleteFramebuffers`, `glDeleteRenderbuffers`) w spos�b bezpieczny watkowo, dodajac zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`).
# # # `void FrameBuffer::resize(const Size& size)`
# # # # Opis semantyczny
Zmienia rozmiar bufora ramki. Tworzy nowa teksture o podanych wymiarach, kt�ra bedzie sluzyc jako "pl�tno" do rysowania.
# # # # Dzialanie
1.  Sprawdza, czy zmiana rozmiaru jest konieczna.
2.  Tworzy nowy obiekt `Texture` o podanym rozmiarze.
3.  Jesli bufor glebi jest wlaczony, alokuje dla niego pamiec (`glRenderbufferStorage`).
4.  Wiaze FBO, a nastepnie dolacza do niego nowa teksture jako bufor koloru (`glFramebufferTexture2D`) oraz opcjonalnie bufor glebi (`glFramebufferRenderbuffer`).
5.  Sprawdza status FBO (`glCheckFramebufferStatus`), aby upewnic sie, ze jest on kompletny i gotowy do uzycia.
# # # `void FrameBuffer::bind(const FrameBufferPtr& depthFramebuffer)`

Aktywuje bufor ramki jako cel renderowania. Wszystkie kolejne operacje rysowania beda kierowane do tekstury tego bufora.
-   Zapisuje i resetuje stan `Painter`.
-   Wywoluje `internalBind()`.
-   Ustawia rozdzielczosc `Painter` na rozmiar bufora.
# # # `void FrameBuffer::release()`

Deaktywuje bufor ramki i przywraca poprzedni cel renderowania (zazwyczaj bufor ekranu).
-   Wywoluje `internalRelease()`.
-   Przywraca poprzedni stan `Painter`.
# # # `void FrameBuffer::draw(...)`

Metody te sluza do rysowania *zawartosci* (tekstury) bufora ramki na aktualnie aktywnym celu renderowania.
-   `draw()`: Rysuje cala teksture.
-   `draw(const Rect& dest, const Rect& src)`: Rysuje fragment (`src`) tekstury w docelowym prostokacie (`dest`).
# # # `void FrameBuffer::doScreenshot(std::string fileName)`

Odczytuje zawartosc pikseli z bufora ramki za pomoca `glReadPixels`, a nastepnie w osobnym watku (`g_asyncDispatcher`) zapisuje je do pliku PNG, odwracajac obraz w osi Y (konwersja z ukladu wsp�lrzednych OpenGL).
# # # Metody `internal...`

-   `internalCreate()`: Generuje obiekty FBO i RBO.
-   `internalBind()` / `internalRelease()`: Bezposrednio wywoluja `glBindFramebuffer` i zarzadzaja statyczna zmienna `boundFbo`.
# # Zaleznosci i powiazania

-   `framework/graphics/framebuffer.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bled�w OpenGL i dostepu do `g_graphics`.
-   `framework/graphics/texture.h`: `FrameBuffer` uzywa obiektu `Texture` jako swojego bufora koloru.
-   `framework/platform/platformwindow.h`: Dostep do `g_window` (potencjalnie).
-   `framework/core/asyncdispatcher.h`: Uzywany do asynchronicznego zapisu zrzut�w ekranu.
-   Jest zarzadzana przez `FrameBufferManager`.

---
# ?? framebuffer.h
# # Opis og�lny

Plik `framebuffer.h` deklaruje klase `FrameBuffer`, kt�ra jest obiektowym interfejsem do zarzadzania buforami ramki (FBO) w OpenGL. Pozwala na renderowanie sceny do tekstury zamiast bezposrednio na ekran.
# # Klasa `FrameBuffer`
# # # Opis semantyczny
`FrameBuffer` enkapsuluje obiekt FBO z OpenGL oraz powiazana z nim teksture (jako bufor koloru) i opcjonalnie bufor glebi. Udostepnia metody do bindowania (aktywacji), zwalniania, zmiany rozmiaru i rysowania zawartosci bufora.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `FrameBuffer(bool withDepth = false)` | Konstruktor. |
| `virtual ~FrameBuffer()` | Destruktor. |
| `void resize(const Size& size)` | Zmienia rozmiar bufora i powiazanej tekstury. |
| `void bind(...)` | Ustawia ten bufor jako aktywny cel renderowania. |
| `void release()` | Przywraca poprzedni cel renderowania. |
| `void draw()` / `draw(const Rect& dest)` / `draw(...)` | Rysuje teksture tego bufora na aktualnie aktywnym celu. |
| `void setSmooth(bool enabled)` | Wlacza/wylacza wygladzanie (filtrowanie liniowe) dla tekstury bufora. |
| `TexturePtr getTexture()` | Zwraca wskaznik do tekstury, do kt�rej renderuje bufor. |
| `Size getSize()` | Zwraca rozmiar bufora. |
| `bool isSmooth()` | Zwraca stan wygladzania. |
| `uint getDepthRenderBuffer()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca ID bufora glebi. |
| `bool hasDepth()` | (Tylko z `WITH_DEPTH_BUFFER`) Zwraca `true`, jesli bufor posiada bufor glebi. |
| `std::vector<uint32_t> readPixels()` | Odczytuje zawartosc bufora do pamieci systemowej. |
| `void doScreenshot(std::string fileName)` | Zapisuje zawartosc bufora do pliku PNG. |
# # # Zmienne prywatne

-   `m_texture`: Wskaznik na obiekt `Texture` uzywany jako bufor koloru.
-   `m_fbo`: ID obiektu FBO w OpenGL.
-   `m_prevBoundFbo`: Przechowuje ID poprzednio aktywnego FBO, aby mozna bylo go przywr�cic.
-   `m_smooth`: Flaga wygladzania.
-   `m_depthRbo`, `m_depth`: (Tylko z `WITH_DEPTH_BUFFER`) ID bufora glebi i flaga jego istnienia.
-   `boundFbo`: Statyczna zmienna sledzaca globalnie aktywny FBO.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Definicje typ�w, np. `TexturePtr`.
-   `framework/graphics/texture.h`: Wymaga pelnej definicji `Texture`.
-   Jest tworzona i zarzadzana przez `FrameBufferManager`. Uzywana przez `Painter`, `Atlas` i w gl�wnej petli renderowania w `GraphicalApplication`.

---
# ?? framebuffermanager.cpp
# # Opis og�lny

Plik `framebuffermanager.cpp` zawiera implementacje klasy `FrameBufferManager`, kt�ra jest singletonem (`g_framebuffers`) odpowiedzialnym za tworzenie i zarzadzanie obiektami `FrameBuffer`.
# # Zmienne globalne
# # # `g_framebuffers`

Globalna instancja `FrameBufferManager`.

```cpp
FrameBufferManager g_framebuffers;
```
# # Klasa `FrameBufferManager`
# # # `void FrameBufferManager::init()`
# # # # Opis semantyczny
Inicjalizuje menedzera. Tworzy dwa predefiniowane, "tymczasowe" bufory ramki, kt�re moga byc uzywane przez r�zne czesci systemu do kr�tkotrwalych operacji renderowania poza ekranem, bez potrzeby tworzenia i niszczenia wlasnych bufor�w.

-   `m_temporaryFramebuffer`: Og�lnego przeznaczenia.
-   `m_drawQueueTemporaryFramebuffer`: Prawdopodobnie uzywany przez `DrawQueue` do specyficznych operacji.
# # # `void FrameBufferManager::terminate()`

Zwalnia wszystkie utworzone bufory ramki, w tym tymczasowe, czyszczac liste `m_framebuffers`.
# # # `FrameBufferPtr FrameBufferManager::createFrameBuffer(bool withDepth)`
# # # # Opis semantyczny
Metoda fabryczna do tworzenia nowych obiekt�w `FrameBuffer`.
# # # # Dzialanie
1.  Tworzy nowa instancje `FrameBuffer`, przekazujac flage `withDepth`.
2.  Dodaje nowo utworzony bufor do wewnetrznej listy `m_framebuffers` w celu sledzenia.
3.  Zwraca wskaznik na nowo utworzony obiekt.
# # Zaleznosci i powiazania

-   `framework/graphics/framebuffermanager.h`: Plik nagl�wkowy.
-   Klasa ta jest uzywana przez `Atlas` do tworzenia swoich "pl�cien" oraz przez `GraphicalApplication` do tworzenia bufor�w dla gl�wnej sceny i mapy.

---
# ?? graph.cpp
# # Opis og�lny

Plik `graph.cpp` implementuje klase `Graph`, kt�ra sluzy do wizualizacji danych w czasie rzeczywistym w formie prostego wykresu liniowego. Jest to narzedzie gl�wnie do cel�w debugowania i profilowania wydajnosci.
# # Zmienne globalne
# # # `g_graphs[GRAPH_LAST + 1]`

Globalna tablica instancji `Graph`, gdzie kazda instancja odpowiada za sledzenie i rysowanie innego parametru (np. czasu klatki, liczby wywolan rysujacych, op�znienia sieciowego).

```cpp
Graph g_graphs[GRAPH_LAST + 1] = {
    {"Total frame time"},
    // ... inne definicje
};
```
# # Klasa `Graph`
# # # `Graph::Graph(const std::string& name, size_t capacity)`

Konstruktor. Inicjalizuje wykres z podana nazwa i maksymalna liczba pr�bek do przechowywania.
# # # `void Graph::draw(const Rect& dest)`
# # # # Opis semantyczny
Rysuje wykres w podanym prostokacie ekranu. Metoda musi byc wywolywana z watku graficznego.
# # # # Dzialanie
1.  Rysuje tlo i ramke wykresu.
2.  Rysuje nazwe wykresu.
3.  Pobiera `elements` ostatnich pr�bek z `m_values` (tyle, ile zmiesci sie w `dest`).
4.  Znajduje minimalna i maksymalna wartosc w pobranym zakresie.
5.  Normalizuje wartosci i tworzy geometrie linii wykresu.
6.  Rysuje etykiety z wartoscia minimalna, maksymalna i ostatnia.
7.  Rysuje linie wykresu za pomoca `g_painter->drawLine()`.
# # # `void Graph::clear()`

Czysci wszystkie zebrane dane z wykresu.
# # # `void Graph::addValue(int value, bool ignoreSmallValues)`
# # # # Opis semantyczny
Dodaje nowa pr�bke danych do wykresu. Metoda jest bezpieczna watkowo dzieki uzyciu `std::mutex`.
# # # # Dzialanie
1.  Opcjonalnie ignoruje male, powtarzajace sie wartosci, aby wykres byl bardziej czytelny.
2.  Dodaje nowa wartosc na koniec kolejki `m_values`.
3.  Jesli kolejka przekracza pojemnosc, usuwa najstarsza wartosc.
# # Zaleznosci i powiazania

-   `framework/graphics/graph.h`: Plik nagl�wkowy.
-   `framework/graphics/painter.h`: Uzywa `g_painter` do rysowania.
-   `framework/graphics/textrender.h`: Uzywa `g_text` do rysowania etykiet.
-   `framework/core/eventdispatcher.h`: Uzywany do walidacji watku.
-   Jest uzywana w r�znych czesciach aplikacji (`GraphicalApplication`, `Protocol`) do zbierania danych o wydajnosci, kt�re sa nastepnie rysowane w gl�wnej petli renderowania.

---
# ?? graph.h
# # Opis og�lny

Plik `graph.h` deklaruje klase `Graph` oraz powiazane z nia typy wyliczeniowe. Jest to narzedzie do wizualizacji danych w czasie rzeczywistym, przeznaczone do debugowania i profilowania.
# # Typ wyliczeniowy `GraphType`

Definiuje stale dla r�znych typ�w wykres�w, kt�re moga byc sledzone w aplikacji.

| Nazwa | Opis |
| :--- | :--- |
| `GRAPH_TOTAL_FRAME_TIME` | Calkowity czas klatki. |
| `GRAPH_CPU_FRAME_TIME` | Czas renderowania po stronie CPU. |
| `GRAPH_GPU_CALLS` | Liczba wywolan do API graficznego. |
| `GRAPH_GPU_DRAWS` | Liczba operacji rysowania. |
| `GRAPH_PROCESSING_POLL` | Czas przetwarzania zdarzen w watku logiki. |
| `GRAPH_GRAPHICS_POLL` | Czas przetwarzania zdarzen w watku graficznym. |
| `GRAPH_DISPATCHER_EVENTS` | Liczba zdarzen w gl�wnym dyspozytorze. |
| `GRAPH_GRAPHICS_EVENTS` | Liczba zdarzen w dyspozytorze graficznym. |
| `GRAPH_LATENCY` | Op�znienie sieciowe (ping). |
# # Klasa `Graph`
# # # Opis semantyczny
Klasa `Graph` przechowuje kolejke (`std::deque`) ostatnich wartosci liczbowych i udostepnia metode do narysowania ich w postaci prostego wykresu liniowego. Jest bezpieczna watkowo przy dodawaniu wartosci.
# # # Stale

-   `MAX_CAPACITY`: Maksymalna liczba pr�bek, jaka moze przechowac wykres.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graph(...)` | Konstruktor. |
| `void draw(const Rect& dest)` | Rysuje wykres w podanym prostokacie. |
| `void clear()` | Czysci dane wykresu. |
| `void addValue(int value, bool ignoreSmallValues = false)` | Dodaje nowa wartosc do wykresu. |
# # # Zmienne prywatne

-   `m_name`: Nazwa wykresu, wyswietlana jako tytul.
-   `m_capacity`: Maksymalna liczba przechowywanych pr�bek.
-   `m_ignores`: Licznik ignorowanych malych wartosci.
-   `m_values`: Kolejka przechowujaca dane.
-   `m_mutex`: Mutex chroniacy dostep do `m_values`.
# # # Zmienne globalne

-   `g_graphs[GRAPH_LAST + 1]`: Globalna tablica, w kt�rej przechowywane sa instancje `Graph` dla kazdego typu z `GraphType`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uzywana przez `GraphicalApplication` do rysowania informacji debugowania. Dane sa do niej dodawane z r�znych czesci systemu, np. z petli gl�wnej, `Painter`, `EventDispatcher`, `Protocol`.

---
# ?? glutil.h
# # Opis og�lny

Plik `glutil.h` (GL Utility) jest plikiem nagl�wkowym, kt�rego jedynym zadaniem jest wlaczenie odpowiednich nagl�wk�w OpenGL, OpenGL ES, EGL lub GLEW, w zaleznosci od platformy i opcji kompilacji. Dziala jako centralny punkt dolaczania bibliotek graficznych, co upraszcza zarzadzanie zaleznosciami w innych plikach.
# # Logika warunkowego dolaczania

Plik uzywa dyrektyw preprocesora do wyboru odpowiednich nagl�wk�w:

1.  **Android lub Emscripten (`ANDROID` || `__EMSCRIPTEN__`)**:
    -   Dolaczane sa nagl�wki **OpenGL ES 2.0** (`<GLES2/gl2.h>`, `<GLES2/gl2ext.h>`) oraz **EGL** (`<EGL/egl.h>`, `<EGL/eglext.h>`). EGL jest interfejsem, kt�ry laczy API renderowania (jak OpenGL ES) z natywnym systemem okienkowym platformy.

2.  **Inne platformy z `OPENGL_ES`**:
    -   Podobnie jak wyzej, dolaczane sa nagl�wki OpenGL ES 2.0 i EGL. Definiowane sa r�wniez makra `GL_GLEXT_PROTOTYPES`, `EGL_EGL_PROTOTYPES`, aby zapewnic dostep do prototyp�w funkcji.

3.  **Domyslnie (Desktop - Windows/Linux/macOS)**:
    -   Dolaczana jest biblioteka **GLEW** (`<GL/glew.h>`). GLEW (OpenGL Extension Wrangler) jest biblioteka, kt�ra upraszcza zarzadzanie i ladowanie rozszerzen OpenGL, co jest konieczne na platformach desktopowych.
    -   Na systemach innych niz Windows, `GLEW_STATIC` jest definiowane, aby linkowac GLEW statycznie.
# # Zaleznosci i powiazania

-   Ten plik nie ma zaleznosci od innych plik�w projektu.
-   Jest dolaczany przez `framework/graphics/declarations.h`, co sprawia, ze definicje OpenGL sa dostepne we wszystkich plikach modulu graficznego.

---
# ?? graphics.cpp
# # Opis og�lny

Plik `graphics.cpp` zawiera implementacje klasy `Graphics`, kt�ra jest singletonem (`g_graphics`) odpowiedzialnym za inicjalizacje i zarzadzanie globalnym stanem silnika graficznego opartego na OpenGL.
# # Zmienne globalne
# # # `g_graphics`

Globalna instancja `Graphics`.

```cpp
Graphics g_graphics;
```
# # Klasa `Graphics`
# # # `Graphics::Graphics()`

Konstruktor. Inicjalizuje domyslna maksymalna wielkosc tekstury na `2048`.
# # # `void Graphics::init()`
# # # # Opis semantyczny
Gl�wna metoda inicjalizujaca. Uruchamia i konfiguruje kontekst OpenGL oraz inicjalizuje wszystkie pod-menedzery graficzne.
# # # # Dzialanie
1.  Odczytuje i zapisuje informacje o sterowniku graficznym (`GL_VENDOR`, `GL_RENDERER`, `GL_VERSION`, `GL_EXTENSIONS`) za pomoca `glGetString`.
2.  Loguje te informacje.
3.  **Na platformach desktopowych**:
    -   Sprawdza, czy wersja OpenGL jest co najmniej 2.0.
    -   Inicjalizuje GLEW (`glewInit()`).
    -   Sprawdza, czy dostepne sa rozszerzenia FBO (Framebuffer Object) i w razie potrzeby mapuje funkcje `...EXT` na standardowe nazwy.
4.  Wlacza globalnie mieszanie kolor�w (`glEnable(GL_BLEND)`).
5.  Pobiera maksymalny obslugiwany rozmiar tekstury z `GL_MAX_TEXTURE_SIZE`.
6.  (Opcjonalnie) Sprawdza wsparcie dla bufora glebi.
7.  Ustawia flage `m_ok` na `true`, sygnalizujac pomyslna inicjalizacje.
8.  Tworzy i bindowanie globalny obiekt `Painter`.
9.  Inicjalizuje menedzery: `g_textures`, `g_framebuffers`, `g_atlas`, `g_text`.
# # # `void Graphics::terminate()`

Zwalnia zasoby w odwrotnej kolejnosci do inicjalizacji, wywolujac `terminate()` na wszystkich pod-menedzerach oraz niszczac obiekt `Painter`.
# # # `void Graphics::resize(const Size& size)`

Aktualizuje rozmiar viewportu. Ustawia `m_viewportSize` i przekazuje nowy rozmiar do `g_painter`, kt�ry z kolei aktualizuje macierz projekcji i `glViewport`.
# # # `void Graphics::checkForError(...)`

Metoda pomocnicza, kt�ra sprawdza bledy OpenGL za pomoca `glGetError()`. Jesli wystapil blad, loguje go wraz z informacja o funkcji, pliku i numerze linii, w kt�rej zostal wykryty. W trybie debugowania powoduje to blad krytyczny.
# # Zaleznosci i powiazania

-   `framework/graphics/graphics.h`: Plik nagl�wkowy.
-   `fontmanager.h`, `painter.h`, `atlas.h`, `texturemanager.h`, `framebuffermanager.h`, `textrender.h`: Inicjalizuje i zarzadza tymi kluczowymi komponentami graficznymi.
-   `framework/platform/platformwindow.h`: Posrednio, poprzez `g_window`, od kt�rego zalezy kontekst OpenGL.
-   Jest to centralna klasa-menedzer dla calego podsystemu graficznego.

---
# ?? graphics.h
# # Opis og�lny

Plik `graphics.h` deklaruje interfejs klasy `Graphics`, kt�ra jest singletonem (`g_graphics`) zarzadzajacym globalnym stanem i inicjalizacja silnika graficznego.
# # Klasa `Graphics`
# # # Opis semantyczny
`Graphics` pelni role gl�wnego menedzera podsystemu graficznego. Odpowiada za inicjalizacje OpenGL/GLES, odpytywanie o mozliwosci sprzetowe (wersja, rozszerzenia, maksymalny rozmiar tekstury) oraz za zarzadzanie cyklem zycia innych menedzer�w graficznych, takich jak `Painter`, `TextureManager` czy `FontManager`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Graphics()` | Konstruktor. |
| `void init()` | Inicjalizuje silnik graficzny (kontekst OpenGL, menedzery). |
| `void terminate()` | Zwalnia zasoby silnika graficznego. |
| `void resize(const Size& size)` | Aktualizuje rozmiar viewportu. |
| `void checkDepthSupport()`| Sprawdza wsparcie dla bufora glebi. |
| `int getMaxTextureSize()` | Zwraca maksymalny obslugiwany rozmiar tekstury. |
| `const Size& getViewportSize()` | Zwraca aktualny rozmiar viewportu (okna/ekranu). |
| `std::string getVendor()` | Zwraca nazwe producenta karty graficznej. |
| `std::string getRenderer()` | Zwraca nazwe modelu karty graficznej/sterownika. |
| `std::string getVersion()` | Zwraca wersje OpenGL. |
| `std::string getExtensions()` | Zwraca liste dostepnych rozszerzen OpenGL. |
| `bool ok()` | Zwraca `true`, jesli inicjalizacja grafiki przebiegla pomyslnie. |
| `void checkForError(...)` | Sprawdza i loguje bledy OpenGL. |
# # # Zmienne prywatne

-   `m_viewportSize`: Aktualny rozmiar obszaru renderowania.
-   `m_vendor`, `m_renderer`, `m_version`, `m_extensions`: Informacje o sterowniku graficznym.
-   `m_maxTextureSize`: Maksymalny rozmiar tekstury obslugiwany przez sprzet.
-   `m_ok`: Flaga pomyslnej inicjalizacji.
# # # Zmienne globalne

-   `g_graphics`: Globalna instancja `Graphics`.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`, `painter.h`: Podstawowe deklaracje i klasa `Painter`.
-   Jest oznaczona jako `@bindsingleton g_graphics`, co udostepnia jej metody (np. `getVendor`) w Lua.
-   Jest inicjalizowana i zamykana przez `GraphicalApplication`.

---
# ?? image.cpp
# # Opis og�lny

Plik `image.cpp` zawiera implementacje klasy `Image`, kt�ra reprezentuje obraz rastrowy w pamieci RAM. Jest to podstawowa klasa do ladowania, manipulowania i zapisywania danych obraz�w, zanim zostana one przeslane do pamieci karty graficznej jako tekstury.
# # Klasa `Image`
# # # `Image::Image(const Size& size, int bpp, uint8 *pixels)`

Konstruktor. Tworzy obiekt `Image` o podanych wymiarach i glebi bitowej (bpp - bits per pixel). Opcjonalnie kopiuje dane pikseli z podanego bufora.
# # # `ImagePtr Image::load(std::string file)`

Statyczna metoda fabryczna do ladowania obrazu z pliku. Obecnie obsluguje tylko format PNG, wywolujac `loadPNG`.
# # # `ImagePtr Image::loadPNG(...)`

Statyczne metody do ladowania obrazu w formacie PNG z pliku lub z bufora w pamieci. Uzywaja funkcji `load_apng` z `apngloader.cpp` do parsowania danych.
# # # `void Image::savePNG(const std::string& fileName)`

Zapisuje obraz do pliku w formacie PNG, uzywajac funkcji `save_png` z `apngloader.cpp`.
# # # `void Image::blit(const Point& dest, const ImagePtr& other)`

Kopiuje piksele z innego obrazu (`other`) do tego obrazu w podane miejsce (`dest`). Kopiowanie odbywa sie z uwzglednieniem przezroczystosci - piksele w pelni przezroczyste w obrazie zr�dlowym nie sa kopiowane.
# # # `void Image::paste(const ImagePtr& other)`

Naklada inny obraz (`other`) na ten obraz, zastepujac istniejace piksele. Nie uwzglednia przezroczystosci.
# # # `ImagePtr Image::upscale()`

Tworzy i zwraca nowy obraz, kt�ry jest dwukrotnie wiekszy od oryginalnego. Kazdy piksel z obrazu zr�dlowego jest powielany do bloku 2x2 w obrazie docelowym (skalowanie metoda "najblizszego sasiada").
# # # `bool Image::nextMipmap()`

Generuje nastepny, mniejszy poziom mipmapy na podstawie biezacych danych pikseli. Oblicza srednia z bloku 2x2 pikseli, aby stworzyc jeden piksel dla mniejszego obrazu. Jest to prosta implementacja filtrowania biliniowego. Zwraca `false`, gdy obraz osiagnie rozmiar 1x1.
# # # `ImagePtr Image::fromQRCode(const std::string& code, int border)`

Statyczna metoda fabryczna, kt�ra generuje obraz kodu QR na podstawie podanego tekstu, uzywajac biblioteki `qrcodegen`.
# # Zaleznosci i powiazania

-   `framework/graphics/image.h`: Plik nagl�wkowy.
-   `framework/core/resourcemanager.h`: Do otwierania i odczytywania plik�w obraz�w.
-   `framework/graphics/apngloader.h`: Do obslugi formatu PNG/APNG.
-   `framework/util/qrcodegen.h`: Do generowania kod�w QR.
-   Obiekty `Image` sa zazwyczaj kr�tkotrwale - istnieja od momentu zaladowania z pliku do momentu utworzenia z nich obiektu `Texture` i przeslania danych do GPU.

---
# ?? hardwarebuffer.h
# # Opis og�lny

Plik `hardwarebuffer.h` deklaruje klase `HardwareBuffer`, kt�ra jest opakowaniem na sprzetowe bufory wierzcholk�w (Vertex Buffer Objects - VBO) w OpenGL. Umozliwia przechowywanie danych geometrycznych (np. wsp�lrzednych wierzcholk�w) w pamieci karty graficznej w celu uzyskania wysokiej wydajnosci renderowania.
# # Klasa `HardwareBuffer`
# # # Opis semantyczny
`HardwareBuffer` enkapsuluje ID bufora VBO w OpenGL i dostarcza podstawowe metody do jego obslugi: bindowania, odpinania i zapisu danych. Uzycie VBO jest znacznie wydajniejsze niz przesylanie danych wierzcholk�w z pamieci RAM do GPU w kazdej klatce.
# # # Typy wyliczeniowe (Enums)

-   **`enum Type`**: Okresla typ bufora.
    -   `VertexBuffer` (`GL_ARRAY_BUFFER`): Przechowuje atrybuty wierzcholk�w (np. pozycje, kolory, wsp�lrzedne tekstur).
    -   `IndexBuffer` (`GL_ELEMENT_ARRAY_BUFFER`): Przechowuje indeksy wierzcholk�w (nieuzywane w tym kodzie).
-   **`enum UsagePattern`**: Wskaz�wka dla sterownika OpenGL, jak dane beda uzywane.
    -   `StreamDraw` (`GL_STREAM_DRAW`): Dane zmieniane czesto, uzywane rzadko.
    -   `StaticDraw` (`GL_STATIC_DRAW`): Dane ustawiane raz, uzywane czesto.
    -   `DynamicDraw` (`GL_DYNAMIC_DRAW`): Dane zmieniane i uzywane czesto.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HardwareBuffer(Type type)` | Konstruktor, tworzy nowy obiekt bufora w OpenGL (`glGenBuffers`). |
| `~HardwareBuffer()` | Destruktor, zwalnia obiekt bufora (`glDeleteBuffers`). |
| `void bind()` | Bindowanie (aktywuje) bufor w kontekscie OpenGL (`glBindBuffer`). |
| `static void unbind(Type type)` | Odpina jakikolwiek bufor danego typu. |
| `void write(...)` | Kopiuje dane z pamieci RAM do bufora w pamieci GPU (`glBufferData`). |
# # # Zmienne prywatne

-   `m_type`: Typ bufora (`VertexBuffer` lub `IndexBuffer`).
-   `m_id`: ID (uchwyt) bufora w OpenGL.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Zawiera `glutil.h` z definicjami OpenGL.
-   Jest uzywana przez `VertexArray` (w `coordsbuffer.h`) do opcjonalnego keszowania geometrii na GPU.
-   `Painter` uzywa `HardwareBuffer` do ustawiania atrybut�w wierzcholk�w podczas rysowania.

---
# ?? image.h
# # Opis og�lny

Plik `image.h` deklaruje klase `Image`, kt�ra reprezentuje obraz rastrowy przechowywany w pamieci systemowej (RAM). Jest to podstawowa struktura danych do manipulacji pikselami przed ich wyslaniem do karty graficznej jako tekstura.
# # Klasa `Image`
# # # Opis semantyczny
`Image` to kontener na surowe dane pikseli. Przechowuje wymiary obrazu, liczbe bit�w na piksel oraz sam bufor pikseli. Udostepnia metody do ladowania obraz�w z plik�w, zapisywania ich, a takze do podstawowych operacji graficznych, takich jak kopiowanie fragment�w (`blit`), generowanie mipmap czy skalowanie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Image(...)` | Konstruktor. |
| `static ImagePtr load(...)` | Statyczna metoda fabryczna do ladowania obrazu z pliku (obecnie tylko PNG). |
| `static ImagePtr loadPNG(...)` | Laduje obraz PNG z pliku lub bufora w pamieci. |
| `void savePNG(...)` | Zapisuje obraz do pliku w formacie PNG. |
| `void blit(...)` | Kopiuje inny obraz na ten obraz z uwzglednieniem przezroczystosci. |
| `void paste(...)` | Naklada inny obraz na ten obraz, zastepujac piksele. |
| `ImagePtr upscale()` | Zwraca nowa, dwukrotnie wieksza wersje obrazu. |
| `void resize(...)` | Zmienia rozmiar obrazu, realokujac bufor pikseli. |
| `bool nextMipmap()` | Generuje kolejny poziom mipmapy, zmniejszajac obraz o polowe. |
| `void setPixel(...)` | Ustawia kolor pojedynczego piksela. |
| `std::vector<uint8>& getPixels()` | Zwraca referencje do wektora pikseli. |
| `uint8* getPixelData()` | Zwraca surowy wskaznik na dane pikseli. |
| `int getPixelCount()` | Zwraca liczbe pikseli. |
| `const Size& getSize()` | Zwraca wymiary obrazu. |
| `int getBpp()` | Zwraca liczbe bajt�w na piksel. |
| `static ImagePtr fromQRCode(...)` | Tworzy obraz z kodu QR. |
# # # Zmienne prywatne

-   `m_pixels`: Wektor przechowujacy dane pikseli.
-   `m_size`: Wymiary obrazu.
-   `m_bpp`: Liczba bajt�w na piksel.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/util/databuffer.h`: Potencjalnie, chociaz tutaj uzywa `std::vector`.
-   Jest uzywana przez `Texture` i `AnimatedTexture` jako zr�dlo danych pikseli podczas tworzenia tekstur.
-   Wykorzystywana przez `PlatformWindow` do ladowania ikon i kursor�w.

---
# ?? framebuffermanager.h
# # Opis og�lny

Plik `framebuffermanager.h` deklaruje klase `FrameBufferManager`, kt�ra jest singletonem (`g_framebuffers`) sluzacym do zarzadzania i tworzenia obiekt�w `FrameBuffer`.
# # Klasa `FrameBufferManager`
# # # Opis semantyczny
`FrameBufferManager` pelni role fabryki i menedzera dla obiekt�w `FrameBuffer`. Upraszcza ich tworzenie i zarzadzanie cyklem zycia. Udostepnia r�wniez dwa predefiniowane, "tymczasowe" bufory, kt�re moga byc uzywane w calym systemie do kr�tkotrwalych operacji renderowania poza ekranem, co pozwala uniknac kosztownego tworzenia i niszczenia FBO.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedzera i tworzy tymczasowe bufory ramki. |
| `void terminate()` | Zwalnia wszystkie zarzadzane bufory ramki. |
| `void clear()` | (Brak implementacji) Prawdopodobnie miala sluzyc do zwolnienia wszystkich bufor�w poza tymczasowymi. |
| `FrameBufferPtr createFrameBuffer(bool withDepth = false)` | Metoda fabryczna tworzaca i zwracajaca nowy obiekt `FrameBuffer`. |
| `const FrameBufferPtr& getTemporaryFrameBuffer()` | Zwraca wskaznik do pierwszego tymczasowego bufora. |
| `const FrameBufferPtr& getDrawQueueTemporaryFrameBuffer()` | Zwraca wskaznik do drugiego tymczasowego bufora, prawdopodobnie uzywanego przez `DrawQueue`. |
# # # Zmienne chronione

-   `m_temporaryFramebuffer`: Pierwszy tymczasowy `FrameBuffer`.
-   `m_drawQueueTemporaryFramebuffer`: Drugi tymczasowy `FrameBuffer`.
-   `m_framebuffers`: Wektor przechowujacy wskazniki do wszystkich utworzonych (i niezwolnionych) bufor�w ramki. |
# # # Zmienne globalne

-   `g_framebuffers`: Globalna instancja `FrameBufferManager`.
# # Zaleznosci i powiazania

-   `framework/graphics/framebuffer.h`: Deklaracja klasy `FrameBuffer`.
-   Jest to kluczowy komponent, od kt�rego zaleza inne czesci systemu graficznego, takie jak `Atlas` i `GraphicalApplication`, kt�re potrzebuja tworzyc wlasne bufory ramki.

---
# ?? painter.h
# # Opis og�lny

Plik `painter.h` deklaruje klase `Painter`, kt�ra jest centralnym interfejsem do wszystkich operacji rysowania w 2D. Abstrakcjonuje ona niskopoziomowe wywolania OpenGL, dostarczajac prostsze API do rysowania prostokat�w, tekstur, linii i zarzadzania stanem renderowania.
# # Klasa `Painter`
# # # Opis semantyczny
`Painter` dziala jak maszyna stan�w. Przechowuje aktualny stan renderowania, taki jak macierze transformacji, kolor, tryb mieszania, aktywny shader, tekstura, itp. Kazda operacja rysowania jest wykonywana w kontekscie tego stanu. `Painter` zarzadza r�wniez wlasnymi, domyslnymi programami shader�w do podstawowych operacji.
# # # Typy wyliczeniowe (Enums)

-   `BlendEquation`: Okresla, jak kolory sa mieszane (np. dodawanie, odejmowanie).
-   `CompositionMode`: Definiuje predefiniowane tryby mieszania (`glBlendFunc`), np. normalne (z przezroczystoscia), addytywne, mnozenie.
-   `DepthFunc`: Okresla funkcje testu glebi.
-   `DrawMode`: Okresla prymityw do rysowania (tr�jkaty, paski tr�jkat�w).
# # # Struktura `PainterState`

Przechowuje pelny stan `Painter`, co pozwala na jego zapisywanie i przywracanie.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Zarzadzanie stanem** | |
| `resetState()` | Przywraca wszystkie ustawienia do wartosci domyslnych. |
| `saveState()` / `restoreSavedState()` | Zapisuje/przywraca stan na wewnetrznym stosie. |
| `setTransformMatrix(...)`, `setProjectionMatrix(...)`, ... | Ustawiaja poszczeg�lne elementy stanu (macierze, tryb mieszania, etc.). |
| `scale()`, `translate()`, `rotate()` | Modyfikuja biezaca macierz transformacji. |
| **Operacje rysowania** | |
| `clear(const Color& color)` | Czysci caly bufor ramki. |
| `drawCoords(...)` | Niskopoziomowa metoda rysujaca geometrie z `CoordsBuffer`. |
| `drawFilledRect(const Rect& dest)` | Rysuje wypelniony prostokat. |
| `drawTexturedRect(...)` | Rysuje prostokat z tekstura. |
| `drawText(...)` | Rysuje tekst (przez `TextRender`). |
| `drawLine(...)` | Rysuje linie. |
| `drawCache(...)` | Rysuje dane zbuforowane w `DrawCache`. |
| **Gettery** | |
| `getTransformMatrix()`, `getColor()`, `getClipRect()`, ... | Zwracaja aktualne wartosci stanu. |
| `draws()`, `calls()` | Zwracaja statystyki renderowania dla biezacej klatki. |
# # # Zmienne chronione/prywatne

-   `m_transformMatrix`, `m_projectionMatrix`, ...: Zmienne przechowujace aktualny stan.
-   `m_transformMatrixStack`: Stos do zapisywania macierzy transformacji.
-   `m_olderStates`: Stos do zapisywania pelnego stanu `PainterState`.
-   `m_draw...Program`: Wskazniki na domyslne programy shader�w.
# # # Zmienne globalne

-   `g_painter`: Globalny wskaznik na instancje `Painter`.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`, `coordsbuffer.h`, `paintershaderprogram.h`, `texture.h`, `colorarray.h`, `drawqueue.h`: Deklaracje typ�w, z kt�rymi `Painter` wsp�lpracuje.
-   Jest to centralny komponent renderujacy, uzywany bezposrednio lub posrednio przez `DrawQueue`, `UIWidget`, `TextRender` i inne.

---
# ?? painter.cpp
# # Opis og�lny

Plik `painter.cpp` zawiera implementacje klasy `Painter`, kt�ra jest sercem silnika renderujacego. Odpowiada za bezposrednia komunikacje z API graficznym (OpenGL) w celu rysowania prymityw�w 2D.
# # Zmienne globalne
# # # `g_painter`

Globalny wskaznik na jedyna instancje `Painter`. Jest inicjalizowany w `Graphics::init()`.

```cpp
Painter* g_painter = nullptr;
```
# # Klasa `Painter`
# # # `Painter::Painter()`

Konstruktor. Inicjalizuje domyslne wartosci stanu, takie jak macierze, kolory i tryby mieszania. Co najwazniejsze, tworzy i kompiluje zestaw domyslnych program�w shader�w, kt�re sa uzywane do podstawowych operacji rysowania:
-   `m_drawTexturedProgram`: Do rysowania tekstur.
-   `m_drawSolidColorProgram`: Do rysowania jednolitych kolor�w.
-   `m_drawSolidColorOnTextureProgram`: Do rysowania jednolitego koloru na wierzchu tekstury.
-   `m_drawOutfitLayersProgram`: Specjalny shader do rysowania stroj�w postaci z kolorowaniem.
-   `m_drawNewProgram`: Shader uzywany przez `DrawCache` do zoptymalizowanego rysowania wsadowego.
-   `m_drawTextProgram`, `m_drawLineProgram`: Specjalne shadery do rysowania tekstu i linii.
# # # `void Painter::bind()` i `void Painter::unbind()`

Metody wywolywane na poczatku i na koncu cyklu zycia `Painter`. `bind()` wlacza podstawowe atrybuty wierzcholk�w, kt�re sa zawsze aktywne.
# # # `void Painter::resetState()`

Przywraca wszystkie parametry `Painter` (kolor, macierze, tryby mieszania itp.) do ich wartosci domyslnych.
# # # `void Painter::saveState()` i `void Painter::restoreSavedState()`

Implementuja mechanizm stosu do zapisywania i przywracania stanu renderowania. Pozwala to na tymczasowa zmiane stanu (np. ustawienie przycinania) i latwy powr�t do poprzedniego stanu.
# # # Metody `updateGl...()`

Prywatne metody pomocnicze (`updateGlTexture`, `updateGlCompositionMode`, `updateGlClipRect` itd.), kt�re aplikuja zmiany stanu `Painter` do rzeczywistego stanu OpenGL. Sa wywolywane, gdy odpowiednia wlasciwosc `Painter` (np. `m_compositionMode`) ulega zmianie.
# # # `void Painter::setResolution(const Size& resolution)`

Aktualizuje rozdzielczosc renderowania. Najwazniejsza czescia jest przeliczenie macierzy projekcji (`m_projectionMatrix`), kt�ra mapuje wsp�lrzedne w pikselach na znormalizowane wsp�lrzedne urzadzenia OpenGL (-1 do 1).
# # # `void Painter::drawCoords(...)`

Niskopoziomowa metoda, kt�ra jest podstawa wiekszosci operacji rysowania.
1.  Bindowanie i konfiguruje odpowiedni program shadera.
2.  Przekazuje do shadera uniformy (macierze, kolor, czas itp.).
3.  Ustawia wskazniki na dane atrybut�w wierzcholk�w (pozycja, wsp�lrzedne tekstury, kolor).
4.  Wywoluje `glDrawArrays` w celu narysowania geometrii.
5.  Zlicza statystyki (`m_draws`, `m_calls`).
# # # Metody `draw...Rect(...)` i `draw...Coords(...)`

Wysokopoziomowe metody rysujace, kt�re przygotowuja `CoordsBuffer` z odpowiednia geometria, a nastepnie wywoluja `drawCoords` do jej narysowania.
# # # `void Painter::drawCache(...)`

Specjalna, zoptymalizowana metoda do rysowania duzej liczby wierzcholk�w na raz. Uzywa dedykowanego shadera (`m_drawNewProgram`), kt�ry pobiera pozycje, wsp�lrzedne tekstury i kolor jako osobne atrybuty dla kazdego wierzcholka.
# # Zaleznosci i powiazania

-   Jest to klasa niskiego poziomu, kt�ra bezposrednio zalezy od API graficznego (OpenGL/GLES/GLEW).
-   `framework/graphics/shaders/shaders.h`: Zawiera kod zr�dlowy domyslnych shader�w.
-   Wsp�lpracuje z `Texture`, `CoordsBuffer`, `ShaderProgram`, `DrawCache`, `TextRender` i innymi komponentami graficznymi.
-   Jest uzywana przez `DrawQueue` do wykonywania wszystkich operacji rysowania.

---
# ?? hardwarebuffer.cpp
# # Opis og�lny

Plik `hardwarebuffer.cpp` zawiera implementacje klasy `HardwareBuffer`, kt�ra jest opakowaniem na bufory VBO (Vertex Buffer Object) w OpenGL.
# # Klasa `HardwareBuffer`
# # # `HardwareBuffer::HardwareBuffer(Type type)`

Konstruktor.
-   **Parametr `type`**: Okresla, czy ma to byc bufor na wierzcholki (`VertexBuffer`) czy indeksy (`IndexBuffer`).
-   **Dzialanie**:
    1.  Zapamietuje typ bufora.
    2.  Wywoluje `glGenBuffers(1, &m_id)` w celu wygenerowania nowego, unikalnego ID dla bufora w kontekscie OpenGL.
    3.  Sprawdza, czy operacja sie powiodla; w przeciwnym razie konczy aplikacje bledem krytycznym.
# # # `HardwareBuffer::~HardwareBuffer()`

Destruktor.
-   **Dzialanie**:
    1.  Zwalnia zas�b OpenGL w spos�b bezpieczny watkowo.
    2.  Zamiast bezposrednio wywolywac `glDeleteBuffers`, dodaje zadanie do kolejki dyspozytora graficznego (`g_graphicsDispatcher`). Gwarantuje to, ze operacja usuniecia zostanie wykonana w watku, kt�ry ma aktywny kontekst OpenGL, nawet jesli destruktor jest wywolywany z innego watku.
# # Zaleznosci i powiazania

-   `framework/graphics/hardwarebuffer.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bled�w OpenGL.
-   `framework/core/application.h`, `eventdispatcher.h`, `logger.h`: Do walidacji, planowania zdarzen i logowania.
-   Jest uzywana przez `VertexArray` (w `coordsbuffer.h`) do przechowywania danych geometrycznych w pamieci karty graficznej, co znacznie przyspiesza renderowanie.

---
# ?? paintershaderprogram.cpp
# # Opis og�lny

Plik `paintershaderprogram.cpp` zawiera implementacje klasy `PainterShaderProgram`, kt�ra jest specjalizacja `ShaderProgram`. Jest ona dostosowana do wsp�lpracy z klasa `Painter`, udostepniajac standardowy zestaw uniform�w i atrybut�w uzywanych w procesie renderowania 2D.
# # Klasa `PainterShaderProgram`
# # # `PainterShaderProgram::PainterShaderProgram(const std::string& name)`

Konstruktor. Wywoluje konstruktor klasy bazowej i inicjalizuje dodatkowe zmienne, takie jak `m_startTime`, kt�ry jest uzywany do animacji opartych na czasie w shaderach.
# # # `void PainterShaderProgram::setupUniforms()`
# # # # Opis semantyczny
Wirtualna metoda, kt�ra po zlinkowaniu programu shadera wyszukuje lokalizacje standardowych uniform�w (`u_TransformMatrix`, `u_ProjectionMatrix`, `u_Color`, `u_Tex0` itd.) i przypisuje im domyslne wartosci.
# # # `bool PainterShaderProgram::link()`

Przeslania metode z `ShaderProgram`.
1.  Ustawia `m_startTime`.
2.  Wiaze standardowe lokalizacje atrybut�w (`VERTEX_ATTR`, `TEXCOORD_ATTR`, etc.) z ich nazwami w shaderze.
3.  Wywoluje `ShaderProgram::link()`.
4.  Jesli linkowanie sie powiedzie, bindowanie program i wywoluje `setupUniforms()`.
# # # Metody `set...()`

Sa to metody do ustawiania wartosci uniform�w. Kazda z nich:
1.  Sprawdza, czy nowa wartosc r�zni sie od aktualnie przechowywanej, aby uniknac zbednych wywolan `glUniform...`.
2.  Bindowanie program shadera (`bind()`).
3.  Ustawia nowa wartosc uniformu w OpenGL.
4.  Aktualizuje przechowywana wartosc.

-   `setTransformMatrix`, `setProjectionMatrix`, `setTextureMatrix`: Ustawiaja macierze.
-   `setColor`: Ustawia gl�wny kolor.
-   `setMatrixColor`: Ustawia macierz kolor�w (dla shadera stroj�w).
-   `setResolution`: Ustawia rozdzielczosc (przydatne do efekt�w zaleznych od pikseli).
-   ... i inne.
# # # `void PainterShaderProgram::updateTime()`

Aktualizuje uniform `u_Time`, przekazujac do shadera czas, jaki uplynal od jego utworzenia. Pozwala to na tworzenie animowanych efekt�w w shaderach.
# # # `void PainterShaderProgram::addMultiTexture(...)` i `void PainterShaderProgram::bindMultiTextures()`

Metody do obslugi dodatkowych tekstur (multi-texturing). `addMultiTexture` laduje teksture i dodaje ja do listy. `bindMultiTextures` aktywuje te tekstury na kolejnych jednostkach teksturujacych (od `GL_TEXTURE1` wzwyz), aby mogly byc uzywane w shaderze.
# # Zaleznosci i powiazania

-   `framework/graphics/paintershaderprogram.h`: Plik nagl�wkowy.
-   `framework/graphics/painter.h`: Scisle wsp�lpracuje z `Painter`, kt�ry ustawia jej uniformy.
-   `framework/graphics/texture.h`, `texturemanager.h`: Do ladowania i zarzadzania dodatkowymi teksturami.
-   `framework/core/clock.h`: Do sledzenia czasu dla animacji.

---
# ?? paintershaderprogram.h
# # Opis og�lny

Plik `paintershaderprogram.h` deklaruje klase `PainterShaderProgram`, kt�ra jest wyspecjalizowana wersja `ShaderProgram`, dostosowana do potrzeb `Painter`. Definiuje ona standardowy zestaw uniform�w i atrybut�w uzywanych w shaderach 2D.
# # Klasa `PainterShaderProgram`
# # # Opis semantyczny
`PainterShaderProgram` dziedziczy po `ShaderProgram` i dodaje do niej warstwe abstrakcji specyficzna dla `Painter`. Zamiast odwolywac sie do uniform�w po nazwach (stringach), udostepnia dedykowane metody `set...()`, kt�re operuja na predefiniowanych, zbuforowanych lokalizacjach. Upraszcza to kod `Painter` i potencjalnie zwieksza wydajnosc.
# # # Typy wyliczeniowe (Enums)

Definiuje stale dla lokalizacji standardowych atrybut�w i uniform�w, co pozwala na ich efektywne buforowanie.

-   **Atrybuty**: `VERTEX_ATTR`, `TEXCOORD_ATTR`, ...
-   **Uniformy**: `PROJECTION_MATRIX_UNIFORM`, `TEXTURE_MATRIX_UNIFORM`, `COLOR_UNIFORM`, `TEX0_UNIFORM`, ...
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PainterShaderProgram(...)`| Konstruktor. |
| `bool link()` | Przeslania metode bazowa, aby dodatkowo zmapowac standardowe atrybuty i uniformy. |
| `setTransformMatrix(...)` | Ustawia macierz transformacji. |
| `setProjectionMatrix(...)`| Ustawia macierz projekcji. |
| `setTextureMatrix(...)` | Ustawia macierz tekstury. |
| `setColor(...)` | Ustawia gl�wny kolor. |
| `setMatrixColor(...)` | Ustawia macierz kolor�w (dla shadera stroj�w). |
| `setDepth(...)` | Ustawia wartosc glebi. |
| `setResolution(...)` | Ustawia rozdzielczosc renderowania. |
| `setOffset(...)` | Ustawia przesuniecie (offset). |
| `updateTime()` | Aktualizuje uniform czasu. |
| `addMultiTexture(...)` | Dodaje dodatkowa teksture do shadera. |
| `bindMultiTextures()` | Bindowanie wszystkie dodatkowe tekstury. |
| `clearMultiTextures()` | Czysci liste dodatkowych tekstur. |
| `enableColorMatrix()` | Wlacza tryb macierzy kolor�w (dla shadera stroj�w). |
# # # Zmienne prywatne

-   `m_startTime`: Czas utworzenia shadera.
-   `m_color`, `m_depth`, `m_transformMatrix`, ...: Przechowuja aktualne wartosci uniform�w, aby uniknac zbednych wywolan `glUniform...`.
-   `m_multiTextures`: Wektor dodatkowych tekstur.
-   `m_useColorMatrix`: Flaga wskazujaca, czy `u_Color` jest macierza 4x4.
# # Zaleznosci i powiazania

-   `framework/graphics/shaderprogram.h`: Klasa bazowa.
-   `framework/graphics/coordsbuffer.h`: Posrednio, poprzez `Painter`.
-   Jest uzywana przez `Painter` jako podstawa dla wszystkich operacji rysowania opartych na shaderach.

---
# ?? shader.cpp
# # Opis og�lny

Plik `shader.cpp` zawiera implementacje klasy `Shader`, kt�ra jest opakowaniem na pojedynczy obiekt shadera w OpenGL (np. shader wierzcholk�w lub shader fragment�w).
# # Klasa `Shader`
# # # `Shader::Shader(Shader::ShaderType shaderType)`

Konstruktor.
-   **Parametr `shaderType`**: Okresla, czy tworzony jest shader wierzcholk�w (`Vertex`) czy fragment�w (`Fragment`).
-   **Dzialanie**: Wywoluje `glCreateShader` z odpowiednim typem, aby utworzyc obiekt shadera w sterowniku graficznym. W przypadku bledu, konczy aplikacje.
# # # `Shader::~Shader()`

Destruktor. Zwalnia zas�b shadera w OpenGL, wywolujac `glDeleteShader`.
# # # `bool Shader::compileSourceCode(const std::string& sourceCode)`
# # # # Opis semantyczny
Kompiluje kod zr�dlowy shadera.
# # # # Dzialanie
1.  Dla OpenGL ES, dodaje na poczatku kodu dyrektywe `precision highp float;`.
2.  Przekazuje kod zr�dlowy do sterownika za pomoca `glShaderSource`.
3.  Kompiluje shader za pomoca `glCompileShader`.
4.  Sprawdza status kompilacji za pomoca `glGetShaderiv`.
5.  Zwraca `true` w przypadku sukcesu, `false` w przeciwnym razie.
# # # `bool Shader::compileSourceFile(const std::string& sourceFile)`

Laduje kod zr�dlowy z pliku za pomoca `g_resources`, a nastepnie wywoluje `compileSourceCode`.
# # # `std::string Shader::log()`

Pobiera i zwraca logi kompilatora shadera (`glGetShaderInfoLog`), kt�re zawieraja informacje o bledach lub ostrzezeniach.
# # Zaleznosci i powiazania

-   `framework/graphics/shader.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do dostepu do funkcji OpenGL.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   `framework/core/resourcemanager.h`: Do ladowania shader�w z plik�w.
-   Obiekty `Shader` sa tworzone i zarzadzane przez `ShaderProgram` (lub `PainterShaderProgram`), kt�ry nastepnie linkuje je w kompletny program shadera.

---
# ?? shadermanager.h
# # Opis og�lny

Plik `shadermanager.h` deklaruje klase `ShaderManager`, kt�ra jest singletonem (`g_shaders`) odpowiedzialnym za zarzadzanie niestandardowymi programami shader�w tworzonymi w skryptach Lua.
# # Klasa `ShaderManager`
# # # Opis semantyczny
`ShaderManager` dziala jako repozytorium dla `PainterShaderProgram` tworzonych dynamicznie. Przechowuje je w mapie pod unikalnymi nazwami, co pozwala na ich p�zniejsze pobieranie i uzywanie w trakcie renderowania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedzera. |
| `void terminate()` | Czysci i zwalnia wszystkie zaladowane shadery. |
| `void createShader(...)` | Tworzy, kompiluje i linkuje nowy `PainterShaderProgram` z podanego kodu zr�dlowego (lub plik�w). Zapisuje go pod dana nazwa. |
| `void createOutfitShader(...)` | Skr�t do `createShader` z wlaczona opcja macierzy kolor�w, specjalnie dla shader�w stroj�w. |
| `void addTexture(...)` | Dodaje dodatkowa teksture do istniejacego programu shadera. |
| `PainterShaderProgramPtr getShader(...)` | Wyszukuje i zwraca wskaznik do programu shadera o podanej nazwie. |
# # # Zmienne prywatne

-   `m_shaders`: Mapa (`std::unordered_map`) przechowujaca wszystkie niestandardowe programy shader�w.
# # # Zmienne globalne

-   `g_shaders`: Globalna instancja `ShaderManager`.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`, `paintershaderprogram.h`: Deklaracje klas shader�w.
-   Jest oznaczona jako `@bindsingleton g_shaders`, co udostepnia jej API (`createShader`, `addTexture`) w skryptach Lua.
-   Jest uzywana przez `UIWidget` (w `uiwidgetimage.cpp`) do rysowania obraz�w z niestandardowymi shaderami.
-   Wszystkie operacje tworzenia i modyfikacji shader�w sa delegowane do watku graficznego za pomoca `g_graphicsDispatcher`, aby zapewnic bezpieczenstwo watkowe.

---
# ?? shadermanager.cpp
# # Opis og�lny

Plik `shadermanager.cpp` zawiera implementacje klasy `ShaderManager`, kt�ra zarzadza niestandardowymi programami shader�w.
# # Zmienne globalne
# # # `g_shaders`

Globalna instancja `ShaderManager`.

```cpp
ShaderManager g_shaders;
```
# # Klasa `ShaderManager`
# # # `void ShaderManager::init()`

Inicjalizuje menedzera. W obecnej implementacji wywoluje `PainterShaderProgram::release()`, aby upewnic sie, ze zaden shader nie jest aktywny.
# # # `void ShaderManager::terminate()`

Czysci mape `m_shaders`, co powoduje zwolnienie wszystkich niestandardowych program�w shader�w.
# # # `void ShaderManager::createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix)`
# # # # Opis semantyczny
Tworzy nowy program shadera. Metoda jest asynchroniczna - dodaje zadanie do dyspozytora graficznego.
# # # # Dzialanie
1.  Sprawdza, czy podane stringi `vertex` i `fragment` sa kodem zr�dlowym (zawieraja znak nowej linii) czy sciezkami do plik�w.
2.  Jesli sa to sciezki, odczytuje zawartosc plik�w za pomoca `g_resources`.
3.  Dodaje do `g_graphicsDispatcher` zadanie (lambda), kt�re:
    -   Wywoluje `PainterShaderProgram::create` w celu skompilowania i zlinkowania shadera.
    -   Jesli operacja sie powiedzie, dodaje nowo utworzony program do mapy `m_shaders`.
# # # `void ShaderManager::addTexture(const std::string& name, const std::string& file)`

Dodaje dodatkowa teksture do istniejacego shadera. Podobnie jak `createShader`, operacja jest wykonywana asynchronicznie w watku graficznym.
# # # `PainterShaderProgramPtr ShaderManager::getShader(const std::string& name)`

Wyszukuje i zwraca program shadera o podanej nazwie. Ta metoda musi byc wywolywana z watku graficznego, co jest zapewnione przez `VALIDATE_GRAPHICS_THREAD()`.
# # Zaleznosci i powiazania

-   `framework/graphics/shadermanager.h`: Plik nagl�wkowy.
-   `framework/graphics/paintershaderprogram.h`: Do tworzenia obiekt�w shader�w.
-   `framework/core/resourcemanager.h`: Do ladowania kodu shader�w z plik�w.
-   `framework/core/eventdispatcher.h`: Do zapewnienia, ze operacje na OpenGL sa wykonywane w watku graficznym.

---
# ?? shader.h
# # Opis og�lny

Plik `shader.h` deklaruje klase `Shader`, kt�ra reprezentuje pojedynczy, skompilowany obiekt shadera w OpenGL (np. shader wierzcholk�w lub fragment�w), ale jeszcze nie zlinkowany w pelny program.
# # Klasa `Shader`
# # # Opis semantyczny
`Shader` jest niskopoziomowym opakowaniem na ID obiektu shadera w OpenGL. Jego gl�wnym zadaniem jest przyjecie kodu zr�dlowego, skompilowanie go i przechowanie wyniku. Obiekty tej klasy sa nastepnie laczone w `ShaderProgram`.
# # # Typ wyliczeniowy `ShaderType`

-   `Vertex`: Oznacza shader wierzcholk�w (`GL_VERTEX_SHADER`).
-   `Fragment`: Oznacza shader fragment�w/pikseli (`GL_FRAGMENT_SHADER`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Shader(ShaderType shaderType)` | Konstruktor, tworzy obiekt shadera w OpenGL. |
| `~Shader()` | Destruktor, zwalnia obiekt shadera. |
| `bool compileSourceCode(...)` | Kompiluje shader z podanego kodu zr�dlowego. |
| `bool compileSourceFile(...)` | Laduje kod z pliku i go kompiluje. |
| `std::string log()` | Zwraca logi kompilatora shadera. |
| `uint getShaderId()` | Zwraca ID obiektu shadera w OpenGL. |
| `ShaderType getShaderType()` | Zwraca typ shadera. |
# # # Zmienne prywatne

-   `m_shaderId`: ID obiektu shadera w OpenGL.
-   `m_shaderType`: Typ shadera.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   Jest tworzona i uzywana przez `ShaderProgram` w procesie budowania kompletnego programu shadera.

---
# ?? textrender.cpp
# # Opis og�lny

Plik `textrender.cpp` implementuje klase `TextRender`, kt�ra jest systemem do optymalizacji renderowania tekstu. Dziala jako globalny cache dla geometrii tekstu, aby uniknac ponownego obliczania pozycji glif�w w kazdej klatce dla tekst�w, kt�re sie nie zmieniaja.
# # Zmienne globalne
# # # `g_text`

Globalna instancja `TextRender`.

```cpp
TextRender g_text;
```
# # Klasa `TextRender`
# # # Opis semantyczny
`TextRender` przechowuje mape (`m_cache`), w kt�rej kluczem jest hash wygenerowany na podstawie tresci tekstu, jego rozmiaru, wyr�wnania i fontu. Wartoscia jest obiekt `TextRenderCache`, kt�ry przechowuje `CoordsBuffer` z gotowa geometria tekstu. Przy pierwszym zadaniu narysowania danego tekstu, geometria jest obliczana i zapisywana w cache. Przy kolejnych zadaniach, uzywana jest juz istniejaca geometria. System posiada r�wniez mechanizm czyszczenia nieuzywanych wpis�w z cache.
# # # `void TextRender::init()` i `void TextRender::terminate()`

Metody inicjalizujace i zwalniajace cache.
# # # `void TextRender::poll()`

Metoda wywolywana okresowo. Jej zadaniem jest czyszczenie cache z wpis�w, kt�re nie byly uzywane od pewnego czasu. Implementuje prosty mechanizm LRU (Least Recently Used) oparty na czasie ostatniego uzycia (`lastUse`).
# # # `uint64_t TextRender::addText(...)`

Generuje unikalny hash dla kombinacji (font, tekst, rozmiar, wyr�wnanie) i tworzy dla niego wpis w cache, jesli jeszcze nie istnieje. Zwraca wygenerowany hash.
# # # `void TextRender::drawText(...)`

Wysokopoziomowa metoda do rysowania tekstu. Najpierw wywoluje `addText`, aby uzyskac/stworzyc wpis w cache, a nastepnie wywoluje druga wersje `drawText` z hashem.
# # # `void TextRender::drawText(const Point& pos, uint64_t hash, ...)`

Gl�wna metoda rysujaca.
1.  Znajduje wpis w cache na podstawie hasha.
2.  Jesli wpis jest nowy (`it->font` nie jest `nullptr`), wywoluje `font->calculateDrawTextCoords`, aby wygenerowac geometrie, keszuje ja w `CoordsBuffer` (`it->coords.cache()`) i zwalnia referencje do fontu i tekstu, aby oszczedzac pamiec.
3.  Wywoluje `g_painter->drawText`, przekazujac mu gotowy `CoordsBuffer` z geometria.
4.  Obsluguje r�wniez rysowanie cienia.
# # # `void TextRender::drawColoredText(...)`

Dziala analogicznie do `drawText`, ale wywoluje `g_painter->drawText` w wersji dla tekstu wielokolorowego.
# # Zaleznosci i powiazania

-   `framework/graphics/textrender.h`: Plik nagl�wkowy.
-   `framework/graphics/painter.h`: Uzywa `g_painter` do finalnego rysowania.
-   `framework/core/eventdispatcher.h`: Do walidacji watku.
-   Jest uzywana przez `DrawQueueItemText` do renderowania tekstu.

---
# ?? shaderprogram.cpp
# # Opis og�lny

Plik `shaderprogram.cpp` zawiera implementacje klasy `ShaderProgram`, kt�ra jest podstawowym obiektem do zarzadzania programami shader�w w OpenGL.
# # Zmienne globalne
# # # `uint ShaderProgram::m_currentProgram`

Statyczna zmienna czlonkowska, kt�ra przechowuje ID aktualnie aktywnego (zbindowanego) programu shadera. Sluzy do unikania zbednych wywolan `glUseProgram`, jesli ten sam program jest juz aktywny.
# # Klasa `ShaderProgram`
# # # `ShaderProgram::ShaderProgram(const std::string& name)`

Konstruktor. Inicjalizuje nazwe, ustawia flage `m_linked` na `false` i tworzy nowy, pusty obiekt programu shadera w OpenGL za pomoca `glCreateProgram()`.
# # # `ShaderProgram::~ShaderProgram()`

Destruktor. Zwalnia zas�b programu shadera, wywolujac `glDeleteProgram()`.
# # # `PainterShaderProgramPtr ShaderProgram::create(...)`

Statyczna metoda fabryczna, kt�ra tworzy i konfiguruje `PainterShaderProgram`. Jest to gl�wny spos�b tworzenia shader�w w tym frameworku.
# # # # Dzialanie
1.  Tworzy nowy obiekt `PainterShaderProgram`.
2.  Dodaje i kompiluje shadery wierzcholk�w i fragment�w.
3.  Opcjonalnie wlacza tryb macierzy kolor�w.
4.  Linkuje program.
5.  W przypadku bled�w kompilacji lub linkowania, loguje szczeg�lowe informacje i zwraca `nullptr`.
# # # `bool ShaderProgram::addShader(...)`

Dolacza wczesniej skompilowany obiekt `Shader` do programu za pomoca `glAttachShader`.
# # # `bool ShaderProgram::addShaderFromSourceCode(...)` i `addShaderFromSourceFile(...)`

Metody pomocnicze, kt�re tworza obiekt `Shader`, kompiluja go z kodu zr�dlowego lub pliku, a nastepnie dodaja do programu.
# # # `bool ShaderProgram::link()`
# # # # Opis semantyczny
Linkuje wszystkie dolaczone shadery w jeden wykonywalny program.
# # # # Dzialanie
1.  Wywoluje `glLinkProgram()`.
2.  Sprawdza status linkowania za pomoca `glGetProgramiv`.
3.  Jesli wystapi blad, pobiera i loguje szczeg�lowy komunikat bledu z `glGetProgramInfoLog`.
4.  Zwraca `true` w przypadku sukcesu.
# # # `bool ShaderProgram::bind()`

Aktywuje program shadera w potoku renderowania OpenGL za pomoca `glUseProgram`. Dzieki `m_currentProgram`, faktyczne wywolanie `glUseProgram` nastepuje tylko wtedy, gdy zmieniany jest program.
# # # `void ShaderProgram::release()`

Deaktywuje jakikolwiek aktywny program shadera (`glUseProgram(0)`).
# # # Metody `...Location(...)` i `set...Value(...)`

Implementuja interfejs do pracy z atrybutami i uniformami w shaderze, opakowujac odpowiednie funkcje OpenGL (`glGetAttribLocation`, `glBindAttribLocation`, `glGetUniformLocation`, `glUniform...`, `glVertexAttrib...`).
# # Zaleznosci i powiazania

-   `framework/graphics/shaderprogram.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do sprawdzania bled�w i dostepu do informacji o sterowniku.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasa bazowa dla `PainterShaderProgram`.
-   Jest zarzadzana przez `ShaderManager`.

---
# ?? texture.cpp
# # Opis og�lny

Plik `texture.cpp` zawiera implementacje klasy `Texture`, kt�ra jest obiektowym opakowaniem na teksture w OpenGL. Odpowiada za tworzenie, ladowanie danych, ustawianie parametr�w i zwalnianie zasob�w tekstury w pamieci karty graficznej.
# # Zmienne globalne
# # # `uint Texture::uniqueId`

Statyczny licznik uzywany do przypisywania unikalnego ID kazdej nowo utworzonej teksturze. Jest to przydatne do szybkiego por�wnywania tekstur.
# # Klasa `Texture`
# # # `Texture::Texture(...)`

Konstruktory.
-   **`Texture(const Size& size, ...)`**: Tworzy pusta teksture o podanych wymiarach.
-   **`Texture(const ImagePtr& image, ...)`**: Tworzy teksture na podstawie obiektu `Image`.
-   **Dzialanie**: Inicjalizuja pola, przypisuja unikalne ID i zwiekszaja globalny licznik tekstur w `g_stats`.
# # # `Texture::~Texture()`

Destruktor. Dodaje zadanie usuniecia tekstury z pamieci GPU do kolejki dyspozytora graficznego (`g_graphicsDispatcher`), co zapewnia bezpieczenstwo watkowe. Zmniejsza globalny licznik tekstur.
# # # `void Texture::replace(const ImagePtr& image)`

Zastepuje zawartosc tekstury nowym obrazem. Stara tekstura w OpenGL jest zwalniana, a nowa zostanie utworzona przy nastepnym wywolaniu `update()`.
# # # `void Texture::resize(const Size& size)`

Zmienia rozmiar istniejacej tekstury, ponownie alokujac dla niej pamiec w GPU za pomoca `glTexImage2D` z `nullptr` jako danymi pikseli.
# # # `void Texture::update()`
# # # # Opis semantyczny
Kluczowa metoda, kt�ra dba o to, aby obiekt tekstury w OpenGL byl poprawnie zainicjalizowany i skonfigurowany. Musi byc wywolywana przed pierwszym uzyciem tekstury.
# # # # Dzialanie
1.  **Jesli tekstura nie istnieje (`m_id == 0`)**:
    -   Generuje nowe ID tekstury (`glGenTextures`).
    -   Bindowanie teksture.
    -   Jesli `m_image` istnieje, przesyla jego dane pikseli do GPU za pomoca `setupPixels`, generujac mipmapy, jesli to wymagane. Nastepnie zwalnia `m_image`, aby oszczedzac RAM.
    -   Jesli nie ma obrazu, tworzy pusta teksture.
2.  **Jesli `m_needsUpdate` jest `true`**:
    -   Bindowanie teksture.
    -   Ustawia parametry zawijania (`setupWrap`).
    -   Ustawia parametry filtrowania (`setupFilters`).
    -   Aktualizuje macierz transformacji (`setupTranformMatrix`).
    -   Resetuje flage `m_needsUpdate`.
# # # `void Texture::setSmooth(bool smooth)` i `void Texture::setRepeat(bool repeat)`

Ustawiaja flagi, kt�re zostana zastosowane do parametr�w tekstury (`GL_TEXTURE_MIN/MAG_FILTER`, `GL_TEXTURE_WRAP_S/T`) podczas nastepnego wywolania `update()`.
# # # Metody `setup...()`

Prywatne metody pomocnicze, kt�re wywoluja odpowiednie funkcje OpenGL do konfiguracji tekstury:
-   `setupSize()`: Sprawdza, czy rozmiar nie przekracza limit�w GPU.
-   `setupWrap()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_WRAP_S/T`.
-   `setupFilters()`: Ustawia `glTexParameteri` dla `GL_TEXTURE_MIN/MAG_FILTER`.
-   `setupTranformMatrix()`: Oblicza macierz do transformacji wsp�lrzednych tekstury (np. w celu odwr�cenia jej w osi Y).
-   `setupPixels()`: Wywoluje `glTexImage2D` do przeslania danych pikseli.
# # Zaleznosci i powiazania

-   `framework/graphics/texture.h`: Plik nagl�wkowy.
-   `framework/graphics/graphics.h`: Do operacji OpenGL i sprawdzania limit�w.
-   `framework/graphics/image.h`: Uzywana jako zr�dlo danych pikseli.
-   Jest klasa bazowa dla `AnimatedTexture`.
-   Jest tworzona i zarzadzana przez `TextureManager`.

---
# ?? texture.h
# # Opis og�lny

Plik `texture.h` deklaruje klase `Texture`, kt�ra jest obiektowym interfejsem do zarzadzania teksturami w OpenGL.
# # Klasa `Texture`
# # # Opis semantyczny
`Texture` enkapsuluje ID tekstury w OpenGL oraz jej wlasciwosci, takie jak rozmiar, wygladzanie (filtrowanie), powtarzanie (wrapping) i mipmapy. Dostarcza metody do tworzenia tekstury z obiektu `Image` lub jako pustej tekstury (np. dla bufora ramki). Metoda `update()` jest kluczowa i synchronizuje stan obiektu C++ z rzeczywistym stanem tekstury w pamieci GPU.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Texture(...)` | Konstruktory. |
| `virtual ~Texture()` | Destruktor. |
| `virtual void replace(...)` | Zastepuje zawartosc tekstury nowym obrazem. |
| `void resize(...)` | Zmienia rozmiar tekstury. |
| `virtual void update()` | Tworzy lub aktualizuje parametry tekstury w OpenGL. |
| `virtual void setUpsideDown(...)` | Ustawia, czy tekstura ma byc odwr�cona. |
| `virtual void setSmooth(...)` | Ustawia wygladzanie (filtrowanie liniowe/najblizszego sasiada). |
| `virtual void setRepeat(...)` | Ustawia tryb powtarzania. |
| `virtual bool buildHardwareMipmaps()` | Wlacza generowanie mipmap przez GPU. |
| `uint getId()` | Zwraca ID tekstury w OpenGL. |
| `uint getUniqueId()` | Zwraca unikalne ID obiektu w aplikacji. |
| `const Size& getSize()` | Zwraca rozmiar tekstury. |
| `const Matrix3& getTransformMatrix()` | Zwraca macierz transformacji dla wsp�lrzednych tekstury. |
| `bool isEmpty()` | Sprawdza, czy tekstura jest pusta. |
| `bool canCache()` | Zwraca `true`, jesli teksture mozna umiescic w atlasie. |
| `virtual bool isAnimatedTexture()` | Zwraca `false` (przeslaniane przez `AnimatedTexture`). |
# # # Zmienne chronione

-   `m_id`: ID tekstury w OpenGL.
-   `m_uniqueId`: Unikalne ID w aplikacji.
-   `m_size`: Rozmiar tekstury.
-   `m_transformMatrix`: Macierz transformacji.
-   `m_hasMipmaps`, `m_smooth`, `m_upsideDown`, `m_repeat`, ...: Flagi stanu.
-   `m_image`: Wskaznik na `Image`, uzywany tylko podczas tworzenia tekstury.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Definicje typ�w, np. `ImagePtr`.
-   Jest klasa bazowa dla `AnimatedTexture`.
-   Jest tworzona i zarzadzana przez `TextureManager`.
-   Jest uzywana przez `Painter`, `FrameBuffer`, `UIWidget` i inne komponenty do rysowania.

---
# ?? texturemanager.cpp
# # Opis og�lny

Plik `texturemanager.cpp` zawiera implementacje klasy `TextureManager`, kt�ra jest singletonem (`g_textures`) odpowiedzialnym za zarzadzanie teksturami w aplikacji. Dziala jako cache, aby zapobiec wielokrotnemu ladowaniu tych samych tekstur z dysku.
# # Zmienne globalne
# # # `g_textures`

Globalna instancja `TextureManager`.

```cpp
TextureManager g_textures;
```
# # Klasa `TextureManager`
# # # `void TextureManager::init()` i `void TextureManager::terminate()`

Metody do inicjalizacji i zwalniania menedzera. `terminate()` czysci wszystkie zbuforowane tekstury.
# # # `void TextureManager::clearCache()`

Czysci wszystkie zbuforowane tekstury, w tym animowane.
# # # `void TextureManager::reload()`

Przeladowuje wszystkie zaladowane tekstury z ich oryginalnych plik�w. Jest to przydatne do "hot-reloading" zasob�w.
# # # `TexturePtr TextureManager::getTexture(const std::string& fileName)`
# # # # Opis semantyczny
Gl�wna metoda do pobierania tekstury. Dziala jak "get-or-load".
# # # # Dzialanie
1.  Sprawdza, czy tekstura o podanej nazwie (`fileName`) jest juz w cache (`m_textures`). Jesli tak, zwraca ja.
2.  Jesli nie, rozwiazuje pelna sciezke do pliku za pomoca `g_resources`.
3.  Ponownie sprawdza cache, tym razem z pelna sciezka.
4.  Jesli tekstury wciaz nie ma, pr�buje ja zaladowac z pliku:
    -   Odczytuje plik do strumienia w pamieci.
    -   Wywoluje `loadTexture()`, aby sparsowac dane (APNG) i utworzyc obiekt `Texture` lub `AnimatedTexture`.
5.  Jesli ladowanie sie powiedzie, dodaje nowa teksture do cache pod obiema nazwami (oryginalna i pelna sciezka) i zwraca ja.
6.  W przypadku bledu, loguje go i zwraca `nullptr`.
# # # `TexturePtr TextureManager::loadTexture(std::stringstream& file, const std::string& source)`

Metoda pomocnicza, kt�ra parsuje strumien danych APNG za pomoca `load_apng`.
-   Jesli plik zawiera jedna klatke, tworzy `Texture`.
-   Jesli plik zawiera wiele klatek, tworzy `AnimatedTexture`.
# # Zaleznosci i powiazania

-   `framework/graphics/texturemanager.h`: Plik nagl�wkowy.
-   `framework/graphics/animatedtexture.h`, `image.h`: Do tworzenia obiekt�w tekstur.
-   `framework/core/resourcemanager.h`: Do odczytywania plik�w tekstur.
-   `framework/graphics/apngloader.h`: Do parsowania formatu APNG.
-   Jest uzywana przez `UIWidget`, `BitmapFont` i inne komponenty, kt�re potrzebuja wyswietlac obrazy.

---
# ?? vertexarray.h
# # Opis og�lny

Plik `vertexarray.h` deklaruje klase `VertexArray`, kt�ra jest prostym, dynamicznym buforem na wsp�lrzedne wierzcholk�w (`float`). Sluzy do gromadzenia geometrii przed wyslaniem jej do renderowania.
# # Klasa `VertexArray`
# # # Opis semantyczny
`VertexArray` to opakowanie na `DataBuffer<float>`, zoptymalizowane do przechowywania par wsp�lrzednych (X, Y). Udostepnia metody do dodawania popularnych prymityw�w 2D (tr�jkaty, prostokaty) i moze opcjonalnie przeniesc swoje dane do sprzetowego bufora VBO (`HardwareBuffer`) w celu zwiekszenia wydajnosci.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `VertexArray()` | Konstruktor. |
| `~VertexArray()` | Destruktor, zwalnia `m_hardwareBuffer`. |
| `VertexArray(VertexArray& c)` | Konstruktor kopiujacy (kopiuje tylko dane z `m_buffer`, nie `m_hardwareBuffer`). |
| `void addVertex(float x, float y)` | Dodaje pojedynczy wierzcholek. |
| `void addTriangle(...)` | Dodaje trzy wierzcholki tworzace tr�jkat. |
| `void addRect(...)` | Dodaje szesc wierzcholk�w tworzacych dwa tr�jkaty (prostokat). |
| `void addQuad(...)` | Dodaje cztery wierzcholki tworzace czworokat (dla `TriangleStrip`). |
| `void clear()` | Czysci bufor. |
| `float *vertices() const` | Zwraca wskaznik na surowe dane. |
| `int vertexCount() const` | Zwraca liczbe wierzcholk�w. |
| `void cache()` | Kopiuje dane z bufora RAM do bufora VBO na karcie graficznej. |
| `bool isCached()` | Zwraca `true`, jesli dane zostaly skopiowane do VBO. |
| `HardwareBuffer* getHardwareCache()` | Zwraca wskaznik na obiekt `HardwareBuffer`. |
# # # Zmienne prywatne

-   `m_buffer`: Bufor `DataBuffer<float>` przechowujacy wsp�lrzedne.
-   `m_hardwareBuffer`: Wskaznik na opcjonalny bufor VBO.
# # Zaleznosci i powiazania

-   `framework/graphics/declarations.h`: Podstawowe deklaracje.
-   `framework/graphics/hardwarebuffer.h`: Do sprzetowego keszowania.
-   `framework/util/databuffer.h`: Uzywana jako wewnetrzny kontener.
-   Jest podstawowym skladnikiem `CoordsBuffer`, kt�ry uzywa dw�ch instancji `VertexArray` (jednej na pozycje, drugiej na wsp�lrzedne tekstur).

---
# ?? texturemanager.h
# # Opis og�lny

Plik `texturemanager.h` deklaruje klase `TextureManager`, kt�ra jest singletonem (`g_textures`) odpowiedzialnym za zarzadzanie (ladowanie, cachowanie, zwalnianie) teksturami w aplikacji.
# # Klasa `TextureManager`
# # # Opis semantyczny
`TextureManager` dziala jako centralne repozytorium tekstur. Gdy jakas czesc kodu prosi o teksture z pliku, menedzer najpierw sprawdza, czy nie zostala ona juz zaladowana. Jesli tak, zwraca istniejaca instancje. Jesli nie, laduje ja z dysku, zapisuje w swojej pamieci podrecznej (cache) i zwraca. Zapobiega to wielokrotnemu ladowaniu tych samych zasob�w i marnowaniu pamieci.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedzera. |
| `void terminate()` | Zwalnia wszystkie zaladowane tekstury. |
| `void clearCache()` | Czysci pamiec podreczna tekstur. |
| `void reload()` | Przeladowuje wszystkie tekstury z plik�w, umozliwiajac "hot-reloading". |
| `void preload(const std::string& fileName)` | Skr�t do `getTexture`, kt�ry laduje teksture do cache, ale nie zwraca jej. |
| `TexturePtr getTexture(const std::string& fileName)` | Pobiera teksture. Jesli nie ma jej w cache, laduje ja. |
| `TexturePtr loadTexture(...)` | Niskopoziomowa metoda do tworzenia tekstury ze strumienia danych. |
# # # Zmienne prywatne

-   `m_textures`: Mapa (`std::unordered_map`) przechowujaca zaladowane tekstury, gdzie kluczem jest nazwa pliku.
-   `m_animatedTextures`: Wektor przechowujacy wskazniki do animowanych tekstur, prawdopodobnie w celu ich aktualizacji.
-   `m_liveReloadEvent`: Wskaznik na zdarzenie, prawdopodobnie do implementacji "live reload".
# # Zaleznosci i powiazania

-   `framework/graphics/texture.h`: Definicja `Texture`.
-   `framework/core/declarations.h`: Deklaracje `ScheduledEventPtr`.
-   Jest to kluczowy menedzer w systemie graficznym, uzywany przez wszystkie komponenty, kt�re musza wyswietlac obrazy, takie jak `UIWidget` czy `BitmapFont`.

---
# ?? textrender.h
# # Opis og�lny

Plik `textrender.h` deklaruje klase `TextRender`, kt�ra jest systemem do optymalizacji renderowania tekstu. Dziala jako globalny cache dla geometrii tekstu.
# # Struktura `TextRenderCache`

Przechowuje wszystkie informacje potrzebne do narysowania tekstu, w tym gotowy `CoordsBuffer` z geometria.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `font` | `BitmapFontPtr` | Font uzyty do wygenerowania geometrii (zwalniany po pierwszym uzyciu). |
| `text` | `std::string` | Tekst (zwalniany po pierwszym uzyciu). |
| `size` | `Size` | Rozmiar obszaru, w kt�rym tekst ma byc rysowany. |
| `align` | `Fw::AlignmentFlag` | Wyr�wnanie tekstu. |
| `texture` | `TexturePtr` | Tekstura fontu. |
| `coords` | `CoordsBuffer` | Zbuforowana geometria tekstu. |
| `lastUse` | `ticks_t` | Czas ostatniego uzycia (do czyszczenia cache). |
# # Klasa `TextRender`
# # # Opis semantyczny
`TextRender` minimalizuje narzut na CPU zwiazany z obliczaniem pozycji poszczeg�lnych glif�w dla czesto wyswietlanych tekst�w. Zamiast przeliczac geometrie w kazdej klatce, robi to tylko raz, a nastepnie przechowuje wynik w cache.
# # # Stale

-   `INDEXES`: Liczba "kubelk�w" w hash mapie. Uzycie wielu map z osobnymi mutexami ma na celu zmniejszenie rywalizacji o zasoby w srodowisku wielowatkowym.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` / `terminate()` | Inicjalizuje i zwalnia system. |
| `void poll()` | Czysci cache z nieuzywanych wpis�w. |
| `uint64_t addText(...)` | Generuje hash dla tekstu i tworzy dla niego wpis w cache. |
| `void drawText(...)` | Rysuje tekst, uzywajac skeszowanej geometrii. |
| `void drawColoredText(...)` | Rysuje tekst wielokolorowy. |
# # # Zmienne prywatne

-   `m_cache[INDEXES]`: Tablica map, kt�ra przechowuje skeszowane dane.
-   `m_mutex[INDEXES]`: Tablica mutex�w, po jednym dla kazdej mapy w `m_cache`.
# # # Zmienne globalne

-   `g_text`: Globalna instancja `TextRender`.
# # Zaleznosci i powiazania

-   `framework/graphics/bitmapfont.h`, `coordsbuffer.h`: Kluczowe struktury danych.
-   `framework/core/clock.h`: Do sledzenia czasu ostatniego uzycia.
-   Jest uzywana przez `DrawQueueItemText` do renderowania tekstu w zoptymalizowany spos�b.

---
# ?? outfits.h
# # Opis og�lny

Plik `outfits.h` zawiera kod zr�dlowy shader�w w postaci stalych string�w, kt�re sa uzywane do renderowania stroj�w postaci z niestandardowymi kolorami.
# # Shadery
# # # `glslAdvancedOutfitVertexShader`
# # # # Opis
Shader wierzcholk�w dla zaawansowanego renderowania stroj�w.
# # # # Dzialanie
1.  **Atrybuty**: Przyjmuje pozycje wierzcholka (`a_Vertex`) i jego wsp�lrzedne na teksturze (`a_TexCoord`).
2.  **Uniformy**:
    -   `u_ProjectionMatrix`, `u_TransformMatrix`: Standardowe macierze do transformacji pozycji.
    -   `u_TextureMatrix`: Do transformacji wsp�lrzednych tekstury.
    -   `u_Offset`, `u_Resolution`: Dodatkowe dane, prawdopodobnie do efekt�w.
3.  **Varying**:
    -   Przekazuje do shadera fragment�w trzy zestawy wsp�lrzednych tekstury:
        -   `v_TexCoord`: Podstawowe.
        -   `v_TexCoord2`: Przesuniete o `u_Offset`.
        -   `v_TexCoord3`: Wsp�lrzedne oparte na rozdzielczosci.
4.  Oblicza finalna pozycje wierzcholka na ekranie (`gl_Position`).
# # # `glslAdvancedOutfitFragmentShader`
# # # # Opis
Shader fragment�w (pikseli) dla zaawansowanego renderowania stroj�w.
# # # # Dzialanie
1.  Pobiera kolor piksela z gl�wnej tekstury (`u_Tex0`) na podstawie `v_TexCoord`.
2.  Sprawdza kolor piksela z tej samej tekstury, ale w przesunietym miejscu (`v_TexCoord2`). Jesli alfa tego piksela jest wieksza od progu, mnozy finalny kolor przez z�lty (`vec4(1.0, 1.0, 0.0, 1.0)`), tworzac efekt podswietlenia lub konturu.
3.  Odrzuca piksel (`discard`), jesli jego alfa jest zbyt niska.

> **NOTE**: Kod shader�w w tym pliku wydaje sie byc eksperymentalny lub nie w pelni zaimplementowany w reszcie kodu. Prawdziwy shader do stroj�w znajduje sie w `shadersources.h`.
# # Zaleznosci i powiazania

-   Jest dolaczany przez `shaders.h`.
-   Kod jest przeznaczony do uzycia przez `PainterShaderProgram`.

---
# ?? newshader.h
# # Opis og�lny

Plik `newshader.h` zawiera kod zr�dlowy dla nowego, zoptymalizowanego systemu renderowania opartego na `DrawCache`. Definiuje shadery wierzcholk�w i fragment�w do rysowania geometrii wsadowej, tekstu i linii.
# # Shadery
# # # `newVertexShader`
# # # # Opis
Shader wierzcholk�w dla `DrawCache`.
# # # # Dzialanie
1.  **Atrybuty**: Przyjmuje pozycje (`a_Vertex`), wsp�lrzedne tekstury (`a_TexCoord`) i **kolor (`a_Color`)** dla kazdego wierzcholka.
2.  **Varying**: Przekazuje wsp�lrzedne tekstury i kolor do shadera fragment�w.
3.  Oblicza pozycje wierzcholka.
# # # `newFragmentShader`
# # # # Opis
Shader fragment�w dla `DrawCache`.
# # # # Dzialanie
1.  Sprawdza, czy wsp�lrzedna X tekstury jest mniejsza od 0. Jesli tak, oznacza to, ze wierzcholek nie ma tekstury i jego kolorem jest po prostu `v_Color`.
2.  W przeciwnym razie, pobiera kolor z tekstury atlasu (`u_Atlas`) i mnozy go przez kolor wierzcholka (`v_Color`).
# # # `textVertexShader` i `textFragmentShader`

Shadery zoptymalizowane do rysowania tekstu. Wierzcholki sa przesuwane o `u_Offset` (pozycja tekstu na ekranie), a kolor jest jednolity dla calego tekstu (`u_Color`).
# # # `lineVertexShader` i `lineFragmentShader`

Proste shadery do rysowania linii. Shader fragment�w po prostu ustawia jednolity kolor `u_Color`.
# # Zaleznosci i powiazania

-   Jest dolaczany przez `shaders.h`.
-   Shadery te sa kompilowane i uzywane przez `Painter` do implementacji `drawCache`, `drawText` i `drawLine`.

---
# ?? shaders.h
# # Opis og�lny

Plik `shaders.h` jest plikiem nagl�wkowym, kt�ry agreguje wszystkie pliki zawierajace kod zr�dlowy shader�w. Sluzy jako pojedynczy punkt dolaczania dla wszystkich predefiniowanych shader�w w systemie.
# # Zawartosc

Dolacza nastepujace pliki:
-   `newshader.h`: Zawiera shadery dla nowego, wsadowego systemu renderowania (`DrawCache`).
-   `shadersources.h`: Zawiera kod zr�dlowy dla standardowych shader�w uzywanych przez `Painter` (rysowanie tekstur, jednolitych kolor�w, stroj�w).
-   `outfits.h`: Zawiera eksperymentalne/alternatywne shadery do stroj�w.
# # Zaleznosci i powiazania

-   Jest dolaczany przez `painter.cpp` w celu uzyskania dostepu do kodu zr�dlowego shader�w, kt�re sa kompilowane podczas inicjalizacji `Painter`.

---
# ?? shadersources.h
# # Opis og�lny

Plik `shadersources.h` zawiera kod zr�dlowy w GLSL dla standardowych shader�w uzywanych przez klase `Painter`. Sa one zdefiniowane jako stale stringi i kompilowane w trakcie dzialania programu.
# # Shadery
# # # `glslMainVertexShader` i `glslMainWithTexCoordsVertexShader`

Sa to "szablony" dla shader�w wierzcholk�w. Definiuja one funkcje `main`, kt�ra wywoluje `calculatePosition()`. Wersja `WithTexCoords` dodatkowo przekazuje wsp�lrzedne tekstury do shadera fragment�w.
# # # `glslPositionOnlyVertexShader`

Jest to implementacja `calculatePosition()`. Oblicza ona finalna pozycje wierzcholka, mnozac jego pozycje przez macierze transformacji i projekcji. Uwzglednia r�wniez glebie (`u_Depth`).
# # # `glslMainFragmentShader`

Szablon dla shader�w fragment�w. Wywoluje `calculatePixel()` i odrzuca piksele o niskiej wartosci alfa, jesli `u_Depth > 0`.
# # # `glslTextureSrcFragmentShader`

Implementacja `calculatePixel()`, kt�ra pobiera kolor z tekstury (`u_Tex0`) i mnozy go przez jednolity kolor (`u_Color`).
# # # `glslSolidColorFragmentShader`

Implementacja `calculatePixel()`, kt�ra zwraca jednolity kolor (`u_Color`).
# # # `glslSolidColorOnTextureFragmentShader`

Implementacja `calculatePixel()`, kt�ra rysuje jednolity kolor (`u_Color`) tylko tam, gdzie tekstura (`u_Tex0`) nie jest w pelni przezroczysta.
# # # `glslOutfitVertexShader` i `glslOutfitFragmentShader`

Shadery do renderowania stroj�w.
-   **Shader wierzcholk�w**: Przekazuje dwie pary wsp�lrzednych tekstury - normalne (`v_TexCoord`) i przesuniete o `u_Offset` (`v_TexCoord2`).
-   **Shader fragment�w**:
    1.  Pobiera kolor bazowy z `v_TexCoord`.
    2.  Pobiera kolor "maski" z `v_TexCoord2`.
    3.  Na podstawie koloru maski (sprawdzajac, kt�ry kanal R, G lub B jest dominujacy), mnozy kolor bazowy przez jeden z czterech kolor�w przekazanych w macierzy `u_Color`. Pozwala to na dynamiczne kolorowanie r�znych czesci stroju.
# # Zaleznosci i powiazania

-   Jest dolaczany przez `shaders.h`.
-   Kod jest uzywany w `painter.cpp` do tworzenia domyslnych program�w shader�w.

---
# ?? http.cpp
# # Opis og�lny

Plik `http.cpp` implementuje klase `Http`, kt�ra jest singletonem (`g_http`) odpowiedzialnym za obsluge zapytan HTTP/HTTPS oraz polaczen WebSocket. Dziala asynchronicznie, wykorzystujac biblioteke Boost.Asio do operacji sieciowych w osobnym watku.
# # Zmienne globalne
# # # `g_http`

Globalna instancja `Http`.
# # Klasa `Http`
# # # `void Http::init()`

Inicjalizuje menedzera. Tworzy i uruchamia osobny watek, w kt�rym bedzie dzialac `boost::asio::io_service` (`m_ios`), obslugujac wszystkie operacje sieciowe.
# # # `void Http::terminate()`

Zamyka menedzera. Zatrzymuje `io_service`, anuluje wszystkie biezace operacje i czeka na zakonczenie watku sieciowego.
# # # `int Http::get(const std::string& url, int timeout)`
# # # # Opis semantyczny
Wysyla asynchroniczne zapytanie HTTP GET.
# # # # Dzialanie
1.  Generuje unikalne ID operacji.
2.  Dodaje zadanie do `m_ios`, kt�re tworzy obiekt `HttpSession`.
3.  `HttpSession` wykonuje zapytanie w watku sieciowym.
4.  Wyniki (postep, blad, odpowiedz) sa przekazywane z powrotem do gl�wnego watku za pomoca `g_dispatcher` i wywolywane sa odpowiednie callbacki w Lua (`g_http.onGetProgress`, `g_http.onGet`).
# # # `int Http::post(...)`

Dziala analogicznie do `get`, ale wysyla zapytanie HTTP POST z podanymi danymi (`data`).
# # # `int Http::download(...)`

Specjalna wersja `get`, kt�ra dodatkowo zapisuje pobrane dane w wewnetrznej mapie `m_downloads`. Pozwala to na dostep do pobranych plik�w przez `ResourceManager` za pomoca wirtualnej sciezki `/downloads/...`.
# # # `int Http::ws(...)`

Inicjuje asynchroniczne polaczenie WebSocket. Tworzy obiekt `WebsocketSession`, kt�ry zarzadza cyklem zycia polaczenia. Callbacki Lua (`onWsOpen`, `onWsMessage`, `onWsClose`, `onWsError`) sa wywolywane w odpowiedzi na zdarzenia z gniazda.
# # # `bool Http::wsSend(int operationId, std::string message)`

Wysyla wiadomosc przez istniejace polaczenie WebSocket o danym `operationId`.
# # # `bool Http::cancel(int id)`

Anuluje operacje (HTTP lub WebSocket) o podanym ID.
# # Zaleznosci i powiazania

-   `framework/http/http.h`: Plik nagl�wkowy.
-   `framework/http/session.h`, `websocket.h`: Implementacje sesji HTTP i WebSocket (niedostepne dla Emscripten).
-   `framework/luaengine/luainterface.h`: Do wywolywania callback�w w Lua.
-   `framework/core/eventdispatcher.h`: Do przekazywania wynik�w z watku sieciowego do watku gl�wnego.
-   `boost/asio`, `boost/beast`: Podstawowe biblioteki do obslugi sieci.

---
# ?? websocket.h
# # Opis og�lny

Plik `websocket.h` deklaruje klase `WebsocketSession`, kt�ra zarzadza pojedynczym polaczeniem WebSocket. Plik ten (i jego implementacja) jest wylaczony z kompilacji dla Emscripten.
# # Typy wyliczeniowe i definicje

-   `enum WebsocketCallbackType`: Definiuje typy zdarzen dla callbacka (`WEBSOCKET_OPEN`, `WEBSOCKET_MESSAGE`, `WEBSOCKET_ERROR`, `WEBSOCKET_CLOSE`).
-   `using WebsocketSession_cb`: Alias dla typu funkcji zwrotnej.
# # Klasa `WebsocketSession`
# # # Opis semantyczny
`WebsocketSession` enkapsuluje cala logike zwiazana z nawiazywaniem, utrzymywaniem i zamykaniem polaczenia WebSocket, wlaczajac w to obsluge protokolu (handshake) i szyfrowania (WSS). Dziala w pelni asynchronicznie w oparciu o Boost.Asio.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `WebsocketSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna proces nawiazywania polaczenia (rozwiazywanie nazwy DNS, laczenie, handshake). |
| `void send(std::string data)` | Dodaje wiadomosc do kolejki wysylania. |
| `void close()` | Zamyka polaczenie. |
# # # Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_resolver`: Do rozwiazywania nazw DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o zdarzeniach.
-   `m_result`: Wskaznik na `HttpResult` do przechowywania stanu.
-   `m_timer`: Timer do obslugi timeout�w.
-   `m_socket`: Gniazdo WebSocket dla polaczen nieszyfrowanych (WS).
-   `m_ssl`: Gniazdo WebSocket dla polaczen szyfrowanych (WSS).
-   `m_context`: Kontekst SSL.
-   `m_streambuf`: Bufor na przychodzace dane.
-   `m_sendQueue`: Kolejka wiadomosci do wyslania.
# # # Metody prywatne (`on_...`)

-   Sa to handlery wywolywane przez Boost.Asio po zakonczeniu operacji asynchronicznych (np. `on_resolve`, `on_connect`, `on_handshake`, `on_read`, `on_send`). Implementuja one logike maszyny stan�w polaczenia.
-   `onError`: Centralna funkcja do obslugi bled�w.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   `boost/asio`, `boost/beast`: Kluczowe biblioteki do obslugi sieci.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# ?? http.h
# # Opis og�lny

Plik `http.h` deklaruje klase `Http`, kt�ra jest singletonem (`g_http`) i stanowi gl�wny interfejs do wykonywania operacji sieciowych opartych na protokolach HTTP/HTTPS i WebSocket.
# # Klasa `Http`
# # # Opis semantyczny
`Http` zarzadza pula operacji sieciowych, kt�re sa wykonywane asynchronicznie w dedykowanym watku. Udostepnia proste API do wysylania zapytan GET, POST, pobierania plik�w oraz nawiazywania polaczen WebSocket. Interakcja z reszta aplikacji (gl�wnie ze skryptami Lua) odbywa sie poprzez system callback�w.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Http()` | Konstruktor, inicjalizuje `io_context` i `work_guard`. |
| `void init()` | Uruchamia watek sieciowy. |
| `void terminate()` | Zatrzymuje watek sieciowy i anuluje wszystkie operacje. |
| `int get(...)` | Inicjuje asynchroniczne zapytanie GET. |
| `int post(...)` | Inicjuje asynchroniczne zapytanie POST. |
| `int download(...)` | Inicjuje asynchroniczne pobieranie pliku. |
| `int ws(...)` | Inicjuje asynchroniczne polaczenie WebSocket. |
| `bool wsSend(...)` | Wysyla dane przez istniejace polaczenie WebSocket. |
| `bool wsClose(...)` | Zamyka polaczenie WebSocket. |
| `bool cancel(int id)` | Anuluje operacje o podanym ID. |
| `const std::map<...>& downloads()` | Zwraca mape pobranych plik�w. |
| `void clearDownloads()` | Czysci mape pobranych plik�w. |
| `HttpResult_ptr getFile(...)` | Pobiera dane pobranego pliku na podstawie jego sciezki. |
| `void setUserAgent(...)` | Ustawia nagl�wek User-Agent dla wszystkich zapytan. |
# # # Zmienne prywatne

-   `m_working`: Flaga kontrolujaca dzialanie watku.
-   `m_operationId`: Licznik do generowania unikalnych ID dla operacji.
-   `m_thread`: Watek roboczy dla operacji sieciowych.
-   `m_ios`: Kontekst `io_context` z Boost.Asio.
-   `m_guard`: `work_guard` zapobiegajacy zakonczeniu `m_ios.run()`, dop�ki nie ma pracy.
-   `m_operations`: Mapa przechowujaca stan wszystkich aktywnych operacji.
-   `m_websockets`: Mapa przechowujaca aktywne sesje WebSocket.
-   `m_downloads`: Mapa przechowujaca pobrane pliki.
-   `m_userAgent`: String User-Agent.
# # # Zmienne globalne

-   `g_http`: Globalna instancja `Http`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest uzywana w skryptach Lua (poprzez bindowania w `luafunctions.cpp`) do komunikacji z serwerami WWW, np. do pobierania aktualizacji, sprawdzania statusu serwer�w itp.
-   Wsp�lpracuje z `ResourceManager` w celu udostepnienia pobranych plik�w przez wirtualny system plik�w.

---
# ?? result.h
# # Opis og�lny

Plik `result.h` deklaruje strukture `HttpResult`, kt�ra sluzy do przechowywania stanu i wyniku pojedynczej operacji HTTP lub WebSocket. Definiuje r�wniez aliasy typ�w dla inteligentnych wskaznik�w i funkcji zwrotnych.
# # Struktura `HttpResult`
# # # Opis semantyczny
`HttpResult` jest kontenerem danych przekazywanym miedzy watkiem sieciowym a watkiem gl�wnym. Agreguje wszystkie informacje zwiazane z danym zapytaniem, takie jak URL, status, postep, dane odpowiedzi i ewentualne bledy.
# # # Pola struktury

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `url` | `std::string` | Adres URL zapytania. |
| `operationId` | `int` | Unikalny identyfikator operacji. |
| `status` | `int` | Kod statusu odpowiedzi HTTP (np. 200, 404). |
| `size` | `int` | Calkowity rozmiar odpowiedzi (z nagl�wka Content-Length). |
| `progress` | `int` | Postep pobierania w procentach (0-100). |
| `redirects` | `int` | Licznik przekierowan. |
| `connected` | `bool` | Flaga wskazujaca, czy polaczenie jest aktywne. |
| `finished` | `bool` | Flaga wskazujaca, czy operacja zostala zakonczona. |
| `canceled` | `bool` | Flaga wskazujaca, czy operacja zostala anulowana. |
| `postData` | `std::string` | Dane wyslane w zapytaniu POST. |
| `response` | `std::vector<uint8_t>`| Surowe bajty odpowiedzi. |
| `error` | `std::string` | Komunikat bledu, jesli wystapil. |
| `session` | `std::weak_ptr<HttpSession>` | Slaby wskaznik do obiektu sesji, aby uniknac cyklicznych referencji. |
# # Definicje typ�w

-   `HttpResult_ptr`: Alias dla `std::shared_ptr<HttpResult>`.
-   `HttpResult_cb`: Alias dla `std::function<void(HttpResult_ptr)>`.
# # Zaleznosci i powiazania

-   Jest to podstawowa struktura danych uzywana przez `Http`, `HttpSession` i `WebsocketSession` do komunikacji i przekazywania wynik�w.
-   Zawiera `std::weak_ptr` do `HttpSession`, aby umozliwic anulowanie operacji z zewnatrz bez tworzenia cyklu referencji.

---
# ?? session.cpp
# # Opis og�lny

Plik `session.cpp` zawiera implementacje klasy `HttpSession`, kt�ra zarzadza pojedyncza sesja HTTP/HTTPS. Jest on wylaczony z kompilacji dla platformy Emscripten.
# # Klasa `HttpSession`
# # # `void HttpSession::start()`
# # # # Opis semantyczny
Rozpoczyna proces wysylania zapytania HTTP.
# # # # Dzialanie
1.  Sprawdza limit przekierowan.
2.  Parsuje URL, aby uzyskac protok�l, domene, port i sciezke.
3.  Ustawia timer (`m_timer`) na obsluge timeoutu.
4.  Konfiguruje obiekt zadania `boost::beast::http::request` (metoda, nagl�wki, tresc).
5.  Uruchamia asynchroniczne rozwiazywanie nazwy DNS za pomoca `m_resolver.async_resolve`.
# # # Metody `on_...()`

Sa to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio, kt�re implementuja maszyne stan�w sesji HTTP:

-   **`on_resolve`**: Wywolywana po rozwiazaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: Wywolywana po nawiazaniu polaczenia TCP.
    -   Jesli protok�l to HTTPS, inicjalizuje kontekst SSL i wykonuje `async_handshake`.
    -   Wysyla zadanie HTTP za pomoca `boost::beast::http::async_write`.
-   **`on_request_sent`**: Wywolywana po wyslaniu zadania. Rozpoczyna odczytywanie nagl�wk�w odpowiedzi za pomoca `async_read_header`.
-   **`on_read_header`**: Wywolywana po odczytaniu nagl�wk�w.
    -   Sprawdza kod statusu.
    -   Jesli jest to przekierowanie (np. 301, 302), tworzy nowa `HttpSession` dla nowego URL.
    -   Jesli status jest niepoprawny, zglasza blad.
    -   Rozpoczyna odczytywanie tresci odpowiedzi za pomoca `async_read_some`.
-   **`on_read`**: Wywolywana wielokrotnie podczas odczytywania tresci odpowiedzi.
    -   Aktualizuje postep pobierania i wywoluje `callback` progresu.
    -   Gdy cala tresc zostanie odczytana (`end_of_stream`), finalizuje operacje, zapisuje odpowiedz w `m_result` i wywoluje `callback` koncowy.
-   **`onTimeout`**: Handler dla timera, kt�ry zglasza blad timeoutu.
-   **`onError`**: Centralna funkcja do obslugi bled�w. Zamyka gniazdo, anuluje timer i wywoluje `callback` z informacja o bledzie.
# # # `void HttpSession::close()`

Zamyka polaczenie, anuluje timer i, w przypadku HTTPS, wykonuje `async_shutdown` dla strumienia SSL.
# # Zaleznosci i powiazania

-   `framework/http/session.h`: Plik nagl�wkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obslugi sieci.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# ?? session.h
# # Opis og�lny

Plik `session.h` deklaruje klase `HttpSession`, kt�ra enkapsuluje logike pojedynczej sesji HTTP/HTTPS. Plik ten jest wylaczony z kompilacji dla Emscripten.
# # Klasa `HttpSession`
# # # Opis semantyczny
`HttpSession` zarzadza calym cyklem zycia zapytania HTTP, od rozwiazania nazwy DNS, przez nawiazanie polaczenia (w tym SSL/TLS handshake), wyslanie zadania, az po odczytanie odpowiedzi. Jest zaprojektowana do dzialania asynchronicznego w ramach `boost::asio::io_service`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `HttpSession(...)` | Konstruktor. |
| `void start()` | Rozpoczyna sesje HTTP. |
| `void cancel()` | Anuluje biezaca operacje. |
# # # Zmienne prywatne

-   `m_service`: Referencja do `io_service`.
-   `m_url`, `m_agent`: URL i User-Agent.
-   `m_socket`: Gniazdo TCP.
-   `m_resolver`: Resolver DNS.
-   `m_callback`: Funkcja zwrotna do powiadamiania o wyniku.
-   `m_result`: Wskaznik na obiekt `HttpResult` przechowujacy stan.
-   `m_timer`: Timer do obslugi timeout�w.
-   `m_timeout`: Czas timeoutu.
-   `m_isJson`: Flaga wskazujaca, czy tresc POST jest w formacie JSON.
-   `m_ssl`, `m_context`: Do obslugi HTTPS.
-   `m_streambuf`: Bufor na dane przychodzace.
-   `m_request`: Obiekt zadania z Boost.Beast.
-   `m_response`: Parser odpowiedzi z Boost.Beast.
# # # Metody prywatne (`on_...`, `close`, `onError`)

Deklaracje handler�w dla operacji asynchronicznych i funkcji pomocniczych.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/http/result.h`: Definicja `HttpResult`.
-   Jest tworzona i uzywana przez klase `Http` do realizacji zapytan GET i POST.

---
# ?? websocket.cpp
# # Opis og�lny

Plik `websocket.cpp` zawiera implementacje klasy `WebsocketSession`, kt�ra zarzadza pojedynczym polaczeniem WebSocket. Plik ten jest wylaczony z kompilacji dla Emscripten.
# # Klasa `WebsocketSession`
# # # `void WebsocketSession::start()`
# # # # Opis semantyczny
Rozpoczyna proces nawiazywania polaczenia WebSocket.
# # # # Dzialanie
1.  Sprawdza limit przekierowan.
2.  Parsuje URL, aby uzyskac protok�l, domene, port i sciezke.
3.  Ustawia timer na obsluge timeoutu.
4.  Tworzy odpowiedni obiekt gniazda (`m_socket` dla WS lub `m_ssl` dla WSS).
5.  Uruchamia asynchroniczne rozwiazywanie nazwy DNS.
# # # `void WebsocketSession::send(std::string data)`

Dodaje wiadomosc do kolejki `m_sendQueue`. Jesli kolejka byla pusta i polaczenie jest aktywne, natychmiast inicjuje operacje wysylania.
# # # Metody `on_...()`

Sa to handlery dla operacji asynchronicznych, kt�re implementuja maszyne stan�w polaczenia WebSocket:

-   **`on_resolve`**: Wywolywana po rozwiazaniu nazwy DNS. Inicjuje `async_connect`.
-   **`on_connect`**: Wywolywana po nawiazaniu polaczenia TCP. W przypadku WSS, wykonuje handshake SSL. Nastepnie inicjuje handshake protokolu WebSocket za pomoca `async_handshake`.
-   **`on_handshake`**: Wywolywana po pomyslnym handshake'u WebSocket. Ustawia stan na `connected`, wywoluje `callback` `WEBSOCKET_OPEN`, rozpoczyna nasluchiwanie wiadomosci (`async_read`) i wysyla wiadomosci z kolejki.
-   **`on_send`**: Wywolywana po wyslaniu wiadomosci. Usuwa wyslana wiadomosc z kolejki i, jesli kolejka nie jest pusta, inicjuje wysylanie nastepnej.
-   **`on_read`**: Wywolywana po otrzymaniu nowej wiadomosci. Resetuje timer, wywoluje `callback` `WEBSOCKET_MESSAGE` i ponownie nasluchuje.
-   **`onTimeout`**: Zglasza blad timeoutu.
-   **`onError`**: Obsluguje bledy i wywoluje `callback` `WEBSOCKET_ERROR`.
# # # `void WebsocketSession::close()`

Zamyka polaczenie, anuluje timer i wywoluje `callback` `WEBSOCKET_CLOSE`.
# # Zaleznosci i powiazania

-   `framework/http/websocket.h`: Plik nagl�wkowy.
-   `framework/stdext/uri.h`: Do parsowania URL.
-   **Boost.Asio** i **Boost.Beast**: Kluczowe biblioteki do obslugi sieci i protokolu WebSocket.
-   Jest tworzona i zarzadzana przez klase `Http`.

---
# ?? mouse.cpp
# # Opis og�lny

Plik `mouse.cpp` implementuje klase `Mouse`, kt�ra jest singletonem (`g_mouse`) odpowiedzialnym za zarzadzanie kursorami myszy.
# # Zmienne globalne
# # # `g_mouse`

Globalna instancja `Mouse`.
# # Klasa `Mouse`
# # # `void Mouse::init()` i `void Mouse::terminate()`

Metody do inicjalizacji i zwalniania zasob�w. `terminate()` czysci liste zaladowanych kursor�w.
# # # `void Mouse::loadCursors(std::string filename)`

Laduje definicje kursor�w z pliku OTML. Parsuje plik i dla kazdego wpisu w sekcji `Cursors` wywoluje `addCursor`.
# # # `void Mouse::addCursor(const std::string& name, const std::string& file, const Point& hotSpot)`
# # # # Opis semantyczny
Laduje obraz kursora z pliku i tworzy z niego natywny kursor systemowy. Jest bezpieczna watkowo.
# # # # Dzialanie
1.  Jesli jest wywolana z watku innego niz graficzny, deleguje zadanie do `g_graphicsDispatcher`.
2.  Wywoluje `g_window.loadMouseCursor`, kt�ra wykonuje operacje specyficzne dla platformy.
3.  Zapisuje zwr�cone ID kursora w mapie `m_cursors` pod podana nazwa.
# # # `void Mouse::pushCursor(const std::string& name)`
# # # # Opis semantyczny
Ustawia nowy kursor i dodaje go na stos aktywnych kursor�w.
# # # # Dzialanie
1.  Deleguje do watku graficznego, jesli to konieczne.
2.  Znajduje ID kursora w `m_cursors`.
3.  Wywoluje `g_window.setMouseCursor` z znalezionym ID.
4.  Dodaje ID na koniec stosu `m_cursorStack`.
# # # `void Mouse::popCursor(const std::string& name)`
# # # # Opis semantyczny
Usuwa kursor ze stosu i przywraca poprzedni.
# # # # Dzialanie
1.  Deleguje do watku graficznego.
2.  Jesli `name` jest puste, usuwa ostatni kursor ze stosu.
3.  Jesli `name` jest podane, wyszukuje i usuwa konkretny kursor ze stosu.
4.  Jesli stos nie jest pusty, ustawia kursor, kt�ry jest teraz na jego szczycie.
5.  Jesli stos jest pusty, przywraca domyslny kursor systemowy.
# # # `bool Mouse::isCursorChanged()`

Zwraca `true`, jesli stos kursor�w nie jest pusty, co oznacza, ze aktualny kursor jest niestandardowy.
# # # `bool Mouse::isPressed(Fw::MouseButton mouseButton)`

Sprawdza i zwraca stan wcisniecia danego przycisku myszy, delegujac zapytanie do `g_window`.
# # Zaleznosci i powiazania

-   `framework/input/mouse.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Widgety moga zmieniac kursor.
-   `framework/platform/platformwindow.h`: Uzywa `g_window` do niskopoziomowych operacji na kursorach.
-   `framework/core/eventdispatcher.h`: Do zapewnienia bezpieczenstwa watkowego.
-   `framework/core/resourcemanager.h`: Do ladowania plik�w definicji kursor�w.

---
# ?? mouse.h
# # Opis og�lny

Plik `mouse.h` deklaruje klase `Mouse`, kt�ra jest interfejsem wysokiego poziomu do zarzadzania kursorami myszy w aplikacji.
# # Klasa `Mouse`
# # # Opis semantyczny
`Mouse` zarzadza kolekcja niestandardowych kursor�w, kt�re moga byc ladowane z plik�w. Implementuje mechanizm stosu (`m_cursorStack`), kt�ry pozwala na tymczasowa zmiane kursora (np. gdy kursor znajduje sie nad widgetem) i latwy powr�t do poprzedniego stanu.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void init()` | Inicjalizuje menedzera. |
| `void terminate()` | Zwalnia zasoby. |
| `void loadCursors(...)` | Laduje definicje kursor�w z pliku OTML. |
| `void addCursor(...)` | Dodaje nowy niestandardowy kursor. |
| `void pushCursor(...)` | Ustawia nowy kursor, dodajac go na szczyt stosu. |
| `void popCursor(...)` | Usuwa kursor ze stosu i przywraca poprzedni. |
| `bool isCursorChanged()` | Sprawdza, czy aktualny kursor jest niestandardowy. |
| `bool isPressed(...)` | Sprawdza stan wcisniecia przycisku myszy. |
# # # Zmienne prywatne

-   `m_cursors`: Mapa przechowujaca nazwy kursor�w i ich ID specyficzne dla platformy.
-   `m_cursorStack`: Stos (`std::deque`) przechowujacy ID aktywnych kursor�w.
-   `m_mutex`: Mutex do ochrony dostepu do `m_cursorStack` z r�znych watk�w.
# # # Zmienne globalne

-   `g_mouse`: Globalna instancja `Mouse`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest uzywana przez `UIWidget` do zmiany wygladu kursora, gdy znajduje sie on nad widgetem.
-   Wsp�lpracuje z `PlatformWindow` w celu faktycznego ustawiania kursora w systemie operacyjnym.

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `luaengine` sluzy do wczesnych deklaracji (forward declarations) i definicji typ�w zwiazanych z silnikiem Lua. Jego celem jest unikanie zaleznosci cyklicznych i zmniejszenie liczby dolaczanych nagl�wk�w.
# # Wczesne deklaracje

-   `LuaInterface`: Gl�wna klasa interfejsu Lua.
-   `LuaObject`: Bazowa klasa dla wszystkich obiekt�w eksportowanych do Lua.
# # Definicje typ�w

-   **`LuaCppFunction`**: Alias dla `std::function<int(LuaInterface*)>`. Jest to typ funkcji C++, kt�ra moze byc wywolana z Lua. Przyjmuje wskaznik do `LuaInterface` i zwraca liczbe wartosci zwr�conych na stos Lua.
-   **`LuaCppFunctionPtr`**: Alias dla `std::unique_ptr<LuaCppFunction>`. Uzywany wewnetrznie do zarzadzania czasem zycia funkcji bindowanych.
-   **`LuaObjectPtr`**: Alias dla `stdext::shared_object_ptr<LuaObject>`. Standardowy spos�b przekazywania i przechowywania obiekt�w C++ w Lua.
# # Zaleznosci i powiazania

-   `framework/global.h`: Zawiera podstawowe definicje.
-   `<memory>`: Dla `std::unique_ptr`.
-   Jest to fundamentalny plik dla calego silnika Lua, dolaczany przez `luainterface.h`, `luaobject.h` i inne.

---
# ?? lbitlib.cpp
# # Opis og�lny

Plik `lbitlib.cpp` zawiera kod zr�dlowy biblioteki `bit32` z Lua 5.2.0, przeniesiony (backported) do uzytku z Lua 5.1.4 (lub LuaJIT, kt�ry jest kompatybilny z 5.1). Biblioteka ta dostarcza operacje bitowe na 32-bitowych liczbach calkowitych bez znaku.
# # Zawartosc

Plik sklada sie z kilku czesci:

1.  **Adaptacje i definicje kompatybilnosci**:
    -   Zawiera kod przeniesiony z `luaconf.h` i `llimits.h` z Lua 5.2, kt�ry definiuje makra (`lua_number2unsigned`) do bezpiecznej konwersji miedzy `lua_Number` (zwykle `double`) a `lua_Unsigned` (32-bitowy `unsigned int`). Jest to konieczne, poniewaz Lua 5.1 nie ma wbudowanego typu calkowitoliczbowego.
    -   Definiuje funkcje `lua_pushunsigned` i `luaL_checkunsigned` do obslugi tego typu na stosie Lua.
    -   Definiuje makro `luaL_newlib` dla kompatybilnosci z `luaL_register` z Lua 5.1.

2.  **Oryginalny kod `lbitlib.c` z Lua 5.2.0**:
    -   Zawiera implementacje wszystkich funkcji z biblioteki `bit32`.
# # # Funkcje biblioteki `bit32`

| Funkcja Lua | Opis |
| :--- | :--- |
| `bit32.band(...)` | Wykonuje bitowe AND na wszystkich argumentach. |
| `bit32.btest(...)` | Wykonuje bitowe AND i zwraca `true`, jesli wynik jest r�zny od zera. |
| `bit32.bor(...)` | Wykonuje bitowe OR na wszystkich argumentach. |
| `bit32.bxor(...)` | Wykonuje bitowe XOR na wszystkich argumentach. |
| `bit32.bnot(x)` | Wykonuje bitowa negacje. |
| `bit32.lshift(x, n)` | Przesuniecie bitowe w lewo. |
| `bit32.rshift(x, n)` | Przesuniecie bitowe w prawo (logiczne). |
| `bit32.arshift(x, n)`| Przesuniecie bitowe w prawo (arytmetyczne). |
| `bit32.lrotate(x, n)`| Rotacja bitowa w lewo. |
| `bit32.rrotate(x, n)`| Rotacja bitowa w prawo. |
| `bit32.extract(n, field, width)`| Ekstrahuje `width` bit�w z liczby `n`, zaczynajac od bitu `field`. |
| `bit32.replace(n, v, field, width)`| Zastepuje bity w liczbie `n` bitami z `v`. |
# # # `int luaopen_bit32 (lua_State *L)`

Gl�wna funkcja, kt�ra rejestruje biblioteke `bit32` w podanym stanie Lua.
# # Zaleznosci i powiazania

-   `lbitlib.h`: Plik nagl�wkowy.
-   Nagl�wki Lua/LuaJIT (`lua.h`, `lualib.h`, `lauxlib.h`).
-   Jest ladowana w `LuaInterface::createLuaState`, aby udostepnic operacje bitowe w skryptach.

---
# ?? lbitlib.h
# # Opis og�lny

Plik `lbitlib.h` jest plikiem nagl�wkowym dla biblioteki `bit32` z Lua 5.2, kt�ra zostala przeniesiona do uzytku w tym projekcie.
# # Deklaracje
# # # `int luaopen_bit32 (lua_State *L)`

Deklaruje funkcje, kt�ra jest punktem wejscia do zaladowania biblioteki `bit32` w stanie Lua. Zgodnie z konwencja Lua, funkcje `luaopen_*` sa uzywane do rejestrowania modul�w.
# # Zaleznosci i powiazania

-   Wymaga definicji `struct lua_State`.
-   Jest dolaczany przez `luainterface.cpp`, aby umozliwic zaladowanie biblioteki `bit32` podczas inicjalizacji `LuaInterface`.

---
# ?? luabinder.h
# # Opis og�lny

Plik `luabinder.h` jest sercem mechanizmu bindowania C++ do Lua. Zawiera on zestaw zaawansowanych szablon�w metaprogramowania, kt�re umozliwiaja automatyczne generowanie funkcji-opakowan (wrapper�w) dla niemal dowolnych funkcji C++, w tym funkcji globalnych, statycznych, metod klas, funkcji `std::function` i lambd.
# # Namespace `luabinder`
# # # Opis semantyczny
Przestrzen nazw `luabinder` zawiera szablony, kt�re dzialaja jak "fabryka" funkcji typu `LuaCppFunction`. Analizuja one sygnature funkcji C++ (typ zwracany i typy argument�w), a nastepnie generuja lambde, kt�ra:
1.  Pobiera argumenty z stosu Lua i konwertuje je na odpowiednie typy C++.
2.  Wywoluje oryginalna funkcje C++ z tymi argumentami.
3.  Pobiera wartosc zwracana przez funkcje C++.
4.  Konwertuje te wartosc na typ zrozumialy dla Lua i umieszcza ja na stosie.
5.  Zwraca liczbe wartosci umieszczonych na stosie.
# # # Gl�wne szablony

-   **`pack_values_into_tuple`**: Szablon rekurencyjny, kt�ry pobiera `N` wartosci ze stosu Lua i umieszcza je w `std::tuple`.
-   **`expand_fun_arguments`**: Szablon rekurencyjny, kt�ry rozpakowuje `std::tuple` z argumentami i wywoluje z nimi docelowa funkcje C++.
-   **`call_fun_and_push_result`**: Szablon, kt�ry wywoluje funkcje i obsluguje wartosc zwracana (specjalizacje dla `void` i typ�w nie-`void`).
-   **`bind_fun_specializer`**: Gl�wny szablon, kt�ry laczy powyzsze, generujac finalna lambde.
-   **`bind_fun(...)`**: Przeciazone funkcje, kt�re sa publicznym API tego namespace. Przyjmuja r�zne typy funkcji (wskazniki, `std::function`, lambdy) i przekierowuja je do odpowiednich specjalizacji.
-   **`make_mem_func(...)` i `make_mem_func_singleton(...)`**: Funkcje pomocnicze, kt�re konwertuja wskazniki na metody klas na obiekty `std::function` (lambdy), kt�re mozna nastepnie zbindowac.
# # Zaleznosci i powiazania

-   Jest to plik wewnetrzny, dolaczany tylko przez `luainterface.h`.
-   Intensywnie korzysta z zaawansowanych cech C++11/14/17, takich jak szablony wariadyczne, `std::tuple`, `std::function`, `std::enable_if`, `decltype`.
-   `framework/stdext/traits.h`: Uzywa `remove_const_ref` do normalizacji typ�w.
-   `luaexception.h`: Moze rzucac wyjatki w przypadku bled�w (np. wywolanie metody na obiekcie `nullptr`).
-   Jest podstawa dla wszystkich metod `bind...` w `LuaInterface`, kt�re automatyzuja proces tworzenia bindowan.

---
# ?? luaexception.h
# # Opis og�lny

Plik `luaexception.h` deklaruje hierarchie klas wyjatk�w specyficznych dla interakcji z silnikiem Lua. Te klasy wyjatk�w sa uzywane do sygnalizowania bled�w, kt�re wystepuja podczas operacji na stosie Lua, rzutowania typ�w lub wywolywania funkcji.
# # Klasa `LuaException`
# # # Opis semantyczny
Jest to bazowa klasa dla wszystkich wyjatk�w zwiazanych z Lua. Dziedziczy po `stdext::exception`. Jej gl�wnym zadaniem jest sformatowanie komunikatu o bledzie, opcjonalnie dolaczajac do niego slad stosu (traceback) z Lua.
# # # Metody

-   `LuaException(const std::string& error, int traceLevel = -1)`: Konstruktor, kt�ry generuje komunikat bledu.
-   `virtual const char* what() const throw()`: Zwraca sformatowany komunikat bledu.
# # Klasa `LuaBadNumberOfArgumentsException`
# # # Opis semantyczny
Specjalistyczny wyjatek rzucany, gdy funkcja C++ bindowana do Lua zostanie wywolana z nieprawidlowa liczba argument�w.
# # # Metody

-   `LuaBadNumberOfArgumentsException(int expected = -1, int got = -1)`: Konstruktor, kt�ry tworzy odpowiedni komunikat o bledzie.
# # Klasa `LuaBadValueCastException`
# # # Opis semantyczny
Specjalistyczny wyjatek rzucany, gdy pr�ba rzutowania wartosci ze stosu Lua na okreslony typ C++ (`luavalue_cast`) nie powiedzie sie.
# # # Metody

-   `LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`: Konstruktor, kt�ry tworzy komunikat bledu informujacy o typach, miedzy kt�rymi rzutowanie zawiodlo.
# # Zaleznosci i powiazania

-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa `stdext::exception`.
-   Wyjatki te sa rzucane przez `LuaInterface` i `luabinder`, a lapane w bezpiecznych punktach wywolan (np. `luaCppFunctionCallback`), aby zapobiec awarii aplikacji i przekazac blad do log�w lub z powrotem do srodowiska Lua.

---
# ?? luaexception.cpp
# # Opis og�lny

Plik `luaexception.cpp` zawiera implementacje klas wyjatk�w zdefiniowanych w `luaexception.h`.
# # Klasa `LuaException`
# # # `LuaException::LuaException(const std::string& error, int traceLevel)`

Konstruktor. Jego gl�wnym zadaniem jest wywolanie `generateLuaErrorMessage`, aby przygotowac pelny komunikat bledu.
# # # `void LuaException::generateLuaErrorMessage(const std::string& error, int traceLevel)`

Metoda ta formatuje finalny komunikat bledu, kt�ry bedzie dostepny przez `what()`.
-   Jesli `traceLevel` jest podany (wiekszy lub r�wny 0), wywoluje `g_lua.traceback`, aby dolaczyc do komunikatu slad stosu wywolan Lua.
-   W przeciwnym razie, po prostu prefiksuje blad napisem "LUA ERROR:".
# # Klasa `LuaBadNumberOfArgumentsException`
# # # `LuaBadNumberOfArgumentsException::LuaBadNumberOfArgumentsException(int expected, int got)`

Konstruktor. Tworzy specyficzny komunikat bledu informujacy o nieprawidlowej liczbie argument�w, a nastepnie wywoluje `generateLuaErrorMessage` z poziomem sledzenia `1`, aby pokazac, kt�ra funkcja w Lua zostala zle wywolana.
# # Klasa `LuaBadValueCastException`
# # # `LuaBadValueCastException::LuaBadValueCastException(const std::string& luaTypeName, const std::string& cppTypeName)`

Konstruktor. Tworzy komunikat bledu informujacy o niemoznosci rzutowania miedzy danym typem Lua a typem C++, a nastepnie wywoluje `generateLuaErrorMessage`.
# # Zaleznosci i powiazania

-   `framework/luaengine/luaexception.h`: Plik nagl�wkowy.
-   `framework/luaengine/luainterface.h`: Uzywa `g_lua` do generowania sladu stosu.
-   Implementuje logike formatowania bled�w, kt�ra jest kluczowa dla debugowania skrypt�w Lua.

---
# ?? luainterface.cpp
# # Opis og�lny

Plik `luainterface.cpp` zawiera implementacje klasy `LuaInterface`, kt�ra jest centralnym interfejsem do komunikacji z silnikiem Lua. Jest to jedna z najwazniejszych klas w calym frameworku.
# # Zmienne globalne
# # # `g_lua`

Globalna instancja `LuaInterface`.
# # Klasa `LuaInterface`
# # # Inicjalizacja i zamykanie

-   **`init()`**: Inicjalizuje `LuaInterface`.
    1.  Tworzy nowy stan Lua (`createLuaState`).
    2.  Zapisuje referencje do globalnego srodowiska.
    3.  Rejestruje bazowa klase `LuaObject` i jej podstawowe metody.
-   **`terminate()`**: Zamyka stan Lua, co powoduje zwolnienie wszystkich zasob�w i wywolanie garbage collectora.
-   **`createLuaState()`**: Tworzy stan Lua (`luaL_newstate`), laduje standardowe biblioteki (`luaL_openlibs`), laduje biblioteke `bit32`, tworzy specjalna "slaba" tabele do przechowywania referencji i instaluje niestandardowe loadery (`dofile`, `loadfile`).
# # # Rejestracja i bindowanie

-   **`registerSingletonClass(...)`**, **`registerClass(...)`**: Implementuja logike tworzenia tabel i metatabel w Lua, kt�re reprezentuja klasy C++. `registerClass` dodatkowo ustawia dziedziczenie, linkujac metatabele klasy pochodnej do metatabeli klasy bazowej za pomoca metametody `__index`.
-   **`register...Function(...)`**, **`register...Field(...)`**: Metody te pobieraja odpowiednie tabele (klasy, metody, fieldmethods) z globalnego srodowiska Lua i umieszczaja w nich funkcje C++ opakowane w `LuaCppFunction`.
# # # Metody obslugi metametod obiekt�w

-   **`luaObjectGetEvent(__index)`**: Handler wywolywany przy pr�bie odczytu pola z obiektu C++ w Lua. Wyszukuje on kolejno: metode "get", pole w tabeli `fields` obiektu, metode w tabeli metod klasy.
-   **`luaObjectSetEvent(__newindex)`**: Handler wywolywany przy pr�bie zapisu pola. Wyszukuje i wywoluje metode "set" lub zapisuje wartosc w tabeli `fields`.
-   **`luaObjectEqualEvent(__eq)`**: Por�wnuje dwa obiekty C++.
-   **`luaObjectCollectEvent(__gc)`**: Handler wywolywany przez garbage collector Lua. Zwalnia `shared_ptr` do obiektu, dekrementujac jego licznik referencji.
# # # Wykonywanie skrypt�w

-   **`runScript(...)`**, **`loadScript(...)`**, **`runBuffer(...)`**: Metody do ladowania i wykonywania skrypt�w Lua z plik�w lub bufor�w w pamieci. `loadScript` uzywa `g_resources` do znalezienia i odczytania pliku.
-   **`safeCall(...)`**: Kluczowa metoda do bezpiecznego wywolywania funkcji Lua. Ustawia `luaErrorHandler` jako funkcje obslugi bled�w, a nastepnie wywoluje `lua_pcall`. W przypadku bledu, lapie go i zwraca jako string lub rzuca wyjatek `LuaException`.
-   **`signalCall(...)`**: Wysokopoziomowa metoda, kt�ra opakowuje `safeCall` i dodatkowo obsluguje wywolywanie tabeli funkcji.
# # # Inne

-   **`traceback(...)`**: Generuje slad stosu wywolan Lua.
-   **`getCurrentSourcePath(...)`**: Zwraca sciezke do pliku skryptu, w kt�rym aktualnie wykonywany jest kod.
-   **`newSandboxEnv()`**: Tworzy nowe, odizolowane srodowisko Lua.
-   **`lua...` (funkcje statyczne)**: Implementacje funkcji C, kt�re sa bezposrednio rejestrowane w Lua (np. `lua_dofile`).
-   **`...Callback`**: Implementacje handler�w dla `lua_pcall` i `__gc`.
-   **Metody opakowujace API Lua**: Plik zawiera dziesiatki metod (`getTop`, `pushNil`, `toString`, `isTable`, etc.), kt�re sa cienkimi, ale bezpieczniejszymi (dzieki `VALIDATE`) opakowaniami na funkcje z biblioteki Lua C API.
# # Zaleznosci i powiazania

-   Jest to centralna klasa, kt�ra laczy C++ z Lua. Zalezy od `lua.h`, `lualib.h`, `lauxlib.h`.
-   Scisle wsp�lpracuje z `LuaObject`, `luabinder.h`, `luavaluecasts.h`.
-   Uzywa `g_resources` do ladowania skrypt�w.
-   Uzywana przez `Application` do inicjalizacji, `ModuleManager` do ladowania modul�w i `UIWidget` do wywolywania callback�w.

---
# ?? luainterface.h
# # Opis og�lny

Plik `luainterface.h` deklaruje klase `LuaInterface`, kt�ra jest gl�wnym interfejsem do interakcji z silnikiem Lua. Jest to klasa singletonowa (`g_lua`), kt�ra enkapsuluje stan Lua (`lua_State*`) i dostarcza bogaty zestaw metod do manipulacji stosem, wywolywania funkcji, bindowania kodu C++ i zarzadzania obiektami.
# # Klasa `LuaInterface`
# # # Opis semantyczny
`LuaInterface` stanowi most miedzy kodem C++ a skryptami Lua. Udostepnia wysokopoziomowe API, kt�re ukrywa zlozonosc bezposredniej pracy z Lua C API. Wszystkie operacje, takie jak umieszczanie wartosci na stosie, odczytywanie ich, wywolywanie funkcji czy rejestrowanie klas, sa opakowane w metody tej klasy.
# # # Metody publiczne (wybrane)
# # # # Inicjalizacja i zarzadzanie
-   `init()` / `terminate()`: Uruchamia i zamyka silnik Lua.
-   `collectGarbage()`: Wymusza uruchomienie garbage collectora.
# # # # Rejestracja i bindowanie
-   `registerSingletonClass(...)`: Rejestruje globalny obiekt (singleton) w Lua.
-   `registerClass(...)`: Rejestruje klase C++ w Lua, umozliwiajac tworzenie jej instancji.
-   `bind...Function(...)`, `bind...Field(...)`: Szablonowe metody do bindowania funkcji i p�l klas.
# # # # Wykonywanie skrypt�w
-   `safeRunScript(...)`: Bezpiecznie wykonuje skrypt z pliku.
-   `runScript(...)`, `runBuffer(...)`: Wykonuja skrypt z pliku lub bufora.
-   `loadScript(...)`, `loadFunction(...)`: Laduja skrypt/funkcje na stos bez jej wykonywania.
-   `safeCall(...)`: Bezpiecznie wywoluje funkcje na stosie, z obsluga bled�w.
-   `signalCall(...)`: Wysokopoziomowa wersja `safeCall` z dodatkowymi funkcjami.
-   `callGlobalField<R, ...T>(...)`: Wygodna metoda do wywolywania globalnej funkcji Lua z C++ i otrzymywania wyniku.
# # # # Manipulacja stosem i typami
-   `push...()` / `pop...()` / `to...()` / `is...()`: Zestaw metod do pracy ze stosem Lua dla r�znych typ�w danych (np. `pushInteger`, `isString`, `toObject`).
-   `getTop()`: Zwraca rozmiar stosu.
-   `ref()` / `unref()`: Do tworzenia i zwalniania trwalych referencji do wartosci Lua.
-   `polymorphicPush<T>(...)`: Szablonowa metoda do umieszczania na stosie dowolnego typu, dla kt�rego zdefiniowano `push_luavalue`.
-   `castValue<T>(...)`: Szablonowa metoda do rzutowania wartosci ze stosu na typ C++, uzywajac `luavalue_cast`.
# # # Zmienne prywatne

-   `L`: Wskaznik na `lua_State`.
-   `m_weakTableRef`: Referencja do tabeli ze slabymi referencjami.
-   `m_cppCallbackDepth`: Licznik zagniezdzenia wywolan zwrotnych C++.
-   `m_totalObjRefs`, `m_totalFuncRefs`: Liczniki do sledzenia alokacji.
-   `m_globalEnv`: Referencja do globalnego srodowiska Lua.
# # Dolaczane pliki
Plik ten na koncu dolacza trzy kluczowe pliki, kt�re sa od niego zalezne i rozszerzaja jego funkcjonalnosc:
-   `luaexception.h`: Definicje wyjatk�w.
-   `luabinder.h`: Maszyneria do bindowania funkcji.
-   `luavaluecasts.h`: Implementacje `push_luavalue` i `luavalue_cast` dla r�znych typ�w.
# # Zaleznosci i powiazania

-   Jest to centralny plik dla calego podsystemu Lua.
-   Zalezny od `framework/luaengine/declarations.h`.
-   Uzywany przez praktycznie kazda czesc aplikacji, kt�ra wchodzi w interakcje z Lua.

---
# ?? luaobject.cpp
# # Opis og�lny

Plik `luaobject.cpp` zawiera implementacje klasy `LuaObject`, kt�ra jest klasa bazowa dla wszystkich obiekt�w C++, kt�re maja byc dostepne w srodowisku Lua.
# # Klasa `LuaObject`
# # # `LuaObject::LuaObject()`

Konstruktor. Inicjalizuje `m_fieldsTableRef` na -1, co oznacza, ze obiekt nie ma jeszcze przypisanej tabeli p�l w Lua.
# # # `LuaObject::~LuaObject()`

Destruktor. Wywoluje `releaseLuaFieldsTable()`, aby zwolnic referencje do tabeli p�l w Lua, co pozwala garbage collectorowi na jej usuniecie. Sprawdza r�wniez, czy nie jest wywolywany podczas zamykania aplikacji.
# # # `bool LuaObject::hasLuaField(const std::string& field)`

Sprawdza, czy obiekt posiada pole o danej nazwie w swojej tabeli p�l Lua.
# # # `void LuaObject::releaseLuaFieldsTable()`

Zwalnia referencje do tabeli p�l (`m_fieldsTableRef`), jesli istnieje.
# # # `void LuaObject::luaSetField(const std::string& key)`
# # # # Opis semantyczny
Ustawia pole w tabeli Lua powiazanej z tym obiektem. Wartosc do ustawienia musi znajdowac sie na szczycie stosu Lua.
# # # # Dzialanie
1.  Jesli obiekt nie ma jeszcze tabeli p�l (`m_fieldsTableRef == -1`), tworzy nowa tabele w Lua i zapisuje do niej referencje.
2.  Pobiera tabele p�l na stos Lua.
3.  Przenosi wartosc ze szczytu stosu na odpowiednie miejsce.
4.  Ustawia pole w tabeli za pomoca `g_lua.setField(key)`.
5.  Zdejmuje tabele p�l ze stosu.
# # # `void LuaObject::luaGetField(const std::string& key)`

Pobiera wartosc pola z tabeli Lua obiektu i umieszcza ja na szczycie stosu. Jesli tabela p�l nie istnieje, umieszcza `nil`.
# # # `void LuaObject::luaGetMetatable()`

Pobiera i umieszcza na stosie metatabele dla klasy tego obiektu. Uzywa statycznej mapy (`metatableMap`) do cachowania referencji do metatabel dla kazdego typu klasy, aby uniknac wielokrotnego wyszukiwania ich w globalnym srodowisku Lua.
# # # `void LuaObject::luaGetFieldsTable()`

Umieszcza na stosie tabele p�l tego obiektu, lub `nil`, jesli ona nie istnieje.
# # # `int LuaObject::getUseCount()`

Zwraca liczbe referencji do obiektu (`shared_object::ref_count()`).
# # # `std::string LuaObject::getClassName()`

Zwraca zdemanglowana nazwe klasy obiektu, kt�ra jest uzywana do znalezienia odpowiedniej metatabeli w Lua.
# # Zaleznosci i powiazania

-   `framework/luaengine/luaobject.h`: Plik nagl�wkowy.
-   `framework/luaengine/luainterface.h`: Intensywnie korzysta z `g_lua` do wszystkich operacji na stanie Lua.
-   `framework/core/application.h`: Do sprawdzania stanu aplikacji.
-   Jest klasa bazowa dla setek innych klas w projekcie, kt�re sa eksportowane do Lua.

---
# ?? luaobject.h
# # Opis og�lny

Plik `luaobject.h` deklaruje klase `LuaObject`, kt�ra jest fundamentalna klasa bazowa dla wszystkich obiekt�w C++, kt�re maja byc widoczne i zarzadzane przez silnik Lua.
# # Klasa `LuaObject`
# # # Opis semantyczny
`LuaObject` dziedziczy po `stdext::shared_object`, co zapewnia zarzadzanie czasem zycia obiektu za pomoca licznika referencji. Dodaje funkcjonalnosc, kt�ra pozwala na dynamiczne dolaczanie do obiektu C++ p�l i metod z poziomu Lua. Kazda instancja `LuaObject` moze posiadac wlasna, unikalna tabele w Lua (`m_fieldsTableRef`), w kt�rej przechowywane sa te dynamiczne dane.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Szablonowe metody do interakcji z Lua** | |
| `connectLuaField(...)`| Laczy funkcje C++ (`std::function`) z polem Lua, tworzac lub rozszerzajac tabele callback�w. |
| `luaCallLuaField(...)`| Wywoluje funkcje przechowywana w polu Lua tego obiektu. |
| `callLuaField(...)`| Wysokopoziomowe opakowanie na `luaCallLuaField`, kt�re obsluguje konwersje typ�w zwracanych. |
| `hasLuaField(...)` | Sprawdza, czy obiekt ma pole o danej nazwie w swojej tabeli Lua. |
| `setLuaField(...)` | Ustawia wartosc pola w tabeli Lua. |
| `getLuaField(...)` | Pobiera wartosc pola z tabeli Lua. |
| **Niskopoziomowe metody do interakcji z Lua** | |
| `releaseLuaFieldsTable()`| Zwalnia referencje do tabeli p�l. |
| `luaSetField(...)` | Ustawia pole, pobierajac wartosc ze szczytu stosu Lua. |
| `luaGetField(...)` | Pobiera pole i umieszcza jego wartosc na stosie Lua. |
| `luaGetMetatable()` | Pobiera i umieszcza na stosie metatabele klasy. |
| `luaGetFieldsTable()`| Umieszcza na stosie tabele p�l obiektu. |
| **Metody pomocnicze** | |
| `getUseCount()` | Zwraca liczbe referencji do obiektu. |
| `getClassName()` | Zwraca nazwe klasy. |
# # # Zmienne prywatne

-   `m_fieldsTableRef`: Przechowuje referencje (indeks w rejestrze Lua) do tabeli p�l tego obiektu.
# # # Funkcje globalne (`connect`)

Szablonowe funkcje globalne, kt�re sa wygodnym opakowaniem na `LuaObject::connectLuaField`, pozwalajac na latwe laczenie zar�wno `std::function`, jak i lambd z polami obiekt�w.
# # Zaleznosci i powiazania

-   `framework/util/stats.h`: Potencjalnie do statystyk.
-   `framework/luaengine/declarations.h`: Podstawowe deklaracje.
-   Jest klasa bazowa dla prawie kazdej klasy w projekcie, kt�ra jest eksportowana do Lua (np. `UIWidget`, `Protocol`, `Module`).
-   Oznaczona jako `@bindclass`, jej podstawowe metody (`getUseCount`, `getClassName`, `getFieldsTable`) sa dostepne w Lua.

---
# ?? luavaluecasts.cpp
# # Opis og�lny

Plik `luavaluecasts.cpp` zawiera implementacje specjalizacji szablon�w `push_luavalue` i `luavalue_cast` dla podstawowych typ�w danych. Te funkcje sa sercem systemu konwersji typ�w miedzy C++ a Lua.
# # Funkcje `push_luavalue`
# # # # Opis semantyczny
Kazda funkcja `push_luavalue` przyjmuje wartosc typu C++ i umieszcza jej odpowiednik na szczycie stosu Lua. Zwraca liczbe wartosci umieszczonych na stosie (zwykle 1).
# # # Implementacje:
-   `bool`: `g_lua.pushBoolean(b)`
-   `int`: `g_lua.pushInteger(i)`
-   `double`: `g_lua.pushNumber(d)`
-   `const char*`, `std::string`: `g_lua.pushString(str)`
-   `LuaCppFunction`: `g_lua.pushCppFunction(func)`
-   **Typy zlozone (`Color`, `Rect`, `Point`, `Size`)**: Tworza nowa tabele w Lua i wypelniaja ja odpowiednimi polami (np. `r`, `g`, `b`, `a` dla `Color`).
-   **`OTMLNodePtr`**: Konwertuje wezel OTML na tabele Lua, rekurencyjnie przetwarzajac jego dzieci.
# # Funkcje `luavalue_cast`
# # # # Opis semantyczny
Kazda funkcja `luavalue_cast` pr�buje odczytac wartosc z podanego indeksu na stosie Lua i skonwertowac ja na odpowiedni typ C++. Zwraca `true` w przypadku sukcesu.
# # # Implementacje:
-   `bool`: `g_lua.toBoolean(index)`
-   `int`, `double`: `g_lua.toInteger(index)`, `g_lua.toNumber(index)`. Sprawdzaja dodatkowo, czy wartosc na stosie jest faktycznie liczba.
-   `std::string`: `g_lua.toString(index)`
-   **Typy zlozone (`Color`, `Rect`, ...)**: Sprawdzaja, czy na stosie jest tabela z odpowiednimi polami lub string, kt�ry mozna sparsowac. Odczytuja wartosci z tabeli i przypisuja je do obiektu C++.
-   **`OTMLNodePtr`**: Konwertuje tabele Lua z powrotem na strukture wezl�w OTML.
-   **`LuaObjectPtr`**: Sprawdza, czy na stosie jest `userdata` i rzutuje je na odpowiedni typ wskaznika.
# # Zaleznosci i powiazania

-   `framework/luaengine/luavaluecasts.h`: Plik nagl�wkowy.
-   `framework/luaengine/luainterface.h`: Uzywaja metod `g_lua` do interakcji ze stosem.
-   `framework/otml/otmlnode.h`: Do konwersji wezl�w OTML.
-   Sa to funkcje niskiego poziomu, uzywane przez `LuaInterface::polymorphicPush` i `LuaInterface::castValue` do automatycznej konwersji typ�w.

---
# ?? luavaluecasts.h
# # Opis og�lny

Plik `luavaluecasts.h` deklaruje zestaw szablonowych funkcji `push_luavalue` i `luavalue_cast`, kt�re definiuja, w jaki spos�b r�zne typy danych C++ sa konwertowane do i z wartosci Lua. Jest to kluczowy element systemu bindowania, kt�ry umozliwia automatyczna konwersje argument�w funkcji i wartosci zwracanych.
# # Szablony i funkcje
# # # `push_luavalue<T>(const T& v)`
# # # # Opis
Szablon funkcji, kt�ry przyjmuje wartosc typu `T` i umieszcza jej reprezentacje na stosie Lua. Dla kazdego typu, kt�ry ma byc przekazywany miedzy C++ a Lua, musi istniec specjalizacja tej funkcji.
# # # `luavalue_cast<T>(int index, T& v)`
# # # # Opis
Szablon funkcji, kt�ry pr�buje odczytac wartosc z podanego indeksu `index` na stosie Lua i skonwertowac ja do typu `T`. Zwraca `true`, jesli konwersja sie powiedzie.
# # # Zadeklarowane specjalizacje

Plik deklaruje (a w przypadku typ�w prostych, r�wniez definiuje `inline`) specjalizacje dla:
-   **Typ�w prostych**: `bool`, `int`, `double`, `float`, liczby calkowite o stalym rozmiarze (`int8`, `uint16`, itp.).
-   **String�w**: `const char*`, `std::string`.
-   **Funkcji C++**: `LuaCppFunction`, `std::function`.
-   **Struktur frameworka**: `Color`, `Rect`, `Point`, `Size`.
-   **Wezl�w OTML**: `OTMLNodePtr`.
-   **Typ�w wyliczeniowych (enum)**.
-   **Obiekt�w C++**: `LuaObjectPtr` i wskazniki do klas pochodnych.
-   **Kontener�w STL**: `std::list`, `std::vector`, `std::set`, `std::deque`, `std::map`.
-   **Krotek**: `std::tuple`.
# # # Przyklad dzialania

```cpp
// C++
void myFunction(int a, const std::string& b) { /* ... */ }

// Lua
myFunction(10, "hello")
```
Gdy `myFunction` jest wywolywana z Lua, `luabinder` uzyje:
-   `luavalue_cast(1, int&)` do konwersji `10` z Lua na `int` w C++.
-   `luavalue_cast(2, std::string&)` do konwersji `"hello"` z Lua na `std::string` w C++.
# # Zaleznosci i powiazania

-   Jest to plik wewnetrzny, dolaczany tylko przez `luainterface.h`.
-   Wymaga definicji `LuaInterface`, `LuaObject`, `LuaException`.
-   Jest podstawa calego systemu automatycznej konwersji typ�w, uzywanego przez `luabinder`.

---
# ?? connection.cpp
# # Opis og�lny

Plik `connection.cpp` zawiera implementacje klasy `Connection`, kt�ra jest niskopoziomowym opakowaniem na asynchroniczne gniazdo TCP (TCP socket) z biblioteki Boost.Asio. Zarzadza ona cyklem zycia polaczenia, operacjami odczytu i zapisu oraz obsluga bled�w.
# # Zmienne globalne

-   `g_ioService`: Globalna instancja `boost::asio::io_service`, kt�ra jest sercem petli zdarzen dla wszystkich operacji sieciowych.
-   `Connection::m_outputStreams`: Statyczna lista, kt�ra dziala jak pula bufor�w wyjsciowych. Zuzyte bufory sa do niej zwracane, co pozwala na ich ponowne wykorzystanie i redukuje alokacje pamieci.
# # Klasa `Connection`
# # # `Connection::Connection()`

Konstruktor. Inicjalizuje obiekty Boost.Asio (`timer`, `resolver`, `socket`) powiazane z `g_ioService`.
# # # `void Connection::poll()` i `void Connection::terminate()`

Statyczne metody, kt�re zarzadzaja globalnym `g_ioService`. `poll()` przetwarza zdarzenia sieciowe, a `terminate()` zatrzymuje `io_service`.
# # # `void Connection::close()`

Zamyka polaczenie. Anuluje wszystkie aktywne operacje asynchroniczne, zamyka gniazdo i resetuje callbacki.
# # # `void Connection::connect(...)`

Rozpoczyna proces nawiazywania polaczenia. Wywoluje `m_resolver.async_resolve` w celu przetlumaczenia nazwy hosta na adres IP.
# # # `void Connection::write(uint8* buffer, size_t size)`

Dodaje dane do bufora wyjsciowego (`m_outputStream`). Aby uniknac zator�w (congestion), faktyczne wyslanie danych jest op�zniane o 0 milisekund za pomoca `m_delayedWriteTimer`. Oznacza to, ze wyslanie nastapi w nastepnej iteracji petli `io_service`, co pozwala na zgrupowanie wielu malych zapis�w w jeden wiekszy.
# # # Metody `read(...)`, `read_until(...)`, `read_some(...)`

Inicjuja asynchroniczne operacje odczytu danych z gniazda. Ustawiaja `m_recvCallback`, kt�ry zostanie wywolany po otrzymaniu danych, oraz `m_readTimer` do obslugi timeoutu.
# # # Metody `on...()`

Sa to handlery (funkcje zwrotne) dla operacji asynchronicznych Boost.Asio:
-   `onResolve`: Wywolywana po rozwiazaniu nazwy DNS. Inicjuje polaczenie.
-   `onConnect`: Wywolywana po nawiazaniu polaczenia. Ustawia opcje gniazda (np. `no_delay` - wylaczenie algorytmu Nagle'a) i wywoluje `m_connectCallback`.
-   `onCanWrite`: Wywolywana przez `m_delayedWriteTimer`. Inicjuje faktyczne wyslanie danych.
-   `onWrite`: Wywolywana po zakonczeniu operacji zapisu. Zwraca bufor do puli.
-   `onRecv`: Wywolywana po otrzymaniu danych. Przekazuje dane do `m_recvCallback`.
-   `onTimeout`: Wywolywana, gdy uplynie czas oczekiwania na operacje.
# # # `void Connection::handleError(...)`

Centralna funkcja do obslugi bled�w sieciowych. Zapisuje blad, wywoluje `m_errorCallback` i zamyka polaczenie.
# # Zaleznosci i powiazania

-   `framework/net/connection.h`: Plik nagl�wkowy.
-   `framework/core/application.h`, `eventdispatcher.h`: Do walidacji i planowania zdarzen.
-   `boost/asio`: Kluczowa zaleznosc do obslugi sieci.
-   Jest uzywana przez klase `Protocol` do implementacji protokolu komunikacyjnego z serwerem gry.

---
# ?? server.h
# # Opis og�lny

Plik `server.h` deklaruje klase `Server`, kt�ra jest prostym opakowaniem na `boost::asio::ip::tcp::acceptor`. Umozliwia tworzenie serwera TCP, kt�ry nasluchuje na przychodzace polaczenia na okreslonym porcie.
# # Klasa `Server`
# # # Opis semantyczny
`Server` dziedziczy po `LuaObject`, co pozwala na tworzenie i zarzadzanie serwerami z poziomu skrypt�w Lua. Jego gl�wnym zadaniem jest akceptowanie nowych polaczen i przekazywanie ich do obslugi (np. w formie obiektu `Connection`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Server(int port)` | Konstruktor, tworzy i bindowanie akceptor do podanego portu. |
| `static ServerPtr create(int port)` | Metoda fabryczna, kt�ra tworzy `Server` i opakowuje go w `shared_ptr`. |
| `bool isOpen()` | Zwraca `true`, jesli serwer nasluchuje. |
| `void close()` | Zamyka akceptor, przestajac nasluchiwac. |
| `void acceptNext()` | Inicjuje asynchroniczna operacje oczekiwania na nastepne polaczenie. Po jego nadejsciu, wywolywany jest `callback` `onAccept` w Lua. |
# # # Zmienne prywatne

-   `m_isOpen`: Flaga wskazujaca, czy serwer jest aktywny.
-   `m_acceptor`: Obiekt `tcp::acceptor` z Boost.Asio.
# # Zaleznosci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   `boost/asio`: Uzywa `tcp::acceptor`.
-   Jest uzywana do implementacji serwer�w nasluchujacych w Lua, np. do niestandardowych narzedzi lub protokol�w.

---
# ?? connection.h
# # Opis og�lny

Plik `connection.h` deklaruje klase `Connection`, kt�ra jest interfejsem do asynchronicznego polaczenia TCP. Jest to kluczowy element podsystemu sieciowego.
# # Klasa `Connection`
# # # Opis semantyczny
`Connection` enkapsuluje `boost::asio::ip::tcp::socket` i zarzadza calym cyklem zycia polaczenia: od nawiazywania, przez wysylanie i odbieranie danych, az po zamykanie i obsluge bled�w. Dziala w pelni asynchronicznie, integrujac sie z globalna petla zdarzen `g_ioService`. Dziedziczy po `LuaObject`, co umozliwia jej uzycie w Lua.
# # # Stale

-   `READ_TIMEOUT`, `WRITE_TIMEOUT`: Czas (w sekundach) na zakonczenie operacji odczytu/zapisu.
-   `SEND_BUFFER_SIZE`, `RECV_BUFFER_SIZE`: Rozmiary bufor�w.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Statyczne** | |
| `static void poll()` | Przetwarza zdarzenia w globalnym `g_ioService`. |
| `static void terminate()` | Zatrzymuje `g_ioService`. |
| **Cykl zycia** | |
| `void connect(...)` | Rozpoczyna asynchroniczne nawiazywanie polaczenia. |
| `void close()` | Zamyka polaczenie. |
| **Operacje I/O** | |
| `void write(...)` | Dodaje dane do kolejki wysylania. |
| `void read(...)` | Rozpoczyna asynchroniczny odczyt okreslonej liczby bajt�w. |
| `void read_until(...)` | Odczytuje dane az do napotkania okreslonego separatora. |
| `void read_some(...)` | Odczytuje dowolna ilosc dostepnych danych (nie wiecej niz rozmiar bufora). |
| **Callbacki i stan** | |
| `void setErrorCallback(...)`| Ustawia funkcje zwrotna dla bled�w. |
| `int getIp()` | Zwraca adres IP zdalnego hosta. |
| `boost::system::error_code getError()` | Zwraca ostatni blad. |
| `bool isConnecting()` | Zwraca `true`, jesli trwa nawiazywanie polaczenia. |
| `bool isConnected()` | Zwraca `true`, jesli polaczenie jest aktywne. |
| `ticks_t getElapsedTicksSinceLastRead()` | Zwraca czas od ostatniej operacji odczytu (do wykrywania timeout�w na wyzszym poziomie). |
# # # Zmienne chronione

-   `m_connectCallback`, `m_errorCallback`, `m_recvCallback`: Funkcje zwrotne.
-   `m_readTimer`, `m_writeTimer`, ...: Obiekty Boost.Asio (timery, resolver, socket).
-   `m_outputStream`, `m_inputStream`: Bufory do zapisu i odczytu.
-   `m_connected`, `m_connecting`: Flagi stanu.
# # Zaleznosci i powiazania

-   `framework/net/declarations.h`: Deklaracje typ�w.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/core/timer.h`: Do sledzenia aktywnosci.
-   Jest uzywana przez `Protocol` do komunikacji z serwerem gry.
-   Jest zwracana przez `Server` po zaakceptowaniu nowego polaczenia.

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `net` sluzy do wczesnych deklaracji (forward declarations) i definicji typ�w wskaznik�w dla klas zwiazanych z obsluga sieci. Pomaga to unikac zaleznosci cyklicznych i skraca czas kompilacji.
# # Deklaracje
# # # `namespace asio`

Deklaruje, ze `asio` jest aliasem dla `boost::asio`.
# # # Wczesne deklaracje klas

-   `InputMessage`
-   `OutputMessage`
-   `Connection`
-   `Protocol`
-   `Server`
-   `PacketPlayer`
-   `PacketRecorder`
# # # Definicje typ�w

Definiuje aliasy dla inteligentnych wskaznik�w (`shared_object_ptr`) do klas sieciowych.

-   `InputMessagePtr`
-   `OutputMessagePtr`
-   `ConnectionPtr`
-   `ProtocolPtr`
-   `ServerPtr`
-   `PacketPlayerPtr`
-   `PacketRecorderPtr`
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest dolaczany przez wiekszosc plik�w nagl�wkowych w module `net`.

---
# ?? inputmessage.h
# # Opis og�lny

Plik `inputmessage.h` deklaruje klase `InputMessage`, kt�ra jest narzedziem do parsowania przychodzacych pakiet�w sieciowych.
# # Klasa `InputMessage`
# # # Opis semantyczny
`InputMessage` dziala jak bufor z wskaznikiem odczytu. Przechowuje surowe dane pakietu i udostepnia metody do sekwencyjnego odczytywania z niego r�znych typ�w danych (np. `getU8`, `getU16`, `getString`). Zarzadza r�wniez pozycja nagl�wka, co pozwala na oddzielenie metadanych pakietu (rozmiar, suma kontrolna) od jego wlasciwej zawartosci (ciala).
# # # Stale

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_HEADER_SIZE`: Maksymalny rozmiar nagl�wka (rezerwowane miejsce na poczatku bufora).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setBuffer(...)` | Kopiuje dane z `std::string` do wewnetrznego bufora. |
| `getBuffer()` | Zwraca caly pakiet (nagl�wek + cialo) jako `std::string`. |
| `getBodyBuffer()`| Zwraca tylko cialo pakietu. |
| `skipBytes(uint32 bytes)` | Przesuwa wskaznik odczytu. |
| `getU8()`, `getU16()`, `getU32()`, `getU64()` | Odczytuja liczby calkowite bez znaku. |
| `getString()` | Odczytuje string (poprzedzony dlugoscia U16). |
| `getDouble()` | Odczytuje liczbe zmiennoprzecinkowa w niestandardowym formacie. |
| `peekU8()`, ... | Odczytuja wartosc bez przesuwania wskaznika. |
| `decryptRsa(...)` | Deszyfruje fragment bufora za pomoca RSA. |
| `getHeaderSize()`, `getMessageSize()`, `getUnreadSize()` | Zwracaja informacje o rozmiarach. |
| `eof()` | Zwraca `true`, jesli wszystkie dane zostaly odczytane. |
# # # Metody chronione (uzywane przez `Protocol`)

-   `reset()`: Resetuje stan wiadomosci.
-   `fillBuffer(...)`: Dopisuje dane do bufora.
-   `setHeaderSize(...)`: Ustawia rozmiar nagl�wka.
-   `readChecksum()`: Odczytuje i weryfikuje sume kontrolna.
# # # Zmienne prywatne

-   `m_headerPos`: Pozycja startowa nagl�wka.
-   `m_readPos`: Aktualna pozycja odczytu.
-   `m_messageSize`: Calkowity rozmiar wiadomosci (bez nagl�wka).
-   `m_buffer`: Bufor na dane.
# # Zaleznosci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostepna w Lua.
-   Jest tworzona i zarzadzana przez `Protocol` do parsowania danych otrzymanych z `Connection`.

---
# ?? outputmessage.cpp
# # Opis og�lny

Plik `outputmessage.cpp` zawiera implementacje klasy `OutputMessage`, kt�ra sluzy do budowania wychodzacych pakiet�w sieciowych.
# # Klasa `OutputMessage`
# # # `OutputMessage::OutputMessage()`

Konstruktor, wywoluje `reset()`.
# # # `void OutputMessage::reset()`

Resetuje stan wiadomosci, ustawiajac wskaznik zapisu (`m_writePos`) i pozycje nagl�wka (`m_headerPos`) na poczatek obszaru na cialo wiadomosci.
# # # `void OutputMessage::setBuffer(const std::string& buffer)`

Kopiuje dane z `std::string` do bufora wiadomosci.
# # # Metody `add...()`

Sluza do dodawania r�znych typ�w danych na koniec wiadomosci.
-   `addU8`, `addU16`, `addU32`, `addU64`: Dodaja liczby calkowite, konwertujac je do porzadku Little Endian.
-   `addString`: Dodaje `std::string`, poprzedzajac go 2-bajtowa dlugoscia.
-   `addRawString`: Dodaje `std::string` bez informacji o dlugosci.
-   `addPaddingBytes`: Dodaje okreslona liczbe bajt�w wypelniajacych.
-   Kazda z tych metod wywoluje `checkWrite` w celu sprawdzenia, czy jest wystarczajaco miejsca w buforze.
# # # `void OutputMessage::encryptRsa()`

Szyfruje ostatnie `N` bajt�w bufora za pomoca klucza publicznego RSA, gdzie `N` to rozmiar klucza.
# # # Metody `write...()`

Metody te operuja na zarezerwowanym miejscu na nagl�wek (przed cialem wiadomosci):
-   `writeChecksum()`: Oblicza sume kontrolna Adler-32 dla ciala wiadomosci i zapisuje ja w nagl�wku.
-   `writeSequence()`: Zapisuje numer sekwencyjny pakietu.
-   `writeMessageSize()`: Zapisuje calkowity rozmiar ciala wiadomosci w nagl�wku.
# # # `void OutputMessage::checkWrite(int bytes)`

Sprawdza, czy dodanie `bytes` bajt�w nie przekroczy maksymalnego rozmiaru bufora. Jesli tak, rzuca wyjatek.
# # Zaleznosci i powiazania

-   `framework/net/outputmessage.h`: Plik nagl�wkowy.
-   `framework/util/crypt.h`: Uzywa `g_crypt` do szyfrowania RSA i `stdext::adler32` do sum kontrolnych.
-   Jest tworzona przez kod logiki gry, wypelniana danymi, a nastepnie przekazywana do `Protocol::send()` w celu wyslania.

---
# ?? outputmessage.h
# # Opis og�lny

Plik `outputmessage.h` deklaruje klase `OutputMessage`, kt�ra jest narzedziem do konstruowania wychodzacych pakiet�w sieciowych.
# # Klasa `OutputMessage`
# # # Opis semantyczny
`OutputMessage` dziala jak bufor z wskaznikiem zapisu. Udostepnia metody do dodawania r�znych typ�w danych (`addU8`, `addString`, itp.), kt�re sa dolaczane na koncu bufora. Posiada r�wniez zarezerwowane miejsce na poczatku bufora na nagl�wek, kt�ry jest wypelniany tuz przed wyslaniem (np. rozmiarem wiadomosci, suma kontrolna).
# # # Stale

-   `BUFFER_MAXSIZE`: Maksymalny rozmiar bufora.
-   `MAX_STRING_LENGTH`: Maksymalna dlugosc stringa.
-   `MAX_HEADER_SIZE`: Rozmiar zarezerwowanego miejsca na nagl�wek.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `reset()` | Resetuje wiadomosc do stanu poczatkowego. |
| `setBuffer(...)` | Ustawia zawartosc ciala wiadomosci. |
| `getBuffer()` | Zwraca gotowy pakiet (nagl�wek + cialo) jako `std::string`. |
| `addU8()`, ..., `addString()` | Dodaja dane do ciala wiadomosci. |
| `encryptRsa()` | Szyfruje czesc wiadomosci za pomoca RSA. |
| `getWritePos()` | Zwraca aktualna pozycje zapisu. |
| `getMessageSize()` | Zwraca aktualny rozmiar ciala wiadomosci. |
| `setWritePos(...)`, `setMessageSize(...)` | Ustawiaja pozycje zapisu i rozmiar. |
# # # Metody chronione (uzywane przez `Protocol`)

-   `getHeaderBuffer()`: Zwraca wskaznik na poczatek gotowego pakietu (poczatek nagl�wka).
-   `writeChecksum()`, `writeSequence()`, `writeMessageSize()`: Wypelniaja nagl�rek odpowiednimi metadanymi.
# # # Zmienne prywatne

-   `m_headerPos`: Aktualna pozycja poczatku nagl�wka.
-   `m_writePos`: Aktualna pozycja zapisu w ciele wiadomosci.
-   `m_messageSize`: Rozmiar calego pakietu (nagl�wek + cialo).
-   `m_buffer`: Bufor na dane.
# # Zaleznosci i powiazania

-   `framework/net/declarations.h`: Podstawowe deklaracje.
-   `framework/luaengine/luaobject.h`: Dziedziczy z `LuaObject`.
-   Oznaczona jako `@bindclass`, jest dostepna w Lua do tworzenia pakiet�w.
-   Jest uzywana przez `Protocol` do przygotowania pakiet�w do wyslania przez `Connection`.

---
# ?? packet_player.cpp
# # Opis og�lny

Plik `packet_player.cpp` zawiera implementacje klasy `PacketPlayer`, kt�ra umozliwia odtwarzanie wczesniej nagranych sesji sieciowych. Jest to narzedzie do debugowania i testowania.
# # Klasa `PacketPlayer`
# # # `PacketPlayer::PacketPlayer(const std::string& file)`

Konstruktor.
-   **Dzialanie**:
    1.  Otwiera plik nagrania z katalogu `records/`.
    2.  Czyta plik linia po linii.
    3.  Kazda linia zawiera typ pakietu (`<` dla przychodzacego, `>` dla wychodzacego), sygnature czasowa i dane pakietu w formacie heksadecymalnym.
    4.  Dekoduje dane heksadecymalne do postaci binarnej i zapisuje pakiety w odpowiednich kolejkach (`m_input` lub `m_output`).
# # # `PacketPlayer::~PacketPlayer()`

Destruktor. Anuluje zaplanowane zdarzenie (`m_event`), jesli istnieje.
# # # `void PacketPlayer::start(...)`

Rozpoczyna odtwarzanie.
-   **Dzialanie**:
    1.  Zapisuje czas startu (`m_start`).
    2.  Zapisuje callbacki do obslugi "otrzymanych" pakiet�w i zdarzenia rozlaczenia.
    3.  Planuje pierwsze wywolanie metody `process()` za 50ms.
# # # `void PacketPlayer::stop()`

Zatrzymuje odtwarzanie, anulujac zdarzenie.
# # # `void PacketPlayer::onOutputPacket(const OutputMessagePtr& packet)`

Metoda wywolywana przez `Protocol`, gdy pr�buje on wyslac pakiet. W trybie odtwarzania, pakiety wychodzace sa analizowane (np. w celu wykrycia wylogowania), ale nie sa nigdzie wysylane.
# # # `void PacketPlayer::process()`
# # # # Opis semantyczny
Gl�wna metoda petli odtwarzacza.
# # # # Dzialanie
1.  Iteruje po kolejce pakiet�w przychodzacych (`m_input`).
2.  Sprawdza sygnature czasowa kazdego pakietu. Jesli czas odtworzenia pakietu (`packet.first + m_start`) juz minal, wywoluje `m_recvCallback` z danymi pakietu i usuwa go z kolejki.
3.  Jesli kolejka nie jest pusta, planuje swoje nastepne wywolanie z op�znieniem r�wnym r�znicy czasu do nastepnego pakietu.
4.  Jesli kolejka jest pusta, wywoluje `m_disconnectCallback`, symulujac koniec sesji.
# # Zaleznosci i powiazania

-   `framework/net/packet_player.h`: Plik nagl�wkowy.
-   `framework/core/clock.h`, `eventdispatcher.h`: Do zarzadzania czasem i planowania zdarzen.
-   `boost/algorithm/hex.hpp`: Do dekodowania danych z formatu heksadecymalnego.
-   Jest uzywana przez `Protocol` w trybie odtwarzania.

---
# ?? packet_player.h
# # Opis og�lny

Plik `packet_player.h` deklaruje klase `PacketPlayer`, kt�ra sluzy do odtwarzania nagranych sesji sieciowych z plik�w.
# # Klasa `PacketPlayer`
# # # Opis semantyczny
`PacketPlayer` odczytuje plik z zarejestrowanymi pakietami i ich sygnaturami czasowymi. Po uruchomieniu, symuluje przychodzace pakiety sieciowe, wywolujac `callback` w odpowiednich odstepach czasu, zgodnie z nagraniem. Pozwala to na debugowanie i testowanie logiki klienta bez potrzeby laczenia sie z serwerem. Dziedziczy po `LuaObject`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketPlayer(const std::string& file)` | Konstruktor, laduje nagranie z pliku. |
| `virtual ~PacketPlayer()` | Destruktor. |
| `void start(...)` | Rozpoczyna odtwarzanie sesji. Przyjmuje callbacki na otrzymanie pakietu i na rozlaczenie. |
| `void stop()` | Zatrzymuje odtwarzanie. |
| `void onOutputPacket(...)` | Przechwytuje pakiety, kt�re normalnie bylyby wyslane, w celu symulacji (np. wykrycia wylogowania). |
# # # Zmienne prywatne

-   `m_start`: Czas rozpoczecia odtwarzania.
-   `m_event`: Wskaznik na zaplanowane zdarzenie do przetwarzania pakiet�w.
-   `m_input`, `m_output`: Kolejki (`std::deque`) przechowujace pary (czas, dane pakietu) dla pakiet�w przychodzacych i wychodzacych.
-   `m_recvCallback`: `Callback` wywolywany z danymi "otrzymanego" pakietu.
-   `m_disconnectCallback`: `Callback` wywolywany na koniec sesji.
# # Zaleznosci i powiazania

-   `framework/core/eventdispatcher.h`: Do planowania zdarzen.
-   `framework/net/outputmessage.h`: Do analizy pakiet�w wychodzacych.
-   Jest tworzona i uzywana przez `Protocol` w trybie odtwarzania.

---
# ?? protocol.h
# # Opis og�lny

Plik `protocol.h` deklaruje klase `Protocol`, kt�ra jest klasa bazowa do implementacji protokol�w komunikacji sieciowej.
# # Klasa `Protocol`
# # # Opis semantyczny
`Protocol` jest abstrakcja wysokiego poziomu, kt�ra zarzadza polaczeniem (`Connection`) i implementuje logike specyficzna dla danego protokolu, taka jak szyfrowanie XTEA, obsluga sum kontrolnych, kompresja i sekwencjonowanie pakiet�w. Przetwarza surowe dane z `Connection` na obiekty `InputMessage` i przygotowuje `OutputMessage` do wyslania. Dziedziczy po `LuaObject`, co pozwala na tworzenie implementacji protokol�w w Lua.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `connect(...)` | Nawiazuje polaczenie z serwerem. |
| `disconnect()` | Zamyka polaczenie. |
| `setRecorder(...)` / `playRecord(...)` | Wlacza tryb nagrywania lub odtwarzania sesji. |
| `bool isConnected()` / `isConnecting()` | Zwracaja stan polaczenia. |
| `ConnectionPtr getConnection()` | Zwraca obiekt `Connection`. |
| **Konfiguracja protokolu** | |
| `generateXteaKey()`, `setXteaKey(...)`, `enableXteaEncryption()` | Zarzadzaja szyfrowaniem XTEA. |
| `enableChecksum()`, `enabledSequencedPackets()`, `enableBigPackets()`, `enableCompression()` | Wlaczaja r�zne cechy protokolu. |
| **Operacje I/O** | |
| `virtual void send(...)` | Wysyla `OutputMessage`, opcjonalnie szyfrujac i dodajac nagl�wki. |
| `virtual void recv()` | Inicjuje proces odbierania nastepnego pakietu. |
# # # Metody chronione

-   `onConnect()`: Wirtualna metoda wywolywana po nawiazaniu polaczenia. Domyslnie wywoluje `onConnect` w Lua.
-   `onRecv(...)`: Wirtualna metoda wywolywana po otrzymaniu i zdeserializowaniu pelnego pakietu. Domyslnie wywoluje `onRecv` w Lua.
-   `onError(...)`: Wirtualna metoda wywolywana w przypadku bledu sieciowego.
# # # Zmienne

-   `m_xteaKey`: Klucz XTEA.
-   `m_packetNumber`: Licznik dla pakiet�w sekwencyjnych.
-   `m_player`, `m_recorder`: Wskazniki na obiekty do odtwarzania/nagrywania.
-   `m_checksumEnabled`, `m_xteaEncryptionEnabled`, ...: Flagi konfiguracji protokolu.
-   `m_connection`: Wskaznik na obiekt `Connection`.
-   `m_inputMessage`: Bufor na przychodzace dane.
-   `m_zstream`: Strumien ZLIB do dekompresji.
# # Zaleznosci i powiazania

-   `framework/net/declarations.h`, `inputmessage.h`, `outputmessage.h`, `connection.h`: Podstawowe klasy sieciowe.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/proxy/proxy.h`: Do integracji z systemem proxy.
-   Oznaczona jako `@bindclass`, jest kluczowym elementem do implementacji logiki sieciowej w Lua.

---
# ?? packet_recorder.cpp
# # Opis og�lny

Plik `packet_recorder.cpp` zawiera implementacje klasy `PacketRecorder`, kt�ra sluzy do nagrywania sesji sieciowej do pliku tekstowego.
# # Klasa `PacketRecorder`
# # # `PacketRecorder::PacketRecorder(const std::string& file)`

Konstruktor.
-   **Dzialanie**:
    1.  Zapisuje czas startu nagrywania (`m_start`).
    2.  Tworzy katalog `records/`, jesli nie istnieje.
    3.  Otwiera plik o podanej nazwie w tym katalogu do zapisu.
# # # `void PacketRecorder::addInputPacket(const InputMessagePtr& packet)`

Nagrywa pakiet przychodzacy.
-   **Dzialanie**:
    1.  Zapisuje do pliku znacznik `<`.
    2.  Zapisuje r�znice czasu od startu nagrywania.
    3.  Zapisuje zawartosc ciala pakietu w formacie heksadecymalnym.
    4.  Dodaje znak nowej linii.
# # # `void PacketRecorder::addOutputPacket(const OutputMessagePtr& packet)`

Nagrywa pakiet wychodzacy.
-   **Dzialanie**:
    1.  Ignoruje pierwszy pakiet wychodzacy (kt�ry zazwyczaj zawiera login i haslo), aby nie zapisywac wrazliwych danych.
    2.  Zapisuje do pliku znacznik `>`.
    3.  Zapisuje r�znice czasu.
    4.  Zapisuje cala zawartosc pakietu (wraz z nagl�wkiem) w formacie heksadecymalnym.
    5.  Dodaje znak nowej linii.
# # Zaleznosci i powiazania

-   `framework/net/packet_recorder.h`: Plik nagl�wkowy.
-   `framework/core/clock.h`, `resourcemanager.h`: Do zarzadzania czasem i plikami.
-   `boost/algorithm/hex.hpp`: Do konwersji danych binarnych na format heksadecymalny.
-   Jest uzywana przez `Protocol`, gdy wlaczony jest tryb nagrywania.

---
# ?? protocol.cpp
# # Opis og�lny

Plik `protocol.cpp` zawiera implementacje klasy `Protocol`, kt�ra stanowi baze dla protokol�w komunikacyjnych. Implementuje ona logike niskiego poziomu, taka jak szyfrowanie, sumy kontrolne i kompresje, delegujac obsluge samych pakiet�w do skrypt�w Lua.
# # Klasa `Protocol`
# # # `Protocol::Protocol()`

Konstruktor. Inicjalizuje domyslne flagi protokolu na `false` i przygotowuje strumien ZLIB do dekompresji.
# # # `void Protocol::connect(const std::string& host, uint16 port)`

Rozpoczyna polaczenie. Jesli `host` to "proxy" lub inny specjalny adres, uzywa `g_proxy`. W przeciwnym razie tworzy nowy `Connection`.
# # # `void Protocol::disconnect()`

Zamyka polaczenie, zwalniajac `Connection` lub sesje proxy.
# # # `void Protocol::send(const OutputMessagePtr& outputMessage, bool rawPacket)`
# # # # Opis semantyczny
Przygotowuje i wysyla pakiet.
# # # # Dzialanie
1.  Jesli wlaczone jest nagrywanie, zapisuje pakiet.
2.  Jesli `rawPacket` jest `false`:
    -   Szyfruje pakiet za pomoca XTEA, jesli wlaczone.
    -   Dodaje sume kontrolna lub numer sekwencyjny.
    -   Dodaje rozmiar pakietu na poczatku.
3.  Wysyla gotowy pakiet przez `Connection` lub `Proxy`.
4.  Resetuje `outputMessage`, aby m�gl byc ponownie uzyty.
# # # `void Protocol::recv()`

Rozpoczyna proces odbierania nowego pakietu, instruujac `Connection`, aby najpierw odczytal nagl�wek o odpowiedniej dlugosci.
# # # `void Protocol::internalRecvHeader(...)` i `internalRecvData(...)`

Handlery wywolywane przez `Connection`. `internalRecvHeader` odczytuje rozmiar ciala pakietu, a `internalRecvData` odczytuje reszte danych. `internalRecvData` nastepnie wykonuje deszyfrowanie, weryfikacje sumy kontrolnej i dekompresje, a na koncu wywoluje `onRecv` z gotowym `InputMessage`.
# # # `void Protocol::generateXteaKey()` i `setXteaKey(...)`

Metody do zarzadzania kluczem szyfrowania XTEA.
# # # `bool Protocol::xteaDecrypt(...)` i `void Protocol::xteaEncrypt(...)`

Implementacje algorytmu XTEA do szyfrowania i deszyfrowania bufor�w wiadomosci.
# # # `void Protocol::onConnect()`, `onRecv(...)`, `onError(...)`

Metody wirtualne, kt�re domyslnie wywoluja odpowiednie funkcje w Lua (`onConnect`, `onRecv`, `onError`), przekazujac im kontrole nad logika protokolu.
# # Zaleznosci i powiazania

-   `framework/net/protocol.h`: Plik nagl�wkowy.
-   `framework/net/connection.h`, `packet_player.h`, `packet_recorder.h`: Komponenty sieciowe.
-   `framework/proxy/proxy.h`: Do integracji z proxy.
-   **ZLIB**: Do kompresji/dekompresji.
-   Jest to kluczowa klasa, kt�ra jest dziedziczona (w Lua) w celu zaimplementowania konkretnego protokolu gry.

---
# ?? server.cpp
# # Opis og�lny

Plik `server.cpp` zawiera implementacje klasy `Server`, kt�ra umozliwia tworzenie prostych serwer�w TCP nasluchujacych na przychodzace polaczenia.
# # Zmienne globalne
# # # `g_ioService`

Globalny `io_service` z Boost.Asio, uzywany r�wniez przez `Connection`, na kt�rym dziala akceptor serwera.
# # Klasa `Server`
# # # `Server::Server(int port)`

Konstruktor. Tworzy i otwiera obiekt `boost::asio::ip::tcp::acceptor`, bindowanie go do wszystkich interfejs�w (`tcp::v4()`) na podanym porcie.
# # # `ServerPtr Server::create(int port)`

Statyczna metoda fabryczna. Tworzy obiekt `Server`, opakowujac go w `shared_ptr`. Obsluguje wyjatki, kt�re moga wystapic, jesli port jest juz zajety.
# # # `void Server::close()`

Zamyka serwer. Anuluje wszystkie oczekujace operacje akceptowania i zamyka akceptor.
# # # `void Server::acceptNext()`
# # # # Opis semantyczny
Rozpoczyna asynchroniczne oczekiwanie na nowe polaczenie.
# # # # Dzialanie
1.  Tworzy nowy, pusty obiekt `Connection`.
2.  Wywoluje `m_acceptor.async_accept`, przekazujac jej gniazdo nowego `Connection` oraz `callback` (lambde).
3.  Gdy nowe polaczenie zostanie nawiazane, `callback` jest wywolywany.
4.  `Callback` ustawia stan `Connection` na `connected` i wywoluje funkcje `onAccept` w skrypcie Lua, przekazujac jej nowy obiekt `Connection` oraz ewentualny kod bledu.
# # Zaleznosci i powiazania

-   `framework/net/server.h`: Plik nagl�wkowy.
-   `framework/net/connection.h`: Tworzy obiekty `Connection` dla nowych polaczen.
-   `boost/asio`: Uzywa `tcp::acceptor`.
-   Jest przeznaczona do uzytku w Lua, co pozwala na tworzenie np. prostych serwer�w pomocniczych, serwer�w proxy lub narzedzi deweloperskich.

---
# ?? inputmessage.cpp
# # Opis og�lny

Plik `inputmessage.cpp` zawiera implementacje klasy `InputMessage`, kt�ra jest narzedziem do parsowania przychodzacych pakiet�w sieciowych.
# # Klasa `InputMessage`
# # # `InputMessage::InputMessage()`

Konstruktor, wywoluje `reset()`.
# # # `void InputMessage::reset()`

Resetuje stan wiadomosci do wartosci poczatkowych, ustawiajac pozycje odczytu i nagl�wka na `MAX_HEADER_SIZE`.
# # # `void InputMessage::setBuffer(const std::string& buffer)`

Ustawia zawartosc ciala wiadomosci, kopiujac dane z `std::string` do wewnetrznego bufora.
# # # Metody `get...()`

Odczytuja dane z bufora, zaczynajac od biezacej pozycji `m_readPos`.
-   Kazda metoda najpierw wywoluje `checkRead`, aby upewnic sie, ze jest wystarczajaco duzo danych do odczytania.
-   Nastepnie odczytuje dane z bufora, konwertujac je z porzadku Little Endian, jesli to konieczne.
-   Na koniec przesuwa wskaznik `m_readPos`.
-   `getString` najpierw odczytuje 2-bajtowa dlugosc, a potem sam string.
-   `getDouble` odczytuje niestandardowy format liczby zmiennoprzecinkowej.
# # # `bool InputMessage::decryptRsa(int size)`

Deszyfruje `size` bajt�w z biezacej pozycji za pomoca klucza prywatnego RSA. Zwraca `true`, jesli pierwszy zdeszyfrowany bajt to 0.
# # # `void InputMessage::fillBuffer(...)`

Dopisuje surowe dane do bufora w biezacej pozycji odczytu (uzywane przez `Protocol` podczas odbierania danych z gniazda).
# # # `void InputMessage::setHeaderSize(uint32 size)`

Ustawia pozycje poczatku nagl�wka (`m_headerPos`), co efektywnie okresla jego rozmiar.
# # # `bool InputMessage::readChecksum()`

Odczytuje 4-bajtowa sume kontrolna z bufora, oblicza sume kontrolna Adler-32 dla reszty danych i por�wnuje je.
# # # `void InputMessage::checkRead(int bytes)`

Prywatna metoda, kt�ra rzuca wyjatek, jesli pr�ba odczytu `bytes` bajt�w wykroczylaby poza granice wiadomosci.
# # Zaleznosci i powiazania

-   `framework/net/inputmessage.h`: Plik nagl�wkowy.
-   `framework/util/crypt.h`: Do deszyfracji RSA.
-   `client/map.h`: Potencjalna zaleznosc, byc moze z starszej wersji.
-   Jest uzywana przez `Protocol` do reprezentowania i parsowania przychodzacych pakiet�w.

---
# ?? packet_recorder.h
# # Opis og�lny

Plik `packet_recorder.h` deklaruje klase `PacketRecorder`, kt�ra sluzy do nagrywania sesji sieciowej do pliku tekstowego w celu p�zniejszej analizy lub odtworzenia.
# # Klasa `PacketRecorder`
# # # Opis semantyczny
`PacketRecorder` przechwytuje pakiety przychodzace (`InputMessage`) i wychodzace (`OutputMessage`) i zapisuje je w czytelnym formacie do pliku. Kazdy wpis zawiera znacznik kierunku (`<` lub `>`), sygnature czasowa i zawartosc pakietu w postaci heksadecymalnej. Dziedziczy po `LuaObject`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `PacketRecorder(const std::string& file)` | Konstruktor, otwiera plik do zapisu. |
| `virtual ~PacketRecorder()` | Destruktor. |
| `void addInputPacket(...)` | Zapisuje pakiet przychodzacy do pliku. |
| `void addOutputPacket(...)` | Zapisuje pakiet wychodzacy do pliku. |
# # # Zmienne prywatne

-   `m_start`: Czas rozpoczecia nagrywania.
-   `m_stream`: Strumien pliku do zapisu.
-   `m_firstOutput`: Flaga uzywana do pominiecia pierwszego pakietu wychodzacego (zwykle zawierajacego haslo).
# # Zaleznosci i powiazania

-   `framework/net/inputmessage.h`, `outputmessage.h`: Przyjmuje obiekty tych typ�w do nagrania.
-   Jest tworzona i uzywana przez `Protocol`, gdy wlaczony jest tryb nagrywania.

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `otml` sluzy do wczesnych deklaracji (forward declarations) i definicji typ�w dla klas zwiazanych z parserem OTML.
# # Wczesne deklaracje

-   `OTMLNode`
-   `OTMLDocument`
-   `OTMLParser`
-   `OTMLEmitter`
# # Definicje typ�w

-   `OTMLNodePtr`: `stdext::shared_object_ptr<OTMLNode>`
-   `OTMLDocumentPtr`: `stdext::shared_object_ptr<OTMLDocument>`
-   `OTMLNodeList`: `std::vector<OTMLNodePtr>`
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest dolaczany przez wszystkie pliki nagl�wkowe w module `otml`.

---
# ?? otmlparser.h
# # Opis og�lny

Plik `otmlparser.h` deklaruje klase `OTMLParser`, kt�ra jest odpowiedzialna za parsowanie dokument�w w formacie OTML (OTClient Markup Language).
# # Klasa `OTMLParser`
# # # Opis semantyczny
`OTMLParser` odczytuje dane linia po linii ze strumienia wejsciowego, analizuje wciecia (kt�re definiuja hierarchie), a nastepnie parsuje tagi i wartosci, budujac drzewo obiekt�w `OTMLNode`.
# # # Metody publiczne

-   `OTMLParser(OTMLDocumentPtr doc, std::istream& in)`: Konstruktor.
-   `void parse()`: Gl�wna metoda rozpoczynajaca proces parsowania.
# # # Metody prywatne

-   `std::string getNextLine()`: Odczytuje nastepna linie ze strumienia.
-   `int getLineDepth(...)`: Oblicza poziom zagniezdzenia na podstawie liczby spacji na poczatku linii.
-   `void parseLine(...)`: Przetwarza pojedyncza linie (sprawdza wciecia, komentarze, puste linie).
-   `void parseNode(...)`: Parsuje tag i wartosc z linii i tworzy nowy `OTMLNode`.
# # # Zmienne prywatne

-   `currentDepth`, `currentLine`: Sledza pozycje w pliku.
-   `doc`: Wskaznik na dokument, kt�ry jest budowany.
-   `currentParent`: Wskaznik na biezacy wezel-rodzica.
-   `parentMap`: Mapa do sledzenia hierarchii.
-   `previousNode`: Wskaznik na ostatnio dodany wezel.
-   `in`: Referencja do strumienia wejsciowego.
# # Zaleznosci i powiazania

-   `framework/otml/declarations.h`: Definicje typ�w.
-   Jest uzywana przez `OTMLDocument::parse`.

---
# ?? otml.h
# # Opis og�lny

Plik `otml.h` jest gl�wnym plikiem nagl�wkowym dla modulu OTML. Jego jedynym zadaniem jest dolaczenie dw�ch najwazniejszych plik�w tego modulu: `otmldocument.h` i `otmlnode.h`.
# # Zawartosc

```cpp
# include "otmldocument.h"
# include "otmlnode.h"
```
# # Zaleznosci i powiazania

-   Ulatwia dolaczanie podstawowych funkcjonalnosci OTML w innych czesciach projektu, kt�re potrzebuja zar�wno `OTMLDocument`, jak i `OTMLNode`.

---
# ?? otmldocument.cpp
# # Opis og�lny

Plik `otmldocument.cpp` zawiera implementacje klasy `OTMLDocument`, kt�ra reprezentuje caly dokument OTML i jest korzeniem drzewa wezl�w.
# # Klasa `OTMLDocument`
# # # `OTMLDocumentPtr OTMLDocument::create()`

Statyczna metoda fabryczna. Tworzy nowy, pusty dokument z domyslnym tagiem "doc".
# # # `OTMLDocumentPtr OTMLDocument::parse(const std::string& fileName)`

Statyczna metoda, kt�ra laduje i parsuje dokument OTML z pliku. Uzywa `g_resources` do odczytania pliku do strumienia, a nastepnie wywoluje `parse(std::istream&, ...)`.
# # # `OTMLDocumentPtr OTMLDocument::parseString(const std::string& data, const std::string& source)`

Parsuje dokument z `std::string`.
# # # `OTMLDocumentPtr OTMLDocument::parse(std::istream& in, const std::::string& source)`

Gl�wna metoda parsujaca.
1.  Tworzy nowy `OTMLDocument`.
2.  Tworzy `OTMLParser` dla tego dokumentu i strumienia.
3.  Wywoluje `parser.parse()` w celu zbudowania drzewa wezl�w.
4.  Zwraca gotowy dokument.
# # # `std::string OTMLDocument::emit()`

Konwertuje cale drzewo wezl�w OTML z powrotem na format tekstowy, uzywajac `OTMLEmitter`.
# # # `bool OTMLDocument::save(const std::string& fileName)`

Zapisuje wyemitowany dokument do pliku za pomoca `g_resources`.
# # Zaleznosci i powiazania

-   `framework/otml/otmldocument.h`: Plik nagl�wkowy.
-   `framework/otml/otmlparser.h`, `otmlemitter.h`: Uzywa parsera i emittera.
-   `framework/core/resourcemanager.h`: Do operacji na plikach.

---
# ?? otmldocument.h
# # Opis og�lny

Plik `otmldocument.h` deklaruje klase `OTMLDocument`, kt�ra jest specjalizacja `OTMLNode` i reprezentuje korzen dokumentu OTML.
# # Klasa `OTMLDocument`
# # # Opis semantyczny
`OTMLDocument` dziedziczy po `OTMLNode`, wiec jest jednoczesnie wezlem (korzeniem) i calym dokumentem. Dodaje funkcjonalnosc zwiazana z plikami: parsowanie z pliku/stringu i zapisywanie do pliku. Przechowuje r�wniez informacje o zr�dle (`source`), z kt�rego zostal zaladowany.
# # # Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static OTMLDocumentPtr create()` | Tworzy pusty dokument. |
| `static OTMLDocumentPtr parse(...)` | Parsuje dokument z pliku, stringu lub strumienia. |
# # # Metody publiczne (instancji)

| Metoda | Opis |
| :--- | :--- |
| `std::string emit()` | Konwertuje dokument na string w formacie OTML. |
| `bool save(const std::string& fileName)` | Zapisuje dokument do pliku. |
# # Zaleznosci i powiazania

-   `framework/otml/otmlnode.h`: Klasa bazowa.
-   Jest uzywana jako punkt wejscia do tworzenia i ladowania struktur OTML w calej aplikacji (np. w `UIManager`, `ConfigManager`).

---
# ?? otmlemitter.cpp
# # Opis og�lny

Plik `otmlemitter.cpp` zawiera implementacje klasy `OTMLEmitter`, kt�ra jest odpowiedzialna za konwersje drzewa `OTMLNode` z powrotem do formatu tekstowego OTML.
# # Klasa `OTMLEmitter`
# # # `std::string OTMLEmitter::emitNode(const OTMLNodePtr& node, int currentDepth)`
# # # # Opis semantyczny
Rekurencyjna, statyczna metoda, kt�ra generuje tekstowa reprezentacje pojedynczego wezla i wszystkich jego dzieci.
# # # # Dzialanie
1.  Dodaje wciecie (2 spacje na poziom) odpowiednie dla `currentDepth`.
2.  Zapisuje tag wezla. Jesli wezel ma wartosc lub jest unikalny, dodaje `:`. Jesli nie ma tagu, zapisuje `-`.
3.  Zapisuje wartosc wezla:
    -   Jesli wartosc to `null` (`m_null`), zapisuje `~`.
    -   Jesli wartosc zawiera znaki nowej linii, formatuje ja jako blok wieloliniowy, uzywajac `|`, `|-` lub `|+` w zaleznosci od tego, jak maja byc traktowane koncowe znaki nowej linii.
    -   W przeciwnym razie, zapisuje wartosc w tej samej linii.
4.  Rekurencyjnie wywoluje `emitNode` dla wszystkich dzieci, zwiekszajac `currentDepth`.
# # Zaleznosci i powiazania

-   `framework/otml/otmlemitter.h`: Plik nagl�wkowy.
-   `framework/otml/otmldocument.h`: Uzywana przez `OTMLDocument::emit()`.

---
# ?? otmlexception.cpp
# # Opis og�lny

Plik `otmlexception.cpp` zawiera implementacje klasy `OTMLException`, kt�ra jest uzywana do sygnalizowania bled�w podczas parsowania lub przetwarzania dokument�w OTML.
# # Klasa `OTMLException`
# # # Konstruktory

-   **`OTMLException(const OTMLNodePtr& node, const std::string& error)`**: Tworzy wyjatek zwiazany z konkretnym wezlem. Komunikat bledu bedzie zawieral informacje o zr�dle (`source`) tego wezla.
-   **`OTMLException(const OTMLDocumentPtr& doc, const std::string& error, int line)`**: Tworzy wyjatek zwiazany z calym dokumentem, opcjonalnie podajac numer linii, w kt�rej wystapil blad parsowania.
# # # Dzialanie
Oba konstruktory buduja szczeg�lowy komunikat bledu w `std::stringstream`, kt�ry jest nastepnie zapisywany w `m_what` i dostepny przez metode `what()`.
# # Zaleznosci i powiazania

-   `framework/otml/otmlexception.h`: Plik nagl�wkowy.
-   `framework/otml/otmldocument.h`: Do dostepu do zr�dla dokumentu.
-   Jest rzucana przez `OTMLParser` w przypadku bled�w skladniowych i przez `OTMLNode` w przypadku bled�w logicznych (np. brak wymaganego dziecka).

---
# ?? otmlexception.h
# # Opis og�lny

Plik `otmlexception.h` deklaruje klase `OTMLException`, kt�ra jest typem wyjatku uzywanym do sygnalizowania bled�w zwiazanych z OTML.
# # Klasa `OTMLException`
# # # Opis semantyczny
Dziedziczy po `stdext::exception`. Jest tworzona z informacja o kontekscie bledu (wezel lub dokument oraz numer linii), co pozwala na generowanie precyzyjnych komunikat�w o bledach, ulatwiajacych debugowanie plik�w OTML.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OTMLException(...)` | Konstruktory. |
| `virtual ~OTMLException()` | Destruktor. |
| `virtual const char* what() const throw()` | Zwraca sformatowany komunikat bledu. |
# # # Zmienne chronione

-   `m_what`: `std::string` przechowujaca komunikat bledu.
# # Zaleznosci i powiazania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   `framework/stdext/exception.h`: Klasa bazowa.
-   Jest rzucana przez `OTMLParser` i `OTMLNode`.

---
# ?? otmlemitter.h
# # Opis og�lny

Plik `otmlemitter.h` deklaruje klase `OTMLEmitter`, kt�ra jest odpowiedzialna za proces "emitowania", czyli konwersji drzewa wezl�w OTML z powrotem do jego tekstowej reprezentacji.
# # Klasa `OTMLEmitter`
# # # Opis semantyczny
`OTMLEmitter` zawiera jedna statyczna metode, kt�ra rekurencyjnie przechodzi przez drzewo `OTMLNode` i buduje sformatowany `std::string` zgodny ze skladnia OTML, uwzgledniajac wciecia, tagi, wartosci (w tym wieloliniowe) i hierarchie.
# # # Metody publiczne (statyczne)

| Metoda | Opis |
| :--- | :--- |
| `static std::string emitNode(...)` | Generuje tekstowa reprezentacje podanego wezla i wszystkich jego dzieci. |
# # Zaleznosci i powiazania

-   `framework/otml/declarations.h`: Podstawowe deklaracje.
-   Jest uzywana przez `OTMLDocument::emit()` i `OTMLNode::emit()`.

---
# ?? otmlparser.cpp
# # Opis og�lny

Plik `otmlparser.cpp` zawiera implementacje klasy `OTMLParser`, kt�ra jest sercem mechanizmu parsowania jezyka OTML.
# # Klasa `OTMLParser`
# # # `OTMLParser::OTMLParser(...)`

Konstruktor. Inicjalizuje stan parsera, ustawiajac biezacy wezel-rodzica na korzen dokumentu.
# # # `void OTMLParser::parse()`

Gl�wna metoda, kt�ra w petli odczytuje kolejne linie ze strumienia (`getNextLine()`) i przekazuje je do `parseLine()`, az do konca pliku.
# # # `int OTMLParser::getLineDepth(...)`

Oblicza poziom wciecia linii, liczac spacje na jej poczatku. Wymusza, aby wciecie bylo wielokrotnoscia dw�ch spacji i zabrania uzywania tabulator�w.
# # # `void OTMLParser::parseLine(std::string line)`

Przetwarza pojedyncza linie.
1.  Oblicza jej glebokosc.
2.  Usuwa biale znaki z poczatku i konca.
3.  Ignoruje puste linie i komentarze (`//`).
4.  Na podstawie r�znicy miedzy biezaca glebokoscia a glebokoscia linii, aktualizuje `currentParent`, wchodzac w glab hierarchii lub wracajac na wyzszy poziom.
5.  Wywoluje `parseNode` w celu sparsowania wlasciwej zawartosci linii.
# # # `void OTMLParser::parseNode(const std::string& data)`

Parsuje tag i wartosc z podanego ciagu znak�w.
1.  Dzieli ciag na tag i wartosc na podstawie separatora `:`.
2.  Obsluguje specjalny przypadek `-` dla wezl�w bez tagu.
3.  Obsluguje wartosci wieloliniowe (rozpoczynajace sie od `|`, `|-`, `|+`), odczytujac kolejne linie, dop�ki wciecie sie zgadza.
4.  Obsluguje listy w nawiasach kwadratowych (`[...]`), dzielac je na osobne wartosci.
5.  Tworzy nowy obiekt `OTMLNode`, ustawia jego wlasciwosci (tag, wartosc, zr�dlo) i dodaje go do `currentParent`.
# # Zaleznosci i powiazania

-   `framework/otml/otmlparser.h`: Plik nagl�wkowy.
-   `framework/otml/otmldocument.h`, `otmlexception.h`: Do tworzenia i obslugi bled�w.
-   `boost/tokenizer.hpp`: Do parsowania list w nawiasach kwadratowych.

---
# ?? otmlnode.h
# # Opis og�lny

Plik `otmlnode.h` deklaruje klase `OTMLNode`, kt�ra jest podstawowym budulcem drzewa dokumentu OTML. Reprezentuje pojedynczy wezel, kt�ry moze miec tag, wartosc i liste dzieci.
# # Klasa `OTMLNode`
# # # Opis semantyczny
`OTMLNode` to uniwersalny kontener na dane w strukturze drzewiastej. Jest uzywany do reprezentowania zar�wno styl�w UI, jak i samych widget�w w plikach `.otui`, a takze modul�w w `.otmod` i konfiguracji w plikach `.otml`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `static OTMLNodePtr create(...)` | Metody fabryczne do tworzenia nowych wezl�w. |
| `tag()`, `size()`, `source()`, `rawValue()` | Gettery dla podstawowych wlasciwosci. |
| `isUnique()`, `isNull()`, `hasTag()`, `hasValue()`, `hasChildren()` | Metody sprawdzajace stan wezla. |
| `setTag(...)`, `setValue(...)`, ... | Settery dla wlasciwosci. |
| `get(const std::string& childTag)` | Zwraca pierwszy wezel-dziecko o danym tagu. |
| `at(const std::string& childTag)` | To samo co `get`, ale rzuca wyjatek, jesli dziecko nie istnieje. |
| `addChild(...)`, `removeChild(...)` | Dodaje/usuwa dziecko. `addChild` obsluguje logike laczenia (merge) dla unikalnych wezl�w. |
| `copy(...)`, `merge(...)`, `clear()`, `clone()` | Metody do manipulacji struktura wezla. |
| `children()` | Zwraca liste wszystkich dzieci. |
| **Szablonowe metody `value...`** | |
| `value<T>()` | Zwraca wartosc wezla, rzutowana na typ `T`. |
| `valueAt<T>(...)` | Zwraca wartosc dziecka o danym tagu. |
| `valueAtIndex<T>(...)` | Zwraca wartosc dziecka o danym indeksie. |
| **Szablonowe metody `write...`** | |
| `write<T>(...)` | Ustawia wartosc wezla. |
| `writeAt<T>(...)` | Tworzy i dodaje unikalne dziecko z dana wartoscia. |
| `writeIn<T>(...)` | Tworzy i dodaje nie-unikalne dziecko z dana wartoscia. |
| `emit()` | Konwertuje wezel i jego dzieci na string. |
# # # Zmienne chronione

-   `m_children`: Mapa przechowujaca dzieci pogrupowane wedlug tag�w.
-   `m_tag`, `m_value`, `m_source`: Podstawowe wlasciwosci.
-   `m_unique`, `m_null`: Flagi stanu.
# # Zaleznosci i powiazania

-   `framework/otml/declarations.h`: Definicje typ�w.
-   `framework/otml/otmlexception.h`: Do rzucania wyjatk�w.
-   Jest to podstawowa klasa modulu OTML, uzywana przez `OTMLParser`, `OTMLEmitter` i `OTMLDocument`.

---
# ?? otmlnode.cpp
# # Opis og�lny

Plik `otmlnode.cpp` zawiera implementacje metod klasy `OTMLNode`.
# # Klasa `OTMLNode`
# # # `OTMLNodePtr OTMLNode::create(...)`

Metody fabryczne, kt�re tworza nowy `OTMLNode` i ustawiaja jego poczatkowe wlasciwosci.
# # # `bool OTMLNode::hasChildren()`

Sprawdza, czy wezel ma jakiekolwiek dzieci, kt�re nie sa `null`.
# # # `OTMLNodePtr OTMLNode::get(const std::string& childTag)`

Wyszukuje w mapie `m_children` pierwsze dziecko o podanym tagu, kt�re nie jest `null`, i je zwraca.
# # # `void OTMLNode::addChild(const OTMLNodePtr& newChild)`

Dodaje nowe dziecko. Implementuje kluczowa logike:
-   Jesli nowe dziecko ma tag i jest unikalne (`isUnique()`), a dziecko o takim samym tagu juz istnieje, to nowe dziecko jest laczone (`merge`) ze starym, effectively nadpisujac/dodajac wlasciwosci.
-   W przeciwnym razie, jest po prostu dodawane do listy dzieci o danym tagu.
-   Kazdemu dziecku nadawany jest unikalny, rosnacy indeks, aby zachowac kolejnosc wstawiania.
# # # `bool OTMLNode::removeChild(...)`

Usuwa podane dziecko z listy.
# # # `void OTMLNode::copy(const OTMLNodePtr& node)`

Gleboko kopiuje wszystkie wlasciwosci i dzieci z innego wezla, zastepujac wlasna zawartosc.
# # # `void OTMLNode::merge(const OTMLNodePtr& node)`

Laczy zawartosc innego wezla z biezacym. W przeciwienstwie do `copy`, nie czysci istniejacych dzieci, lecz dodaje nowe (lub laczy, jesli sa unikalne).
# # # `OTMLNodeList OTMLNode::children()`

Zwraca liste wszystkich nie-nullowych dzieci, posortowana wedlug ich indeksu wstawienia.
# # # `OTMLNodePtr OTMLNode::clone()`

Tworzy i zwraca gleboka kopie wezla i wszystkich jego dzieci.
# # Zaleznosci i powiazania

-   `framework/otml/otmlnode.h`: Plik nagl�wkowy.
-   `framework/otml/otmlemitter.h`: Uzywany w metodzie `emit()`.
-   Jest to implementacja centralnej struktury danych dla systemu OTML.

---
# ?? androidplatform.cpp
# # Opis og�lny

Plik `androidplatform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla systemu Android. Jest kompilowany tylko wtedy, gdy zdefiniowano makro `ANDROID`.
# # Klasa `Platform` (implementacja dla Androida)

Wiele metod jest pustymi implementacjami lub zwraca domyslne wartosci, poniewaz ich funkcjonalnosc nie jest dostepna lub nie ma sensu na platformie Android w taki sam spos�b, jak na desktopie.

| Metoda | Implementacja na Androidzie |
| :--- | :--- |
| `processArgs(...)` | Pusta (argumenty sa obslugiwane inaczej). |
| `spawnProcess(...)`| Zwraca `false`. |
| `getProcessId()` | Zwraca `getpid()`. |
| `isProcessRunning(...)` | Zwraca `false`. |
| `killProcess(...)` | Zwraca `false`. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | Zwraca wynik `getcwd()`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Puste/zwracaja `true`/`false`. Operacje na plikach sa obslugiwane przez `ResourceManager`. |
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
# # Zaleznosci i powiazania

-   `framework/platform/platform.h`: Plik nagl�wkowy.
-   `framework/platform/androidwindow.h`: Do otwierania URL.
-   `framework/core/eventdispatcher.h`: Do bezpiecznego watkowo wywolywania metod z `AndroidWindow`.

---
# ?? androidwindow.cpp
# # Opis og�lny

Plik `androidwindow.cpp` zawiera implementacje klasy `AndroidWindow`, kt�ra jest specyficzna dla platformy Android implementacja `PlatformWindow`. Zarzadza ona cyklem zycia okna, obsluga wejscia (dotyk, klawiatura) oraz kontekstem graficznym EGL/OpenGL ES.
# # Zmienne globalne
# # # `g_androidWindow`

Globalna instancja `AndroidWindow`.
# # Klasa `AndroidWindow`
# # # `AndroidWindow::AndroidWindow()`

Konstruktor. Inicjalizuje mape klawiszy (`m_keyMap`), tlumaczac kody klawiszy Android (`AKEYCODE_*`) na wewnetrzne kody `Fw::Key`.
# # # `void AndroidWindow::internalInitGL()` i `internalDestroyGL()`

Metody do zarzadzania kontekstem graficznym EGL.
-   `internalInitGL`: Pobiera domyslny wyswietlacz EGL, wybiera konfiguracje, tworzy powierzchnie renderowania (`EGLSurface`) na podstawie natywnego okna Android i tworzy kontekst OpenGL ES 2.0.
-   `internalDestroyGL`: Zwalnia powierzchnie i kontekst EGL.
# # # `void AndroidWindow::init(struct android_app* app)`

Gl�wna metoda inicjalizujaca. Zapisuje wskaznik na `android_app` i ustawia `callbacki` dla zdarzen cyklu zycia aplikacji i zdarzen wejsciowych.
# # # `void AndroidWindow::poll()`

Przetwarza zdarzenia systemowe z kolejki Androida za pomoca `ALooper_pollAll`.
# # # `void AndroidWindow::swapBuffers()`

Zamienia bufory ekranu za pomoca `eglSwapBuffers`.
# # # `void AndroidWindow::handleCmd(int32_t cmd)`

Handler dla zdarzen cyklu zycia aplikacji Android (np. `APP_CMD_INIT_WINDOW`, `APP_CMD_GAINED_FOCUS`). W odpowiedzi na te zdarzenia, tworzy lub niszczy kontekst GL i aktualizuje stan widocznosci.
# # # `int AndroidWindow::handleInput(AInputEvent* event)`

Handler dla zdarzen wejsciowych.
-   **`AINPUT_EVENT_TYPE_MOTION` (dotyk)**:
    -   Tlumaczy zdarzenia dotyku (`ACTION_DOWN`, `ACTION_UP`, `ACTION_MOVE`) na zdarzenia myszy (`MousePress`, `MouseRelease`, `MouseMove`).
    -   Implementuje logike do symulacji klikniecia lewym i prawym przyciskiem myszy oraz przeciagania na ekranie dotykowym.
    -   Obsluguje wielodotyk, mapujac drugi i trzeci palec na `Fw::MouseTouch2` i `Fw::MouseTouch3`.
-   **`AINPUT_EVENT_TYPE_KEY` (klawiatura)**:
    -   Tlumaczy kod klawisza Android na kod `Fw::Key`.
    -   Wywoluje `processKeyDown` lub `processKeyUp`.
# # # `void AndroidWindow::showTextEditor(...)`

Wywoluje metode Javy (`showTextEdit`) za pomoca JNI, aby wyswietlic natywna klawiature i pole edycji tekstu Androida.
# # # `void AndroidWindow::openUrl(std::string url)`

Otwiera URL za pomoca intencji Androida, wywolujac metode Javy przez JNI.
# # # Funkcja `JNIEXPORT ... commitText(...)`

Funkcja C wywolywana z kodu Javy, kt�ra przekazuje tekst wpisany na klawiaturze Androida z powrotem do aplikacji.
# # Zaleznosci i powiazania

-   Nagl�wki NDK Androida (`android_native_app_glue.h`, `jni.h`).
-   Nagl�wki EGL i GLES.
-   Wsp�lpracuje z `GraphicalApplication` poprzez `callbacki` `m_onInputEvent`, `m_onResize`, `m_onClose`.

---
# ?? androidwindow.h
# # Opis og�lny

Plik `androidwindow.h` deklaruje klase `AndroidWindow`, kt�ra jest implementacja `PlatformWindow` dla systemu Android.
# # Klasa `AndroidWindow`
# # # Opis semantyczny
`AndroidWindow` integruje aplikacje z natywnym cyklem zycia i systemem zdarzen Androida za pomoca struktury `android_app` z NDK. Zarzadza kontekstem graficznym EGL/GLES i tlumaczy natywne zdarzenia wejsciowe (dotyk, klawisze sprzetowe) na wewnetrzny format `InputEvent`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| **Zarzadzanie cyklem zycia** | |
| `init(struct android_app* app)` | Inicjalizuje okno, laczac je ze struktura `android_app`. |
| `handleCmd(int32_t cmd)` | Obsluguje komendy cyklu zycia aplikacji od systemu Android. |
| `handleInput(AInputEvent* event)` | Przetwarza natywne zdarzenia wejsciowe. |
| **Interfejs `PlatformWindow`** | |
| `poll()` | Przetwarza zdarzenia z kolejki systemowej. |
| `swapBuffers()` | Zamienia bufory EGL. |
| `getDisplaySize()` | Zwraca rozmiar okna. |
| `showTextEditor(...)` | Wyswietla natywna klawiature Androida. |
| `openUrl(...)` | Otwiera URL. |
| ... | Implementacje innych metod `PlatformWindow`, czesto puste, poniewaz pojecia takie jak "minimalizacja" czy "zmiana tytulu okna" nie maja bezposredniego odpowiednika na Androidzie. |
# # # Zmienne prywatne

-   `m_egl...`: Uchwyty do zasob�w EGL (Display, Context, Surface, Config).
-   `m_multiInputEvent[3]`: Bufory na zdarzenia wielodotykowe.
# # # Zmienne globalne

-   `g_androidWindow`: Globalna instancja `AndroidWindow`.
# # Zaleznosci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Wymaga `android_native_app_glue.h` i nagl�wk�w JNI/EGL/GLES, kt�re sa czescia Android NDK.
-   W `platformwindow.cpp` wskaznik `g_window` jest przypisywany do `g_androidWindow`, gdy kompilacja odbywa sie dla Androida.

---
# ?? crashhandler.h
# # Opis og�lny

Plik `crashhandler.h` deklaruje funkcje do instalacji i deinstalacji globalnego mechanizmu obslugi awarii (crash handler).
# # Funkcje
# # # `void installCrashHandler()`

Rejestruje handlery dla sygnal�w lub wyjatk�w systemowych (w zaleznosci od platformy), kt�re sa wywolywane w przypadku krytycznego bledu aplikacji (np. naruszenie ochrony pamieci).
# # # `void uninstallCrashHandler()`

Odinstalowuje wczesniej zarejestrowane handlery.
# # Dyrektywa preprocesora

Cala zawartosc pliku jest objeta dyrektywa `#ifdef CRASH_HANDLER`, co oznacza, ze funkcje te sa dostepne tylko wtedy, gdy opcja `CRASH_HANDLER` jest wlaczona w CMake.
# # Zaleznosci i powiazania

-   Funkcje te sa implementowane w plikach specyficznych dla platformy: `unixcrashhandler.cpp` i `win32crashhandler.cpp`.
-   `installCrashHandler` jest zazwyczaj wywolywana na samym poczatku dzialania aplikacji.

---
# ?? platform.cpp
# # Opis og�lny

Plik `platform.cpp` ma za zadanie jedynie zdefiniowac globalna instancje klasy `Platform`.
# # Zmienne globalne
# # # `g_platform`

Globalna, jedyna instancja klasy `Platform`, kt�ra dostarcza interfejs do funkcji specyficznych dla systemu operacyjnego.

```cpp
Platform g_platform;
```
# # Zaleznosci i powiazania

-   `framework/platform/platform.h`: Plik nagl�wkowy, kt�ry deklaruje klase `Platform`.
-   Wlasciwa implementacja metod tej klasy znajduje sie w plikach `win32platform.cpp`, `unixplatform.cpp` i `androidplatform.cpp`, z kt�rych tylko jeden jest kompilowany w zaleznosci od docelowej platformy.

---
# ?? platformwindow.cpp
# # Opis og�lny

Plik `platformwindow.cpp` jest kluczowym plikiem, kt�ry zarzadza implementacja okna specyficzna dla danej platformy. Jego gl�wnym zadaniem jest dolaczenie odpowiedniego pliku nagl�wkowego (np. `win32window.h` lub `x11window.h`) i zdefiniowanie globalnego wskaznika `g_window`, kt�ry bedzie wskazywal na wlasciwa, platformowa instancje okna.
# # Zmienne globalne
# # # `g_window`

Globalna referencja do obiektu okna. Jest to centralny punkt dostepu do wszystkich operacji zwiazanych z oknem w calym frameworku. W zaleznosci od platformy, wskazuje na instancje `WIN32Window`, `X11Window`, `AndroidWindow` lub `SDLWindow`.

```cpp
# ifdef ANDROID
PlatformWindow& g_window = g_androidWindow;
# else
PlatformWindow& g_window = window; // gdzie 'window' to globalna instancja np. WIN32Window
# endif
```
# # Klasa `PlatformWindow`
# # # `int PlatformWindow::loadMouseCursor(...)`

Laduje obraz kursora, sprawdza jego poprawnosc (rozmiar 32x32, 4 kanaly kolor�w) i deleguje wlasciwe tworzenie kursora do metody wirtualnej `internalLoadMouseCursor`, kt�ra jest zaimplementowana w klasach pochodnych.
# # # `void PlatformWindow::updateUnmaximizedCoords()`

Zapisuje aktualna pozycje i rozmiar okna, ale tylko wtedy, gdy okno nie jest zmaksymalizowane ani w trybie pelnoekranowym. Sluzy do przywracania poprzedniego stanu okna.
# # # `void PlatformWindow::processKeyDown(Fw::Key keyCode)`

Obsluguje zdarzenie wcisniecia klawisza.
-   Aktualizuje stan modyfikator�w (Ctrl, Alt, Shift).
-   Sprawdza, czy klawisz nie jest juz wcisniety (obsluga auto-powtarzania).
-   Ustawia stan klawisza na wcisniety (`m_keysState`).
-   Wysyla zdarzenia `KeyDownInputEvent` i `KeyPressInputEvent` do zarejestrowanego `callbacka`.
# # # `void PlatformWindow::processKeyUp(Fw::Key keyCode)`

Obsluguje zdarzenie zwolnienia klawisza.
-   Aktualizuje stan modyfikator�w.
-   Ustawia stan klawisza na zwolniony.
-   Wysyla zdarzenie `KeyUpInputEvent`.
# # # `void PlatformWindow::releaseAllKeys()`

Resetuje stan wszystkich wcisnietych klawiszy i przycisk�w myszy. Wywolywana np. gdy okno traci fokus.
# # # `void PlatformWindow::fireKeysPress()`

Metoda wywolywana cyklicznie. Sprawdza, kt�re klawisze sa wcisniete i od odpowiednio dlugiego czasu, a nastepnie generuje zdarzenia `KeyPressInputEvent` (auto-powtarzanie).
# # Zaleznosci i powiazania

-   Wlacza jeden z plik�w nagl�wkowych specyficznych dla platformy (`win32window.h`, `x11window.h`, etc.).
-   `framework/core/eventdispatcher.h`: Uzywa `g_dispatcher` do bezpiecznego watkowo przetwarzania zdarzen.
-   `framework/graphics/image.h`: Do ladowania obraz�w kursor�w.
-   Jest to implementacja czesci wsp�lnej dla wszystkich platform, podczas gdy specyfika jest w klasach pochodnych.

---
# ?? platform.h
# # Opis og�lny

Plik `platform.h` deklaruje klase `Platform`, kt�ra jest interfejsem do funkcji specyficznych dla systemu operacyjnego. Zapewnia abstrakcje nad r�znicami miedzy platformami (Windows, Linux, macOS, Android).
# # Klasa `Platform`
# # # Opis semantyczny
`Platform` dostarcza zestaw statycznych metod do interakcji z systemem operacyjnym. Implementacja tych metod znajduje sie w plikach specyficznych dla platformy (np. `win32platform.cpp`, `unixplatform.cpp`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `void processArgs(...)` | Przetwarza argumenty wiersza polecen, konwertujac je do UTF-8. |
| `bool spawnProcess(...)` | Uruchamia nowy proces. |
| `int getProcessId()` | Zwraca ID biezacego procesu. |
| `bool isProcessRunning(...)` | Sprawdza, czy proces o danej nazwie jest uruchomiony. |
| `bool killProcess(...)` | Zamyka proces o danej nazwie. |
| `std::string getTempPath()` | Zwraca sciezke do katalogu tymczasowego. |
| `std::string getCurrentDir()` | Zwraca biezacy katalog roboczy. |
| `bool copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Podstawowe operacje na plikach. |
| `ticks_t getFileModificationTime(...)` | Zwraca czas ostatniej modyfikacji pliku. |
| `bool openUrl(...)` | Otwiera URL w domyslnej przegladarce. |
| `bool openDir(...)` | Otwiera katalog w menedzerze plik�w. |
| `std::string getCPUName()` | Zwraca nazwe procesora. |
| `double getTotalSystemMemory()`| Zwraca calkowita ilosc pamieci RAM. |
| `double getMemoryUsage()` | Zwraca uzycie pamieci przez biezacy proces. |
| `std::string getOSName()` | Zwraca nazwe systemu operacyjnego. |
| `std::string traceback(...)` | Generuje slad stosu wywolan C++. |
| `std::vector<std::string> getMacAddresses()` | Zwraca liste adres�w MAC. |
| `std::string getUserName()` | Zwraca nazwe zalogowanego uzytkownika. |
| `std::vector<std::string> getDlls()` | (Windows) Zwraca liste zaladowanych bibliotek DLL. |
| `std::vector<std::string> getProcesses()` | Zwraca liste uruchomionych proces�w. |
| `std::vector<std::string> getWindows()` | (Windows) Zwraca liste tytul�w otwartych okien. |
# # # Zmienne globalne

-   `g_platform`: Globalna instancja `Platform`.
# # Zaleznosci i powiazania

-   Uzywana w calym projekcie do operacji, kt�re wymagaja interakcji z systemem operacyjnym.
-   Jej implementacja jest dostarczana przez pliki `*.cpp` specyficzne dla platformy.

---
# ?? platformwindow.h
# # Opis og�lny

Plik `platformwindow.h` deklaruje abstrakcyjna klase bazowa `PlatformWindow`, kt�ra definiuje wsp�lny interfejs do zarzadzania oknem aplikacji na r�znych systemach operacyjnych.
# # Klasa `PlatformWindow`
# # # Opis semantyczny
`PlatformWindow` jest klasa abstrakcyjna, kt�ra ukrywa szczeg�ly implementacyjne zwiazane z tworzeniem okna, obsluga zdarzen i zarzadzaniem kontekstem graficznym. Kazda platforma (Windows, Linux, Android) dostarcza wlasna, konkretna implementacje tej klasy.
# # # Metody czysto wirtualne (do implementacji przez klasy pochodne)

-   `init()`, `terminate()`: Cykl zycia okna.
-   `move()`, `resize()`, `show()`, `hide()`, `minimize()`, `maximize()`: Zarzadzanie stanem okna.
-   `poll()`: Przetwarzanie zdarzen systemowych.
-   `swapBuffers()`: Zamiana bufor�w graficznych.
-   `set...()`: Metody do ustawiania wlasciwosci okna (tytul, ikona, VSync, etc.).
-   `get...()`: Metody do pobierania informacji (rozmiar ekranu, tekst ze schowka).
# # # Metody z implementacja

-   `loadMouseCursor(...)`: Laduje kursor z pliku.
-   `processKeyDown()`, `processKeyUp()`, `releaseAllKeys()`, `fireKeysPress()`: Implementuja logike obslugi stanu klawiatury, kt�ra jest wsp�lna dla wszystkich platform.
-   Gettery dla stanu okna (`getSize`, `getPosition`, `isVisible`, `isKeyPressed`, etc.).
# # # Zmienne chronione

-   `m_keyMap`: Mapa tlumaczaca kody klawiszy specyficzne dla platformy na wewnetrzne kody `Fw::Key`.
-   `m_keysState`, `m_lastKeysPress`: Mapy do sledzenia stanu klawiszy.
-   `m_size`, `m_position`, `m_minimumSize`: Wlasciwosci geometryczne okna.
-   `m_inputEvent`: Obiekt do przechowywania danych o biezacym zdarzeniu wejsciowym.
-   `m_visible`, `m_focused`, `m_fullscreen`, `m_maximized`: Flagi stanu okna.
-   `m_onClose`, `m_onResize`, `m_onInputEvent`: Callbacki do powiadamiania `GraphicalApplication` o zdarzeniach.
# # # Zmienne globalne

-   `g_window`: Globalna referencja do aktywnej instancji `PlatformWindow`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   `framework/core/inputevent.h`: Struktura `InputEvent`.
-   `framework/graphics/declarations.h`: Deklaracje typ�w graficznych.
-   Jest klasa bazowa dla `WIN32Window`, `X11Window`, `AndroidWindow`, `SDLWindow`.
-   Jest uzywana przez `GraphicalApplication` do wszystkich operacji na oknie.

---
# ?? sdlwindow.cpp
# # Opis og�lny

Plik `sdlwindow.cpp` zawiera implementacje klasy `SDLWindow`, kt�ra jest wersja `PlatformWindow` dla platformy Emscripten (WebAssembly), oparta na bibliotece SDL.

> **NOTE:** Implementacja jest w wiekszosci pusta. Sugeruje to, ze obsluga okna i zdarzen w Emscripten jest realizowana w inny spos�b, prawdopodobnie poprzez gl�wna petle Emscripten i bezposrednie wywolania JavaScript, a ta klasa jest jedynie "zaslepka" (placeholderem), aby kod sie kompilowal.
# # Klasa `SDLWindow`

Wszystkie metody implementujace interfejs `PlatformWindow` sa puste. Oznacza to, ze operacje takie jak `resize`, `move`, `setTitle`, `poll` czy `swapBuffers` nie maja tutaj zadnego efektu i musza byc obslugiwane przez zewnetrzny kod (prawdopodobnie w gl�wnej petli `emscripten_set_main_loop`).
# # # `SDLWindow::SDLWindow()`

Konstruktor. Inicjalizuje domyslne rozmiary i stan.
# # # `std::string SDLWindow::getPlatformType()`

Zwraca `"WASM"`.
# # Zaleznosci i powiazania

-   `framework/platform/sdlwindow.h`: Plik nagl�wkowy.
-   W `platformwindow.cpp` (niezalaczony, ale mozna sie domyslac), `g_window` jest ustawiane na instancje `SDLWindow` gdy kompilacja odbywa sie dla Emscripten.

---
# ?? sdlwindow.h
# # Opis og�lny

Plik `sdlwindow.h` deklaruje klase `SDLWindow`, kt�ra jest implementacja `PlatformWindow` dla platformy Emscripten (WebAssembly), oparta na bibliotece SDL.
# # Klasa `SDLWindow`
# # # Opis semantyczny
`SDLWindow` jest klasa-zaslepka, kt�ra spelnia kontrakt interfejsu `PlatformWindow`, ale wiekszosc jej metod jest pusta. Logika okna dla Emscripten jest zazwyczaj obslugiwana przez gl�wna petle zdefiniowana w `emscripten.h` i interakcje z API przegladarki, a nie przez tradycyjny model okienkowy.
# # # Metody publiczne
Deklaruje wszystkie metody wirtualne z `PlatformWindow` z pustymi implementacjami.
# # # Zmienne prywatne
-   `m_egl...`: Pola zwiazane z EGL, odziedziczone po logice Androida, ale prawdopodobnie nieuzywane w kontekscie Emscripten/SDL.
# # Zaleznosci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Jest to implementacja `PlatformWindow` uzywana, gdy zdefiniowano `__EMSCRIPTEN__`.

---
# ?? unixcrashhandler.cpp
# # Opis og�lny

Plik `unixcrashhandler.cpp` zawiera implementacje mechanizmu obslugi awarii (crash handler) dla system�w uniksowych (Linux, macOS). Jest kompilowany tylko wtedy, gdy zdefiniowano `CRASH_HANDLER` i platforma nie jest Windows ani Emscripten.
# # Funkcje
# # # `void crashHandler(int signum, siginfo_t* info, void* secret)`
# # # # Opis semantyczny
Jest to funkcja obslugi sygnalu, kt�ra jest wywolywana przez system operacyjny w momencie wystapienia krytycznego bledu (np. blad segmentacji). Jej zadaniem jest zebranie jak najwiekszej ilosci informacji o stanie programu w momencie awarii i zapisanie ich do logu.
# # # # Dzialanie
1.  Loguje komunikat "Application crashed".
2.  Tworzy strumien `stringstream` do budowy raportu.
3.  Zapisuje podstawowe informacje o aplikacji (nazwa, wersja, data kompilacji itp.).
4.  Pobiera kontekst procesora (`ucontext_t`) i zapisuje wartosci rejestr�w (np. `rip`, `rax` dla x64; `eip`, `eax` dla x86).
5.  Generuje slad stosu wywolan (backtrace) za pomoca `backtrace()` i `backtrace_symbols()`.
6.  Opcjonalnie (jesli zdefiniowano `DEMANGLE_BACKTRACE_SYMBOLS`), pr�buje zdemanglowac nazwy funkcji C++ w sladzie stosu.
7.  Zapisuje caly raport do pliku `crash_report.log` i do gl�wnego logu aplikacji.
8.  Przywraca domyslna obsluge sygnal�w, aby umozliwic systemowi operacyjnemu dokonczenie procesu zamykania aplikacji.
# # # `void installCrashHandler()`

Rejestruje funkcje `crashHandler` jako handler dla sygnal�w:
-   `SIGILL`: Nielegalna instrukcja.
-   `SIGSEGV`: Naruszenie ochrony pamieci.
-   `SIGFPE`: Blad operacji zmiennoprzecinkowej.
-   `SIGABRT`: Sygnal przerwania (np. z `assert`).
# # # `void uninstallCrashHandler()`

Pusta funkcja, deinstalacja nie jest zaimplementowana.
# # Zaleznosci i powiazania

-   `framework/platform/crashhandler.h`: Plik nagl�wkowy.
-   `framework/global.h`, `framework/core/application.h`: Do pobierania informacji o aplikacji.
-   Nagl�wki systemowe: `execinfo.h`, `ucontext.h`, `signal.h`.

---
# ?? unixplatform.cpp
# # Opis og�lny

Plik `unixplatform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla system�w uniksowych (Linux, macOS). Jest kompilowany, gdy platforma nie jest ani Windows, ani Emscripten.
# # Klasa `Platform` (implementacja dla Uniksa)

| Metoda | Implementacja na Uniksie |
| :--- | :--- |
| `spawnProcess(...)` | Uzywa `fork()` i `execv()` do uruchomienia nowego procesu. |
| `getProcessId()` | Uzywa `getpid()`. |
| `isProcessRunning(...)`, `killProcess(...)` | Puste implementacje. |
| `getTempPath()` | Zwraca `/tmp/`. |
| `getCurrentDir()` | Uzywa `getcwd()`. |
| `copyFile(...)` | Wywoluje systemowa komende `cp`. |
| `fileExists(...)` | Uzywa `stat()`. |
| `removeFile(...)` | Uzywa `unlink()`. |
| `getFileModificationTime(...)`| Uzywa `stat()` do odczytania `st_mtime`. |
| `openUrl(...)`, `openDir(...)` | Wywoluje systemowa komende `xdg-open`. Moze to zrobic natychmiast lub w `EventDispatcher`. |
| `getCPUName()` | Parsuje plik `/proc/cpuinfo`. |
| `getTotalSystemMemory()` | Parsuje plik `/proc/meminfo`. |
| `getMemoryUsage()` | Pusta implementacja. |
| `getOSName()` | Parsuje plik `/etc/issue`. |
| `traceback(...)` | Uzywa `backtrace()` i `backtrace_symbols()` do generowania sladu stosu, z opcjonalnym demanglowaniem nazw funkcji. |
| `getMacAddresses()` | Pusta implementacja. |
| `getUserName()` | Uzywa `getlogin_r()`. |
| `getDlls()`, `getProcesses()`, `getWindows()` | Puste implementacje (brak bezposrednich odpowiednik�w). |
# # Zaleznosci i powiazania

-   `framework/platform/platform.h`: Plik nagl�wkowy.
-   Nagl�wki systemowe POSIX (`unistd.h`, `sys/stat.h`, `execinfo.h`).
-   `framework/core/eventdispatcher.h`: Do asynchronicznego otwierania URL/katalog�w.

---
# ?? win32crashhandler.cpp
# # Opis og�lny

Plik `win32crashhandler.cpp` zawiera implementacje mechanizmu obslugi awarii (crash handler) dla systemu Windows. Jest kompilowany, gdy zdefiniowano `WIN32` i `CRASH_HANDLER`.
# # Funkcje
# # # `const char *getExceptionName(DWORD exceptionCode)`

Funkcja pomocnicza, kt�ra tlumaczy kod wyjatku Windows (np. `EXCEPTION_ACCESS_VIOLATION`) ?? czytelna nazwe.
# # # `void Stacktrace(LPEXCEPTION_POINTERS e, std::stringstream& ss)`

Generuje slad stosu wywolan. Uzywa funkcji z biblioteki `DbgHelp.dll` (`StackWalk`, `SymGetModuleBase`, `SymGetSymFromAddr`), aby przejsc przez stos i odczytac nazwy funkcji i modul�w.
# # # `LONG CALLBACK ExceptionHandler(PEXCEPTION_POINTERS e)`

Starsza wersja handlera. Generuje raport tekstowy podobny do wersji uniksowej, zapisuje go do pliku i wyswietla `MessageBox` z informacja o awarii.
# # # `LONG WINAPI UnhandledExceptionFilter2(PEXCEPTION_POINTERS exception)`

Nowsza, gl�wna funkcja obslugi wyjatk�w.
-   **Dzialanie**:
    1.  Tworzy i zapisuje **minidump** awarii do plik�w (`exception.dmp`, `exception_full.dmp`). Minidump to plik, kt�ry mozna otworzyc w debuggerze (np. Visual Studio, WinDbg) w celu posmiertnej analizy stanu programu.
    2.  Jesli `quiet_crash` jest `true` (ustawiane przez `uninstallCrashHandler`), cicho zamyka aplikacje.
    3.  W przeciwnym razie, wywoluje `ExceptionHandler` w celu wygenerowania raportu tekstowego i wyswietlenia komunikatu.
# # # `void installCrashHandler()`

Rejestruje `UnhandledExceptionFilter2` jako globalny handler nieobsluzonych wyjatk�w za pomoca `SetUnhandledExceptionFilter`.
# # # `void uninstallCrashHandler()`

Ustawia flage `quiet_crash` na `true`. Jest to uzywane np. podczas aktualizacji, aby cicho zamknac stara wersje klienta bez wyswietlania okna bledu.
# # Zaleznosci i powiazania

-   `framework/platform/crashhandler.h`: Plik nagl�wkowy.
-   `framework/global.h`, `core/application.h`, `core/resourcemanager.h`.
-   Nagl�wki Windows (`windows.h`, `imagehlp.h`, `DbgHelp.h`).

---
# ?? win32platform.cpp
# # Opis og�lny

Plik `win32platform.cpp` zawiera implementacje metod klasy `Platform` specyficznych dla systemu Windows.
# # Klasa `Platform` (implementacja dla Windows)

| Metoda | Implementacja na Windows |
| :--- | :--- |
| `processArgs(...)` | Uzywa `CommandLineToArgvW` do poprawnego sparsowania argument�w wiersza polecen (z obsluga Unicode). |
| `spawnProcess(...)`| Uzywa `ShellExecuteW`. |
| `getProcessId()` | Uzywa `GetCurrentProcessId()`. |
| `isProcessRunning(...)` | Uzywa `FindWindowA`. |
| `killProcess(...)` | Uzywa `FindWindowA`, `GetProcessId` i `TerminateProcess`. |
| `getTempPath()` | Uzywa `GetTempPathW`. |
| `getCurrentDir()` | Uzywa `GetCurrentDirectoryW`. |
| `copyFile(...)`, `fileExists(...)`, `removeFile(...)` | Uzywaja odpowiednik�w z WinAPI (`CopyFileW`, `GetFileAttributesW`, `DeleteFileW`). |
| `getFileModificationTime(...)`| Uzywa `GetFileAttributesExW`. |
| `openUrl(...)`, `openDir(...)` | Uzywaja `ShellExecuteW`. |
| `getCPUName()` | Odczytuje wartosc z rejestru systemowego. |
| `getTotalSystemMemory()`| Uzywa `GlobalMemoryStatusEx`. |
| `getMemoryUsage()` | Uzywa `GetProcessMemoryInfo`. |
| `getOSName()` | Uzywa `VerifyVersionInfo` i `GetProductInfo` do uzyskania szczeg�lowej nazwy wersji Windows. |
| `traceback(...)` | Prosta implementacja, zwraca tylko informacje o miejscu wywolania. |
| `getMacAddresses()` | Uzywa `GetAdaptersInfo`. |
| `getUserName()` | Uzywa `GetUserNameA`. |
| `getDlls()` | Uzywa `EnumProcessModules`. |
| `getProcesses()` | Uzywa `CreateToolhelp32Snapshot` do iteracji po procesach. |
| `getWindows()` | Uzywa `EnumWindows` do iteracji po otwartych oknach. |
# # Zaleznosci i powiazania

-   `framework/platform/platform.h`: Plik nagl�wkowy.
-   Nagl�wki WinAPI.
-   `boost/algorithm/string.hpp`: Do operacji na stringach.

---
# ?? win32window.cpp
# # Opis og�lny

Plik `win32window.cpp` zawiera implementacje klasy `WIN32Window`, kt�ra jest specyficzna dla Windows implementacja `PlatformWindow`. Zarzadza ona natywnym oknem WinAPI, obsluga zdarzen i kontekstem graficznym (WGL dla OpenGL lub EGL dla OpenGL ES/DirectX).
# # Klasa `WIN32Window`
# # # `WIN32Window::WIN32Window()`

Konstruktor. Inicjalizuje mape klawiszy (`m_keyMap`), tlumaczac wirtualne kody klawiszy Windows (`VK_*`) na wewnetrzne kody `Fw::Key`.
# # # `void WIN32Window::init()`

Inicjalizuje okno, wywolujac kolejno:
1.  `internalSetupTimerAccuracy()`: Zwieksza precyzje systemowego timera.
2.  `internalCreateWindow()`: Rejestruje klase okna i tworzy okno za pomoca `CreateWindowExA`.
3.  `internalCreateGLContext()`: Tworzy kontekst graficzny (WGL lub EGL).
4.  `internalRestoreGLContext()`: Aktywuje kontekst.
# # # `void WIN32Window::internalCreateGLContext()`

Implementacja tworzenia kontekstu graficznego:
-   **Dla OpenGL ES (`OPENGL_ES`)**: Uzywa EGL (ANGLE), pr�bujac kolejno backend�w D3D11, D3D9 i WARP, aby zapewnic maksymalna kompatybilnosc.
-   **Dla standardowego OpenGL**: Uzywa WGL. Tworzy `PIXELFORMATDESCRIPTOR`, wybiera format pikseli i tworzy kontekst za pomoca `wglCreateContext`.
# # # `LRESULT WIN32Window::windowProc(...)`

Gl�wna funkcja obslugi zdarzen okna (Window Procedure). Odbiera komunikaty od systemu Windows.
-   Przekazuje zdarzenia do `dispatcherWindowProc` w celu obslugi w gl�wnym watku aplikacji.
-   Bezposrednio obsluguje niekt�re komunikaty, kt�re musza byc przetworzone synchronicznie (np. `WM_SETCURSOR`, `WM_GETMINMAXINFO`).
# # # `LRESULT WIN32Window::dispatcherWindowProc(...)`

Metoda wywolywana przez `g_dispatcher` w gl�wnym watku. Tlumaczy komunikaty Windows (`WM_KEYDOWN`, `WM_LBUTTONDOWN`, `WM_MOUSEMOVE` itp.) na wewnetrzne `InputEvent` i przekazuje je do `m_onInputEvent` (czyli do `GraphicalApplication`).
# # # `void WIN32Window::poll()`

Przetwarza kolejke komunikat�w Windows za pomoca `PeekMessage`, `TranslateMessage` i `DispatchMessage`.
# # # `void WIN32Window::swapBuffers()`

Zamienia bufory ekranu za pomoca `SwapBuffers` (dla WGL) lub `eglSwapBuffers` (dla EGL).
# # # `void WIN32Window::setVerticalSync(bool enable)`

Wlacza/wylacza synchronizacje pionowa, uzywajac rozszerzen WGL (`WGL_EXT_swap_control`).
# # # Inne metody

Implementuja interfejs `PlatformWindow`, opakowujac odpowiednie funkcje WinAPI (np. `SetWindowTextW` dla `setTitle`, `ShellExecuteW` dla `openUrl`).
# # Zaleznosci i powiazania

-   Nagl�wki WinAPI.
-   Nagl�wki OpenGL/EGL/WGL.
-   Wsp�lpracuje z `GraphicalApplication` i `Mouse`.

---
# ?? win32window.h
# # Opis og�lny

Plik `win32window.h` deklaruje klase `WIN32Window`, kt�ra jest implementacja `PlatformWindow` dla systemu Windows.
# # Klasa `WIN32Window`
# # # Opis semantyczny
`WIN32Window` enkapsuluje uchwyty i logike zwiazana z natywnym oknem WinAPI. Zarzadza jego cyklem zycia, obsluga komunikat�w systemowych i tworzeniem kontekstu graficznego (WGL dla OpenGL lub EGL dla OpenGL ES przez ANGLE).
# # # Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnetrznego zarzadzania oknem i kontekstem GL.
-   `windowProc(...)`: Gl�wna funkcja obslugi komunikat�w Windows.
-   `dispatcherWindowProc(...)`: Handler komunikat�w wykonywany w gl�wnym watku.
-   `retranslateVirtualKey(...)`: Tlumaczy kody klawiszy WinAPI.
-   `getClientRect()`, `getWindowRect()`, `adjustWindowRect()`: Metody pomocnicze do geometrii okna.
# # # Zmienne prywatne

-   `m_window`: Uchwyt `HWND` do okna.
-   `m_instance`: Uchwyt `HINSTANCE` do modulu aplikacji.
-   `m_deviceContext`: Uchwyt `HDC` do kontekstu urzadzenia.
-   `m_cursors`: Wektor uchwyt�w `HCURSOR`.
-   `m_cursor`, `m_defaultCursor`: Aktywny i domyslny kursor.
-   `m_hidden`: Flaga ukrycia okna.
-   `m_egl...` / `m_wglContext`: Uchwyty do zasob�w EGL lub WGL.
# # Zaleznosci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Nagl�wki WinAPI i OpenGL/EGL.

---
# ?? x11window.h
# # Opis og�lny

Plik `x11window.h` deklaruje klase `X11Window`, kt�ra jest implementacja `PlatformWindow` dla system�w uniksowych uzywajacych serwera X11 (gl�wnie Linux).
# # Klasa `X11Window`
# # # Opis semantyczny
`X11Window` zarzadza natywnym oknem X11, obsluga jego zdarzen oraz tworzeniem kontekstu graficznego (GLX dla OpenGL lub EGL dla OpenGL ES).
# # # Metody prywatne i chronione

-   `internal...()`: Grupa metod do wewnetrznego zarzadzania oknem i kontekstem GL.
-   `getExtensionProcAddress(...)`, `isExtensionSupported(...)`: Do obslugi rozszerzen GLX/EGL.
# # # Zmienne prywatne

-   `m_display`: Wskaznik na `Display` (polaczenie z serwerem X11).
-   `m_visual`: Informacje o wizualu (glebia kolor�w itp.).
-   `m_window`: ID okna.
-   `m_rootWindow`: ID okna gl�wnego.
-   `m_colormap`: Mapa kolor�w.
-   `m_cursors`: Wektor kursor�w.
-   `m_cursor`, `m_hiddenCursor`: Aktywny i ukryty kursor.
-   `m_xim`, `m_xic`: Do obslugi metod wprowadzania tekstu.
-   `m_wmDelete`: Atom do obslugi zdarzenia zamkniecia okna.
-   `m_glxContext` / `m_egl...`: Uchwyty do zasob�w GLX lub EGL.
# # Zaleznosci i powiazania

-   `platformwindow.h`: Klasa bazowa.
-   Nagl�wki X11, GLX, EGL.

---
# ?? x11window.cpp
# # Opis og�lny

Plik `x11window.cpp` zawiera implementacje klasy `X11Window` dla system�w uniksowych z X11.
# # Klasa `X11Window`
# # # `X11Window::X11Window()`

Konstruktor. Inicjalizuje mape klawiszy, tlumaczac `KeySym` z X11 na `Fw::Key`.
# # # `void X11Window::init()`

Inicjalizuje okno, wywolujac kolejno:
1.  `internalOpenDisplay()`: Otwiera polaczenie z serwerem X11.
2.  `internalCheckGL()`: Sprawdza dostepnosc GLX/EGL.
3.  `internalChooseGLVisual()`: Wybiera odpowiedni format wizualny.
4.  `internalCreateGLContext()`: Tworzy kontekst graficzny.
5.  `internalCreateWindow()`: Tworzy okno X11.
# # # `void X11Window::internalCreateWindow()`

Tworzy okno za pomoca `XCreateWindow`, ustawia atrybuty, w tym maske zdarzen, i przygotowuje obsluge zamkniecia okna przez menedzera okien. Inicjalizuje r�wniez XIM/XIC do obslugi wprowadzania tekstu.
# # # `void X11Window::poll()`

Przetwarza kolejke zdarzen X11 za pomoca `XPending` i `XNextEvent`. Tlumaczy zdarzenia X11 (`KeyPress`, `ButtonPress`, `MotionNotify`, `ConfigureNotify` itp.) na wewnetrzne `InputEvent` i wywoluje odpowiednie `callbacki` w `g_dispatcher`. Obsluguje r�wniez logike auto-powtarzania klawiszy i wprowadzania tekstu.
# # # `void X11Window::swapBuffers()`

Zamienia bufory ekranu za pomoca `glXSwapBuffers` (dla GLX) lub `eglSwapBuffers` (dla EGL).
# # # `void X11Window::setFullscreen(bool fullscreen)`

Zmienia stan okna na pelnoekranowy, wysylajac odpowiedni komunikat `_NET_WM_STATE` do menedzera okien.
# # # `void X11Window::setClipboardText(...)` i `getClipboardText()`

Implementuja obsluge schowka za pomoca mechanizmu selekcji X11.
# # # Inne metody

Implementuja interfejs `PlatformWindow`, opakowujac odpowiednie funkcje X11 (np. `XStoreName` dla `setTitle`, `XMoveWindow` dla `move`).
# # Zaleznosci i powiazania

-   Nagl�wki X11, GLX, EGL.
-   Wsp�lpracuje z `GraphicalApplication`.

---
# ?? proxy.cpp
# # Opis og�lny

Plik `proxy.cpp` zawiera implementacje klasy `ProxyManager`, kt�ra zarzadza systemem proxy do komunikacji z serwerem gry.
# # Zmienne globalne
# # # `g_proxy`

Globalna instancja `ProxyManager`.
# # Klasa `ProxyManager`
# # # `void ProxyManager::init()` i `terminate()`

Uruchamiaja i zatrzymuja dedykowany watek sieciowy, w kt�rym dziala `io_context` dla operacji proxy.
# # # `void ProxyManager::clear()`

Zamyka wszystkie aktywne sesje i polaczenia z serwerami proxy.
# # # `bool ProxyManager::isActive()`

Zwraca `true`, jesli skonfigurowano co najmniej jeden serwer proxy.
# # # `void ProxyManager::addProxy(...)`

Dodaje nowy serwer proxy do puli. Tworzy obiekt `Proxy` i uruchamia go.
# # # `void ProxyManager::removeProxy(...)`

Usuwa serwer proxy z puli.
# # # `uint32_t ProxyManager::addSession(...)`

Tworzy nowa sesje proxy dla polaczenia z serwerem gry. Tworzy obiekt `Session` i zwraca jego unikalne ID.
# # # `void ProxyManager::removeSession(...)`

Zamyka sesje o danym ID.
# # # `void ProxyManager::send(...)`

Wysyla pakiet w ramach danej sesji. Znajduje odpowiedni obiekt `Session` i przekazuje mu pakiet.
# # # `int ProxyManager::getPing()`

Zwraca najlepszy (najnizszy) ping sposr�d wszystkich aktywnych i polaczonych serwer�w proxy.
# # Zaleznosci i powiazania

-   `framework/proxy/proxy.h`: Plik nagl�wkowy.
-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`.
-   Jest uzywana przez `Protocol` do tunelowania polaczenia przez serwery proxy.

---
# ?? proxy.h
# # Opis og�lny

Plik `proxy.h` deklaruje klase `ProxyManager`, kt�ra jest singletonem (`g_proxy`) odpowiedzialnym za zarzadzanie calym systemem polaczen proxy. Stanowi on gl�wny punkt wejscia do konfiguracji i wykorzystania tunelowania ruchu sieciowego.
# # Klasa `ProxyManager`
# # # Opis semantyczny
`ProxyManager` zarzadza pula dostepnych serwer�w proxy (obiekty `Proxy`) oraz pula aktywnych sesji klienta (obiekty `Session`). Jego zadaniem jest koordynacja miedzy sesjami a serwerami proxy, dynamiczne wybieranie najlepszych serwer�w do tunelowania ruchu oraz dostarczanie interfejsu do zarzadzania tym procesem z poziomu aplikacji i skrypt�w Lua. Dziala w dedykowanym watku sieciowym, aby nie blokowac gl�wnego watku aplikacji.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Uruchamia i zatrzymuje watek sieciowy `ProxyManager`. |
| `clear()` | Zamyka wszystkie aktywne sesje i polaczenia z serwerami proxy. |
| `setMaxActiveProxies(int value)` | Ustawia, przez ile najlepszych (pod wzgledem pingu) serwer�w proxy ma byc jednoczesnie tunelowany ruch dla kazdej sesji. |
| `isActive()` | Zwraca `true`, jesli co najmniej jeden serwer proxy jest skonfigurowany. |
| `addProxy(...)` / `removeProxy(...)` | Dodaje lub usuwa serwer proxy z puli dostepnych serwer�w. |
| `uint32_t addSession(...)` | Tworzy nowa sesje proxy dla polaczenia z serwerem gry. Zwraca unikalne ID sesji. |
| `void removeSession(uint32_t sessionId)` | Zamyka i usuwa sesje o podanym ID. |
| `void send(uint32_t sessionId, ProxyPacketPtr packet)` | Wysyla pakiet w ramach okreslonej sesji. `ProxyManager` przekazuje go do odpowiedniego obiektu `Session`. |
| `std::map<...> getProxies()` | Zwraca mape dostepnych serwer�w proxy wraz z ich pingiem. |
| `std::map<...> getProxiesDebugInfo()` | Zwraca szczeg�lowe informacje diagnostyczne o kazdym proxy. |
| `int getPing()` | Zwraca najnizszy ping sposr�d wszystkich aktywnych serwer�w proxy. |
# # # Zmienne prywatne

-   `m_io`: Kontekst `io_context` z Boost.Asio, na kt�rym dzialaja wszystkie operacje sieciowe proxy.
-   `m_guard`: Obiekt `work_guard`, kt�ry zapobiega zakonczeniu dzialania `m_io`, dop�ki `ProxyManager` jest aktywny.
-   `m_working`: Flaga kontrolujaca dzialanie watku.
-   `m_thread`: Dedykowany watek dla operacji sieciowych proxy.
-   `m_maxActiveProxies`: Maksymalna liczba proxy uzywanych przez jedna sesje.
-   `m_proxies`: Lista wskaznik�w na dostepne obiekty `Proxy`.
-   `m_sessions`: Lista wskaznik�w na aktywne obiekty `Session`.
# # # Zmienne globalne

-   `g_proxy`: Globalna instancja `ProxyManager`.
# # Zaleznosci i powiazania

-   `framework/proxy/proxy_client.h`: Definicje klas `Proxy` i `Session`, kt�rymi zarzadza.
-   Jest uzywana przez `Protocol` do tworzenia tunelowanych polaczen.
-   Jej API jest dostepne w Lua (przez `luafunctions.cpp`), co pozwala na dynamiczna konfiguracje proxy ze skrypt�w.

---
# ?? proxy_client.h
# # Opis og�lny

Plik `proxy_client.h` deklaruje dwie kluczowe klasy dla systemu proxy: `Proxy` i `Session`. Te klasy implementuja logike klienta, kt�ry laczy sie z serwerami proxy i tuneluje przez nie ruch sieciowy.
# # Definicje typ�w

-   `ProxyPacket`: Alias dla `std::vector<uint8_t>`, reprezentuje pojedynczy pakiet.
-   `ProxyPacketPtr`: Alias dla `std::shared_ptr<ProxyPacket>`.
-   `Session`, `SessionPtr`: Wczesna deklaracja i alias dla wskaznika na `Session`.
# # Klasa `Proxy`
# # # Opis semantyczny
`Proxy` reprezentuje pojedyncze, trwale polaczenie z jednym serwerem proxy. Jego zadaniem jest utrzymanie polaczenia, monitorowanie jego jakosci (ping), przesylanie pakiet�w dla wielu sesji oraz raportowanie swojego stanu do `ProxyManager`.
# # # Stale i typy wyliczeniowe

-   `CHECK_INTERVAL`: Interwal (w ms) sprawdzania stanu polaczenia i wysylania ping�w.
-   `BUFFER_SIZE`: Rozmiar bufora odczytu.
-   `enum ProxyState`: Definiuje stany, w jakich moze znajdowac sie polaczenie z proxy (np. `STATE_NOT_CONNECTED`, `STATE_CONNECTING`, `STATE_CONNECTED`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Proxy(...)` | Konstruktor. |
| `void start()` | Inicjuje cykl zycia obiektu, dodajac go do globalnej puli i uruchamiajac petle `check`. |
| `void terminate()` | Zamyka polaczenie i usuwa obiekt z globalnej puli. |
| `uint32_t getPing()` | Zwraca op�znienie do serwera proxy, uwzgledniajac priorytet. |
| `uint32_t getRealPing()` | Zwraca rzeczywiste op�znienie (bez priorytetu). |
| `bool isConnected()` | Zwraca `true`, jesli polaczenie jest w stanie `STATE_CONNECTED`. |
| `std::string getDebugInfo()`| Zwraca informacje diagnostyczne. |
| `bool isActive()` | Zwraca `true`, jesli przez to proxy przechodzi ruch co najmniej jednej sesji. |
| `void addSession(...)` | Wysyla do serwera proxy polecenie utworzenia nowej sesji tunelowania. |
| `void removeSession(...)` | Wysyla polecenie zamkniecia sesji. |
| `void send(...)` | Dodaje pakiet do kolejki wysylania do serwera proxy. |
# # Klasa `Session`
# # # Opis semantyczny
`Session` reprezentuje pojedyncza sesje klienta z serwerem gry, kt�ra jest tunelowana przez jeden lub wiecej serwer�w proxy. Moze dzialac w dw�ch trybach: jako serwer (akceptujac lokalne polaczenie od klienta gry) lub jako klient (gdy jest tworzona bezposrednio przez `Protocol`). Odpowiada za dynamiczne wybieranie najlepszych `Proxy` do wysylania pakiet�w oraz za re-asemblacje pakiet�w przychodzacych, kt�re moga docierac z r�znych `Proxy` i w r�znej kolejnosci.
# # # Stale

-   `CHECK_INTERVAL`: Interwal (w ms) sprawdzania stanu sesji i wyboru proxy.
-   `BUFFER_SIZE`: Rozmiar bufora.
-   `TIMEOUT`: Czas (w ms) braku aktywnosci, po kt�rym sesja jest zamykana.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `Session(...)` | Konstruktory dla trybu serwera i klienta. |
| `uint32_t getId()` | Zwraca unikalne ID sesji. |
| `void start(...)` | Uruchamia sesje, rozpoczynajac petle `check` i (w trybie serwera) nasluchiwanie na pakiety od klienta. |
| `void terminate(...)` | Zamyka sesje, informujac powiazane `Proxy` i klienta. |
| `void onPacket(...)` | Handler dla pakiet�w przychodzacych **od klienta gry**. Opakowuje je w protok�l proxy i wysyla. |
| `void onProxyPacket(...)` | Handler dla pakiet�w przychodzacych **od serwer�w proxy**. Odpakowuje je, sprawdza kolejnosc i przekazuje do klienta gry. |
# # Zaleznosci i powiazania

-   **Boost.Asio**: Fundamentalna zaleznosc do wszystkich operacji sieciowych.
-   Klasy `Proxy` i `Session` sa ze soba scisle powiazane. `Session` utrzymuje zbi�r `Proxy`, przez kt�re wysyla dane. `Proxy` jest swiadome sesji, kt�re obsluguje.
-   Obie klasy sa zarzadzane przez `ProxyManager`.
-   W projekcie istnieja globalne, dostepne w watku `io_context` kontenery `g_sessions` i `g_proxies` do wzajemnej komunikacji.

---
# ?? proxy_client.cpp
# # Opis og�lny

Plik `proxy_client.cpp` zawiera implementacje logiki dla klas `Proxy` i `Session`, kt�re razem tworza system klienta proxy. Kod jest w pelni asynchroniczny i oparty na Boost.Asio.
# # Zmienne globalne

-   `g_sessions`: Globalna mapa (`std::map`) przechowujaca slabe wskazniki (`std::weak_ptr`) do aktywnych sesji, indeksowane po ich ID.
-   `g_proxies`: Globalny zbi�r (`std::set`) przechowujacy wskazniki do aktywnych obiekt�w `Proxy`.
-   `UID`: Unikalny identyfikator tej instancji klienta, uzywany w pakietach ping.
# # Klasa `Proxy` (implementacja)
# # # `void Proxy::check(...)`

Gl�wna metoda cyklu zycia `Proxy`. Dziala jak maszyna stan�w, wywolywana cyklicznie przez `m_timer`.
-   W stanie `STATE_NOT_CONNECTED`, inicjuje `connect()`.
-   W stanie `STATE_CONNECTING`, sprawdza timeout dla polaczenia.
-   W stanie `STATE_CONNECTED`, wysyla pakiety ping, jesli nie oczekuje na odpowiedz.
-   W stanie `STATE_CONNECTING_WAIT_FOR_PING`, czeka na pierwsza odpowiedz ping.
# # # `void Proxy::connect()`

Asynchronicznie rozwiazuje nazwe hosta, a nastepnie laczy sie z serwerem proxy. Po pomyslnym polaczeniu, ustawia opcje gniazda (`no_delay`, rozmiary bufor�w), rozpoczyna odczyt nagl�wk�w i wysyla pierwszy ping.
# # # `void Proxy::disconnect()`

Zamyka gniazdo i resetuje stan do `STATE_NOT_CONNECTED`.
# # # `void Proxy::ping()`

Wysyla pakiet kontrolny "ping" do serwera proxy. Pakiet zawiera unikalne ID klienta (`UID`) i ostatni zmierzony ping.
# # # `void Proxy::onPing(uint32_t packetId)`

Handler odpowiedzi na ping. Oblicza nowy ping na podstawie czasu wyslania i odebrania pakietu. Jesli to byl pierwszy ping, zmienia stan na `STATE_CONNECTED`.
# # # `void Proxy::readHeader()` i `onHeader(...)`

Implementuja dwuetapowy odczyt pakietu: najpierw odczytywany jest 2-bajtowy nagl�wek z rozmiarem, a nastepnie reszta pakietu.
# # # `void Proxy::onPacket(...)`

Przetwarza przychodzacy pakiet. Na podstawie `sessionId` decyduje, czy jest to pakiet danych dla sesji, czy pakiet kontrolny (ping, zamkniecie sesji). Znajduje odpowiednia sesje w `g_sessions` i przekazuje jej dane.
# # # `void Proxy::send(...)`

Implementuje kolejke wysylania. Dodaje pakiet do `m_sendQueue` i rozpoczyna operacje `async_write`, jesli kolejka byla pusta.
# # Klasa `Session` (implementacja)
# # # `void Session::start(int maxConnections)`

Dodaje sesje do globalnej mapy `g_sessions`, uruchamia petle `check` i, w trybie serwera, rozpoczyna odczyt danych od klienta gry.
# # # `void Session::terminate(...)`

Zamyka sesje, informuje wszystkie powiazane `Proxy` o zamknieciu, zamyka gniazdo (jesli jest) i wywoluje `callback` rozlaczenia.
# # # `void Session::check(...)`

Metoda cykliczna. Sprawdza timeout braku aktywnosci i wywoluje `selectProxies` w celu optymalizacji routingu.
# # # `void Session::selectProxies()`

Inteligentny algorytm wyboru proxy.
1.  Iteruje po wszystkich globalnie dostepnych, polaczonych `Proxy`.
2.  Znajduje najlepsze `Proxy`, kt�re nie jest jeszcze uzywane przez te sesje.
3.  Jesli liczba aktywnych proxy dla tej sesji jest mniejsza niz `m_maxConnections`, dodaje najlepsze znalezione `Proxy`.
4.  Jesli liczba jest r�wna `m_maxConnections`, a znalezione `Proxy` jest znacznie lepsze niz najgorsze z aktualnie uzywanych, zastepuje najgorsze nowym.
5.  Po dodaniu nowego `Proxy`, wysyla do niego wszystkie pakiety z kolejki `m_proxySendQueue` (pakiety, kt�re mogly zostac utracone przez poprzednie `Proxy`).
# # # `void Session::onProxyPacket(...)`

Handler dla pakiet�w przychodzacych od proxy.
-   Sprawdza numer sekwencyjny (`packetId`). Odrzuca stare pakiety.
-   Usuwa z `m_proxySendQueue` pakiety wychodzace, kt�rych otrzymanie potwierdzil serwer proxy (`lastRecivedPacketId`).
-   Dodaje przychodzacy pakiet do kolejki `m_sendQueue` (kt�ra tutaj dziala jako bufor odbiorczy do re-asemblacji).
-   Jesli pakiet jest tym, na kt�ry czeka (`packetId == m_inputPacketId`), przetwarza go (i wszystkie nastepne w kolejce), wywolujac `m_recvCallback` lub wysylajac do klienta gry.
# # # `void Session::onPacket(...)`

Handler dla pakiet�w przychodzacych od klienta gry.
1.  Generuje nowy numer sekwencyjny (`m_outputPacketId`).
2.  Opakowuje pakiet w nagl�wek protokolu proxy.
3.  Dodaje opakowany pakiet do `m_proxySendQueue` (bufor do retransmisji).
4.  Wysyla pakiet do wszystkich aktywnych `Proxy`.

---
# ?? combinedsoundsource.cpp
# # Opis og�lny

Plik `combinedsoundsource.cpp` zawiera implementacje klasy `CombinedSoundSource`, kt�ra jest specjalnym rodzajem zr�dla dzwieku.
# # Klasa `CombinedSoundSource`
# # # Opis semantyczny
`CombinedSoundSource` dziala jak kontener na wiele innych obiekt�w `SoundSource`. Wszystkie operacje wykonane na `CombinedSoundSource` (np. `play()`, `stop()`, `setGain()`) sa delegowane i wykonywane na kazdym z podrzednych zr�del dzwieku, kt�re przechowuje. Jest to uzyteczne do tworzenia zlozonych efekt�w dzwiekowych lub do implementacji obejsc (workarounds), jak w przypadku problemu z dzwiekiem stereo na Linuksie (gdzie dzwiek stereo jest symulowany przez dwa zr�dla mono).
# # # `CombinedSoundSource::CombinedSoundSource()`

Konstruktor. Wywoluje konstruktor klasy bazowej `SoundSource` z ID 0, poniewaz sam nie reprezentuje rzeczywistego zr�dla w OpenAL.
# # # `void CombinedSoundSource::addSource(const SoundSourcePtr& source)`

Dodaje nowe podrzedne zr�dlo dzwieku do wewnetrznego wektora `m_sources`.
# # # Metody operacyjne (`play`, `stop`, `setLooping`, `setGain`, etc.)

Kazda z tych metod jest prosta petla, kt�ra iteruje po wektorze `m_sources` i wywoluje odpowiednia metode na kazdym z podrzednych obiekt�w `SoundSource`.

```cpp
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
# # # Metody sprawdzajace stan (`isBuffering`, `isPlaying`)

Zwracaja `true`, jesli **kt�rekolwiek** z podrzednych zr�del spelnia dany warunek.

```cpp
bool CombinedSoundSource::isPlaying()
{
    for(const SoundSourcePtr& source : m_sources) {
        if(source->isPlaying())
            return true;
}
    return false;
}
```
# # # `void CombinedSoundSource::update()`

Metoda wywolywana w petli `SoundManager::poll()`. Wywoluje `update()` na wszystkich podrzednych zr�dlach, co jest potrzebne np. do obslugi plynnego wyciszania/zglasniania (fading).
# # Zaleznosci i powiazania

-   `framework/sound/combinedsoundsource.h`: Plik nagl�wkowy.
-   Uzywana w `SoundManager` jako obejscie problemu z dzwiekiem stereo na Linuksie.

---
# ?? combinedsoundsource.h
# # Opis og�lny

Plik `combinedsoundsource.h` deklaruje klase `CombinedSoundSource`, kt�ra jest kompozytem wielu zr�del dzwieku, zachowujacym sie jak jedno.
# # Klasa `CombinedSoundSource`
# # # Opis semantyczny
`CombinedSoundSource` implementuje wzorzec projektowy "Kompozyt". Pozwala traktowac grupe obiekt�w `SoundSource` w ten sam spos�b, co pojedynczy obiekt. Wszystkie operacje sa delegowane do wewnetrznej kolekcji zr�del. Dziedziczy po `SoundSource`, aby zachowac zgodnosc interfejsu.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `CombinedSoundSource()` | Konstruktor. |
| `void addSource(...)` | Dodaje podrzedne zr�dlo dzwieku. |
| `std::vector<...> getSources()` | Zwraca liste podrzednych zr�del. |
| `play()`, `stop()`, `setLooping()`, `setGain()`, `setPosition()`, etc. | Metody delegujace operacje do wszystkich podrzednych zr�del. |
| `isBuffering()`, `isPlaying()` | Sprawdzaja stan, zwracajac `true`, jesli co najmniej jedno podrzedne zr�dlo jest w danym stanie. |
# # # Metody chronione

-   `virtual void update()`: Przeslania metode z `SoundSource` i wywoluje `update()` na wszystkich dzieciach.
# # # Zmienne prywatne

-   `m_sources`: Wektor (`std::vector`) przechowujacy wskazniki na podrzedne obiekty `SoundSource`.
# # Zaleznosci i powiazania

-   `framework/sound/soundsource.h`: Klasa bazowa i typ przechowywanych obiekt�w.
-   Jest tworzona i uzywana przez `SoundManager`.

---
# ?? oggsoundfile.cpp
# # Opis og�lny

Plik `oggsoundfile.cpp` zawiera implementacje klasy `OggSoundFile`, kt�ra jest odpowiedzialna za odczytywanie i dekodowanie plik�w dzwiekowych w formacie Ogg Vorbis.
# # Klasa `OggSoundFile`
# # # `OggSoundFile::OggSoundFile(const FileStreamPtr& fileStream)`

Konstruktor. Wywoluje konstruktor klasy bazowej `SoundFile`.
# # # `OggSoundFile::~OggSoundFile()`

Destruktor. Zwalnia zasoby zwiazane z biblioteka Vorbis, wywolujac `ov_clear()`.
# # # `bool OggSoundFile::prepareOgg()`
# # # # Opis semantyczny
Inicjalizuje proces dekodowania pliku Ogg Vorbis.
# # # # Dzialanie
1.  Tworzy strukture `ov_callbacks` z wskaznikami na statyczne metody `cb_...`, kt�re beda uzywane przez biblioteke Vorbis do odczytu danych ze strumienia `FileStream`.
2.  Wywoluje `ov_open_callbacks`, przekazujac `FileStream` jako zr�dlo danych.
3.  Pobiera informacje o pliku (liczba kanal�w, czestotliwosc pr�bkowania) za pomoca `ov_info`.
4.  Zapisuje te informacje w polach klasy bazowej (`m_channels`, `m_rate`).
5.  Oblicza calkowity rozmiar zdekompresowanych danych za pomoca `ov_pcm_total`.
# # # `int OggSoundFile::read(void *buffer, int bufferSize)`

Odczytuje i dekoduje fragment pliku dzwiekowego do podanego bufora. Wywoluje `ov_read`, kt�ra wykonuje cala prace zwiazana z dekodowaniem.
# # # `void OggSoundFile::reset()`

Przewija strumien dzwiekowy na poczatek za pomoca `ov_pcm_seek()`.
# # # Statyczne metody `cb_...`

Sa to funkcje zwrotne (callbacks) C, kt�re opakowuja metody obiektu `FileStream`, tlumaczac interfejs wymagany przez `libvorbisfile` na interfejs `FileStream`.
-   `cb_read`: opakowuje `file->read()`
-   `cb_seek`: opakowuje `file->seek()`
-   `cb_close`: opakowuje `file->close()`
-   `cb_tell`: opakowuje `file->tell()`
# # Zaleznosci i powiazania

-   `framework/sound/oggsoundfile.h`: Plik nagl�wkowy.
-   **libvorbisfile**: Kluczowa zaleznosc do dekodowania plik�w Ogg Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`, gdy wykryty zostanie plik w formacie Ogg.

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `sound` sluzy do wczesnych deklaracji klas i definicji typ�w wskaznik�w zwiazanych z systemem dzwieku. Jest on kompilowany tylko wtedy, gdy zdefiniowano flage `FW_SOUND`.
# # Wczesne deklaracje

-   `SoundManager`
-   `SoundSource`
-   `SoundBuffer`
-   `SoundFile`
-   `SoundChannel`
-   `StreamSoundSource`
-   `CombinedSoundSource`
-   `OggSoundFile`
# # Definicje typ�w

-   `SoundSourcePtr`
-   `SoundFilePtr`
-   `SoundBufferPtr`
-   `SoundChannelPtr`
-   `StreamSoundSourcePtr`
-   `CombinedSoundSourcePtr`
-   `OggSoundFilePtr`
# # Dolaczanie nagl�wk�w OpenAL

Plik dolacza nagl�wki biblioteki OpenAL (`al.h`, `alc.h`), kt�ra jest podstawa calego systemu dzwieku.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest dolaczany przez wszystkie pliki nagl�wkowe w module `sound`.

---
# ?? oggsoundfile.h
# # Opis og�lny

Plik `oggsoundfile.h` deklaruje klase `OggSoundFile`, kt�ra jest konkretna implementacja `SoundFile` do obslugi plik�w w formacie Ogg Vorbis.
# # Klasa `OggSoundFile`
# # # Opis semantyczny
`OggSoundFile` dziedziczy po `SoundFile` i implementuje jej wirtualne metody, uzywajac biblioteki `libvorbisfile` do dekodowania danych. Enkapsuluje ona strukture `OggVorbis_File` i dostarcza `callbacki` C, kt�re pozwalaja bibliotece Vorbis na odczyt danych ze strumienia `FileStream`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `OggSoundFile(...)` | Konstruktor. |
| `virtual ~OggSoundFile()` | Destruktor. |
| `bool prepareOgg()` | Inicjalizuje dekoder Vorbis i odczytuje metadane pliku. |
| `int read(...)` | Odczytuje i dekoduje fragment danych. |
| `void reset()` | Przewija strumien na poczatek. |
# # # Metody prywatne (statyczne)

-   `cb_read`, `cb_seek`, `cb_close`, `cb_tell`: Statyczne funkcje zwrotne dla `libvorbisfile`.
# # # Zmienne prywatne

-   `m_vorbisFile`: Uchwyt do struktur `libvorbisfile`.
# # Zaleznosci i powiazania

-   `framework/sound/soundfile.h`: Klasa bazowa.
-   `vorbis/vorbisfile.h`: Nagl�wek biblioteki Vorbis.
-   Jest tworzona przez `SoundFile::loadSoundFile`.

---
# ?? soundbuffer.cpp
# # Opis og�lny

Plik `soundbuffer.cpp` zawiera implementacje klasy `SoundBuffer`, kt�ra jest opakowaniem na bufor audio w OpenAL.
# # Klasa `SoundBuffer`
# # # Opis semantyczny
`SoundBuffer` reprezentuje blok danych audio (pr�bek dzwiekowych) zaladowany do pamieci, gotowy do odtworzenia przez OpenAL. Kazdy `SoundBuffer` ma unikalne ID w OpenAL. Jest uzywany do przechowywania kr�tkich, czesto odtwarzanych dzwiek�w, kt�re oplaca sie trzymac w pamieci.
# # # `SoundBuffer::SoundBuffer()`

Konstruktor. Generuje nowy bufor OpenAL za pomoca `alGenBuffers()` i zapisuje jego ID.
# # # `SoundBuffer::~SoundBuffer()`

Destruktor. Zwalnia bufor OpenAL za pomoca `alDeleteBuffers()`.
# # # `bool SoundBuffer::fillBuffer(const SoundFilePtr& soundFile)`

Wypelnia bufor danymi z obiektu `SoundFile`.
1.  Pobiera format, rozmiar i czestotliwosc pr�bkowania z `soundFile`.
2.  Odczytuje cala zawartosc pliku dzwiekowego do tymczasowego bufora w RAM.
3.  Wywoluje druga wersje `fillBuffer` w celu przeslania danych do OpenAL.
# # # `bool SoundBuffer::fillBuffer(ALenum sampleFormat, const DataBuffer<char>& data, int size, int rate)`

Przesyla surowe dane pr�bek dzwiekowych do bufora OpenAL za pomoca `alBufferData()`.
# # Zaleznosci i powiazania

-   `framework/sound/soundbuffer.h`: Plik nagl�wkowy.
-   `framework/sound/soundfile.h`: Do pobierania danych z plik�w.
-   Jest tworzona i zarzadzana przez `SoundManager`, kt�ry przechowuje je w cache.
-   Jest uzywana przez `SoundSource` jako zr�dlo danych do odtwarzania.

---
# ?? soundbuffer.h
# # Opis og�lny

Plik `soundbuffer.h` deklaruje klase `SoundBuffer`, kt�ra jest opakowaniem na bufor audio OpenAL.
# # Klasa `SoundBuffer`
# # # Opis semantyczny
`SoundBuffer` enkapsuluje ID bufora OpenAL i dostarcza metody do wypelniania go danymi dzwiekowymi. Jest to obiekt przechowujacy dane audio, kt�ry moze byc nastepnie przypisany do jednego lub wielu `SoundSource` w celu odtwarzania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundBuffer()` / `~SoundBuffer()` | Konstruktor i destruktor zarzadzajace zasobem OpenAL. |
| `bool fillBuffer(const SoundFilePtr& soundFile)` | Wypelnia bufor danymi z pliku dzwiekowego. |
| `bool fillBuffer(...)` | Wypelnia bufor surowymi danymi z pamieci. |
| `uint getBufferId()` | Zwraca ID bufora w OpenAL. |
# # # Zmienne prywatne

-   `m_bufferId`: ID (uchwyt) bufora w OpenAL.
# # Zaleznosci i powiazania

-   `framework/sound/declarations.h`: Definicje typ�w.
-   `framework/util/databuffer.h`: Do pracy z buforami danych.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# ?? soundfile.cpp
# # Opis og�lny

Plik `soundfile.cpp` zawiera implementacje klasy `SoundFile`, kt�ra jest abstrakcyjna klasa bazowa do odczytu r�znych format�w plik�w dzwiekowych.
# # Klasa `SoundFile`
# # # `SoundFile::SoundFile(const FileStreamPtr& fileStream)`

Konstruktor. Zapisuje wskaznik do strumienia pliku.
# # # `SoundFilePtr SoundFile::loadSoundFile(const std::string& filename)`
# # # # Opis semantyczny
Statyczna metoda fabryczna, kt�ra pr�buje zaladowac plik dzwiekowy. Automatycznie wykrywa format pliku i tworzy odpowiednia podklase `SoundFile`.
# # # # Dzialanie
1.  Otwiera plik za pomoca `g_resources.openFile()`.
2.  Odczytuje pierwsze 4 bajty ("magiczne bajty"), aby zidentyfikowac format.
3.  Jesli plik to Ogg Vorbis (zaczyna sie od "OggS"), tworzy instancje `OggSoundFile` i wywoluje jej metode `prepareOgg()`.
4.  W przypadku nieznanego formatu rzuca wyjatek.
# # # `ALenum SoundFile::getSampleFormat()`

Konwertuje wewnetrzne informacje o liczbie kanal�w i bitach na sekunde na format zrozumialy dla OpenAL (np. `AL_FORMAT_STEREO16`).
# # Zaleznosci i powiazania

-   `framework/sound/soundfile.h`: Plik nagl�wkowy.
-   `framework/sound/oggsoundfile.h`: Implementacja dla formatu Ogg.
-   `framework/core/resourcemanager.h`: Do otwierania plik�w.
-   Jest uzywana przez `SoundBuffer` i `StreamSoundSource` jako zr�dlo danych audio.

---
# ?? soundchannel.cpp
# # Opis og�lny

Plik `soundchannel.cpp` zawiera implementacje klasy `SoundChannel`, kt�ra reprezentuje kanal dzwiekowy, umozliwiajacy odtwarzanie dzwiek�w w spos�b zorganizowany i kontrolowany.
# # Klasa `SoundChannel`
# # # `SoundSourcePtr SoundChannel::play(...)`

Odtwarza nowy dzwiek na tym kanale. Jesli inny dzwiek jest juz odtwarzany, zostaje on zatrzymany. Wywoluje `g_sounds.play`, aby utworzyc i uruchomic nowe zr�dlo dzwieku.
# # # `void SoundChannel::stop(float fadetime)`

Zatrzymuje biezacy dzwiek i czysci kolejke. Opcjonalnie moze to zrobic z efektem wyciszania (`fadetime`).
# # # `void SoundChannel::enqueue(...)`

Dodaje plik dzwiekowy do kolejki odtwarzania. Gdy biezacy dzwiek sie skonczy, `update()` automatycznie odtworzy nastepny z kolejki. Kolejka jest tasowana, aby zapewnic losowa kolejnosc odtwarzania.
# # # `void SoundChannel::update()`

Metoda wywolywana cyklicznie przez `SoundManager`.
-   Sprawdza, czy biezace zr�dlo dzwieku zakonczylo odtwarzanie. Jesli tak, zwalnia je.
-   Jesli nie ma biezacego zr�dla, a kolejka nie jest pusta, pobiera nastepny utw�r z kolejki i go odtwarza.
# # # `void SoundChannel::setEnabled(bool enable)`

Wlacza lub wylacza kanal. Wylaczenie kanalu natychmiast zatrzymuje odtwarzany dzwiek i zapobiega odtwarzaniu nowych.
# # # `void SoundChannel::setGain(float gain)`

Ustawia og�lna glosnosc dla kanalu. Glosnosc ta jest mnozona przez glosnosc poszczeg�lnych dzwiek�w odtwarzanych na tym kanale.
# # Zaleznosci i powiazania

-   `framework/sound/soundchannel.h`: Plik nagl�wkowy.
-   `framework/sound/streamsoundsource.h`: Uzywane do efekt�w wyciszania.
-   `framework/sound/soundmanager.h`: Uzywa `g_sounds` do tworzenia zr�del dzwieku.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# ?? soundchannel.h
# # Opis og�lny

Plik `soundchannel.h` deklaruje klase `SoundChannel`, kt�ra reprezentuje logiczny kanal audio.
# # Klasa `SoundChannel`
# # # Opis semantyczny
`SoundChannel` pozwala na grupowanie i zarzadzanie odtwarzaniem dzwiek�w. Kazdy kanal moze odtwarzac tylko jeden dzwiek naraz, ale posiada kolejke, kt�ra pozwala na automatyczne odtwarzanie kolejnych utwor�w. Umozliwia globalna kontrole nad grupa dzwiek�w, np. ustawienie glosnosci dla calej muzyki w grze.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundChannel(int id)` | Konstruktor. |
| `SoundSourcePtr play(...)`| Odtwarza dzwiek na tym kanale, przerywajac poprzedni. |
| `void stop(...)` | Zatrzymuje odtwarzanie i czysci kolejke. |
| `void enqueue(...)` | Dodaje dzwiek do kolejki odtwarzania. |
| `void enable()` / `disable()` | Wlacza/wylacza kanal. |
| `void setGain(float gain)` | Ustawia glosnosc kanalu. |
| `float getGain()` | Zwraca glosnosc kanalu. |
| `bool isEnabled()` | Sprawdza, czy kanal jest wlaczony. |
| `int getId()` | Zwraca ID kanalu. |
# # # Metody chronione

-   `void update()`: Metoda cykliczna do zarzadzania kolejka.
# # # Zmienne prywatne

-   `m_queue`: Kolejka (`std::deque`) utwor�w do odtworzenia.
-   `m_currentSource`: Wskaznik na aktualnie odtwarzane zr�dlo dzwieku.
-   `m_enabled`: Flaga wlaczenia kanalu.
-   `m_id`: ID kanalu.
-   `m_gain`: Glosnosc kanalu.
# # Zaleznosci i powiazania

-   `framework/sound/soundsource.h`: Uzywa `SoundSourcePtr`.
-   Jest oznaczona jako `@bindclass`, co udostepnia jej API w Lua.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# ?? soundfile.h
# # Opis og�lny

Plik `soundfile.h` deklaruje abstrakcyjna klase bazowa `SoundFile`, kt�ra definiuje wsp�lny interfejs do odczytu danych z r�znych format�w plik�w dzwiekowych.
# # Klasa `SoundFile`
# # # Opis semantyczny
`SoundFile` jest abstrakcja nad plikiem dzwiekowym. Ukrywa szczeg�ly konkretnego formatu (np. Ogg, WAV), dostarczajac ujednolicony spos�b na odczytywanie zdekompresowanych pr�bek audio.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundFile(...)` | Konstruktor. |
| `static SoundFilePtr loadSoundFile(...)`| Statyczna metoda fabryczna, kt�ra wykrywa format pliku i tworzy odpowiednia podklase. |
| `virtual int read(...) = 0` | Czysto wirtualna metoda do odczytu zdekompresowanych danych. |
| `virtual void reset() = 0` | Czysto wirtualna metoda do przewiniecia strumienia na poczatek. |
| `bool eof()` | Sprawdza, czy osiagnieto koniec pliku. |
| `ALenum getSampleFormat()` | Konwertuje format (kanaly, bity) na format OpenAL. |
| `getChannels()`, `getRate()`, `getBpp()`, `getSize()`, `getName()`| Gettery dla metadanych pliku. |
# # # Zmienne chronione

-   `m_file`: Wskaznik na `FileStream`, z kt�rego odczytywane sa dane.
-   `m_channels`, `m_rate`, `m_bps`, `m_size`: Metadane dzwieku.
# # Zaleznosci i powiazania

-   `framework/sound/declarations.h`: Deklaracje.
-   `framework/core/filestream.h`: Uzywa `FileStream` jako zr�dla danych.
-   Jest klasa bazowa dla `OggSoundFile` i potencjalnie innych klas dla r�znych format�w.

---
# ?? soundmanager.cpp
# # Opis og�lny

Plik `soundmanager.cpp` zawiera implementacje klasy `SoundManager`, kt�ra jest singletonem (`g_sounds`) i centralnym punktem zarzadzania calym podsystemem dzwieku.
# # Zmienne globalne
# # # `g_sounds`

Globalna instancja `SoundManager`.
# # Klasa `SoundManager`
# # # `void SoundManager::init()`

Inicjalizuje system dzwieku.
1.  Otwiera domyslne urzadzenie audio za pomoca `alcOpenDevice`.
2.  Tworzy kontekst OpenAL za pomoca `alcCreateContext`.
3.  Ustawia ten kontekst jako aktywny za pomoca `alcMakeContextCurrent`.
# # # `void SoundManager::terminate()`

Zamyka system dzwieku. Zwalnia wszystkie zasoby (zr�dla, bufory, kanaly), niszczy kontekst i zamyka urzadzenie audio.
# # # `void SoundManager::poll()`

Metoda wywolywana cyklicznie w gl�wnej petli aplikacji.
-   Aktualizuje wszystkie aktywne zr�dla dzwieku (`m_sources`).
-   Aktualizuje wszystkie kanaly dzwiekowe (`m_channels`), co pozwala na zarzadzanie kolejkami odtwarzania.
-   Przetwarza asynchronicznie ladowane pliki dzwiekowe.
# # # `void SoundManager::setAudioEnabled(bool enable)`

Globalnie wlacza lub wylacza dzwiek. Wylaczenie powoduje zatrzymanie wszystkich odtwarzanych dzwiek�w.
# # # `void SoundManager::preload(std::string filename)`

Laduje plik dzwiekowy do pamieci i tworzy z niego `SoundBuffer`. Jest to optymalizacja dla kr�tkich, czesto uzywanych dzwiek�w. Bufor jest przechowywany w cache (`m_buffers`).
# # # `SoundSourcePtr SoundManager::play(...)`

Gl�wna metoda do odtwarzania dzwieku.
1.  Tworzy odpowiednie zr�dlo dzwieku (`SoundSource` dla skeszowanych plik�w lub `StreamSoundSource` dla strumieniowanych).
2.  Ustawia jego parametry (glosnosc, fadetime).
3.  Rozpoczyna odtwarzanie i dodaje zr�dlo do listy aktywnych zr�del.
# # # `SoundChannelPtr SoundManager::getChannel(int channel)`

Zwraca obiekt kanalu o danym ID. Jesli kanal nie istnieje, jest tworzony.
# # # `SoundSourcePtr SoundManager::createSoundSource(...)`

Metoda pomocnicza, kt�ra decyduje, czy utworzyc `SoundSource` (z bufora) czy `StreamSoundSource` (strumieniowanie z pliku). Dla Linuksa implementuje obejscie problemu z dzwiekiem stereo, tworzac `CombinedSoundSource` z dwoma zr�dlami mono.
# # # `void SoundManager::ensureContext()`

Upewnia sie, ze kontekst OpenAL jest aktywny w biezacym watku.
# # Zaleznosci i powiazania

-   **OpenAL**: Podstawowa biblioteka do obslugi dzwieku.
-   Wsp�lpracuje ze wszystkimi klasami z modulu `sound`.
-   `framework/core/asyncdispatcher.h`: Uzywany do asynchronicznego ladowania plik�w dzwiekowych.

---
# ?? soundmanager.h
# # Opis og�lny

Plik `soundmanager.h` deklaruje klase `SoundManager`, kt�ra jest singletonem (`g_sounds`) zarzadzajacym calym systemem dzwieku w aplikacji.
# # Klasa `SoundManager`
# # # Opis semantyczny
`SoundManager` jest centralnym interfejsem do odtwarzania dzwiek�w. Odpowiada za inicjalizacje i zamykanie OpenAL, zarzadzanie zr�dlami dzwieku (`SoundSource`), buforami (`SoundBuffer`) i kanalami (`SoundChannel`). Posiada mechanizm cachowania dla malych plik�w dzwiekowych i strumieniowania dla wiekszych.
# # # Stale

-   `MAX_CACHE_SIZE`: Maksymalny rozmiar pliku (w bajtach), kt�ry bedzie cachowany w pamieci.
-   `POLL_DELAY`: Minimalny interwal (w ms) miedzy wywolaniami `poll()`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Inicjalizuja i zamykaja system dzwieku. |
| `poll()` | Aktualizuje stan wszystkich aktywnych zr�del i kanal�w. |
| `setAudioEnabled(...)`, `enableAudio()`, `disableAudio()` | Globalnie wlaczaja/wylaczaja dzwiek. |
| `stopAll()` | Zatrzymuje wszystkie odtwarzane dzwieki. |
| `void preload(...)` | Laduje dzwiek do pamieci podrecznej. |
| `SoundSourcePtr play(...)` | Odtwarza dzwiek z pliku. |
| `SoundChannelPtr getChannel(...)` | Pobiera lub tworzy kanal dzwiekowy. |
| `std::string resolveSoundFile(...)` | Rozwiazuje sciezke do pliku dzwiekowego. |
| `void ensureContext()` | Upewnia sie, ze kontekst OpenAL jest aktywny. |
# # # Zmienne prywatne

-   `m_device`, `m_context`: Uchwyty do urzadzenia i kontekstu OpenAL.
-   `m_streamFiles`: Mapa do zarzadzania asynchronicznym ladowaniem plik�w strumieniowanych.
-   `m_buffers`: Cache dla `SoundBuffer`.
-   `m_sources`: Lista aktywnych zr�del dzwieku.
-   `m_audioEnabled`: Globalna flaga wlaczenia dzwieku.
-   `m_channels`: Mapa kanal�w dzwiekowych.
# # # Zmienne globalne

-   `g_sounds`: Globalna instancja `SoundManager`.
# # Zaleznosci i powiazania

-   `framework/sound/declarations.h`, `soundchannel.h`.
-   Oznaczona jako `@bindsingleton g_sounds`, udostepnia swoje API w Lua.

---
# ?? soundsource.cpp
# # Opis og�lny

Plik `soundsource.cpp` zawiera implementacje klasy `SoundSource`, kt�ra jest opakowaniem na zr�dlo dzwieku w OpenAL.
# # Klasa `SoundSource`
# # # `SoundSource::SoundSource()`

Konstruktor. Generuje nowe zr�dlo w OpenAL za pomoca `alGenSources()` i ustawia domyslne parametry, takie jak dystans referencyjny.
# # # `SoundSource::~SoundSource()`

Destruktor. Zatrzymuje odtwarzanie i zwalnia zas�b zr�dla w OpenAL za pomoca `alDeleteSources()`.
# # # `void SoundSource::play()`

Rozpoczyna odtwarzanie dzwieku za pomoca `alSourcePlay()`.
# # # `void SoundSource::stop()`

Zatrzymuje odtwarzanie (`alSourceStop()`) i odlacza bufor od zr�dla.
# # # `bool SoundSource::isBuffering()`

Sprawdza, czy zr�dlo jest w stanie innym niz `AL_STOPPED` (czyli `AL_PLAYING` lub `AL_PAUSED`).
# # # Metody `set...()`

Sa to opakowania na funkcje `alSource...()`, kt�re ustawiaja r�zne wlasciwosci zr�dla dzwieku:
-   `setBuffer`: Przypisuje `SoundBuffer` do zr�dla.
-   `setLooping`: Ustawia zapetlanie.
-   `setRelative`: Ustawia, czy pozycja zr�dla jest wzgledna do sluchacza.
-   `setGain`: Ustawia glosnosc.
-   `setPitch`: Ustawia wysokosc dzwieku.
-   `setPosition`, `setVelocity`: Ustawiaja wlasciwosci 3D dzwieku.
# # # `void SoundSource::setFading(...)`

Inicjuje proces plynnego zglasniania (`FadingOn`) lub wyciszania (`FadingOff`) dzwieku w okreslonym czasie. Zapisuje stan i czas rozpoczecia.
# # # `void SoundSource::update()`

Metoda wywolywana cyklicznie przez `SoundManager`. Implementuje logike "fadingu", aktualizujac glosnosc zr�dla w kazdej klatce na podstawie uplywajacego czasu.
# # Zaleznosci i powiazania

-   `framework/sound/soundsource.h`: Plik nagl�wkowy.
-   `framework/sound/soundbuffer.h`: Uzywa `SoundBuffer` jako zr�dla danych.
-   `framework/core/clock.h`: Do obslugi czasu w mechanizmie "fading".

---
# ?? streamsoundsource.cpp
# # Opis og�lny

Plik `streamsoundsource.cpp` zawiera implementacje klasy `StreamSoundSource`, kt�ra jest specjalizacja `SoundSource` do odtwarzania dzwiek�w strumieniowo z plik�w.
# # Klasa `StreamSoundSource`
# # # Opis semantyczny
`StreamSoundSource` jest przeznaczona do odtwarzania dlugich plik�w dzwiekowych (np. muzyki), kt�re nie sa w calosci ladowane do pamieci. Zamiast tego, uzywa mechanizmu kolejkowania malych bufor�w w OpenAL. Dane sa odczytywane z pliku i dekodowane w locie, a nastepnie umieszczane w buforach, kt�re sa dodawane do kolejki odtwarzania zr�dla.
# # # `StreamSoundSource::StreamSoundSource()`

Konstruktor. Tworzy `STREAM_FRAGMENTS` (zwykle 4) malych obiekt�w `SoundBuffer`, kt�re beda uzywane do kolejkowania.
# # # `void StreamSoundSource::setSoundFile(...)`

Ustawia plik dzwiekowy, z kt�rego beda strumieniowane dane. Jesli zr�dlo czekalo na plik, rozpoczyna odtwarzanie.
# # # `void StreamSoundSource::play()`

Rozpoczyna odtwarzanie. Jesli plik dzwiekowy nie zostal jeszcze zaladowany (bo ladowanie odbywa sie asynchronicznie), ustawia flage `m_waitingFile`. W przeciwnym razie, wywoluje `queueBuffers()` i `SoundSource::play()`.
# # # `void StreamSoundSource::stop()`

Zatrzymuje odtwarzanie i czysci kolejke bufor�w za pomoca `unqueueBuffers()`.
# # # `void StreamSoundSource::update()`

Metoda wywolywana cyklicznie.
1.  Sprawdza, ile bufor�w zostalo juz przetworzonych (odtworzonych) przez OpenAL.
2.  Odkolejkowuje przetworzone bufory.
3.  Wypelnia je nowymi danymi z pliku i ponownie dodaje do kolejki.
4.  Obsluguje zapetlanie i sprawdza, czy odtwarzanie nie zostalo przerwane przez "buffer underrun" (gdy OpenAL skonczy odtwarzac, a nie ma nowych bufor�w w kolejce).
# # # `bool StreamSoundSource::fillBufferAndQueue(uint buffer)`

Kluczowa metoda.
1.  Odczytuje fragment danych z `m_soundFile`.
2.  Obsluguje zapetlanie, resetujac plik po dojsciu do konca.
3.  Opcjonalnie wykonuje "down-mix" z stereo do mono, jesli `m_downMix` jest ustawione.
4.  Wypelnia podany bufor OpenAL nowymi danymi.
5.  Dodaje bufor do kolejki odtwarzania zr�dla.
# # Zaleznosci i powiazania

-   `framework/sound/streamsoundsource.h`: Plik nagl�wkowy.
-   `framework/sound/soundbuffer.h`, `soundfile.h`: Uzywa tych klas do zarzadzania buforami i odczytu plik�w.
-   Jest tworzona przez `SoundManager` dla plik�w, kt�re nie sa cachowane.

---
# ?? streamsoundsource.h
# # Opis og�lny

Plik `streamsoundsource.h` deklaruje klase `StreamSoundSource`, kt�ra jest implementacja `SoundSource` do strumieniowego odtwarzania dzwieku.
# # Klasa `StreamSoundSource`
# # # Opis semantyczny
`StreamSoundSource` pozwala na odtwarzanie dlugich plik�w dzwiekowych bez potrzeby ladowania ich w calosci do pamieci. Dziala poprzez dzielenie dzwieku na male fragmenty, kt�re sa dynamicznie ladowane do kolejki bufor�w OpenAL w trakcie odtwarzania.
# # # Stale

-   `STREAM_BUFFER_SIZE`: Calkowity rozmiar bufora cyklicznego w pamieci.
-   `STREAM_FRAGMENTS`: Liczba fragment�w (bufor�w OpenAL), na kt�re jest podzielony bufor cykliczny.
-   `STREAM_FRAGMENT_SIZE`: Rozmiar pojedynczego fragmentu.
# # # Typ wyliczeniowy `DownMix`

Okresla, czy i jak konwertowac dzwiek stereo na mono (tylko lewy kanal, tylko prawy, lub brak konwersji).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `StreamSoundSource()` | Konstruktor, tworzy bufory. |
| `virtual ~StreamSoundSource()` | Destruktor. |
| `void play()` | Rozpoczyna strumieniowanie i odtwarzanie. |
| `void stop()` | Zatrzymuje odtwarzanie i czysci kolejke bufor�w. |
| `bool isPlaying()` | Zwraca, czy zr�dlo jest w stanie odtwarzania. |
| `void setSoundFile(...)` | Ustawia plik dzwiekowy do strumieniowania. |
| `void downMix(...)` | Ustawia tryb konwersji na mono. |
| `void update()` | Aktualizuje kolejke bufor�w (metoda cykliczna). |
# # # Zmienne prywatne

-   `m_soundFile`: Wskaznik na plik dzwiekowy.
-   `m_buffers`: Tablica bufor�w OpenAL uzywanych w kolejce.
-   `m_downMix`: Tryb konwersji na mono.
-   `m_looping`, `m_playing`, `m_eof`, `m_waitingFile`: Flagi stanu.
# # Zaleznosci i powiazania

-   `framework/sound/soundsource.h`: Klasa bazowa.
-   Jest tworzona przez `SoundManager` do odtwarzania duzych plik�w dzwiekowych.

---
# ?? soundsource.h
# # Opis og�lny

Plik `soundsource.h` deklaruje klase `SoundSource`, kt�ra jest abstrakcyjnym opakowaniem na zr�dlo dzwieku w OpenAL.
# # Klasa `SoundSource`
# # # Opis semantyczny
`SoundSource` reprezentuje punkt w przestrzeni, z kt�rego wydobywa sie dzwiek. Enkapsuluje ona ID zr�dla OpenAL i dostarcza interfejs do kontrolowania jego wlasciwosci, takich jak glosnosc, wysokosc dzwieku, pozycja, zapetlanie i stan odtwarzania. Dziedziczy po `LuaObject`.
# # # Typ wyliczeniowy `FadeState`

-   `NoFading`: Brak efektu.
-   `FadingOn`: Dzwiek jest w trakcie zglasniania.
-   `FadingOff`: Dzwiek jest w trakcie wyciszania.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `SoundSource()` | Konstruktor. |
| `virtual ~SoundSource()` | Destruktor. |
| `virtual void play()` | Rozpoczyna odtwarzanie. |
| `virtual void stop()` | Zatrzymuje odtwarzanie. |
| `virtual bool isBuffering()` | Sprawdza stan zr�dla w OpenAL. |
| `virtual bool isPlaying()` | Domyslnie to samo co `isBuffering`. |
| `void setName(...)` | Ustawia nazwe (do identyfikacji). |
| `virtual void setLooping(...)` | Wlacza/wylacza zapetlanie. |
| `virtual void setRelative(...)` | Ustawia, czy pozycja jest wzgledna do sluchacza. |
| `virtual void setReferenceDistance(...)` | Ustawia dystans referencyjny dla tlumienia dzwieku 3D. |
| `virtual void setGain(...)` | Ustawia glosnosc. |
| `virtual void setPitch(...)` | Ustawia wysokosc dzwieku. |
| `virtual void setPosition(...)` / `setVelocity(...)` | Ustawiaja wlasciwosci 3D. |
| `virtual void setFading(...)` | Inicjuje efekt plynnego zglasniania/wyciszania. |
# # # Metody chronione

-   `void setBuffer(...)`: Przypisuje `SoundBuffer` do zr�dla.
-   `virtual void update()`: Metoda cykliczna do obslugi np. "fadingu".
# # # Zmienne

-   `m_sourceId`: ID zr�dla w OpenAL.
-   `m_name`: Nazwa.
-   `m_buffer`: Wskaznik na `SoundBuffer` (dla zr�del nie-strumieniowych).
-   `m_fade...`: Zmienne do obslugi "fadingu".
-   `m_gain`: Aktualna glosnosc.
# # Zaleznosci i powiazania

-   `framework/sound/declarations.h`, `soundbuffer.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasa bazowa dla `StreamSoundSource` i `CombinedSoundSource`.
-   Jest tworzona i zarzadzana przez `SoundManager`.

---
# ?? any.h
# # Opis og�lny

Plik `any.h` zawiera implementacje klasy `stdext::any`, kt�ra jest prosta, wlasna wersja `std::any` (dostepnego od C++17) lub `boost::any`. Pozwala na przechowywanie wartosci dowolnego typu w spos�b bezpieczny typowo.
# # Klasa `any`
# # # Opis semantyczny
`any` dziala jak polimorficzny kontener. Wewnatrz przechowuje wskaznik na obiekt-opakowanie (`placeholder`), kt�ry jest tworzony na stercie. Obiekt-opakowanie jest szablonem (`holder<T>`), kt�ry przechowuje rzeczywista wartosc i informacje o jej typie (`type_info`).
# # # Struktury wewnetrzne

-   **`placeholder`**: Abstrakcyjna klasa bazowa dla opakowan. Definiuje wirtualny interfejs do pobierania `type_info` i klonowania.
-   **`holder<T>`**: Szablonowa klasa pochodna, kt�ra faktycznie przechowuje wartosc typu `T`.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `any()` | Konstruktor domyslny (pusty). |
| `any(const any& other)` | Konstruktor kopiujacy (gleboka kopia). |
| `template<typename T> any(const T& value)` | Konstruktor szablonowy, tworzy `holder<T>`. |
| `~any()` | Destruktor, zwalnia `placeholder`. |
| `any& swap(any& rhs)` | Zamienia zawartosc dw�ch obiekt�w `any`. |
| `operator=` | Operatory przypisania. |
| `bool empty()` | Zwraca `true`, jesli `any` nie przechowuje wartosci. |
| `template<typename T> const T& cast() const` | Rzutuje i zwraca przechowywana wartosc. Rzuca `VALIDATE` error, jesli typ jest nieprawidlowy. |
| `const std::type_info & type() const` | Zwraca `type_info` przechowywanej wartosci. |
# # # Funkcja `any_cast`

Funkcja pomocnicza, kt�ra wykonuje bezpieczne rzutowanie. Sprawdza, czy typ przechowywany w `any` zgadza sie z typem docelowym.
# # Zaleznosci i powiazania

-   `<algorithm>`, `<typeinfo>`: Standardowe nagl�wki C++.
-   Jest uzywana w `dynamic_storage` do przechowywania wartosci r�znych typ�w.

---
# ?? cast.h
# # Opis og�lny

Plik `cast.h` zawiera zestaw szablonowych funkcji i klas do konwersji (rzutowania) miedzy r�znymi typami danych, gl�wnie z i do `std::string`.
# # Funkcje `cast`
# # # `template<typename T, typename R> bool cast(const T& in, R& out)`

Gl�wna, szablonowa funkcja. Uzywa `std::stringstream` do konwersji. Zwraca `true`, jesli konwersja sie powiodla.
# # # Specjalizacje

Plik zawiera specjalizacje dla typowych i problematycznych konwersji, aby byly one bardziej wydajne i niezawodne:
-   `string` do `string`: Proste przypisanie.
-   `string` do `bool`: Obsluguje tylko "true" i "false".
-   `string` do `char`: Tylko dla string�w o dlugosci 1.
-   `string` do `long`, `int`, `double`, `float`: Uzywaja `atol` i `atof`, ale z dodatkowa walidacja znak�w, aby uniknac nieprawidlowych konwersji (np. "123a" nie zostanie skonwertowane).
-   `bool` do `string`: Konwertuje na "true" lub "false".
# # Klasa `cast_exception`

Wyjatek rzucany przez `safe_cast`, gdy konwersja sie nie powiedzie.
# # Funkcje `safe_cast` i `unsafe_cast`

-   **`safe_cast<R, T>(...)`**: Opakowanie na `cast`, kt�re rzuca `cast_exception` w przypadku niepowodzenia.
-   **`unsafe_cast<R, T>(...)`**: Opakowanie na `safe_cast`, kt�re lapie wyjatek, loguje blad i zwraca wartosc domyslna.
# # Zaleznosci i powiazania

-   `stdext/exception.h`, `demangle.h`: Do obslugi bled�w i nazw typ�w.
-   Sa to fundamentalne narzedzia uzywane w calym projekcie, szczeg�lnie do parsowania wartosci z plik�w OTML i konwersji typ�w dla Lua.

---
# ?? demangle.cpp
# # Opis og�lny

Plik `demangle.cpp` zawiera implementacje funkcji `demangle_name`, kt�ra konwertuje "znieksztalcone" (mangled) nazwy typ�w C++ na ich czytelna forme.
# # Funkcja `demangle_name`
# # # `const char* demangle_name(const char* name)`
# # # # Opis semantyczny
Nazwy typ�w C++ (szczeg�lnie w przypadku szablon�w i przestrzeni nazw) sa przez kompilator zamieniane na unikalne, ale nieczytelne identyfikatory (np. `N6stdext11cast_exceptionE`). Funkcja ta odwraca ten proces, uzywajac narzedzi specyficznych dla danego kompilatora.
# # # # Implementacja
-   **Dla MSVC (`_MSC_VER`)**: Uzywa funkcji `UnDecorateSymbolName` z biblioteki `DbgHelp.dll`.
-   **Dla GCC/Clang**: Uzywa funkcji `abi::__cxa_demangle` z biblioteki `cxxabi`.
# # Zaleznosci i powiazania

-   `framework/stdext/demangle.h`: Plik nagl�wkowy.
-   Nagl�wki specyficzne dla platformy (`dbghelp.h` lub `cxxabi.h`).
-   Jest uzywana w systemie rzutowania (`cast_exception`) i w logowaniu, aby dostarczac czytelne nazwy typ�w w komunikatach o bledach.

---
# ?? compiler.h
# # Opis og�lny

Plik `compiler.h` zawiera makra i dyrektywy preprocesora specyficzne dla kompilatora. Jego celem jest ujednolicenie obslugi r�znych kompilator�w (GCC, Clang, MSVC) i zapewnienie kompatybilnosci.
# # Zawartosc
# # # `BUILD_COMPILER`

Makro, kt�re jest definiowane jako string zawierajacy nazwe i wersje uzywanego kompilatora. Jest to ustalane na podstawie predefiniowanych makr kompilatora (`__clang__`, `__GNUC__`, `_MSC_VER`).
# # # Sprawdzanie wersji kompilatora

Plik zawiera dyrektywy `#error`, kt�re zatrzymaja kompilacje, jesli wersja kompilatora jest zbyt stara (wymagany GCC >= 4.6, MSVC >= 2013).
# # # Wylaczanie ostrzezen (MSVC)

Dla kompilatora MSVC, wylacza szereg czesto wystepujacych, ale zazwyczaj nieszkodliwych ostrzezen (`#pragma warning(disable: ...)`), aby utrzymac czysty output kompilacji.
# # # `__PRETTY_FUNCTION__`

Dla MSVC, definiuje `__PRETTY_FUNCTION__` jako alias dla `__FUNCDNAME__`, aby ujednolicic spos�b uzyskiwania "ozdobnej" nazwy funkcji.
# # # `likely(x)` i `unlikely(x)`

Makra do optymalizacji podpowiedzi dla kompilatora (branch prediction). Dla GCC/Clang uzywaja `__builtin_expect`. Dla innych kompilator�w sa puste.
# # # Sprawdzanie wsparcia C++0x

Sprawdza, czy kompilator wspiera wymagany standard C++ (C++11 lub nowszy).
# # Zaleznosci i powiazania

-   Jest to jeden z najbardziej fundamentalnych plik�w nagl�wkowych, dolaczany przez `global.h`, i wplywa na kompilacje calego projektu.

---
# ?? demangle.h
# # Opis og�lny

Plik `demangle.h` deklaruje funkcje pomocnicze do "demanglowania" (odkodowywania) nazw typ�w C++, kt�re sa znieksztalcane przez kompilator w procesie kompilacji.
# # Namespace `stdext`
# # # Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `const char* demangle_name(const char* name)` | Przyjmuje znieksztalcona nazwe i zwraca jej czytelna wersje. |
| `template<typename T> std::string demangle_class()`| Szablonowa funkcja, kt�ra zwraca czytelna nazwe klasy dla danego typu `T`. |
| `template<typename T> std::string demangle_type()` | Szablonowa funkcja, kt�ra zwraca czytelna nazwe dowolnego typu `T`. |
# # Zaleznosci i powiazania

-   `<typeinfo>`, `<string>`: Standardowe nagl�wki.
-   Jest uzywana do generowania czytelnych komunikat�w o bledach, np. w `cast_exception` i `LuaBadValueCastException`.

---
# ?? boolean.h
# # Opis og�lny

Plik `boolean.h` deklaruje prosta klase szablonowa `stdext::boolean`, kt�ra jest opakowaniem na typ `bool` z mozliwoscia zdefiniowania wartosci domyslnej.
# # Klasa `boolean`
# # # `template<bool def>`

-   **Parametr szablonu `def`**: Okresla domyslna wartosc (`true` lub `false`).
# # # Opis semantyczny
`boolean` zachowuje sie jak standardowy `bool`, ale jego konstruktor domyslny inicjalizuje go wartoscia `def`. Jest to przydatne do inicjalizacji p�l w klasach, gdzie domyslna wartosc `bool` (kt�ra jest nieokreslona) moglaby prowadzic do bled�w.
# # # Przyklad uzycia

```cpp
class MyWidget {
    stdext::boolean<true> m_visible; // Domyslnie true
    stdext::boolean<false> m_enabled; // Domyslnie false
};
```
# # # Operatory

Klasa przeciaza operatory `operator bool&`, `operator bool const&` i `operator=`, co pozwala na uzywanie jej w taki sam spos�b, jak standardowego `bool`.
# # Zaleznosci i powiazania

-   Jest to prosta klasa narzedziowa, uzywana w wielu miejscach w projekcie (np. w `UIWidget`) do definiowania flag stanu.

---
# ?? dumper.h
# # Opis og�lny

Plik `dumper.h` zawiera proste narzedzie do szybkiego debugowania, kt�re pozwala na wypisywanie wartosci wielu zmiennych na standardowe wyjscie w jednej linii.
# # Zmienne globalne
# # # `dump`

Globalny obiekt o specjalnej strukturze, kt�ry przeciaza operator `<<`.
# # # Opis semantyczny
Uzycie `dump` pozwala na tworzenie lancuchowych wywolan, kt�re wypisuja wartosci oddzielone spacjami, a na koncu automatycznie dodaja znak nowej linii.
# # # Przyklad uzycia
```cpp
int x = 10;
std::string y = "hello";
dump << "Wartosci:" << x << y;
```
**Wyjscie:**
```
Wartosci: 10 hello 
```
# # # Implementacja
-   Tworzy globalny obiekt, kt�rego `operator<<` zwraca tymczasowy obiekt `dumper_dummy`.
-   `dumper_dummy` ma przeciazony `operator<<` do wypisywania wartosci i destruktor, kt�ry wypisuje znak nowej linii.
# # Zaleznosci i powiazania

-   `<iostream>`: Do wypisywania na `std::cout`.
-   Jest to narzedzie wylacznie do cel�w debugowania.

---
# ?? dynamic_storage.h
# # Opis og�lny

Plik `dynamic_storage.h` deklaruje klase szablonowa `dynamic_storage`, kt�ra implementuje dynamiczny kontener asocjacyjny, gdzie kluczem jest typ calkowitoliczbowy, a wartoscia moze byc dowolny typ (przechowywany za pomoca `stdext::any`).
# # Klasa `dynamic_storage`
# # # Opis semantyczny
`dynamic_storage` dziala jak mapa, ale jest zaimplementowana w oparciu o `std::vector<stdext::any>`. Klucz (`Key`) jest uzywany jako indeks w wektorze. Jest to wydajne, jesli klucze sa malymi, kolejnymi liczbami calkowitymi. Pozwala na przechowywanie heterogenicznych danych w jednym kontenerze.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `template<typename T> void set(...)` | Ustawia wartosc dla danego klucza. W razie potrzeby rozszerza wektor. |
| `bool remove(...)` | Usuwa wartosc dla danego klucza (zastepujac ja pustym `any`). |
| `template<typename T> T get(...) const` | Pobiera wartosc dla danego klucza, rzutujac ja na typ `T`. Zwraca wartosc domyslna, jesli klucz nie istnieje. |
| `bool has(...) const` | Sprawdza, czy klucz istnieje i ma przypisana wartosc. |
| `std::size_t size() const` | Zwraca liczbe niepustych element�w. |
| `void clear()` | Czysci kontener. |
# # # Zmienne prywatne

-   `m_data`: Wektor `stdext::any`, kt�ry przechowuje dane.
# # Zaleznosci i powiazania

-   `stdext/types.h`, `stdext/any.h`: Wymagane definicje.
-   `<unordered_map>`: Nagl�wek jest dolaczony, ale nie jest uzywany.
-   Moze byc uzywana do implementacji niestandardowych system�w atrybut�w lub wlasciwosci dla obiekt�w.

---
# ?? exception.h
# # Opis og�lny

Plik `exception.h` deklaruje klase `stdext::exception`, kt�ra jest bazowa klasa dla wszystkich niestandardowych wyjatk�w w projekcie.
# # Klasa `exception`
# # # Opis semantyczny
Dziedziczy po `std::exception` i rozszerza ja o konstruktor przyjmujacy `std::string` oraz o przechowywanie komunikatu bledu w `m_what`. Upraszcza to tworzenie i rzucanie wyjatk�w z niestandardowymi komunikatami.
# # # Metody

-   `exception(const std::string& what)`: Konstruktor.
-   `virtual const char* what() const throw()`: Zwraca komunikat bledu.
# # Funkcja `throw_exception`

Funkcja pomocnicza, kt�ra tworzy i rzuca `stdext::exception`.

```cpp
inline void throw_exception(const std::string& what) { throw exception(what); }
```
# # Zaleznosci i powiazania

-   Jest klasa bazowa dla `cast_exception` i `LuaException`.
-   Jest uzywana w calym projekcie do sygnalizowania bled�w, kt�re moga byc przechwycone i obsluzone na wyzszym poziomie.

---
# ?? fastrand.h
# # Opis og�lny

Plik `fastrand.h` zawiera implementacje prostej i szybkiej funkcji do generowania liczb pseudolosowych.
# # Funkcja `fastrand`
# # # `static int fastrand()`
# # # # Opis semantyczny
Implementuje liniowy generator kongruentny (Linear Congruential Generator - LCG). Jest to bardzo prosty i szybki algorytm, ale o niskiej jakosci losowosci w por�wnaniu do nowoczesniejszych generator�w (jak Mersenne Twister). Jest odpowiedni do zastosowan, gdzie wydajnosc jest wazniejsza niz jakosc losowosci (np. proste efekty wizualne).
# # # # Dzialanie
-   Uzywa statycznej zmiennej `g_seed` jako stanu.
-   W kazdym wywolaniu, aktualizuje `g_seed` wedlug wzoru: `g_seed = (a * g_seed + c)`.
-   Zwraca 15 najbardziej znaczacych bit�w z wyzszych 16 bit�w wyniku.
# # Zaleznosci i powiazania

-   Jest to samodzielna funkcja narzedziowa.

---
# ?? math.cpp
# # Opis og�lny

Plik `math.cpp` zawiera implementacje funkcji matematycznych i losowych zadeklarowanych w `math.h`.
# # Funkcje
# # # `uint32_t stdext::adler32(...)`

Implementuje algorytm sumy kontrolnej Adler-32, kt�ry jest szybszy, ale mniej niezawodny niz CRC32.
# # # `long stdext::random_range(long min, long max)`

Generuje losowa liczbe calkowita z podanego zakresu (wlacznie). Uzywa generatora Mersenne Twister (`std::mt19937`) zasilanego przez `std::random_device`, co zapewnia wysoka jakosc losowosci.
# # # `float stdext::random_range(float min, float max)`

Generuje losowa liczbe zmiennoprzecinkowa z podanego zakresu.
# # # `double stdext::round(double r)`

Implementuje zaokraglanie matematyczne (od .5 w g�re).
# # Zaleznosci i powiazania

-   `framework/stdext/math.h`: Plik nagl�wkowy.
-   `<random>`: Do generowania liczb losowych.

---
# ?? math.h
# # Opis og�lny

Plik `math.h` deklaruje zestaw funkcji pomocniczych zwiazanych z matematyka, operacjami bitowymi i losowoscia.
# # Funkcje

-   **`is_power_of_two(v)`**: Sprawdza, czy liczba jest potega dw�jki.
-   **`to_power_of_two(v)`**: Zwraca najblizsza potege dw�jki, kt�ra jest wieksza lub r�wna `v`.
-   **`readULE16`, `readULE32`, `readULE64`**: Odczytuja liczby calkowite bez znaku w porzadku Little Endian z bufora.
-   **`writeULE16`, `writeULE32`, `writeULE64`**: Zapisuja liczby do bufora w porzadku Little Endian.
-   **`readSLE...`, `writeSLE...`**: Analogiczne funkcje dla liczb ze znakiem.
-   **`adler32(...)`**: Deklaracja funkcji sumy kontrolnej.
-   **`random_range(...)`**: Deklaracje funkcji do generowania liczb losowych.
-   **`round(...)`**: Deklaracja funkcji zaokraglajacej.
-   **`clamp(...)`**: Szablonowa funkcja ograniczajaca wartosc do podanego zakresu.
# # Zaleznosci i powiazania

-   Sa to podstawowe funkcje narzedziowe, uzywane w wielu miejscach, szczeg�lnie w obsludze sieci (odczyt/zapis pakiet�w) i grafice (operacje na potegach dw�jki dla tekstur).

---
# ?? net.h
# # Opis og�lny

Plik `net.h` deklaruje funkcje pomocnicze zwiazane z operacjami na adresach IP.
# # Namespace `stdext`
# # # Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `std::string ip_to_string(uint32 ip)` | Konwertuje 32-bitowy adres IP (w porzadku sieciowym) na jego reprezentacje tekstowa (np. "127.0.0.1"). |
| `uint32 string_to_ip(const std::string& string)` | Konwertuje adres IP w formacie tekstowym na jego 32-bitowa reprezentacje w porzadku sieciowym. |
| `std::vector<uint32> listSubnetAddresses(...)` | Generuje liste wszystkich adres�w IP w danej podsieci. |
# # Zaleznosci i powiazania

-   `stdext/types.h`.
-   Implementacja w `net.cpp` uzywa Boost.Asio do konwersji.
-   Funkcje te sa uzywane w logice sieciowej, np. do logowania adres�w IP.

---
# ?? packed_any.h
# # Opis og�lny

Plik `packed_any.h` deklaruje klase `stdext::packed_any`, kt�ra jest zoptymalizowana pod katem pamieci wersja `stdext::any`.
# # Klasa `packed_any`
# # # Opis semantyczny
`packed_any` dziala podobnie do `any`, ale wprowadza optymalizacje dla malych, trywialnych typ�w (takich jak `int`, `bool`, `enum`, wskazniki). Zamiast alokowac pamiec na stercie dla `holdera`, wartosci takich typ�w sa przechowywane bezposrednio w wskazniku `content` poprzez rzutowanie. Flaga `scalar` odr�znia te dwa tryby przechowywania. Zmniejsza to fragmentacje pamieci i narzut na alokacje dla czesto uzywanych, malych typ�w.
# # # Szablon `can_pack_in_any`

Szablon pomocniczy, kt�ry w czasie kompilacji okresla, czy dany typ `T` moze byc "spakowany" bezposrednio we wskazniku. Warunkiem jest, aby `sizeof(T)` byl mniejszy lub r�wny `sizeof(void*)` i aby typ byl trywialnie kopiowalny.
# # # Metody i pola

Sa analogiczne do `stdext::any`, z dodatkowym polem `scalar` do rozr�zniania trybu.
# # # Funkcja `packed_any_cast`

Posiada dwie specjalizacje: jedna dla typ�w "pakowalnych" (kt�ra rzutuje wskaznik z powrotem na wartosc) i druga dla typ�w nie-pakowalnych (kt�ra dziala jak `any_cast`).
# # Zaleznosci i powiazania

-   Jest uzywana w `packed_storage` jako mechanizm przechowywania wartosci.

---
# ?? shared_object.h
# # Opis og�lny

Plik `shared_object.h` zawiera implementacje wlasnego, intruzywnego inteligentnego wskaznika (`shared_object_ptr`) i powiazanej z nim klasy bazowej (`shared_object`).
# # Klasa `shared_object`
# # # Opis semantyczny
Jest to klasa bazowa, po kt�rej musza dziedziczyc wszystkie klasy, kt�re chca byc zarzadzane przez `shared_object_ptr`. Zawiera ona licznik referencji (`refs`) i metody do jego inkrementacji i dekrementacji. Jest to tzw. "intruzywny" wskaznik, poniewaz sam obiekt przechowuje sw�j licznik referencji.
# # # Metody

-   `add_ref()`: Inkrementuje licznik.
-   `dec_ref()`: Dekrementuje licznik. Jesli osiagnie 0, obiekt usuwa sam siebie (`delete this`).
-   `ref_count()`: Zwraca liczbe referencji.
-   `..._self_cast()`: Metody pomocnicze do bezpiecznego rzutowania `this` na `shared_object_ptr`.
# # Klasa `shared_object_ptr`
# # # Opis semantyczny
Jest to szablonowa klasa inteligentnego wskaznika, kt�ra nasladuje zachowanie `std::shared_ptr`, ale wsp�lpracuje z `shared_object`. Zarzadza czasem zycia obiektu, na kt�ry wskazuje, automatycznie wywolujac `add_ref` i `dec_ref`.
# # # Metody i operatory

Implementuje wszystkie standardowe operacje dla inteligentnych wskaznik�w: konstruktory, destruktor, operatory przypisania, dereferencji (`*`, `->`), por�wnania, a takze konwersje do `bool`.
# # # Funkcje pomocnicze

-   `get_pointer`, `static_pointer_cast`, `const_pointer_cast`, `dynamic_pointer_cast`, `make_shared_object`: Funkcje globalne nasladujace te znane z `<memory>`.
# # Zaleznosci i powiazania

-   Jest to fundamentalny element frameworka. Prawie wszystkie klasy, kt�re sa dynamicznie alokowane i przekazywane miedzy r�znymi czesciami systemu (szczeg�lnie do i z Lua), dziedzicza po `shared_object` i sa zarzadzane przez `shared_object_ptr`.

---
# ?? stdext.h
# # Opis og�lny

Plik `stdext.h` jest gl�wnym plikiem nagl�wkowym dla modulu `stdext` (standard extensions). Jego jedynym zadaniem jest dolaczenie wszystkich innych plik�w nagl�wkowych z tego modulu w jednym miejscu.
# # Zawartosc

Dolacza wszystkie pliki z `framework/stdext/`, w tym:
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
# # Zaleznosci i powiazania

-   Jest dolaczany przez `global.h`, co sprawia, ze wszystkie narzedzia z `stdext` sa dostepne w calym projekcie.

---
# ?? packed_storage.h
# # Opis og�lny

Plik `packed_storage.h` deklaruje klase szablonowa `packed_storage`, kt�ra jest kontenerem asocjacyjnym zoptymalizowanym pod katem minimalnego zuzycia pamieci.
# # Klasa `packed_storage`
# # # Opis semantyczny
`packed_storage` dziala jak mapa, ale zamiast zlozonych struktur drzewiastych lub tablic hashujacych, przechowuje swoje elementy w prostej, dynamicznie alokowanej tablicy par `(klucz, wartosc)`. Wartosci sa przechowywane w `packed_any`, co dodatkowo minimalizuje zuzycie pamieci. Jest to rozwiazanie kompromisowe: zuzywa bardzo malo pamieci, ale operacje wyszukiwania, dodawania i usuwania maja zlozonosc liniowa O(n). Jest odpowiednia dla malej liczby element�w.
# # # Metody publiczne

Sa analogiczne do `dynamic_storage`: `set`, `remove`, `get`, `has`, `clear`, `size`.
# # # Zmienne prywatne

-   `m_values`: Wskaznik na tablice `value_pair`.
-   `m_size`: Aktualna liczba element�w.
# # Zaleznosci i powiazania

-   `stdext/types.h`, `stdext/packed_any.h`.
-   Moze byc uzywana tam, gdzie liczy sie kazdy bajt pamieci, a liczba przechowywanych element�w jest niewielka.

---
# ?? thread.h
# # Opis og�lny

Plik `thread.h` jest prostym plikiem nagl�wkowym, kt�ry dolacza standardowe nagl�wki C++ zwiazane z wielowatkowoscia.
# # Zawartosc

```cpp
# include <thread>
# include <condition_variable>
# include <mutex>
```
# # Zaleznosci i powiazania

-   Sluzy jako centralny punkt dolaczania nagl�wk�w wielowatkowosci, co ulatwia zarzadzanie zaleznosciami.
-   Jest uzywany przez klasy takie jak `AsyncDispatcher`, `Logger`, `ProxyManager`.

---
# ?? time.h
# # Opis og�lny

Plik `time.h` deklaruje zestaw funkcji i klas do obslugi czasu, stanowiac opakowanie na `std::chrono`.
# # Namespace `stdext`
# # # Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `ticks_t time()` | Zwraca czas w sekundach od epoki (Unix timestamp). |
| `ticks_t millis()` | Zwraca czas w milisekundach od uruchomienia aplikacji. |
| `ticks_t micros()` | Zwraca czas w mikrosekundach od uruchomienia aplikacji. |
| `void millisleep(size_t ms)` | Usypia biezacy watek na `ms` milisekund. |
| `void microsleep(size_t us)` | Usypia biezacy watek na `us` mikrosekund. |
# # # Struktura `timer`

Prosta klasa-stoper, podobna do `Timer` z modulu `core`, ale dzialajaca na "rzeczywistym" czasie z `stdext::micros()`, a nie na buforowanym czasie z `g_clock`.
# # Zaleznosci i powiazania

-   `stdext/types.h`.
-   Implementacja w `time.cpp` uzywa `std::chrono` i `std::this_thread`.
-   Sa to niskopoziomowe funkcje czasowe, na kt�rych bazuje `Clock`.

---
# ?? traits.h
# # Opis og�lny

Plik `traits.h` zawiera szablony metaprogramowania (type traits), kt�re sa uzywane do manipulacji i analizy typ�w w czasie kompilacji.
# # Namespace `stdext`
# # # Szablony

-   **`replace_extent`**: Usuwa wymiar tablicy z typu i zastepuje go wskaznikiem. Np. `int[10]` staje sie `const int*`.
-   **`remove_const_ref`**: Metafunkcja, kt�ra z danego typu `T` usuwa kwalifikatory `const` oraz referencje, zwracajac "czysty" typ. Np. `const std::string&` staje sie `std::string`.
# # Zaleznosci i powiazania

-   `<type_traits>`: Standardowy nagl�wek C++.
-   Sa to zaawansowane narzedzia metaprogramowania, uzywane gl�wnie w `luabinder.h` do analizy sygnatur funkcji i w `format.h` do obslugi argument�w.

---
# ?? string.h
# # Opis og�lny

Plik `string.h` deklaruje zestaw funkcji pomocniczych do manipulacji i konwersji ciag�w znak�w (`std::string`).
# # Namespace `stdext`
# # # Funkcje

| Funkcja | Opis |
| :--- | :--- |
| `to_string<T>(...)` / `from_string<T>(...)` | Skr�ty do `unsafe_cast` dla konwersji z/do stringa. |
| `resolve_path(...)` | Laczy sciezke do pliku ze sciezka zr�dlowa. |
| `date_time_string()` | Zwraca sformatowana date i czas. |
| `dec_to_hex(...)` / `hex_to_dec(...)` | Konwersje miedzy systemem dziesietnym a szesnastkowym. |
| `tolower(...)`, `toupper(...)`, `trim(...)`, `ucwords(...)` | Standardowe operacje na stringach. |
| `ends_with(...)`, `starts_with(...)`, `replace_all(...)` | Operacje wyszukiwania i zamiany. |
| `is_valid_utf8(...)` | Sprawdza, czy string jest poprawnym ciagiem UTF-8. |
| `utf8_to_latin1(...)`, `latin1_to_utf8(...)` | Konwersje kodowania znak�w. |
| `utf8_to_utf16(...)`, `utf16_to_utf8(...)` | (Windows) Konwersje do/z UTF-16 (`std::wstring`). |
| `split(...)` | Dzieli string na wektor string�w na podstawie separator�w. |
# # Zaleznosci i powiazania

-   `stdext/types.h`, `cast.h`.
-   Implementacja w `string.cpp` uzywa biblioteki Boost.StringAlgo do niekt�rych operacji.
-   Sa to podstawowe funkcje narzedziowe uzywane w calym projekcie.

---
# ?? time.cpp
# # Opis og�lny

Plik `time.cpp` zawiera implementacje funkcji czasowych zadeklarowanych w `time.h`.
# # Namespace `stdext`
# # # `startup_time`

Statyczna zmienna, kt�ra przechowuje czas uruchomienia aplikacji. Jest uzywana jako punkt odniesienia dla `millis()` i `micros()`.

```cpp
const static auto startup_time = std::chrono::high_resolution_clock::now();
```
# # # Implementacje funkcji

-   **`time()`**: Uzywa `std::time(NULL)`.
-   **`millis()`**, **`micros()`**: Obliczaja r�znice miedzy biezacym czasem a `startup_time` za pomoca `std::chrono` i konwertuja wynik na odpowiednia jednostke.
-   **`millisleep()`**, **`microsleep()`**: Uzywaja `std::this_thread::sleep_for`.
# # Zaleznosci i powiazania

-   `stdext/time.h`: Plik nagl�wkowy.
-   `<chrono>`, `<ctime>`, `<thread>`: Standardowe biblioteki C++.

---
# ?? uri.h
# # Opis og�lny

Plik `uri.h` deklaruje strukture `ParsedURI` oraz funkcje do parsowania adres�w URL.
# # Struktura `ParsedURI`

Przechowuje rozbity na czesci adres URL.

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `protocol` | `std::string` | Protok�l (np. "http", "wss"). |
| `domain` | `std::string` | Domena (np. "example.com"). |
| `port` | `std::string` | Port. |
| `query` | `std::string` | Sciezka i zapytanie (np. "/path?a=1"). |
# # Funkcja `parseURI`
# # # `ParsedURI parseURI(const std::string& url)`

Parsuje podany URL i zwraca strukture `ParsedURI` z jego komponentami.
# # Zaleznosci i powiazania

-   Jest uzywana przez `HttpSession` i `WebsocketSession` do analizy podanego adresu URL.

---
# ?? net.cpp
# # Opis og�lny

Plik `net.cpp` zawiera implementacje funkcji pomocniczych do operacji na adresach IP, zadeklarowanych w `net.h`.
# # Namespace `stdext`
# # # `std::string ip_to_string(uint32 ip)`

Konwertuje 32-bitowy adres IP z porzadku sieciowego na porzadek hosta, a nastepnie na `std::string` za pomoca `boost::asio::ip::address_v4`.
# # # `uint32 string_to_ip(const std::string& string)`

Konwertuje `std::string` na obiekt `address_v4`, a nastepnie na 32-bitowa liczbe w porzadku sieciowym.
# # # `std::vector<uint32> listSubnetAddresses(uint32 address, uint8 mask)`

Generuje liste wszystkich adres�w IP w podanej podsieci. Oblicza maske bitowa i iteruje po wszystkich mozliwych adresach w zakresie, dodajac je do listy.
# # Zaleznosci i powiazania

-   `framework/stdext/net.h`: Plik nagl�wkowy.
-   `boost/asio`: Uzywana do konwersji adres�w IP.
-   Sa to funkcje narzedziowe uzywane w logice sieciowej.

---
# ?? uri.cpp
# # Opis og�lny

Plik `uri.cpp` zawiera implementacje funkcji `parseURI` do parsowania adres�w URL.
# # Funkcja `parseURI`
# # # `ParsedURI parseURI(const std::string& url)`

Uzywa wyrazenia regularnego (`std::regex`) do rozbicia adresu URL na jego komponenty: protok�l, domene, port i sciezke/zapytanie. Obsluguje protokoly "http", "https", "ws", "wss" i poprawnie ustawia domyslne porty (80 dla http/ws, 443 dla https/wss).
# # Zaleznosci i powiazania

-   `framework/stdext/uri.h`: Plik nagl�wkowy.
-   `<regex>`: Do parsowania.
-   `boost/algorithm/string.hpp`: Do konwersji na male litery.
-   Jest uzywana przez `HttpSession` i `WebsocketSession`.

---
# ?? types.h
# # Opis og�lny

Plik `types.h` definiuje zestaw alias�w dla typ�w calkowitoliczbowych o stalym rozmiarze oraz inne podstawowe typy uzywane w calym frameworku.
# # Definicje typ�w

-   **Skr�ty**: `uchar`, `ushort`, `uint`, `ulong`.
-   **Liczby o stalym rozmiarze**: `uint64`, `uint32`, `uint16`, `uint8` oraz ich wersje ze znakiem (`int...`).
-   **`ticks_t`**: Alias dla `int64`, uzywany do przechowywania czasu w milisekundach lub mikrosekundach.
-   **`refcount_t`**: Typ dla licznika referencji.
-   **`size_t`, `ptrdiff_t`**: Importuje typy ze `std`.
# # Zaleznosci i powiazania

-   `<cstdint>`, `<cstddef>`: Standardowe nagl�wki.
-   Jest to fundamentalny plik, dolaczany przez `stdext.h` i `global.h`, zapewniajacy sp�jne i przenosne typy danych w calym projekcie.

---
# ?? format.h
# # Opis og�lny

Plik `format.h` zawiera implementacje funkcji `stdext::format`, kt�ra jest bezpieczna typowo alternatywa dla `sprintf`, podobna do `boost::format` lub `fmt::format`.
# # Funkcje
# # # `stdext::print(...)`

Funkcja debugujaca, kt�ra wypisuje na konsole dowolna liczbe argument�w, oddzielajac je tabulatorami, podobnie jak `print` w Lua.
# # # `stdext::snprintf(...)`

Opakowanie na `snprintf` / `_snprintf`, kt�re potrafi obslugiwac typy niestandardowe, takie jak `std::string`, poprzez `sprintf_cast`.
# # # `stdext::format(...)`

Gl�wna funkcja.
-   **Dzialanie**:
    1.  Wywoluje `snprintf` z `NULL` jako buforem, aby obliczyc wymagana dlugosc wynikowego stringa.
    2.  Alokuje `std::string` o odpowiednim rozmiarze.
    3.  Wywoluje `snprintf` ponownie, tym razem zapisujac wynik do bufora stringa.
-   **Zalety**: Jest w pelni bezpieczna (brak przepelnienia bufora) i obsluguje r�zne typy danych.
# # Zaleznosci i powiazania

-   `stdext/traits.h`: Do analizy typ�w.
-   `<tuple>`, `<sstream>`: Do metaprogramowania i formatowania.
-   Jest to kluczowe narzedzie uzywane w calym projekcie do formatowania string�w, szczeg�lnie w logach i komunikatach o bledach.

---
# ?? string.cpp
# # Opis og�lny

Plik `string.cpp` zawiera implementacje funkcji pomocniczych do manipulacji stringami, zadeklarowanych w `string.h`.
# # Funkcje

-   **`resolve_path(...)`**: Implementuje logike laczenia sciezek, obslugujac sciezki absolutne i wzgledne.
-   **`date_time_string()`, `timestamp_to_date(...)`**: Uzywaja `std::localtime` i `std::strftime` do formatowania daty i czasu.
-   **`dec_to_hex(...)`, `hex_to_dec(...)`**: Uzywaja `std::stringstream` do konwersji.
-   **Konwersje kodowania**: `is_valid_utf8` implementuje walidacje bajt po bajcie. `utf8_to_latin1` i `latin1_to_utf8` implementuja uproszczona konwersje. Wersje dla Windows (`..._to_utf16`) uzywaja funkcji WinAPI `MultiByteToWideChar` i `WideCharToMultiByte`.
-   **Inne operacje**: `tolower`, `toupper`, `trim`, `ends_with`, `starts_with`, `replace_all`, `split` sa opakowaniami na odpowiednie funkcje z biblioteki Boost.StringAlgo.
# # Zaleznosci i powiazania

-   `framework/stdext/string.h`, `format.h`.
-   `boost/algorithm/string.hpp`: Kluczowa zaleznosc dla wielu operacji.
-   `physfs.h`: Potencjalnie, choc nie jest bezposrednio uzywany.
-   Nagl�wki WinAPI (dla konwersji kodowania).

---
# ?? declarations.h
# # Opis og�lny

Plik `declarations.h` w module `ui` jest plikiem nagl�wkowym do wczesnych deklaracji (forward declarations) i definicji typ�w dla klas interfejsu uzytkownika.
# # Wczesne deklaracje

-   `UIManager`
-   `UIWidget`
-   `UITextEdit`
-   `UILayout` i wszystkie jego podklasy (`UIBoxLayout`, `UIGridLayout`, etc.)
-   `UIAnchor`, `UIAnchorGroup`, `UIAnchorLayout`
# # Definicje typ�w

-   `UIWidgetPtr`, `UITextEditPtr`, `UILayoutPtr`, ...: Aliasy dla `shared_object_ptr` do klas UI.
-   `UIWidgetList`: Alias dla `std::deque<UIWidgetPtr>`.
-   `UIAnchorList`: Alias dla `std::vector<UIAnchorPtr>`.
# # Zaleznosci i powiazania

-   `framework/global.h`: Podstawowe definicje.
-   Jest dolaczany przez wszystkie pliki nagl�wkowe w module `ui`.

---
# ?? ui.h
# # Opis og�lny

Plik `ui.h` jest gl�wnym, zbiorczym plikiem nagl�wkowym dla modulu UI. Jego zadaniem jest dolaczenie wszystkich najwazniejszych nagl�wk�w zwiazanych z interfejsem uzytkownika w jednym miejscu.
# # Zawartosc

Dolacza wszystkie podstawowe komponenty UI:
-   `uimanager.h`
-   `uiwidget.h`
-   `uitextedit.h`
-   `uilayout.h` i jego pochodne (`uihorizontallayout.h`, `uiverticallayout.h`, `uigridlayout.h`, `uianchorlayout.h`).
# # Zaleznosci i powiazania

-   Ulatwia dolaczanie calego podsystemu UI w innych czesciach projektu, kt�re go potrzebuja (np. w plikach modul�w gry).

---
# ?? uiboxlayout.cpp
# # Opis og�lny

Plik `uiboxlayout.cpp` zawiera implementacje klasy `UIBoxLayout`, kt�ra jest abstrakcyjna klasa bazowa dla layout�w ukladajacych widgety w jednej linii (poziomo lub pionowo).
# # Klasa `UIBoxLayout`
# # # `UIBoxLayout::UIBoxLayout(UIWidgetPtr parentWidget)`

Konstruktor. Wywoluje konstruktor `UILayout` i inicjalizuje `m_spacing` na 0.
# # # `void UIBoxLayout::applyStyle(const OTMLNodePtr& styleNode)`

Parsuje atrybuty specyficzne dla `UIBoxLayout` z wezla OTML.
-   `spacing`: Odstep miedzy widgetami.
-   `fit-children`: Flaga okreslajaca, czy layout powinien dostosowac rozmiar rodzica do sumarycznego rozmiaru dzieci.
# # # `addWidget` i `removeWidget`

Te metody po prostu wywoluja `update()`, poniewaz kazda zmiana w liczbie dzieci wymaga ponownego przeliczenia layoutu.
# # Zaleznosci i powiazania

-   `framework/ui/uiboxlayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   Jest klasa bazowa dla `UIHorizontalLayout` i `UIVerticalLayout`.

---
# ?? uiboxlayout.h
# # Opis og�lny

Plik `uiboxlayout.h` deklaruje klase `UIBoxLayout`, kt�ra jest abstrakcyjna klasa bazowa dla layout�w liniowych.
# # Klasa `UIBoxLayout`
# # # Opis semantyczny
`UIBoxLayout` dziedziczy po `UILayout` i dodaje wsp�lna funkcjonalnosc dla layout�w horyzontalnych i wertykalnych, a mianowicie:
-   `spacing`: Odstep miedzy kolejnymi elementami.
-   `fit-children`: Mozliwosc automatycznego dostosowania rozmiaru widgetu-rodzica, aby zmiescil wszystkie swoje dzieci.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setSpacing(int spacing)` | Ustawia odstep miedzy widgetami. |
| `setFitChildren(bool fitParent)` | Wlacza/wylacza dopasowywanie rozmiaru rodzica. |
# # # Zmienne chronione

-   `m_fitChildren`: Flaga `fit-children`.
-   `m_spacing`: Wartosc odstepu.
# # Zaleznosci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Jest klasa bazowa dla `UIHorizontalLayout` i `UIVerticalLayout`.
-   Oznaczona jako `@bindclass`, jej metody sa dostepne w Lua.

---
# ?? uigridlayout.cpp
# # Opis og�lny

Plik `uigridlayout.cpp` zawiera implementacje klasy `UIGridLayout`, kt�ra uklada widgety w siatce o stalym rozmiarze kom�rek.
# # Klasa `UIGridLayout`
# # # `UIGridLayout::UIGridLayout(...)`

Konstruktor, ustawia domyslne wartosci (rozmiar kom�rki 16x16, 1 kolumna).
# # # `void UIGridLayout::applyStyle(...)`

Parsuje atrybuty specyficzne dla siatki z wezla OTML, takie jak `cell-size`, `cell-spacing`, `num-columns`, `flow`.
# # # `bool UIGridLayout::internalUpdate()`
# # # # Opis semantyczny
Gl�wna metoda przeliczajaca pozycje widget�w w siatce.
# # # # Dzialanie
1.  Pobiera liste dzieci od rodzica.
2.  **Tryb `flow`**: Jesli wlaczony, dynamicznie oblicza liczbe kolumn (`numColumns`), tak aby zmiescily sie w szerokosci rodzica. Na podstawie tego oblicza liczbe wierszy.
3.  **Tryb `auto-spacing`**: Jesli wlaczony, dynamicznie oblicza odstep miedzy kom�rkami (`cellSpacing`), aby r�wnomiernie rozlozyc je na calej szerokosci rodzica.
4.  W petli przechodzi przez wszystkie widoczne widgety:
    -   Oblicza wiersz i kolumne dla biezacego widgetu.
    -   Na tej podstawie oblicza jego pozycje.
    -   Ustawia docelowy prostokat (`Rect`) widgetu na rozmiar kom�rki w obliczonej pozycji.
5.  **Tryb `fit-children`**: Jesli wlaczony, oblicza wymagana wysokosc rodzica, aby zmiescic wszystkie wiersze, i planuje jej ustawienie w `EventDispatcher` (aby uniknac problem�w z rekurencyjnymi aktualizacjami).
# # Zaleznosci i powiazania

-   `framework/ui/uigridlayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokosci rodzica.

---
# ?? uigridlayout.h
# # Opis og�lny

Plik `uigridlayout.h` deklaruje klase `UIGridLayout`, kt�ra implementuje layout siatkowy.
# # Klasa `UIGridLayout`
# # # Opis semantyczny
`UIGridLayout` uklada swoje widgety w regularnej siatce. Moze miec stala liczbe kolumn lub dynamicznie dostosowywac ja do dostepnej przestrzeni (`flow`). Posiada r�wniez opcje automatycznego dostosowywania odstep�w i rozmiaru rodzica.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setCellSize(...)` | Ustawia rozmiar pojedynczej kom�rki siatki. |
| `setCellSpacing(...)` | Ustawia odstep miedzy kom�rkami. |
| `setNumColumns(...)` | Ustawia stala liczbe kolumn. |
| `setNumLines(...)` | Ustawia maksymalna liczbe wierszy. |
| `setFlow(bool enable)` | Wlacza/wylacza tryb "plynny", w kt�rym liczba kolumn jest dynamiczna. |
| `setAutoSpacing(bool enable)`| Wlacza/wylacza automatyczne obliczanie odstep�w. |
| `setFitChildren(bool enable)`| Wlacza/wylacza dopasowywanie wysokosci rodzica. |
# # # Zmienne prywatne

-   `m_cellSize`: Rozmiar kom�rki.
-   `m_cellSpacing`: Odstep miedzy kom�rkami.
-   `m_numColumns`, `m_numLines`: Liczba kolumn i wierszy.
-   `m_autoSpacing`, `m_fitChildren`, `m_flow`: Flagi tryb�w.
# # Zaleznosci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# ?? uihorizontallayout.cpp
# # Opis og�lny

Plik `uihorizontallayout.cpp` zawiera implementacje klasy `UIHorizontalLayout`, kt�ra uklada widgety w jednym rzedzie, od lewej do prawej lub od prawej do lewej.
# # Klasa `UIHorizontalLayout`
# # # `void UIHorizontalLayout::applyStyle(...)`

Parsuje atrybut `align-right` z wezla OTML.
# # # `bool UIHorizontalLayout::internalUpdate()`
# # # # Opis semantyczny
Gl�wna metoda przeliczajaca pozycje widget�w.
# # # # Dzialanie
1.  Pobiera liste dzieci. Jesli `m_alignRight` jest `true`, odwraca kolejnosc listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycje `x` na podstawie pozycji i szerokosci poprzedniego widgetu oraz odstep�w (`spacing`, `margin`).
    -   Oblicza pozycje `y` w zaleznosci od wyr�wnania pionowego widgetu (`AlignTop`, `AlignBottom`, `AlignCenter`) wewnatrz wysokosci rodzica.
    -   Jesli widget nie ma stalego rozmiaru, jego wysokosc jest rozciagana do wysokosci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumaryczna, preferowana szerokosc (`preferredWidth`).
4.  Jesli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie szerokosci rodzica na `preferredWidth`.
# # Zaleznosci i powiazania

-   `framework/ui/uihorizontallayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania szerokosci rodzica.

---
# ?? uihorizontallayout.h
# # Opis og�lny

Plik `uihorizontallayout.h` deklaruje klase `UIHorizontalLayout`, kt�ra implementuje layout horyzontalny.
# # Klasa `UIHorizontalLayout`
# # # Opis semantyczny
`UIHorizontalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukladania widget�w w pojedynczym rzedzie. Moze ukladac elementy od lewej do prawej (domyslnie) lub od prawej do lewej (`align-right`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignRight(bool alignRight)` | Wlacza/wylacza ukladanie od prawej do lewej. |
# # # Zmienne chronione

-   `m_alignRight`: Flaga trybu wyr�wnania do prawej.
# # Zaleznosci i powiazania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# ?? uilayout.cpp
# # Opis og�lny

Plik `uilayout.cpp` zawiera implementacje klasy `UILayout`, kt�ra jest abstrakcyjna klasa bazowa dla wszystkich menedzer�w layoutu.
# # Klasa `UILayout`
# # # `void UILayout::update()`
# # # # Opis semantyczny
Gl�wna metoda publiczna inicjujaca aktualizacje layoutu.
# # # # Dzialanie
1.  Sprawdza, czy aktualizacje nie sa wylaczone (`m_updateDisabled`).
2.  Sprawdza, czy aktualizacja nie jest juz w toku (`m_updating`), aby zapobiec rekurencji. Jesli tak, planuje aktualizacje na p�zniej (`updateLater()`).
3.  Ustawia flage `m_updating` na `true`.
4.  Wywoluje wirtualna metode `internalUpdate()`, gdzie klasy pochodne implementuja swoja logike.
5.  Wywoluje `callback` `onLayoutUpdate` na widzecie-rodzicu.
6.  Resetuje flage `m_updating`.
# # # `void UILayout::updateLater()`

Planuje wykonanie `update()` w nastepnej iteracji petli `EventDispatcher`. Jest to mechanizm zapobiegajacy wielokrotnym, zbednym przeliczeniom layoutu w tej samej klatce.
# # Zaleznosci i powiazania

-   `framework/ui/uilayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Kazdy layout jest powiazany z widgetem-rodzicem.
-   `framework/core/eventdispatcher.h`: Do planowania op�znionych aktualizacji.

---
# ?? uilayout.h
# # Opis og�lny

Plik `uilayout.h` deklaruje abstrakcyjna klase bazowa `UILayout`, kt�ra definiuje wsp�lny interfejs dla wszystkich klas zarzadzajacych pozycja i rozmiarem widget�w-dzieci.
# # Klasa `UILayout`
# # # Opis semantyczny
`UILayout` jest powiazany z jednym widgetem-rodzicem (`m_parentWidget`). Jego zadaniem jest automatyczne zarzadzanie geometria dzieci tego widgetu. Kazda podklasa (`UIAnchorLayout`, `UIBoxLayout` itd.) implementuje inny algorytm ukladania element�w. Posiada mechanizmy do wlaczania/wylaczania aktualizacji oraz do unikania rekurencyjnych i zbednych przeliczen.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `UILayout(UIWidgetPtr parentWidget)`| Konstruktor. |
| `void update()` | Natychmiast zada przeliczenia layoutu. |
| `void updateLater()` | Planuje przeliczenie layoutu w najblizszej przyszlosci. |
| `virtual void applyStyle(...)` | Stosuje wlasciwosci layoutu z wezla OTML. |
| `virtual void addWidget(...)` | Powiadamia layout o dodaniu nowego widgetu. |
| `virtual void removeWidget(...)` | Powiadamia layout o usunieciu widgetu. |
| `void disableUpdates()` / `enableUpdates()`| Tymczasowo wstrzymuje/wznawia aktualizacje layoutu. |
| `void setParent(...)` / `getParentWidget()` | Zarzadza powiazaniem z widgetem-rodzicem. |
| `bool isUpdating()` | Zwraca `true`, jesli layout jest w trakcie aktualizacji. |
| `isUI...Layout()` | Metody RTTI (Run-Time Type Information) do identyfikacji typu layoutu. |
# # # Zmienne chronione

-   `m_updateDisabled`: Licznik blokad aktualizacji.
-   `m_updating`, `m_updateScheduled`: Flagi zapobiegajace rekurencji i wielokrotnym aktualizacjom.
-   `m_parentWidget`: Wskaznik do widgetu, kt�rego dziecmi zarzadza layout.
# # Zaleznosci i powiazania

-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   `framework/otml/otml.h`: Do parsowania styl�w.
-   Jest klasa bazowa dla wszystkich konkretnych implementacji layout�w.
-   Kazdy `UIWidget` moze miec jeden `UILayout`.

---
# ?? uimanager.h
# # Opis og�lny

Plik `uimanager.h` deklaruje klase `UIManager`, kt�ra jest singletonem (`g_ui`) i centralnym punktem zarzadzania calym interfejsem uzytkownika.
# # Klasa `UIManager`
# # # Opis semantyczny
`UIManager` zarzadza hierarchia widget�w, poczynajac od korzenia (`m_rootWidget`). Odpowiada za propagacje zdarzen wejsciowych (mysz, klawiatura), renderowanie, zarzadzanie stylami OTML oraz sledzenie globalnych stan�w UI, takich jak aktualnie wcisniety, najechany czy przeciagany widget.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia menedzera. |
| `void render(Fw::DrawPane)`| Rozpoczyna proces renderowania UI dla danej warstwy. |
| `void resize(const Size&)` | Aktualizuje rozmiar `m_rootWidget`. |
| `void inputEvent(...)` | Gl�wny punkt wejscia dla wszystkich zdarzen wejsciowych. |
| `void clearStyles()` | Czysci zaladowane style. |
| `bool importStyle(...)` | Laduje style z pliku `.otui`. |
| `OTMLNodePtr getStyle(...)` | Zwraca definicje stylu o podanej nazwie. |
| `UIWidgetPtr loadUI(...)` | Laduje i tworzy hierarchie widget�w z pliku `.otui`. |
| `UIWidgetPtr createWidget(...)` | Tworzy widget na podstawie nazwy stylu. |
| `setMouseReceiver(...)` / `setKeyboardReceiver(...)` | Ustawia widget, kt�ry "przechwytuje" zdarzenia myszy/klawiatury. |
| `get...Widget()` | Zwracaja wskazniki na widgety w okreslonych stanach (przeciagany, najechany, wcisniety). |
# # # Metody chronione (wywolywane przez `UIWidget`)

-   `onWidgetAppear(...)`, `onWidgetDisappear(...)`, `onWidgetDestroy(...)`: Callbacki informujace menedzera o zmianach w drzewie widget�w, co pozwala na aktualizacje globalnych stan�w (np. `m_hoveredWidget`).
# # # Zmienne prywatne

-   `m_rootWidget`: Korzen drzewa widget�w, wypelnia cale okno.
-   `m_mouseReceiver`, `m_keyboardReceiver`: Widgety przechwytujace zdarzenia.
-   `m_draggingWidget`, `m_hoveredWidget`, `m_pressedWidget`: Sledza globalne stany myszy.
-   `m_styles`: Mapa przechowujaca wszystkie zaladowane style.
-   `m_destroyedWidgets`: Lista do sledzenia niszczonych widget�w w celach debugowania wyciek�w pamieci.
# # # Zmienne globalne

-   `g_ui`: Globalna instancja `UIManager`.
# # Zaleznosci i powiazania

-   `framework/ui/declarations.h`, `uiwidget.h`.
-   `framework/core/inputevent.h`.
-   Scisle wsp�lpracuje z `GraphicalApplication` (kt�ra przekazuje jej zdarzenia) i `PlatformWindow`.
-   Zarzadza cyklem zycia i interakcjami wszystkich `UIWidget`.

---
# ?? uitextedit.cpp
# # Opis og�lny

Plik `uitextedit.cpp` zawiera implementacje klasy `UITextEdit`, kt�ra jest specjalizowanym widgetem do wprowadzania i edycji tekstu.
# # Klasa `UITextEdit`
# # # `UITextEdit::UITextEdit()`

Konstruktor. Inicjalizuje wszystkie pola zwiazane z edycja tekstu do wartosci domyslnych (np. kursor na pozycji 0, widoczny, tekst edytowalny).
# # # `void UITextEdit::drawSelf(...)`

Przeslonieta metoda rysujaca.
1.  Rysuje tlo, ramke, obraz i ikone (dziedziczone z `UIWidget`).
2.  Jesli tekst jest pusty, rysuje `placeholder`.
3.  Rysuje tekst, uzywajac `CoordsBuffer` (`m_glyphsTextCoordsBuffer`) do zbuforowania geometrii.
4.  Rysuje zaznaczenie, najpierw rysujac tlo zaznaczenia, a potem tekst w innym kolorze na wierzchu.
5.  Rysuje migajacy kursor w odpowiedniej pozycji.
# # # `void UITextEdit::update(bool focusCursor)`

Kluczowa metoda, kt�ra przelicza cala geometrie tekstu.
1.  Pobiera tekst do wyswietlenia (zwykly lub ukryty `*`).
2.  Zawija tekst, jesli `m_textWrap` jest wlaczone.
3.  Oblicza pozycje wszystkich glif�w za pomoca `m_font->calculateGlyphsPositions`.
4.  Jesli `m_autoScroll` i `focusCursor` sa `true`, automatycznie przewija widok, tak aby kursor byl zawsze widoczny.
5.  Przelicza, kt�re glify sa widoczne w obszarze widgetu, i generuje dla nich wsp�lrzedne w `m_glyphsCoords`.
# # # Metody edycji tekstu

-   `setCursorPos`, `setSelection`, `clearSelection`, `selectAll`: Zarzadzaja pozycja kursora i zaznaczeniem.
-   `appendText`, `appendCharacter`, `removeCharacter`: Modyfikuja tekst.
-   `del`, `paste`, `copy`, `cut`: Implementuja standardowe operacje edycyjne.
# # # `int UITextEdit::getTextPos(Point pos)`

Konwertuje pozycje myszy (w pikselach) na indeks znaku w tekscie.
# # # Obsluga zdarzen (`on...`)

Przeslania metody obslugi zdarzen z `UIWidget`, aby zaimplementowac logike edycji tekstu:
-   `onKeyPress`: Obsluguje nawigacje (strzalki, Home, End), usuwanie (Delete, Backspace), zaznaczanie (Shift + strzalki), kopiowanie/wklejanie (Ctrl+C/V).
-   `onKeyText`: Wstawia wprowadzony tekst.
-   `onMousePress`, `onMouseMove`, `onDoubleClick`: Obsluguja ustawianie kursora i zaznaczanie tekstu mysza.
# # Zaleznosci i powiazania

-   `framework/ui/uitextedit.h`: Plik nagl�wkowy.
-   `framework/graphics/bitmapfont.h`: Intensywnie uzywa `Bitmapfont` do obliczen.
-   `framework/platform/platformwindow.h`: Do interakcji ze schowkiem.
-   Na Androidzie, zamiast wlasnego renderowania, wywoluje natywne pole edycji tekstu.

---
# ?? uimanager.cpp
# # Opis og�lny

Plik `uimanager.cpp` zawiera implementacje klasy `UIManager`, kt�ra jest centralnym menedzerem interfejsu uzytkownika.
# # Klasa `UIManager`
# # # `void UIManager::init()`

Inicjalizuje menedzera, tworzac gl�wny, niewidoczny widget (`m_rootWidget`), kt�ry jest korzeniem calego drzewa UI i zajmuje cala powierzchnie okna.
# # # `void UIManager::render(Fw::DrawPane drawPane)`

Rozpoczyna proces renderowania, wywolujac metode `draw()` na `m_rootWidget` dla okreslonej warstwy rysowania.
# # # `void UIManager::resize(const Size& size)`

Aktualizuje rozmiar `m_rootWidget`, co powoduje rekurencyjne przeliczenie layoutu dla wszystkich widget�w potomnych.
# # # `void UIManager::inputEvent(const InputEvent& event)`
# # # # Opis semantyczny
Gl�wny punkt wejscia dla wszystkich zdarzen wejsciowych. Tlumaczy surowe zdarzenia na akcje w UI.
# # # # Dzialanie
-   Dla zdarzen klawiatury, przekazuje je do `m_keyboardReceiver`.
-   Dla wcisniecia przycisku myszy:
    1.  Identyfikuje widget pod kursorem.
    2.  Aktualizuje `m_pressedWidget`.
    3.  Propaguje zdarzenie `onMousePress` w d�l drzewa.
-   Dla zwolnienia przycisku myszy:
    1.  Jesli trwalo przeciaganie, konczy je i obsluguje "upuszczenie".
    2.  Propaguje zdarzenie `onMouseRelease`.
    3.  Jesli zwolnienie nastapilo nad pierwotnie wcisnietym widgetem, generuje zdarzenie `onClick`.
-   Dla ruchu myszy:
    1.  Aktualizuje `m_hoveredWidget`.
    2.  Jesli jakis widget jest wcisniety i przeciagalny, rozpoczyna przeciaganie.
    3.  Propaguje zdarzenie `onMouseMove`.
-   Dla k�lka myszy, propaguje zdarzenie.
# # # `void UIManager::update...Widget(...)`

Metody te zarzadzaja globalnym stanem UI:
-   `updatePressedWidget`: Zmienia, kt�ry widget jest aktualnie wcisniety.
-   `updateDraggingWidget`: Rozpoczyna lub konczy przeciaganie widgetu.
-   `updateHoveredWidget`: Aktualizuje, nad kt�rym widgetem znajduje sie kursor.
# # # `bool UIManager::importStyle(...)`

Laduje i parsuje plik `.otui` ze stylami, dodajac je do `m_styles`.
# # # `UIWidgetPtr UIManager::loadUI(...)` i `createWidgetFromOTML(...)`

Implementuja logike tworzenia widget�w na podstawie plik�w i wezl�w OTML. `createWidgetFromOTML` jest kluczowa metoda, kt�ra:
1.  Znajduje styl bazowy.
2.  Laczy (merge) go ze stylem zdefiniowanym w pliku UI.
3.  Na podstawie atrybutu `__class`, wywoluje w Lua funkcje fabryczna (`create`) dla danego typu widgetu.
4.  Stosuje styl i rekurencyjnie tworzy dzieci.
# # # `void UIManager::onWidgetDestroy(...)`

Callback wywolywany przez `UIWidget`. Czysci wszystkie globalne referencje do niszczonego widgetu (np. `m_hoveredWidget`, `m_pressedWidget`). W trybie debugowania, planuje sprawdzenie, czy nie pozostaly zadne wiszace referencje do widgetu po jego zniszczeniu.
# # Zaleznosci i powiazania

-   Jest to centralna klasa UI, kt�ra laczy `PlatformWindow` (zr�dlo zdarzen) z `UIWidget` (odbiorcy zdarzen).
-   Zarzadza calym drzewem widget�w.
-   Wsp�lpracuje z `OTML` do parsowania styl�w i layout�w.

---
# ?? uitextedit.h
# # Opis og�lny

Plik `uitextedit.h` deklaruje klase `UITextEdit`, kt�ra jest widgetem sluzacym do wprowadzania i edycji tekstu przez uzytkownika.
# # Klasa `UITextEdit`
# # # Opis semantyczny
`UITextEdit` dziedziczy po `UIWidget` i rozszerza jego funkcjonalnosc o logike obslugi kursora, zaznaczania tekstu, wprowadzania z klawiatury, kopiowania/wklejania i zawijania wierszy. Jest to jeden z najbardziej zlozonych widget�w w podstawowym zestawie.
# # # Metody publiczne
# # # # Zarzadzanie tekstem i kursorem
-   `setCursorPos(...)`: Ustawia pozycje kursora.
-   `setSelection(...)`: Ustawia zaznaczenie.
-   `setTextHidden(...)`: Wlacza tryb "hasla" (wyswietla `*`).
-   `setMaxLength(...)`: Ustawia maksymalna dlugosc tekstu.
-   `appendText(...)`: Dodaje tekst w pozycji kursora.
-   `del()`, `paste()`, `copy()`, `cut()`: Standardowe operacje edycyjne.
-   `selectAll()`, `clearSelection()`: Zarzadzanie zaznaczeniem.
# # # # Konfiguracja
-   `setEditable(...)`: Wlacza/wylacza mozliwosc edycji.
-   `setMultiline(...)`: Wlacza/wylacza tryb wieloliniowy.
-   `setValidCharacters(...)`: Ogranicza dozwolone znaki.
-   `setPlaceholder(...)`: Ustawia tekst wyswietlany, gdy pole jest puste.
# # # # Gettery
-   `getCursorPos()`, `getSelection()`, `getTextPos(...)`, ...: Zwracaja informacje o stanie edytora.
# # # Zmienne prywatne

-   `m_cursorPos`: Pozycja kursora.
-   `m_selectionStart`, `m_selectionEnd`: Granice zaznaczenia.
-   `m_textHidden`, `m_multiline`, `m_editable`, ...: Flagi konfiguracyjne.
-   `m_glyphsCoords`, `m_glyphsTexCoords`: Wektory przechowujace geometrie renderowanego tekstu.
-   `m_glyphsTextCoordsBuffer`, `m_glyphsSelectCoordsBuffer`: Bufory `CoordsBuffer` dla tekstu i zaznaczenia.
-   `m_placeholder`, `m_placeholderColor`, ...: Wlasciwosci placeholdera.
# # Zaleznosci i powiazania

-   `framework/ui/uiwidget.h`: Klasa bazowa.
-   Jest oznaczona jako `@bindclass`, co udostepnia jej bogate API w Lua.
-   Jest jednym z podstawowych, predefiniowanych typ�w widget�w tworzonych przez `UIManager`.

---
# ?? uitranslator.cpp
# # Opis og�lny

Plik `uitranslator.cpp` zawiera implementacje funkcji, kt�re tlumacza tekstowe reprezentacje r�znych enum�w uzywanych w UI na ich faktyczne wartosci liczbowe.
# # Namespace `Fw`
# # # `Fw::AlignmentFlag Fw::translateAlignment(std::string aligment)`

Konwertuje string (np. "top-left", "center") na odpowiednia flage z `Fw::AlignmentFlag`. Uzywa `boost::to_lower` i `boost::erase_all` do normalizacji wejscia.
# # # `Fw::AnchorEdge Fw::translateAnchorEdge(std::string anchorEdge)`

Konwertuje string (np. "left", "horizontal-center") na odpowiednia wartosc z `Fw::AnchorEdge`.
# # # `Fw::WidgetState Fw::translateState(std::string state)`

Konwertuje string (np. "hover", "pressed") na odpowiednia flage z `Fw::WidgetState`.
# # # `Fw::AutoFocusPolicy Fw::translateAutoFocusPolicy(std::string policy)`

Konwertuje string (np. "first", "last") na odpowiednia wartosc z `Fw::AutoFocusPolicy`.
# # Zaleznosci i powiazania

-   `framework/ui/uitranslator.h`: Plik nagl�wkowy.
-   `boost/algorithm/string.hpp`: Do normalizacji string�w.
-   Funkcje te sa uzywane przez `UIWidget` i jego podklasy podczas parsowania styl�w z OTML, aby przekonwertowac wartosci tekstowe na enumy.

---
# ?? uitranslator.h
# # Opis og�lny

Plik `uitranslator.h` deklaruje zestaw funkcji pomocniczych do konwersji string�w na wartosci wyliczeniowe (enum) uzywane w systemie UI.
# # Namespace `Fw`
# # # Deklaracje funkcji

| Funkcja | Opis |
| :--- | :--- |
| `AlignmentFlag translateAlignment(...)`| Konwertuje string na `Fw::AlignmentFlag`. |
| `AnchorEdge translateAnchorEdge(...)` | Konwertuje string na `Fw::AnchorEdge`. |
| `WidgetState translateState(...)` | Konwertuje string na `Fw::WidgetState`. |
| `AutoFocusPolicy translateAutoFocusPolicy(...)`| Konwertuje string na `Fw::AutoFocusPolicy`. |
# # Zaleznosci i powiazania

-   `framework/const.h`: Definicje enum�w.
-   `<string>`: Do operacji na stringach.
-   Te funkcje sa kluczowe dla parsowania plik�w OTML, gdzie wlasciwosci takie jak wyr�wnanie sa zdefiniowane za pomoca sl�w kluczowych.

---
# ?? uiverticallayout.cpp
# # Opis og�lny

Plik `uiverticallayout.cpp` zawiera implementacje klasy `UIVerticalLayout`, kt�ra uklada widgety w jednej kolumnie, od g�ry do dolu lub od dolu do g�ry.
# # Klasa `UIVerticalLayout`
# # # `void UIVerticalLayout::applyStyle(...)`

Parsuje atrybut `align-bottom` z wezla OTML.
# # # `bool UIVerticalLayout::internalUpdate()`
# # # # Opis semantyczny
Gl�wna metoda przeliczajaca pozycje widget�w. Dziala analogicznie do `UIHorizontalLayout::internalUpdate`, ale operuje na osi Y.
# # # # Dzialanie
1.  Pobiera liste dzieci. Jesli `m_alignBottom` jest `true`, odwraca kolejnosc listy.
2.  Iteruje po widgetach:
    -   Oblicza pozycje `y` na podstawie pozycji i wysokosci poprzedniego widgetu oraz odstep�w.
    -   Oblicza pozycje `x` w zaleznosci od wyr�wnania poziomego widgetu (`AlignLeft`, `AlignRight`, `AlignCenter`) wewnatrz szerokosci rodzica.
    -   Jesli widget nie ma stalego rozmiaru, jego szerokosc jest rozciagana do szerokosci rodzica.
    -   Ustawia nowy `Rect` dla widgetu.
3.  Oblicza sumaryczna, preferowana wysokosc (`preferredHeight`).
4.  Jesli `m_fitChildren` jest `true`, planuje asynchroniczne ustawienie wysokosci rodzica na `preferredHeight`.
# # Zaleznosci i powiazania

-   `framework/ui/uiverticallayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.
-   `framework/core/eventdispatcher.h`: Do asynchronicznego ustawiania wysokosci rodzica.

---
# ?? uiverticallayout.h
# # Opis og�lny

Plik `uiverticallayout.h` deklaruje klase `UIVerticalLayout`, kt�ra implementuje layout wertykalny.
# # Klasa `UIVerticalLayout`
# # # Opis semantyczny
`UIVerticalLayout` dziedziczy po `UIBoxLayout` i specjalizuje go do ukladania widget�w w pojedynczej kolumnie. Moze ukladac elementy od g�ry do dolu (domyslnie) lub od dolu do g�ry (`align-bottom`).
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `setAlignBottom(bool alignBottom)` | Wlacza/wylacza ukladanie od dolu do g�ry. |
| `isAlignBottom()` | Zwraca stan flagi `align-bottom`. |
# # # Zmienne chronione

-   `m_alignBottom`: Flaga trybu wyr�wnania do dolu.
# # Zaleznosci i powiazania

-   `framework/ui/uiboxlayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.

---
# ?? uiwidget.cpp
# # Opis og�lny

Plik `uiwidget.cpp` jest gl�wnym plikiem implementacyjnym dla klasy `UIWidget`. Zawiera on logike dla podstawowych operacji na widgetach, takich jak zarzadzanie dziecmi, obsluga layout�w, zdarzen, stan�w i styl�w.
# # Klasa `UIWidget`
# # # `UIWidget::UIWidget()`

Konstruktor. Inicjalizuje wszystkie pola do wartosci domyslnych, w tym podstawowy styl, wlasciwosci tekstu i obrazu. Co wazne, zapisuje sciezke do skryptu Lua, w kt�rym widget zostal utworzony (`m_source`), co jest niezwykle przydatne do debugowania.
# # # `void UIWidget::draw(...)`

Gl�wna metoda renderujaca. Jest rekurencyjna.
1.  Wywoluje `drawSelf()` do narysowania samego widgetu.
2.  Jesli wlaczone jest przycinanie (`m_clipping`), ustawia odpowiedni `DrawQueueConditionClip`.
3.  Wywoluje `drawChildren()` do narysowania wszystkich widocznych dzieci.
4.  Stosuje globalne efekty dla widgetu i jego dzieci, takie jak przezroczystosc (`setOpacity`) i rotacja (`setRotation`), dodajac odpowiednie warunki do `DrawQueue`.
# # # `void UIWidget::addChild(...)`, `insertChild(...)`, `removeChild(...)`

Metody do zarzadzania hierarchia widget�w. Poza modyfikacja `m_children`, dbaja o:
-   Ustawienie/zresetowanie wskaznika `m_parent` w dziecku.
-   Dodanie/usuniecie widgetu z layoutu rodzica.
-   Aktualizacje stanu fokusu, jesli usuwane jest dziecko z fokusem.
-   Aktualizacje stan�w indeksowych (`FirstState`, `LastState`) u rodzenstwa.
-   Powiadomienie `UIManager` o pojawieniu sie/zniknieciu widgetu.
# # # `void UIWidget::focusChild(...)`, `focusNextChild(...)`, `focusPreviousChild(...)`

Implementuja logike zarzadzania fokusem wewnatrz widgetu. `focusChild` zmienia `m_focusedChild` i wywoluje callbacki `onFocusChange`. `focusNext/PreviousChild` implementuja nawigacje (np. klawiszem Tab).
# # # `void UIWidget::applyStyle(const OTMLNodePtr& styleNode)`

Aplikuje wlasciwosci z wezla stylu do widgetu. Wywoluje `onStyleApply` oraz `onStyleApply` w Lua.
# # # `void UIWidget::updateState(Fw::WidgetState state)`

Kluczowa metoda, kt�ra aktualizuje pojedyncza flage stanu (np. `HoverState`). Oblicza, czy widget powinien miec dany stan (np. dla `HoverState` sprawdza, czy `g_ui.getHoveredWidget() == this`), a nastepnie wywoluje `setState`.
# # # `void UIWidget::updateStates()`

Wywoluje `updateState` dla wszystkich mozliwych stan�w, synchronizujac pelny stan widgetu.
# # # `void UIWidget::updateStyle()`

Gdy stan widgetu sie zmienia, ta metoda jest wywolywana. Przebudowuje ona tymczasowy wezel stylu (`m_stateStyle`), laczac style z warunk�w (`$!hover`, `$checked`, itp.), a nastepnie wywoluje `applyStyle` z tym nowym, polaczonym stylem.
# # # Metody `on...` i `propagateOn...`

Implementuja domyslna obsluge i propagacje zdarzen w drzewie widget�w. Metody `propagate...` decyduja, do kt�rych dzieci przekazac zdarzenie, a nastepnie wywoluja metode `on...` na samym widgecie.
# # Zaleznosci i powiazania

-   Jest to centralna klasa modulu UI, kt�ra zalezy od prawie wszystkich innych jego czesci (`UIManager`, `UILayout`, `UITranslator`) oraz wielu modul�w frameworka (`Graphics`, `LuaInterface`, `EventDispatcher`, `OTML`).

---
# ?? uiwidget.h
# # Opis og�lny

Plik `uiwidget.h` deklaruje klase `UIWidget`, kt�ra jest fundamentalna klasa bazowa dla wszystkich element�w interfejsu uzytkownika.
# # Struktura `EdgeGroup`

Szablonowa struktura pomocnicza do przechowywania wartosci dla czterech krawedzi (g�ra, prawo, d�l, lewo), uzywana dla `margin`, `padding`, `border-width` i `border-color`.
# # Klasa `UIWidget`
# # # Opis semantyczny
`UIWidget` jest obiektowym odpowiednikiem elementu DOM. Reprezentuje prostokatny obszar na ekranie, kt�ry moze byc rysowany, reagowac na zdarzenia i zawierac inne widgety. Implementuje model drzewa (rodzic-dzieci), system zdarzen (propagacja i obsluga), system stan�w (aktywny, najechany, etc.), zarzadzanie layoutem oraz integracje z OTML i Lua.
# # # Podzial interfejsu (w pliku `.h`)

Interfejs klasy jest podzielony na sekcje tematyczne:
-   **Widget Core**: Podstawowe metody do zarzadzania hierarchia, layoutem, stylami i stanami.
-   **State Management**: Metody do zarzadzania stanami (`setState`, `hasState`).
-   **Event Processing**: Wirtualne metody `on...` do obslugi zdarzen.
-   **Function Shortcuts**: Wygodne metody opakowujace (`hide`, `show`, `enable`).
-   **Base Style**: Pola i metody zwiazane z podstawowymi wlasciwosciami wizualnymi (tlo, ramka, ikona, przezroczystosc).
-   **Image**: Pola i metody zwiazane z wyswietlaniem obrazu (`m_imageTexture`, `setImageSource`).
-   **Text**: Pola i metody zwiazane z wyswietlaniem tekstu (`m_text`, `m_font`, `setText`).
# # # Kluczowe wlasciwosci

-   **Hierarchia**: `m_parent`, `m_children`.
-   **Geometria**: `m_rect`.
-   **Styl**: `m_style` (wezel OTML), `m_states`.
-   **Layout**: `m_layout`.
-   **Zdarzenia**: Zestaw wirtualnych metod `on...` (np. `onMousePress`, `onKeyPress`).
-   **Wyglad**: `m_backgroundColor`, `m_borderColor`, `m_imageTexture`, `m_text`, `m_font`, etc.
# # Zaleznosci i powiazania

-   `framework/ui/declarations.h`, `uilayout.h`.
-   `framework/luaengine/luaobject.h`: Klasa bazowa.
-   Jest klasa bazowa dla wszystkich innych widget�w, np. `UITextEdit`.
-   Jest zarzadzana przez `UIManager`.

---
# ?? uiwidgetimage.cpp
# # Opis og�lny

Plik `uiwidgetimage.cpp` zawiera implementacje czesci klasy `UIWidget` odpowiedzialnej za obsluge i renderowanie obrazu tla.

> **NOTE:** To nie jest osobna klasa, lecz czesc implementacji `UIWidget`, wydzielona do osobnego pliku dla lepszej organizacji kodu.
# # Klasa `UIWidget` (czesc implementacji)
# # # `void UIWidget::initImage()`

Inicjalizuje pola zwiazane z obrazem do wartosci domyslnych.
# # # `void UIWidget::parseImageStyle(const OTMLNodePtr& styleNode)`

Parsuje z wezla OTML wszystkie atrybuty zwiazane z obrazem (`image-source`, `image-clip`, `image-color`, `image-border`, `image-shader` itp.) i wywoluje odpowiednie settery.
# # # `void UIWidget::drawImage(const Rect& screenCoords)`
# # # # Opis semantyczny
Gl�wna metoda rysujaca obraz.
# # # # Dzialanie
1.  Sprawdza, czy tekstura obrazu istnieje.
2.  Jesli geometria (`screenCoords`) lub wlasciwosci obrazu ulegly zmianie (`m_imageMustRecache`), przelicza i buforuje wsp�lrzedne wierzcholk�w i tekstur w `m_imageCoordsBuffer`.
    -   Obsluguje r�zne tryby: proste skalowanie, zachowanie proporcji (`m_imageFixedRatio`), powtarzanie (`m_imageRepeated`) oraz zlozone rysowanie z ramka (`m_imageBordered`), kt�re dzieli obraz na 9 czesci i odpowiednio je skaluje/powtarza.
3.  Dodaje zadanie rysowania do `g_drawQueue`. Jesli zdefiniowano `m_shader`, uzywa specjalnego `DrawQueueItemImageWithShader`.
# # # `void UIWidget::setQRCode(...)`

Generuje obraz kodu QR, tworzy z niego teksture i ustawia ja jako `m_imageTexture`.
# # # `void UIWidget::setImageSource(const std::string& source)`

Laduje teksture z pliku za pomoca `g_textures` i ustawia ja jako `m_imageTexture`. Jesli wlaczone jest `m_imageAutoResize`, dostosowuje rozmiar widgetu do rozmiaru obrazu.
# # # `void UIWidget::setImageSourceBase64(...)`

Dekoduje obraz zakodowany w Base64, tworzy z niego teksture i ustawia ja.
# # Zaleznosci i powiazania

-   `framework/ui/uiwidget.h`: Plik nagl�wkowy klasy, kt�ra implementuje.
-   `framework/graphics/painter.h`, `image.h`, `texture.h`, `texturemanager.h`: Komponenty graficzne.
-   `framework/util/crypt.h`: Do dekodowania Base64.

---
# ?? uianchorlayout.h
# # Opis og�lny

Plik `uianchorlayout.h` deklaruje klasy `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, kt�re razem implementuja system layoutu oparty na "kotwicach" (anchors).
# # Klasa `UIAnchor`
# # # Opis semantyczny
Reprezentuje pojedyncza regule "kotwiczenia", kt�ra wiaze jedna krawedz widgetu z krawedzia innego widgetu (lub rodzica).

-   **Pola**: `m_anchoredEdge` (krawedz tego widgetu), `m_hookedWidgetId` (ID widgetu docelowego), `m_hookedEdge` (krawedz widgetu docelowego).
# # Klasa `UIAnchorGroup`
# # # Opis semantyczny
Kontener na wszystkie kotwice (`UIAnchor`) przypisane do jednego widgetu. Posiada r�wniez flage `m_updated` uzywana przez algorytm layoutu.
# # Klasa `UIAnchorLayout`
# # # Opis semantyczny
`UIAnchorLayout` to menedzer layoutu, kt�ry pozycjonuje i skaluje swoje widgety-dzieci na podstawie zdefiniowanych dla nich regul kotwiczenia. Pozwala to na tworzenie elastycznych i responsywnych interfejs�w, kt�re dostosowuja sie do zmian rozmiaru okna.
# # # Metody publiczne

| Metoda | Opis |
| :--- | :--- |
| `addAnchor(...)` | Dodaje nowa regule kotwiczenia dla widgetu. |
| `removeAnchors(...)` | Usuwa wszystkie kotwice z widgetu. |
| `hasAnchors(...)` | Sprawdza, czy widget ma jakiekolwiek kotwice. |
| `centerIn(...)` | Skr�t do dodania kotwic centrujacych widget. |
| `fill(...)` | Skr�t do dodania kotwic rozciagajacych widget na caly obszar innego widgetu. |
# # # Zmienne prywatne

-   `m_anchorsGroups`: Mapa przechowujaca `UIAnchorGroup` dla kazdego zarzadzanego widgetu.
# # Zaleznosci i powiazania

-   `framework/ui/uilayout.h`: Klasa bazowa.
-   Oznaczona jako `@bindclass`.
-   Jest jednym z najczesciej uzywanych layout�w w projekcie.

---
# ?? uiwidgettext.cpp
# # Opis og�lny

Plik `uiwidgettext.cpp` zawiera implementacje czesci klasy `UIWidget` odpowiedzialnej za obsluge i renderowanie tekstu.

> **NOTE:** To nie jest osobna klasa, lecz czesc implementacji `UIWidget`, wydzielona do osobnego pliku.
# # Klasa `UIWidget` (czesc implementacji)
# # # `void UIWidget::initText()`

Inicjalizuje pola zwiazane z tekstem do wartosci domyslnych (np. domyslny font, wyr�wnanie do srodka).
# # # `void UIWidget::updateText()`

Metoda wywolywana po kazdej zmianie tekstu lub jego wlasciwosci.
1.  Jesli zawijanie jest wlaczone, wywoluje `m_font->wrapText()`, aby przygotowac tekst do wyswietlenia (`m_drawText`).
2.  Jesli wlaczone jest `m_textAutoResize`, oblicza nowy, preferowany rozmiar widgetu na podstawie rozmiaru tekstu i go ustawia.
3.  Ustawia flage `m_textMustRecache`, aby geometria zostala przeliczona przy nastepnym rysowaniu.
# # # `void UIWidget::parseTextStyle(...)`

Parsuje z wezla OTML wszystkie atrybuty zwiazane z tekstem (`text`, `font`, `text-align`, `text-wrap` itp.).
# # # `void UIWidget::drawText(const Rect& screenCoords)`

Dodaje zadanie rysowania tekstu do `g_drawQueue`. Uzywa `m_font` do wykonania wlasciwej operacji rysowania, przekazujac mu tekst (`m_drawText`), obszar (`m_textCachedScreenCoords`), wyr�wnanie, kolor i ewentualne informacje o wielu kolorach.
# # # `void UIWidget::onTextChange(...)` i `onFontChange(...)`

Wirtualne metody, kt�re domyslnie wywoluja odpowiednie `callbacki` w Lua.
# # # `void UIWidget::setText(std::string text, ...)`

Gl�wny setter dla tekstu. Jesli `m_textOnlyUpperCase` jest `true`, konwertuje tekst na wielkie litery. Aktualizuje `m_text`, wywoluje `updateText()` i `onTextChange`.
# # # `void UIWidget::setColoredText(...)`

Setter dla tekstu wielokolorowego. Parsuje wektor string�w, budujac `m_text` i `m_textColors`.
# # # `void UIWidget::setFont(...)`

Ustawia font, pobierajac go z `g_fonts`.
# # Zaleznosci i powiazania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `text-align`.
-   `framework/graphics/fontmanager.h`: Do pobierania font�w.

---
# ?? uiwidgetbasestyle.cpp
# # Opis og�lny

Plik `uiwidgetbasestyle.cpp` zawiera implementacje czesci klasy `UIWidget` odpowiedzialnej za podstawowy styl, czyli wlasciwosci wsp�lne dla wszystkich widget�w, takie jak tlo, ramka, ikona i og�lne atrybuty.
# # Klasa `UIWidget` (czesc implementacji)
# # # `void UIWidget::initBaseStyle()`

Inicjalizuje podstawowe wlasciwosci stylu do wartosci domyslnych (np. przezroczyste tlo, bialy kolor, brak ramki).
# # # `void UIWidget::parseBaseStyle(const OTMLNodePtr& styleNode)`

Gl�wna metoda parsujaca styl.
1.  Najpierw parsuje pola i `callbacki` Lua (`@` i `&`), aby byly dostepne podczas parsowania innych atrybut�w.
2.  Nastepnie parsuje wszystkie podstawowe atrybuty, takie jak `color`, `x`, `y`, `width`, `height`, `background-color`, `opacity`, `rotation`, `enabled`, `visible`, `margin`, `padding`, `border`, `icon`, etc.
3.  Obsluguje r�wniez definicje layoutu (`layout: ...`) oraz deklaracje kotwic (`anchors.left: ...`).
# # # `void UIWidget::drawBackground(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadanie narysowania prostokata wypelnionego kolorem `m_backgroundColor`.
# # # `void UIWidget::drawBorder(const Rect& screenCoords)`

Dodaje do `g_drawQueue` zadania narysowania czterech prostokat�w tworzacych ramke, kazdy z odpowiednim kolorem i gruboscia.
# # # `void UIWidget::drawIcon(const Rect& screenCoords)`

Jesli `m_icon` jest ustawiony, dodaje do `g_drawQueue` zadanie narysowania tekstury ikony w odpowiednim miejscu, uwzgledniajac `m_iconAlign`, `m_iconOffset` i `m_iconColor`.
# # # `void UIWidget::setIcon(const std::string& iconFile)`

Laduje teksture ikony za pomoca `g_textures` i ustawia jej domyslny `clip-rect`.
# # Zaleznosci i powiazania

-   `framework/ui/uiwidget.h`.
-   `framework/ui/uitranslator.h`: Do parsowania `icon-align`.
-   `framework/graphics/texturemanager.h`: Do ladowania tekstur ikon.
-   `framework/graphics/painter.h`: Posrednio, poprzez `g_drawQueue`.

---
# ?? uianchorlayout.cpp
# # Opis og�lny

Plik `uianchorlayout.cpp` zawiera implementacje klas `UIAnchor`, `UIAnchorGroup` i `UIAnchorLayout`, kt�re razem tworza system layoutu opartego na kotwicach.
# # Klasa `UIAnchor`
# # # `UIWidgetPtr UIAnchor::getHookedWidget(...)`

Znajduje widget, do kt�rego dana kotwica jest "przyczepiona". Obsluguje specjalne identyfikatory:
-   `parent`: widget-rodzic.
-   `next`: nastepne rodzenstwo.
-   `prev`: poprzednie rodzenstwo.
-   Inne: szuka dziecka o danym ID w rodzicu.
# # # `int UIAnchor::getHookedPoint(...)`

Oblicza wsp�lrzedna (X lub Y) krawedzi widgetu, do kt�rego kotwica jest przyczepiona.
# # Klasa `UIAnchorGroup`
# # # `void UIAnchorGroup::addAnchor(...)`

Dodaje nowa kotwice do grupy. Jesli kotwica dla tej samej krawedzi juz istnieje, jest ona zastepowana.
# # Klasa `UIAnchorLayout`
# # # `void UIAnchorLayout::addAnchor(...)`

Gl�wna metoda do tworzenia i dodawania nowej reguly kotwiczenia. Tworzy obiekt `UIAnchor` i dodaje go do odpowiedniej `UIAnchorGroup`.
# # # `bool UIAnchorLayout::updateWidget(...)`
# # # # Opis semantyczny
Rekurencyjna metoda, kt�ra oblicza nowy `Rect` dla pojedynczego widgetu na podstawie jego kotwic.
# # # # Dzialanie
1.  Jesli widget, do kt�rego sie kotwiczymy, sam nie zostal jeszcze zaktualizowany, wywoluje `updateWidget` rekurencyjnie dla niego.
2.  Iteruje po wszystkich kotwicach widgetu.
3.  Dla kazdej kotwicy, oblicza docelowy punkt (`point`) na podstawie `getHookedPoint`.
4.  Modyfikuje `newRect` widgetu, ustawiajac lub przesuwajac odpowiednia krawedz (`moveLeft`, `setRight`, `moveVerticalCenter`, itp.).
5.  Po przetworzeniu wszystkich kotwic, ustawia nowy `Rect` dla widgetu.
# # # `bool UIAnchorLayout::internalUpdate()`

Gl�wna metoda aktualizacji layoutu.
1.  Resetuje flagi `m_updated` we wszystkich `UIAnchorGroup`.
2.  W petli przechodzi przez wszystkie widgety zarzadzane przez ten layout i, jesli nie zostaly jeszcze zaktualizowane, wywoluje dla nich `updateWidget`. Petla zapewnia, ze wszystkie zaleznosci zostana rozwiazane.
# # Zaleznosci i powiazania

-   `framework/ui/uianchorlayout.h`: Plik nagl�wkowy.
-   `framework/ui/uiwidget.h`: Operuje na widgetach.

---
# Meta-dokumenty
# # ?? Spis tresci

-   **`const.h`**: Definicje globalnych stalych, makr i typ�w wyliczeniowych.
-   **`CMakeLists.txt`**: Skrypt konfiguracyjny budowania projektu.
-   **`global.h`**: Centralny plik nagl�wkowy, agregujacy podstawowe zaleznosci.
-   **`pch.h`**: Prekompilowany nagl�wek ze standardowymi bibliotekami.
-   **`luafunctions.cpp`**: Implementacja bindowan C++ do Lua.
-   **`resourcemanager.h`**: Deklaracja menedzera zasob�w.
-   **`adaptiverenderer.cpp`**: Implementacja renderera adaptacyjnego.
-   **`adaptiverenderer.h`**: Deklaracja renderera adaptacyjnego.
-   **`application.cpp`**: Implementacja bazowej klasy aplikacji.
-   **`application.h`**: Deklaracja bazowej klasy aplikacji.
-   **`asyncdispatcher.h`**: Deklaracja dyspozytora zadan asynchronicznych.
-   **`binarytree.cpp`**: Implementacja czytnika/writera formatu binarnego drzewa.
-   **`asyncdispatcher.cpp`**: Implementacja dyspozytora zadan asynchronicznych.
-   **`clock.h`**: Deklaracja klasy zegara.
-   **`binarytree.h`**: Deklaracja klas do obslugi formatu binarnego drzewa.
-   **`config.cpp`**: Implementacja klasy do zarzadzania pojedyncza konfiguracja.
-   **`configmanager.cpp`**: Implementacja menedzera konfiguracji.
-   **`configmanager.h`**: Deklaracja menedzera konfiguracji.
-   **`config.h`**: Deklaracja klasy `Config`.
-   **`clock.cpp`**: Implementacja klasy zegara.
-   **`consoleapplication.h`**: Deklaracja aplikacji konsolowej.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `core`.
-   **`event.cpp`**: Implementacja klasy `Event`.
-   **`event.h`**: Deklaracja klasy `Event`.
-   **`eventdispatcher.cpp`**: Implementacja dyspozytora zdarzen.
-   **`eventdispatcher.h`**: Deklaracja dyspozytora zdarzen.
-   **`filestream.cpp`**: Implementacja strumienia plikowego.
-   **`filestream.h`**: Deklaracja strumienia plikowego.
-   **`graphicalapplication.cpp`**: Implementacja aplikacji graficznej.
-   **`inputevent.h`**: Deklaracja struktury `InputEvent`.
-   **`graphicalapplication.h`**: Deklaracja aplikacji graficznej.
-   **`logger.h`**: Deklaracja klasy `Logger`.
-   **`module.cpp`**: Implementacja klasy `Module`.
-   **`modulemanager.cpp`**: Implementacja menedzera modul�w.
-   **`logger.cpp`**: Implementacja klasy `Logger`.
-   **`module.h`**: Deklaracja klasy `Module`.
-   **`modulemanager.h`**: Deklaracja menedzera modul�w.
-   **`scheduledevent.cpp`**: Implementacja zdarzenia zaplanowanego.
-   **`resourcemanager.cpp`**: Implementacja menedzera zasob�w.
-   **`scheduledevent.h`**: Deklaracja zdarzenia zaplanowanego.
-   **`timer.cpp`**: Implementacja timera.
-   **`timer.h`**: Deklaracja timera.
-   **`consoleapplication.cpp`**: Implementacja aplikacji konsolowej.
-   **`shaderprogram.h`**: Deklaracja programu shadera.
-   **`animatedtexture.cpp`**: Implementacja tekstury animowanej.
-   **`animatedtexture.h`**: Deklaracja tekstury animowanej.
-   **`apngloader.cpp`**: Implementacja ladowarki APNG.
-   **`apngloader.h`**: Deklaracja ladowarki APNG.
-   **`atlas.cpp`**: Implementacja atlasu tekstur.
-   **`bitmapfont.cpp`**: Implementacja fontu bitmapowego.
-   **`atlas.h`**: Deklaracja atlasu tekstur.
-   **`bitmapfont.h`**: Deklaracja fontu bitmapowego.
-   **`cachedtext.cpp`**: Implementacja keszowanego tekstu.
-   **`colorarray.h`**: Deklaracja tablicy kolor�w.
-   **`cachedtext.h`**: Deklaracja keszowanego tekstu.
-   **`coordsbuffer.h`**: Deklaracja bufora wsp�lrzednych.
-   **`deptharray.h`**: Deklaracja tablicy glebokosci.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `graphics`.
-   **`coordsbuffer.cpp`**: Implementacja bufora wsp�lrzednych.
-   **`drawcache.cpp`**: Implementacja cache'a rysowania.
-   **`drawcache.h`**: Deklaracja cache'a rysowania.
-   **`drawqueue.cpp`**: Implementacja kolejki rysowania.
-   **`fontmanager.cpp`**: Implementacja menedzera font�w.
-   **`fontmanager.h`**: Deklaracja menedzera font�w.
-   **`drawqueue.h`**: Deklaracja kolejki rysowania.
-   **`framebuffer.cpp`**: Implementacja bufora ramki.
-   **`framebuffer.h`**: Deklaracja bufora ramki.
-   **`framebuffermanager.cpp`**: Implementacja menedzera bufor�w ramki.
-   **`graph.cpp`**: Implementacja wykresu debugujacego.
-   **`graph.h`**: Deklaracja wykresu debugujacego.
-   **`glutil.h`**: Narzedzia OpenGL.
-   **`graphics.cpp`**: Implementacja menedzera grafiki.
-   **`graphics.h`**: Deklaracja menedzera grafiki.
-   **`image.cpp`**: Implementacja klasy `Image`.
-   **`hardwarebuffer.h`**: Deklaracja bufora sprzetowego.
-   **`image.h`**: Deklaracja klasy `Image`.
-   **`framebuffermanager.h`**: Deklaracja menedzera bufor�w ramki.
-   **`painter.h`**: Deklaracja klasy `Painter`.
-   **`painter.cpp`**: Implementacja klasy `Painter`.
-   **`hardwarebuffer.cpp`**: Implementacja bufora sprzetowego.
-   **`paintershaderprogram.cpp`**: Implementacja programu shadera dla `Painter`.
-   **`paintershaderprogram.h`**: Deklaracja programu shadera dla `Painter`.
-   **`shader.cpp`**: Implementacja klasy `Shader`.
-   **`shadermanager.h`**: Deklaracja menedzera shader�w.
-   **`shadermanager.cpp`**: Implementacja menedzera shader�w.
-   **`shader.h`**: Deklaracja klasy `Shader`.
-   **`textrender.cpp`**: Implementacja renderera tekstu.
-   **`shaderprogram.cpp`**: Implementacja programu shadera.
-   **`texture.cpp`**: Implementacja klasy `Texture`.
-   **`texture.h`**: Deklaracja klasy `Texture`.
-   **`texturemanager.cpp`**: Implementacja menedzera tekstur.
-   **`vertexarray.h`**: Deklaracja tablicy wierzcholk�w.
-   **`texturemanager.h`**: Deklaracja menedzera tekstur.
-   **`textrender.h`**: Deklaracja renderera tekstu.
-   **`outfits.h`**: Shadery dla stroj�w.
-   **`newshader.h`**: Nowe shadery.
-   **`shaders.h`**: Agregacja shader�w.
-   **`shadersources.h`**: Zr�dla standardowych shader�w.
-   **`http.cpp`**: Implementacja klienta HTTP/WebSocket.
-   **`websocket.h`**: Deklaracja sesji WebSocket.
-   **`http.h`**: Deklaracja klienta HTTP/WebSocket.
-   **`result.h`**: Deklaracja struktury `HttpResult`.
-   **`session.cpp`**: Implementacja sesji HTTP.
-   **`session.h`**: Deklaracja sesji HTTP.
-   **`websocket.cpp`**: Implementacja sesji WebSocket.
-   **`mouse.cpp`**: Implementacja menedzera myszy.
-   **`mouse.h`**: Deklaracja menedzera myszy.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `luaengine`.
-   **`lbitlib.cpp`**: Implementacja biblioteki `bit32` dla Lua.
-   **`lbitlib.h`**: Deklaracja biblioteki `bit32`.
-   **`luabinder.h`**: Mechanizm bindowania C++ do Lua.
-   **`luaexception.h`**: Deklaracja wyjatk�w Lua.
-   **`luaexception.cpp`**: Implementacja wyjatk�w Lua.
-   **`luainterface.cpp`**: Implementacja interfejsu Lua.
-   **`luainterface.h`**: Deklaracja interfejsu Lua.
-   **`luaobject.cpp`**: Implementacja `LuaObject`.
-   **`luaobject.h`**: Deklaracja `LuaObject`.
-   **`luavaluecasts.cpp`**: Implementacja konwersji typ�w Lua.
-   **`luavaluecasts.h`**: Deklaracja konwersji typ�w Lua.
-   **`connection.cpp`**: Implementacja polaczenia TCP.
-   **`server.h`**: Deklaracja serwera TCP.
-   **`connection.h`**: Deklaracja polaczenia TCP.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `net`.
-   **`inputmessage.h`**: Deklaracja wiadomosci przychodzacej.
-   **`outputmessage.cpp`**: Implementacja wiadomosci wychodzacej.
-   **`outputmessage.h`**: Deklaracja wiadomosci wychodzacej.
-   **`packet_player.cpp`**: Implementacja odtwarzacza pakiet�w.
-   **`packet_player.h`**: Deklaracja odtwarzacza pakiet�w.
-   **`protocol.h`**: Deklaracja protokolu sieciowego.
-   **`packet_recorder.cpp`**: Implementacja nagrywarki pakiet�w.
-   **`protocol.cpp`**: Implementacja protokolu sieciowego.
-   **`server.cpp`**: Implementacja serwera TCP.
-   **`inputmessage.cpp`**: Implementacja wiadomosci przychodzacej.
-   **`packet_recorder.h`**: Deklaracja nagrywarki pakiet�w.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `otml`.
-   **`otmlparser.h`**: Deklaracja parsera OTML.
-   **`otml.h`**: Agregacja nagl�wk�w OTML.
-   **`otmldocument.cpp`**: Implementacja dokumentu OTML.
-   **`otmldocument.h`**: Deklaracja dokumentu OTML.
-   **`otmlemitter.cpp`**: Implementacja emittera OTML.
-   **`otmlexception.cpp`**: Implementacja wyjatk�w OTML.
-   **`otmlexception.h`**: Deklaracja wyjatk�w OTML.
-   **`otmlemitter.h`**: Deklaracja emittera OTML.
-   **`otmlparser.cpp`**: Implementacja parsera OTML.
-   **`otmlnode.h`**: Deklaracja wezla OTML.
-   **`otmlnode.cpp`**: Implementacja wezla OTML.
-   **`androidplatform.cpp`**: Implementacja platformy dla Androida.
-   **`androidwindow.cpp`**: Implementacja okna dla Androida.
-   **`androidwindow.h`**: Deklaracja okna dla Androida.
-   **`crashhandler.h`**: Deklaracja obslugi awarii.
-   **`platform.cpp`**: Implementacja globalnej instancji platformy.
-   **`platformwindow.cpp`**: Implementacja bazowej klasy okna.
-   **`platform.h`**: Deklaracja klasy `Platform`.
-   **`platformwindow.h`**: Deklaracja bazowej klasy okna.
-   **`sdlwindow.cpp`**: Implementacja okna SDL (WASM).
-   **`sdlwindow.h`**: Deklaracja okna SDL.
-   **`unixcrashhandler.cpp`**: Implementacja obslugi awarii dla Uniksa.
-   **`unixplatform.cpp`**: Implementacja platformy dla Uniksa.
-   **`win32crashhandler.cpp`**: Implementacja obslugi awarii dla Windows.
-   **`win32platform.cpp`**: Implementacja platformy dla Windows.
-   **`win32window.cpp`**: Implementacja okna dla Windows.
-   **`win32window.h`**: Deklaracja okna dla Windows.
-   **`x11window.h`**: Deklaracja okna X11.
-   **`x11window.cpp`**: Implementacja okna X11.
-   **`proxy.cpp`**: Implementacja menedzera proxy.
-   **`proxy.h`**: Deklaracja menedzera proxy.
-   **`proxy_client.h`**: Deklaracja klienta proxy.
-   **`proxy_client.cpp`**: Implementacja klienta proxy.
-   **`combinedsoundsource.cpp`**: Implementacja zlozonego zr�dla dzwieku.
-   **`combinedsoundsource.h`**: Deklaracja zlozonego zr�dla dzwieku.
-   **`oggsoundfile.cpp`**: Implementacja pliku dzwiekowego OGG.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `sound`.
-   **`oggsoundfile.h`**: Deklaracja pliku dzwiekowego OGG.
-   **`soundbuffer.cpp`**: Implementacja bufora dzwieku.
-   **`soundbuffer.h`**: Deklaracja bufora dzwieku.
-   **`soundfile.cpp`**: Implementacja pliku dzwiekowego.
-   **`soundchannel.cpp`**: Implementacja kanalu dzwiekowego.
-   **`soundchannel.h`**: Deklaracja kanalu dzwiekowego.
-   **`soundfile.h`**: Deklaracja pliku dzwiekowego.
-   **`soundmanager.cpp`**: Implementacja menedzera dzwieku.
-   **`soundmanager.h`**: Deklaracja menedzera dzwieku.
-   **`soundsource.cpp`**: Implementacja zr�dla dzwieku.
-   **`streamsoundsource.cpp`**: Implementacja strumieniowego zr�dla dzwieku.
-   **`streamsoundsource.h`**: Deklaracja strumieniowego zr�dla dzwieku.
-   **`soundsource.h`**: Deklaracja zr�dla dzwieku.
-   **`any.h`**: Implementacja `stdext::any`.
-   **`cast.h`**: Funkcje do rzutowania typ�w.
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
-   **`stdext.h`**: Agregacja nagl�wk�w `stdext`.
-   **`packed_storage.h`**: Implementacja `packed_storage`.
-   **`thread.h`**: Agregacja nagl�wk�w watk�w.
-   **`time.h`**: Deklaracja funkcji czasowych.
-   **`traits.h`**: Narzedzia metaprogramowania.
-   **`string.h`**: Deklaracja funkcji do string�w.
-   **`time.cpp`**: Implementacja funkcji czasowych.
-   **`uri.h`**: Deklaracja parsera URI.
-   **`net.cpp`**: Implementacja narzedzi sieciowych.
-   **`uri.cpp`**: Implementacja parsera URI.
-   **`types.h`**: Definicje typ�w.
-   **`format.h`**: Implementacja `stdext::format`.
-   **`string.cpp`**: Implementacja funkcji do string�w.
-   **`declarations.h`**: Wczesne deklaracje dla modulu `ui`.
-   **`ui.h`**: Agregacja nagl�wk�w UI.
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
-   **`uitranslator.cpp`**: Implementacja translator�w UI.
-   **`uitranslator.h`**: Deklaracja translator�w UI.
-   **`uiverticallayout.cpp`**: Implementacja `UIVerticalLayout`.
-   **`uiverticallayout.h`**: Deklaracja `UIVerticalLayout`.
-   **`uiwidget.cpp`**: Implementacja `UIWidget`.
-   **`uiwidget.h`**: Deklaracja `UIWidget`.
-   **`uiwidgetimage.cpp`**: Implementacja czesci `UIWidget` (obraz).
-   **`uianchorlayout.h`**: Deklaracja `UIAnchorLayout`.
-   **`uiwidgettext.cpp`**: Implementacja czesci `UIWidget` (tekst).
-   **`uiwidgetbasestyle.cpp`**: Implementacja czesci `UIWidget` (styl).
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
-   **`qrcodegen.c`**: Implementacja generatora kod�w QR.
-   **`qrcodegen.h`**: Deklaracja generatora kod�w QR.
-   **`rect.h`**: Implementacja `Rect`.
-   **`size.h`**: Implementacja `Size`.
-   **`stats.cpp`**: Implementacja systemu statystyk.
-   **`stats.h`**: Deklaracja systemu statystyk.
-   **`tinystr.cpp`**: Implementacja `TiXmlString`.
-   **`tinyxmlparser.cpp`**: Implementacja parsera TinyXML.
-   **`tinystr.h`**: Deklaracja `TiXmlString`.
-   **`tinyxml.cpp`**: Implementacja TinyXML.
-   **`tinyxmlerror.cpp`**: Bledy TinyXML.
-   **`tinyxml.h`**: Deklaracja TinyXML.

---
# # ?? Indeks funkcji/metod
*W przygotowaniu*

---
# # ?? Mapa zaleznosci

```mermaid
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

    subgraph Zaleznosci_Zewnetrzne
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
    Framework_Net --> Zaleznosci_Zewnetrzne
    ResourceManager --> PhysFS
```
# # ?? Architektura systemu

System `otclient` jest zbudowany w oparciu o architekture modulowa i warstwowa, kt�ra oddziela rdzen frameworka od logiki specyficznej dla klienta gry.
# # # Warstwy

1.  **Warstwa platformy (`framework/platform`)**
    -   **Opis**: Najnizsza warstwa, kt�ra abstrakcjonuje interakcje z systemem operacyjnym. Zawiera implementacje dla Windows (WinAPI), Linux/macOS (X11) i Android (NDK/JNI).
    -   **Komponenty**: `Platform` (operacje na plikach, procesach), `PlatformWindow` (zarzadzanie oknem, wejsciem, kontekstem graficznym), `CrashHandler`.
    -   **Cel**: Zapewnienie przenosnosci kodu miedzy r�znymi systemami.

2.  **Warstwa rozszerzen standardowych (`framework/stdext`)**
    -   **Opis**: Zbi�r narzedzi i rozszerzen do standardowej biblioteki C++, kt�re sa uzywane w calym projekcie.
    -   **Komponenty**: `shared_object_ptr` (inteligentne wskazniki), `cast` (bezpieczne rzutowanie typ�w), `format` (formatowanie string�w), `string` (narzedzia do string�w), `time` (obsluga czasu).
    -   **Cel**: Dostarczenie sp�jnego i rozbudowanego zestawu narzedzi podstawowych.

3.  **Warstwa rdzenia frameworka (`framework/core`)**
    -   **Opis**: Serce aplikacji. Implementuje gl�wne petle, system zdarzen, zarzadzanie zasobami, modulami i konfiguracja.
    -   **Komponenty**: `Application` (i pochodne), `EventDispatcher`, `ResourceManager`, `ModuleManager`, `ConfigManager`, `Logger`.
    -   **Cel**: Zapewnienie solidnej podstawy i infrastruktury dla dzialania aplikacji.

4.  **Warstwa silnik�w (Framework Engines)**
    -   **Opis**: Zbi�r wyspecjalizowanych podsystem�w (silnik�w), kt�re realizuja kluczowe funkcjonalnosci.
    -   **Komponenty**:
        -   **Silnik graficzny (`framework/graphics`, `framework/ui`)**: `Graphics`, `Painter`, `TextureManager`, `UIManager`, `UIWidget`. Odpowiada za cale renderowanie 2D i interfejs uzytkownika.
        -   **Silnik Lua (`framework/luaengine`)**: `LuaInterface`, `luabinder`. Most miedzy C++ a Lua, umozliwiajacy skryptowanie.
        -   **Silnik sieciowy (`framework/net`, `framework/proxy`)**: `Protocol`, `Connection`, `ProxyManager`. Obsluguje komunikacje z serwerem.
        -   **Silnik dzwieku (`framework/sound`)**: `SoundManager`. Obsluguje odtwarzanie dzwieku.
    -   **Cel**: Enkapsulacja zlozonych funkcjonalnosci w oddzielne, zarzadzalne moduly.

5.  **Warstwa logiki klienta (`src/client`)**
    -   **Opis**: Najwyzsza warstwa, kt�ra zawiera logike specyficzna dla klienta gry Tibii. Implementuje ona mechanike gry, renderowanie swiata, postaci, przedmiot�w itp.
    -   **Komponenty**: (Niezalaczone w promptcie) `Game`, `Map`, `Creature`, `Item`, `ProtocolGame`.
    -   **Cel**: Implementacja wlasciwej gry. Ta warstwa intensywnie korzysta z API dostarczanego przez nizsze warstwy frameworka.

6.  **Warstwa skryptowa (Moduly Lua)**
    -   **Opis**: Zewnetrzna warstwa, kt�ra pozwala na rozszerzanie i modyfikowanie klienta bez potrzeby rekompilacji kodu C++. Skrypty Lua maja dostep do API frameworka i logiki klienta za posrednictwem bindowan.
    -   **Komponenty**: Pliki `.lua` i `.otmod` w katalogach `modules/` i `mods/`.
    -   **Cel**: Umozliwienie tworzenia wtyczek, modyfikacji interfejsu i dodawania nowej funkcjonalnosci.
# # # Przeplyw danych i interakcje

-   **Start aplikacji**: `main()` tworzy instancje `GraphicalApplication`, kt�ra inicjalizuje warstwy od dolu do g�ry (Platforma -> Rdzen -> Silniki).
-   **Gl�wna petla**: `GraphicalApplication::run()` uruchamia wielowatkowa petle. Watek logiki (`worker`) aktualizuje stan gry i przygotowuje dane do rysowania. Watek renderowania (gl�wny) rysuje te dane na ekranie i odbiera zdarzenia od `PlatformWindow`.
-   **Zdarzenia wejsciowe**: `PlatformWindow` -> `GraphicalApplication` -> `UIManager` -> `UIWidget` -> Skrypt Lua (callback `onClick` itp.).
-   **Komunikacja sieciowa**: Skrypt Lua (np. `g_game.login(...)`) -> `ProtocolGame` (Lua) -> `Protocol` (C++) -> `Connection` (C++) -> Siec. Pakiety przychodzace ida w odwrotna strone.
-   **Renderowanie**: Logika klienta (C++ lub Lua) tworzy widgety i ustawia ich wlasciwosci -> `UIManager` i `UIWidget` przygotowuja `DrawQueue` -> `GraphicalApplication` przekazuje `DrawQueue` do `Painter` -> `Painter` wykonuje wywolania OpenGL.
