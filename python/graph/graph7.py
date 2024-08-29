
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,4,9,16,25]

x2 = [1,2,3,4,5]
y2 = [2,8,18,32,50]

x3 = [1,2,3,4,5]
y3 = [3,12,27,48,75]

# Creation des figures
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12,24))
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

# Premiere courbe
axs[0, 0].plot(x1,y1)
axs[0, 0].plot(x2,y2)
axs[0, 0].plot(x3,y3)
axs[0, 0].set_title("Courbe 1")
axs[0, 0].set_xlabel("x (cm)")
axs[0, 0].set_ylabel("y (cm2)")

# Deuxieme courbe
axs[0, 1].plot(x1,y1)
axs[0, 1].plot(x2,y2)
axs[0, 1].plot(x3,y3)
axs[0, 1].set_title("Courbe 2")
axs[0, 1].set_xlabel("x (cm)")
axs[0, 1].set_ylabel("y (cm2)")

# Troisieme courbe
axs[1, 0].plot(x1,y1)
axs[1, 0].plot(x2,y2)
axs[1, 0].plot(x3,y3)
axs[1, 0].set_title("Courbe 3")
axs[1, 0].set_xlabel("x (cm)")
axs[1, 0].set_ylabel("y (cm2)")

# Quatrieme courbe
axs[1, 1].plot(x1,y1)
axs[1, 1].plot(x2,y2)
axs[1, 1].set_title("Courbe 4")
axs[1, 1].set_xlabel("x (cm)")
axs[1, 1].set_ylabel("y (cm2)")

# Cinquieme courbe
axs[2, 0].plot(x2,y2)
axs[2, 0].plot(x3,y3)
axs[2, 0].set_title("Courbe 5")
axs[2, 0].set_xlabel("x (cm)")
axs[2, 0].set_ylabel("y (cm2)")

# Sauvegarde des figures
fig.savefig("resultat.png")

# Affichage des figures
plt.show()
