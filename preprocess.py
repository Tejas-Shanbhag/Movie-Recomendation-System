
import numpy as np
import re
import pandas as pd
import ast
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from utils import convert_genres, convert_cast, get_director, stem_text


movies_df = pd.read_csv('tmdb_5000_movies.csv')
credits_df = pd.read_csv('tmdb_5000_credits.csv')


movies = movies_df.merge(credits_df, on='title')

req_cols = ['genres','movie_id','keywords','title','overview','cast','crew']
movies = movies[req_cols].dropna()


movies['genres'] = movies['genres'].apply(convert_genres)
movies['keywords'] = movies['keywords'].apply(convert_genres)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(get_director)
movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])


movies['tags'] = movies['overview']+ movies['genres']+ movies['keywords'] + movies['cast'] + movies['crew']

new_df= movies[['movie_id','title','tags']]
new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())


cv = CountVectorizer(max_features=5000,stop_words='english')
final_vectors = cv.fit_transform(new_df['tags'])

similarity_result = cosine_similarity(final_vectors)

pickle.dump(new_df,open('movies.pkl','wb'))
pickle.dump(similarity_result,open('similarity.pkl','wb'))





