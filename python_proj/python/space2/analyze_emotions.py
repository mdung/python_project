import cv2
from deepface import DeepFace

# Load the pre-trained emotion recognition model
model = DeepFace.build_model("Emotion")

def analyze_emotions(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Use the emotion recognition model to analyze facial expressions
    result = DeepFace.analyze(img, actions=['emotion'], models={"emotion": model})

    # Extract emotion prediction
    emotion = result['emotion']['dominant']

    # Display the result
    print("Dominant Emotion:", emotion)

    # Draw bounding box and emotion label on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, f"Emotion: {emotion}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the image with the analysis result
    cv2.imshow('Emotion Analysis', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'C:/pto/2.jpg'
analyze_emotions(image_path)
