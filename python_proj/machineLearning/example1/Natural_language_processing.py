import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Sample data input (replace this with your own text)
text = "Natural language processing is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."

# Download necessary resources (only need to run this once)
nltk.download('punkt')
nltk.download('stopwords')

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation and convert to lowercase
tokens = [word.lower() for word in tokens if word.isalpha()]

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Print processed tokens
print(stemmed_tokens)
