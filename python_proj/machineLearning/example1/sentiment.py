import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sample data input (replace this with your own social media posts)
social_media_posts = [
    "I had a great day at the beach today!",
    "Feeling down and stressed about work...",
    "Just got a promotion! So excited!",
    "This weather is ruining my weekend plans.",
    "Attended a fantastic concert last night!"
]

# Download necessary resources (only need to run this once)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each social media post
for post in social_media_posts:
    sentiment_scores = sia.polarity_scores(post)
    sentiment = "positive" if sentiment_scores['compound'] > 0 else "negative" if sentiment_scores['compound'] < 0 else "neutral"

    print(f"Text: {post}")
    print(f"Sentiment: {sentiment}")
    print(f"Sentiment Scores: {sentiment_scores}")
    print("-" * 40)
