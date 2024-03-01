import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c")  # Get text from the Text widget
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            result_label.config(text="Positive Sentiment", foreground="green")
        elif sentiment < 0:
            result_label.config(text="Negative Sentiment", foreground="red")
        else:
            result_label.config(text="Neutral Sentiment", foreground="blue")
    else:
        result_label.config(text="Please enter some text", foreground="black")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Create and configure the Text widget for user input
text_entry = tk.Text(root, wrap="word", width=40, height=10)
text_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Create and configure the Analyze button
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

# Create and configure the result label
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

# Run the main loop
root.mainloop()
