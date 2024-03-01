import tkinter as tk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")

        self.label1 = tk.Label(self.master, text="Enter text:")
        self.label1.pack()

        self.text_entry = tk.Entry(self.master, width=40)
        self.text_entry.pack()

        self.label2 = tk.Label(self.master, text="Choose target language:")
        self.label2.pack()

        self.languages = ["en", "es", "fr", "de", "ja"]  # You can add more language codes
        self.language_var = tk.StringVar()
        self.language_var.set(self.languages[0])

        self.language_menu = tk.OptionMenu(self.master, self.language_var, *self.languages)
        self.language_menu.pack()

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def translate_text(self):
        text_to_translate = self.text_entry.get()
        target_language = self.language_var.get()

        if not text_to_translate:
            self.result_label.config(text="Please enter text to translate.")
            return

        try:
            translator = Translator()
            translation = translator.translate(text_to_translate, dest=target_language)
            translated_text = translation.text
            self.result_label.config(text=f"Translation: {translated_text}")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
