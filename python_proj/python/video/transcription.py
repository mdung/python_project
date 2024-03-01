import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import speech_recognition as sr
import simpleaudio

class AudioTranscriber:
    def __init__(self, master):
        self.master = master
        master.title("Audio Transcriber")

        self.transcription_text = tk.Text(master, height=10, width=50)
        self.transcription_text.pack()

        self.browse_button = tk.Button(master, text="Browse Audio File", command=self.browse_file)
        self.browse_button.pack()

        self.play_button = tk.Button(master, text="Play Audio", command=self.play_audio)
        self.play_button.pack()

        self.export_button = tk.Button(master, text="Export Subtitles", command=self.export_subtitles)
        self.export_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.transcribe_audio(file_path)

    def play_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            audio = AudioSegment.from_mp3(file_path)

            # Convert audio to WAV (simpleaudio supports WAV)
            wav_audio = audio.export(format="wav").read()

            # Play the audio using simpleaudio
            play_obj = simpleaudio.play_buffer(wav_audio, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

            # Wait until audio is finished playing
            play_obj.wait_done()

    def transcribe_audio(self, file_path):
        audio = AudioSegment.from_mp3(file_path)
        recognizer = sr.Recognizer()

        text_segments = []

        for i, chunk in enumerate(audio[::5000]):  # Process audio in 5-second chunks
            audio_chunk = sr.AudioData(chunk.raw_data, sample_width=chunk.sample_width, frame_rate=chunk.frame_rate,
                                       num_channels=chunk.channels)
            try:
                text = recognizer.recognize_google(audio_chunk)
                start_time = i * 5
                end_time = min((i + 1) * 5, len(audio) / 1000)
                text_segments.append((start_time, end_time, text))
            except sr.UnknownValueError:
                pass  # Ignore unrecognized audio chunks

        self.display_transcription(text_segments)

    def display_transcription(self, text_segments):
        self.transcription_text.delete(1.0, tk.END)
        for i, (start_time, end_time, text) in enumerate(text_segments, start=1):
            subtitle = f"{i}\n{self.format_time(start_time)} --> {self.format_time(end_time)}\n{text}\n\n"
            self.transcription_text.insert(tk.END, subtitle)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},000"

    def export_subtitles(self):
        subtitles = self.transcription_text.get(1.0, tk.END)
        save_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
        if save_path:
            with open(save_path, "w") as file:
                file.write(subtitles)

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriber(root)
    root.mainloop()
