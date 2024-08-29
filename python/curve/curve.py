import math
import matplotlib.pyplot as plt

def calculate_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def eliminer_points_eloignes(points, courbe, distance_max):
    # Cette fonction élimine les points de la liste 'points' qui sont à une distance
    # supérieure à 'distance_max' de la courbe 'courbe'.
    points_elimines = []

    for point in points:
        distance_minimale = float("inf")

        # Parcourir les points de la courbe pour trouver la distance minimale
        for point_courbe in courbe:
            distance = calculate_distance(point, point_courbe)
            distance_minimale = min(distance_minimale, distance)

        # Si la distance minimale est inférieure ou égale à la distance maximale autorisée,
        # conserver le point, sinon l'éliminer
        if distance_minimale <= distance_max:
            points_elimines.append(point)

    return points_elimines

# Exemple d'utilisation avec une visualisation graphique :
courbe = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
points = [(0, 0), (1.5, 1.5), (2.5, 2.5), (5.5, 5.5)]
points += [(1, 2), (3, 2), (1.2,3), (1.7,5)]
distance_max = 1.0  # Ajustez cette distance en conséquence

# Appeler la fonction pour éliminer les points éloignés
points_filtrés = eliminer_points_eloignes(points, courbe, distance_max)

# Créer des listes séparées pour les coordonnées X et Y des points
x_courbe, y_courbe = zip(*courbe)
x_points, y_points = zip(*points)
x_points_filtrés, y_points_filtrés = zip(*points_filtrés)

# Créer un graphique pour visualiser la courbe et les points éliminés
plt.figure(figsize=(8, 6))
plt.plot(x_courbe, y_courbe, label='Courbe de référence')
plt.scatter(x_points, y_points, color='red', marker='x', label='Points éloignés')
plt.scatter(x_points_filtrés, y_points_filtrés, color='green', marker='o', label='Points conservés')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Élimination des points éloignés de la courbe')
plt.grid(True)
plt.show()

