import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.label = ttk.Label(self.master, text="Enter text:")
        self.label.grid(row=0, column=0, pady=10)

        self.entry_text = tk.StringVar()
        self.entry = ttk.Entry(self.master, textvariable=self.entry_text, width=30)
        self.entry.grid(row=0, column=1, pady=10)

        self.generate_button = ttk.Button(self.master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.grid(row=0, column=2, pady=10)

        self.qr_code_image_label = ttk.Label(self.master, text="QR Code will be displayed here.")
        self.qr_code_image_label.grid(row=1, column=0, columnspan=3, pady=10)

    def generate_qr_code(self):
        text_to_encode = self.entry_text.get()

        if text_to_encode:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image (optional)
            img.save("qrcode.png")

            # Display the image
            img = ImageTk.PhotoImage(img)
            self.qr_code_image_label.config(image=img)
            self.qr_code_image_label.image = img

        else:
            self.qr_code_image_label.config(text="Please enter text.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
