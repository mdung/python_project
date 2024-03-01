import pandas as pd
import datetime
import cryptocompare

def fetch_cryptocompare_data(symbol, end_date=datetime.datetime.now(), chunk_size=2000):
    try:
        df_list = []

        while end_date > datetime.datetime(2009, 1, 1):
            start_date = end_date - datetime.timedelta(days=chunk_size)
            if start_date < datetime.datetime(2009, 1, 1):
                start_date = datetime.datetime(2009, 1, 1)

            # Fetch historical data for the chunk
            historical_data = cryptocompare.get_historical_price_day(
                symbol, currency='USD', toTs=end_date, limit=chunk_size, exchange='Coinbase'
            )

            # Convert the data to a DataFrame
            df_chunk = pd.DataFrame(historical_data)

            # Convert timestamp to datetime
            df_chunk['time'] = pd.to_datetime(df_chunk['time'], unit='s')

            # Set timestamp as the index
            df_chunk.set_index('time', inplace=True)

            # Concatenate the chunk to the list
            df_list.append(df_chunk)

            # Move the end_date to the start of the next chunk
            end_date = start_date

        # Concatenate all chunks into a single DataFrame
        df = pd.concat(df_list[::-1])  # Reverse the list to maintain chronological order

        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def fetch_all_coins_history():
    # List of common cryptocurrency symbols
    symbols = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'EOS', 'ADA', 'XLM', 'TRX', 'XMR']

    for symbol in symbols:
        data = fetch_cryptocompare_data(symbol)
        if data is not None:
            print(f"Data for {symbol} fetched successfully.")
            # You can process or save the data as needed.
            # For example, you can save the DataFrame to a CSV file:
            data.to_csv(f"{symbol}_historical_data.csv")
        else:
            print(f"Failed to fetch data for {symbol}.")

if __name__ == "__main__":
    fetch_all_coins_history()
