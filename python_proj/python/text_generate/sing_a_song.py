from gtts import gTTS
from pydub import AudioSegment
from pydub.generators import Sine

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_file)

def combine_audio(original_audio_file, vocal_audio_file, output_file):
    original_audio = AudioSegment.from_mp3(original_audio_file)
    vocal_audio = AudioSegment.from_mp3(vocal_audio_file)

    # Ensure both audio files have the same duration
    if len(original_audio) > len(vocal_audio):
        original_audio = original_audio[:len(vocal_audio)]
    else:
        vocal_audio = vocal_audio[:len(original_audio)]

    combined_audio = original_audio.overlay(vocal_audio)

    combined_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    # Replace the following with your song lyrics
    song_lyrics = "This is the song lyrics. You can replace it with your own lyrics."

    # Convert text to speech
    text_to_speech(song_lyrics, "vocal.mp3")

    # Replace 'original_song.mp3' with the path to your instrumental song
    combine_audio("original_song.mp3", "vocal.mp3", "output_song.mp3")
