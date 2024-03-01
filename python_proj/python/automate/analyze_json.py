import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read and analyze JSON files
def analyze_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract relevant information (customize based on your criteria)
    url = data.get("URL", "")
    title = data.get("Title", "")
    description = data.get("Description", "")

    # Combine text data for analysis
    text_data = f"{title} {description}"

    return url, text_data

# Function to perform clustering
def cluster_data(text_data_list):
    # Vectorize text data
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(text_data_list)

    # Apply KMeans clustering with explicit n_init setting
    kmeans = KMeans(n_clusters=3, n_init=10)  # Set n_init explicitly to suppress the warning
    kmeans.fit(X)

    # Add cluster labels to the data
    cluster_labels = kmeans.labels_
    clustered_data = list(zip(text_data_list, cluster_labels))

    return clustered_data

# Main function to process files in a folder and generate output
def process_folder(input_folder, output_folder):
    text_data_list = []

    # Iterate through files in the folder and its subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                url, text_data = analyze_json(file_path)
                text_data_list.append(text_data)

    # Perform clustering
    clustered_data = cluster_data(text_data_list)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save clustered data to output files
    for i, (text_data, cluster_label) in enumerate(clustered_data):
        output_file_path = os.path.join(output_folder, f"output_{i+1}_cluster{cluster_label}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text_data)

if __name__ == "__main__":
    input_folder = "output"
    output_folder = "Cluster"
    process_folder(input_folder, output_folder)
