import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Set up Twitter API credentials
consumer_key = 'P3yORYItjh41LBJzYXiGeO3Pa'
consumer_secret = 'kZJmJH8I7uIEKxw9YKyuDh9ePJPTScKpHrSnQq8zJgr8Xw4JPI'
access_token = '106404188-CFg5B9pkG8Cbj0nJF5NU4y24XLvyN7NcEP5Hazle'
access_token_secret = 'u7xyiq5UoS6wS6xVHETUdBMwE1EsbafjSzNCXzBbA2DUK'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_sentiment(tweet_text):
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(tweet_text)

    # Classify sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def plot_sentiment_distribution(sentiments):
    labels = list(sentiments.keys())
    sizes = list(sentiments.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'red', 'gray'])
    plt.title("Sentiment Distribution of Tweets")
    plt.show()

def main():
    # Fetch tweets from your timeline
    tweets = api.home_timeline(count=100)

    # Analyze sentiment for each tweet
    sentiment_count = {'positive': 0, 'negative': 0, 'neutral': 0}

    for tweet in tweets:
        tweet_text = tweet.text
        sentiment = analyze_sentiment(tweet_text)
        sentiment_count[sentiment] += 1

    # Plot sentiment distribution
    plot_sentiment_distribution(sentiment_count)

if __name__ == "__main__":
    main()
