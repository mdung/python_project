import tkinter as tk
from tkinter import filedialog
from googletrans import Translator

def translate_text(input_text, target_language):
    translator = Translator()
    translation = translator.translate(input_text, dest=target_language)
    return translation.text

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    entry_var.set(file_path)

def translate_and_save():
    input_path = entry_var.get()

    if not input_path:
        # Provide an error message or handle the case when no file is selected
        return

    with open(input_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    target_language = "vi"
    translated_text = translate_text(input_text, target_language)

    output_path = "translation_" + generate_meaningful_name() + ".txt"

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    # You can add a success message or open the output file, etc.

def generate_meaningful_name():
    # Implement a logic to generate a meaningful name for the output file
    # For simplicity, let's use a placeholder name
    return "translation_name"

# GUI setup
app = tk.Tk()
app.title("Text Translator")

# Entry for file path
entry_var = tk.StringVar()
entry = tk.Entry(app, textvariable=entry_var, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Browse button
browse_button = tk.Button(app, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Translate button
translate_button = tk.Button(app, text="Translate and Save", command=translate_and_save)
translate_button.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()
