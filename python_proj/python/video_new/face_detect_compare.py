import os
import cv2
import tkinter as tk
from tkinter import filedialog

class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        master.title("Face Recognition App")

        self.label1 = tk.Label(master, text="Upload Video:")
        self.label1.pack()

        self.upload_button1 = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button1.pack()

        self.label2 = tk.Label(master, text="Upload Folder with Existing Photos:")
        self.label2.pack()

        self.upload_button2 = tk.Button(master, text="Upload", command=self.upload_folder)
        self.upload_button2.pack()

        self.detect_button = tk.Button(master, text="Detect and Match Faces", command=self.detect_and_match_faces)
        self.detect_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_path = file_path
            self.label1.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def upload_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.existing_photos_folder = folder_path
            self.label2.config(text=f"Uploaded Folder: {os.path.basename(folder_path)}")

    def detect_and_match_faces(self):
        if hasattr(self, 'video_path') and hasattr(self, 'existing_photos_folder'):
            # Load face detection model from OpenCV
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Create a folder for matched faces
            output_folder = self.create_output_folder()

            # Initialize face recognition model (you may want to use a more sophisticated model)
            face_recognizer = self.create_face_recognizer()

            # Train the face recognition model with existing photos
            self.train_face_recognition_model(face_recognizer)

            # Process each frame in the video
            cap = cv2.VideoCapture(self.video_path)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Convert the frame to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces in the frame
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # Match detected faces with existing photos
                for (x, y, w, h) in faces:
                    face_region = gray[y:y + h, x:x + w]

                    # Predict the label of the detected face
                    label, confidence = face_recognizer.predict(face_region)

                    # If confidence is below a certain threshold, consider it a match
                    if confidence < 100:
                        matched_face_path = os.path.join(output_folder, f"matched_face_{label}.png")
                        cv2.imwrite(matched_face_path, face_region)

                # Display the frame with rectangles around detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow("Face Recognition", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

            self.label1.config(text=f"Face Matching Completed! Matched faces saved in: {os.path.basename(output_folder)}")
        else:
            self.label1.config(text="Please upload a video and a folder with existing photos first!")

    def create_output_folder(self):
        input_filename = os.path.basename(self.video_path)
        folder_name = f"matched_faces_{os.path.splitext(input_filename)[0]}"
        output_folder = os.path.join(os.path.dirname(self.video_path), folder_name)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        return output_folder

    def create_face_recognizer(self):
        if cv2.__version__.startswith('3.'):
            return cv2.face.createLBPHFaceRecognizer()
        else:
            return cv2.face.LBPHFaceRecognizer_create()

    def train_face_recognition_model(self, face_recognizer):
        labels = []
        faces = []
        for label, person_folder in enumerate(os.listdir(self.existing_photos_folder)):
            person_path = os.path.join(self.existing_photos_folder, person_folder)
            for filename in os.listdir(person_path):
                image_path = os.path.join(person_path, filename)
                face_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                labels.append(label)
                faces.append(face_image)

        face_recognizer.train(faces, labels)

def main():
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
