import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

class PhotoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Downloader")

        self.label = tk.Label(root, text="Enter Website Link:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.download_button = tk.Button(root, text="Download Photos", command=self.download_photos)
        self.download_button.pack()

        self.image_label = tk.Label(root, text="Preview:")
        self.image_label.pack()

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

    def download_photos(self):
        website_url = self.entry.get()

        try:
            response = requests.get(website_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all image tags on the webpage
            img_tags = soup.find_all('img')

            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    # Create an absolute URL if it's a relative URL
                    img_url = urljoin(website_url, img_url)

                    # Download the image
                    img_response = requests.get(img_url)
                    img = Image.open(BytesIO(img_response.content))

                    # Display the image in the GUI
                    photo = ImageTk.PhotoImage(img)
                    self.canvas.config(width=img.width, height=img.height)
                    self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                    self.canvas.image = photo

                    # Ask user to select a folder to save the image
                    folder_path = filedialog.askdirectory()
                    if folder_path:
                        # Generate a meaningful name for the photo
                        img_name = os.path.basename(urlparse(img_url).path)
                        file_name = os.path.join(folder_path, "Downloaded_Photos", f"downloaded_photo_{img_name}")

                        # Create the folder if it doesn't exist
                        os.makedirs(os.path.dirname(file_name), exist_ok=True)

                        # Save the image
                        img.save(file_name)
                        print(f"Image downloaded and saved as {file_name}")

        except Exception as e:
            print(f"Error downloading images: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoDownloaderApp(root)
    root.mainloop()
