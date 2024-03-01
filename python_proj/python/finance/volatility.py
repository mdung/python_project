import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def download_historical_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

def calculate_daily_returns(prices):
    return prices.pct_change().dropna()

def calculate_volatility(returns):
    return np.std(returns)

def calculate_annualized_volatility(returns):
    daily_volatility = calculate_volatility(returns)
    annualized_volatility = daily_volatility * np.sqrt(252)  # Assuming 252 trading days in a year
    return annualized_volatility

def calculate_beta(stock_returns, market_returns):
    covariance_matrix = np.cov(stock_returns, market_returns)
    beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
    return beta

def calculate_var(returns, confidence_level=0.95):
    return norm.ppf(1 - confidence_level, loc=np.mean(returns), scale=np.std(returns))

def main():
    # Replace 'AAPL' with the desired stock symbol
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'

    # Download historical data
    stock_prices = download_historical_data(ticker, start_date, end_date)

    # Calculate daily returns
    returns = calculate_daily_returns(stock_prices)

    # Calculate risk metrics
    volatility = calculate_volatility(returns)
    annualized_volatility = calculate_annualized_volatility(returns)

    # Assuming the market index, replace 'SPY' with the desired market index
    market_prices = download_historical_data('SPY', start_date, end_date)
    market_returns = calculate_daily_returns(market_prices)

    beta = calculate_beta(returns, market_returns)

    # Calculate Value at Risk (VaR)
    confidence_level = 0.95
    var_95 = calculate_var(returns, confidence_level)

    # Display results
    print(f"Volatility: {volatility:.4f}")
    print(f"Annualized Volatility: {annualized_volatility:.4f}")
    print(f"Beta: {beta:.4f}")
    print(f"Value at Risk (VaR) at {confidence_level * 100:.0f}% confidence level: {var_95:.4f}")

    # Plot stock prices and returns
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    stock_prices.plot(title=f"{ticker} Stock Prices")
    plt.subplot(2, 1, 2)
    returns.plot(title=f"{ticker} Daily Returns")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
