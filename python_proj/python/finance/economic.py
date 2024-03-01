import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_inflation_data():
    # Replace the URL with the actual FRED API endpoint for the desired economic indicator
    api_url = "https://api.stlouisfed.org/fred/series/observations"
    api_key = "your_api_key"  # Get your API key by signing up on the FRED website

    params = {
        "series_id": "CPIAUCNS",  # Consumer Price Index for All Urban Consumers: All Items
        "api_key": api_key,
        "file_type": "json"
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()["observations"]
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df['value'] = pd.to_numeric(df['value'])
        return df
    else:
        print(f"Failed to fetch inflation data. Status code: {response.status_code}")
        return None

def analyze_inflation_data(inflation_data):
    if inflation_data is not None:
        # Perform analysis (example: plot inflation over time)
        plt.figure(figsize=(10, 6))
        plt.plot(inflation_data.index, inflation_data['value'], label="Inflation")
        plt.title("Inflation Over Time")
        plt.xlabel("Date")
        plt.ylabel("Inflation")
        plt.legend()
        plt.show()
    else:
        print("No inflation data available.")

if __name__ == '__main__':
    inflation_data = fetch_inflation_data()
    analyze_inflation_data(inflation_data)
