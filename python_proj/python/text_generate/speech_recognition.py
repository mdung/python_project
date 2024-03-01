import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            print("Please speak something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

            print("Recognizing...")

        # Use Google Web Speech API for speech recognition
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    return None

if __name__ == "__main__":
    result = speech_to_text()

    if result:
        print("Spoken text: ", result)
