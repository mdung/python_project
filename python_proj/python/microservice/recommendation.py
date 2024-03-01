# Install required libraries
# pip install Flask pandas scikit-learn

# recommendation_service.py
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Sample data (replace with your actual dataset)
content_data = {
    'content_id': [1, 2, 3, 4],
    'content_title': ['Article 1', 'Article 2', 'Article 3', 'Article 4'],
    'content_description': ['Description 1', 'Description 2', 'Description 3', 'Description 4']
}

user_data = {
    'user_id': [1, 2, 3],
    'viewed_content': [[1, 2], [2, 3], [1, 3, 4]]
}

# Convert data to DataFrames
content_df = pd.DataFrame(content_data)
user_df = pd.DataFrame(user_data)

# Build content features using TF-IDF
vectorizer = CountVectorizer(stop_words='english')
content_matrix = vectorizer.fit_transform(content_df['content_description'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(content_matrix, content_matrix)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    try:
        data = request.json
        user_id = data.get('user_id')

        if user_id is None or user_id not in user_df['user_id'].values:
            return jsonify({'error': 'Invalid user_id'}), 400

        user_viewed_content = user_df[user_df['user_id'] == user_id]['viewed_content'].iloc[0]

        # Aggregate content scores based on user's viewed content
        content_scores = cosine_sim[user_viewed_content].sum(axis=0)

        # Sort content by scores and recommend the top one
        recommended_content_id = content_scores.argsort()[::-1][0]
        recommendation = content_df[content_df['content_id'] == recommended_content_id][['content_id', 'content_title']].to_dict(orient='records')[0]

        return jsonify({'recommendation': recommendation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
