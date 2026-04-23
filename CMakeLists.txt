cmake_minimum_required(VERSION 3.10)
project(MaLib3_Python LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

# 1. Dépendance envers MaLib1
# Le Superbuild a configuré CMAKE_PREFIX_PATH pour qu'on le trouve dans 'install'
find_package(MaLib1 REQUIRED)

# 2. Génération de code via Python
find_package(Python3 REQUIRED COMPONENTS Interpreter)
set(GEN_DIR ${CMAKE_CURRENT_BINARY_DIR}/gen)

# Cette commande définit COMMENT générer le fichier, mais ne l'exécute pas encore
add_custom_command(
    OUTPUT ${GEN_DIR}/unite.cpp
    COMMAND Python3::Interpreter ${CMAKE_CURRENT_SOURCE_DIR}/tools/xmlToUnit.py 
            "dummy.xml" ${GEN_DIR}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/tools/xmlToUnit.py
    COMMENT "Execution du script Python de generation..."
)

# 3. Création de la lib MaLib3
# On inclut le fichier généré dans les sources
add_library(MaLib3 SHARED ${GEN_DIR}/unite.cpp src/lib3.cpp)
target_include_directories(MaLib3 PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# On lie MaLib1 (les drapeaux de compilation de MaLib1 sont propagés)
target_link_libraries(MaLib3 PRIVATE MaLib1)

install(TARGETS MaLib3 
    EXPORT MaLib3Targets
    DESTINATION lib
    INCLUDES DESTINATION include
)

install(FILES include/lib3.h DESTINATION include)

# NOTE : Ici on génère un fichier nommé MaLib3_PythonConfig.cmake 
# pour correspondre au find_package(MaLib3_Python) de l'app finale
install(EXPORT MaLib3Targets
    FILE MaLib3_PythonConfig.cmake
    DESTINATION lib/cmake/MaLib3_Python
)
