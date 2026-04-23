import sys
import os

# Petit script qui lit un fichier XML Bidon et genere un .cpp
xml_file = sys.argv[1]
out_dir = sys.argv[2]

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

cpp_content = """
#include <iostream>
void generated_function() {
    std::cout << "[GENERE] Bonjour depuis le code genere par Python !" << std::endl;
}
"""

with open(os.path.join(out_dir, "unite.cpp"), "w") as f:
    f.write(cpp_content)

print(f"Generation terminee dans {out_dir}")
