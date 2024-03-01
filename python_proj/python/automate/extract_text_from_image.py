from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

    return text

if __name__ == "__main__":
    # Specify the path to your image file
    image_path = "D:/pic/python/bio.png"  # Replace with the actual path to your image file

    # Call the extract_text_from_image function
    extracted_text = extract_text_from_image(image_path)

    # Specify the output file path
    output_file = "output/extracted_text.txt"  # Replace with your desired output file path

    # Write the extracted text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Extracted Text:\n")
        file.write(extracted_text)

    print(f"Extracted text saved to: {output_file}")
