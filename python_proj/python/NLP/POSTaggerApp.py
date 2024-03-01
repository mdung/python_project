import tkinter as tk
from tkinter import scrolledtext
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords

class POSTaggerApp:
    def __init__(self, master):
        self.master = master
        master.title("POS Tagger App")

        self.input_label = tk.Label(master, text="Enter a sentence:")
        self.input_label.pack()

        self.input_text = tk.Text(master, height=3, width=50)
        self.input_text.pack()

        self.result_label = tk.Label(master, text="POS Tags:")
        self.result_label.pack()

        self.result_text = scrolledtext.ScrolledText(master, height=5, width=50)
        self.result_text.pack()

        self.tag_button = tk.Button(master, text="Tag Sentence", command=self.tag_sentence)
        self.tag_button.pack()

    def tag_sentence(self):
        sentence = self.input_text.get("1.0", tk.END).strip()

        # Tokenize the sentence and remove stopwords
        tokens = [word.lower() for word in word_tokenize(sentence) if word.isalnum() and word.lower() not in stopwords.words('english')]

        # Perform part-of-speech tagging
        pos_tags = pos_tag(tokens)

        # Display the result
        result_str = "\n".join([f"{word}: {tag}" for word, tag in pos_tags])
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = POSTaggerApp(root)
    root.mainloop()
