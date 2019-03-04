import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('aamir.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio))