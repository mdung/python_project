import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Schedule:
    def __init__(self, staff_name, shift_date, shift_time):
        self.staff_name = staff_name
        self.shift_date = shift_date
        self.shift_time = shift_time

class ScheduleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Staff Scheduling Simulation")

        # Connect to SQLite database
        self.conn = sqlite3.connect("schedule.db")
        self.create_tables()

        # GUI Components
        self.label = tk.Label(master, text="Medical Staff Scheduling Simulation")
        self.label.pack()

        self.staff_label = tk.Label(master, text="Staff Name:")
        self.staff_label.pack()

        self.staff_entry = tk.Entry(master)
        self.staff_entry.pack()

        self.role_label = tk.Label(master, text="Staff Role:")
        self.role_label.pack()

        self.role_entry = tk.Entry(master)
        self.role_entry.pack()

        self.schedule_tree = ttk.Treeview(master, columns=("Staff Name", "Shift Date", "Shift Time"), show="headings")
        self.schedule_tree.heading("Staff Name", text="Staff Name")
        self.schedule_tree.heading("Shift Date", text="Shift Date")
        self.schedule_tree.heading("Shift Time", text="Shift Time")
        self.schedule_tree.pack()

        self.create_schedule_button = tk.Button(master, text="Create Schedule", command=self.create_schedule)
        self.create_schedule_button.pack()

        self.load_schedule_button = tk.Button(master, text="Load Schedule", command=self.load_schedule)
        self.load_schedule_button.pack()

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS staff (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    role TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS schedule (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    staff_name TEXT,
                    shift_date TEXT,
                    shift_time TEXT,
                    FOREIGN KEY (staff_name) REFERENCES staff (name)
                )
            ''')

    def create_schedule(self):
        staff_name = self.staff_entry.get()
        staff_role = self.role_entry.get()

        if not staff_name or not staff_role:
            messagebox.showwarning("Error", "Please enter both Staff Name and Staff Role.")
            return

        staff = Staff(name=staff_name, role=staff_role)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO staff (name, role) VALUES (?, ?)", (staff_name, staff_role))

        self.staff_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)

        schedule_date = datetime.now().strftime("%Y-%m-%d")
        schedule_time = datetime.now().strftime("%H:%M:%S")

        schedule = Schedule(staff_name=staff_name, shift_date=schedule_date, shift_time=schedule_time)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO schedule (staff_name, shift_date, shift_time) VALUES (?, ?, ?)",
                           (staff_name, schedule_date, schedule_time))

        self.load_schedule()

    def load_schedule(self):
        self.schedule_tree.delete(*self.schedule_tree.get_children())

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM schedule")
            schedules = cursor.fetchall()

            for schedule in schedules:
                self.schedule_tree.insert("", tk.END, values=schedule[1:])

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
