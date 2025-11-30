import sys
from .traduction import mugen_python_fr

def traduire(code):
    for eng, fr in mugen_python_fr.items():
        code = code.replace(fr, eng)
    return code

def executer(fichier):
    with open(fichier, "r") as f:
        code_fr = f.read()

    code_py = traduire(code_fr)
    exec(code_py)

def cli():
    if len(sys.argv) < 2:
        print("Utilisation : mgpy <fichier>")
        sys.exit(1)

    fichier = sys.argv[1]
    executer(fichier)
