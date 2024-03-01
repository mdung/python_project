import os
import pyttsx3
import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu, Scale

def text_file_to_speech(input_filename, selected_voice, selected_rate):
    with open(input_filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extracting the name of the file (without extension) for the output MP3 file
    output_filename = os.path.splitext(os.path.basename(input_filename))[0] + "_output.mp3"

    engine = pyttsx3.init()

    # Set the voice
    voices = engine.getProperty('voices')
    selected_voice_id = None
    for voice in voices:
        if selected_voice.lower() in voice.name.lower():
            selected_voice_id = voice.id
            break

    if selected_voice_id:
        engine.setProperty('voice', selected_voice_id)
        engine.setProperty('rate', selected_rate)
        engine.save_to_file(text, output_filename)
        engine.runAndWait()
        print(f"Text from '{input_filename}' converted to speech and saved as '{output_filename}'")
    else:
        print(f"Error: Selected voice '{selected_voice}' not found.")

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
    voice_var.set("en-US-Standard-A")  # Default voice

    voice_label = tk.Label(root, text="Select Voice:")
    voice_label.grid(row=1, column=0, padx=10, pady=10)

    # Predefined list of interesting voices
    interesting_voices = [
        "en-US-Standard-A", "en-US-Standard-B", "en-US-Standard-C", "en-US-Standard-D",
        "en-US-Standard-E", "en-US-Standard-F", "en-US-Standard-G", "en-US-Standard-H",
        "en-US-Standard-I", "en-US-Standard-J", "en-US-Neural2-A", "en-US-Neural2-C",
        "en-US-Neural2-D", "en-US-Neural2-E", "en-US-Neural2-F", "en-US-Neural2-G",
        "en-US-Neural2-H", "en-US-Neural2-I", "en-US-Neural2-J", "en-US-News-K",
        "en-US-News-L", "en-US-News-M", "en-US-News-N", "en-US-Studio-M", "en-US-Studio-O",
        "en-US-Wavenet-A", "en-US-Wavenet-B", "en-US-Wavenet-C", "en-US-Wavenet-D",
        "en-US-Wavenet-E", "en-US-Wavenet-F", "en-US-Wavenet-G", "en-US-Wavenet-H",
        "en-US-Wavenet-I", "en-US-Wavenet-J"
    ]

    voice_menu = OptionMenu(root, voice_var, *interesting_voices)
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
