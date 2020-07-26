
import os
import time
import playsound
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
os.chdir(r'F:\Projects\Voice Assistant\VoiceFiles')


def Speak(text):
    tts = gTTS(text=text,lang='en' )
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception occured ",e)
            
            
    return said
            
text =  get_audio()   
if "what is your name" in text:
    Speak('My name is Clash Princess')
if "what do you do" in text:
    Speak('i play clash of clans')

