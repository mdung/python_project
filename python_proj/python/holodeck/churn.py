import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ChurnAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Churn Analysis")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Load Telecom Data", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.analyze_button = tk.Button(self.frame, text="Analyze Churn", command=self.analyze_churn)
        self.analyze_button.pack(pady=10)

        # Initialize DataFrame
        self.telecom_data = pd.DataFrame()
        self.model = None

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select Telecom Dataset CSV file",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.telecom_data = pd.read_csv(file_path)
            tk.messagebox.showinfo("Success", "Telecom dataset loaded successfully!")

    def analyze_churn(self):
        if self.telecom_data.empty:
            tk.messagebox.showwarning("Warning", "Please load telecom data first.")
            return

        # Preprocess data and build a churn prediction model
        X = self.telecom_data.drop(['Churn'], axis=1)
        y = self.telecom_data['Churn']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Display accuracy and confusion matrix
        accuracy = accuracy_score(y_test, y_pred)
        confusion_mat = confusion_matrix(y_test, y_pred)

        tk.messagebox.showinfo("Churn Analysis Results", f"Accuracy: {accuracy:.2f}\n\nConfusion Matrix:\n{confusion_mat}")

        # Visualize confusion matrix
        self.visualize_confusion_matrix(confusion_mat)

    def visualize_confusion_matrix(self, confusion_matrix):
        plt.figure(figsize=(5, 4))
        plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title('Confusion Matrix')
        plt.colorbar()

        classes = ['Not Churned', 'Churned']
        tick_marks = range(len(classes))

        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')

        plt.tight_layout()

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChurnAnalysisApp(root)
    root.mainloop()
