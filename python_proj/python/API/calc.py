import tkinter as tk
from math import sin, cos, tan, radians

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.screen = tk.Entry(master, font=('Arial', 20), bd=10, insertwidth=4, width=15, justify='right')
        self.screen.grid(row=0, column=0, columnspan=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 16), padx=20, pady=20,
                               command=lambda t=text: self.click(t))
            button.grid(row=row, column=col)

    def click(self, value):
        if value == 'C':
            self.screen.delete(0, tk.END)
        elif value == '=':
            try:
                expression = self.screen.get()
                expression = expression.replace("sin", "sin(radians(").replace("cos", "cos(radians(").replace("tan", "tan(radians(") + ")"
                result = eval(expression)
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, str(result))
            except Exception as e:
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, "Error")
        else:
            self.screen.insert(tk.END, value)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
