from surprise.prediction_algorithms.knns import KNNBasic

def model(trainset, based_status):

    #Declaring the similarity options.
    sim_options = {'name': 'cosine',
                   'user_based': based_status}

    # KNN algorithm is used to find similar user - items
    sim_ui = KNNBasic(sim_options=sim_options, verbose=False, random_state=33).fit(trainset)

    return sim_ui


def get_recommendations(data, movie_md, user_id, top_n, algo):
    # creating an empty list to store the recommended product ids
    recommendations = []

    # creating an user item interactions matrix
    user_movie_interactions_matrix = data.pivot(index='userId', columns='movieId', values='rating')

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