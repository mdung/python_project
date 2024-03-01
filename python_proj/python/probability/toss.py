import tkinter as tk
from tkinter import ttk
import random

class CoinTossSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Coin Toss Simulator")

        self.result_label = ttk.Label(root, text="Result: ")
        self.result_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.toss_button = ttk.Button(root, text="Toss Coin", command=self.toss_coin)
        self.toss_button.grid(row=1, column=0, columnspan=2, pady=10)

    def toss_coin(self):
        outcomes = ["Heads", "Tails"]
        result = random.choice(outcomes)
        self.result_label.config(text="Result: " + result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoinTossSimulator(root)
    root.mainloop()
