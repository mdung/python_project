from google.cloud import translate_v2 as translate
from googletrans import Translator
import os

# Set Google Cloud credentials (replace 'path/to/your/credentials.json' with your JSON key file)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

# Initialize Google Cloud Translation API client
client = translate.Client()

# Function to translate text using Google Cloud Translation API
def translate_text_googlecloud(text, target_language):
    result = client.translate(text, target_language=target_language)
    translated_text = result['input']
    return translated_text

# Function to translate text using googletrans library
def translate_text_googletrans(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Simple chatbot for language translation
def language_translation_chatbot():
    print("Language Translation Chatbot")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        target_language = input("Enter target language (e.g., 'es' for Spanish): ")

        # Translate user input
        translated_text_googlecloud = translate_text_googlecloud(user_input, target_language)
        translated_text_googletrans = translate_text_googletrans(user_input, target_language)

        # Display translated text
        print(f"Google Cloud Translation API: {translated_text_googlecloud}")
        print(f"googletrans Library: {translated_text_googletrans}\n")

# Run the chatbot
language_translation_chatbot()
