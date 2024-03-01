import tkinter as tk

class RemoteControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Remote Robot Control")
        self.master.geometry("400x300")  # Default size
        self.create_widgets()

    def create_widgets(self):
        self.forward_button = tk.Button(self.master, text="Forward", command=self.move_forward)
        self.forward_button.pack(pady=10)

        self.left_button = tk.Button(self.master, text="Left", command=self.move_left)
        self.left_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_movement)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.right_button = tk.Button(self.master, text="Right", command=self.move_right)
        self.right_button.pack(side=tk.LEFT, padx=10)

        self.backward_button = tk.Button(self.master, text="Backward", command=self.move_backward)
        self.backward_button.pack(pady=10)

        # Resize event binding for responsive layout
        self.master.bind("<Configure>", self.on_resize)

    def move_forward(self):
        print("Moving forward")

    def move_left(self):
        print("Turning left")

    def stop_movement(self):
        print("Stopping")

    def move_right(self):
        print("Turning right")

    def move_backward(self):
        print("Moving backward")

    def on_resize(self, event):
        # Adjust button positions on window resize
        new_width = event.width
        new_height = event.height

        self.master.geometry(f"{new_width}x{new_height}")

        # Modify button positions based on the new window size
        self.forward_button.pack_forget()
        self.left_button.pack_forget()
        self.stop_button.pack_forget()
        self.right_button.pack_forget()
        self.backward_button.pack_forget()

        self.forward_button.pack(pady=new_height // 10)
        self.left_button.pack(side=tk.LEFT, padx=new_width // 10)
        self.stop_button.pack(side=tk.LEFT, padx=new_width // 10)
        self.right_button.pack(side=tk.LEFT, padx=new_width // 10)
        self.backward_button.pack(pady=new_height // 10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoteControlApp(root)
    root.mainloop()
