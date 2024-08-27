from collaborative_filtering import recommend_items as cf_recommend
from content_based_filtering import recommend_items as cb_recommend
import pandas as pd

def main():
    # Collaborative Filtering
    interactions, items = pd.read_csv('data/interactions.csv'), pd.read_csv('data/items.csv')
    similarity_matrix, user_item_matrix = cf_recommend(interactions)
    user_id = 1
    cf_recommendations = cf_recommend(user_id, similarity_matrix, user_item_matrix)
    print(f"Collaborative Filtering Recommendations for User {user_id}:\n{cf_recommendations}")

    # Content-Based Filtering
    cosine_sim, items = cb_recommend(items)
    item_id = 1
    cb_recommendations = cb_recommend(item_id, cosine_sim, items)
    print(f"Content-Based Filtering Recommendations for Item {item_id}:\n{cb_recommendations}")

if __name__ == "__main__":
    main()

