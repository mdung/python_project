import tkinter as tk
from tkinter import ttk

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = {}

        self.tree = ttk.Treeview(master, columns=("Category", "Amount"), show="headings")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.category_entry = tk.Entry(master)
        self.amount_entry = tk.Entry(master)

        self.category_label = tk.Label(master, text="Category:")
        self.amount_label = tk.Label(master, text="Amount:")

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)

        self.category_label.pack()
        self.category_entry.pack()
        self.amount_label.pack()
        self.amount_entry.pack()
        self.add_button.pack()

    def add_expense(self):
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        if category and amount:
            amount = float(amount)
            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount

            self.update_treeview()
            self.clear_entries()

    def update_treeview(self):
        # Clear previous data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Populate with updated data
        for category, amount in self.expenses.items():
            self.tree.insert("", "end", values=(category, f"${amount:.2f}"))

    def clear_entries(self):
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    expense_tracker = ExpenseTracker(root)
    root.mainloop()
