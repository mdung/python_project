import tkinter as tk
from tkinter import ttk
import sqlite3

class DrawingSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Simulator")

        # Database setup
        self.conn = sqlite3.connect('drawing_data.db')
        self.create_table()

        # Drawing variables
        self.drawing = False
        self.last_x = None
        self.last_y = None

        # GUI components
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS brushstrokes
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           x INTEGER,
                           y INTEGER,
                           pressure REAL,
                           artist TEXT)''')
        self.conn.commit()

    def create_widgets(self):
        # Canvas Frame
        canvas_frame = ttk.Frame(self.root, padding="10")
        canvas_frame.grid(row=0, column=0, padx=10, pady=10)

        self.canvas = tk.Canvas(canvas_frame, width=800, height=600, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_drawing)

        artist_label = ttk.Label(canvas_frame, text="Artist:")
        artist_label.pack(side=tk.LEFT)

        self.artist_entry = ttk.Entry(canvas_frame)
        self.artist_entry.pack(side=tk.LEFT)

        save_button = ttk.Button(canvas_frame, text="Save Drawing", command=self.save_drawing)
        save_button.pack(side=tk.LEFT)

    def paint(self, event):
        x, y = event.x, event.y
        pressure = 1.0  # In a real application, you would capture pressure data from a drawing tablet.

        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=2, smooth=tk.TRUE)

            # Save brushstroke data to the database
            self.save_brushstroke_data(x, y, pressure)

        self.last_x = x
        self.last_y = y

    def reset_drawing(self, event):
        self.last_x = None
        self.last_y = None

    def save_brushstroke_data(self, x, y, pressure):
        artist = self.artist_entry.get()
        if not artist:
            artist = "Unknown"

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO brushstrokes (x, y, pressure, artist) VALUES (?, ?, ?, ?)", (x, y, pressure, artist))
        self.conn.commit()

    def save_drawing(self):
        # Save the entire drawing to a file or perform additional actions as needed.
        messagebox.showinfo("Save Drawing", "Drawing saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingSimulatorApp(root)
    root.mainloop()
