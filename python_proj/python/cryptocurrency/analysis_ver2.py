import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your CSV data
file_path = 'ADA_historical_data.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Data Exploration and Analysis
print("Data Summary:")
print(df.describe())

# Feature Engineering
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

# Feature Selection
features = df[['open', 'high', 'low', 'volumefrom', 'volumeto']]
target = df['close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Model Prediction
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualization
fig, ax1 = plt.subplots(figsize=(12, 6))

# Line plot for actual and predicted close prices
ax1.plot(df.index, df['close'], label='Actual Close Price', color='blue')
ax1.plot(y_test.index, y_pred, label='Predicted Close Price', color='red', linestyle='dashed')
ax1.set_xlabel('Time')
ax1.set_ylabel('Close Price', color='black')
ax1.legend(loc='upper left')

# Bar plot for the difference between actual and predicted prices
ax2 = ax1.twinx()
ax2.bar(y_test.index, y_test - y_pred, alpha=0.2, color='gray', label='Prediction Error')
ax2.set_ylabel('Prediction Error', color='black')
ax2.legend(loc='upper right')

plt.title('Actual vs Predicted Close Price with Prediction Error')
plt.show()
