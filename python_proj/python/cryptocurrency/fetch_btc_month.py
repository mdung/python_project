import pandas as pd
import datetime
import cryptocompare

def fetch_cryptocompare_data(symbol, days=30):
    try:
        # Calculate the from timestamp (e.g., 30 days ago)
        to_timestamp = datetime.datetime.now()
        from_timestamp = to_timestamp - datetime.timedelta(days=days)

        # Fetch historical data
        historical_data = cryptocompare.get_historical_price_day(
            symbol, currency='USD', toTs=to_timestamp, limit=days, exchange='Coinbase'
        )

        # Convert the data to a DataFrame
        df = pd.DataFrame(historical_data)

        # Convert timestamp to datetime
        df['time'] = pd.to_datetime(df['time'], unit='s')

        # Set timestamp as the index
        df.set_index('time', inplace=True)

        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

if __name__ == "__main__":
    # Replace 'BTC' with the desired cryptocurrency symbol
    symbol = 'BTC'

    # Fetch historical data for the specified symbol
    data = fetch_cryptocompare_data(symbol, days=30)

    if data is not None:
        print(f"Data for {symbol} fetched successfully.")
        # You can process or save the data as needed.
        # For example, you can save the DataFrame to a CSV file:
        data.to_csv(f"{symbol}_historical_data.csv")
    else:
        print(f"Failed to fetch data for {symbol}.")
