import tkinter as tk

class ExampleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Example App")

        # UI components
        self.label_data = tk.Label(master, text="Enter data (comma-separated):")
        self.entry_data = tk.Entry(master)
        self.button_process = tk.Button(master, text="Process Data", command=self.process_data)

        # Layout
        self.label_data.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_data.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.button_process.grid(row=2, column=0, padx=10, pady=10)

    def process_data(self):
        # Get data from entry and do something with it (in this example, just print)
        input_data = self.entry_data.get()
        print("Entered data:", input_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()
