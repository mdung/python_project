import csv
import numpy as np

def generate_random_data_csv(file_path, num_samples=100, num_features=2):
    random_data = np.random.rand(num_samples, num_features)
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in random_data:
            csv_writer.writerow(row)

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    # Ask user for the file path to save the generated CSV file
    save_path = filedialog.asksaveasfilename(
        title="Save CSV File", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if save_path:
        generate_random_data_csv(save_path)
        print(f"CSV file generated and saved at {save_path}")
