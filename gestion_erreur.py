import traceback

# Codes de couleur ANSI pour la console
ROUGE = "\033[91m"
RESET = "\033[0m"

def afficher_erreur(fichier, code, exception):
    """
    Affiche les erreurs
    """
    if isinstance(exception, SyntaxError):
        lineno = exception.lineno or 0
        texte = exception.text or ""
        offset = exception.offset or 0

        print(f"{ROUGE}Fichier \"{fichier}\", ligne {lineno}{RESET}")
        print(f"    {texte.rstrip()}")
        # caret sous l'endroit exact de l'erreur
        print("    " + " " * (offset - 1) + "^")
        print(f"{ROUGE}SyntaxeErreur: syntaxe invalide{RESET}")

    else:
        # Pour les autres types d'erreurs
        tb = traceback.format_exception_only(type(exception), exception)
        print(f"{ROUGE}{''.join(tb).strip()}{RESET}")
