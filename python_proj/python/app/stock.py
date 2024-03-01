import tkinter as tk
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StockPriceTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stock Price Tracker")

        # Entry for stock symbol
        self.symbol_entry = ttk.Entry(self.root)
        self.symbol_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to fetch data
        fetch_button = ttk.Button(self.root, text="Fetch Data", command=self.fetch_data)
        fetch_button.grid(row=0, column=1, padx=10, pady=10)

        # Figure for plotting
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, columnspan=2)

    def fetch_data(self):
        try:
            symbol = self.symbol_entry.get().upper()
            data = yf.download(symbol, period="1y")

            # Plotting the data
            self.ax.clear()
            data['Close'].plot(ax=self.ax, title=f"Stock Price for {symbol}")
            self.ax.set_xlabel("Date")
            self.ax.set_ylabel("Closing Price")

            # Refresh canvas
            self.canvas.draw()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error fetching data: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    stock_tracker = StockPriceTracker()
    stock_tracker.run()
