import cv2
import numpy as np
import dlib

def detect_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use dlib to detect faces
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray)

    return faces, image

def remove_red_eye(image, faces):
    # Define a simple red-eye correction function
    def correct_red_eye(eye):
        # Reduce the red intensity by setting the red channel to the average of the green and blue channels
        eye[:, :, 2] = (eye[:, :, 1] + eye[:, :, 0]) // 2
        return eye

    # Loop through detected faces
    for face in faces:
        # Extract face coordinates
        x, y, w, h = [coord for coord in (face.left(), face.top(), face.width(), face.height())]

        # Define the region of interest (ROI) containing the eyes
        eyes_roi = image[y:y + h, x:x + w]

        # Correct red-eye in each eye region
        for i in range(0, eyes_roi.shape[0], 2):
            for j in range(0, eyes_roi.shape[1], 2):
                eye = eyes_roi[i:i + 2, j:j + 2]
                eyes_roi[i:i + 2, j:j + 2] = correct_red_eye(eye)

    return image

def display_images(original_image, corrected_image):
    # Display the original and corrected images side by side
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Corrected Image', corrected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'img_src/t.jpg'

    faces, original_image = detect_faces(image_path)
    corrected_image = remove_red_eye(original_image.copy(), faces)

    # Display the images
    display_images(original_image, corrected_image)
