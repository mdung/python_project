import os
import shutil
from difflib import SequenceMatcher

def categorize_and_organize_pdfs(pdf_folder, new_big_folder):
    # Ensure the new big folder exists
    if not os.path.exists(new_big_folder):
        os.makedirs(new_big_folder)

    # Get a list of all PDF files in the specified folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    # Create a dictionary to store categories and corresponding files
    categories = {}

    # Iterate through each PDF file
    for pdf_file in pdf_files:
        matched_category = None

        # Compare the PDF file name with existing categories
        for category, category_files in categories.items():
            for category_file in category_files:
                similarity_ratio = similar(pdf_file, category_file)
                if similarity_ratio > 0.8:  # Adjust the similarity threshold as needed
                    matched_category = category
                    break

        # If a matching category is found, add the PDF to that category
        if matched_category:
            categories[matched_category].append(pdf_file)
        else:
            # Create a new category for the PDF
            categories[pdf_file] = [pdf_file]

    # Organize PDFs into folders within the new big folder
    for category, category_files in categories.items():
        category_folder = os.path.join(new_big_folder, category)
        os.makedirs(category_folder, exist_ok=True)

        for pdf_file in category_files:
            source_path = os.path.join(pdf_folder, pdf_file)
            destination_path = os.path.join(category_folder, pdf_file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{pdf_file}' to '{category_folder}'.")

def similar(a, b):
    # Function to calculate similarity ratio between two strings
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    # Specify the PDF folder and the new big folder
    pdf_folder = "D:/OrganizedOfficeFiles/PDF_Files"  # Replace with the actual path to your PDF folder
    new_big_folder = "D:\PDF"  # Replace with the desired path for the new big folder

    # Call the categorize_and_organize_pdfs function
    categorize_and_organize_pdfs(pdf_folder, new_big_folder)
