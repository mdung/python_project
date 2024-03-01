import os
import shutil

def move_office_files(source_drive, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Define the file extensions for Excel, PDF, and Word documents
    excel_extensions = [".xls", ".xlsx", ".xlsm"]
    pdf_extensions = [".pdf"]
    word_extensions = [".doc", ".docx"]

    # Iterate through files on the specified drive
    for root, _, files in os.walk(source_drive):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the file has an Excel, PDF, or Word document extension
            _, file_extension = os.path.splitext(filename)
            file_extension_lower = file_extension.lower()

            if file_extension_lower in excel_extensions:
                file_type_folder = os.path.join(destination_folder, "Excel_Files")
            elif file_extension_lower in pdf_extensions:
                file_type_folder = os.path.join(destination_folder, "PDF_Files")
            elif file_extension_lower in word_extensions:
                file_type_folder = os.path.join(destination_folder, "Word_Files")
            else:
                continue  # Skip files with other extensions

            if not os.path.exists(file_type_folder):
                os.makedirs(file_type_folder)

            # Move the file to the corresponding folder
            destination_path = os.path.join(file_type_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved '{filename}' to '{file_type_folder}'.")

if __name__ == "__main__":
    # Specify the source drive and destination folder
    source_drive = "D:/"  # Replace with the desired drive letter
    destination_folder = "D:/OrganizedOfficeFiles"

    # Call the move_office_files function
    move_office_files(source_drive, destination_folder)
