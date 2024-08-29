import matplotlib.pyplot as plt

# donnees pour la courbe 1
x1 = [1,2,3,4,5]
y1 = [5,4,3,2,1]

# donnees pour la courbe 2
x2 = [1,2,3,4,5]
y2 = [1,2,3,4,5]

# donnees pour la courbe 3
x3 = [1,2,3,4,5]
y3 = [2,4,6,8,10]

# Creation du graphe
plt.plot(x1,y1, label='Courbe 1')
plt.plot(x2,y2, label='Courbe 2')
plt.plot(x3,y3, label='Courbe 3')

# Legendes
plt.xlabel('Abscisse')
plt.ylabel('Ordonnee')
plt.title('Mon graphe')
plt.legend()

# Enregistrer le graphe au format PNG
plt.savefig('multiple_plots2.png')
