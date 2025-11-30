import sys
import re
from .traduction import mugen_python_fr

def traduire(code):
    for eng, fr in mugen_python_fr.items():
        code = re.sub(r'\b' + fr + r'\b', eng, code)
    return code

def executer_fichier(chemin):
    with open(chemin, "r") as f:
        code_mugen = f.read()
    code_python = traduire(code_mugen)
    exec(code_python, {})

def main():
    if len(sys.argv) < 2:
        print("Utilisation : mgpy <script>")
        return
    executer_fichier(sys.argv[1])
