import tkinter as tk

class RobotControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Control System")

        # Create buttons for robot control
        self.forward_button = tk.Button(master, text="Forward", command=self.move_forward)
        self.backward_button = tk.Button(master, text="Backward", command=self.move_backward)
        self.left_button = tk.Button(master, text="Left", command=self.turn_left)
        self.right_button = tk.Button(master, text="Right", command=self.turn_right)

        # Place buttons on the GUI
        self.forward_button.grid(row=0, column=1)
        self.backward_button.grid(row=2, column=1)
        self.left_button.grid(row=1, column=0)
        self.right_button.grid(row=1, column=2)

    def move_forward(self):
        print("Robot moving forward")

    def move_backward(self):
        print("Robot moving backward")

    def turn_left(self):
        print("Robot turning left")

    def turn_right(self):
        print("Robot turning right")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlApp(root)
    root.mainloop()
