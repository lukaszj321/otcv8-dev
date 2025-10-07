# Kompilacja na systemie Linux

Ten przewodnik opisuje, jak skompilować OTCv8 na systemach operacyjnych opartych na Linuksie, takich jak Ubuntu.

## Wymagania wstępne

Będziesz potrzebować następujących zależności:

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

2.  **Utwórz folder build:**
    ```bash
    mkdir build && cd build
    ```

3.  **Uruchom CMake i skompiluj:**
    ```bash
    cmake ..
    make
    ```

Po pomyślnej kompilacji plik wykonywalny znajdzie się w folderze `build`.