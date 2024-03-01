import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TitanicAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Titanic Dataset Analyzer")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Load Titanic Dataset", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.analyze_button = tk.Button(self.frame, text="Analyze Survival Factors", command=self.analyze_data)
        self.analyze_button.pack(pady=10)

        # Initialize DataFrame
        self.titanic_data = pd.DataFrame()

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select Titanic Dataset CSV file", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.titanic_data = pd.read_csv(file_path)
            tk.messagebox.showinfo("Success", "Titanic dataset loaded successfully!")

    def analyze_data(self):
        if self.titanic_data.empty:
            tk.messagebox.showwarning("Warning", "Please load the Titanic dataset first.")
            return

        # Data Analysis and Visualization
        # You can customize this section based on your analysis goals

        # Example: Survival by Pclass
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Pclass', hue='Survived', data=self.titanic_data)
        plt.title('Survival by Pclass')
        plt.xlabel('Passenger Class')
        plt.ylabel('Count')
        plt.legend(title='Survived', labels=['No', 'Yes'])
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TitanicAnalyzerApp(root)
    root.mainloop()
