import pyaudio
import speech_recognition as sr

print("PyAudio Version:", pyaudio.__version__)
print("SpeechRecognition Version:", sr.__version__)
r=sr.Recognizer()
print("Librarile au fost importate cu succes.")