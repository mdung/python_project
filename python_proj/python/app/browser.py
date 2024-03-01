import tkinter as tk
from tkinterweb import TkinterWeb

class SimpleWebBrowser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Web Browser")

        self.browser = TkinterWeb(self.root)
        self.browser.pack(expand=True, fill=tk.BOTH)

        # Entry for URL
        self.url_entry = tk.Entry(self.root)
        self.url_entry.pack(fill=tk.X)

        # Button to open URL
        open_button = tk.Button(self.root, text="Open URL", command=self.open_url)
        open_button.pack()

    def open_url(self):
        url = self.url_entry.get()
        if url:
            self.browser.open_new_tab(url)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    browser = SimpleWebBrowser()
    browser.run()
