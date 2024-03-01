import os
import tkinter as tk
from tkinter import filedialog

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")

        # Initialize current directory
        self.current_directory = os.getcwd()

        # Create and configure the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create and configure the listbox
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(expand=tk.YES, fill=tk.BOTH)
        self.listbox.bind('<Double-Button-1>', self.on_double_click)

        # Create and configure the scrollbar
        scrollbar = tk.Scrollbar(self.listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Create and configure buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        button_open = tk.Button(frame_buttons, text="Open", command=self.open_directory)
        button_open.grid(row=0, column=0, padx=5)

        button_delete = tk.Button(frame_buttons, text="Delete", command=self.delete_file)
        button_delete.grid(row=0, column=1, padx=5)

        button_exit = tk.Button(frame_buttons, text="Exit", command=self.root.destroy)
        button_exit.grid(row=0, column=2, padx=5)

        # Update the listbox with the files in the current directory
        self.update_listbox()

    def open_directory(self):
        # Ask the user to select a directory
        directory = filedialog.askdirectory(initialdir=self.current_directory, title="Select Directory")
        if directory:
            self.current_directory = directory
            self.update_listbox()

    def delete_file(self):
        # Get the selected file
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_file = self.listbox.get(selected_index)
            file_path = os.path.join(self.current_directory, selected_file)

            # Confirm deletion
            confirm = tk.messagebox.askyesno("Delete", f"Do you want to delete '{selected_file}'?")
            if confirm:
                # Delete the file
                os.remove(file_path)
                self.update_listbox()

    def on_double_click(self, event):
        # Open the selected file or directory on double-click
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_file = self.listbox.get(selected_index)
            file_path = os.path.join(self.current_directory, selected_file)

            if os.path.isdir(file_path):
                self.current_directory = file_path
                self.update_listbox()

    def update_listbox(self):
        # Update the listbox with files in the current directory
        self.listbox.delete(0, tk.END)
        files = os.listdir(self.current_directory)
        for file in files:
            self.listbox.insert(tk.END, file)

if __name__ == "__main__":
    root = tk.Tk()
    file_explorer = FileExplorer(root)
    root.mainloop()
