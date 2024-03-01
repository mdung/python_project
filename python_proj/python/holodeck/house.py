import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HousePricePredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Price Predictor")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Generate Real Estate Data", command=self.generate_data)
        self.load_data_button.pack(pady=10)

        self.predict_button = tk.Button(self.frame, text="Predict House Prices", command=self.predict_prices)
        self.predict_button.pack(pady=10)

        # Initialize DataFrame
        self.real_estate_data = pd.DataFrame()
        self.model = None

    def generate_data(self):
        # Generate a simplified real estate dataset
        np.random.seed(42)
        num_samples = 100
        bedrooms = np.random.randint(1, 6, size=num_samples)
        bathrooms = np.random.randint(1, 4, size=num_samples)
        area = np.random.randint(800, 3000, size=num_samples)
        price = 50000 + 300 * bedrooms + 200 * bathrooms + 150 * area + np.random.normal(scale=10000, size=num_samples)

        self.real_estate_data = pd.DataFrame({'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Area': area, 'Price': price})

        messagebox.showinfo("Success", "Real estate data generated successfully!")

    def predict_prices(self):
        if self.real_estate_data.empty:
            messagebox.showwarning("Warning", "Please generate real estate data first.")
            return

        # Prepare data for training
        X = self.real_estate_data[['Bedrooms', 'Bathrooms', 'Area']]
        y = self.real_estate_data['Price']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a linear regression model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Predict house prices on the test set
        y_pred = self.model.predict(X_test)

        # Visualize predictions
        self.visualize_predictions(X_test, y_test, y_pred)

    def visualize_predictions(self, X_test, y_test, y_pred):
        # Create a scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(X_test['Area'], y_test, label='Actual Prices', color='blue')
        plt.scatter(X_test['Area'], y_pred, label='Predicted Prices', color='red')
        plt.title('House Price Prediction')
        plt.xlabel('Area')
        plt.ylabel('Price')
        plt.legend()

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HousePricePredictorApp(root)
    root.mainloop()
