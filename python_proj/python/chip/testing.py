import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import random
from datetime import datetime

class ChipTestingApp:
    def __init__(self, master):
        self.master = master
        master.title("Chip Testing Automation System")

        self.create_widgets()

    def create_widgets(self):
        self.test_button = ttk.Button(self.master, text="Start Test", command=self.start_test)
        self.test_button.pack(pady=10)

        self.results_label = tk.Label(self.master, text="")
        self.results_label.pack(pady=10)

    def start_test(self):
        test_results = self.run_chip_tests()
        self.display_test_results(test_results)

    def run_chip_tests(self):
        # Simulate chip testing process
        test_results = []
        for chip_id in range(1, 11):
            result = {
                "ChipID": chip_id,
                "TestDateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "TestResult": random.choice(["Pass", "Fail"]),
                "Defects": random.randint(0, 5)
            }
            test_results.append(result)

        # Save results to a CSV file
        df = pd.DataFrame(test_results)
        df.to_csv("chip_test_results.csv", index=False)

        return test_results

    def display_test_results(self, test_results):
        if test_results:
            results_text = "Test Results:\n"
            for result in test_results:
                results_text += f"Chip ID: {result['ChipID']}, Test Result: {result['TestResult']}, Defects: {result['Defects']}\n"
            self.results_label.config(text=results_text)
            messagebox.showinfo("Test Completed", "Chip testing completed successfully!")
        else:
            self.results_label.config(text="No test results available.")
            messagebox.showwarning("No Results", "No test results available.")

if __name__ == '__main__':
    root = tk.Tk()
    app = ChipTestingApp(root)
    root.mainloop()
