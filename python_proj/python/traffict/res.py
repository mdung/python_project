import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class RestaurantMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Menu Simulation")

        # Connect to SQLite database
        self.conn = sqlite3.connect("restaurant_menu.db")
        self.create_tables()

        # GUI Components
        self.label = tk.Label(master, text="Restaurant Menu Simulation")
        self.label.pack()

        self.name_label = tk.Label(master, text="Item Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.category_label = tk.Label(master, text="Item Category:")
        self.category_label.pack()

        self.category_entry = tk.Entry(master)
        self.category_entry.pack()

        self.price_label = tk.Label(master, text="Item Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(master)
        self.price_entry.pack()

        self.add_item_button = tk.Button(master, text="Add Item", command=self.add_menu_item)
        self.add_item_button.pack()

        self.menu_tree = ttk.Treeview(master, columns=("Item Name", "Category", "Price"), show="headings")
        self.menu_tree.heading("Item Name", text="Item Name")
        self.menu_tree.heading("Category", text="Category")
        self.menu_tree.heading("Price", text="Price")
        self.menu_tree.pack()

        self.load_menu_button = tk.Button(master, text="Load Menu", command=self.load_menu)
        self.load_menu_button.pack()

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    price REAL
                )
            ''')

    def add_menu_item(self):
        item_name = self.name_entry.get()
        item_category = self.category_entry.get()
        item_price = self.price_entry.get()

        if not item_name or not item_category or not item_price:
            messagebox.showwarning("Error", "Please enter all item details.")
            return

        try:
            item_price = float(item_price)
        except ValueError:
            messagebox.showwarning("Error", "Invalid price. Please enter a numeric value.")
            return

        menu_item = MenuItem(name=item_name, category=item_category, price=item_price)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO menu (name, category, price) VALUES (?, ?, ?)",
                           (menu_item.name, menu_item.category, menu_item.price))

        self.name_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

        self.load_menu()

    def load_menu(self):
        self.menu_tree.delete(*self.menu_tree.get_children())

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM menu")
            menu_items = cursor.fetchall()

            for item in menu_items:
                self.menu_tree.insert("", tk.END, values=item[1:])

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()
