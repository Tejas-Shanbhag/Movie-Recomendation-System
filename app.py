import streamlit as st
import sklearn
import numpy as np
import pandas as pd
import pickle
import requests



def fetch_movies(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=e1fa0372ce6262edbbb9881c86a05c05".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+ data['poster_path']


def recommend_movies(new_df,movie_name,similarity_result):
    movie_list_val = []
    movie_id_list = []
    movie_index = new_df[new_df['title'] == movie_name].index[0]
    distances = similarity_result[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key =lambda x : x[1])[1:7]
    for i in movie_list:
       movie_list_val.append(new_df.iloc[i[0]].title)
       movie_id_list.append(new_df.iloc[i[0]].movie_id)
    return movie_list_val,movie_id_list


st.title("Movie Recommendation System")
#st.image('hollywood.jpeg')

movies_df = pickle.load(open('movies.pkl','rb'))
similarity_vectors = pickle.load(open('similarity.pkl','rb'))

movie_name = st.selectbox("Select a Movie to get Recommendations",movies_df['title'].values, index=5)

st.write(" ")
if st.button("Recommend"):
    movie_list,movie_id = recommend_movies(movies_df,movie_name,similarity_vectors)
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        st.text(movie_list[0])
        st.image(fetch_movies(movie_id[0]),use_column_width=True)

    with col2:
        st.text(movie_list[1])
        st.image(fetch_movies(movie_id[1]),use_column_width=True)

    with col3:
        st.text(movie_list[2])
        st.image(fetch_movies(movie_id[2]),use_column_width=True)

    with col4:
        st.text(movie_list[3])
        st.image(fetch_movies(movie_id[3]),use_column_width=True)

    with col5:
        st.text(movie_list[4])
        st.image(fetch_movies(movie_id[4]),use_column_width=True)

    with col6:
        st.text(movie_list[5])
        st.image(fetch_movies(movie_id[5]),use_column_width=True)

