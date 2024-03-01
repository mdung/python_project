import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

nltk.download('stopwords')

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def preprocess_text(text):
    sentences = nltk.sent_tokenize(text)
    sentence_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return sentences, sentence_tokens

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [word.lower() for word in sent1 if word.isalnum() and word.lower() not in stopwords]
    sent2 = [word.lower() for word in sent2 if word.isalnum() and word.lower() not in stopwords]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in sent1:
        vector1[all_words.index(word)] += 1

    for word in sent2:
        vector2[all_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stopwords):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stopwords)

    return similarity_matrix

def generate_summary(file_path, top_n=5):
    text = read_text(file_path)
    sentences, sentence_tokens = preprocess_text(text)
    stop_words = set(stopwords.words('english'))

    similarity_matrix = build_similarity_matrix(sentence_tokens, stop_words)

    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)

    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

    summary_sentences = [sentence for score, sentence in ranked_sentences[:top_n]]
    summary = ' '.join(summary_sentences)

    return summary

if __name__ == "__main__":
    # Replace 'your_text.txt' with the path to your actual text file
    file_path = 'your_text.txt'
    summary = generate_summary(file_path)

    print("\nOriginal Text:\n")
    print(read_text(file_path))

    print("\nSummary:\n")
    print(summary)
