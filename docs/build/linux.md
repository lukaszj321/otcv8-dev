# Kompilacja na systemie Linux

Ten przewodnik opisuje, jak skompilowac OTCv8 na systemach operacyjnych opartych na Linuksie, takich jak Ubuntu.

## Wymagania wstepne

Bedziesz potrzebowac nastepujacych zaleznosci:

- `git`
- `cmake`
- `g++` lub `clang`
- Biblioteki deweloperskie dla `OpenGL`, `OpenAL`, `libcurl` i `zlib`.

## Kroki kompilacji

1.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/lukaszj321/otcv8-dev.git
    cd otcv8-dev
    ```

2.  **Utw�rz folder build:**
    ```bash
    mkdir build && cd build
    ```

3.  **Uruchom CMake i skompiluj:**
    ```bash
    cmake ..
    make
    ```

Po pomyslnej kompilacji plik wykonywalny znajdzie sie w folderze `build`.