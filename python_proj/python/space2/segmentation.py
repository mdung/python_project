import cv2
import numpy as np

def segment_objects(image_path, lower_color, upper_color):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the color range for segmentation
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create a binary mask for the specified color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the original image to segment the objects
    segmented_img = cv2.bitwise_and(img, img, mask=mask)

    # Display the original and segmented images
    cv2.imshow('Original Image', img)
    cv2.imshow('Segmented Image', segmented_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'C:/pto/2.jpg'

# Specify the lower and upper color bounds for segmentation (HSV format)
lower_color_bound = [30, 50, 50]  # Example: Lower bound for green color
upper_color_bound = [90, 255, 255]  # Example: Upper bound for green color

segment_objects(image_path, lower_color_bound, upper_color_bound)
