import streamlit as st
import pandas as pd
import pickle
import requests
# from streamlit_lottie import st_lottie

# Function to fetch poster and movie details
def fetch_movie_details(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a89bd48535fad9d4ec39ea960111a56b&language=en-US')
    data = response.json()
    poster_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    overview = data['overview']
    rating = data['vote_average']
    return poster_path, overview, rating

@st.cache_data
def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_details = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        details = fetch_movie_details(movie_id)
        recommended_movies_details.append(details)

    return recommended_movies, recommended_movies_details

# Function to load Lottie animation from URL
def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Background-Image with CSS
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://wallpapercave.com/wp/wp2757874.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

# Load Lottie animations
# lottie_url = "https://lottie.host/5f2dad6b-6646-4c16-bf5d-410b92f227c9/aP0UjbCIXF.json"  # Example URL
# lottie_animation = load_lottieurl(lottie_url)

st.title('Movie Recommender Buddy🎬')
# st_lottie(lottie_animation, height=200, key="header_animation")

selected_movie_name = st.selectbox(
    "Which movie have you watched?",
    movies['title'].values)

# Recommend button and display results
if st.button("Recommend") and selected_movie_name:
    recommendations, details = recommend_movies(selected_movie_name)

    for i, (movie, detail) in enumerate(zip(recommendations, details)):
        st.subheader(movie)
        poster, overview, rating = detail
        st.markdown(f'<a href="https://www.google.com/search?q={movie}+movie"><img src="{poster}" width="200"></a>',
                    unsafe_allow_html=True)
        with st.expander("More Details", expanded=False):
            st.write(f"**Rating:** {rating}")
            st.write(f"**Overview:** {overview}")

