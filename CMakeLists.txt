cmake_minimum_required(VERSION 3.10)

# Project name
project(PingAdvance LANGUAGES C CXX)

# Add source files
set(SRC_FILES
        src/ping_c/ping.c
        src/ping_c/ping_common.c
        src/ping_c/ping_common.h
        src/ping_adv.cpp
        src/ping_c/SNAPSHOT.h
)

# Specify the executable target
add_executable(${PROJECT_NAME} ${SRC_FILES})

# Set the C++ standard
set_target_properties(${PROJECT_NAME} PROPERTIES
        CXX_STANDARD 17
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
)

# Include directories
target_include_directories(${PROJECT_NAME} PRIVATE src)
