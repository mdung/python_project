import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVFileGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV File Generator")

        self.label = tk.Label(self.master, text="Generate CSV File:")
        self.label.pack()

        self.generate_button = tk.Button(self.master, text="Generate CSV", command=self.generate_csv)
        self.generate_button.pack()

    def generate_csv(self):
        data = {'Name': ['John', 'Alice', 'Bob'],
                'Age': [25, 30, 22],
                'City': ['New York', 'San Francisco', 'Los Angeles']}

        df = pd.DataFrame(data)

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if file_path:
            df.to_csv(file_path, index=False)
            self.show_message(f"CSV file generated and saved at:\n{file_path}")
        else:
            self.show_error("File not saved.")

    def show_message(self, message):
        message_label = tk.Label(self.master, text=message, fg="green")
        message_label.pack()

    def show_error(self, message):
        error_label = tk.Label(self.master, text=f"Error: {message}", fg="red")
        error_label.pack()

def main():
    root = tk.Tk()
    app = CSVFileGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
