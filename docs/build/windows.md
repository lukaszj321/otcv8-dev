# Kompilacja w systemie Windows

Ten przewodnik pomoze Ci skompilowac OTCv8 przy uzyciu Visual Studio w systemie Windows.

## Wymagania wstepne

- **Visual Studio 2019 lub nowsze**: Upewnij sie, ze masz zainstalowany komponent "Programowanie aplikacji klasycznych w jezyku C++".
- **Git**: Do klonowania repozytorium.
- **vcpkg**: Menedzer pakiet�w C++ dla Windows, do zarzadzania zaleznosciami.

## Instalacja zaleznosci przez vcpkg

Po zainstalowaniu vcpkg, uzyj nastepujacych polecen, aby pobrac i zainstalowac wymagane biblioteki:

```bash
vcpkg install physfs zlib glew boost-iostreams boost-asio boost-system boost-filesystem boost-variant protobuf luajit curl openal-soft```

## Kroki kompilacji

1.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/lukaszj321/otcv8-dev.git
    ```

2.  **Skonfiguruj projekt za pomoca CMake:**
    Uruchom CMake-GUI, wskaz folder zr�dlowy i folder, w kt�rym chcesz zbudowac projekt. Kliknij "Configure" i wybierz swoja wersje Visual Studio. Bedziesz musial wskazac plik `vcpkg.cmake` w ustawieniach CMake, aby polaczyc zaleznosci.

3.  **Otw�rz i skompiluj w Visual Studio:**
    Po pomyslnej konfiguracji, kliknij "Generate", a nastepnie "Open Project". Visual Studio otworzy wygenerowane rozwiazanie. Teraz mozesz skompilowac projekt, klikajac `Build > Build Solution`.