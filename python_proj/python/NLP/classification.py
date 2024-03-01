import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text data
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    # Tokenize and remove stopwords
    words = word_tokenize(text)
    filtered_words = [ps.stem(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]

    return ' '.join(filtered_words)

# Function to train the text classification model
def train_model(train_texts, train_labels):
    vectorizer = TfidfVectorizer(sublinear_tf=True, encoding='utf-8', decode_error='ignore', stop_words='english')
    train_features = vectorizer.fit_transform(train_texts)

    clf = MultinomialNB()
    clf.fit(train_features, train_labels)

    return vectorizer, clf

# Function to predict category for a given text
def predict_category(text, vectorizer, clf):
    preprocessed_text = preprocess_text(text)
    features = vectorizer.transform([preprocessed_text])
    category = clf.predict(features)[0]
    return category

# GUI callback function
def classify_text():
    input_text = text_input.get("1.0", "end-1c")

    if input_text.strip() == "":
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter some text.")
        result_text.config(state=tk.DISABLED)
        return

    category = predict_category(input_text, vectorizer, clf)

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Predicted Category: {category}")
    result_text.config(state=tk.DISABLED)

# Load your dataset for training here (replace the placeholders)
# For simplicity, let's assume you have a CSV file with 'text' and 'category' columns
# df = pd.read_csv('your_dataset.csv')
# train_texts = df['text'].tolist()
# train_labels = df['category'].tolist()

# Example dataset for demonstration purposes
train_texts = [
    "This is a positive document.",
    "Negative sentiment detected in this text.",
    "The weather is great today!",
    "The stock market is down.",
    "Python programming is fun."
]
train_labels = ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']

vectorizer, clf = train_model(train_texts, train_labels)

# Create the main window
app = tk.Tk()
app.title("Text Classification App")

# Create and place widgets
label = tk.Label(app, text="Enter Text:")
label.pack(pady=5)

text_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=5)
text_input.pack(pady=10)

classify_button = tk.Button(app, text="Classify Text", command=classify_text)
classify_button.pack(pady=5)

result_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=5, state=tk.DISABLED)
result_text.pack(pady=10)

# Start the main loop
app.mainloop()
