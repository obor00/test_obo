
import matplotlib.pyplot as plt

# créer un tableau de 3 courbes 
x1 = [1, 2, 3] 
y1 = [2, 4, 1] 
  
x2 = [1, 2, 3] 
y2 = [4, 1, 3] 
  
x3 = [1, 2, 3] 
y3 = [1, 3, 5] 

# créer un figure
fig = plt.figure()

# afficher les 5 graphes
for i in range(5):
    ax = fig.add_subplot(5, 1, i+1)
    ax.plot(x1, y1, label = "Courbe 1") 
    ax.plot(x2, y2, label = "Courbe 2") 
    ax.plot(x3, y3, label = "Courbe 3") 
    ax.legend()
    ax.set_xlabel('x (Unité)')
    ax.set_ylabel('y (Unité)')

# sauvegarder les 5 graphes
plt.savefig("resultat.png")
plt.show()
