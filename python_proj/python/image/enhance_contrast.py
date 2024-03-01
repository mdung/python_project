import cv2
import numpy as np

def enhance_contrast(image_path, alpha=1.2, beta=30):
    # Read the image
    original_image = cv2.imread(image_path)

    # Apply contrast enhancement formula
    enhanced_image = cv2.convertScaleAbs(original_image, alpha=alpha, beta=beta)

    return original_image, enhanced_image

def display_images(original_image, enhanced_image):
    # Display the original and enhanced images side by side
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Enhanced Image', enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'img_src/2.jpg'

    original_image, enhanced_image = enhance_contrast(image_path)

    # Display the images
    display_images(original_image, enhanced_image)
