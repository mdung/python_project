import tkinter as tk
from tkinter import messagebox

class LongestIncreasingSubarrayApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Longest Increasing Subarray Solver")

        self.label = tk.Label(master, text="Enter space-separated numbers:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.solve_button = tk.Button(master, text="Solve", command=self.solve_problem)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def solve_problem(self):
        try:
            numbers = [int(x) for x in self.entry.get().split()]
            if not numbers:
                raise ValueError("Please enter valid numbers.")

            longest_increasing_subarray = self.find_longest_increasing_subarray(numbers)
            result_message = f"The longest increasing subarray is: {longest_increasing_subarray}"
            self.result_label.config(text=result_message)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.result_label.config(text="")

    def find_longest_increasing_subarray(self, nums):
        if not nums:
            return []

        max_length = 1
        current_length = 1
        start_index = 0
        max_length_start = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    max_length_start = start_index
                current_length = 1
                start_index = i

        # Check the last subarray
        if current_length > max_length:
            max_length_start = start_index

        return nums[max_length_start:max_length_start + max_length]

if __name__ == "__main__":
    root = tk.Tk()
    app = LongestIncreasingSubarrayApp(root)
    root.mainloop()
