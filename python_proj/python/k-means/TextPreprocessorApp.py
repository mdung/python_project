import tkinter as tk
from tkinter import Text, Scrollbar, END
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources (run this once if not already done)
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

class TextPreprocessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Preprocessor App")

        # Create UI elements
        self.text_input = Text(root, wrap="word", width=40, height=10)
        self.scrollbar = Scrollbar(root, command=self.text_input.yview)
        self.text_input.config(yscrollcommand=self.scrollbar.set)

        self.preprocessed_display = Text(root, wrap="word", state=tk.DISABLED, width=40, height=10)

        self.process_button = tk.Button(root, text="Process Text", command=self.process_text)

        # Pack UI elements
        self.text_input.pack(padx=10, pady=10)
        self.scrollbar.pack(side="right", fill="y")
        self.preprocessed_display.pack(padx=10, pady=10)
        self.process_button.pack(pady=10)

    def process_text(self):
        input_text = self.text_input.get("1.0", END).strip()

        if not input_text:
            return

        # Tokenize, remove stopwords, and perform stemming using NLTK
        preprocessed_text = self.tokenize_and_preprocess(input_text)

        # Display the preprocessed text
        self.display_preprocessed_text(preprocessed_text)

    def tokenize_and_preprocess(self, input_text):
        # Tokenize the input text
        tokens = word_tokenize(input_text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Perform stemming
        porter = PorterStemmer()
        stemmed_tokens = [porter.stem(word) for word in filtered_tokens]

        # Join the preprocessed tokens into a string
        preprocessed_text = ' '.join(stemmed_tokens)

        return preprocessed_text

    def display_preprocessed_text(self, preprocessed_text):
        self.preprocessed_display.config(state=tk.NORMAL)
        self.preprocessed_display.delete("1.0", END)
        self.preprocessed_display.insert(END, preprocessed_text)
        self.preprocessed_display.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextPreprocessorApp(root)
    root.mainloop()
