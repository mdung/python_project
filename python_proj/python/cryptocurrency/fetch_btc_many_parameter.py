import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your CSV data
file_path = 'BTC_historical_data.csv'  # Replace with your actual file path
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

# Model Training (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Historical Data Visualization
plt.figure(figsize=(16, 8))
plt.plot(df.index, df['close'], label='Historical Close Price', color='blue')

# Future Prediction
future_dates_month = pd.date_range(df.index[-1], periods=30, freq='D')[1:]  # Next 30 days
future_dates_year = pd.date_range(df.index[-1], periods=365, freq='D')[1:]  # Next 365 days

# Generate features for prediction
future_features_month = pd.DataFrame(np.random.rand(len(future_dates_month), len(features.columns)), columns=features.columns, index=future_dates_month)
future_features_year = pd.DataFrame(np.random.rand(len(future_dates_year), len(features.columns)), columns=features.columns, index=future_dates_year)

# Predictions
future_predictions_month = model.predict(future_features_month)
future_predictions_year = model.predict(future_features_year)

# Plot Future Predictions
plt.plot(future_dates_month, future_predictions_month, label='Predicted Close Price (Next Month)', color='orange', linestyle='dashed')
plt.plot(future_dates_year, future_predictions_year, label='Predicted Close Price (Next Year)', color='red', linestyle='dashed')

# Labels and Legend
plt.title('Historical and Predicted Close Price')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.show()
