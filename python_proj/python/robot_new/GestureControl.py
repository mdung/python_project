import cv2
import mediapipe as mp

class GestureControl:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_gesture(self):
        while True:
            ret, frame = self.cap.read()

            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)

            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with Mediapipe Hands
            results = self.hands.process(rgb_frame)

            # Draw hand landmarks on the frame
            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, landmarks, self.mp_hands.HAND_CONNECTIONS)

                    # Extracting hand landmarks for gesture recognition
                    thumb_tip = landmarks.landmark[4]
                    index_tip = landmarks.landmark[8]
                    middle_tip = landmarks.landmark[12]
                    ring_tip = landmarks.landmark[16]
                    pinky_tip = landmarks.landmark[20]

                    # Implement your own logic for gesture control based on landmarks
                    # Example: Move forward if the index finger is up, stop if it's down
                    if index_tip.y < middle_tip.y:
                        print("Move forward")
                    else:
                        print("Stop")

            # Display the resulting frame
            cv2.imshow('Gesture Control', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the window
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    gesture_control = GestureControl()
    gesture_control.detect_gesture()
