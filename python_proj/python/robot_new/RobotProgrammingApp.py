import tkinter as tk
from tkinter import Canvas, ttk

class RobotProgrammingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Programming Interface")

        self.canvas = Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(pady=10)

        self.robot_image = tk.PhotoImage(file="robot.png")  # Provide the path to your robot image
        self.robot = self.canvas.create_image(50, 50, anchor=tk.NW, image=self.robot_image)

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(pady=10)

        ttk.Button(self.controls_frame, text="Clear All", command=self.clear_all).grid(row=0, column=0, padx=10)
        ttk.Button(self.controls_frame, text="Run Program", command=self.run_program).grid(row=0, column=1, padx=10)

        self.program = []

    def on_click(self, event):
        x, y = event.x, event.y
        object_id = self.canvas.find_closest(x, y)[0]
        if object_id == self.robot:
            self.canvas.tag_raise(self.robot)
            self.start_x, self.start_y = x, y

    def on_drag(self, event):
        x, y = event.x, event.y
        dx, dy = x - self.start_x, y - self.start_y
        self.canvas.move(self.robot, dx, dy)
        self.start_x, self.start_y = x, y

        self.program.append((dx, dy))

    def clear_all(self):
        self.canvas.delete("all")
        self.robot = self.canvas.create_image(50, 50, anchor=tk.NW, image=self.robot_image)
        self.program = []

    def run_program(self):
        for step in self.program:
            dx, dy = step
            self.root.after(500, lambda: self.canvas.move(self.robot, dx, dy))

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotProgrammingApp(root)
    root.mainloop()
