import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# Create a SQLite database and table for CRM data
conn = sqlite3.connect('crm.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        lead_status TEXT NOT NULL,
        date_added TEXT NOT NULL
    )
''')
conn.commit()

class CRMSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Relationship Management (CRM) System")

        # Create and configure the Treeview widget for displaying customer data
        self.tree = ttk.Treeview(root, columns=('ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Lead Status', 'Date Added'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('First Name', text='First Name')
        self.tree.heading('Last Name', text='Last Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Phone Number', text='Phone Number')
        self.tree.heading('Lead Status', text='Lead Status')
        self.tree.heading('Date Added', text='Date Added')
        self.tree.pack(pady=10)

        # Create and configure the Entry widgets and buttons
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_number_var = tk.StringVar()
        self.lead_status_var = tk.StringVar()

        tk.Label(root, text="First Name:").pack()
        self.first_name_entry = tk.Entry(root, textvariable=self.first_name_var)
        self.first_name_entry.pack()

        tk.Label(root, text="Last Name:").pack()
        self.last_name_entry = tk.Entry(root, textvariable=self.last_name_var)
        self.last_name_entry.pack()

        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.pack()

        tk.Label(root, text="Phone Number:").pack()
        self.phone_number_entry = tk.Entry(root, textvariable=self.phone_number_var)
        self.phone_number_entry.pack()

        tk.Label(root, text="Lead Status:").pack()
        self.lead_status_entry = tk.Entry(root, textvariable=self.lead_status_var)
        self.lead_status_entry.pack()

        tk.Button(root, text="Add Customer", command=self.add_customer).pack(pady=10)
        tk.Button(root, text="View Customer Details", command=self.view_customer_details).pack(pady=10)

        # Initialize the customer data display
        self.refresh_customer_data()

    def add_customer(self):
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        email = self.email_var.get()
        phone_number = self.phone_number_var.get()
        lead_status = self.lead_status_var.get()
        date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute('INSERT INTO customers (first_name, last_name, email, phone_number, lead_status, date_added) VALUES (?, ?, ?, ?, ?, ?)',
                       (first_name, last_name, email, phone_number, lead_status, date_added))
        conn.commit()

        # Refresh the customer data display
        self.refresh_customer_data()

    def view_customer_details(self):
        selected_item = self.tree.selection()
        if selected_item:
            customer_id = self.tree.item(selected_item, 'values')[0]
            # Fetch customer details from the database and display them
            cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
            customer_details = cursor.fetchone()
            if customer_details:
                tk.messagebox.showinfo("Customer Details", f"ID: {customer_details[0]}\nFirst Name: {customer_details[1]}\nLast Name: {customer_details[2]}\nEmail: {customer_details[3]}\nPhone Number: {customer_details[4]}\nLead Status: {customer_details[5]}\nDate Added: {customer_details[6]}")
            else:
                tk.messagebox.showwarning("Error", "Customer details not found.")
        else:
            tk.messagebox.showwarning("Error", "Please select a customer from the list.")

    def refresh_customer_data(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM customers')
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRMSystem(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
