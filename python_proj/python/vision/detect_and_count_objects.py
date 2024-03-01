import cv2

def detect_and_count_objects(image_path, min_area=500):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    object_count = 0

    # Loop over the contours
    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < min_area:
            continue

        # Increment object count
        object_count += 1

        # Draw the contour on the original image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

        # Find the bounding box coordinates and draw it on the image
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Add label with object count
        cv2.putText(image, f'Object {object_count}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Detected Objects', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return object_count

# Example usage
if __name__ == "__main__":
    image_path = 'your_image.jpg'  # Replace 'your_image.jpg' with the path to your image
    min_area = 500  # Minimum area to consider as an object (adjust as needed)
    object_count = detect_and_count_objects(image_path, min_area)
    print(f'Number of objects detected: {object_count}')
