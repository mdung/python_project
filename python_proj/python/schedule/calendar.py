import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class CalendarScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Scheduler")

        self.create_widgets()
        self.setup_database()

    def create_widgets(self):
        self.event_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=15, width=40)
        self.event_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Event", command=self.delete_event)
        self.delete_button.pack(pady=5)

    def setup_database(self):
        self.conn = sqlite3.connect("calendar.db")
        self.cursor = self.conn.cursor()

        # Create events table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_name TEXT,
                event_date TEXT
            )
        ''')
        self.conn.commit()

        # Load existing events
        self.load_events()

    def load_events(self):
        self.event_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM events")
        events = self.cursor.fetchall()
        for event in events:
            self.event_listbox.insert(tk.END, f"{event[1]} - {event[2]}")

    def add_event(self):
        event_name = simple_input_dialog("Enter event name:")
        if not event_name:
            return

        event_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("INSERT INTO events (event_name, event_date) VALUES (?, ?)", (event_name, event_date))
        self.conn.commit()

        self.load_events()

    def delete_event(self):
        selected_index = self.event_listbox.curselection()
        if not selected_index:
            return

        event_id = selected_index[0] + 1  # Adding 1 since SQLite uses 1-based indexing
        confirm_delete = messagebox.askokcancel("Delete Event", "Are you sure you want to delete this event?")

        if confirm_delete:
            self.cursor.execute("DELETE FROM events WHERE id=?", (event_id,))
            self.conn.commit()
            self.load_events()

def simple_input_dialog(prompt):
    return simple_dialog("Input", prompt)

def simple_dialog(title, prompt):
    return messagebox.askstring(title, prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarScheduler(root)
    root.mainloop()
