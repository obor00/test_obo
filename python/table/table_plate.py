# Exemple de dictionnaire
dictionnaire = {
    "a": {
        "b": {
            "c": ["foo", "bar"]
        }
    },
    "d": [
        {  "oo": "bar"  },
        { "kk": "hello"}
    ],
    "f": {
        "e": "bar"
    }
}


# Solution
liste = []

def recursif(dic, cle=""):
    # Parcours les clés du dictionnaire
    for key, value in dic.items():
        if isinstance(value, dict):
            # Si la valeur est un dictionnaire, appelle la fonction recursivement
            recursif(value, cle + key + ".")
        elif isinstance(value, list):
            # Si la valeur est une liste, parcourt ses éléments
            for i, elt in enumerate(value):
                if isinstance(elt, dict):
                    # Si l'élément est un dictionnaire, appelle la fonction recursivement
                    recursif(elt, cle + key + "." + str(i) + ".")
                else:
                    # Sinon ajoute l'élément à la liste
                    liste.append((cle + key + "." + str(i), elt))
        else:
            # Sinon ajoute la valeur à la liste
            liste.append((cle + key, value))

recursif(dictionnaire)
print(liste)

# Sortie: [('a.b.c.0', 'foo'), ('a.b.c.1', 'bar'), ('d.0.oo', 'bar'), ('d.1.kk', 'hello'), ('f.e', 'bar')]


