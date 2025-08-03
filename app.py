import pickle
import streamlit as st
import requests
import pandas as pd
import time

#https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
@st.cache_data
def fetch_poster(movie_id) :
  url =  f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=98624a25b9c16a0adec84939b3f26d9c&language=en-US"
  print("Fetching URL:", url)  # DEBUG line
  for attempt in range(3):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Will raise HTTPError if not 200
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "http://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/300x450?text=No+Poster"
        except Exception as e:
            print(f"[Attempt {attempt+1}] Failed to fetch poster: {e}")
            time.sleep(1)
    
  return "https://via.placeholder.com/300x450?text=API+Error"



def recommend(movie) :
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True , key = lambda x : x[1])
    recommended_movies_name = []
    recommended_movies_poster = [] 
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        time.sleep(0.5) 
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster



st.header("Movie Recommendation System")
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similary.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or Select a Movie',
    movie_list
)

if st.button('show recommendation'):
    recommended_movies_name , recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1 :
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2 :
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3 :
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4 :
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with col5 :
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])