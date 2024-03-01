# Import necessary libraries
from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Flask app
app = Flask(__name__)

# Initialize NLTK Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Define a route for sentiment analysis
@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        # Get the text from the request
        data = request.get_json()
        text = data['text']

        # Perform sentiment analysis
        sentiment_score = sia.polarity_scores(text)

        # Determine sentiment label based on the compound score
        if sentiment_score['compound'] >= 0.05:
            sentiment_label = 'positive'
        elif sentiment_score['compound'] <= -0.05:
            sentiment_label = 'negative'
        else:
            sentiment_label = 'neutral'

        # Prepare the response
        response = {
            'text': text,
            'sentiment': {
                'label': sentiment_label,
                'score': sentiment_score['compound']
            }
        }

        # Return the response as JSON
        return jsonify(response)

    except Exception as e:
        # Handle errors and return an error response
        error_response = {'error': str(e)}
        return jsonify(error_response), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
