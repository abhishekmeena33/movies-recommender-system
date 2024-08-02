import streamlit as st
import pandas as pd
import pickle
import requests



def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=a89bd48535fad9d4ec39ea960111a56b&language=en-US%27'.format(
            movie_id))

    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        #fetching poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

#Background-Image with css

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://www.pixel4k.com/wp-content/uploads/2019/03/colorful-blur-4k_1551645486.jpg.webp");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.title('Movie Recommender Buddy')

selected_movie_name = st.selectbox(
    "Which movie have you watched?",
    movies['title'].values)

#st.button("Reset", type="primary")
if st.button("Recommend") or st.text_input:
    recommendations, posters = recommend_movies(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.markdown(f'<a href="https://www.google.com/search?q={recommendations[0]}+movie"><img src="{posters[0]}" width="100"></a>',unsafe_allow_html=True)

    with col2:
        st.text(recommendations[1])
        st.markdown(f'<a href="https://www.google.com/search?q={recommendations[1]}+movie"><img src="{posters[1]}" width="100"></a>',unsafe_allow_html=True)

    with col3:
        st.text(recommendations[2])
        st.markdown(f'<a href="https://www.google.com/search?q={recommendations[2]}+movie"><img src="{posters[2]}" width="100"></a>',unsafe_allow_html=True)

    with col4:
        st.text(recommendations[3])
        st.markdown(f'<a href="https://www.google.com/search?q={recommendations[3]}+movie"><img src="{posters[3]}" width="100"></a>',unsafe_allow_html=True)

    with col5:
        st.text(recommendations[4])
        st.markdown(f'<a href="https://www.google.com/search?q={recommendations[4]}+movie"><img src="{posters[4]}" width="100"></a>',unsafe_allow_html=True)
    # for i in range(5):
    #     col = st.columns(5)[i]
    #     with col:
    #         st.text(recommendations[i])
    #         st.markdown(f'<a href="https://www.google.com/search?q={recommendations[i]}"><img src="{posters[i]}" width="100"></a>',unsafe_allow_html=True)