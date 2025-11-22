# mugenpy/traducteur.py

def traduire(code):
    remplacements = {
        "afficher": "print",
        "si ": "if ",
        "sinon": "else",
        "tant_que": "while",
        "pour ": "for ",
        "dans ": "in ",
        "definir ": "def ",
        "retourner": "return",
        "vrai": "True",
        "faux": "False",
        "et": "and",
        "ou": "or",
        "non": "not",
    }

    for fr, en in remplacements.items():
        code = code.replace(fr, en)

    return code
