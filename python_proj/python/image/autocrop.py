import cv2
import numpy as np

def autocrop(image_path, output_path='autocropped_image.jpg'):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Canny edge detector to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Iterate over the sorted contours
    for contour in contours:
        # Approximate the contour
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the contour has four vertices, it is likely a rectangle
        if len(approx) == 4:
            # Get the bounding box of the contour
            x, y, w, h = cv2.boundingRect(approx)

            # Crop the image using the bounding box
            cropped_image = image[y:y + h, x:x + w]

            # Save the autocropped image
            cv2.imwrite(output_path, cropped_image)

            # Display the original and autocropped images
            cv2.imshow('Original Image', image)
            cv2.imshow('Autocropped Image', cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break  # Stop after finding the first rectangle

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'img_src/v.jpg'

    autocrop(image_path)
