dictionnaire = {
    "cle1": {
        "sous_cle1": {
            "sous_sous_cle1": "valeur1",
            "sous_sous_cle2": "valeur2"
        },
        "sous_cle2": "valeur3"
    },
    "cle2": "valeur4"
}

# Recherche de la clé
def recherche_cle(dictionnaire, cle_recherchee):
    for cle, valeur in dictionnaire.items():
        if cle == cle_recherchee:
            return valeur

        if isinstance(valeur, dict):
            valeur = recherche_cle(valeur, cle_recherchee)
            if valeur is not None:
                return valeur

# Appel de la fonction
resultat = recherche_cle(dictionnaire, "sous_sous_cle1")

if resultat:
    print(resultat)
else:
    print("Clé non trouvée")

