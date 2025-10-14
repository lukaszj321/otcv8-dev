cmake_minimum_required(VERSION 3.10)
project(otclient)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Ustaw domyślny typ budowy
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

if(VERSION)
    add_definitions(-DVERSION="${VERSION}")
endif()

add_executable(${PROJECT_NAME} ${framework_SOURCES} ${client_SOURCES} ${executable_SOURCES})
target_link_libraries(${PROJECT_NAME} ${framework_LIBRARIES})

if(APPLE AND USE_STATIC_LIBS)
    target_link_libraries(${PROJECT_NAME} "-framework Foundation" "-framework IOKit")
endif()
