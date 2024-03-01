import tkinter as tk
from math import *

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Calculator")
        self.geometry("400x500")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display input and results
        entry = tk.Entry(self, textvariable=self.result_var, font=('Helvetica', 14), justify='right', bd=10)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Helvetica', 14), command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_input = self.result_var.get()

        if button == "=":
            try:
                result = eval(current_input)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_input += str(button)
            self.result_var.set(current_input)

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()
