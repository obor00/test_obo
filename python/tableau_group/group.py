import pandas as pd

# charger le tableau
data = pd.read_csv("data.csv")
print(data)

#print (data['rwmixread'].dtype)
# grouper par rwmixread, rwtype et bs
grouped_data = data.groupby(by=['rwmixread','rwtype', 'bs'])

# définir un dictionnaire pour stocker les valeurs
stats_dict = {}

# boucler sur les groupes
for name, group in grouped_data:
    # calculer min, max et moyenne
    min_readbw = group['readbw'].min()
    max_readbw = group['readbw'].max()
    mean_readbw = group['readbw'].mean()
    min_writebw = group['writebw'].min()
    max_writebw = group['writebw'].max()
    mean_writebw = group['writebw'].mean()

    # ajouter les valeurs au dictionnaire
    stats_dict[name] = {
        'min_readbw': min_readbw,
        'max_readbw': max_readbw,
        'mean_readbw': mean_readbw,
        'min_writebw': min_writebw,
        'max_writebw': max_writebw,
        'mean_writebw': mean_writebw,
    }

# construire un nouveau tableau
new_data = []
for index, row in data.iterrows():
    key = (row['rwmixread'], row['rwtype'], row['bs'])
    # ajouter les valeurs min, max et moyenne
    row['min,max,moyenne'] = stats_dict[key]
    new_data.append(row)

# sauvegarder le nouveau tableau
new_data = pd.DataFrame(new_data)
new_data.to_csv('new_data.csv', index=False)
