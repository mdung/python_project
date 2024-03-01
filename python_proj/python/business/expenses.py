import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# Create a SQLite database and table for expense data
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense_name TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date_added TEXT NOT NULL
    )
''')
conn.commit()

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Create and configure the Treeview widget for displaying expense data
        self.tree = ttk.Treeview(root, columns=('ID', 'Expense Name', 'Category', 'Amount', 'Date Added'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Expense Name', text='Expense Name')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Amount', text='Amount')
        self.tree.heading('Date Added', text='Date Added')
        self.tree.pack(pady=10)

        # Create and configure the Entry widgets and buttons
        self.expense_name_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()

        tk.Label(root, text="Expense Name:").pack()
        self.expense_name_entry = tk.Entry(root, textvariable=self.expense_name_var)
        self.expense_name_entry.pack()

        tk.Label(root, text="Category:").pack()
        self.category_entry = tk.Entry(root, textvariable=self.category_var)
        self.category_entry.pack()

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var)
        self.amount_entry.pack()

        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=10)
        tk.Button(root, text="View Expense Details", command=self.view_expense_details).pack(pady=10)

        # Initialize the expense data display
        self.refresh_expense_data()

    def add_expense(self):
        expense_name = self.expense_name_var.get()
        category = self.category_var.get()
        amount = self.amount_var.get()
        date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute('INSERT INTO expenses (expense_name, category, amount, date_added) VALUES (?, ?, ?, ?)',
                       (expense_name, category, amount, date_added))
        conn.commit()

        # Refresh the expense data display
        self.refresh_expense_data()

    def view_expense_details(self):
        selected_item = self.tree.selection()
        if selected_item:
            expense_id = self.tree.item(selected_item, 'values')[0]
            # Fetch expense details from the database and display them
            cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
            expense_details = cursor.fetchone()
            if expense_details:
                tk.messagebox.showinfo("Expense Details", f"ID: {expense_details[0]}\nExpense Name: {expense_details[1]}\nCategory: {expense_details[2]}\nAmount: {expense_details[3]}\nDate Added: {expense_details[4]}")
            else:
                tk.messagebox.showwarning("Error", "Expense details not found.")
        else:
            tk.messagebox.showwarning("Error", "Please select an expense from the list.")

    def refresh_expense_data(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
