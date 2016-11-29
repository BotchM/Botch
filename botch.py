import speech_recognition as sr
import sys
import os
from os import path

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    user = r.recognize_sphinx(audio)
    print(user)
    if user == "excel":
        excel()
    elif user == "internet":
        os.system("start chrome.exe")
    elif user == "music":
        media()
    print("Sphinx thinks you said " + user)

        
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
