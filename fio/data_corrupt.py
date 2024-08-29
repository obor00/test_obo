# On commence par importer les arguments du programme
import sys

# On récupère les arguments
if len(sys.argv) < 5 or sys.argv[1] == '-h':
    print('Utilisation : python fichier.py fichier_dorigine adresse_byte_modif nouvelle_val_byte fichier_de_sortie')
    sys.exit()

fichier_dorigine = sys.argv[1]
adr_byte_modif = int(sys.argv[2])
nouvelle_val_byte = int(sys.argv[3])
fichier_de_sortie = sys.argv[4]

# On ouvre le fichier d'origine
f = open(fichier_dorigine, 'rb')
data = f.read()
f.close()

# On ecrase le ou les bytes souhaités
data = data[:adr_byte_modif] + bytes([nouvelle_val_byte]) + data[adr_byte_modif + 1:] # On remplace le 11ème byte par un byte nul

# On cree le nouveau fichier 
f = open(fichier_de_sortie, 'wb') # On ouvre le fichier en mode écriture binaire (wb)
f.write(data) # On écrit les données
f.close() # On ferme le fichier
