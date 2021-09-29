import speech_recognition as sr 
from gtts import gTTS
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.say("Yes boss")
engine.say("How can I help?")
engine.runAndWait()
try: 
    with sr.Microphone() as source: 
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'mode' in command:
            print(command)
except: 
    pass