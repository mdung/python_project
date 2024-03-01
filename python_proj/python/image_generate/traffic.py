import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def detect_traffic_signs(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the image to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Use the HoughCircles function to detect circular shapes (traffic signs)
    circles = cv2.HoughCircles(
        blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
        param1=50, param2=30, minRadius=20, maxRadius=100
    )

    if circles is not None:
        # Initialize a list to store the detected signs and their labels
        detected_signs = []

        # Draw circles on the original image and classify the signs
        for circle in circles[0, :]:
            center = (int(circle[0]), int(circle[1]))
            radius = int(circle[2])

            # Crop the region of interest around the detected circle
            roi = image[int(circle[1] - radius):int(circle[1] + radius),
                  int(circle[0] - radius):int(circle[0] + radius)]

            # Classify the sign based on a simple condition (e.g., color)
            sign_label = classify_traffic_sign(roi)

            # Draw the circle and label on the original image
            cv2.circle(image, center, radius, (0, 255, 0), 2)
            cv2.putText(image, sign_label, center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            # Save the detected sign and its label
            detected_signs.append((center, radius, sign_label))

    return image, detected_signs

def classify_traffic_sign(roi):
    # Placeholder for a more advanced classifier
    # For simplicity, let's use a basic condition based on color
    avg_color = np.mean(roi, axis=(0, 1))

    if avg_color[2] > 150:  # Assuming red color for simplicity
        return "Stop Sign"
    else:
        return "Other Sign"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_var.set(file_path)

def detect_and_save():
    input_path = entry_var.get()

    if not input_path:
        # Provide an error message or handle the case when no file is selected
        return

    output_image_path = "detected_signs_" + generate_meaningful_name() + ".png"
    output_text_path = "detected_signs_" + generate_meaningful_name() + ".txt"

    # Detect traffic signs
    result_image, detected_signs = detect_traffic_signs(input_path)

    # Save the result image
    cv2.imwrite(output_image_path, result_image)

    # Write detected signs and labels to a text file
    with open(output_text_path, 'w') as text_file:
        text_file.write("Detected Signs:\n")
        for sign in detected_signs:
            text_file.write(f"Type: {sign[2]}, Center: {sign[0]}, Radius: {sign[1]}\n")

    # Print detected signs and labels
    print("Detected Signs:")
    for sign in detected_signs:
        print(f"Type: {sign[2]}, Center: {sign[0]}, Radius: {sign[1]}")

    # You can add a success message or open the output file, etc.

def generate_meaningful_name():
    # Implement a logic to generate a meaningful name for the output file
    # For simplicity, let's use a placeholder name
    return "detected_signs"

# GUI setup
app = tk.Tk()
app.title("Traffic Sign Detector")

# Entry for file path
entry_var = tk.StringVar()
entry = tk.Entry(app, textvariable=entry_var, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Browse button
browse_button = tk.Button(app, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Detect button
detect_button = tk.Button(app, text="Detect and Save", command=detect_and_save)
detect_button.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()
