import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Initialize the global vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Function to read and analyze JSON files
def analyze_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract relevant information for analysis
    url = data.get("URL", "")
    title = data.get("Title", "")
    description = data.get("Description", "")

    # Combine text data for analysis
    text_data = f"{title} {description}"

    return url, text_data

# Function to build a content-based recommendation system
def build_recommendation_system(text_data_list):
    # Vectorize text data
    X = vectorizer.fit_transform(text_data_list)

    # Calculate similarity matrix
    similarity_matrix = linear_kernel(X, X)

    return similarity_matrix

# Function to get recommended URLs based on user preferences
def get_recommendations(user_preferences, text_data_list, similarity_matrix, urls, vectorizer):
    # Vectorize user preferences
    user_vector = vectorizer.transform([user_preferences])

    # Calculate similarity between user preferences and URLs
    similarity_scores = linear_kernel(user_vector, similarity_matrix).flatten()

    # Get indices of URLs sorted by similarity score
    url_indices = similarity_scores.argsort()[::-1]

    # Get recommended URLs
    recommendations = [(urls[i], similarity_scores[i]) for i in url_indices]

    return recommendations

# Main function to process files in a folder and generate recommendations
def process_folder(input_folder, user_preferences, output_folder):
    text_data_list = []
    urls = []

    # Iterate through files in the folder and its subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                url, text_data = analyze_json(file_path)
                urls.append(url)
                text_data_list.append(text_data)

    # Build content-based recommendation system
    similarity_matrix = build_recommendation_system(text_data_list)

    # Get recommendations based on user preferences
    recommendations = get_recommendations(user_preferences, text_data_list, similarity_matrix, urls, vectorizer)

    # Save recommendations to individual output files
    for i, (recommended_url, similarity_score) in enumerate(recommendations):
        output_file_path = os.path.join(output_folder, f"recommendations_{i+1}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Recommended URL: {recommended_url} (Similarity Score: {similarity_score})\n")

if __name__ == "__main__":
    input_folder = "output"
    user_preferences = "Your user preferences go here"
    output_folder = "recommendations"
    process_folder(input_folder, user_preferences, output_folder)
