import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data input (replace this with your own stock market data)
# For simplicity, we'll generate synthetic data
np.random.seed(0)
days = np.arange(1, 101)
prices = 100 + 2 * days + np.random.randn(100) * 10

# Create a DataFrame
df = pd.DataFrame({'Day': days, 'Price': prices})

# Plot the stock price data
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Price'], label='Stock Price')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('Stock Market Data Analysis')
plt.legend()
plt.show()

# Split the data into training and testing sets
X = df[['Day']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Plot the predicted values
plt.figure(figsize=(10, 6))
plt.plot(X_test, y_test, label='Actual Price')
plt.plot(X_test, y_pred, label='Predicted Price', linestyle='dashed')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('Stock Price Prediction')
plt.legend()
plt.show()
