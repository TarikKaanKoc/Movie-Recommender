import streamlit as st
import pandas as pd
from surprise import Dataset, Reader
import json
########################################## Load Data #############################################

@st.cache(allow_output_mutation=True)
def load_data():

    credits = pd.read_csv("data/credits.csv", low_memory=False)
    keywords = pd.read_csv("data/keywords.csv")
    mm = pd.read_csv("data/movies_metadata.csv",
                     low_memory=False)
    ratings = pd.read_csv("data/ratings.csv")
    small_ratings = pd.read_csv("data/ratings_small.csv")

    return credits, keywords, mm, ratings, small_ratings


########################################## Content-Based Filtering ##########################################
def preprocessing(df_mm,df_keywords,df_credits):

    df_mm = df_mm[df_mm['vote_count'] >= 55]
    df_mm = df_mm[['id','original_title','overview','genres']]
    df_mm['title'] = df_mm['original_title'].copy()
    df_mm.reset_index(inplace=True, drop=True)
    df_credits = df_credits[["id","cast"]]

    movie_md = df_mm[df_mm['id'].str.isnumeric()] # removes the columns which has no id

    movie_md['id'] = movie_md['id'].astype(int)
    df = pd.merge(movie_md, df_keywords, on='id', how='left')
    df.reset_index(inplace=True, drop=True)

    df = pd.merge(df, df_credits, on='id', how='left')
    df.reset_index(inplace=True, drop=True)

    df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in eval(x)])
    df['genres'] = df['genres'].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

    df['keywords'].fillna('[]', inplace=True)

    df['keywords'] = df['keywords'].apply(lambda x: [i['name'] for i in eval(x)])
    df['keywords'] = df['keywords'].apply(lambda x: ' '.join([i.replace(" ",'') for i in x]))

    df['cast'].fillna('[]', inplace=True)

    df['cast'] = df['cast'].apply(lambda x: [i['name'] for i in eval(x)])
    df['cast'] = df['cast'].apply(lambda x: ' '.join([i.replace(" ",'') for i in x]))

    df['tags'] = df['overview'] + ' ' + df['genres'] +  ' ' + df['original_title'] + ' ' + df['keywords'] + ' ' + df['cast']
    # Delete useless columns
    df.drop(['original_title', 'overview', 'genres', 'keywords', 'cast'], inplace=True, axis=1)
    df.drop(df[df['tags'].isnull()].index, inplace=True,axis=0)
    df.drop_duplicates(inplace=True)

    return df

# model based  and memory based preprocessing
def mb_mb_preprocessing(movie_md,ratings):

    # movie dataframe with votes more than 55
    movie_md = movie_md[movie_md['vote_count']>55][['id','title']]

    # IDs of movies with count more than 55
    movie_ids = [int(x) for x in movie_md['id'].values]

    # Select ratings of movies with more than 55 counts
    ratings = ratings[ratings['movieId'].isin(movie_ids)]

    # Reset Index
    ratings.reset_index(inplace=True, drop=True)

    # Initialize a surprise reader object
    reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 5), skip_lines=1)

    # Load the data
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader=reader)

    # Build trainset object(perform this only when you are using whole data to train)
    trainset = data.build_full_trainset()

    return trainset, ratings, movie_md

def get_details(df_mm,yt_url,movie_name):
    
    df = df_mm.copy()
    df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in eval(x)])
    df['genres'] = df['genres'].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

    
    # for temp in range(len(yt_url)):
    #     with st.container():
    #         # columns for show details
    #         left_col, right_col = st.columns(2)
    #         with left_col:
    #             print("Debug col - left")
    #             # youtube video - left column
    #             st.video(yt_url[temp])
    #         with right_col:
    #             print("Debug col - right")
    #             # movie details - rigth column
    #             movie_title = list(df_mm[df_mm["title"] == movie_name[temp]].title) 
    #             print(movie_title)
    #             st.subheader(movie_title[0])
    #             print("subheader right column")
    #             movie_overview = list(df_mm[df_mm["title"] == movie_name[temp]].overview)
    #             st.write(movie_overview[0])
    #             movie_genres = list(df_mm[df_mm["title"] == movie_name[temp]].genres)
    #             st.write(movie_genres)
    #             imdb_id = list(df_mm[df_mm["title"] == movie_name[temp]].imdb_id)
    #             st.markdown(f"""
    #                 [![IMDB](https://img.shields.io/badge/IMDb-F5C518.svg?style=for-the-badge&logo=IMDb&logoColor=black)](https://www.imdb.com/title/{imdb_id[0]}/)
    #                 """)


    for temp in range(len(yt_url)):
        with st.container():
            # columns for show details
            left_col, right_col = st.columns(2)
            with left_col:
                print("Debug col - left")
                # youtube video - left column
                st.video(yt_url[temp])
            with right_col:
                print("Debug col - right")
                # movie details - rigth column
                movie_title = list(df_mm[df_mm["title"] == movie_name[temp]].title) 
                print(movie_title)
                st.subheader(movie_title[0])
                print("subheader right column")
                movie_overview = list(df_mm[df_mm["title"] == movie_name[temp]].overview)
                st.write(movie_overview[0])
                movie_genres = list(df_mm[df_mm["title"] == movie_name[temp]].genres)                
                st.write(movie_genres)
                imdb_id = list(df_mm[df_mm["title"] == movie_name[temp]].imdb_id)
            
                st.markdown(f"""
                    [![IMDB](https://img.shields.io/badge/IMDb-F5C518.svg?style=for-the-badge&logo=IMDb&logoColor=black)](https://www.imdb.com/title/{imdb_id[0]}/)
                    """)