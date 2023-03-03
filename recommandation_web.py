# TP : Recommandation syste, - collaborative filtering : top n
__author__ = "Jean-Loui AHOUANSE, Norbert SOUWOUIN and Osseni ASSAVIE"
__status__ = "Developpement"

# Liens du dépots : https://github.com/JeanlouisAhs/recomandation-system.git
# Dernière version sur la branche dev


import streamlit as st
import numpy as np


def recommend_movies(matrix, user_id, n=5):
    # Calcul de la matrice de simularité (ou corrélation)
    similarities_matrix = np.corrcoef(matrix)

    # Notes de l'utilisateur sélectionné
    user_ratings = matrix[:, user_id]

    # Les indices des films déjà notés par l'utilisateur
    rated_indices = np.where(user_ratings > 0)[0]

    # Les indices des films non notés par l'utilisateur
    unrated_indices = np.where(user_ratings == 0)[0]

    # Liste des similitudes entre l'utilisateur et les autres utilisateurs
    similarities = similarities_matrix[:, user_id]

    # Les indices des n utilisateurs les plus similaires
    similar_user_indices = similarities.argsort()[::-1][1:n+1]

    recommendations = []
    for unrated_index in unrated_indices:
        numerator = 0
        denominator = 0
        for similar_user_index in similar_user_indices:
            if matrix[unrated_index][similar_user_index] != 0:
                numerator += similarities[similar_user_index] * matrix[unrated_index][similar_user_index]
                denominator += similarities[similar_user_index]
        if denominator != 0:
            recommendations.append((unrated_index, numerator / denominator))

    # Tri des films recommandés par ordre décroissant de note
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:n]


def main():
    # Demander le nombre de films et le nombre d'utilisateurs
    x = st.number_input("Entrez le nombre de films :", min_value=1, step=1)
    y = st.number_input("Entrez le nombre d'utilisateurs :", min_value=1, step=1)

    # Création de la matrice
    matrix = np.zeros((x, y))

    # Remplissage de la matrice
    st.write("Remplissage de la matrice :")
    st.write("(Mettez chaque ligne de la matrice séparer par des virgules, les cases vides sont remplacé par de zéros )")
    st.write("Ex : 2,0,2,3")
    for i in range(x):
        row = st.text_input(f"Entrez la ligne {i+1} :", value="", key=f"row_{i}")
        values = row.split(",")
        for j in range(y):
            if values[j] != '':
                matrix[i][j] = float(values[j])
            else:
                matrix[i][j] = 0.0

    # Demander le Top n
    n = st.number_input("Entrez le Top n :", min_value=1, step=1)

    # Sélection de l'utilisateur
    user_id = st.selectbox("Sélectionnez un utilisateur :", list(range(y)))

    # Calcul des films recommandés pour l'utilisateur sélectionné
    recommendations = recommend_movies(matrix, user_id, n)

    # Affichage des films recommandés
    st.write(f"Top {n} des films recommandés pour l'utilisateur {user_id} :")
    for recommendation in recommendations:

        # st.write(f"Film {recommendation[0]}  ")
        # st.slider("Note sur 5",min_value=0.0, max_value=5.0, value=recommendation[1], disabled=True)

        st.write(f"Film {recommendation[0]} - note : {recommendation[1]}")

if __name__ == "__main__":
    main()































# import streamlit as st
# import numpy as np
#
# #Création de la matrice
# x = 6
# y = 5
# matrix = np.array([[0, 4, 5, 3, 0],
#                    [5, 4, 0, 0, 2],
#                    [4, 0, 0, 0, 5],
#                    [0, 2, 4, 3, 0],
#                    [0, 0, 5, 0, 4],
#                    [5, 0, 3, 0, 0]])
#
# # Calcul de la matrice de simularité ( ou corrélation)
# similarities_matrix = np.corrcoef(matrix)
#
# # Définir une fonction de recommandation
# def get_recommendations(movie_id, n=5):
#     ratings = matrix[:, movie_id]
#     similar_indices = similarities_matrix[movie_id].argsort()[::-1][1:n+1]
#     similar_ratings = ratings[similar_indices]
#     weights = similarities_matrix[movie_id][similar_indices]
#     mean_rating = np.average(similar_ratings, weights=weights)
#     return mean_rating
#
# # Interface utilisateur Streamlit
# st.title("Système de recommandation de films")
#
# # Demander le film à l'utilisateur
# movie_id = st.selectbox("Sélectionner un film:", [f"Film {i}" for i in range(x)])
#
# # Obtenir des recommandations pour le film sélectionné
# mean_rating = get_recommendations(int(movie_id[-1]))
#
# # Afficher la note moyenne pour les recommandations
# st.write(f"Note moyenne pour les 5 recommandations: {mean_rating}")