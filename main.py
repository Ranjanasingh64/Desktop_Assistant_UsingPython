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
    



    
#text = takeCommand()
#speak(text)
#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir. How are you doing")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. How are you doing")

    else:
        speak("Good Evening Sir. How are you doing")   

    speak ("I am JARVIS. Tell me sir how can I help you")     



## after writing below statement the python will start reading from this line only

if __name__ == "__main__":
    wish_me()
    
    while True:

        query = takeCommand().lower()
        #print(query)

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        
        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")        


        elif "github" in query:
            speak("Opening Github")
            webbrowser.open("github.com")  

    
    ## This quey is for say the time
        elif "time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        
        elif "goodbye" in query:
        #elif "Goodbye" in query:
            speak("OK Sir. I am always here for you. Bye Bye")
            exit()




    

    