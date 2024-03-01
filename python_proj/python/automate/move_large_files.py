import os
import shutil

def move_large_files(source_folder, destination_folder, user_folders, threshold_size_mb=100):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through specified user folders in the source folder
    for user_folder in user_folders:
        folder_path = os.path.join(source_folder, user_folder)

        # Check if the user folder exists
        if os.path.exists(folder_path):
            # Iterate through files in the user folder
            for root, _, files in os.walk(folder_path):
                for filename in files:
                    file_path = os.path.join(root, filename)

                    # Get file size in megabytes
                    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

                    # Check if the file size exceeds the threshold
                    if file_size_mb > threshold_size_mb:
                        # Create a folder based on the file type
                        file_type_folder = os.path.join(destination_folder, get_file_extension(filename))
                        if not os.path.exists(file_type_folder):
                            os.makedirs(file_type_folder)

                        # Move the file to the corresponding folder
                        destination_path = os.path.join(file_type_folder, filename)
                        shutil.move(file_path, destination_path)
                        print(f"Moved '{filename}' to '{file_type_folder}'.")

def get_file_extension(filename):
    _, file_extension = os.path.splitext(filename)
    return file_extension[1:].lower()  # Remove the dot and convert to lowercase

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder = "C:/"
    destination_folder = "D:/BigSizeFiles"

    # Specify the user folders to target
    user_folders = ["Users", "YourUserName"]  # Add more user folders as needed

    # Specify the threshold size in megabytes
    threshold_size_mb = 100

    # Call the move_large_files function
    move_large_files(source_folder, destination_folder, user_folders, threshold_size_mb)
