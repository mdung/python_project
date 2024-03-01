import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def prepare_data(stock_data):
    # Create a new column 'Next Close' with the next day's closing price
    stock_data['Next Close'] = stock_data['Close'].shift(-1)

    # Drop NaN values
    stock_data = stock_data.dropna()

    # Features (X) and target variable (y)
    X = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = stock_data['Next Close']

    return X, y

def train_model(X_train, y_train):
    # Initialize Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test):
    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Calculate Mean Squared Error
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Visualize actual vs predicted prices
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.index, y_test.values, label='Actual Next Close', color='blue')
    plt.plot(y_test.index, predictions, label='Predicted Next Close', color='red')
    plt.title('Actual vs Predicted Next Close Prices')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Input stock symbol and date range
    stock_ticker = input("Enter the stock symbol (e.g., AAPL): ").upper()
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365 * 5)).strftime('%Y-%m-%d')  # 5 years of historical data

    # Fetch stock data
    stock_data = fetch_stock_data(stock_ticker, start_date, end_date)

    if not stock_data.empty:
        # Prepare data
        X, y = prepare_data(stock_data)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Train the model
        model = train_model(X_train, y_train)

        # Evaluate the model
        evaluate_model(model, X_test, y_test)
    else:
        print(f"No data available for {stock_ticker}. Please check the stock symbol.")
