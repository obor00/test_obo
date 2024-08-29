dictionnaire = {
    'clé1' : {
        'clé2' : {
            'clé3' : 'valeur1',
            'clé4' : 'valeur2'
        },
        'clé5' : 'valeur3'
    },
    'clé6' : 'valeur4'
}

# Liste des clés prédéfinies
liste_clés = ['clé1', 'clé2', 'clé3', 'cle5']

# Déclaration du dictionnaire final
dict_final = {}

# Parcours récursif du dictionnaire
def parcours_dict(dict_courant, clés):
    # Si le dictionnaire courant est vide, on arrête le parcours
    if dict_courant == {}:
        return

    # On récupère la première clé
    clé_courante = clés.pop(0)

    # Si la clé existe dans le dictionnaire courant
    if clé_courante in dict_courant:
        # Si c'est la dernière clé
        if len(clés) == 0:
            dict_final[clé_courante] = dict_courant[clé_courante]
        # Sinon, on continue le parcours
        else:
            parcours_dict(dict_courant[clé_courante], clés)

# On démarre le parcours récursif
parcours_dict(dictionnaire, liste_clés)

# Affichage du résultat
print(dict_final)
