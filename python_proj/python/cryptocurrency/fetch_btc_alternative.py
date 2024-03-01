import pandas as pd
import ccxt
import datetime

def fetch_crypto_data(symbol, timeframe='1d', limit=2000):
    try:
        exchange = ccxt.coinbase()
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

        # Convert the data to a DataFrame
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        # Convert timestamp to datetime
        df['time'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Set timestamp as the index
        df.set_index('time', inplace=True)

        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

if __name__ == "__main__":
    # Replace 'BTC/USD' with the desired trading pair
    symbol = 'BTC/USD'

    # Fetch historical data for the specified symbol
    data = fetch_crypto_data(symbol)

    if data is not None:
        print(f"Data for {symbol} fetched successfully.")
        # You can process or save the data as needed.
        # For example, you can save the DataFrame to a CSV file:
        data.to_csv(f"{symbol.replace('/', '_')}_historical_data.csv")
    else:
        print(f"Failed to fetch data for {symbol}.")
