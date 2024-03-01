import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# Create a SQLite database and tables for project and task data
conn = sqlite3.connect('project_management.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL,
        date_created TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        task_name TEXT NOT NULL,
        is_completed INTEGER NOT NULL,
        date_added TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects(id)
    )
''')
conn.commit()

class ProjectManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Management Tool")

        # Create and configure the Treeview widget for displaying project and task data
        self.project_tree = ttk.Treeview(root, columns=('ID', 'Project Name', 'Date Created'), show='headings')
        self.project_tree.heading('ID', text='ID')
        self.project_tree.heading('Project Name', text='Project Name')
        self.project_tree.heading('Date Created', text='Date Created')
        self.project_tree.pack(pady=10)

        self.task_tree = ttk.Treeview(root, columns=('ID', 'Project ID', 'Task Name', 'Completed', 'Date Added'), show='headings')
        self.task_tree.heading('ID', text='ID')
        self.task_tree.heading('Project ID', text='Project ID')
        self.task_tree.heading('Task Name', text='Task Name')
        self.task_tree.heading('Completed', text='Completed')
        self.task_tree.heading('Date Added', text='Date Added')
        self.task_tree.pack(pady=10)

        # Create and configure the Entry widgets and buttons
        self.project_name_var = tk.StringVar()
        self.task_name_var = tk.StringVar()

        tk.Label(root, text="Project Name:").pack()
        self.project_name_entry = tk.Entry(root, textvariable=self.project_name_var)
        self.project_name_entry.pack()

        tk.Label(root, text="Task Name:").pack()
        self.task_name_entry = tk.Entry(root, textvariable=self.task_name_var)
        self.task_name_entry.pack()

        tk.Button(root, text="Add Project", command=self.add_project).pack(pady=5)
        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Mark Task as Completed", command=self.mark_task_completed).pack(pady=5)
        tk.Button(root, text="View Project Details", command=self.view_project_details).pack(pady=5)

        # Initialize the project and task data displays
        self.refresh_project_data()
        self.refresh_task_data()

    def add_project(self):
        project_name = self.project_name_var.get()
        date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute('INSERT INTO projects (project_name, date_created) VALUES (?, ?)',
                       (project_name, date_created))
        conn.commit()

        # Refresh the project data display
        self.refresh_project_data()

    def add_task(self):
        selected_project = self.project_tree.selection()
        if selected_project:
            project_id = self.project_tree.item(selected_project, 'values')[0]
            task_name = self.task_name_var.get()
            is_completed = 0
            date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insert data into the database
            cursor.execute('INSERT INTO tasks (project_id, task_name, is_completed, date_added) VALUES (?, ?, ?, ?)',
                           (project_id, task_name, is_completed, date_added))
            conn.commit()

            # Refresh the task data display
            self.refresh_task_data()
        else:
            tk.messagebox.showwarning("Error", "Please select a project from the list.")

    def mark_task_completed(self):
        selected_task = self.task_tree.selection()
        if selected_task:
            task_id = self.task_tree.item(selected_task, 'values')[0]
            cursor.execute('UPDATE tasks SET is_completed = 1 WHERE id = ?', (task_id,))
            conn.commit()

            # Refresh the task data display
            self.refresh_task_data()
        else:
            tk.messagebox.showwarning("Error", "Please select a task from the list.")

    def view_project_details(self):
        selected_project = self.project_tree.selection()
        if selected_project:
            project_id = self.project_tree.item(selected_project, 'values')[0]
            # Fetch project details from the database and display them
            cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
            project_details = cursor.fetchone()
            if project_details:
                # Fetch tasks associated with the project from the database
                cursor.execute('SELECT * FROM tasks WHERE project_id = ?', (project_id,))
                task_details = cursor.fetchall()

                # Display project and task details
                project_details_str = f"ID: {project_details[0]}\nProject Name: {project_details[1]}\nDate Created: {project_details[2]}\n"
                task_details_str = "Tasks:\n"
                for task in task_details:
                    task_details_str += f"  - ID: {task[0]}, Task Name: {task[2]}, Completed: {'Yes' if task[3] == 1 else 'No'}, Date Added: {task[4]}\n"

                tk.messagebox.showinfo("Project Details", project_details_str + task_details_str)
            else:
                tk.messagebox.showwarning("Error", "Project details not found.")
        else:
            tk.messagebox.showwarning("Error", "Please select a project from the list.")

    def refresh_project_data(self):
        # Clear existing data in the Treeview
        for item in self.project_tree.get_children():
            self.project_tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM projects')
        rows = cursor.fetchall()

        for row in rows:
            self.project_tree.insert('', 'end', values=row)

    def refresh_task_data(self):
        # Clear existing data in the Treeview
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)

        # Fetch data from the database and populate the Treeview
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()

        for row in rows:
            self.task_tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectManagementApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
