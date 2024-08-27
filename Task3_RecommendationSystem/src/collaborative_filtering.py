import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

def load_data():
    interactions = pd.read_csv('data/interactions.csv')
    items = pd.read_csv('data/items.csv')
    return interactions, items

def collaborative_filtering(interactions):
    user_item_matrix = interactions.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
    scaler = StandardScaler()
    scaled_matrix = scaler.fit_transform(user_item_matrix)
    similarity_matrix = cosine_similarity(scaled_matrix)
    return similarity_matrix, user_item_matrix

def recommend_items(user_id, similarity_matrix, user_item_matrix):
    user_index = user_item_matrix.index.get_loc(user_id)
    user_similarities = similarity_matrix[user_index]
    similar_users = user_item_matrix.index[user_similarities.argsort()[::-1]]
    recommendations = user_item_matrix.loc[similar_users].mean(axis=0).sort_values(ascending=False)
    return recommendations

if __name__ == "__main__":
    interactions, items = load_data()
    similarity_matrix, user_item_matrix = collaborative_filtering(interactions)
    user_id = 1
    recommendations = recommend_items(user_id, similarity_matrix, user_item_matrix)
    print(f"Recommendations for User {user_id}:\n{recommendations}")

