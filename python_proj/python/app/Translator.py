import tkinter as tk
from googletrans import Translator

class LanguageTranslator:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")

        self.translator = Translator()

        self.input_label = tk.Label(master, text="Enter Text:")
        self.input_entry = tk.Entry(master, width=50)
        self.translate_button = tk.Button(master, text="Translate", command=self.translate_text)

        self.output_label = tk.Label(master, text="Translation:")
        self.output_text = tk.Text(master, wrap=tk.WORD, height=5, width=50, state=tk.DISABLED)

        self.input_label.pack()
        self.input_entry.pack()
        self.translate_button.pack()
        self.output_label.pack()
        self.output_text.pack()

    def translate_text(self):
        input_text = self.input_entry.get()

        if input_text:
            translation = self.translator.translate(input_text, dest="en")
            translated_text = translation.text
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, translated_text)
            self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    translator_app = LanguageTranslator(root)
    root.mainloop()
