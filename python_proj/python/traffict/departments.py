import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random

class Patient:
    def __init__(self, name, condition, current_department="ER"):
        self.name = name
        self.condition = condition
        self.current_department = current_department

class HospitalSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Patient Flow Simulation")

        # Connect to SQLite database
        self.conn = sqlite3.connect("hospital_flow.db")
        self.create_tables()

        # GUI Components
        self.label = tk.Label(master, text="Hospital Patient Flow Simulation")
        self.label.pack()

        self.name_label = tk.Label(master, text="Patient Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.condition_label = tk.Label(master, text="Patient Condition:")
        self.condition_label.pack()

        self.condition_entry = tk.Entry(master)
        self.condition_entry.pack()

        self.flow_tree = ttk.Treeview(master, columns=("Patient Name", "Condition", "Current Department"), show="headings")
        self.flow_tree.heading("Patient Name", text="Patient Name")
        self.flow_tree.heading("Condition", text="Condition")
        self.flow_tree.heading("Current Department", text="Current Department")
        self.flow_tree.pack()

        self.move_patient_button = tk.Button(master, text="Move Patient", command=self.move_patient)
        self.move_patient_button.pack()

        self.load_flow_button = tk.Button(master, text="Load Patient Flow", command=self.load_patient_flow)
        self.load_flow_button.pack()

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    condition TEXT,
                    current_department TEXT
                )
            ''')

    def move_patient(self):
        patient_name = self.name_entry.get()
        patient_condition = self.condition_entry.get()

        if not patient_name or not patient_condition:
            messagebox.showwarning("Error", "Please enter both Patient Name and Condition.")
            return

        patient = Patient(name=patient_name, condition=patient_condition)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO patients (name, condition, current_department) VALUES (?, ?, ?)",
                           (patient_name, patient_condition, patient.current_department))

        self.name_entry.delete(0, tk.END)
        self.condition_entry.delete(0, tk.END)

        self.load_patient_flow()

    def load_patient_flow(self):
        self.flow_tree.delete(*self.flow_tree.get_children())

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM patients")
            patients = cursor.fetchall()

            for patient in patients:
                self.flow_tree.insert("", tk.END, values=patient[1:])

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalSimulation(root)
    root.mainloop()
