import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DecisionTreeClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Decision Tree Classifier App")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Load Dataset", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.train_button = tk.Button(self.frame, text="Train Decision Tree", command=self.train_model)
        self.train_button.pack(pady=10)

        # Initialize DataFrame
        self.dataset = pd.DataFrame()
        self.model = None

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select Dataset CSV file",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.dataset = pd.read_csv(file_path)
            tk.messagebox.showinfo("Success", "Dataset loaded successfully!")

    def train_model(self):
        if self.dataset.empty:
            tk.messagebox.showwarning("Warning", "Please load the dataset first.")
            return

        # Assuming the last column is the target variable
        X = self.dataset.iloc[:, :-1]
        y = self.dataset.iloc[:, -1]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a decision tree classifier
        self.model = DecisionTreeClassifier(random_state=42)
        self.model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        confusion_mat = confusion_matrix(y_test, y_pred)
        classification_rep = classification_report(y_test, y_pred)

        tk.messagebox.showinfo("Model Evaluation",
                               f"Accuracy: {accuracy:.2f}\n\nConfusion Matrix:\n{confusion_mat}\n\nClassification Report:\n{classification_rep}")

        # Visualize the decision tree
        self.visualize_decision_tree()

    def visualize_decision_tree(self):
        plt.figure(figsize=(10, 8))
        self.plot_tree(self.model, feature_names=self.dataset.columns[:-1], class_names=self.dataset.iloc[:, -1].unique(),
                       filled=True, rounded=True)
        plt.title('Decision Tree Visualization')

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    @staticmethod
    def plot_tree(tree, feature_names, class_names, filled=True, rounded=True):
        import graphviz
        from sklearn.tree import export_graphviz

        dot_data = export_graphviz(tree, out_file=None, feature_names=feature_names, class_names=class_names,
                                   filled=filled, rounded=rounded, special_characters=True)

        graph = graphviz.Source(dot_data)
        graph.render("decision_tree", view=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DecisionTreeClassifierApp(root)
    root.mainloop()
