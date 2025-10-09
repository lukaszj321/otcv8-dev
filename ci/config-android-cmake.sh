#!/usr/bin/env bash
set -euo pipefail

# Gdzie rozpakowałeś prebuilt’y (android_libs.7z -> android/android_libs/…)
PREFIX="${GITHUB_WORKSPACE:-$PWD}/android/android_libs/arm64-v8a"

echo "==> Using PREFIX: $PREFIX"

# Szybkie sanity-checki (jeśli coś brakuje, CI poda czytelny komunikat)
[[ -f "$PREFIX/lib/libzip.a" ]] || { echo "::error::Brak libzip.a w $PREFIX/lib"; exit 1; }
[[ -f "$PREFIX/lib/libbz2.a" ]] || { echo "::error::Brak libbz2.a w $PREFIX/lib"; exit 1; }
[[ -f "$PREFIX/include/zip.h" ]] || { echo "::error::Brak nagłówka zip.h w $PREFIX/include"; exit 1; }
[[ -f "$PREFIX/include/zipconf.h" ]] || { echo "::error::Brak nagłówka zipconf.h w $PREFIX/include"; exit 1; }
[[ -d "$PREFIX/include/boost" ]] || { echo "::error::Brak nagłówków Boost w $PREFIX/include/boost"; exit 1; }

# (opcjonalnie) LuaJIT – podajemy tylko jeśli jest w paczce
EXTRA_ARGS=()
LUAJIT_LIB=""
if [[ -f "$PREFIX/lib/libluajit.a" ]]; then
  LUAJIT_LIB="$PREFIX/lib/libluajit.a"
elif [[ -f "$PREFIX/lib/libluajit-5.1.a" ]]; then
  LUAJIT_LIB="$PREFIX/lib/libluajit-5.1.a"
fi
if [[ -n "${LUAJIT_LIB}" ]]; then
  LUAJIT_INC="$PREFIX/include"
  [[ -d "$PREFIX/include/luajit" ]] && LUAJIT_INC="$PREFIX/include/luajit"
  EXTRA_ARGS+=(-DLUAJIT_LIBRARY="$LUAJIT_LIB" -DLUAJIT_INCLUDE_DIR="$LUAJIT_INC")
fi

cmake -S . -B build-android-arm64 -G Ninja \
  -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK_ROOT/build/cmake/android.toolchain.cmake" \
  -DANDROID_ABI=arm64-v8a \
  -DANDROID_PLATFORM=android-25 \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DBOOST_ROOT="$PREFIX" \
  -DBOOST_INCLUDEDIR="$PREFIX/include" \
  -DBOOST_LIBRARYDIR="$PREFIX/lib" \
  -DBZIP2_INCLUDE_DIR="$PREFIX/include" \
  -DBZIP2_LIBRARIES="$PREFIX/lib/libbz2.a" \
  -DLIBZIP_INCLUDE_DIR_ZIP="$PREFIX/include" \
  -DLIBZIP_INCLUDE_DIR_ZIPCONF="$PREFIX/include" \
  -DLIBZIP_LIBRARY="$PREFIX/lib/libzip.a" \
  -DCMAKE_FIND_ROOT_PATH="$PREFIX" \
  -DCMAKE_PREFIX_PATH="$PREFIX" \
  "${EXTRA_ARGS[@]}"
