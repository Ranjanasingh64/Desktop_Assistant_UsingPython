import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


## Taking voice from mine system
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[1].id)
#print(type(voices))
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

## speak function
def speak(text):
    """This function takes text and returns voice
    Args: 
        text (_type_):string

    """
    
    engine.say(text)
    engine.runAndWait()

# speak("my name is vrishti and my sis is vritika")

## Speech recognition function
def takeCommand():
    """This function recognise voice and return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 
        audio = r.listen(source)

    #command = r.recognize_google(audio)
    #print(command)


        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language= "en-in")
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please......")
            return "None"
        return query
text = takeCommand()
speak(text)
print("test")

