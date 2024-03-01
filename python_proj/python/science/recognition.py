import cv2
import dlib
import numpy as np

# Load the pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model from dlib
face_recognizer = dlib.face_recognition_model_v1("shape_predictor_68_face_landmarks.dat")

# Load a sample image and its corresponding face encoding
sample_image = cv2.imread("sample_face.jpg")
sample_encoding = np.load("sample_encoding.npy")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get the face landmarks
        landmarks = face_recognizer(frame, face)

        # Compute the face encoding
        face_encoding = np.array(face_recognizer.compute_face_descriptor(frame, landmarks))

        # Compare the face encoding with the sample encoding
        distance = np.linalg.norm(face_encoding - sample_encoding)

        # Recognize if the distance is below a certain threshold
        if distance < 0.6:
            label = "Recognized"
        else:
            label = "Unknown"

        # Draw a rectangle around the face and display the label
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
        cv2.putText(frame, label, (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Facial Recognition", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
