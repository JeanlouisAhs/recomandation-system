# TP : Recommandation syste, - collaborative filtering : top n
__author__ = "Jean-Loui AHOUANSE, Norbert SOUWOUIN ans Osseni ASSAVIE"
__email__ = "rob@spot.colorado.edu"
__status__ = "Developpement"

# Liens du dépots : https://github.com/JeanlouisAhs/recomandation-system.git
# Dernière version sur la branche dev

import numpy as np


#Création de la matrice

x = int(input("Entrez le nombre de films : "))
y = int(input("Entrez le nombre d'utilisateurs : "))

matrix = np.zeros((x, y))
print("Remplissage la matrice:\n\n")
print("Vous remplirez la matrice ligne par ligne les éléments sont séparés par des virgules\n")
print("Si vous ne mettez aucune note entre deux virgule on considère cette valeur comme inexistante .\n")
print("Ces case vides seront remplacé par 0. Ex : ',2,,2,5' correspond à 'O,2,O,2,5'  \n\n")
for i in range(x):
    row = input("Entrez la ligne {} :  ".format(i+1)).split(",")
    for j in range(y):
        if row[j] != '':
            matrix[i][j] = float(row[j])
        else:
            matrix[i][j] = 0.0

print("Voici la matrice initiale : \n")
print(matrix)

#Demander le n : le top des simularities
n = int(input("Entrez le Top n "))

# Calcul de la matrice de simularité ( ou corrélation)
similarities_matrix = np.corrcoef(matrix)

print("Voici la matrice de simularité : \n")
print(similarities_matrix)


# Remplissage des notes manquantes dans la matrice initiale
for i in range(x):
    for j in range(y):
        if matrix[i][j] == 0:
            similarities = similarities_matrix[i]

            # Les indices des n films les plus similaires
            similar_indices = similarities.argsort()[::-1][1:n+1]

            numerator = 0
            denominator = 0
            for idx in similar_indices:
                # On vérifie si la note donné pour le film idx par l'utilisateur j est différente de zéro
                if matrix[idx][j] != 0:
                    numerator += similarities_matrix[i][idx] * matrix[idx][j]
                    denominator += similarities_matrix[i][idx]
            if denominator != 0:
                matrix[i][j] = numerator / denominator

print("Voici la finale : \n")
print(matrix)