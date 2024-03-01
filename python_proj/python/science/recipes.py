import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data (you should replace this with your actual recipe dataset)
recipes_data = {
    'RecipeID': [1, 2, 3, 4],
    'Title': ['Pasta Carbonara', 'Vegetable Stir-Fry', 'Grilled Chicken Salad', 'Vegetarian Chili'],
    'Ingredients': ['pasta, eggs, bacon, Parmesan cheese', 'vegetables, tofu, soy sauce, ginger', 'chicken, lettuce, tomatoes, dressing', 'beans, tomatoes, onions, spices'],
    'DietaryPreferences': ['Non-Vegetarian', 'Vegetarian', 'Non-Vegetarian', 'Vegetarian']
}

user_preferences = {
    'DietaryPreferences': 'Vegetarian'
}

# Create a DataFrame from the sample data
recipes_df = pd.DataFrame(recipes_data)

# Preprocess the data
recipes_df['Ingredients'] = recipes_df['Ingredients'].str.lower()
recipes_df['DietaryPreferences'] = recipes_df['DietaryPreferences'].str.lower()

# Filter recipes based on user preferences
filtered_recipes = recipes_df[recipes_df['DietaryPreferences'] == user_preferences['DietaryPreferences']]

# Create a TF-IDF vectorizer to convert ingredients into a matrix of TF-IDF features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_recipes['Ingredients'])

# Calculate the cosine similarity between recipes
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recipe recommendations
def get_recommendations(recipe_title, cosine_similarities=cosine_similarities):
    recipe_index = filtered_recipes[filtered_recipes['Title'] == recipe_title].index[0]
    similar_recipes = list(enumerate(cosine_similarities[recipe_index]))
    similar_recipes = sorted(similar_recipes, key=lambda x: x[1], reverse=True)
    similar_recipes = similar_recipes[1:4]  # Exclude the recipe itself and get top 3 recommendations

    recommended_recipe_indices = [index for index, _ in similar_recipes]
    recommended_recipes = filtered_recipes.iloc[recommended_recipe_indices]['Title'].tolist()

    return recommended_recipes

# Example: Get recipe recommendations for a specific recipe
recipe_title = 'Vegetable Stir-Fry'
recommendations = get_recommendations(recipe_title)

# Print the recommendations
print(f"Recommendations for '{recipe_title}': {recommendations}")
