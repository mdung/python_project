import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Sample user-item interactions (replace this with your actual dataset)
data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Item1': [5, 4, 0, 2],
    'Item2': [0, 3, 5, 4],
    'Item3': [2, 0, 4, 5],
    'Item4': [4, 0, 3, 0],
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data).set_index('User')

# Function to calculate cosine similarity between users
def calculate_cosine_similarity(dataframe):
    return cosine_similarity(dataframe)

# Function to generate product recommendations for a user
def get_product_recommendations(user, dataframe, similarity_matrix):
    user_ratings = dataframe.loc[user].values.reshape(1, -1)
    similarities = similarity_matrix.dot(user_ratings.T)
    normalized_similarities = similarities / np.abs(similarities).sum(axis=0)
    predicted_ratings = dataframe.values.T.dot(normalized_similarities)

    # Exclude items already rated by the user
    predicted_ratings[user_ratings.flatten() > 0] = 0

    recommendations = pd.Series(predicted_ratings.flatten(), index=dataframe.columns)
    recommendations = recommendations.sort_values(ascending=False)

    return recommendations

# Function to visualize the recommendations as a heatmap
def visualize_recommendations(recommendations):
    plt.figure(figsize=(10, 6))
    sns.heatmap([recommendations.values], annot=True, cmap='YlGnBu', cbar=False, fmt=".1f")
    plt.title('Product Recommendations')
    plt.xlabel('Items')
    plt.ylabel('User')
    plt.show()

# Calculate cosine similarity matrix
cosine_similarity_matrix = calculate_cosine_similarity(df)

# Example: Get product recommendations for 'User1'
user_recommendations = get_product_recommendations('User1', df, cosine_similarity_matrix)

# Visualize the recommendations
visualize_recommendations(user_recommendations)
