import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta

class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Reservation System")

        # Create and set up the database
        self.conn = sqlite3.connect('reservation.db')
        self.cursor = self.conn.cursor()

        # Create the reservations table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                party_size INTEGER NOT NULL
            )
        ''')

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Create the treeview to display reservations
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Date', 'Time', 'Party Size'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Party Size', text='Party Size')

        # Populate the treeview
        self.load_reservations()

        # Create entry widgets
        self.name_entry = tk.Entry(self.root)
        self.date_entry = tk.Entry(self.root)
        self.time_entry = tk.Entry(self.root)
        self.party_size_entry = tk.Entry(self.root)

        # Create labels
        name_label = tk.Label(self.root, text='Name:')
        date_label = tk.Label(self.root, text='Date (YYYY-MM-DD):')
        time_label = tk.Label(self.root, text='Time (HH:MM):')
        party_size_label = tk.Label(self.root, text='Party Size:')

        # Create buttons
        reserve_button = tk.Button(self.root, text='Reserve Table', command=self.reserve_table)
        cancel_button = tk.Button(self.root, text='Cancel Reservation', command=self.cancel_reservation)

        # Grid layout
        self.tree.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        date_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)
        time_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.time_entry.grid(row=3, column=1, padx=10, pady=5)
        party_size_label.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.party_size_entry.grid(row=4, column=1, padx=10, pady=5)
        reserve_button.grid(row=1, column=2, padx=10, pady=5)
        cancel_button.grid(row=2, column=2, padx=10, pady=5)

    def load_reservations(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Retrieve data from the database
        self.cursor.execute('SELECT * FROM reservations')
        reservations = self.cursor.fetchall()

        # Populate the treeview with data
        for reservation in reservations:
            self.tree.insert('', 'end', values=reservation)

    def reserve_table(self):
        # Get values from entry widgets
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        party_size = self.party_size_entry.get()

        # Insert data into the database
        self.cursor.execute('INSERT INTO reservations (name, date, time, party_size) VALUES (?, ?, ?, ?)',
                            (name, date, time, party_size))
        self.conn.commit()

        # Clear entry widgets
        self.name_entry.delete(0, 'end')
        self.date_entry.delete(0, 'end')
        self.time_entry.delete(0, 'end')
        self.party_size_entry.delete(0, 'end')

        # Reload the treeview
        self.load_reservations()

    def cancel_reservation(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Extract the ID from the selected item
            selected_id = self.tree.item(selected_item)['values'][0]

            # Delete the selected item from the database
            self.cursor.execute('DELETE FROM reservations WHERE id = ?', (selected_id,))
            self.conn.commit()

            # Reload the treeview
            self.load_reservations()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationSystem(root)
    root.mainloop()
