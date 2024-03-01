import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random

class Patient:
    def __init__(self, name, condition, triage_status="Pending"):
        self.name = name
        self.condition = condition
        self.triage_status = triage_status

class TriageSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Emergency Department Triage Simulation")

        # Connect to SQLite database
        self.conn = sqlite3.connect("triage.db")
        self.create_tables()

        # GUI Components
        self.label = tk.Label(master, text="Emergency Department Triage Simulation")
        self.label.pack()

        self.name_label = tk.Label(master, text="Patient Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.condition_label = tk.Label(master, text="Patient Condition:")
        self.condition_label.pack()

        self.condition_entry = tk.Entry(master)
        self.condition_entry.pack()

        self.triage_tree = ttk.Treeview(master, columns=("Patient Name", "Condition", "Triage Status"), show="headings")
        self.triage_tree.heading("Patient Name", text="Patient Name")
        self.triage_tree.heading("Condition", text="Condition")
        self.triage_tree.heading("Triage Status", text="Triage Status")
        self.triage_tree.pack()

        self.triage_button = tk.Button(master, text="Perform Triage", command=self.perform_triage)
        self.triage_button.pack()

        self.load_triage_button = tk.Button(master, text="Load Triage", command=self.load_triage)
        self.load_triage_button.pack()

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    condition TEXT,
                    triage_status TEXT
                )
            ''')

    def perform_triage(self):
        patient_name = self.name_entry.get()
        patient_condition = self.condition_entry.get()

        if not patient_name or not patient_condition:
            messagebox.showwarning("Error", "Please enter both Patient Name and Condition.")
            return

        triage_status = self.triage_logic(patient_condition)

        patient = Patient(name=patient_name, condition=patient_condition, triage_status=triage_status)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO patients (name, condition, triage_status) VALUES (?, ?, ?)",
                           (patient_name, patient_condition, triage_status))

        self.name_entry.delete(0, tk.END)
        self.condition_entry.delete(0, tk.END)

        self.load_triage()

    def triage_logic(self, condition):
        # Implement your triage logic here based on patient condition
        # For simplicity, we'll use a random choice for demonstration
        triage_options = ["Critical", "Urgent", "Standard"]
        return random.choice(triage_options)

    def load_triage(self):
        self.triage_tree.delete(*self.triage_tree.get_children())

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM patients")
            patients = cursor.fetchall()

            for patient in patients:
                self.triage_tree.insert("", tk.END, values=patient[1:])

if __name__ == "__main__":
    root = tk.Tk()
    app = TriageSimulation(root)
    root.mainloop()
