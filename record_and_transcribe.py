


import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

# Step 1: Record Audio
def record_audio(filename="my_recording.wav", duration=5, samplerate=44100):
    print("Recording... Speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(filename, samplerate, recording)  # Save as WAV file
    print("Recording saved as {}".format(filename))

# Step 2: Transcribe Audio
def transcribe_audio(filename="my_recording.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print("Recognizing speech...")
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription:", text)
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results; {}".format(e))

# Run everything
if __name__ == "__main__":
    record_audio()  # Record 5 seconds by default
    transcribe_audio()
