import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta

class RestaurantPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant POS System")

        # Create and set up the database
        self.conn = sqlite3.connect('restaurant_management.db')
        self.cursor = self.conn.cursor()

        # Create tables if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                order_time TEXT NOT NULL,
                FOREIGN KEY (item_id) REFERENCES menu (id)
            )
        ''')

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Create the menu treeview
        self.menu_tree = ttk.Treeview(self.root, columns=('ID', 'Item Name', 'Price'), show='headings')
        self.menu_tree.heading('ID', text='ID')
        self.menu_tree.heading('Item Name', text='Item Name')
        self.menu_tree.heading('Price', text='Price')

        # Populate the menu treeview
        self.load_menu()

        # Create entry widgets
        self.item_name_entry = tk.Entry(self.root)
        self.price_entry = tk.Entry(self.root)
        self.quantity_entry = tk.Entry(self.root)

        # Create labels
        item_name_label = tk.Label(self.root, text='Item Name:')
        price_label = tk.Label(self.root, text='Price:')
        quantity_label = tk.Label(self.root, text='Quantity:')

        # Create buttons
        add_to_order_button = tk.Button(self.root, text='Add to Order', command=self.add_to_order)
        process_order_button = tk.Button(self.root, text='Process Order', command=self.process_order)

        # Grid layout for menu treeview
        self.menu_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Grid layout for order entry
        item_name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.item_name_entry.grid(row=1, column=1, padx=10, pady=5)
        price_label.grid(row=1, column=2, padx=10, pady=5, sticky='e')
        self.price_entry.grid(row=1, column=3, padx=10, pady=5)
        quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)
        add_to_order_button.grid(row=2, column=2, padx=10, pady=5)
        process_order_button.grid(row=2, column=3, padx=10, pady=5)

    def load_menu(self):
        # Clear the menu treeview
        for row in self.menu_tree.get_children():
            self.menu_tree.delete(row)

        # Retrieve data from the database
        self.cursor.execute('SELECT * FROM menu')
        menu_items = self.cursor.fetchall()

        # Populate the menu treeview with data
        for item in menu_items:
            self.menu_tree.insert('', 'end', values=item)

    def add_to_order(self):
        # Get values from entry widgets
        item_name = self.item_name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        # Insert data into the orders table
        self.cursor.execute('INSERT INTO orders (item_id, quantity, total_price, order_time) VALUES (?, ?, ?, ?)',
                            (1, quantity, float(price) * int(quantity), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()

        # Reload the menu treeview
        self.load_menu()

    def process_order(self):
        # Calculate the total price for the order
        self.cursor.execute('SELECT SUM(total_price) FROM orders')
        total_price = self.cursor.fetchone()[0]

        # Generate a receipt
        receipt_text = f"Order Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        receipt_text += "Items\t\tQuantity\t\tTotal Price\n"

        # Retrieve order details
        self.cursor.execute('''
            SELECT menu.item_name, orders.quantity, orders.total_price
            FROM orders
            JOIN menu ON orders.item_id = menu.id
        ''')
        order_details = self.cursor.fetchall()

        # Add order details to the receipt
        for item in order_details:
            receipt_text += f"{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}\n"

        receipt_text += f"\nTotal Price: {total_price}"

        # Display the receipt in a new window
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")

        receipt_label = tk.Label(receipt_window, text=receipt_text, justify='left')
        receipt_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantPOS(root)
    root.mainloop()
