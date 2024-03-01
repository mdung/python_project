import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# Create a SQLite database and table for inventory
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        date_added TEXT NOT NULL
    )
''')
conn.commit()

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        # Create and configure the Treeview widget for displaying inventory
        self.tree = ttk.Treeview(root, columns=('ID', 'Product Name', 'Quantity', 'Date Added'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Product Name', text='Product Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Date Added', text='Date Added')
        self.tree.pack(pady=10)

        # Create and configure the Entry widgets and buttons
        self.product_name_var = tk.StringVar()
        self.quantity_var = tk.IntVar()

        tk.Label(root, text="Product Name:").pack()
        self.product_name_entry = tk.Entry(root, textvariable=self.product_name_var)
        self.product_name_entry.pack()

        tk.Label(root, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(root, textvariable=self.quantity_var)
        self.quantity_entry.pack()

        tk.Button(root, text="Add to Inventory", command=self.add_to_inventory).pack(pady=10)
        tk.Button(root, text="Refresh Inventory", command=self.refresh_inventory).pack(pady=10)

        # Initialize the inventory display
        self.refresh_inventory()

    def add_to_inventory(self):
        product_name = self.product_name_var.get()
        quantity = self.quantity_var.get()
        date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute('INSERT INTO inventory (product_name, quantity, date_added) VALUES (?, ?, ?)',
                       (product_name, quantity, date_added))
        conn.commit()

        # Refresh the inventory display
        self.refresh_inventory()

    def refresh_inventory(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM inventory')
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
