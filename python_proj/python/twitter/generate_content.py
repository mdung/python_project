import tweepy
import openai
import schedule
import time

# Set up your Twitter API credentials
consumer_key = 'P3yORYItjh41LBJzYXiGeO3Pa'
consumer_secret = 'kZJmJH8I7uIEKxw9YKyuDh9ePJPTScKpHrSnQq8zJgr8Xw4JPI'
access_token = '106404188-CFg5B9pkG8Cbj0nJF5NU4y24XLvyN7NcEP5Hazle'
access_token_secret = 'u7xyiq5UoS6wS6xVHETUdBMwE1EsbafjSzNCXzBbA2DUK'

# Set up your OpenAI API key
openai.api_key = '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'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate content using GPT-3
def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to post a tweet
def post_tweet(content):
    api.update_status(content)

# Function to create a scheduled tweet
def schedule_tweet():
    prompt = "Generate a tweet about"
    generated_content = generate_content(prompt)

    # Post the generated content as a tweet
    post_tweet(generated_content)

# Schedule tweets every 6 hours (adjust as needed)
schedule.every(6).hours.do(schedule_tweet)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
