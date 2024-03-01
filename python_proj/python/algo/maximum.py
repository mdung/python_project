import tkinter as tk
from tkinter import messagebox

class MaxElementFinderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Max Element Finder")

        self.label = tk.Label(master, text="Enter space-separated numbers:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.find_button = tk.Button(master, text="Find Maximum", command=self.find_maximum)
        self.find_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def find_maximum(self):
        try:
            numbers = [int(x) for x in self.entry.get().split()]
            if not numbers:
                raise ValueError("Please enter valid numbers.")

            max_element = max(numbers)
            result_message = f"The maximum element is: {max_element}"
            self.result_label.config(text=result_message)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MaxElementFinderApp(root)
    root.mainloop()
