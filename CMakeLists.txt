cmake_minimum_required(VERSION 3.10)
project(otclient)

# Wymuszamy C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Domyślny build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

option(FRAMEWORK_SOUND     "Use SOUND"    OFF)
option(FRAMEWORK_GRAPHICS  "Use GRAPHICS" ON)
option(FRAMEWORK_XML       "Use XML"      ON)
option(FRAMEWORK_NET       "Use NET"      ON)

# Włącz podprojekty
include(src/framework/CMakeLists.txt)
include(src/client/CMakeLists.txt)

# Linker flags (dla nie-Apple i nie-WASM)
if(NOT APPLE AND NOT WASM)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -no-pie -Wl,-Map=${PROJECT_NAME}.map")
endif()

set(executable_SOURCES
    src/main.cpp
)

# Ikona dla Windows
if(WIN32)
    add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/otcicon.o
        COMMAND ${CMAKE_RC_COMPILER}
        -I${CMAKE_CURRENT_SOURCE_DIR}/src
        -i${CMAKE_CURRENT_SOURCE_DIR}/src/otcicon.rc
        -o ${CMAKE_CURRENT_BINARY_DIR}/otcicon.o)
    set(executable_SOURCES ${executable_SOURCES} otcicon.o)
endif()

# Wersja (może być przekazana przez -DVERSION=xxx)
if(VERSION)
    add_definitions(-DVERSION="${VERSION}")
endif()

# Tworzenie binarki
add_executable(${PROJECT_NAME} ${framework_SOURCES} ${client_SOURCES} ${executable_SOURCES})
target_link_libraries(${PROJECT_NAME} ${framework_LIBRARIES})

# Specjalne linkowanie dla macOS
if(APPLE AND USE_STATIC_LIBS)
    target_link_libraries(${PROJECT_NAME} "-framework Foundation" "-framework IOKit")
endif()
