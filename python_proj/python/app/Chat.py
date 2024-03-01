import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import socket

class ChatApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Application")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.server_address = "localhost"
        self.server_port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, self.server_port))

        self.receive_thread = Thread(target=self.receive_messages, daemon=True)
        self.receive_thread.start()

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode("utf-8"))
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    self.chat_history.insert(tk.END, f"{message}\n")
                    self.chat_history.see(tk.END)
            except ConnectionAbortedError:
                break

if __name__ == "__main__":
    root = tk.Tk()
    chat_app = ChatApplication(root)
    root.mainloop()
