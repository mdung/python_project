import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# Create a SQLite database and table for time tracking data
conn = sqlite3.connect('time_tracking_system.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS time_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT,
        total_hours REAL
    )
''')
conn.commit()

class TimeTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Tracking System")

        # Create and configure the Treeview widget for displaying time records
        self.tree = ttk.Treeview(root, columns=('ID', 'Employee Name', 'Start Time', 'End Time', 'Total Hours'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Employee Name', text='Employee Name')
        self.tree.heading('Start Time', text='Start Time')
        self.tree.heading('End Time', text='End Time')
        self.tree.heading('Total Hours', text='Total Hours')
        self.tree.pack(pady=10)

        # Create and configure the Entry widgets and buttons
        self.employee_name_var = tk.StringVar()
        self.start_time_var = tk.StringVar()
        self.end_time_var = tk.StringVar()

        tk.Label(root, text="Employee Name:").pack()
        self.employee_name_entry = tk.Entry(root, textvariable=self.employee_name_var)
        self.employee_name_entry.pack()

        tk.Label(root, text="Start Time:").pack()
        self.start_time_entry = tk.Entry(root, textvariable=self.start_time_var)
        self.start_time_entry.pack()

        tk.Label(root, text="End Time:").pack()
        self.end_time_entry = tk.Entry(root, textvariable=self.end_time_var)
        self.end_time_entry.pack()

        tk.Button(root, text="Log Time", command=self.log_time).pack(pady=10)
        tk.Button(root, text="Calculate Total Hours", command=self.calculate_total_hours).pack(pady=10)

        # Initialize the time records display
        self.refresh_time_records()

    def log_time(self):
        employee_name = self.employee_name_var.get()
        start_time = self.start_time_var.get()
        end_time = self.end_time_var.get()

        # Insert data into the database
        cursor.execute('INSERT INTO time_records (employee_name, start_time, end_time) VALUES (?, ?, ?)',
                       (employee_name, start_time, end_time))
        conn.commit()

        # Refresh the time records display
        self.refresh_time_records()

    def calculate_total_hours(self):
        selected_item = self.tree.selection()
        if selected_item:
            time_record_id = self.tree.item(selected_item, 'values')[0]
            cursor.execute('SELECT start_time, end_time FROM time_records WHERE id = ?', (time_record_id,))
            times = cursor.fetchone()
            if times and times[0] and times[1]:
                start_time = datetime.strptime(times[0], '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime(times[1], '%Y-%m-%d %H:%M:%S')
                total_hours = (end_time - start_time).total_seconds() / 3600
                cursor.execute('UPDATE time_records SET total_hours = ? WHERE id = ?', (total_hours, time_record_id))
                conn.commit()

                # Refresh the time records display
                self.refresh_time_records()
            else:
                tk.messagebox.showwarning("Error", "Invalid time records.")
        else:
            tk.messagebox.showwarning("Error", "Please select a time record from the list.")

    def refresh_time_records(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM time_records')
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTrackingApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
