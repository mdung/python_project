from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        input_path = os.path.join(input_folder, file_name)

        # Check if the file is an image (you can add more image extensions if needed)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image
            img = Image.open(input_path)

            # Resize the image
            resized_img = img.resize(new_size)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, file_name)
            resized_img.save(output_path)

            print(f"Resized: {file_name}")

if __name__ == "__main__":
    # Specify input folder, output folder, and new size (width, height)
    input_folder = "C:\python_folder\input"
    output_folder = "C:\python_folder\output"
    new_size = (300, 200)  # Adjust the size as needed

    # Call the resize_images function
    resize_images(input_folder, output_folder, new_size)
