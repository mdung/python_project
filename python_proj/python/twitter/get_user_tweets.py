import tweepy
from datetime import datetime, timedelta

# Replace these with your Twitter API keys
consumer_key = 'P3yORYItjh41LBJzYXiGeO3Pa'
consumer_secret = 'kZJmJH8I7uIEKxw9YKyuDh9ePJPTScKpHrSnQq8zJgr8Xw4JPI'
access_token = '106404188-CFg5B9pkG8Cbj0nJF5NU4y24XLvyN7NcEP5Hazle'
access_token_secret = 'u7xyiq5UoS6wS6xVHETUdBMwE1EsbafjSzNCXzBbA2DUK'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_user_tweets(username, count=100):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    return tweets

def calculate_engagement(tweets):
    total_likes = sum(tweet.favorite_count for tweet in tweets)
    total_retweets = sum(tweet.retweet_count for tweet in tweets)
    return total_likes + total_retweets

def calculate_average_engagement_per_tweet(tweets):
    return calculate_engagement(tweets) / len(tweets)

def calculate_engagement_over_time(tweets):
    engagement_per_day = {}
    for tweet in tweets:
        date = tweet.created_at.date()
        if date in engagement_per_day:
            engagement_per_day[date] += tweet.favorite_count + tweet.retweet_count
        else:
            engagement_per_day[date] = tweet.favorite_count + tweet.retweet_count
    return engagement_per_day

def main():
    username = input("Enter the Twitter username: ")
    tweet_count = int(input("Enter the number of tweets to analyze: "))

    user_tweets = get_user_tweets(username, tweet_count)

    total_engagement = calculate_engagement(user_tweets)
    avg_engagement_per_tweet = calculate_average_engagement_per_tweet(user_tweets)
    engagement_over_time = calculate_engagement_over_time(user_tweets)

    print("\nAnalysis Results:")
    print(f"Total engagement: {total_engagement}")
    print(f"Average engagement per tweet: {avg_engagement_per_tweet}")
    print("\nEngagement over time:")
    for date, engagement in engagement_over_time.items():
        print(f"{date}: {engagement} engagements")

if __name__ == "__main__":
    main()
