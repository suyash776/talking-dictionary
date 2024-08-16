#helper.property
#helper for the main function
from os import system
import re
import speech_recognition as rec
import platform

if platform.system() =='Windows':
    import pyttsx3

def announce(speak):
    formatted=re.sub(r'[^\w]', ' ', speak)
    print(formatted)
    if platform.system() =='Windows':
        engine = pyttsx3.init()
        engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.say(formatted)
        engine.runAndWait()
    else:
        system('say '+ formatted)

def recognize (audio):
    print("Recognizing audio...")
    recognizer= rec.Recognizer()
    return recognizer.recognize_google(audio)

def listen():
    recognizer = rec.Recognizer()
    with rec.Microphone() as source:
        print("Say something!")
        print("Listening...")
        return recognizer.listen(source)
