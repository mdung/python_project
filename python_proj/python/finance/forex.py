from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk

class ForexRateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forex Rates")

        self.currency_rates = CurrencyRates()
        self.currency_pairs = ["USD to EUR", "USD to GBP", "USD to JPY", "EUR to GBP", "EUR to JPY", "GBP to JPY"]

        self.label = tk.Label(root, text="Select Currency Pair:")
        self.label.pack(pady=10)

        self.currency_var = tk.StringVar()
        self.currency_var.set(self.currency_pairs[0])

        self.currency_dropdown = ttk.Combobox(root, values=self.currency_pairs, textvariable=self.currency_var)
        self.currency_dropdown.pack(pady=10)

        self.fetch_button = tk.Button(root, text="Fetch Rates", command=self.fetch_rates)
        self.fetch_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def fetch_rates(self):
        selected_pair = self.currency_var.get()
        base_currency, target_currency = selected_pair.split(" to ")

        try:
            rate = self.currency_rates.get_rate(base_currency, target_currency)
            self.result_label.config(text=f"1 {base_currency} = {rate:.4f} {target_currency}")
        except Exception as e:
            self.result_label.config(text=f"Error fetching rates: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ForexRateApp(root)
    root.mainloop()
