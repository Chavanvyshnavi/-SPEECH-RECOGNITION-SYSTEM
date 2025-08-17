# ------------------------------
# Simple Speech-to-Text Program
# Task: Record short audio and transcribe it into text
# Libraries used: sounddevice, scipy, speechrecognition
# ------------------------------

import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr

# Step 1: Record audio
def record_audio(filename="my_recording.wav", duration=5, fs=44100):
    print("🎤 Recording... Please speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wav.write(filename, fs, recording)
    print(f"✅ Recording saved as {filename}")

# Step 2: Transcribe audio to text
def transcribe_audio(filename="my_recording.wav"):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            print("🔎 Recognizing speech...")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print("📝 Recognized text:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand the audio.")
    except sr.RequestError:
        print("⚠️ Could not connect to the speech recognition service.")

# Step 3: Run everything together
if __name__ == "__main__":
    record_audio()          # Record for 5 seconds
    transcribe_audio()      # Convert to text
