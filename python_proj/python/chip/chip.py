import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog


class ChipAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Chip Manufacturing Data Analyzer")

        self.load_button = Button(master, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=10)

        self.analyze_button = Button(master, text="Analyze Data", command=self.analyze_data)
        self.analyze_button.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")

    def analyze_data(self):
        if hasattr(self, 'data'):
            # Add your data analysis logic here
            # For example, let's plot a histogram of a numeric column
            numeric_column = self.select_numeric_column()
            if numeric_column:
                plt.hist(self.data[numeric_column].dropna(), bins=20, color='blue', alpha=0.7)
                plt.title(f'Histogram of {numeric_column}')
                plt.xlabel(numeric_column)
                plt.ylabel('Frequency')
                plt.show()
        else:
            messagebox.showwarning("Warning", "Please load data first.")

    def select_numeric_column(self):
        if hasattr(self, 'data'):
            numeric_columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_columns:
                selected_column = simpledialog.askstring("Select Column", "Select a numeric column:",
                                                         initialvalue=numeric_columns[0], parent=self.master)
                return selected_column
            else:
                messagebox.showwarning("No Numeric Columns", "No numeric columns found in the data.")
        return None

if __name__ == '__main__':
    root = Tk()
    app = ChipAnalyzerApp(root)
    root.mainloop()
