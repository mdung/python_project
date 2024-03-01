import yfinance as yf
import tkinter as tk
from tkinter import ttk

class StockPriceTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Stock Price Tracker")

        self.create_widgets()

    def create_widgets(self):
        self.symbol_label = ttk.Label(self.master, text="Stock Symbol:")
        self.symbol_label.pack(pady=10)

        self.symbol_entry = ttk.Entry(self.master)
        self.symbol_entry.pack(pady=10)

        self.track_button = ttk.Button(self.master, text="Track", command=self.track_stock)
        self.track_button.pack(pady=10)

        self.price_label = ttk.Label(self.master, text="Current Price:")
        self.price_label.pack(pady=10)

    def track_stock(self):
        symbol = self.symbol_entry.get().upper()

        try:
            stock_data = yf.Ticker(symbol)
            current_price = stock_data.history(period='1d')['Close'].iloc[-1]
            self.update_price_label(f"Current Price: ${current_price:.2f}")
        except Exception as e:
            self.update_price_label(f"Error fetching data. {str(e)}")

    def update_price_label(self, text):
        self.price_label.config(text=text)

if __name__ == '__main__':
    root = tk.Tk()
    app = StockPriceTrackerApp(root)
    root.mainloop()
