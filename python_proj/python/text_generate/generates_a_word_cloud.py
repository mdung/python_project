import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def generate_word_cloud(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    words = [word.lower() for word in words if word.lower() not in stop_words]

    # Join the words back into a single string
    cleaned_text = ' '.join(words)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Example text for testing
    example_text = """
    This is an example text for generating a word cloud. Word clouds are a visual representation of the most
    frequently occurring words in a given text. The script processes the text by tokenizing it, removing stopwords
    and punctuation, and then generates the word cloud. You can customize this script for your own text data.
    """

    generate_word_cloud(example_text)
