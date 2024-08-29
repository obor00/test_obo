import matplotlib.pyplot as plt
import numpy as np

#Creer un nouveau document PDF
#pdf = PdfPages('Mon_document.pdf')

#Ajouter un titre
title = "Mon titre"

#Creer un graphique
fig, ax= plt.subplots(8,2)
print(type(ax))
print(type(ax[0,0]))

#Donnees pour le graphique 1
x_data = np.linspace(0, 10, 100)
y_data = 2 * x_data

#Graphique 1
ax[0,0].plot(x_data, y_data, color='red')
ax[0,0].set_title('Ligne droite')
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
#ax[0].set_legend('hello legend')

#Donnees pour le graphique 2
x_data2 = np.linspace(0, 10, 100)
y_data2 = np.sin(x_data2)

#Graphique 2
ax[1,0].plot(x_data2, y_data2, color='blue')
ax[1,0].set_title('Sinusoide')
ax[1,0].set_xlabel('x')
ax[1,0].set_ylabel('y')

#Sauvegarde du graphique dans le PDF
plt.suptitle(title)
plt.show()
#pdf.savefig(fig)

#Fermeture du PDF
#pdf.close()

