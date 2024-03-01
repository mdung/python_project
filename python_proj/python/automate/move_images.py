import os
import shutil

def move_images(source_drive, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Define a list of common image file extensions
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]

    # Iterate through files on the specified drive
    for root, _, files in os.walk(source_drive):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the file has a common image extension
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in image_extensions:
                # Create a folder based on the file type
                file_type_folder = os.path.join(destination_folder, get_file_type_folder(file_extension))
                if not os.path.exists(file_type_folder):
                    os.makedirs(file_type_folder)

                # Move the image to the corresponding folder
                destination_path = os.path.join(file_type_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved '{filename}' to '{file_type_folder}'.")

def get_file_type_folder(file_extension):
    # Generate a meaningful subfolder name based on the file extension
    if file_extension.lower() == ".jpg" or file_extension.lower() == ".jpeg":
        return "JPEG_Images"
    elif file_extension.lower() == ".png":
        return "PNG_Images"
    elif file_extension.lower() == ".gif":
        return "GIF_Images"
    elif file_extension.lower() == ".bmp":
        return "BMP_Images"
    elif file_extension.lower() == ".tiff" or file_extension.lower() == ".webp":
        return "Other_Images"
    else:
        return "Unknown_Images"

if __name__ == "__main__":
    # Specify the source drive and destination folder
    source_drive = "D:/"  # Replace with the desired drive letter
    destination_folder = "D:/OrganizedImages"

    # Call the move_images function
    move_images(source_drive, destination_folder)
