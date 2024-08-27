import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def load_data():
    items = pd.read_csv('data/items.csv')
    return items

def content_based_filtering(items):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(items['genre'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim, items

def recommend_items(item_id, cosine_sim, items):
    idx = items.index[items['item_id'] == item_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    item_indices = [i[0] for i in sim_scores]
    return items.iloc[item_indices]

if __name__ == "__main__":
    items = load_data()
    cosine_sim, items = content_based_filtering(items)
    item_id = 1
    recommendations = recommend_items(item_id, cosine_sim, items)
    print(f"Recommendations for Item {item_id}:\n{recommendations}")

