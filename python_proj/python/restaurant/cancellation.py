import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from plyer import notification  # Install plyer: pip install plyer

class ReservationSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Cancellation System")

        # Database setup
        self.conn = sqlite3.connect('reservation_data.db')
        self.create_table()

        # GUI components
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           date TEXT,
                           status TEXT)''')
        self.conn.commit()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, sticky="w")

        ttk.Label(input_frame, text="Date:").grid(row=1, column=0, sticky="e")
        self.date_entry = ttk.Entry(input_frame)
        self.date_entry.grid(row=1, column=1, sticky="w")

        reserve_button = ttk.Button(input_frame, text="Reserve", command=self.reserve)
        reserve_button.grid(row=2, columnspan=2)

        # Reservation List Frame
        list_frame = ttk.Frame(self.root, padding="10")
        list_frame.grid(row=1, column=0, padx=10, pady=10)

        self.reservation_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=5)
        self.reservation_listbox.pack(expand=True, fill=tk.BOTH)

        cancel_button = ttk.Button(list_frame, text="Cancel Reservation", command=self.cancel_reservation)
        cancel_button.pack()

        # Display initial reservations
        self.display_reservations()

    def reserve(self):
        name = self.name_entry.get()
        date = self.date_entry.get()

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO reservations (name, date, status) VALUES (?, ?, ?)", (name, date, "Reserved"))
        self.conn.commit()

        # Display reservation in the listbox
        self.display_reservations()

        # Notify the user
        notification.notify(
            title="Reservation",
            message=f"Reservation for {name} on {date} is confirmed!",
        )

    def cancel_reservation(self):
        selected_index = self.reservation_listbox.curselection()
        if selected_index:
            reservation_id = self.reservation_listbox.get(selected_index[0]).split(":")[0]

            cursor = self.conn.cursor()
            cursor.execute("UPDATE reservations SET status=? WHERE id=?", ("Cancelled", reservation_id))
            self.conn.commit()

            # Display updated reservations
            self.display_reservations()

            # Notify the user
            notification.notify(
                title="Reservation Cancellation",
                message="Your reservation has been cancelled.",
            )

    def display_reservations(self):
        self.reservation_listbox.delete(0, tk.END)

        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, date, status FROM reservations")
        reservations = cursor.fetchall()

        for reservation in reservations:
            self.reservation_listbox.insert(tk.END, f"{reservation[0]}: {reservation[1]} - {reservation[2]} ({reservation[3]})")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationSystemApp(root)
    root.mainloop()
