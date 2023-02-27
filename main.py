import numpy as np

# Press the green button in the gutter to run the script.

#Création de la matrice

x = int(input("Entrez le nombre de films de la matrice: "))
y = int(input("Entrez le nombre d'utilisateurs de la matrice: "))

matrix = np.zeros((x, y))
print("Remplissez la matrice:")
# for i in range(x):
#     for j in range(y):
#         matrix[i][j] = float(input("Entrez la valeur de la case ({}, {}): ".format(i+1, j+1)))

# for i in range(x):
#     row = input("Entrez la ligne {} séparée par des virgules: ".format(i+1)).split(",")
#     for j in range(y):
#         matrix[i][j] = float(row[j])

for i in range(x):
    row = input("Entrez la ligne {} séparée par des virgules: ".format(i+1)).split(",")
    for j in range(y):
        if row[j] != '':
            matrix[i][j] = float(row[j])
        else:
            matrix[i][j] = 0.0

print(matrix)

#Demander le n : le top des simularities
n = int(input("Entrez le Top n "))

# Calcul de la matrice de corrélation
corr_matrix = np.corrcoef(matrix)

print(corr_matrix)


# Remplissage des notes manquantes dans la matrice initiale
for i in range(x):
    for j in range(y):
        if matrix[i][j] == 0:
            similarities = corr_matrix[i]
            similar_indices = similarities.argsort()[::-1][1:n+1] # Les indices des n films les plus similaires
            numerator = 0
            denominator = 0
            for idx in similar_indices:
                if matrix[idx][j] != 0:
                    numerator += corr_matrix[i][idx] * matrix[idx][j]
                    denominator += corr_matrix[i][idx]
            if denominator != 0:
                matrix[i][j] = numerator / denominator

print(matrix)