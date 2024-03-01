import os
import pyttsx3
import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu, Scale

def text_file_to_speech(input_filename, selected_voice, selected_rate):
    with open(input_filename, 'r', encoding='utf-8-sig') as file:
        text = file.read()

    # Extracting the name of the file (without extension) for the output MP3 file
    output_filename = os.path.splitext(os.path.basename(input_filename))[0] + "_output.mp3"

    engine = pyttsx3.init()

    # Set the voice
    voices = engine.getProperty('voices')
    selected_voice_id = None
    for voice in voices:
        if selected_voice.lower() in voice.name.lower() and 'vietnamese' in voice.languages:
            selected_voice_id = voice.id
            break

    if selected_voice_id:
        engine.setProperty('voice', selected_voice)  # Use the voice name, not the ID
        engine.setProperty('rate', selected_rate)
        engine.save_to_file(text, output_filename)
        engine.runAndWait()
        print(f"Text from '{input_filename}' converted to speech and saved as '{output_filename}'")
    else:
        print(f"Error: Selected Vietnamese voice not found or does not support Vietnamese language.")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        entry_var.set(file_path)

def convert_to_speech():
    input_file = entry_var.get()
    selected_voice = voice_var.get()
    selected_rate = rate_var.get()

    if not os.path.isfile(input_file):
        result_label_var.set("Error: The specified file does not exist.")
    else:
        text_file_to_speech(input_file, selected_voice, selected_rate)
        result_label_var.set(f"Conversion complete. Check the console for details.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text-to-Speech Converter")

    # Entry widget for displaying selected file path
    entry_var = StringVar()
    entry = tk.Entry(root, textvariable=entry_var, width=40)
    entry.grid(row=0, column=0, padx=10, pady=10)

    # Browse button to open file dialog
    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    # Voice settings dropdown
    voice_var = StringVar(root)
    voice_var.set("vietnamese")  # Initial value

    voice_label = tk.Label(root, text="Select Voice:")
    voice_label.grid(row=1, column=0, padx=10, pady=10)

    # Fetch available voices
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_options = [voice.name for voice in voices if 'vietnamese' in voice.languages]

    voice_menu = OptionMenu(root, voice_var, *voice_options)
    voice_menu.config(width=20)  # Set the width to accommodate longer voice names
    voice_menu.grid(row=1, column=1, padx=10, pady=10)

    # Rate settings slider
    rate_var = tk.IntVar(root)
    rate_var.set(150)  # Default rate

    rate_label = tk.Label(root, text="Select Speech Rate:")
    rate_label.grid(row=2, column=0, padx=10, pady=10)

    rate_slider = Scale(root, from_=50, to=300, variable=rate_var, orient=tk.HORIZONTAL)
    rate_slider.grid(row=2, column=1, padx=10, pady=10)

    # Convert button to start text-to-speech conversion
    convert_button = tk.Button(root, text="Convert", command=convert_to_speech)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Label to display conversion result
    result_label_var = StringVar()
    result_label = tk.Label(root, textvariable=result_label_var)
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()
