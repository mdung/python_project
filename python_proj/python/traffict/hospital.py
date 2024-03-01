import tkinter as tk
from tkinter import messagebox
import random

class Patient:
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

class HospitalSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Admission and Discharge Simulation")

        self.patients = []

        # GUI Components
        self.label = tk.Label(master, text="Hospital Simulation")
        self.label.pack()

        self.admit_button = tk.Button(master, text="Admit Patient", command=self.admit_patient)
        self.admit_button.pack()

        self.discharge_button = tk.Button(master, text="Discharge Patient", command=self.discharge_patient)
        self.discharge_button.pack()

        self.patient_listbox = tk.Listbox(master)
        self.patient_listbox.pack()

    def admit_patient(self):
        patient_name = f"Patient-{len(self.patients) + 1}"
        patient_condition = random.choice(["Critical", "Serious", "Stable"])
        patient = Patient(name=patient_name, condition=patient_condition)
        self.patients.append(patient)
        self.update_patient_list()

    def discharge_patient(self):
        selected_index = self.patient_listbox.curselection()
        if selected_index:
            selected_patient = self.patients.pop(selected_index[0])
            messagebox.showinfo("Discharge", f"{selected_patient.name} discharged.")
            self.update_patient_list()
        else:
            messagebox.showwarning("Error", "Select a patient to discharge.")

    def update_patient_list(self):
        self.patient_listbox.delete(0, tk.END)
        for patient in self.patients:
            self.patient_listbox.insert(tk.END, f"{patient.name} - {patient.condition}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalSimulation(root)
    root.mainloop()
