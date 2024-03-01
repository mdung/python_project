import tkinter as tk
from tkinter import ttk
import sqlite3

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Specials Management")

        # Create and set up the database
        self.conn = sqlite3.connect('restaurant.db')
        self.cursor = self.conn.cursor()

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Create the treeview to display specials
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Description', 'Price'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Price', text='Price')

        # Populate the treeview
        self.load_specials()

        # Create entry widgets
        self.name_entry = tk.Entry(self.root)
        self.desc_entry = tk.Entry(self.root)
        self.price_entry = tk.Entry(self.root)

        # Create labels
        name_label = tk.Label(self.root, text='Name:')
        desc_label = tk.Label(self.root, text='Description:')
        price_label = tk.Label(self.root, text='Price:')

        # Create buttons
        add_button = tk.Button(self.root, text='Add Special', command=self.add_special)
        delete_button = tk.Button(self.root, text='Delete Special', command=self.delete_special)

        # Grid layout
        self.tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        desc_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.desc_entry.grid(row=2, column=1, padx=10, pady=5)
        price_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)
        add_button.grid(row=1, column=2, padx=10, pady=5)
        delete_button.grid(row=2, column=2, padx=10, pady=5)

        # Bind double-click event on treeview to update entry widgets
        self.tree.bind('<Double-1>', self.update_entries)

    def load_specials(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Retrieve data from the database
        self.cursor.execute('SELECT * FROM specials')
        specials = self.cursor.fetchall()

        # Populate the treeview with data
        for special in specials:
            self.tree.insert('', 'end', values=special)

    def add_special(self):
        # Get values from entry widgets
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        price = self.price_entry.get()

        # Insert data into the database
        self.cursor.execute('INSERT INTO specials (name, description, price) VALUES (?, ?, ?)', (name, desc, price))
        self.conn.commit()

        # Clear entry widgets
        self.name_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')

        # Reload the treeview
        self.load_specials()

    def delete_special(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Extract the ID from the selected item
            selected_id = self.tree.item(selected_item)['values'][0]

            # Delete the selected item from the database
            self.cursor.execute('DELETE FROM specials WHERE id = ?', (selected_id,))
            self.conn.commit()

            # Reload the treeview
            self.load_specials()

    def update_entries(self, event):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Extract values from the selected item
            selected_values = self.tree.item(selected_item)['values']

            # Update entry widgets with selected values
            self.name_entry.delete(0, 'end')
            self.name_entry.insert('end', selected_values[1])

            self.desc_entry.delete(0, 'end')
            self.desc_entry.insert('end', selected_values[2])

            self.price_entry.delete(0, 'end')
            self.price_entry.insert('end', selected_values[3])

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
