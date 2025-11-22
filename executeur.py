# mugenpy/exécuteur.py

import sys
from .traducteur import traduire

def run():
    if len(sys.argv) < 2:
        print("Usage : mgnpy fichier.mgpy")
        sys.exit(1)

    fichier = sys.argv[1]

    try:
        with open(fichier, "r", encoding="utf-8") as f:
            code_fr = f.read()
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable → {fichier}")
        sys.exit(1)

    # Traduction FR → Python
    code_py = traduire(code_fr)

    # Exécution du code traduit
    try:
        exec(code_py, {})
    except Exception as e:
        print("Erreur dans le code traduit :")
        print(e)
