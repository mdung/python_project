import tkinter as tk

class SearchApp(tk.Tk):
    def __init__(self, dataset):
        super().__init__()

        self.title("Search Algorithm")
        self.geometry("400x200")

        self.dataset = dataset

        self.target_label = tk.Label(self, text="Target Element:")
        self.target_label.pack(pady=10)

        self.target_entry = tk.Entry(self)
        self.target_entry.pack(pady=5)

        self.search_button = tk.Button(self, text="Search", command=self.search_element)
        self.search_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def search_element(self):
        target = self.target_entry.get()

        try:
            target = int(target)
            result = self.linear_search(target)
            self.display_result(result)
        except ValueError:
            self.result_label.config(text="Invalid target element. Please enter an integer.")

    def linear_search(self, target):
        for index, element in enumerate(self.dataset):
            if element == target:
                return index

        return -1

    def display_result(self, result):
        if result != -1:
            self.result_label.config(text=f"Element found at index {result}.")
        else:
            self.result_label.config(text="Element not found in the dataset.")

if __name__ == "__main__":
    dataset = [12, 45, 23, 67, 89, 34, 56, 78, 98, 21]

    search_app = SearchApp(dataset)
    search_app.mainloop()
