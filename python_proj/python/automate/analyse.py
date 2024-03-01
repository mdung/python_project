import os
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import joblib

def load_json_data(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                json_file_path = os.path.join(root, filename)
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    json_data = json.load(json_file)
                    # Extract relevant text data from the JSON file, adjust as needed
                    text_data = json_data.get('text', '')  # Change 'text' to the actual key containing text
                    category = json_data.get('category', 'Other')  # Change 'category' to the actual key containing category
                    data.append({'Text': text_data, 'Category': category})
    return data

# Specify the folder path containing JSON files
json_folder_path = 'output'

# Load JSON data from the specified folder
data = load_json_data(json_folder_path)

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(df['Text'], df['Category'], test_size=0.2, random_state=42)

# Build a text classification model pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(train_data, train_labels)

# Evaluate the model
predicted_labels = model.predict(test_data)
accuracy = metrics.accuracy_score(test_labels, predicted_labels)
print(f'Model Accuracy: {accuracy}')

# Save the model for future use
joblib.dump(model, 'text_classifier_model.joblib')

# Example of how to use the trained model
new_text = 'Contact us for more information'
predicted_category = model.predict([new_text])[0]
print(f'Predicted Category for "{new_text}": {predicted_category}')
