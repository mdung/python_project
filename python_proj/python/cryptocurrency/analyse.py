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
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close'], label='Actual Close Price', color='blue')
plt.plot(y_test.index, y_pred, label='Predicted Close Price', color='red', linestyle='dashed')
plt.title('Actual vs Predicted Close Price')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.show()
