import tkinter as tk
from tkinter import scrolledtext
import markovify

class HeadlineGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Headline Generator")

        self.label1 = tk.Label(self.master, text="Enter input text:")
        self.label1.pack()

        self.input_text = scrolledtext.ScrolledText(self.master, width=40, height=5)
        self.input_text.pack()

        self.generate_button = tk.Button(self.master, text="Generate Headline", command=self.generate_headline)
        self.generate_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def generate_headline(self):
        input_text = self.input_text.get("1.0", tk.END).strip()

        if not input_text:
            self.result_label.config(text="Please enter input text.")
            return

        try:
            model = markovify.Text(input_text)
            headline = model.make_short_sentence(100, tries=100)

            if headline:
                self.result_label.config(text=f"Generated Headline: {headline}")
            else:
                self.result_label.config(text="Unable to generate a headline. Try different input.")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HeadlineGeneratorApp(root)
    root.mainloop()
