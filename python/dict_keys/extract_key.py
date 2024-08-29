dictionnaire = {
    'clé1': {
        'sous-clé1': {
            'sous-sous-clé1': 'valeur1',
            'sous-sous-clé2': 'valeur2'
        },
        'sous-clé2': 'valeur3'
    },
    'clé2': 'valeur4'
}

def rechercher_valeur(dictionnaire, clé):
    if clé in dictionnaire:
        return dictionnaire[clé]
    for key in dictionnaire:
        valeur = dictionnaire[key]
        if type(valeur) == dict:
            return rechercher_valeur(valeur, clé)

valeur = rechercher_valeur(dictionnaire, 'sous-sous-clé1')
print(valeur) # 'valeur1'
valeur = rechercher_valeur(dictionnaire, 'sous-clé2')
print(valeur) # 'valeur1'
valeur = rechercher_valeur(dictionnaire, 'xxxxx-clé2')
print(valeur) # 'valeur1'
