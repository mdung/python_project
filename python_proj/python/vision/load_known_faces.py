import cv2
import face_recognition
import os  # Import the os module for working with file paths and directories

def load_known_faces(known_faces_folder):
    known_faces = []
    known_names = []

    # Load known faces from images in the folder
    for file_name in os.listdir(known_faces_folder):
        image_path = os.path.join(known_faces_folder, file_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]  # Assuming one face per image
        known_faces.append(encoding)
        known_names.append(os.path.splitext(file_name)[0])

    return known_faces, known_names

def recognize_faces(known_faces_folder):
    # Load known faces and their names
    known_faces, known_names = load_known_faces(known_faces_folder)

    # Initialize the video capture
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            # Compare face with known faces
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            # Check if a match is found
            if True in matches:
                matched_index = matches.index(True)
                name = known_names[matched_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    video_capture.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    known_faces_folder = 'known_faces'  # Folder containing images of known faces
    recognize_faces(known_faces_folder)
