cmake_minimum_required(VERSION 3.20)
project(crash_app LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(crash_app crash.cpp)

if (MSVC)
    # Debug-friendly: full PDB, no optimizations, debug CRT statically linked so
    # the test binary has no extra DLL dependencies and symbols resolve cleanly.
    target_compile_options(crash_app PRIVATE
        /Zi /Od /W3 /MTd /EHsc
    )
    target_link_options(crash_app PRIVATE
        /DEBUG
        /INCREMENTAL:NO
    )
endif()
