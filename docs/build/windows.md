# Kompilacja w systemie Windows

Ten przewodnik pomoże Ci skompilować OTCv8 przy użyciu Visual Studio w systemie Windows.

## Wymagania wstępne

- **Visual Studio 2019 lub nowsze**: Upewnij się, że masz zainstalowany komponent "Programowanie aplikacji klasycznych w języku C++".
- **Git**: Do klonowania repozytorium.
- **vcpkg**: Menedżer pakietów C++ dla Windows, do zarządzania zależnościami.

## Instalacja zależności przez vcpkg

Po zainstalowaniu vcpkg, użyj następujących poleceń, aby pobrać i zainstalować wymagane biblioteki:

```bash
vcpkg install physfs zlib glew boost-iostreams boost-asio boost-system boost-filesystem boost-variant protobuf luajit curl openal-soft```

## Kroki kompilacji

1.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/lukaszj321/otcv8-dev.git
    ```

2.  **Skonfiguruj projekt za pomocą CMake:**
    Uruchom CMake-GUI, wskaż folder źródłowy i folder, w którym chcesz zbudować projekt. Kliknij "Configure" i wybierz swoją wersję Visual Studio. Będziesz musiał wskazać plik `vcpkg.cmake` w ustawieniach CMake, aby połączyć zależności.

3.  **Otwórz i skompiluj w Visual Studio:**
    Po pomyślnej konfiguracji, kliknij "Generate", a następnie "Open Project". Visual Studio otworzy wygenerowane rozwiązanie. Teraz możesz skompilować projekt, klikając `Build > Build Solution`.