import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class AvatarCustomizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Avatar Customizer")

        self.avatar_path = None
        self.customized_avatar_path = None

        # Create GUI components
        self.label_avatar = tk.Label(root, text="Select Avatar Image:")
        self.label_avatar.pack()

        self.btn_browse = tk.Button(root, text="Browse", command=self.browse_avatar)
        self.btn_browse.pack()

        self.label_hairstyle = tk.Label(root, text="Hairstyle:")
        self.label_hairstyle.pack()

        self.hairstyle_var = tk.StringVar()
        self.hairstyle_var.set("Short Hair")  # Default hairstyle
        self.entry_hairstyle = tk.Entry(root, textvariable=self.hairstyle_var)
        self.entry_hairstyle.pack()

        self.label_hair_color = tk.Label(root, text="Hair Color:")
        self.label_hair_color.pack()

        self.hair_color_var = tk.StringVar()
        self.hair_color_var.set("Black")  # Default hair color
        self.entry_hair_color = tk.Entry(root, textvariable=self.hair_color_var)
        self.entry_hair_color.pack()

        self.btn_customize = tk.Button(root, text="Customize Avatar", command=self.customize_avatar)
        self.btn_customize.pack()

        self.btn_save = tk.Button(root, text="Save Customized Avatar", command=self.save_customized_avatar)
        self.btn_save.pack()

    def browse_avatar(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.avatar_path = file_path
            self.load_avatar_image(file_path)

    def load_avatar_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((150, 150), resample=Image.ANTIALIAS)  # Use resample instead of Image.ANTIALIAS
        self.avatar_image = ImageTk.PhotoImage(image)
        self.label_avatar.config(image=self.avatar_image)
        self.label_avatar.image = self.avatar_image

    def customize_avatar(self):
        if not self.avatar_path:
            tk.messagebox.showerror("Error", "Please select an avatar image.")
            return

        # Retrieve customization options
        hairstyle = self.hairstyle_var.get()
        hair_color = self.hair_color_var.get()

        # Apply customization (dummy implementation)
        self.customized_avatar_path = self.apply_customization(self.avatar_path, hairstyle, hair_color)

        # Display the customized avatar (optional)
        self.load_avatar_image(self.customized_avatar_path)

    def apply_customization(self, avatar_path, hairstyle, hair_color):
        # Implement the logic to customize the avatar based on the provided options
        # This could involve image processing techniques or using predefined templates.
        # For simplicity, a dummy implementation is provided that just returns the original avatar path.

        # You should replace this with your actual customization logic.
        return avatar_path

    def save_customized_avatar(self):
        if not self.customized_avatar_path:
            tk.messagebox.showerror("Error", "Please customize the avatar first.")
            return

        # Get a meaningful name for the output file
        output_filename = self.get_output_filename()

        # Copy the customized avatar to the output filename
        import shutil
        shutil.copyfile(self.customized_avatar_path, output_filename)

        tk.messagebox.showinfo("Success", f"Customized avatar saved as {output_filename}")

    def get_output_filename(self):
        return tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

if __name__ == "__main__":
    root = tk.Tk()
    app = AvatarCustomizer(root)
    root.mainloop()
