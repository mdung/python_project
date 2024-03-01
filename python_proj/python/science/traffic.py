# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load sample traffic congestion data (replace with your own dataset)
# Assume the dataset has features like 'Hour', 'Day', 'Weather', 'TrafficVolume', etc.
data = {
    'Hour': [8, 12, 16, 20, 8, 12, 16, 20],
    'Day': ['Weekday'] * 4 + ['Weekend'] * 4,
    'Weather': ['Clear', 'Clear', 'Rain', 'Rain', 'Clear', 'Clear', 'Rain', 'Rain'],
    'TrafficVolume': [100, 150, 200, 250, 120, 180, 220, 280]
}

df = pd.DataFrame(data)

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['Day', 'Weather'], drop_first=True)

# Split the data into training and testing sets
X = df.drop('TrafficVolume', axis=1)
y = df['TrafficVolume']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Visualize predicted vs actual traffic volume
plt.scatter(X_test['Hour'], y_test, label='Actual Traffic Volume', alpha=0.7)
plt.scatter(X_test['Hour'], y_pred, label='Predicted Traffic Volume', alpha=0.7)
plt.xlabel('Hour')
plt.ylabel('Traffic Volume')
plt.legend()
plt.title('Predicted vs Actual Traffic Volume')
plt.show()
