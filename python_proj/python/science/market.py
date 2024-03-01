import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def visualize_stock_data(stock_data, ticker):
    # Plotting stock data
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{ticker} Close Price', color='blue')

    # Adding labels and title
    plt.title(f'Stock Price Visualization - {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Input stock symbol and date range
    stock_ticker = input("Enter the stock symbol (e.g., AAPL): ").upper()
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

    # Fetch stock data
    stock_data = fetch_stock_data(stock_ticker, start_date, end_date)

    if not stock_data.empty:
        # Visualize stock data
        visualize_stock_data(stock_data, stock_ticker)
    else:
        print(f"No data available for {stock_ticker}. Please check the stock symbol.")
