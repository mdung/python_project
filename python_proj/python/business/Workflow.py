import tkinter as tk
from tkinter import ttk, simpledialog
import sqlite3

class WorkflowAutomationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Workflow Automation System")

        # Database setup
        self.connection = sqlite3.connect("workflow.db")
        self.cursor = self.connection.cursor()
        self.create_table()

        # Create and set up the GUI components
        self.tree = ttk.Treeview(self.master, columns=("Task", "Status"), show="headings")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Status", text="Status")
        self.tree.pack(padx=10, pady=10)

        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.edit_task_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack()

        self.delete_task_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.load_tasks()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "Pending"))
            self.connection.commit()
            self.load_tasks()

    def edit_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item, "values")[0]
            current_task = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (task_id,)).fetchone()[0]
            updated_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
            if updated_task:
                self.cursor.execute("UPDATE tasks SET task=? WHERE id=?", (updated_task, task_id))
                self.connection.commit()
                self.load_tasks()

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item, "values")[0]
            self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            self.connection.commit()
            self.load_tasks()

    def load_tasks(self):
        self.tree.delete(*self.tree.get_children())
        tasks = self.cursor.execute("SELECT id, task, status FROM tasks").fetchall()
        for task in tasks:
            self.tree.insert("", "end", values=task)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkflowAutomationApp(root)
    root.mainloop()
