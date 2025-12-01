import sys
import re
from .traducteur import mugen_python_mots

def traduire(code):
    """
    Traduit le code écrit en français en code Python.
    """
    for eng, fr in mugen_python_mots.items():
        code = re.sub(rf'\b{re.escape(fr)}\b', eng, code)
    return code

def executer(fichier):
    """
    Exécute un fichier .mgpy traduit en Python.
    """
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            code_fr = f.read()
    except FileNotFoundError:
        print(f"Erreur : fichier '{fichier}' introuvable.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        sys.exit(1)

    code_py = traduire(code_fr)

    try:
        exec(code_py)
    except Exception as e:
        print(f"Erreur lors de l'exécution du code : {e}")

def cli():
    """
    Interface en ligne de commande pour mgpy.
    """
    if len(sys.argv) < 2:
        print("Utilisation : mgpy <fichier>")
        sys.exit(1)

    fichier = sys.argv[1]
    executer(fichier)
