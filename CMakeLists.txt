cmake_minimum_required(VERSION 3.13)
project(otcv8-dev LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Dodaj katalog z plikami źródłowymi
file(GLOB SRC_FILES src/*.cpp)

# Dodaj katalog z plikami nagłówkowymi
include_directories(
    ${CMAKE_SOURCE_DIR}/include
)

# Dodaj zewnętrzne biblioteki, jeśli potrzebujesz (przykład z Boost)
find_package(Boost REQUIRED COMPONENTS filesystem system)
include_directories(${Boost_INCLUDE_DIRS})

# Dodaj bibliotekę lub program
add_executable(otcv8 ${SRC_FILES})

# Podlinkuj zewnętrzne biblioteki
target_link_libraries(otcv8 PRIVATE ${Boost_LIBRARIES} zip lua5.1 glew physfs ssl bz2 luajit-5.1)

# Jeśli używasz innych bibliotek, dodaj je tutaj
# target_link_libraries(otcv8 PRIVATE ...)

# Opcjonalnie: Dodaj testy
# enable_testing()
# add_subdirectory(tests)
