import tkinter as tk
from tkinter import scrolledtext
from nltk.corpus import wordnet
from nltk.wsd import lesk

class VocabularyEnhancerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Vocabulary Enhancer")

        self.label1 = tk.Label(self.master, text="Enter text:")
        self.label1.pack()

        self.input_text = scrolledtext.ScrolledText(self.master, width=40, height=5)
        self.input_text.pack()

        self.enhance_button = tk.Button(self.master, text="Enhance Vocabulary", command=self.enhance_vocabulary)
        self.enhance_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def enhance_vocabulary(self):
        input_text = self.input_text.get("1.0", tk.END).strip()

        if not input_text:
            self.result_label.config(text="Please enter text.")
            return

        try:
            enhanced_text = self.replace_with_synonyms(input_text)
            self.result_label.config(text=f"Enhanced Text:\n{enhanced_text}")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

    def replace_with_synonyms(self, text):
        words = text.split()
        enhanced_words = []

        for word in words:
            synonym = self.get_synonym(word)
            enhanced_words.append(synonym if synonym else word)

        enhanced_text = ' '.join(enhanced_words)
        return enhanced_text

    def get_synonym(self, word):
        synsets = wordnet.synsets(word)
        if synsets:
            # Using Lesk algorithm to find the most appropriate synonym
            most_likely_synset = lesk(word.split(), synsets)
            if most_likely_synset:
                synonyms = [lemma.name() for lemma in most_likely_synset.lemmas()]
                # Avoid choosing the same word as a synonym
                synonyms = [syn for syn in synonyms if syn.lower() != word.lower()]
                return synonyms[0] if synonyms else None
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabularyEnhancerApp(root)
    root.mainloop()
