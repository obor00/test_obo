# Exemple de dictionnaire
dictionnaire = {
    "a": {
        "b": {
            "c": "foo"
        }
    },
    "d": {
        "e": "bar"
    },
    "f": {
        "e": "bar"
    }
}


def rechercher_cles(dictionnaire, cle):
    cles_complete = []
    for k, v in dictionnaire.items():
        if k == cle:
            cles_complete.append(k)
        elif isinstance(v, dict):
            cles_complete.extend([k + "." + c for c in rechercher_cles(v, cle)])
    return cles_complete

# Exemple d'utilisation
cle_complete = rechercher_cles(dictionnaire, 'e')
print(cle_complete) # d.e
