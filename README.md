# -SPEECH-RECOGNITION-SYSTEM
company name: codtech IT solutions

Name: C.vyshnavi

Intern id: CT04DY411

Domain: Artificial Intelligence

Duration:4weeks

mentor:Neela Santosh 

description:The task was to build a basic speech recognition system that can record a short audio clip and convert it into text. To achieve this, we used pre-trained models available in libraries such as speechrecognition and supporting tools like sounddevice and scipy.

Audio Recording:
We first used the sounddevice library to capture sound from the computer’s microphone. The program records a few seconds of audio (in our case, 5 seconds) and saves it as a .wav file using the scipy.io.wavfile module. This makes it easy to store and reuse the recording.

Speech-to-Text Conversion:
After recording, the saved .wav file is passed into the speechrecognition library. This library uses pre-trained speech models and Google’s Speech Recognition API to process the audio and convert spoken words into written text.

Error Handling:
Since speech recognition may not always be perfect, the program also includes error handling. For example, if the speech is not clear, it will notify the user that it could not understand the audio, or if there is a connection problem, it will show a warning message.

Output:
Once processed, the recognized text is displayed on the screen. This completes the cycle of recording → saving → transcribing → displaying results.

Outcome

The final system is a functional speech-to-text application. It is beginner-friendly, easy to run, and demonstrates the basic workflow of how modern speech recognition works. By combining recording, saving, and transcribing, this task fulfills the requirement of building a simple yet effective Speech Recognition System.
