import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

def text_summarization(text, num_sentences=5):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(filtered_words)

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word.lower() in sentence.lower():
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq
                else:
                    sentence_scores[sentence] += freq

    # Select the top N sentences with highest scores
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Detokenize the selected sentences to form the summary
    summary = TreebankWordDetokenizer().detokenize(summary_sentences)

    return summary

if __name__ == "__main__":
    # Example text for testing
    example_text = """
    Text summarization is the process of distilling the most important information from a source to produce a shortened version. 
    There are two main approaches to text summarization: extractive and abstractive. Extractive summarization involves selecting 
    and combining existing sentences to form a summary, while abstractive summarization generates new sentences to convey the 
    main ideas. This script implements an extractive text summarization tool using natural language processing techniques.
    It uses the nltk library for tokenization, stop-word removal, and frequency analysis to identify the most important sentences
    in the given text. The number of sentences in the final summary can be adjusted by changing the 'num_sentences' parameter.
    """

    # Set the number of sentences in the summary
    num_sentences_in_summary = 3

    # Generate the summary
    summary = text_summarization(example_text, num_sentences=num_sentences_in_summary)

    # Print the summary
    print("Original Text:\n", example_text)
    print("\nSummary:\n", summary)
