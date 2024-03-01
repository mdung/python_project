import os
import shutil

def organize_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Mapping of file extensions to folder names (customize as needed)
    extension_mappings = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".mp3": "Audio",
        ".mp4": "Videos",
        ".docx": "Documents",
        ".zip": "Archives",
        ".exe": "Executables",
        # Add more mappings as needed
    }

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Extract file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()  # Convert to lowercase for case-insensitivity

        # Determine the folder name based on the file extension
        folder_name = extension_mappings.get(file_extension, "Other")

        # Create a folder for the file type if it doesn't exist
        file_type_folder = os.path.join(destination_folder, folder_name)
        if not os.path.exists(file_type_folder):
            os.makedirs(file_type_folder)

        # Move the file to the corresponding folder
        destination_path = os.path.join(file_type_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{file_type_folder}'.")

if __name__ == "__main__":
    # Specify the source and destination folders
    source_directory = "D:\download"
    destination_directory = "D:\download_organized"

    # Call the organize_files function
    organize_files(source_directory, destination_directory)
