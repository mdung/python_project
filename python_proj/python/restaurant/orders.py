import tkinter as tk
from tkinter import ttk
import sqlite3

class OrderSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Management System")

        # Create and set up the database
        self.conn = sqlite3.connect('orders.db')
        self.cursor = self.conn.cursor()

        # Create the orders table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                order_type TEXT NOT NULL,
                items TEXT NOT NULL,
                total_price REAL NOT NULL
            )
        ''')

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Create the treeview to display orders
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Customer Name', 'Order Type', 'Items', 'Total Price'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Customer Name', text='Customer Name')
        self.tree.heading('Order Type', text='Order Type')
        self.tree.heading('Items', text='Items')
        self.tree.heading('Total Price', text='Total Price')

        # Populate the treeview
        self.load_orders()

        # Create entry widgets
        self.customer_name_entry = tk.Entry(self.root)
        self.order_type_var = tk.StringVar(value="Dine-In")
        self.order_type_combo = ttk.Combobox(self.root, textvariable=self.order_type_var, values=["Dine-In", "Takeout"])
        self.items_entry = tk.Entry(self.root)
        self.total_price_entry = tk.Entry(self.root)

        # Create labels
        customer_name_label = tk.Label(self.root, text='Customer Name:')
        order_type_label = tk.Label(self.root, text='Order Type:')
        items_label = tk.Label(self.root, text='Items:')
        total_price_label = tk.Label(self.root, text='Total Price:')

        # Create buttons
        place_order_button = tk.Button(self.root, text='Place Order', command=self.place_order)
        cancel_order_button = tk.Button(self.root, text='Cancel Order', command=self.cancel_order)

        # Grid layout
        self.tree.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        customer_name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=5)
        order_type_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.order_type_combo.grid(row=2, column=1, padx=10, pady=5)
        items_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.items_entry.grid(row=3, column=1, padx=10, pady=5)
        total_price_label.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.total_price_entry.grid(row=4, column=1, padx=10, pady=5)
        place_order_button.grid(row=1, column=2, padx=10, pady=5)
        cancel_order_button.grid(row=2, column=2, padx=10, pady=5)

    def load_orders(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Retrieve data from the database
        self.cursor.execute('SELECT * FROM orders')
        orders = self.cursor.fetchall()

        # Populate the treeview with data
        for order in orders:
            self.tree.insert('', 'end', values=order)

    def place_order(self):
        # Get values from entry widgets
        customer_name = self.customer_name_entry.get()
        order_type = self.order_type_var.get()
        items = self.items_entry.get()
        total_price = self.total_price_entry.get()

        # Insert data into the database
        self.cursor.execute('INSERT INTO orders (customer_name, order_type, items, total_price) VALUES (?, ?, ?, ?)',
                            (customer_name, order_type, items, total_price))
        self.conn.commit()

        # Clear entry widgets
        self.customer_name_entry.delete(0, 'end')
        self.order_type_var.set("Dine-In")
        self.items_entry.delete(0, 'end')
        self.total_price_entry.delete(0, 'end')

        # Reload the treeview
        self.load_orders()

    def cancel_order(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Extract the ID from the selected item
            selected_id = self.tree.item(selected_item)['values'][0]

            # Delete the selected item from the database
            self.cursor.execute('DELETE FROM orders WHERE id = ?', (selected_id,))
            self.conn.commit()

            # Reload the treeview
            self.load_orders()

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderSystem(root)
    root.mainloop()
