import requests
import pandas as pd
from datetime import datetime

def fetch_coingecko_data(symbol, days=30):
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = f"/coins/{symbol}/market_chart"

    # Calculate the from timestamp (e.g., 30 days ago)
    to_timestamp = int(datetime.now().timestamp()) * 1000  # current timestamp
    from_timestamp = to_timestamp - (days * 24 * 60 * 60 * 1000)

    params = {
        'vs_currency': 'usd',  # You can change the currency if needed
        'from': from_timestamp,
        'to': to_timestamp,
        'interval': '1d',  # '1d' for daily data, '1h' for hourly data, etc.
    }

    try:
        response = requests.get(base_url + endpoint, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract OHLCV data
        ohlcv_data = data.get('prices', [])

        # Convert the data to a DataFrame
        df = pd.DataFrame(ohlcv_data, columns=['timestamp', 'price'])

        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Set timestamp as the index
        df.set_index('timestamp', inplace=True)

        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

if __name__ == "__main__":
    # Replace 'bitcoin' with the desired cryptocurrency symbol
    symbol = 'bitcoin'

    # Fetch historical data for the specified symbol
    data = fetch_coingecko_data(symbol, days=30)

    if data is not None:
        print(f"Data for {symbol} fetched successfully.")
        # You can process or save the data as needed.
        # For example, you can save the DataFrame to a CSV file:
        data.to_csv(f"{symbol}_historical_data.csv")
    else:
        print(f"Failed to fetch data for {symbol}.")
