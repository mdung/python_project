import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class ICOAnalyzer:
    def __init__(self):
        self.ico_data = None

    def fetch_ico_data(self):
        # Replace the URL with the actual API endpoint providing ICO data
        api_url = "https://api.example.com/ico_data"
        response = requests.get(api_url)

        if response.status_code == 200:
            ico_data = response.json()
            self.ico_data = pd.DataFrame(ico_data)
            self.ico_data['Start Date'] = pd.to_datetime(self.ico_data['Start Date'])
            print("ICO data fetched successfully.")
        else:
            print(f"Failed to fetch ICO data. Status code: {response.status_code}")

    def analyze_ico_data(self):
        if self.ico_data is not None:
            # Perform analysis (example: plot ICOs over time)
            self.plot_ico_count_over_time()
        else:
            print("No ICO data available. Please fetch data first.")

    def plot_ico_count_over_time(self):
        grouped_data = self.ico_data.groupby(self.ico_data['Start Date'].dt.to_period("M")).size()
        plt.figure(figsize=(10, 6))
        grouped_data.plot(kind='bar', color='skyblue')
        plt.title("Number of ICOs Over Time")
        plt.xlabel("Month")
        plt.ylabel("Number of ICOs")
        plt.show()

if __name__ == '__main__':
    ico_analyzer = ICOAnalyzer()

    # Fetch ICO data
    ico_analyzer.fetch_ico_data()

    # Analyze and visualize ICO data
    ico_analyzer.analyze_ico_data()
