# Recommendation system - collaborative filtering (Item to item - top n) using correlation coefficients.


We have simulated this recommendation system by taking the example of films, users and the ratings given by users for these films.

## Process
- The first entry is a matrix of ratings assigned by users for each film.
- The second entry is the top n
- We determine the correlation matrix of movies
- We determine the missing ratings for each user, then we return the complete matrix

## Web Interfaces

To get a more attractive rendering, we designed a web application based on the model using streamlit [streamlit](https://streamlit.io/).
