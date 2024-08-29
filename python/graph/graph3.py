import matplotlib.pyplot as plt
import numpy as np

# Générer des données pour les courbes
x1 = np.linspace(0, 10, 50)
y1 = np.cos(x1)
x2 = np.linspace(0, 10, 50)
y2 = np.sin(x2)

# Créer un graphe et ajouter des courbes
plt.title("Plusieurs courbes sur le même graphe")
plt.xlabel("Axe des abcisses")
plt.ylabel("Axe des ordonnées")
plt.plot(x1, y1, label="Courbe 1")
plt.plot(x2, y2, label="Courbe 2")
plt.legend()
plt.savefig("graphe.png")
# plt.show()
