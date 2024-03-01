import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class Patient:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity

class HospitalSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Bed Allocation Simulation")

        # Connect to SQLite database
        self.conn = sqlite3.connect("hospital.db")
        self.create_tables()

        # GUI Components
        self.label = tk.Label(master, text="Hospital Bed Allocation Simulation")
        self.label.pack()

        self.admit_button = tk.Button(master, text="Admit Patient", command=self.admit_patient)
        self.admit_button.pack()

        self.discharge_button = tk.Button(master, text="Discharge Patient", command=self.discharge_patient)
        self.discharge_button.pack()

        self.patient_listbox = tk.Listbox(master)
        self.patient_listbox.pack()

        self.load_patients()

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    severity INTEGER
                )
            ''')

    def load_patients(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM patients")
            patients = cursor.fetchall()

            self.patients = [Patient(name, severity) for _, name, severity in patients]
            self.update_patient_list()

    def admit_patient(self):
        patient_name = f"Patient-{len(self.patients) + 1}"
        patient_severity = random.randint(1, 5)
        patient = Patient(name=patient_name, severity=patient_severity)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO patients (name, severity) VALUES (?, ?)", (patient_name, patient_severity))

        self.patients.append(patient)
        self.update_patient_list()

    def discharge_patient(self):
        selected_index = self.patient_listbox.curselection()
        if selected_index:
            selected_patient = self.patients.pop(selected_index[0])

            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM patients WHERE name=?", (selected_patient.name,))

            messagebox.showinfo("Discharge", f"{selected_patient.name} discharged.")
            self.update_patient_list()
        else:
            messagebox.showwarning("Error", "Select a patient to discharge.")

    def update_patient_list(self):
        self.patient_listbox.delete(0, tk.END)
        for patient in self.patients:
            self.patient_listbox.insert(tk.END, f"{patient.name} - Severity: {patient.severity}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalSimulation(root)
    root.mainloop()
