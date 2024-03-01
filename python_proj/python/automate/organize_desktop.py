import os
import shutil

def organize_desktop(desktop_path):
    # Ensure the 'OrganizedDesktop' folder exists on the desktop
    organized_folder = os.path.join(desktop_path, 'OrganizedDesktop')
    if not os.path.exists(organized_folder):
        os.makedirs(organized_folder)

    # Iterate through files on the desktop
    for filename in os.listdir(desktop_path):
        source_path = os.path.join(desktop_path, filename)

        # Skip folders and hidden files
        if os.path.isdir(source_path) or filename.startswith('.'):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Create a folder for the file type if it doesn't exist
        file_type_folder = os.path.join(organized_folder, file_extension[1:])
        if not os.path.exists(file_type_folder):
                os.makedirs(file_type_folder)

        # Move the file to the corresponding folder
        destination_path = os.path.join(file_type_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{file_type_folder}'.")

if __name__ == "__main__":
    # Specify the path to your desktop
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

    # Call the organize_desktop function
    organize_desktop(desktop_path)
