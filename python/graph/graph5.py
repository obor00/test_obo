
import matplotlib.pyplot as plt

# Graphe 1 
x1 = [1,2,3]
y1_1 = [1,4,1]
y1_2 = [3,2,6]
y1_3 = [2,3,5]

plt.plot(x1,y1_1, label = "Courbe 1")
plt.plot(x1,y1_2, label = "Courbe 2")
plt.plot(x1,y1_3, label = "Courbe 3")

plt.xlabel("Echelle (Unités)")
plt.ylabel("Valeur (Unités)")
plt.legend()

# Graphe 2 
x2 = [1,2,3]
y2_1 = [2,5,1]
y2_2 = [4,2,3]
y2_3 = [1,4,2]

plt.plot(x2,y2_1, label = "Courbe 1")
plt.plot(x2,y2_2, label = "Courbe 2")
plt.plot(x2,y2_3, label = "Courbe 3")

plt.xlabel("Echelle (Unités)")
plt.ylabel("Valeur (Unités)")
plt.legend()

# Graphe 3 
x3 = [1,2,3]
y3_1 = [4,3,2]
y3_2 = [2,4,1]
y3_3 = [3,1,2]

plt.plot(x3,y3_1, label = "Courbe 1")
plt.plot(x3,y3_2, label = "Courbe 2")
plt.plot(x3,y3_3, label = "Courbe 3")

plt.xlabel("Echelle (Unités)")
plt.ylabel("Valeur (Unités)")
plt.legend()

# Graphe 4 
x4 = [1,2,3]
y4_1 = [2,3,4]
y4_2 = [5,1,2]
y4_3 = [4,2,3]

plt.plot(x4,y4_1, label = "Courbe 1")
plt.plot(x4,y4_2, label = "Courbe 2")
plt.plot(x4,y4_3, label = "Courbe 3")

plt.xlabel("Echelle (Unités)")
plt.ylabel("Valeur (Unités)")
plt.legend()

# Graphe 5 
x5 = [1,2,3]
y5_1 = [4,2,3]
y5_2 = [1,4,2]
y5_3 = [3,1,4]

plt.plot(x5,y5_1, label = "Courbe 1")
plt.plot(x5,y5_2, label = "Courbe 2")
plt.plot(x5,y5_3, label = "Courbe 3")

plt.xlabel("Echelle (Unités)")
plt.ylabel("Valeur (Unités)")
plt.legend()

plt.savefig('graphes.png')
