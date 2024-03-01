import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, TextClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout
from moviepy.video.fx.all import resize
import os

# Placeholder class for Entry widget
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.put_placeholder()

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

def generate_video(avatar_path, text_to_say, output_filename):
    avatar = VideoFileClip(avatar_path)

    txt_clip = TextClip(text_to_say, fontsize=24, color='white', bg_color='black', size=(avatar.size[0], avatar.size[1] // 4))

    video = CompositeVideoClip([avatar, txt_clip.set_position(('center', 'bottom')).set_duration(avatar.duration)])

    audio = avatar.audio
    audio = audio_fadein(audio, 1).fx(audio_fadeout, 1)

    video = video.set_audio(audio)

    video = resize(video, height=360)

    video.write_videofile(output_filename, codec='libx264', audio_codec='aac')

class AvatarVideoGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Avatar Video Generator")

        self.avatar_path = None

        # Create GUI components
        self.label_avatar = tk.Label(root, text="Select Avatar Image:")
        self.label_avatar.pack()

        self.btn_browse = tk.Button(root, text="Browse", command=self.browse_avatar)
        self.btn_browse.pack()

        # Improve label_text with more context
        self.label_text = tk.Label(root, text="Enter the text you want the avatar to say:")
        self.label_text.pack()

        # Use the EntryWithPlaceholder class for the entry field
        self.entry_text = EntryWithPlaceholder(root, placeholder="Hello, world!")
        self.entry_text.pack()

        self.btn_generate = tk.Button(root, text="Generate Video", command=self.generate_video)
        self.btn_generate.pack()

    def browse_avatar(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.avatar_path = file_path

    def generate_video(self):
        if not self.avatar_path:
            messagebox.showerror("Error", "Please select an avatar image.")
            return

        text_to_say = self.entry_text.get()
        if not text_to_say:
            messagebox.showerror("Error", "Please enter text to say.")
            return

        output_filename = self.get_output_filename()

        generate_video(self.avatar_path, text_to_say, output_filename)
        messagebox.showinfo("Success", f"Video created and saved as {output_filename}")

    def get_output_filename(self):
        if self.avatar_path:
            avatar_name = os.path.splitext(os.path.basename(self.avatar_path))[0]
            return f"{avatar_name}_output.mp4"
        return "output.mp4"

if __name__ == "__main__":
    root = tk.Tk()
    app = AvatarVideoGenerator(root)
    root.mainloop()
