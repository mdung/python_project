import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import time  # Added for delay

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
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            response = requests.get(website_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')

            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    img_url = urljoin(website_url, img_url)
                    img_response = requests.get(img_url, headers=headers)
                    img_response.raise_for_status()

                    img = Image.open(BytesIO(img_response.content))
                    photo = ImageTk.PhotoImage(img)

                    self.canvas.config(width=img.width, height=img.height)
                    self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                    self.canvas.image = photo

                    folder_path = filedialog.askdirectory()
                    if folder_path:
                        img_name = os.path.basename(urlparse(img_url).path)
                        file_name = os.path.join(folder_path, "Downloaded_Photos", f"downloaded_photo_{img_name}")
                        os.makedirs(os.path.dirname(file_name), exist_ok=True)
                        img.save(file_name)
                        print(f"Image downloaded and saved as {file_name}")

                    # Introduce a delay between requests
                    time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"Error during requests: {e}")
        except Exception as e:
            print(f"Error downloading images: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoDownloaderApp(root)
    root.mainloop()
