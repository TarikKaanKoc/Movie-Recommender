import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

# TFIDF_Preprocessing and creating cosine similarity
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

# rec function
def recommendation(movie_title,df,similarity):
    id_of_movie = df[df['title'] == movie_title].index[0]
    distances = similarity[id_of_movie]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    return movie_list

