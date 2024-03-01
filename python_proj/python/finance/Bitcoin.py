import requests
from bs4 import BeautifulSoup
import time

def get_bitcoin_price():
    url = "https://www.coindesk.com/price/bitcoin"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Update the selector based on the current HTML structure
        price_element = soup.find("div", class_="price-value")

        if price_element:
            return price_element.text.strip()
        else:
            return "Price not found on the webpage."
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

def main():
    print("Real-time Bitcoin Price Tracker")

    while True:
        bitcoin_price = get_bitcoin_price()
        print(f"Bitcoin Price: {bitcoin_price}")
        time.sleep(60)  # Fetch the price every minute

if __name__ == "__main__":
    main()
