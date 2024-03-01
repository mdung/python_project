import tkinter as tk

class VirtualJoystick:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Joystick")

        # Canvas to draw the joystick
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        # Center coordinates of the joystick
        self.joystick_center_x = 150
        self.joystick_center_y = 150

        # Joystick parameters
        self.joystick_radius = 50
        self.joystick = self.canvas.create_oval(
            self.joystick_center_x - self.joystick_radius,
            self.joystick_center_y - self.joystick_radius,
            self.joystick_center_x + self.joystick_radius,
            self.joystick_center_y + self.joystick_radius,
            fill="blue"
        )

        # Bind mouse events to joystick movement
        self.canvas.bind("<B1-Motion>", self.move_joystick)
        self.canvas.bind("<ButtonRelease-1>", self.reset_joystick)

    def move_joystick(self, event):
        # Calculate the distance from the joystick center to the mouse position
        distance = ((event.x - self.joystick_center_x)**2 +
                    (event.y - self.joystick_center_y)**2)**0.5

        # Limit the joystick movement within its radius
        if distance <= self.joystick_radius:
            # Move the joystick to the mouse position
            self.canvas.coords(
                self.joystick,
                event.x - self.joystick_radius,
                event.y - self.joystick_radius,
                event.x + self.joystick_radius,
                event.y + self.joystick_radius
            )
        else:
            # Move the joystick to the edge of its radius along the line to the mouse position
            angle = self.calculate_angle(event.x, event.y)
            x = self.joystick_center_x + self.joystick_radius * \
                self.cosine(angle)
            y = self.joystick_center_y + self.joystick_radius * \
                self.sine(angle)
            self.canvas.coords(
                self.joystick,
                x - self.joystick_radius,
                y - self.joystick_radius,
                x + self.joystick_radius,
                y + self.joystick_radius
            )

    def reset_joystick(self, event):
        # Reset the joystick to the center
        self.canvas.coords(
            self.joystick,
            self.joystick_center_x - self.joystick_radius,
            self.joystick_center_y - self.joystick_radius,
            self.joystick_center_x + self.joystick_radius,
            self.joystick_center_y + self.joystick_radius
        )

    def calculate_angle(self, x, y):
        # Calculate the angle between the joystick center and the mouse position
        return math.atan2(y - self.joystick_center_y, x - self.joystick_center_x)

    def cosine(self, angle):
        # Calculate the cosine of an angle in radians
        return math.cos(angle)

    def sine(self, angle):
        # Calculate the sine of an angle in radians
        return math.sin(angle)


if __name__ == "__main__":
    import math

    root = tk.Tk()
    app = VirtualJoystick(root)
    root.mainloop()
