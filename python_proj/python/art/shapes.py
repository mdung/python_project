import tkinter as tk
from tkinter import ttk
import sqlite3
import numpy as np
import random

class AbstractArtGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Abstract Art Generator")

        # Database setup
        self.conn = sqlite3.connect('abstract_art_data.db')
        self.create_table()

        # GUI components
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS generated_art
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           shape TEXT,
                           color TEXT)''')
        self.conn.commit()

    def create_widgets(self):
        # Canvas Frame
        canvas_frame = ttk.Frame(self.root, padding="10")
        canvas_frame.grid(row=0, column=0, padx=10, pady=10)

        self.canvas = tk.Canvas(canvas_frame, width=600, height=600, bg="white")
        self.canvas.pack()

        generate_button = ttk.Button(canvas_frame, text="Generate Art", command=self.generate_art)
        generate_button.pack()

    def generate_art(self):
        # Generate random abstract art
        shape = random.choice(["rectangle", "oval", "polygon"])
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Random hex color

        # Save generated art to the database
        self.save_generated_art_to_db(shape, color)

        # Draw the shape on the canvas
        self.draw_shape(shape, color)

    def save_generated_art_to_db(self, shape, color):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO generated_art (shape, color) VALUES (?, ?)", (shape, color))
        self.conn.commit()

    def draw_shape(self, shape, color):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the shape based on user input
        if shape == "rectangle":
            self.canvas.create_rectangle(50, 50, 550, 550, fill=color)
        elif shape == "oval":
            self.canvas.create_oval(50, 50, 550, 550, fill=color)
        elif shape == "polygon":
            points = [50, 300, 300, 50, 550, 300, 300, 550]
            self.canvas.create_polygon(points, fill=color, outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = AbstractArtGeneratorApp(root)
    root.mainloop()
