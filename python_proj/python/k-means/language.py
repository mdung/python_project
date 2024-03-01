import tkinter as tk
from tkinter import Scrollbar, Text, END
import openai  # Make sure to install the OpenAI library by running: pip install openai

# Set your OpenAI API key
openai.api_key = "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"

class LanguageModelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Model App")

        # Create UI elements
        self.text_input = Text(root, wrap="word", width=40, height=10)
        self.scrollbar = Scrollbar(root, command=self.text_input.yview)
        self.text_input.config(yscrollcommand=self.scrollbar.set)

        self.response_display = Text(root, wrap="word", state=tk.DISABLED, width=40, height=10)

        self.generate_button = tk.Button(root, text="Generate Response", command=self.generate_response)

        # Pack UI elements
        self.text_input.pack(padx=10, pady=10)
        self.scrollbar.pack(side="right", fill="y")
        self.response_display.pack(padx=10, pady=10)
        self.generate_button.pack(pady=10)

    def generate_response(self):
        input_text = self.text_input.get("1.0", END).strip()

        if not input_text:
            return

        # Call the OpenAI API for response generation
        response = self.call_openai_api(input_text)

        # Display the response
        self.display_response(response)

    def call_openai_api(self, input_text):
        # You can replace this with your own language model or API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            temperature=0.7,
            max_tokens=150
        )

        return response.choices[0].text.strip()

    def display_response(self, response):
        self.response_display.config(state=tk.NORMAL)
        self.response_display.delete("1.0", END)
        self.response_display.insert(END, response)
        self.response_display.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageModelApp(root)
    root.mainloop()
