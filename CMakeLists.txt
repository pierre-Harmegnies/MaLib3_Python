cmake_minimum_required(VERSION 3.10)
project(MaLib3_Python LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

# 1. Dependance envers Lib1 (trouvee par le superbuild)
find_package(MaLib1 REQUIRED)

# 2. Generation Python
find_package(Python3 REQUIRED COMPONENTS Interpreter)
set(GEN_DIR ${CMAKE_CURRENT_BINARY_DIR}/gen)

add_custom_command(
    OUTPUT ${GEN_DIR}/unite.cpp
    COMMAND Python3::Interpreter ${CMAKE_CURRENT_SOURCE_DIR}/tools/xmlToUnit.py 
            "dummy.xml" ${GEN_DIR}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/tools/xmlToUnit.py
    COMMENT "Execution du script Python de generation..."
)

# 3. Creation de la lib (SHARED)
add_library(MaLib3 SHARED ${GEN_DIR}/unite.cpp src/lib3.cpp)
target_include_directories(MaLib3 PUBLIC include)

# On linke la Lib1 (indispensable si utilisee en interne)
target_link_libraries(MaLib3 PRIVATE MaLib1)

install(TARGETS MaLib3 DESTINATION lib)
install(FILES include/lib3.h DESTINATION include)
