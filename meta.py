meta = """
        def preprocessing(df_metadata,df_keywords,df_credits):

        df_metadata = df_metadata[df_metadata['vote_count'] >= 55]
        movie_md = df_metadata[['id','original_title','overview','genres']]
        movie_md['title'] = movie_md['original_title']
        movie_md.reset_index(inplace=True, drop=True)
        df_credits = df_credits[["id","cast"]]

        movie_md = movie_md[movie_md['id'].str.isnumeric()] # removes the columns which has no id

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

        # Create, tags feature
        df['tags'] = df['overview'] + ' ' + df['genres'] +  ' ' + df['original_title'] + ' ' + df['keywords'] + ' ' + df['cast']
        # Delete useless columns
        df.drop(['original_title', 'overview', 'genres', 'keywords', 'cast'], inplace=True, axis=1)

        df.drop(df[df['tags'].isnull()].index, inplace=True,axis=0)
        df.drop_duplicates(inplace=True)

        return df
        """

meta2 = """
        df['tags'] = df['overview'] + ' ' + df['genres'] +  ' ' + df['original_title'] + ' ' + df['keywords'] + ' ' + df['cast']
        """

meta3 = """
        def cosine_sim(df):

        # Initialize a tfidf object
        tfidf = TfidfVectorizer(max_features=5000)
        # Transform the data
        vectorized_data = tfidf.fit_transform(df['tags'].values)
        vectorized_dataframe = pd.DataFrame(vectorized_data.toarray(), index=df['tags'].index.tolist())

        # Initialize a PCA object
        svd = TruncatedSVD(n_components=3000)
        # Fit transform the data
        reduced_data = svd.fit_transform(vectorized_dataframe)
        similarity = cosine_similarity(reduced_data)

        return similarity
        """

meta4 = """
        def mb_mb_preprocessing(df_mm,ratings):     

    df_mm = df_mm[df_mm['vote_count']>100][['id','title']]


    movie_ids = [int(x) for x in df_mm['id'].values]

   
    ratings = ratings[ratings['movieId'].isin(movie_ids)]

    # Reset Index
    ratings.reset_index(inplace=True, drop=True)

    # Initialize a surprise reader object
    reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 5), skip_lines=1)

    # Load the data
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader=reader)

    # Build trainset object(perform this only when you are using whole data to train)
    trainset = data.build_full_trainset()

    return trainset
       """

meta5 = """
def get_recommendations(ratings, movie_md, user_id, top_n, algo):
    # creating an empty list to store the recommended product ids
    recommendations = []

    # creating an user item interactions matrix
    user_movie_interactions_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')

    # extracting those product ids which the user_id has not interacted yet
    non_interacted_movies = user_movie_interactions_matrix.loc[user_id][
    user_movie_interactions_matrix.loc[user_id].isnull()].index.tolist()

    # looping through each of the product ids which user_id has not interacted yet
    for item_id in non_interacted_movies:
        # predicting the ratings for those non interacted product ids by this user
        est = algo.predict(user_id, item_id).est

        # appending the predicted ratings
        movie_name = movie_md[movie_md['id'] == str(item_id)]['title'].values[0]
        recommendations.append((movie_name, est))

    # sorting the predicted ratings in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:top_n]  # returing top n highest predicted rating products for this user
        """

meta6 = """
        def model(trainset, based_status):

    #Declaring the similarity options.
    sim_options = {'name': 'cosine',
                   'user_based': based_status}

    # KNN algorithm is used to find similar user - items
    sim_ui = KNNBasic(sim_options=sim_options, verbose=False, random_state=33).fit(trainset)

    return sim_ui

        """

meta7 = """
def search(result):
    movie_name = []
    yt_url = []

    for i in result:
        title = [i][0][0]
        movie_name.append(title)
        result = YoutubeSearch(title + "Trailer", max_results=1).to_json()
        get_yt_key = result.split(",")[-1][16:36]
        yt_url.append("https://www.youtube.com" + get_yt_key)

    return movie_name, yt_url

        """

meta8 = """
def get_details(df_mm,yt_url,movie_name):

    for temp in range(len(yt_url)):
        with st.container():
            # columns for show details
            left_col, right_col = st.columns(2)
            with left_col:
                # youtube video - left column
                st.video(yt_url[temp])
            with right_col:
                # movie details - rigth column
                movie_title = list(df_mm[df_mm["title"] == movie_name[temp]].title)
                st.subheader(movie_title[0])
                movie_overview = list(df_mm[df_mm["title"] == movie_name[temp]].overview)
                st.write(movie_overview[0])
                movie_genres = list(df_mm[df_mm["title"] == movie_name[temp]].genres)
                st.write(movie_genres)
                imdb_id = list(df_mm[df_mm["title"] == movie_name[temp]].imdb_id)
               ## st.markdown(f
                    [![IMDB](https://img.shields.io/badge/IMDb-F5C518.svg?style=for-the-badge&logo=IMDb&logoColor=black)](https://www.imdb.com/title/{imdb_id[0]}/)
                   )
        """
