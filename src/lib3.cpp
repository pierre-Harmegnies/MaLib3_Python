#include "lib3.h"
#include "lib1.h" // On utilise Lib1 !
#include <iostream>

// Declare la fonction generee par Python (on ferait un .h normalement)
void generated_function();

namespace Lib3 {
    void callAll() {
        std::cout << "[LIB3] Appel de Lib 1 : " << Lib1::getName() << std::endl;
        generated_function();
    }
}
