import tkinter as tk
from tkinter import scrolledtext
from pyfiglet import Figlet

class AsciiArtConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("ASCII Art Converter")

        self.label = tk.Label(self.master, text="Enter Text:")
        self.label.pack()

        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack()

        self.convert_button = tk.Button(self.master, text="Convert to ASCII Art", command=self.convert_text)
        self.convert_button.pack()

        self.ascii_output = tk.Text(self.master, wrap=tk.WORD, width=40, height=10)
        self.ascii_output.pack()

    def convert_text(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        if input_text:
            ascii_art = self.generate_ascii_art(input_text)
            self.display_ascii_art(ascii_art)
        else:
            self.ascii_output.delete(1.0, tk.END)
            self.ascii_output.insert(tk.END, "Please enter some text.")

    def generate_ascii_art(self, text):
        figlet = Figlet()
        return figlet.renderText(text)

    def display_ascii_art(self, ascii_art):
        self.ascii_output.delete(1.0, tk.END)
        self.ascii_output.insert(tk.END, ascii_art)

def main():
    root = tk.Tk()
    app = AsciiArtConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
