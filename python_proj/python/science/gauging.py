import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [headline.text.strip() for headline in soup.find_all('h2')]
    return headlines

def analyze_sentiment(headlines):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []

    for headline in headlines:
        sentiment_score = analyzer.polarity_scores(headline)['compound']
        sentiments.append(sentiment_score)

    return sentiments

def plot_sentiment_analysis(headlines, sentiments):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(headlines)), sentiments, color='blue')
    plt.xlabel('News Headlines')
    plt.ylabel('Sentiment Score')
    plt.title('News Sentiment Analysis')
    plt.xticks(range(len(headlines)), headlines, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    # Replace this URL with the news website you want to analyze
    news_url = 'https://www.reuters.com/world'




    # Get news headlines from the specified URL
    headlines = get_news_headlines(news_url)

    # Analyze sentiment of news headlines
    sentiments = analyze_sentiment(headlines)

    # Plot sentiment analysis results
    plot_sentiment_analysis(headlines, sentiments)

if __name__ == "__main__":
    main()
