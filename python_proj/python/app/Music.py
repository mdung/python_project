import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create and configure the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create and configure the listbox
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(expand=True, fill=tk.BOTH)
        self.listbox.bind('<Double-Button-1>', self.play_selected)

        # Create and configure buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        button_add = tk.Button(frame_buttons, text="Add Song", command=self.add_song)
        button_add.grid(row=0, column=0, padx=5)

        button_play = tk.Button(frame_buttons, text="Play", command=self.play_selected)
        button_play.grid(row=0, column=1, padx=5)

        button_stop = tk.Button(frame_buttons, text="Stop", command=self.stop_song)
        button_stop.grid(row=0, column=2, padx=5)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if song_path:
            song_name = os.path.basename(song_path)
            self.listbox.insert(tk.END, song_name)
            self.listbox.activate(tk.END)  # Automatically select the last added song
            pygame.mixer.music.load(song_path)

    def play_selected(self, event=None):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_song = self.listbox.get(selected_index)
            song_path = os.path.join(os.getcwd(), selected_song)
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.run()
