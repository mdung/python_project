import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load and preprocess data
def load_data():
    # Replace this with your dataset
    # Example: data = pd.read_csv("your_dataset.csv")
    # Ensure that the dataset contains features and a target variable (disease progression)
    # For simplicity, let's assume a CSV file with numeric features and a 'progression' column.
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'progression': [10, 20, 30, 40, 50]
    })
    return data

# Function to train the machine learning model
def train_model(data):
    X = data.drop('progression', axis=1)
    y = data['progression']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error on Test Set: {mse}")

    return model

# Function to update the plot based on user input
def update_plot():
    # Replace this with your input features
    # Example: feature1_val = float(entry_feature1.get())
    #          feature2_val = float(entry_feature2.get())
    feature1_val = 6  # Replace with actual input
    feature2_val = 4  # Replace with actual input

    # Make a prediction using the trained model
    prediction = model.predict([[feature1_val, feature2_val]])

    # Update the plot
    ax.clear()
    ax.set_title("Disease Progression Prediction")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

    # Scatter plot of training data
    ax.scatter(X_train['feature1'], X_train['feature2'], c=y_train, cmap='viridis', label='Training Data')

    # Scatter plot of test data
    ax.scatter(X_test['feature1'], X_test['feature2'], c=y_test, cmap='viridis', marker='x', label='Test Data')

    # Highlight the input point
    ax.scatter(feature1_val, feature2_val, color='red', marker='o', s=100, label='Input')

    # Display the prediction
    ax.text(feature1_val, feature2_val, f'Prediction: {prediction[0]:.2f}', color='red', fontsize=10)

    ax.legend()
    canvas.draw()

# GUI setup
root = tk.Tk()
root.title("Disease Progression Prediction App")

# Load and preprocess data
data = load_data()

# Train the machine learning model
model = train_model(data)

# Frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and entry widgets for input features
ttk.Label(frame, text="Feature 1:").grid(row=0, column=0, sticky=tk.W)
entry_feature1 = ttk.Entry(frame)
entry_feature1.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Feature 2:").grid(row=1, column=0, sticky=tk.W)
entry_feature2 = ttk.Entry(frame)
entry_feature2.grid(row=1, column=1, sticky=tk.W)

# Button to predict and update plot
predict_button = ttk.Button(frame, text="Predict", command=update_plot)
predict_button.grid(row=2, column=0, columnspan=2, pady=10)

# Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Run the GUI
root.mainloop()
