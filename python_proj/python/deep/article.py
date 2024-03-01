import newspaper
from transformers import pipeline

# Function to extract text content from a news article URL
def extract_text_from_url(article_url):
    article = newspaper.Article(article_url)
    article.download()
    article.parse()
    return article.text

# Function to generate a summarized version of the text using deep learning
def generate_summary(text):
    summarization_pipeline = pipeline(task="summarization", model="facebook/bart-large-cnn")
    summary = summarization_pipeline(text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']

# Function to provide personalized news updates based on user preferences
def personalized_news_update(user_interests):
    # Example: user_interests is a list of topics the user is interested in (e.g., ["technology", "health"])
    news_sources = newspaper.build("https://news.ycombinator.com/")

    personalized_updates = []

    for article in news_sources.articles:
        article.download()
        article.parse()

        # Extract article text
        article_text = article.text

        # Generate a summary using deep learning
        summary = generate_summary(article_text)

        # Check if the summary contains keywords of user interest
        if any(interest.lower() in summary.lower() for interest in user_interests):
            personalized_updates.append({
                "title": article.title,
                "summary": summary,
                "url": article.url
            })

    return personalized_updates

if __name__ == "__main__":
    # Example: user_interests is a list of topics the user is interested in (e.g., ["technology", "health"])
    user_interests = ["technology", "health"]

    # Get personalized news updates
    updates = personalized_news_update(user_interests)

    # Print the personalized news updates
    for update in updates:
        print("\nTitle:", update["title"])
        print("Summary:", update["summary"])
        print("URL:", update["url"])
