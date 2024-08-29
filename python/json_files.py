# Importation de la bibliothèque os
import os

# Création d'un dictionnaire vide
data_dict = {}

# Parcours du dossier pour lire les fichiers JSON
for file in os.listdir('dossier'):
    # Seulement les fichiers JSON sont lus
    if file.endswith(".json"):
        # Ouverture du fichier
        with open(file, "r") as json_file:
            # Chargement des données JSON dans le dictionnaire
            data_dict[file] = json.load(json_file)

# Parcours des données JSON dans le dictionnaire
for key, value in data_dict.items():
    # Assemblage des données JSON par clé
    # ...
